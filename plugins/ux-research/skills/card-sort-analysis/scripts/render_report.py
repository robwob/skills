#!/usr/bin/env python3
"""Render the two-layer card sort report as one self-contained HTML file.

Inputs:
  --findings FILE   the written findings (JSON, see references/reporting.md)
  --results FILE    results.json from analyse.py (optional: an image-route
                    study has no computed results)
  --out FILE        where to write the HTML

Layer 1 is what a stakeholder reads: the proposed structure, findings,
contested cards, recommendations tagged with confidence and basis, and what
the study cannot tell you. Layer 2 is the evidence behind it.

Uses only the standard library. Fonts, styles and the dendrogram are inline,
so the file opens anywhere without a network.
"""
from __future__ import annotations

import argparse
import base64
import datetime
import html
import json
import math
import mimetypes
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(os.path.dirname(HERE), "templates", "report.html")

CONFIDENCE = ("High", "Medium", "Low")
BASIS = {
    "computed": "computed from the data",
    "screenshot": "read from a screenshot, confirmed by you",
    "judgement": "researcher's judgement",
}
GUIDE = "guide/how-to-analyse-card-sort-results.md"
IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg",
               ".jpeg": "image/jpeg", ".webp": "image/webp",
               ".gif": "image/gif"}
MAX_IMAGE_BYTES = 3 * 1024 * 1024

DEFAULT_LIMITS = [
    "A card sort gives candidate groupings and labels, not a validated "
    "structure. Test the structure you propose with a tree test before "
    "treating it as settled.",
    "It shows how people group content, not whether they can find it.",
    "Participants make one level of groups, so it says nothing about depth "
    "or subcategories.",
    "Cards are isolated labels, with no surrounding content or links, so "
    "behaviour in context is not covered.",
    "It shows what was grouped, not why. An unmoderated sort cannot tell "
    "an unclear label from a card that fits several areas.",
]

_dash_changes = 0


class ReportError(Exception):
    pass


def clean(text):
    """No em dashes in anything generated. Counts what it had to change."""
    global _dash_changes
    text = str(text)
    out = re.sub(r"\s*\u2014\s*", ", ", text)
    out = re.sub(r"(\d)\s*\u2013\s*(\d)", r"\1 to \2", out)
    out = out.replace("\u2013", "-")
    if out != text:
        _dash_changes += 1
    return out


def esc(text):
    return html.escape(clean(text), quote=True)


def pct(x):
    return int(math.floor(x * 100 + 0.5))


def chip(text, low=False):
    cls = "chip lowconf" if low else "chip"
    return '<span class="%s">%s</span>' % (cls, esc(text))


def confidence_chips(confidence, basis):
    chips = []
    if confidence:
        chips.append(chip("Confidence: %s" % confidence,
                          low=(confidence == "Low")))
    if basis:
        chips.append(chip("Basis: %s" % BASIS[basis],
                          low=(basis == "screenshot")))
    return '<div class="chips">%s</div>' % "".join(chips) if chips else ""


def check_item(item, where):
    conf = item.get("confidence")
    if conf is not None and conf not in CONFIDENCE:
        raise ReportError("%s: confidence must be one of %s, got '%s'." % (
            where, ", ".join(CONFIDENCE), conf))
    basis = item.get("basis")
    if basis is not None and basis not in BASIS:
        raise ReportError("%s: basis must be one of %s, got '%s'." % (
            where, ", ".join(BASIS), basis))


def table(headers, rows, caption=None, num_cols=()):
    out = ['<div class="tablewrap"><table>']
    if caption:
        out.append("<caption>%s</caption>" % esc(caption))
    out.append("<thead><tr>%s</tr></thead>" % "".join(
        '<th scope="col">%s</th>' % esc(h) for h in headers))
    out.append("<tbody>")
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            cls = ' class="num"' if i in num_cols else ""
            cells.append("<td%s>%s</td>" % (cls, esc(c)))
        out.append("<tr>%s</tr>" % "".join(cells))
    out.append("</tbody></table></div>")
    return "".join(out)


def heat_colour(v):
    """Single hue, lightness falls as the value rises (greyscale-safe)."""
    light = 97 - 0.69 * v
    text = "#14171a" if light > 55 else "#ffffff"
    return "hsl(215,70%%,%.1f%%)" % light, text


def heatmap(cards, values, caption, approximate=False):
    """approximate=True prefixes every number with ~ so shading read from a
    screenshot is never mistaken for a printed value."""
    mark = "~" if approximate else ""
    out = ['<div class="tablewrap"><table class="heat">',
           "<caption>%s</caption>" % esc(caption), "<thead><tr><th></th>"]
    for c in cards:
        out.append('<th scope="col" class="col"><span>%s</span></th>'
                   % esc(c))
    out.append("</tr></thead><tbody>")
    for i, c in enumerate(cards):
        out.append('<tr><th scope="row">%s</th>' % esc(c))
        for j in range(len(cards)):
            v = values[i][j]
            if i == j:
                out.append('<td class="self">%s</td>' % pct(v / 100))
            else:
                bg, fg = heat_colour(v)
                out.append('<td style="background:%s;color:%s">%s%d</td>' % (
                    bg, fg, mark, pct(v / 100)))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    out.append('<div class="legend"><span>0%%</span><span class="ramp" '
               'role="img" aria-label="Scale from light for 0 percent to '
               'dark for 100 percent"></span><span>100%% of participants '
               'grouped the pair together. %s</span></div>' % (
                   "The ~ marks values estimated from shading, not printed "
                   "by the tool." if approximate
                   else "Numbers are printed in every cell."))
    return "".join(out)


def dendrogram_svg(dend, alt):
    cards, Z = dend["cards"], dend["linkage"]
    n = len(cards)
    children = {}
    for k, (a, b, dist, _) in enumerate(Z):
        children[n + k] = (int(a), int(b), 1.0 - float(dist))
    root = n + len(Z) - 1
    order = []

    def walk(node):
        if node < n:
            order.append(node)
        else:
            a, b, _ = children[node]
            walk(a)
            walk(b)
    walk(root)
    y = {leaf: 20 + 22 * i for i, leaf in enumerate(order)}
    sim = {leaf: 1.0 for leaf in range(n)}
    for node, (a, b, s) in children.items():
        sim[node] = s

    def place(node):
        if node < n:
            return y[node]
        a, b, _ = children[node]
        y[node] = (place(a) + place(b)) / 2.0
        return y[node]
    place(root)

    label_w = min(300, int(max(len(c) for c in cards) * 6.6) + 14)
    plot_w = 420
    left, right = label_w + 8, label_w + 8 + plot_w
    height = 20 + 22 * n + 34

    def x(s):
        return left + (1.0 - s) * plot_w

    parts = []
    for node, (a, b, s) in children.items():
        for child in (a, b):
            parts.append('<path class="branch" d="M%.1f %.1f H%.1f"/>' % (
                x(sim[child]), y[child], x(s)))
        parts.append('<path class="branch" d="M%.1f %.1f V%.1f"/>' % (
            x(s), y[a], y[b]))
    for leaf in order:
        parts.append('<text x="%d" y="%.1f" text-anchor="end">%s</text>' % (
            left - 8, y[leaf] + 4, esc(cards[leaf])))
    base = 20 + 22 * n - 8
    parts.append('<line class="axis" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (
        left, base, right, base))
    for t in (100, 80, 60, 40, 20, 0):
        tx = x(t / 100.0)
        parts.append('<line class="axis" x1="%.1f" y1="%d" x2="%.1f" '
                     'y2="%d"/>' % (tx, base, tx, base + 5))
        parts.append('<text class="tick" x="%.1f" y="%d" text-anchor="middle">'
                     '%d%%</text>' % (tx, base + 18, t))
    cut = dend.get("cut_similarity")
    if cut:
        cx = x(cut)
        parts.append('<line class="cut" x1="%.1f" y1="8" x2="%.1f" y2="%d"/>'
                     % (cx, cx, base))
        parts.append('<text x="%.1f" y="%d" text-anchor="middle">cut %d%%'
                     '</text>' % (cx, height - 4, pct(cut)))
    return ('<svg class="dendro" viewBox="0 0 %d %d" role="img" '
            'aria-labelledby="dendro-title dendro-desc">'
            '<title id="dendro-title">Dendrogram of the cards</title>'
            '<desc id="dendro-desc">%s</desc>%s</svg>' % (
                right + 20, height, esc(alt), "".join(parts)))


# ---------------------------------------------------------------- sections

def layer_one(f, res):
    out = ['<span class="layer-label">Layer 1, for the people who decide'
           '</span>']
    out.append('<h2 id="summary">Summary</h2><div class="summary">')
    for line in f["summary"]:
        out.append("<p>%s</p>" % esc(line))
    out.append("</div>")

    structure = f.get("proposed_structure")
    if structure:
        out.append('<h2 id="structure">Proposed structure</h2>')
        out.append('<p class="draft-note">A draft to test, not a finished '
                   'navigation. A card sort gives ideas for groupings, and a '
                   'tree test is the usual next step.</p>')
        for i, g in enumerate(structure):
            check_item(g, "proposed_structure[%d]" % i)
            cards = "".join("<li>%s</li>" % esc(c) for c in g["cards"])
            note = "<p>%s</p>" % esc(g["note"]) if g.get("note") else ""
            out.append('<div class="card"><h3>%s</h3>%s<ul class="cards-list">'
                       '%s</ul>%s</div>' % (
                           esc(g["name"]), note, cards,
                           confidence_chips(g.get("confidence"),
                                            g.get("basis"))))

    findings = f.get("findings")
    if findings:
        out.append('<h2 id="findings">Findings</h2>')
        for i, item in enumerate(findings):
            check_item(item, "findings[%d]" % i)
            out.append('<div class="card"><h3>%s</h3><p>%s</p>%s</div>' % (
                esc(item["headline"]), esc(item["evidence"]),
                confidence_chips(item.get("confidence"), item.get("basis"))))

    out.append('<h2 id="contested">Cards no single group settles</h2>')
    contested = f.get("contested")
    if contested is None and res:
        contested = auto_contested(res)
    if contested:
        out.append(table(
            ["Card", "What the data shows", "What to do"],
            [[c["card"], c["what_the_data_shows"], c["action"]]
             for c in contested]))
        out.append('<p class="howto">The data cannot say whether a card is '
                   'contested because the label is unclear, because it fits '
                   'several areas, or because different users see it '
                   'differently.</p>')
    else:
        out.append("<p>No card was flagged at the settings used.</p>")

    recs = f.get("recommendations")
    if recs:
        out.append('<h2 id="recommendations">Recommendations</h2>')
        for i, r in enumerate(recs):
            check_item(r, "recommendations[%d]" % i)
            out.append('<div class="card"><p>%s</p>%s</div>' % (
                esc(r["text"]),
                confidence_chips(r.get("confidence"), r.get("basis"))))

    out.append('<h2 id="limits">What this study cannot tell you</h2><ul>')
    for line in f.get("limits") or DEFAULT_LIMITS:
        out.append("<li>%s</li>" % esc(line))
    out.append("</ul>")
    if f.get("route") in ("image", "combined"):
        out.append('<div class="notice">Figures read from screenshots carry '
                   'a risk of transcription error and no tool documents how '
                   'its matrix or dendrogram is calculated. They were '
                   'confirmed with you, and findings that rest on them are '
                   'marked lower confidence.</div>')
    if f.get("next_step"):
        out.append("<h3>Next step</h3><p>%s</p>" % esc(f["next_step"]))
    return out


def auto_contested(res):
    rows = []
    for c in res.get("contested", []):
        if not c.get("reasons"):
            continue
        if res.get("sort_type") == "closed":
            if c["top_share"] != c["top_share"]:       # NaN: nobody sorted it
                data = "Nobody sorted this card."
            else:
                data = "%s holds %d%% of participants%s. %s." % (
                    c["top_category"], pct(c["top_share"]),
                    (", with %s at %d%%" % (c["second_category"],
                                            pct(c["second_share"]))
                     if c.get("second_category") else ""), c["reasons"])
        else:
            data = ("%d%% similar to its own group, %d%% to the nearest "
                    "other. %s." % (pct(c["cohesion"]),
                                    pct(c["best_other"]), c["reasons"]))
        rows.append({
            "card": c["card"],
            "what_the_data_shows": data[0].upper() + data[1:],
            "action": "Find out why: ask a few participants where they "
                      "would look for it, or test candidate homes in a "
                      "tree test.",
        })
    return rows


def howto(section):
    return ('<p class="howto">To do this yourself, see %s in <code>%s</code>.'
            "</p>" % (esc(section), esc(GUIDE)))


def load_screenshot(item):
    path = item["path"]
    ext = os.path.splitext(path)[1].lower()
    if ext not in IMAGE_TYPES:
        raise ReportError("Screenshot %s is not a png, jpg, webp or gif."
                          % path)
    try:
        size = os.path.getsize(path)
        if size > MAX_IMAGE_BYTES:
            raise ReportError(
                "Screenshot %s is %.1f MB. Resize it below %d MB so the "
                "report stays small." % (path, size / 1e6,
                                         MAX_IMAGE_BYTES // (1024 * 1024)))
        with open(path, "rb") as fh:
            data = base64.b64encode(fh.read()).decode("ascii")
    except FileNotFoundError:
        raise ReportError("Screenshot not found: %s" % path)
    return "data:%s;base64,%s" % (IMAGE_TYPES[ext], data)


def layer_two(f, res):
    out = ['<span class="layer-label">Layer 2, the evidence</span>']
    settings = (res or {}).get("settings") or f.get("settings") or {}
    if settings:
        out.append('<h2 id="settings">Settings used</h2>')
        out.append('<p class="howto">These change the answer, so they travel '
                   'with it.</p>')
        out.append(table(["Setting", "Value"],
                         [[k.replace("_", " "), v if not isinstance(v, list)
                           else (", ".join(map(str, v)) or "none")]
                          for k, v in settings.items()]))

    if res and res.get("cards"):
        closed = res.get("sort_type") == "closed"
        out.append('<h2 id="cards">Cards</h2>')
        out.append(howto("section 3 (Cards)"))
        if closed:
            rows = [[c["card"], c["sorted_by"], c["top_category"],
                     "%d%%" % pct(c["top_share"]) if c["sorted_by"] else "n/a",
                     "%d%% to %d%%" % (pct(c["ci_low"]), pct(c["ci_high"]))
                     if c["sorted_by"] else "n/a",
                     ("%s %d%%" % (c["second_category"],
                                   pct(c["second_share"]))
                      if c["second_category"] else "none")]
                    for c in res["cards"]]
            out.append(table(["Card", "Sorted by", "Top category", "Share",
                              "95% interval", "Runner-up"], rows,
                             num_cols=(1,)))
        else:
            rows = [[c["card"], c["sorted_by"], c["categories"],
                     c["top_category"],
                     "%d%%" % pct(c["top_share"]) if c["sorted_by"] else "n/a",
                     "%d%% to %d%%" % (pct(c["ci_low"]), pct(c["ci_high"]))
                     if c["sorted_by"] else "n/a"] for c in res["cards"]]
            out.append(table(["Card", "Sorted by", "Categories used",
                              "Top category", "Share", "95% interval"], rows,
                             num_cols=(1, 2)))
        out.append('<p class="howto">Share is of the participants who sorted '
                   'the card. The interval shows how far a share from this '
                   'many people can be trusted.</p>')

    if res and res.get("categories"):
        out.append('<h2 id="categories">Categories</h2>')
        out.append(howto("section 4 (Categories)"))
        if res.get("sort_type") == "closed":
            out.append(table(
                ["Category", "Cards it is top for", "Average share",
                 "Which cards"],
                [[c["category"], len(c["cards"]),
                  "%d%%" % pct(c["mean_share"]) if c["cards"] else "n/a",
                  ", ".join(c["cards"])] for c in res["categories"]],
                num_cols=(1,)))
        else:
            out.append(table(
                ["Category", "Participants", "Unique cards", "Agreement"],
                [[c["category"], c["participants"], c["unique_cards"],
                  "%d%%" % pct(c["agreement"])] for c in res["categories"]],
                num_cols=(1, 2, 3)))
            out.append('<p class="howto">Agreement is a convention, not a '
                       'validated cut-off, and a category used by one '
                       'participant says nothing about agreement.</p>')

    if res and res.get("matrix"):
        m = res["matrix"]
        out.append('<h2 id="matrix">Similarity matrix</h2>')
        out.append(howto("section 6 (Similarity Matrix)"))
        out.append(heatmap(m["order"], m["values_pct"],
                           "Share of participants who put each pair of cards "
                           "in the same group (computed)"))

    if res and res.get("dendrogram"):
        d = res["dendrogram"]
        out.append('<h2 id="dendrogram">Dendrogram</h2>')
        out.append(howto("section 7 (Dendrogram)"))
        out.append('<p>%s linkage, cut at %d%% similarity. Computed from the '
                   'matrix above. A tool\'s own dendrogram may use a '
                   'different method and look different.</p>' % (
                       esc(d["method"].capitalize()),
                       pct(d["cut_similarity"])))
        out.append(dendrogram_svg(
            d, "Tree joining the most similar cards first. A text version "
               "follows."))
        out.append("<details><summary>Text version of the tree</summary>"
                   "<pre>%s</pre></details>" % esc("\n".join(res["tree"])))
        out.append("<h3>Groups at this cut</h3><ul>%s</ul>" % "".join(
            "<li>%s</li>" % esc(", ".join(g)) for g in res["groups"]))
        if res.get("sweep"):
            out.append("<h3>How much the structure moves at other cuts</h3>")
            out.append(table(
                ["Cut", "Groups", "Groups of one card",
                 "Pairs treated the same as at the chosen cut"],
                [["%d%%%s" % (pct(r["cut"]),
                              " (chosen)" if abs(r["cut"] - d["cut_similarity"])
                              < 1e-9 else ""),
                  r["groups"], r["singletons"],
                  "%d%%" % pct(r["agreement_with_chosen"])]
                 for r in res["sweep"]], num_cols=(1, 2, 3)))
        if res.get("comparison"):
            cmp_ = res["comparison"]
            out.append("<h3>The same cut with %s linkage</h3><p>%d%% of card "
                       "pairs are treated the same way.</p><ul>%s</ul>" % (
                           esc(cmp_["method"]), pct(cmp_["agreement"]),
                           "".join("<li>%s</li>" % esc(", ".join(g))
                                   for g in cmp_["groups"])))

    if res and res.get("stability"):
        out.append('<h2 id="stability">Stability</h2>')
        out.append('<p class="howto">Participants resampled with '
                   'replacement and the analysis repeated. Bands follow the '
                   'clusterboot documentation, written for clustering in '
                   'general, not for card sorts.</p>')
        out.append(table(
            ["Group", "Mean Jaccard", "Band"],
            [[", ".join(r["group"]), "%.2f" % r["mean_jaccard"], r["band"]]
             for r in res["stability"]], num_cols=(1,)))

    if res and res.get("participants"):
        out.append('<h2 id="participants">Participants</h2>')
        out.append(howto("section 2 (Participants)"))
        out.append(table(
            ["Participant", "Groups", "Unsorted", "Flags"],
            [[p["participant"], p["groups"], p["unsorted"],
              p["flags"] or "none"] for p in res["participants"]],
            num_cols=(1, 2)))
        out.append('<p class="howto">Flags are prompts to look at a sort, not '
                   'reasons to remove it.</p>')

    t = f.get("transcribed")
    if t:
        out.append('<h2 id="transcribed">Read from your screenshots</h2>')
        out.append('<div class="notice">%s</div>' % esc(
            t.get("note") or "These figures were read from screenshots and "
            "confirmed by you. They carry a risk of transcription error."))
        if t.get("legend"):
            out.append("<p>Legend as confirmed: %s</p>" % esc(t["legend"]))
        if t.get("matrix"):
            approx = bool(t["matrix"].get("approximate"))
            out.append(heatmap(
                t["matrix"]["cards"], t["matrix"]["values_pct"],
                "Similarity matrix as transcribed from your screenshot "
                "(lower confidence than a computed matrix%s)" % (
                    "; values estimated from shading" if approx else ""),
                approximate=approx))
        if t.get("merges"):
            out.append("<h3>Dendrogram joins as transcribed</h3>")
            out.append(table(
                ["Cards joined", "Value shown", "Meaning of the value"],
                [[", ".join(m["members"]), m["value"], m.get("meaning", "")]
                 for m in t["merges"]]))
    shots = f.get("screenshots") or []
    for s in shots:
        src = load_screenshot(s)
        out.append('<figure><img src="%s" alt="%s"><figcaption>%s'
                   "</figcaption></figure>" % (
                       src, esc(s["alt"]), esc(s.get("caption", s["alt"]))))
    return out


def render(findings, results):
    for key in ("title", "study", "summary"):
        if key not in findings:
            raise ReportError("findings.json needs '%s'." % key)
    s = findings["study"]
    for key in ("tool", "sort_type", "participants", "cards", "route"):
        if key not in s:
            raise ReportError("findings.study needs '%s'." % key)
    if s["route"] not in ("data", "image", "combined"):
        raise ReportError("study.route must be data, image or combined.")
    findings = dict(findings)
    findings["route"] = s["route"]

    date = findings.get("date") or datetime.date.today().strftime("%d %B %Y")
    body = ["<h1>%s</h1>" % esc(findings["title"]),
            '<p class="meta">%s sort, %s participants, %s cards. Tool: %s. '
            "Route: %s. %s</p>" % (
                esc(s["sort_type"].capitalize()), esc(s["participants"]),
                esc(s["cards"]), esc(s["tool"]), esc(s["route"]), esc(date))]
    body += layer_one(findings, results)
    body += layer_two(findings, results)
    body.append("<footer>Produced with the card-sort-analysis skill. The "
                "settings used are listed in the evidence section, and "
                "<code>%s</code> explains how each view is calculated."
                "</footer>" % esc(GUIDE))
    with open(TEMPLATE, encoding="utf-8") as fh:
        page = fh.read()
    return (page.replace("{{TITLE}}", esc(findings["title"]))
            .replace("{{BODY}}", "\n".join(body)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--findings", required=True)
    ap.add_argument("--results")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    try:
        with open(args.findings, encoding="utf-8") as fh:
            findings = json.load(fh)
        results = None
        if args.results:
            with open(args.results, encoding="utf-8") as fh:
                results = json.load(fh)
        page = render(findings, results)
    except (ReportError, FileNotFoundError, json.JSONDecodeError) as exc:
        sys.stderr.write("Error: %s\n" % exc)
        return 2
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    if _dash_changes:
        sys.stderr.write("Note: replaced em or en dashes in %d text "
                         "item(s).\n" % _dash_changes)
    print("Report written to %s" % os.path.abspath(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
