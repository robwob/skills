#!/usr/bin/env python3
"""Arithmetic and checks for interview-analysis. Standard library only.

Seven commands, each printing what it did and every choice it made:

  columns       list the columns of one or more transcript CSVs, with sample values,
                a guessed type, and the distinct speakers
  pseudonymise  combine transcripts into one file, rename participants P1, P2 ...,
                and write a private key file
  stats         per interview: length, turns and words by role, and the participant's
                share of the words
  prompts       list interviewer turns that look hypothetical or leading, so the
                answers to them can be weighed
  quotes        check every quote is verbatim, from the right participant, not the
                interviewer, and at the right timestamp
  tally         count participants per theme from a coding file, and suggest the
                concern on each confidence component
  confidence    apply the confidence rule to findings, opportunities and
                recommendations, and show the working

A transcript CSV has one row per turn: who spoke, when, and what they said. One file per
interview, or one file holding several interviews with a column naming the interview.

Run any command with --help for its options. See scripts/README.md.
"""
import argparse
import csv
import difflib
import json
import os
import re
import sys
import unicodedata


# ---------------------------------------------------------------------------
# Loading


def read_csv(path):
    """Return (headers, rows). Rows are dicts. Tolerates a UTF-8 byte order mark."""
    if path.lower().endswith((".xlsx", ".xls")):
        sys.exit(
            f"{path} is a spreadsheet, not a CSV. Export it as CSV from the tool or from "
            "Excel, Numbers or Google Sheets (File, Download, CSV), then run this again."
        )
    if not os.path.exists(path):
        sys.exit(f"File not found: {path}")
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        return [h for h in (reader.fieldnames or [])], rows


def require(headers, *cols, where=""):
    missing = [c for c in cols if c and c not in headers]
    if missing:
        found = "\n  ".join(headers)
        sys.exit(f"Column not found{where}: {', '.join(missing)}\nColumns in the file:\n  {found}")


# ---------------------------------------------------------------------------
# Timestamps


TIME_RE = re.compile(r"^\s*(?:(\d+):)?(\d{1,2}):(\d{1,2})(?:[.,](\d+))?\s*$")


def to_seconds(text):
    """Parse 1:02:03, 01:02:03.500, 00:01:02,500, 62:03, 62.5 or 62. None if blank or unreadable."""
    t = (text or "").strip()
    if not t:
        return None
    m = TIME_RE.match(t)
    if m:
        h, mnt, s, frac = m.groups()
        secs = int(h or 0) * 3600 + int(mnt) * 60 + int(s)
        if frac:
            secs += float("0." + frac)
        return float(secs)
    try:
        return float(t)
    except ValueError:
        return None


def fmt_time(secs):
    if secs is None:
        return "?"
    secs = int(secs)
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def looks_like_time(values):
    vals = [v for v in values if v and v.strip()]
    return bool(vals) and all(to_seconds(v) is not None for v in vals)


# ---------------------------------------------------------------------------
# The normalised transcript: one row per turn, written by `pseudonymise`


NORM_COLS = ["interview", "turn", "participant", "role", "start", "end", "text"]


def load_turns(path):
    headers, rows = read_csv(path)
    require(headers, *NORM_COLS, where=" (run `pseudonymise` first: it writes this layout)")
    turns = []
    for r in rows:
        turns.append({
            "interview": r["interview"],
            "turn": int(r["turn"]),
            "participant": r["participant"],
            "role": r["role"],
            "start": r["start"],
            "end": r["end"],
            "start_s": to_seconds(r["start"]),
            "end_s": to_seconds(r["end"]),
            "text": r["text"] or "",
        })
    # Where only start times exist, a turn ends where the next one in the interview starts.
    by_iv = {}
    for t in turns:
        by_iv.setdefault(t["interview"], []).append(t)
    for ts in by_iv.values():
        ts.sort(key=lambda t: t["turn"])
        for a, b in zip(ts, ts[1:]):
            if a["end_s"] is None and b["start_s"] is not None:
                a["end_s"] = b["start_s"]
    return turns


# ---------------------------------------------------------------------------
# columns


def guess_type(values):
    vals = [v.strip() for v in values if v and v.strip()]
    if not vals:
        return "empty"
    if looks_like_time(vals):
        return "timestamp?"
    distinct = len(set(v.lower() for v in vals))
    avg_len = sum(len(v) for v in vals) / len(vals)
    if avg_len > 40:
        return "spoken text?"
    if distinct <= max(4, len(vals) // 4):
        return f"speaker or interview? ({distinct} distinct values)"
    return "short text"


def cmd_columns(args):
    for path in args.files:
        headers, rows = read_csv(path)
        print(f"{path}: {len(rows)} rows, {len(headers)} columns\n")
        for i, h in enumerate(headers, 1):
            col = [r.get(h) or "" for r in rows]
            sample = next((v for v in col if v.strip()), "").replace("\n", " ")
            if len(sample) > 70:
                sample = sample[:67] + "..."
            g = guess_type(col)
            print(f"{i:>3}. {h}")
            print(f"     guess:  {g}")
            print(f"     sample: {sample!r}")
            if g.startswith("speaker"):
                counts = {}
                for v in col:
                    counts[v.strip()] = counts.get(v.strip(), 0) + 1
                listed = ", ".join(f"{k!r} ({n} rows)" for k, n in sorted(counts.items(), key=lambda kv: -kv[1]))
                print(f"     values: {listed}")
        print()
    print("The guesses are a starting point only. Confirm with the user which column is the speaker, "
          "which the text and which the timestamps, and which speaker values are the interviewer.")


# ---------------------------------------------------------------------------
# pseudonymise


GENERIC = re.compile(
    r"^(participant|interviewee|respondent|user|customer|speaker|interviewer|moderator|"
    r"researcher|facilitator|host|guest|unknown)[\s_-]*[a-z]?\d*$",
    re.IGNORECASE,
)


def cmd_pseudonymise(args):
    interviewer_values = {v.strip().lower() for v in args.interviewer}
    turns = []
    for path in args.files:
        headers, rows = read_csv(path)
        require(headers, args.speaker, args.text, args.start, args.end, args.interview, where=f" in {path}")
        stem = os.path.splitext(os.path.basename(path))[0]
        for r in rows:
            speaker = (r.get(args.speaker) or "").strip()
            text = r.get(args.text) or ""
            if not speaker and not text.strip():
                continue
            turns.append({
                "interview": (r.get(args.interview) or "").strip() if args.interview else stem,
                "speaker": speaker,
                "start": (r.get(args.start) or "").strip() if args.start else "",
                "end": (r.get(args.end) or "").strip() if args.end else "",
                "text": text,
            })

    if not turns:
        sys.exit("No turns found.")
    seen_interviewer = {t["speaker"].lower() for t in turns} & interviewer_values
    if not seen_interviewer:
        speakers = sorted({t["speaker"] for t in turns})
        sys.exit("None of the --interviewer values appear in the speaker column.\nSpeakers found:\n  "
                 + "\n  ".join(repr(s) for s in speakers))

    # A participant is a non-interviewer speaker within one interview. The same label in two
    # interviews ("Participant") is two people.
    key, interviews = {}, []
    for t in turns:
        if t["interview"] not in interviews:
            interviews.append(t["interview"])
        if t["speaker"].lower() in interviewer_values:
            continue
        k = (t["interview"], t["speaker"])
        if k not in key:
            key[k] = f"P{len(key) + 1}"

    # Names to replace inside the text: speaker values that are real names, not role labels.
    names = {}
    for (iv, spk), pid in key.items():
        if spk and not GENERIC.match(spk):
            names[spk] = pid
    interviewer_names = {t["speaker"] for t in turns
                         if t["speaker"].lower() in interviewer_values and not GENERIC.match(t["speaker"])}
    for n in interviewer_names:
        names.setdefault(n, "[Interviewer]")

    replaced = 0
    order = sorted(names.items(), key=lambda kv: -len(kv[0]))  # longest first
    for t in turns:
        text = t["text"]
        for name, sub in order:
            if name in text:
                replaced += text.count(name)
                text = text.replace(name, sub)
        t["text"] = text

    first_hits = []
    for name in names:
        parts = name.split()
        first = parts[0] if parts else ""
        if len(parts) > 1 and len(first) > 2:
            for t in turns:
                if re.search(rf"\b{re.escape(first)}\b", t["text"]):
                    first_hits.append((t["interview"], t["start"], first))

    counters = {}
    out_rows = []
    for t in turns:
        counters[t["interview"]] = counters.get(t["interview"], 0) + 1
        is_int = t["speaker"].lower() in interviewer_values
        pid = key.get((t["interview"], t["speaker"]), "")
        # Interviewer turns carry the interview's participant, so a turn can always be traced.
        out_rows.append({
            "interview": t["interview"],
            "turn": counters[t["interview"]],
            "participant": "" if is_int else pid,
            "role": "interviewer" if is_int else "participant",
            "start": t["start"],
            "end": t["end"],
            "text": t["text"],
        })

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=NORM_COLS)
        w.writeheader()
        w.writerows(out_rows)
    with open(args.key, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["participant_id", "interview", "original_speaker"])
        for (iv, spk), pid in key.items():
            w.writerow([pid, iv, spk])

    print(f"{len(interviews)} interview(s), {len(out_rows)} turns.")
    print(f"{len(key)} participant(s) renamed P1 to P{len(key)}, in order of first appearance:")
    for (iv, spk), pid in key.items():
        print(f"  {pid}: interview {iv!r}")
    multi = [iv for iv in interviews if sum(1 for (i, _) in key if i == iv) > 1]
    if multi:
        print(f"More than one participant in: {', '.join(multi)}. Confirm these are paired interviews, "
              "not a mislabelled interviewer.")
    none = [iv for iv in interviews if not any(i == iv for (i, _) in key)]
    if none:
        print(f"No participant found in: {', '.join(none)}. Check the --interviewer values.")
    print(f"{replaced} occurrence(s) of a speaker's name replaced inside the text.")
    if not args.start:
        print("No --start column given: quotes and coding cannot be tied to a time in the recording.")
    print(f"Combined, pseudonymised transcript: {os.path.abspath(args.out)}")
    print(f"Key (keep private, never put it in the report): {os.path.abspath(args.key)}")
    if first_hits:
        print("\nFirst names that may still identify someone. Check these turns by hand:")
        for iv, start, first in first_hits:
            print(f"  interview {iv!r} at {start or '?'}: {first!r}")
    generic = sorted({spk for (_, spk) in key if GENERIC.match(spk)})
    if generic:
        print(f"\nSpeakers are labelled by role ({', '.join(repr(g) for g in generic)}), so their names "
              "are not known and cannot be replaced automatically. Read for names while coding.")
    print("Names of other people, places and employers inside the text are not touched.")


# ---------------------------------------------------------------------------
# stats


def words(text):
    return len(re.findall(r"\b[\w']+\b", text or ""))


def cmd_stats(args):
    turns = load_turns(args.file)
    by_iv = {}
    for t in turns:
        by_iv.setdefault(t["interview"], []).append(t)
    print(f"{'Interview':<20} {'Participant':<12} {'Length':>8} {'Turns I/P':>10} {'Words I/P':>13} {'P share':>8}")
    flagged = []
    for iv, ts in by_iv.items():
        pids = sorted({t["participant"] for t in ts if t["participant"]}, key=lambda p: int(p[1:]) if p[1:].isdigit() else 0)
        starts = [t["start_s"] for t in ts if t["start_s"] is not None]
        ends = [t["end_s"] for t in ts if t["end_s"] is not None]
        length = (max(ends + starts) - min(starts)) if starts else None
        ti = sum(1 for t in ts if t["role"] == "interviewer")
        tp = sum(1 for t in ts if t["role"] == "participant")
        wi = sum(words(t["text"]) for t in ts if t["role"] == "interviewer")
        wp = sum(words(t["text"]) for t in ts if t["role"] == "participant")
        share = wp / (wi + wp) if wi + wp else 0
        print(f"{iv[:20]:<20} {', '.join(pids)[:12]:<12} {fmt_time(length):>8} {f'{ti}/{tp}':>10} "
              f"{f'{wi}/{wp}':>13} {share:>8.0%}")
        if share < 0.5:
            flagged.append(iv)
    print("\nLength runs from the first timestamp to the last; a final turn with no end time is not counted.")
    if flagged:
        print(f"The interviewer spoke more words than the participant in: {', '.join(flagged)}. "
              "Read those interviews for leading or closed questions before weighting their evidence.")


# ---------------------------------------------------------------------------
# prompts


HYPOTHETICAL = re.compile(
    r"\b(would you|if you could|if there (was|were)|imagine|how likely|will you|"
    r"could you see yourself|would it be|what if)\b", re.IGNORECASE)
LEADING = re.compile(
    r"\b(don't you|do you not|wouldn't you|isn't it|wasn't it|didn't you find|would you agree|"
    r"i guess you|so you'd|so you would|presumably|surely)\b|,\s*right\?\s*$", re.IGNORECASE)


def cmd_prompts(args):
    turns = load_turns(args.file)
    by_iv = {}
    for t in turns:
        by_iv.setdefault(t["interview"], []).append(t)
    found = 0
    for iv, ts in by_iv.items():
        ts.sort(key=lambda t: t["turn"])
        for i, t in enumerate(ts):
            if t["role"] != "interviewer":
                continue
            kinds = []
            if HYPOTHETICAL.search(t["text"]):
                kinds.append("hypothetical")
            if LEADING.search(t["text"]):
                kinds.append("leading")
            if not kinds:
                continue
            nxt = next((u for u in ts[i + 1:] if u["role"] == "participant"), None)
            found += 1
            print(f"[{' + '.join(kinds)}] interview {iv!r} at {t['start'] or '?'}: \"{t['text'].strip()}\"")
            if nxt:
                print(f"     answered by {nxt['participant']} at {nxt['start'] or '?'}")
    print(f"\n{found} interviewer turn(s) flagged.")
    print("Matched on wording only, so read each one: some are harmless. An answer to a hypothetical "
          "question is a prediction, and an answer to a leading one is weaker than an unprompted "
          "remark. Code them that way.")


# ---------------------------------------------------------------------------
# quotes


QUOTE_MAP = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "′": "'", "″": '"',
    "–": "-", "—": "-", "…": "...", " ": " ",
}


def norm(text):
    """Normalise only what does not change meaning: typographic quotes, dashes, spacing, case."""
    text = unicodedata.normalize("NFKC", text or "")
    for a, b in QUOTE_MAP.items():
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip().lower()


def split_ellipsis(quote):
    """A quote with '...' is checked as fragments that must appear in order."""
    return [f.strip() for f in re.split(r"\.\.\.|\[\.\.\.\]", norm(quote)) if f.strip()]


def find_in_order(fragments, text):
    pos = 0
    for f in fragments:
        i = text.find(f, pos)
        if i < 0:
            return False
        pos = i + len(f)
    return True


def locate(fragments, ts):
    """Find the fragments in one turn, or else across consecutive turns of the same speaker
    in order. Returns the first turn they start in, or None."""
    for t in ts:
        if find_in_order(fragments, norm(t["text"])):
            return t
    joined, owners = "", []
    for t in ts:
        start = len(joined)
        joined += norm(t["text"]) + " "
        owners.append((start, t))
    if fragments and find_in_order(fragments, joined):
        i = joined.find(fragments[0])
        owner = None
        for start, t in owners:
            if start <= i:
                owner = t
        return owner
    return None


def within(at_s, t):
    if at_s is None or t["start_s"] is None:
        return True
    end = t["end_s"] if t["end_s"] is not None else t["start_s"]
    return t["start_s"] - 1 <= at_s <= end + 1


def closest(quote, turns):
    q = norm(quote)
    best, best_ratio = None, 0.0
    for t in turns:
        text = norm(t["text"])
        if not text:
            continue
        sm = difflib.SequenceMatcher(None, q, text, autojunk=False)
        m = sm.find_longest_match(0, len(q), 0, len(text))
        start = max(0, m.b - m.a)
        window = text[start:start + len(q) + 20]
        r = difflib.SequenceMatcher(None, q, window).ratio()
        if r > best_ratio:
            best, best_ratio = (t, window), r
    return best, best_ratio


def cmd_quotes(args):
    turns = load_turns(args.file)
    with open(args.quotes, encoding="utf-8") as fh:
        quotes = json.load(fh)
    if isinstance(quotes, dict):
        quotes = quotes.get("quotes", [])

    pids = {t["participant"] for t in turns if t["participant"]}
    iv_of = {t["participant"]: t["interview"] for t in turns if t["participant"]}
    failures = 0
    for i, item in enumerate(quotes, 1):
        quote = item.get("quote", "")
        pid = str(item.get("participant", "")).strip()
        at = str(item.get("at", "") or "").strip()
        frags = split_ellipsis(quote)
        own = [t for t in turns if t["participant"] == pid]
        found_at = ""
        if pid not in pids:
            status = "PARTICIPANT NOT IN DATA"
        else:
            hit = locate(frags, own)
            if hit:
                found_at = hit["start"]
                if at and not within(to_seconds(at), hit):
                    status = f"TIMESTAMP WRONG (found at {hit['start'] or '?'})"
                else:
                    status = "VERBATIM"
            else:
                interviewer = [t for t in turns if t["role"] == "interviewer" and t["interview"] == iv_of.get(pid)]
                if interviewer and locate(frags, interviewer):
                    status = "INTERVIEWER'S WORDS"
                else:
                    others = sorted({t["participant"] for t in turns if t["participant"] and t["participant"] != pid
                                     and locate(frags, [t])})
                    status = (f"WRONG PARTICIPANT (found under {', '.join(others)})" if others else "NOT FOUND")
        ok = status == "VERBATIM"
        failures += not ok
        where = f" at {found_at}" if ok and found_at else ""
        print(f"{i:>3}. [{status}] {pid}{where}: \"{quote}\"")
        if status == "NOT FOUND":
            match, ratio = closest(quote, [t for t in turns if t["role"] == "participant"])
            if match and ratio >= 0.5:
                t, window = match
                print(f"     Closest text ({t['participant']} at {t['start'] or '?'}, {ratio:.0%} similar): \"{window}\"")
            print("     Replace it with the participant's exact words, or remove it.")

    print(f"\n{len(quotes) - failures} of {len(quotes)} quotes verbatim, from the right participant and time.")
    print("Checked ignoring case, spacing and typographic quote marks. '...' marks a cut, and the "
          "pieces must appear in order. Nothing else is forgiven.")
    if failures:
        sys.exit(1)


# ---------------------------------------------------------------------------
# tally


EVIDENCE_ORDER = ["shown", "occasion", "general", "opinion", "hypothetical"]
STANCES = {"for", "against"}
CONCERNS = ["none", "minor", "moderate", "serious"]


def strongest(types):
    return min(types, key=EVIDENCE_ORDER.index)


def suggest(k, m, n):
    """Suggested concern per component. The library's own lines, tagged (derived) there."""
    if k >= n / 2 and k >= 2:
        adequacy = "none"
    elif k >= 3:
        adequacy = "minor"
    elif k == 2:
        adequacy = "moderate"
    else:
        adequacy = "serious"
    ratio = m / k if k else 1
    if m == 0:
        coherence = "none"
    elif ratio <= 1 / 3:
        coherence = "minor"
    elif ratio < 1:
        coherence = "moderate"
    else:
        coherence = "serious"
    return adequacy, coherence


def evidence_concern(by_type):
    """by_type: count of supporting participants by their strongest evidence type."""
    k = sum(by_type.values())
    strong = by_type.get("shown", 0) + by_type.get("occasion", 0)
    if k and strong >= k / 2:
        return "none"
    if strong >= 1:
        return "minor"
    if by_type.get("general", 0):
        return "moderate"
    return "serious"


def cmd_tally(args):
    headers, rows = read_csv(args.file)
    require(headers, "participant", "theme", "evidence", "stance")

    errors = []
    turns = load_turns(args.transcripts) if args.transcripts else None
    all_pids = sorted({t["participant"] for t in turns if t["participant"]},
                      key=lambda p: int(p[1:]) if p[1:].isdigit() else 0) if turns else None

    segments = {}
    if args.segments:
        sh, srows = read_csv(args.segments)
        require(sh, "participant", "segment", where=f" in {args.segments}")
        segments = {r["participant"].strip(): r["segment"].strip() for r in srows}

    themes = {}
    for line, r in enumerate(rows, 2):
        pid = r["participant"].strip()
        theme = r["theme"].strip()
        ev = r["evidence"].strip().lower()
        stance = r["stance"].strip().lower()
        at = (r.get("at") or "").strip()
        if ev not in EVIDENCE_ORDER:
            errors.append(f"row {line}: evidence {ev!r} is not one of {', '.join(EVIDENCE_ORDER)}")
            continue
        if stance not in STANCES:
            errors.append(f"row {line}: stance {stance!r} is not 'for' or 'against'")
            continue
        if turns is not None:
            if pid not in all_pids:
                errors.append(f"row {line}: participant {pid!r} is not in the transcripts")
                continue
            if at:
                at_s = to_seconds(at)
                own = [t for t in turns if t["participant"] == pid]
                if not any(within(at_s, t) for t in own if t["start_s"] is not None):
                    errors.append(f"row {line}: no turn by {pid} at {at}")
        th = themes.setdefault(theme, {"for": {}, "against": {}})
        th[stance].setdefault(pid, []).append(ev)

    n = args.participants or (len(all_pids) if all_pids else None)
    if not n:
        sys.exit("Give --transcripts (the pseudonymised file) or --participants N, so counts can be "
                 "stated out of the total.")

    result = {"participants": n, "themes": []}
    for theme, th in themes.items():
        fors, againsts = th["for"], th["against"]
        mixed = sorted(set(fors) & set(againsts))
        k, m = len(fors), len(againsts)
        by_type = {}
        for pid, evs in fors.items():
            s = strongest(evs)
            by_type[s] = by_type.get(s, 0) + 1
        adequacy, coherence = suggest(k, m, n)
        evidence = evidence_concern(by_type)
        seg_break = {}
        if segments:
            for pid in fors:
                seg = segments.get(pid, "(no segment)")
                seg_break[seg] = seg_break.get(seg, 0) + 1
        result["themes"].append({
            "theme": theme, "for": sorted(fors), "against": sorted(againsts), "mixed": mixed,
            "for_count": k, "against_count": m, "strongest_evidence": by_type, "segments": seg_break,
            "suggested": {"adequacy": adequacy, "coherence": coherence, "evidence": evidence},
        })

    seg_sizes = {}
    for pid, seg in segments.items():
        seg_sizes[seg] = seg_sizes.get(seg, 0) + 1

    result["themes"].sort(key=lambda t: -t["for_count"])
    for t in result["themes"]:
        print(f"\n{t['theme']}")
        print(f"  For: {t['for_count']} of {n} ({', '.join(t['for']) or 'none'})")
        print(f"  Against: {t['against_count']} ({', '.join(t['against']) or 'none'})")
        if t["mixed"]:
            print(f"  Said both: {', '.join(t['mixed'])}. Report what each said, not a side.")
        ev = ", ".join(f"{k}: {v}" for k, v in sorted(t["strongest_evidence"].items(),
                                                       key=lambda kv: EVIDENCE_ORDER.index(kv[0])))
        print(f"  Strongest evidence per supporting participant: {ev or 'none'}")
        if t["segments"]:
            print("  By segment: " + ", ".join(f"{s} {c} of {seg_sizes.get(s, '?')}" for s, c in t["segments"].items()))
        s = t["suggested"]
        print(f"  Suggested concerns: adequacy {s['adequacy']}, coherence {s['coherence']}, "
              f"evidence {s['evidence']}. Relevance: your judgement.")

    print(f"\nCounts are participants, not mentions. n = {n}.")
    print("The suggested concerns assume the finding claims something about participants in general. "
          "A finding scoped to the people who said it (\"two participants...\") needs less. "
          "Every concern is confirmed or changed, with a reason, in the assessments file.")
    if errors:
        print("\nProblems in the coding file:")
        for e in errors:
            print(f"  {e}")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print(f"Written: {os.path.abspath(args.json)}")
    if errors:
        sys.exit(1)


# ---------------------------------------------------------------------------
# confidence


LEVELS = ["High", "Medium", "Low"]
COMPONENTS = ["adequacy", "coherence", "evidence", "relevance"]


def lower(a, b):
    return a if LEVELS.index(a) >= LEVELS.index(b) else b


def finding_level(concerns):
    serious = sum(1 for c in concerns if c == "serious")
    moderate = sum(1 for c in concerns if c == "moderate")
    minor = sum(1 for c in concerns if c == "minor")
    if serious:
        return "Low", f"{serious} serious concern(s)"
    if moderate >= 2:
        return "Low", f"{moderate} moderate concerns"
    if moderate == 1:
        return "Medium", "1 moderate concern"
    if minor >= 3:
        return "Medium", f"{minor} minor concerns"
    if minor:
        return "High", f"{minor} minor concern(s), not enough to lower it"
    return "High", "no concerns"


def apply_override(item, level, errors, label):
    ov = item.get("override")
    if not ov:
        return level, ""
    if ov not in LEVELS:
        errors.append(f"{label}: override {ov!r} is not High, Medium or Low")
        return level, ""
    if not (item.get("override_why") or "").strip():
        errors.append(f"{label}: an override needs override_why")
        return level, ""
    if LEVELS.index(ov) < LEVELS.index(level):
        errors.append(f"{label}: override can only lower the level, not raise it from {level} to {ov}")
        return level, ""
    return ov, f"lowered to {ov} by judgement: {item['override_why']}"


def cmd_confidence(args):
    with open(args.file, encoding="utf-8") as fh:
        data = json.load(fh)
    errors = []
    levels = {}
    out = {"findings": [], "opportunities": [], "recommendations": []}

    print("Findings")
    for f in data.get("findings", []):
        fid = f.get("id", "?")
        concerns, why = [], []
        for c in COMPONENTS:
            comp = f.get(c)
            if not isinstance(comp, dict):
                errors.append(f"{fid}: {c} is missing")
                continue
            concern = (comp.get("concern") or "").lower()
            if concern not in CONCERNS:
                errors.append(f"{fid}: {c} concern {concern!r} is not one of {', '.join(CONCERNS)}")
                continue
            if concern != "none" and not (comp.get("why") or "").strip():
                errors.append(f"{fid}: {c} has a {concern} concern and no why")
            concerns.append(concern)
            why.append(f"{c} {concern}")
        level, basis = finding_level(concerns)
        level, note = apply_override(f, level, errors, fid)
        levels[fid] = level
        print(f"  {fid} {f.get('title', '')}")
        print(f"     {', '.join(why)} -> {basis} -> {level}" + (f"; {note}" if note else ""))
        out["findings"].append({"id": fid, "level": level, "working": f"{', '.join(why)}: {basis}" + (f"; {note}" if note else "")})

    def from_level(item, label, allowed):
        srcs = item.get("from") or []
        if not srcs:
            kind = "opportunity" if allowed == "F" else "recommendation"
            errors.append(f"{label}: 'from' is empty. Every {kind} comes from at least one "
                          + ("finding" if allowed == "F" else "finding or opportunity"))
            return None, ""
        missing = [s for s in srcs if s not in levels or s[0] not in allowed]
        if missing:
            errors.append(f"{label}: 'from' names {', '.join(missing)}, which is not a known "
                          + ("finding" if allowed == "F" else "finding or opportunity"))
            return None, ""
        lv = "High"
        for s in srcs:
            lv = lower(lv, levels[s])
        return lv, "lowest of " + ", ".join(f"{s} {levels[s]}" for s in srcs)

    print("\nOpportunities")
    for o in data.get("opportunities", []):
        oid = o.get("id", "?")
        lv, basis = from_level(o, oid, "F")
        if lv is None:
            continue
        lv, note = apply_override(o, lv, errors, oid)
        levels[oid] = lv
        print(f"  {oid} {o.get('title', '')}")
        print(f"     {basis} -> {lv}" + (f"; {note}" if note else ""))
        out["opportunities"].append({"id": oid, "level": lv, "working": basis + (f"; {note}" if note else "")})

    print("\nRecommendations")
    for r in data.get("recommendations", []):
        rid = r.get("id", "?")
        if r.get("designer_only"):
            print(f"  {rid} {r.get('title', '')}")
            print("     Not assessed: the designer's own, with no finding behind it.")
            out["recommendations"].append({"id": rid, "level": "Not assessed", "working": "no finding behind it"})
            continue
        lv, basis = from_level(r, rid, "FO")
        if lv is None:
            continue
        shown = (r.get("shown_in_behaviour") or "").strip()
        if shown:
            cap = f"{basis}; not capped, because participants' own behaviour already shows it working: {shown}"
        else:
            capped = lower(lv, "Medium")
            cap = basis + ("; capped at Medium: interviews show the need, not that this answer meets it"
                           if capped != lv else "")
            lv = capped
        lv, note = apply_override(r, lv, errors, rid)
        print(f"  {rid} {r.get('title', '')}")
        print(f"     {cap} -> {lv}" + (f"; {note}" if note else ""))
        out["recommendations"].append({"id": rid, "level": lv, "working": cap + (f"; {note}" if note else "")})

    print("\nRule: start at High. Any serious concern, or two moderate, gives Low. One moderate, or three "
          "minor, gives Medium. An opportunity takes the lowest level of the findings it comes from. A "
          "recommendation takes the lowest of its sources and is capped at Medium unless participants' "
          "own behaviour already shows it working. Judgement can lower a level, with a reason, never raise it.")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2)
        print(f"Written: {os.path.abspath(args.json)}")
    if errors:
        print("\nProblems in the assessments file:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)


# ---------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("columns", help="list columns with a guessed type and the speakers")
    p.add_argument("files", nargs="+")
    p.set_defaults(func=cmd_columns)

    p = sub.add_parser("pseudonymise", help="combine transcripts and rename participants P1, P2 ...")
    p.add_argument("files", nargs="+", help="one or more transcript CSVs")
    p.add_argument("--speaker", required=True, help="column naming who spoke")
    p.add_argument("--text", required=True, help="column holding what they said")
    p.add_argument("--start", help="column holding when the turn started")
    p.add_argument("--end", help="column holding when the turn ended, if there is one")
    p.add_argument("--interview", help="column naming the interview, when one file holds several. "
                                       "Otherwise each file is one interview, named after the file")
    p.add_argument("--interviewer", action="append", required=True,
                   help="a speaker value that is the interviewer (name or label). Repeat for each")
    p.add_argument("--out", required=True, help="combined, pseudonymised CSV to write")
    p.add_argument("--key", required=True, help="private key CSV to write")
    p.set_defaults(func=cmd_pseudonymise)

    p = sub.add_parser("stats", help="length, turns and words per interview")
    p.add_argument("file", help="the pseudonymised transcript")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("prompts", help="list hypothetical or leading interviewer turns")
    p.add_argument("file", help="the pseudonymised transcript")
    p.set_defaults(func=cmd_prompts)

    p = sub.add_parser("quotes", help="check quotes are verbatim, attributed and timed correctly")
    p.add_argument("file", help="the pseudonymised transcript")
    p.add_argument("--quotes", required=True,
                   help='JSON list of {"quote": ..., "participant": ..., "at": optional timestamp}')
    p.set_defaults(func=cmd_quotes)

    p = sub.add_parser("tally", help="participants per theme, with suggested concerns")
    p.add_argument("file", help="coding CSV: participant, theme, evidence, stance, and optionally at, code")
    p.add_argument("--transcripts", help="the pseudonymised transcript, to check every row against it")
    p.add_argument("--participants", type=int, help="total participants, if --transcripts is not given")
    p.add_argument("--segments", help="CSV with participant and segment columns")
    p.add_argument("--json", help="also write the results to this JSON file")
    p.set_defaults(func=cmd_tally)

    p = sub.add_parser("confidence", help="apply the confidence rule and show the working")
    p.add_argument("file", help="assessments JSON")
    p.add_argument("--json", help="also write the levels to this JSON file")
    p.set_defaults(func=cmd_confidence)

    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
