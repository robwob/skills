#!/usr/bin/env python3
"""Analyse open and hybrid card sort results.

Input: a CSV with one row per card placement:

    participant_id,card,category[,order]

A blank category means the participant left that card unsorted.

What it computes, in order:
  1. data checks per participant
  2. cards view: where each card was placed, with a confidence interval
  3. categories view: standardised categories and their agreement
  4. similarity matrix: share of participants who grouped each pair together
  5. hierarchical clustering (average linkage by default) and a dendrogram
  6. how the structure moves under other cut points and another linkage
  7. bootstrap stability of the clusters
  8. cards that no single group settles ("contested" cards)

Every setting that changes the answer is printed and saved with the results.
Requires numpy and scipy.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import json
import math
import os
import sys
from collections import Counter

try:
    import numpy as np
    from scipy.cluster.hierarchy import (cophenet, fcluster, leaves_list,
                                         linkage, to_tree)
    from scipy.spatial.distance import squareform
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        "This script needs numpy and scipy. Install them with:\n"
        "  python3 -m pip install numpy scipy\n(%s)\n" % exc
    )
    sys.exit(2)

# Defaults below are conventions of this script, not evidence-based
# thresholds. They are printed next to every result they affect.
DEFAULT_CUT = 0.5            # similarity at which the dendrogram is cut
CUT_SWEEP = (0.3, 0.4, 0.5, 0.6, 0.7)
CONTESTED_MARGIN = 0.15      # card is this close to a second group
STABILITY_STABLE = 0.75      # mean Jaccard bands follow the clusterboot
STABILITY_DOUBTFUL = 0.60    # documentation (a general-purpose guide)
MIN_BOOTSTRAP_PARTICIPANTS = 10
VAGUE_NAMES = {
    "stuff", "misc", "miscellaneous", "other", "others", "random", "things",
    "general", "n/a", "na", "unsure", "dont know", "don't know", "idk",
}
UNSORTED_LOOKALIKES = {"unsorted", "(unsorted)", "unsorted cards", "not sorted"}


class InputError(Exception):
    """A problem with the user's data or options, reported without a trace."""


def norm(text):
    """Case and whitespace normalisation used to recognise the same label."""
    return " ".join(text.split()).casefold()


def pct(x):
    """Whole-number percentage, rounding halves up (not to even)."""
    return int(math.floor(x * 100 + 0.5))


def wilson(k, n, z=1.96):
    """95% Wilson score interval for k successes out of n."""
    if n == 0:
        return float("nan"), float("nan")
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


# ---------------------------------------------------------------- loading

def read_placements(path, cols):
    try:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            headers = reader.fieldnames or []
            needed = (cols["participant"], cols["card"], cols["category"])
            missing = [c for c in needed if c not in headers]
            if missing:
                raise InputError(
                    "Column(s) not found: %s. Columns in the file: %s. Use "
                    "--col-participant, --col-card and --col-category to map "
                    "them." % (", ".join(missing), ", ".join(headers))
                )
            preset_col = cols.get("preset")
            has_preset = preset_col in headers
            rows = []
            for line_no, row in enumerate(reader, start=2):
                p = (row.get(cols["participant"]) or "").strip()
                card = " ".join((row.get(cols["card"]) or "").split())
                cat = " ".join((row.get(cols["category"]) or "").split())
                if not (p or card or cat):
                    continue
                if not p or not card:
                    raise InputError(
                        "Line %d: participant and card must both be filled "
                        "in." % line_no
                    )
                preset = None
                if has_preset:
                    preset = (row.get(preset_col) or "").strip().casefold() \
                        in ("1", "true", "yes", "y", "preset")
                rows.append((p, card, cat, preset))
    except FileNotFoundError:
        raise InputError("File not found: %s" % path)
    except UnicodeDecodeError:
        raise InputError(
            "Could not read %s as UTF-8. Re-save it as CSV UTF-8." % path
        )
    if not rows:
        raise InputError("No data rows found in %s." % path)
    return rows


def read_merge_file(path):
    """Map raw category names to standardised names (columns raw, standard)."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            headers = reader.fieldnames or []
            if "raw" not in headers or "standard" not in headers:
                raise InputError(
                    "The merge file needs the columns 'raw' and 'standard'. "
                    "Found: %s." % ", ".join(headers)
                )
            mapping = {}
            for row in reader:
                raw = " ".join((row.get("raw") or "").split())
                std = " ".join((row.get("standard") or "").split())
                if raw and std:
                    mapping[norm(raw)] = std
    except FileNotFoundError:
        raise InputError("Merge file not found: %s" % path)
    return mapping


def read_card_list(path):
    try:
        with open(path, encoding="utf-8-sig") as fh:
            return [" ".join(line.split()) for line in fh if line.strip()]
    except FileNotFoundError:
        raise InputError("Card list not found: %s" % path)


class Study:
    """Placements arranged as arrays.

    group_labels[p, i]  the participant's own group for card i (-1 unsorted).
                        Groups are identified by normalised name within a
                        participant. The similarity matrix uses these, so it
                        does not depend on how categories are standardised.
    std_labels[p, i]    the standardised category id for card i (-1 unsorted).
                        Used only by the cards and categories views.
    """

    def __init__(self, rows, merge_map, card_list, exclude, unsorted_labels):
        excluded = set(exclude)
        known_ids = {r[0] for r in rows}
        self.has_preset = any(r[3] is not None for r in rows)
        preset_raw = set()
        unknown = sorted(excluded - known_ids)
        if unknown:
            raise InputError(
                "--exclude names participants not in the data: %s"
                % ", ".join(unknown)
            )
        lookalike_hits = Counter()
        participants = []
        per_p = {}
        for p, card, cat, is_preset in rows:
            if p in excluded:
                continue
            if p not in per_p:
                per_p[p] = {}
                participants.append(p)
            if card in per_p[p]:
                raise InputError(
                    "Participant %s has the card '%s' more than once. Each "
                    "participant must place each card once." % (p, card)
                )
            key = norm(cat)
            if key and key in unsorted_labels:
                cat = ""
            elif key in UNSORTED_LOOKALIKES:
                lookalike_hits[cat] += 1
            per_p[p][card] = cat
            if is_preset and cat:
                preset_raw.add(norm(cat))
        if not participants:
            raise InputError("No participants left after exclusions.")

        seen_cards = []
        for p in participants:
            for card in per_p[p]:
                if card not in seen_cards:
                    seen_cards.append(card)
        if card_list:
            stray = [c for c in seen_cards if c not in set(card_list)]
            if stray:
                raise InputError(
                    "Cards in the data but not in the card list: %s"
                    % "; ".join(stray)
                )
            cards = list(card_list)
        else:
            cards = seen_cards
        if len(cards) < 2:
            raise InputError("At least two cards are needed.")

        self.cards = cards
        self.participants = participants
        self.excluded = sorted(excluded)
        self.lookalikes = dict(lookalike_hits)
        self.missing_cells = 0
        P, n = len(participants), len(cards)
        card_index = {c: i for i, c in enumerate(cards)}

        # raw forms per normalised key, to choose a display label
        forms = {}
        for p in participants:
            for cat in per_p[p].values():
                if cat:
                    forms.setdefault(norm(cat), Counter())[cat] += 1

        def std_key(raw):
            key = norm(raw)
            return norm(merge_map[key]) if key in merge_map else key

        self.merge_used = bool(merge_map)
        self.unused_merge = sorted(k for k in merge_map if k not in forms)
        std_display = {}
        for key, counter in forms.items():
            if key in merge_map:
                std_display.setdefault(norm(merge_map[key]), merge_map[key])
            else:
                std_display.setdefault(key, counter.most_common(1)[0][0])
        self.std_names = sorted(std_display.values(), key=str.casefold)
        std_id = {
            k: self.std_names.index(v) for k, v in std_display.items()
        }
        self.preset_ids = {
            std_id[std_key(k)] for k in preset_raw if k in forms
        }

        self.group_labels = -np.ones((P, n), dtype=int)
        self.std_labels = -np.ones((P, n), dtype=int)
        self.group_names = []  # per participant: list of group display names
        for pi, p in enumerate(participants):
            local = {}
            names = []
            for card, cat in per_p[p].items():
                if not cat:
                    continue
                key = norm(cat)
                if key not in local:
                    local[key] = len(local)
                    names.append(cat)
                self.group_labels[pi, card_index[card]] = local[key]
                self.std_labels[pi, card_index[card]] = std_id[std_key(cat)]
            self.group_names.append(names)
            self.missing_cells += sum(1 for c in cards if c not in per_p[p])

    @property
    def P(self):
        return len(self.participants)

    @property
    def n(self):
        return len(self.cards)


# ---------------------------------------------------------- core arithmetic

def pair_arrays(group_labels):
    """Per participant: together[p,i,j] and both_sorted[p,i,j] as 0/1."""
    sorted_ = group_labels >= 0
    same = group_labels[:, :, None] == group_labels[:, None, :]
    both = sorted_[:, :, None] & sorted_[:, None, :]
    return (same & both).astype(np.uint8), both.astype(np.uint8)


def similarity(together_sum, both_sum, n_participants, mode):
    if mode == "singleton":
        S = together_sum / float(n_participants)
        empty = 0
    else:
        S = np.zeros(together_sum.shape, dtype=float)
        np.divide(together_sum, both_sum, out=S, where=both_sum > 0)
        off_diag = ~np.eye(S.shape[0], dtype=bool)
        empty = int(((both_sum == 0) & off_diag).sum()) // 2
    S = S.astype(float)
    np.fill_diagonal(S, 1.0)
    return S, empty


def condensed_distance(S):
    D = 1.0 - S
    D = (D + D.T) / 2.0
    np.fill_diagonal(D, 0.0)
    D[D < 0] = 0.0
    return squareform(D, checks=False)


def cluster(S, method):
    return linkage(condensed_distance(S), method=method)


def cut_labels(Z, cut_similarity):
    return fcluster(Z, t=(1.0 - cut_similarity) + 1e-9, criterion="distance")


def pair_agreement(a, b):
    """Share of card pairs treated the same way (together/apart) by both."""
    iu = np.triu_indices(len(a), k=1)
    same_a = (a[:, None] == a[None, :])[iu]
    same_b = (b[:, None] == b[None, :])[iu]
    return float((same_a == same_b).mean())


def groups_from_labels(labels, cards):
    groups = {}
    for i, lab in enumerate(labels):
        groups.setdefault(int(lab), []).append(cards[i])
    return sorted(groups.values(), key=lambda g: (-len(g), g[0]))


# ----------------------------------------------------------------- views

def participant_checks(study, together, both):
    P = study.P
    rows = []
    group_counts = []
    for pi in range(P):
        g = study.group_labels[pi]
        sorted_mask = g >= 0
        group_counts.append(len(set(g[sorted_mask].tolist())))
    median_groups = float(np.median(group_counts))
    sum_t = together.sum(axis=0, dtype=np.int64)
    sum_b = both.sum(axis=0, dtype=np.int64)
    iu = np.triu_indices(study.n, k=1)
    for pi, p in enumerate(study.participants):
        g = study.group_labels[pi]
        n_sorted = int((g >= 0).sum())
        n_groups = group_counts[pi]
        flags = []
        if n_sorted > 1 and n_groups == 1:
            flags.append("everything in one group")
        if n_sorted > 1 and n_groups == n_sorted:
            flags.append("every card in its own group")
        elif median_groups > 0 and n_groups > 2 * median_groups:
            flags.append("many more groups than typical")
        if n_sorted < study.n:
            flags.append("%d card(s) unsorted" % (study.n - n_sorted))
        if any(norm(name) in VAGUE_NAMES for name in study.group_names[pi]):
            flags.append("vague group name")
        t_p = together[pi].astype(float)
        b_p = both[pi].astype(float)
        loo_den = sum_b - both[pi]
        loo = np.zeros(sum_t.shape, dtype=float)
        np.divide(sum_t - together[pi], loo_den, out=loo, where=loo_den > 0)
        mask = b_p[iu] > 0
        align = float("nan")
        if mask.sum() > 2 and study.P > 2:
            x, y = t_p[iu][mask], loo[iu][mask]
            if x.std() > 0 and y.std() > 0:
                align = float(np.corrcoef(x, y)[0, 1])
        rows.append({
            "participant": p, "groups": n_groups, "sorted": n_sorted,
            "unsorted": study.n - n_sorted, "alignment": align,
            "flags": "; ".join(flags),
        })
    return rows, median_groups


def cards_view(study):
    rows = []
    for i, card in enumerate(study.cards):
        col = study.std_labels[:, i]
        sorted_by = int((col >= 0).sum())
        counts = Counter(col[col >= 0].tolist())
        ordered = counts.most_common()
        top_id, top_n = ordered[0] if ordered else (-1, 0)
        lo, hi = wilson(top_n, sorted_by)
        rows.append({
            "card": card,
            "sorted_by": sorted_by,
            "categories": len(counts),
            "top_category": study.std_names[top_id] if top_id >= 0 else "",
            "top_count": top_n,
            "top_share": top_n / sorted_by if sorted_by else float("nan"),
            "ci_low": lo, "ci_high": hi,
            "all_categories": "; ".join(
                "%s: %d" % (study.std_names[k], v) for k, v in ordered
            ),
        })
    return rows


def categories_view(study):
    rows = []
    for cid, name in enumerate(study.std_names):
        used = (study.std_labels == cid)
        contributors = int(used.any(axis=1).sum())
        card_counts = used.sum(axis=0)
        in_cat = [i for i in range(study.n) if card_counts[i] > 0]
        m = len(in_cat)
        agreement = (
            float(sum(card_counts[i] for i in in_cat)) / (m * contributors)
            if m and contributors else float("nan")
        )
        rows.append({
            "category": name,
            "origin": ("" if not study.has_preset else
                       "preset" if cid in study.preset_ids
                       else "participant"),
            "participants": contributors,
            "unique_cards": m,
            "agreement": agreement,
            "cards": "; ".join(
                "%s (%d)" % (study.cards[i], card_counts[i])
                for i in sorted(in_cat, key=lambda i: -card_counts[i])
            ),
        })
    rows.sort(key=lambda r: (-r["participants"], r["category"].casefold()))
    return rows


def nested_tree(Z, cards):
    root = to_tree(Z)
    lines = []

    def walk(node, depth):
        pad = "  " * depth
        if node.is_leaf():
            lines.append(pad + cards[node.id])
        else:
            lines.append("%sJoined at %d%% similarity (%d cards)"
                         % (pad, pct(1 - node.dist), node.count))
            walk(node.get_left(), depth + 1)
            walk(node.get_right(), depth + 1)

    walk(root, 0)
    return lines


def merge_table(Z, cards):
    members = {i: [cards[i]] for i in range(len(cards))}
    rows = []
    for step, (a, b, dist, size) in enumerate(Z, start=1):
        a, b = int(a), int(b)
        left, right = members[a], members[b]
        members[len(cards) + step - 1] = left + right
        rows.append({
            "step": step,
            "left": " | ".join(left), "right": " | ".join(right),
            "similarity": 1 - float(dist), "size": int(size),
        })
    return rows


def contested_cards(S, labels, cards, retention, cut):
    rows = []
    clusters = {}
    for i, lab in enumerate(labels):
        clusters.setdefault(int(lab), []).append(i)
    for i, lab in enumerate(labels):
        mates = [j for j in clusters[int(lab)] if j != i]
        cohesion = float(S[i, mates].mean()) if mates else 0.0
        best_other, best_name = 0.0, ""
        for other, members in clusters.items():
            if other == int(lab):
                continue
            avg = float(S[i, members].mean())
            if avg > best_other:
                best_other, best_name = avg, cards[members[0]]
        margin = cohesion - best_other
        reasons = []
        if not mates:
            reasons.append("does not join any group at this cut")
        elif cohesion < cut:
            reasons.append("low similarity to its own group")
        if mates and margin < CONTESTED_MARGIN:
            reasons.append("nearly as similar to another group")
        if retention is not None and mates and retention[i] < STABILITY_DOUBTFUL:
            reasons.append("often moves group when participants are resampled")
        rows.append({
            "card": cards[i], "cohesion": cohesion,
            "best_other": best_other, "margin": margin,
            "retention": float(retention[i]) if retention is not None
            and mates else float("nan"),
            "reasons": "; ".join(reasons),
            "group_mates": ", ".join(cards[j] for j in mates),
        })
    return rows


def bootstrap(together, both, mode, method, cut, labels, B, seed):
    """Resample participants with replacement and re-cluster each time."""
    rng = np.random.default_rng(seed)
    P = together.shape[0]
    n = together.shape[1]
    co = np.zeros((n, n), dtype=float)
    original = {}
    for i, lab in enumerate(labels):
        original.setdefault(int(lab), set()).add(i)
    jaccards = {lab: [] for lab, m in original.items() if len(m) > 1}
    for _ in range(B):
        idx = rng.integers(0, P, size=P)
        t = together[idx].sum(axis=0, dtype=np.int64)
        b = both[idx].sum(axis=0, dtype=np.int64)
        S_b, _ = similarity(t, b, P, mode)
        lab_b = cut_labels(cluster(S_b, method), cut)
        co += (lab_b[:, None] == lab_b[None, :])
        boot_sets = {}
        for i, lab in enumerate(lab_b):
            boot_sets.setdefault(int(lab), set()).add(i)
        for lab, members in original.items():
            if lab not in jaccards:
                continue
            jaccards[lab].append(max(
                len(members & s) / len(members | s)
                for s in boot_sets.values()
            ))
    co /= B
    retention = np.zeros(n)
    for lab, members in original.items():
        for i in members:
            mates = [j for j in members if j != i]
            retention[i] = co[i, mates].mean() if mates else 1.0
    return {lab: float(np.mean(v)) for lab, v in jaccards.items()}, retention


def stability_band(j):
    if j >= STABILITY_STABLE:
        return "stable"
    if j >= STABILITY_DOUBTFUL:
        return "doubtful"
    return "unstable"


# --------------------------------------------------------------- explain

def resolve_card(study, name):
    lookup = {c.casefold(): i for i, c in enumerate(study.cards)}
    if " ".join(name.split()).casefold() in lookup:
        return lookup[" ".join(name.split()).casefold()]
    close = difflib.get_close_matches(name, study.cards, n=3, cutoff=0.5)
    hint = " Did you mean: %s?" % "; ".join(close) if close else ""
    raise InputError("Card not found: '%s'.%s" % (name, hint))


def explain_pair(study, together, both, a_name, b_name, mode):
    a, b = resolve_card(study, a_name), resolve_card(study, b_name)
    lines = ["Pair: '%s' and '%s'" % (study.cards[a], study.cards[b]), ""]
    lines.append("%-12s %-26s %-26s %s" % (
        "Participant", study.cards[a][:26], study.cards[b][:26], "Together?"))
    t_total = b_total = 0
    for pi, p in enumerate(study.participants):
        def where(i):
            g = int(study.group_labels[pi, i])
            return "(unsorted)" if g < 0 else study.group_names[pi][g]
        t = int(together[pi, a, b])
        bs = int(both[pi, a, b])
        t_total += t
        b_total += bs
        lines.append("%-12s %-26s %-26s %s" % (
            p, where(a)[:26], where(b)[:26], "yes" if t else "no"))
    lines.append("")
    lines.append("Grouped together by %d of %d participants." % (
        t_total, study.P))
    lines.append("  singleton mode:  %d / %d = %d%%" % (
        t_total, study.P, pct(t_total / study.P)))
    if b_total:
        lines.append("  pairwise mode:   %d / %d = %d%%  (%d participants "
                     "sorted both cards)" % (
                         t_total, b_total, pct(t_total / b_total), b_total))
    lines.append("Setting in use: %s." % mode)
    return "\n".join(lines)


# ----------------------------------------------------------------- output

def table(headers, rows):
    widths = [len(h) for h in headers]
    text_rows = [[str(c) for c in r] for r in rows]
    for r in text_rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(c))
    out = ["  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))]
    out.append("  ".join("-" * w for w in widths))
    for r in text_rows:
        out.append("  ".join(c.ljust(widths[i]) for i, c in enumerate(r)))
    return out


def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(headers)
        w.writerows(rows)


def fmt(x, digits=0):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return ("%." + str(digits) + "f") % x


CLOSED_MIN_SHARE = 0.5  # script default, not an evidence-based threshold


def closed_cards_view(study):
    """Per card: placement counts across the preset categories."""
    K = len(study.std_names)
    rows = []
    for i, card in enumerate(study.cards):
        col = study.std_labels[:, i]
        sorted_by = int((col >= 0).sum())
        counts = np.bincount(col[col >= 0], minlength=K)
        order = sorted(range(K), key=lambda k: (-counts[k],
                                                study.std_names[k].casefold()))
        top = order[0]
        second = order[1] if K > 1 else None
        top_n = int(counts[top])
        sec_n = int(counts[second]) if second is not None else 0
        lo, hi = wilson(top_n, sorted_by)
        lo2, hi2 = wilson(sec_n, sorted_by)
        rows.append({
            "card": card, "sorted_by": sorted_by,
            "top_category": study.std_names[top] if sorted_by else "",
            "top_count": top_n,
            "top_share": top_n / sorted_by if sorted_by else float("nan"),
            "ci_low": lo, "ci_high": hi,
            "second_category": (study.std_names[second]
                                if second is not None and sec_n else ""),
            "second_share": sec_n / sorted_by if sorted_by else 0.0,
            "second_ci_low": lo2, "second_ci_high": hi2,
            "counts": [int(c) for c in counts],
        })
    return rows


def bootstrap_top(study, B, seed):
    """Share of resamples in which each card keeps its top category."""
    P, n, K = study.P, study.n, len(study.std_names)
    onehot = np.zeros((P, n, K), dtype=np.int32)
    for p in range(P):
        for i in range(n):
            k = study.std_labels[p, i]
            if k >= 0:
                onehot[p, i, k] = 1
    original = onehot.sum(axis=0).argmax(axis=1)
    rng = np.random.default_rng(seed)
    held = np.zeros(n)
    for _ in range(B):
        idx = rng.integers(0, P, size=P)
        held += (onehot[idx].sum(axis=0).argmax(axis=1) == original)
    return held / B


def run_closed(study, args, together, both):
    checks, median_groups = participant_checks(study, together, both)
    cards_rows = closed_cards_view(study)
    held = None
    boot_note = ""
    if args.bootstrap > 0:
        if study.P < MIN_BOOTSTRAP_PARTICIPANTS:
            boot_note = ("Only %d participants: resampling this few gives "
                         "unreliable stability figures, so treat them as a "
                         "rough guide only." % study.P)
        held = bootstrap_top(study, args.bootstrap, args.seed)

    contested = []
    for i, r in enumerate(cards_rows):
        reasons = []
        margin = r["top_share"] - r["second_share"]
        if r["sorted_by"] == 0:
            reasons.append("nobody sorted this card")
        else:
            if r["top_share"] < CLOSED_MIN_SHARE:
                reasons.append("no category holds %d%% of participants"
                               % pct(CLOSED_MIN_SHARE))
            if r["second_category"] and r["second_ci_high"] >= r["ci_low"]:
                reasons.append("runner-up's interval overlaps the top "
                               "placement's")
            if held is not None and held[i] < STABILITY_DOUBTFUL:
                reasons.append("top placement changes when participants "
                               "are resampled")
        contested.append({
            "card": r["card"], "top_category": r["top_category"],
            "top_share": r["top_share"],
            "second_category": r["second_category"],
            "second_share": r["second_share"],
            "margin": margin if r["sorted_by"] else float("nan"),
            "held": float(held[i]) if held is not None else float("nan"),
            "reasons": "; ".join(reasons),
        })

    settings = {
        "input": os.path.basename(args.input),
        "sort_type": "closed",
        "participants_analysed": study.P,
        "participants_excluded": study.excluded,
        "cards": study.n,
        "categories": len(study.std_names),
        "share_denominator": "participants who sorted that card",
        "interval": "95% Wilson score interval",
        "bootstrap_resamples": args.bootstrap,
        "seed": args.seed,
        "category_names": ("standardised with merge file" if study.merge_used
                           else "case and spacing normalised only"),
    }

    out = []
    add = out.append
    add("CARD SORT ANALYSIS (CLOSED SORT)")
    add("=" * 32)
    add("%d participants, %d cards, %d categories." % (
        study.P, study.n, len(study.std_names)))
    add("")
    add("SETTINGS (these change the answer, so they travel with the results)")
    for k, v in settings.items():
        add("  %-22s %s" % (k, v))
    add("")
    add("Similarity matrices and dendrograms are not computed for a closed "
        "sort. The categories were supplied, so cards that share one may "
        "reflect your labels rather than how participants think. Placement "
        "agreement is the analysis that fits, and a tree test is the usual "
        "way to check the structure.")
    if study.unused_merge:
        add("NOTE: merge file entries that match no category in the data "
            "(check spelling): %s." % ", ".join(
                "'%s'" % k for k in study.unused_merge))
    if study.lookalikes:
        add("NOTE: found category name(s) %s. If these mean a card was left "
            "unsorted, rerun with --unsorted-label." % ", ".join(
                "'%s'" % k for k in study.lookalikes))

    add("")
    add("1. DATA CHECKS")
    add("Flags are prompts to look, not reasons to delete. 'Groups' is the "
        "number of categories the participant used.")
    add("")
    out += table(["participant", "categories used", "unsorted", "flags"],
                 [[r["participant"], r["groups"], r["unsorted"], r["flags"]]
                  for r in checks])

    add("")
    add("2. PLACEMENT AGREEMENT PER CARD (95% Wilson interval)")
    add("Share is of the participants who sorted the card. Put the interval "
        "in front of anyone who reads the share on its own.")
    add("")
    out += table(
        ["card", "sorted by", "top category", "share", "95% interval",
         "runner-up"],
        [[r["card"], r["sorted_by"], r["top_category"],
          "%d%%" % pct(r["top_share"]) if r["sorted_by"] else "n/a",
          "%d%% to %d%%" % (pct(r["ci_low"]), pct(r["ci_high"]))
          if r["sorted_by"] else "n/a",
          ("%s %d%%" % (r["second_category"], pct(r["second_share"]))
           if r["second_category"] else "none")] for r in cards_rows])

    add("")
    add("3. RESULTS MATRIX (participants per card and category, with share)")
    add("")
    heads = ["card"] + study.std_names
    mrows = []
    for r in cards_rows:
        row = [r["card"]]
        for k, c in enumerate(r["counts"]):
            row.append("%d (%d%%)" % (c, pct(c / r["sorted_by"]))
                       if r["sorted_by"] else "0")
        mrows.append(row)
    out += table(heads, mrows)

    add("")
    add("4. CATEGORIES VIEW")
    add("For each category: the cards it is the top placement for, and the "
        "average share those cards get. (The open-sort agreement figure is "
        "not used here: in a closed sort a few misplaced cards would drag "
        "it down without saying anything about the category.)")
    add("")
    cat_rows = []
    for name in study.std_names:
        mine = [r for r in cards_rows if r["top_category"] == name]
        cat_rows.append({
            "category": name, "cards": [r["card"] for r in mine],
            "mean_share": (sum(r["top_share"] for r in mine) / len(mine)
                           if mine else float("nan")),
        })
    out += table(
        ["category", "cards it is top for", "average share", "which cards"],
        [[c["category"], len(c["cards"]),
          "%d%%" % pct(c["mean_share"]) if c["cards"] else "n/a",
          ", ".join(c["cards"])] for c in cat_rows])

    if held is not None:
        add("")
        add("5. STABILITY OF EACH CARD'S TOP PLACEMENT (%d resamples of "
            "participants, seed %d)" % (args.bootstrap, args.seed))
        add("The share of resamples in which the card keeps the same top "
            "category. Ties go to the category that sorts first "
            "alphabetically.")
        if boot_note:
            add(boot_note)
        add("")
        out += table(["card", "top category", "held in resamples"],
                     [[c["card"], c["top_category"],
                       "%d%%" % pct(c["held"])] for c in contested])

    add("")
    add("6. CARDS NO SINGLE CATEGORY SETTLES")
    add("A card is listed when no category holds %d%% of participants, the "
        "runner-up's 95%% interval overlaps the top placement's (a "
        "conservative check that the top category is clearly ahead), or the "
        "top placement moves under resampling (held in under %d%% of "
        "resamples). The %d%% and %d%% figures are this script's defaults, "
        "not evidence-based." % (
            pct(CLOSED_MIN_SHARE), pct(STABILITY_DOUBTFUL),
            pct(CLOSED_MIN_SHARE), pct(STABILITY_DOUBTFUL)))
    add("")
    flagged = [c for c in contested if c["reasons"]]
    if flagged:
        out += table(
            ["card", "top", "share", "runner-up", "why"],
            [[c["card"], c["top_category"],
              "%d%%" % pct(c["top_share"]) if c["top_share"] == c["top_share"]
              else "n/a",
              ("%s %d%%" % (c["second_category"], pct(c["second_share"]))
               if c["second_category"] else "none"),
              c["reasons"]] for c in flagged])
    else:
        add("None flagged at these settings.")
    add("")
    add("Causes to check for each flagged card: an unclear label, a card "
        "that fits more than one category, or different groups of users "
        "placing it differently. The data cannot tell these apart.")

    results = {
        "sort_type": "closed",
        "settings": settings,
        "participants": checks,
        "cards": cards_rows,
        "categories": cat_rows,
        "contested": contested,
        "category_names": study.std_names,
    }
    files = {
        "cards.csv": (
            ["card", "sorted_by", "top_category", "top_count",
             "top_share_pct", "ci_low_pct", "ci_high_pct", "second_category",
             "second_share_pct"],
            [[r["card"], r["sorted_by"], r["top_category"], r["top_count"],
              fmt(100 * r["top_share"], 1), fmt(100 * r["ci_low"], 1),
              fmt(100 * r["ci_high"], 1), r["second_category"],
              fmt(100 * r["second_share"], 1)] for r in cards_rows]),
        "results_matrix.csv": (
            ["card", "sorted_by"] + study.std_names,
            [[r["card"], r["sorted_by"]] + r["counts"] for r in cards_rows]),
        "categories.csv": (
            ["category", "cards_it_is_top_for", "average_share_pct",
             "which_cards"],
            [[c["category"], len(c["cards"]),
              fmt(100 * c["mean_share"], 1), "; ".join(c["cards"])]
             for c in cat_rows]),
        "participants.csv": (
            ["participant", "categories_used", "sorted", "unsorted", "flags"],
            [[r["participant"], r["groups"], r["sorted"], r["unsorted"],
              r["flags"]] for r in checks]),
        "contested.csv": (
            ["card", "top_category", "top_share_pct", "second_category",
             "second_share_pct", "held_pct", "reasons"],
            [[c["card"], c["top_category"], fmt(100 * c["top_share"], 1),
              c["second_category"], fmt(100 * c["second_share"], 1),
              fmt(100 * c["held"], 1), c["reasons"]] for c in contested]),
    }
    return "\n".join(out), (results, files)


def run(args):
    cols = {"participant": args.col_participant, "card": args.col_card,
            "category": args.col_category, "preset": args.col_preset}
    rows = read_placements(args.input, cols)

    if args.list_categories:
        counts, users = Counter(), {}
        for p, _, cat, _ in rows:
            if cat:
                counts[norm(cat)] += 1
                users.setdefault(norm(cat), set()).add(p)
        shown = {}
        for _, _, cat, _ in rows:
            if cat:
                shown.setdefault(norm(cat), cat)
        out = ["Category names as typed (case and spacing ignored), most used "
               "first:", ""]
        out += table(
            ["category", "placements", "participants"],
            [[shown[k], counts[k], len(users[k])]
             for k, _ in counts.most_common()])
        return "\n".join(out), None

    merge_map = read_merge_file(args.merge_file) if args.merge_file else {}
    card_list = read_card_list(args.cards) if args.cards else None
    exclude = [x.strip() for x in args.exclude.split(",") if x.strip()]
    unsorted_labels = {norm(x) for x in args.unsorted_label}
    study = Study(rows, merge_map, card_list, exclude, unsorted_labels)

    cut = args.cut / 100.0 if args.cut > 1 else args.cut
    if not 0 < cut < 1:
        raise InputError("--cut must be between 0 and 1 (or 1 and 100 as a "
                         "percentage).")

    together, both = pair_arrays(study.group_labels)

    if args.sort_type == "closed":
        if args.explain:
            raise InputError("--explain describes similarity, which closed "
                             "sorts do not use.")
        return run_closed(study, args, together, both)

    if args.explain:
        return explain_pair(study, together, both, args.explain[0],
                            args.explain[1], args.unsorted), None

    t_sum = together.sum(axis=0, dtype=np.int64)
    b_sum = both.sum(axis=0, dtype=np.int64)
    S, empty_pairs = similarity(t_sum, b_sum, study.P, args.unsorted)
    Z = cluster(S, args.linkage)
    labels = cut_labels(Z, cut)
    order = leaves_list(Z)
    coph, _ = cophenet(Z, condensed_distance(S))

    checks, median_groups = participant_checks(study, together, both)
    cards_rows = cards_view(study)
    cats_rows = categories_view(study)

    sweep = []
    for c in sorted(set(CUT_SWEEP) | {cut}):
        lab_c = cut_labels(Z, c)
        sweep.append({
            "cut": c, "groups": len(set(lab_c.tolist())),
            "singletons": sum(1 for g in Counter(lab_c.tolist()).values()
                              if g == 1),
            "agreement_with_chosen": pair_agreement(lab_c, labels),
        })

    compare = None
    if args.compare_linkage != "none" and args.compare_linkage != args.linkage:
        Z2 = cluster(S, args.compare_linkage)
        lab2 = cut_labels(Z2, cut)
        compare = {
            "method": args.compare_linkage,
            "groups": groups_from_labels(lab2, study.cards),
            "agreement": pair_agreement(lab2, labels),
        }

    stability = retention = stability_rows = None
    boot_note = ""
    if args.bootstrap > 0:
        if study.P < MIN_BOOTSTRAP_PARTICIPANTS:
            boot_note = ("Only %d participants: resampling this few gives "
                         "unreliable stability figures, so treat them as a "
                         "rough guide only." % study.P)
        stability, retention = bootstrap(
            together, both, args.unsorted, args.linkage, cut, labels,
            args.bootstrap, args.seed)

    contested = contested_cards(S, labels, study.cards, retention, cut)
    groups = groups_from_labels(labels, study.cards)

    settings = {
        "input": os.path.basename(args.input),
        "sort_type": args.sort_type,
        "participants_analysed": study.P,
        "participants_excluded": study.excluded,
        "cards": study.n,
        "unsorted_handling": args.unsorted,
        "similarity": "share of participants who grouped the pair together",
        "distance": "1 minus similarity",
        "linkage": args.linkage,
        "cut_similarity": cut,
        "comparison_linkage": args.compare_linkage,
        "bootstrap_resamples": args.bootstrap,
        "seed": args.seed,
        "category_names": ("standardised with merge file" if study.merge_used
                           else "case and spacing normalised only"),
        "group_identity": "a participant's own groups, by normalised name",
    }

    # ---- text summary
    out = []
    add = out.append
    add("CARD SORT ANALYSIS")
    add("=" * 18)
    add("%d participants, %d cards." % (study.P, study.n))
    add("")
    add("SETTINGS (these change the answer, so they travel with the results)")
    for k, v in settings.items():
        add("  %-22s %s" % (k, v))
    if study.lookalikes:
        add("")
        add("NOTE: found category name(s) %s. If these mean a card was left "
            "unsorted, rerun with --unsorted-label." % ", ".join(
                "'%s'" % k for k in study.lookalikes))
    if args.sort_type == "hybrid" or study.has_preset:
        presets = [study.std_names[k] for k in sorted(study.preset_ids)]
        add("")
        add("NOTE: hybrid sort. Predefined categories can anchor what "
            "participants create, so read agreement on %s with that in "
            "mind, and review the participant-created groups separately." %
            (", ".join("'%s'" % p for p in presets) if presets
             else "the predefined categories (mark them with a "
                  "category_preset column to have them listed)"))
    if study.unused_merge:
        add("NOTE: merge file entries that match no category in the data "
            "(check spelling): %s." % ", ".join(
                "'%s'" % k for k in study.unused_merge))
    if study.missing_cells:
        add("NOTE: %d participant/card combinations were absent from the "
            "file and were treated as unsorted." % study.missing_cells)
    if empty_pairs:
        add("NOTE: %d card pair(s) were never sorted together with both "
            "cards by anyone (pairwise mode); their similarity is shown as "
            "0." % empty_pairs)

    add("")
    add("1. DATA CHECKS")
    add("Median number of groups per participant: %s. Flags are prompts to "
        "look, not reasons to delete. A participant who looks odd may simply "
        "sort differently." % fmt(median_groups, 1))
    add("Alignment is the correlation between a participant's pairings and "
        "everyone else's (blank when it cannot be computed).")
    add("")
    out += table(["participant", "groups", "unsorted", "alignment", "flags"],
                 [[r["participant"], r["groups"], r["unsorted"],
                   fmt(r["alignment"], 2), r["flags"]] for r in checks])

    add("")
    add("2. CARDS VIEW (top placement, with 95% Wilson interval)")
    add("Share is of the participants who sorted the card. With few "
        "participants the interval is wide, and that width is the point.")
    add("")
    out += table(
        ["card", "sorted by", "categories", "top category", "share",
         "95% interval"],
        [[r["card"], r["sorted_by"], r["categories"], r["top_category"],
          "%d%%" % pct(r["top_share"]) if r["sorted_by"] else "n/a",
          "%d%% to %d%%" % (pct(r["ci_low"]), pct(r["ci_high"]))
          if r["sorted_by"] else "n/a"] for r in cards_rows])

    add("")
    add("3. CATEGORIES VIEW")
    add("Agreement = mean, over the unique cards in the category, of the "
        "share of that category's participants who put the card there "
        "(Kuric et al. definition). A convention, not a validated cut-off.")
    add("")
    if study.has_preset:
        out += table(
            ["category", "origin", "participants", "unique cards",
             "agreement"],
            [[r["category"], r["origin"], r["participants"],
              r["unique_cards"], "%d%%" % pct(r["agreement"])]
             for r in cats_rows])
    else:
        out += table(
            ["category", "participants", "unique cards", "agreement"],
            [[r["category"], r["participants"], r["unique_cards"],
              "%d%%" % pct(r["agreement"])] for r in cats_rows])

    add("")
    add("4. SIMILARITY MATRIX")
    add("Saved as matrix.csv with --out (cards in dendrogram order, values "
        "are percentages of participants).")

    add("")
    add("5. CLUSTERING (%s linkage)" % args.linkage)
    add("Cophenetic correlation (how faithfully the tree reproduces the "
        "matrix): %s" % fmt(float(coph), 2))
    add("")
    add("Tree (the text alternative to the dendrogram image):")
    out += ["  " + line for line in nested_tree(Z, study.cards)]
    add("")
    note = {
        "average": "the average pairwise similarity inside each group is at "
                   "least %d%%" % pct(cut),
        "complete": "every pair of cards inside each group is at least "
                    "%d%% similar" % pct(cut),
        "single": "every card has at least one link of %d%% or more to "
                  "another card in its group (groups can chain)" % pct(cut),
    }[args.linkage]
    add("Groups at the %d%% cut (%s):" % (pct(cut), note))
    for g in groups:
        add("  - " + ", ".join(g))

    add("")
    add("6. HOW MUCH THE STRUCTURE MOVES")
    add("The cut point is a judgement. Agreement is the share of card pairs "
        "treated the same way (together or apart) as at your chosen cut.")
    add("")
    out += table(
        ["cut", "groups", "single-card groups", "agreement with chosen cut"],
        [["%d%%" % pct(r["cut"]) + (" (chosen)" if abs(r["cut"] - cut) < 1e-9
                                    else ""),
          r["groups"], r["singletons"],
          "%d%%" % pct(r["agreement_with_chosen"])] for r in sweep])
    if compare:
        add("")
        add("Same cut with %s linkage: pair agreement with %s linkage is "
            "%d%%. Groups:" % (compare["method"], args.linkage,
                               pct(compare["agreement"])))
        for g in compare["groups"]:
            add("  - " + ", ".join(g))

    if stability is not None:
        add("")
        add("7. STABILITY (%d bootstrap resamples of participants, seed %d)"
            % (args.bootstrap, args.seed))
        add("Mean Jaccard overlap between each group and its best match in "
            "each resample. Bands follow the clusterboot documentation "
            "(0.75 stable, 0.60 to 0.75 doubtful, under 0.60 unstable), "
            "written for clustering in general rather than card sorts.")
        if boot_note:
            add(boot_note)
        add("")
        by_lab = {int(l): [] for l in labels}
        for i, l in enumerate(labels):
            by_lab[int(l)].append(study.cards[i])
        stability_rows = []
        for lab, j in sorted(stability.items(),
                             key=lambda kv: -len(by_lab[kv[0]])):
            stability_rows.append({"group": by_lab[lab], "mean_jaccard": j,
                                   "band": stability_band(j)})
        out += table(["group", "mean Jaccard", "band"],
                     [[", ".join(r["group"]), fmt(r["mean_jaccard"], 2),
                       r["band"]] for r in stability_rows])

    add("")
    add("8. CARDS NO SINGLE GROUP SETTLES")
    add("A card is listed when it does not join a group, is only weakly "
        "similar to its own group, is nearly as similar to another group "
        "(margin under %d points), or moves group often under resampling "
        "(retention under %d%%). These thresholds are this script's "
        "defaults, not evidence-based." % (
            pct(CONTESTED_MARGIN), pct(STABILITY_DOUBTFUL)))
    add("")
    flagged = [r for r in contested if r["reasons"]]
    if flagged:
        out += table(
            ["card", "own group", "best other", "margin", "retention",
             "why"],
            [[r["card"], "%d%%" % pct(r["cohesion"]),
              "%d%%" % pct(r["best_other"]), "%d" % pct(r["margin"]),
              ("%d%%" % pct(r["retention"])
               if not math.isnan(r["retention"]) else "n/a"),
              r["reasons"]] for r in flagged])
    else:
        add("None flagged at these settings.")
    add("")
    add("Causes to check for each flagged card: an unclear label, a card "
        "that fits more than one area, or different groups of users "
        "sorting differently. The data cannot tell these apart.")

    results = {
        "sort_type": args.sort_type,
        "settings": settings,
        "participants": checks,
        "cards": cards_rows,
        "categories": cats_rows,
        "matrix": {
            "order": [study.cards[i] for i in order],
            "values_pct": [[round(100 * float(S[i, j]), 1) for j in order]
                           for i in order],
        },
        "dendrogram": {
            "cards": study.cards,
            "linkage": [[float(x) for x in row] for row in Z],
            "cut_similarity": cut,
            "method": args.linkage,
        },
        "groups": groups,
        "sweep": sweep,
        "comparison": compare,
        "stability": stability_rows,
        "contested": contested,
        "cophenetic_correlation": float(coph),
        "tree": nested_tree(Z, study.cards),
    }
    files = {
        "matrix.csv": (["card"] + [study.cards[i] for i in order],
                       [[study.cards[i]] + [
                           "%.1f" % (100 * S[i, j]) for j in order]
                        for i in order]),
        "cards.csv": (
            ["card", "sorted_by", "categories", "top_category", "top_count",
             "top_share_pct", "ci_low_pct", "ci_high_pct", "all_categories"],
            [[r["card"], r["sorted_by"], r["categories"], r["top_category"],
              r["top_count"], fmt(100 * r["top_share"], 1),
              fmt(100 * r["ci_low"], 1), fmt(100 * r["ci_high"], 1),
              r["all_categories"]] for r in cards_rows]),
        "categories.csv": (
            ["category", "origin", "participants", "unique_cards",
             "agreement_pct", "cards"],
            [[r["category"], r["origin"], r["participants"],
              r["unique_cards"], fmt(100 * r["agreement"], 1), r["cards"]]
             for r in cats_rows]),
        "participants.csv": (
            ["participant", "groups", "sorted", "unsorted", "alignment",
             "flags"],
            [[r["participant"], r["groups"], r["sorted"], r["unsorted"],
              fmt(r["alignment"], 3), r["flags"]] for r in checks]),
        "dendrogram.csv": (
            ["step", "left", "right", "similarity_pct", "size"],
            [[r["step"], r["left"], r["right"],
              "%.1f" % (100 * r["similarity"]), r["size"]]
             for r in merge_table(Z, study.cards)]),
        "contested.csv": (
            ["card", "own_group_pct", "best_other_pct", "margin_points",
             "retention_pct", "reasons", "group_mates"],
            [[r["card"], fmt(100 * r["cohesion"], 1),
              fmt(100 * r["best_other"], 1), fmt(100 * r["margin"], 1),
              fmt(100 * r["retention"], 1), r["reasons"], r["group_mates"]]
             for r in contested]),
    }
    return "\n".join(out), (results, files)


def build_parser():
    ap = argparse.ArgumentParser(
        description="Analyse open and hybrid card sort results.")
    ap.add_argument("input", help="CSV with one row per card placement")
    ap.add_argument("--sort-type", choices=("open", "closed", "hybrid"),
                    default="open",
                    help="open and hybrid sorts get the similarity and "
                    "clustering analysis. closed sorts get placement "
                    "agreement instead (default open)")
    ap.add_argument("--cards", help="text file, one card per line (catches "
                    "cards nobody sorted)")
    ap.add_argument("--merge-file", help="CSV with columns raw,standard "
                    "mapping category names to standardised ones")
    ap.add_argument("--exclude", default="", help="comma-separated "
                    "participant IDs to leave out")
    ap.add_argument("--unsorted", choices=("singleton", "pairwise"),
                    default="singleton",
                    help="how a card left unsorted counts toward a pair. "
                    "singleton: it is 'not together' with every card and the "
                    "participant stays in the denominator. pairwise: the "
                    "participant is left out of any pair involving it.")
    ap.add_argument("--unsorted-label", action="append", default=[],
                    help="category name that means 'left unsorted' (repeat "
                    "for several)")
    ap.add_argument("--linkage", choices=("average", "complete", "single"),
                    default="average")
    ap.add_argument("--compare-linkage", choices=("average", "complete",
                                                  "single", "none"),
                    default="complete")
    ap.add_argument("--cut", type=float, default=DEFAULT_CUT,
                    help="similarity at which to cut the tree, 0 to 1 "
                    "(default 0.5)")
    ap.add_argument("--bootstrap", type=int, default=1000,
                    help="bootstrap resamples, 0 to skip (default 1000)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", help="directory to write CSV tables and "
                    "results.json into")
    ap.add_argument("--explain", nargs=2, metavar=("CARD_A", "CARD_B"),
                    help="show the arithmetic behind one matrix cell")
    ap.add_argument("--list-categories", action="store_true",
                    help="list category names to help build a merge file")
    ap.add_argument("--col-participant", default="participant_id")
    ap.add_argument("--col-card", default="card")
    ap.add_argument("--col-category", default="category")
    ap.add_argument("--col-preset", default="category_preset",
                    help="optional column marking categories the researcher "
                    "supplied (hybrid sorts)")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        text, extra = run(args)
    except InputError as exc:
        sys.stderr.write("Error: %s\n" % exc)
        return 2
    print(text)
    if extra and args.out:
        results, files = extra
        os.makedirs(args.out, exist_ok=True)
        for name, (headers, rows) in files.items():
            write_csv(os.path.join(args.out, name), headers, rows)
        with open(os.path.join(args.out, "results.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(results, fh, indent=2, default=float)
        with open(os.path.join(args.out, "summary.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write(text + "\n")
        print("\nTables written to %s" % os.path.abspath(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
