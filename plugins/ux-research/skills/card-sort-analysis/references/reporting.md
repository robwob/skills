# Reporting

How to write the findings and build the report. Read it before Step 8.

**Last updated:** 21 October 2026

---

## What the evidence says about card sort reports

There is no authoritative template for a card sort report. What exists is vendor guidance, NN/g and
MeasuringU on what the method can and cannot claim, and a few practitioner write-ups. Five points
hold up across them:

- **A card sort produces ideas, not a final structure.** NN/g and Spencer both say so.
- **A dendrogram is not an information architecture.** Spencer warns against using it as the site
  hierarchy, and Hudson says it "is not a taxonomic hierarchy".
- **Report agreement as numbers, preferably with confidence intervals** (MeasuringU).
- **Validate with a tree test** before treating any structure as settled (NN/g).
- **Use single-hue colour scales that change in lightness, print the numbers, and give a table as
  the text alternative** (WCAG 1.4.1 and 1.4.11, Crameri et al. 2020).

**No source tests which format gets read.** A report format here is a judgement. The two-layer HTML
report is: short decision layer first, evidence second, with the tables also saved as CSV. `(derived)`

## Structure

**Layer 1, for the people who decide**
1. **Summary.** Two or three sentences. What was found, the one thing that is unresolved, and that
   the structure is a draft.
2. **Proposed structure,** labelled a draft. Groups with their cards, each with a confidence and a
   basis. Cards no group settles are shown apart, not forced in.
3. **Findings.** Three to five. Each is a headline, the evidence with its numbers, a confidence and a
   basis.
4. **Cards no single group settles.** The card, what the data shows, what to do.
5. **Recommendations.** Each with a confidence and a basis, labelled as judgement where it is.
6. **What this study cannot tell you.** Defaults are supplied. Add to them where the study has
   specific limits (a small sample, one user group, a screenshot route).
7. **Next step.** Usually a tree test, naming what to test.

**Layer 2, the evidence.** The renderer builds it from the results file: settings used, per-card
agreement, categories, the similarity matrix as numbers, the dendrogram with a text version, how the
structure moves at other cuts, stability, participants, and any transcribed screenshots.

## Confidence

Three levels, stated against what would change the decision. `(derived)`, from MeasuringU's test of
whether a decision would change at either end of an interval:

- **High.** Computed from the data, and the decision would be the same at either end of the interval
  and under resampling. For example a group that re-forms in nearly every resample, with every card
  placed there by most participants.
- **Medium.** Computed, but the interval is wide enough that the decision could change, the
  stability is doubtful, or the point is a judgement resting on computed evidence.
- **Low.** Read only from a screenshot, or based on a small or unstable sample, or a judgement with
  thin data behind it.

Do not use a number to stand in for confidence. A percentage of agreement is evidence for a
finding, not the confidence in it.

## Basis

Every item says where it comes from:

| Value | Means |
|---|---|
| `computed` | Calculated from the data by the script |
| `screenshot` | Read from a screenshot and confirmed by the user |
| `judgement` | The researcher's reading, not directly shown by the data |

Keep data, findings and recommendations apart, as NN/g's distinction does. Data is what
participants did. A finding is the pattern in it. A recommendation is what you suggest, and it is
labelled as judgement.

## The findings file

JSON, with these fields. `examples/sample-findings.json` is a full working example.

```json
{
  "title": "Report title",
  "date": "21 October 2026",
  "study": {
    "tool": "Playbook UX",
    "sort_type": "open",
    "participants": 19,
    "cards": 12,
    "route": "data"
  },
  "summary": ["One to three short paragraphs."],
  "proposed_structure": [
    {"name": "Group name", "cards": ["Card A", "Card B"], "note": "Optional.",
     "confidence": "High", "basis": "computed"}
  ],
  "findings": [
    {"headline": "...", "evidence": "...", "confidence": "Medium", "basis": "computed"}
  ],
  "contested": [
    {"card": "...", "what_the_data_shows": "...", "action": "..."}
  ],
  "recommendations": [
    {"text": "...", "confidence": "Medium", "basis": "judgement"}
  ],
  "limits": ["Optional. Replaces the default list."],
  "next_step": "Optional.",
  "transcribed": {},
  "screenshots": []
}
```

**Required:** `title`, `study` (with `tool`, `sort_type`, `participants`, `cards`, `route`) and
`summary`. `route` is `data`, `image` or `combined`. Confidence must be High, Medium or Low, and
basis must be `computed`, `screenshot` or `judgement`. The renderer rejects anything else.

**`contested` can be left out.** The renderer then builds it from the results, but the generic
action it writes is weaker than one you write, so write it where you can.

**`limits` replaces the defaults, so include them.** If you supply your own, keep the five defaults
that still apply and add the study-specific ones.

The `transcribed` and `screenshots` fields are described in `image-route.md`.

## Building it

```
python3 -I scripts/render_report.py --findings findings.json --results analysis/results.json --out report.html
```

Leave `--results` out on the image route. The renderer escapes all text, embeds screenshots, makes
no network requests, and replaces any em or en dash it finds. It tells you when it does.

## What to say about the cut and the method

State, in the findings or in Layer 1, that:

- the cut is a judgement, and give the range of groups across neighbouring cuts
- the dendrogram is average linkage computed from the matrix, and a tool's own dendrogram may differ
- unsorted cards were counted under the stated setting

## Framing the next step

A card sort establishes how people group content. Whether they can find it comes next. Write the
next step as a sequence: this round proposes a structure and names the unresolved cards, the next
round tests it. Do not write the absence of a tree test as a flaw in the card sort. `(house)`

## What not to write

- "The users want X." A card sort shows how a sample grouped cards.
- A structure presented as final.
- A percentage without the number of participants.
- A recommendation without a confidence and a basis.
- A threshold ("above 60% is good") as if it were evidence. It is a vendor convention.

---

## Sources

- NN/g, [Card Sorting: Uncover Users' Mental Models](https://www.nngroup.com/articles/card-sorting-definition/) and [Card Sorting vs. Tree Testing](https://www.nngroup.com/articles/card-sorting-tree-testing-differences/)
- NN/g, [Data vs. Findings vs. Insights](https://www.nngroup.com/articles/data-findings-insights-differences/)
- MeasuringU, [Card sorting](https://measuringu.com/card-sorting/) and [Card sorting for IA](https://measuringu.com/card-sorting-ia/)
- Spencer, interview in UXmatters, [All About Card Sorting](http://www.uxmatters.com/mt/archives/2009/05/all-about-card-sorting-an-interview-with-donna-spencer.php) (2009)
- W3C, [Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), [Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) and [Complex Images](https://www.w3.org/WAI/tutorials/images/complex/)
- Crameri, Shephard and Heron, [The misuse of colour in science communication](https://pmc.ncbi.nlm.nih.gov/articles/PMC7595127) (Nature Communications, 2020)
- ONRR, [Open source card sorting](https://blog.onrr.gov/card-sort/) (2020), the clearest real example found of stating limits and next steps

---

## Change log

**21 October 2026.** File created. Built from a research pass that found no authoritative report
template and no evidence comparing report formats, so the format and the confidence levels are
marked `(derived)`.
