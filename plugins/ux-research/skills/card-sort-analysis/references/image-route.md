# The image route

For a similarity matrix or dendrogram that exists only as a screenshot. Several tools show these
views on screen and export them only as images or PDFs, or not at all. This is a core route, not
a workaround, and it is also the weakest source of numbers in the skill.

**Last updated:** 21 October 2026

---

## What to say first

> "I'll read these from your screenshots. That's less reliable than computing from data, so I'll
> show you what I read and ask you to confirm it, and the findings that rest on it will be marked
> lower confidence."

## What to ask for

- **One screenshot per view**, not a screenshot of the whole page, so labels stay large enough to
  read.
- **The legend or axis** in the frame, or a second screenshot of it. Without the legend the colours
  and the axis have no meaning.
- **All card labels visible.** Labels cut off at the edge cannot be read, and guessing a label is
  worse than asking for another screenshot.
- **A higher resolution or a crop** if text is blurry. Ask rather than guess.
- **A screenshot of the tool's settings for the view,** if it has any (a method, a threshold).

## Before reading anything, ask

1. **What does a darker cell mean?** More often together, or less. Do not assume. UserTesting's
   distance matrix counts people who did not group two cards, so darker or higher can mean less
   similar `(unverified)`.
2. **Are values printed?** Many matrices show shading only, with the value on hover.
3. **For a dendrogram, what does the axis show,** a percentage of agreement or a distance, and which
   direction is more similar?
4. **Which method produced it,** if the tool says. Optimal Workshop and UXtweak offer an Actual
   Agreement and a Best Merge (or Best Match) method with different meanings for the percentage.
   Playbook UX documents none `(unverified)`.

If the user cannot answer 3 or 4, say so in the report and **do not read heights as percentages.**

## Reading each view

### Similarity matrix

- Write the card labels as read, in the order shown. **The tool reorders the matrix** so similar
  cards sit together, so the order is not the original card order.
- If values are printed, transcribe them.
- **If values are not printed, read shading bands, not numbers.** Use four bands: none (white or
  the palest), low, medium, high. Record each cell as a band, and in the findings file use the
  band's midpoint with `"approximate": true` so the report shows it with a tilde (for example
  `~70`). **Never present a shade as an exact percentage.**
- Ask the user to hover the few cells that matter, usually the pairs on either side of a decision,
  and give you the printed values. A handful of exact values beats a whole matrix of estimates.

### Dendrogram

- Transcribe the joins from the leaves upward: which cards or groups join, and the value where
  they join (read off the axis, or printed).
- Mark the value as read from the axis, to the nearest tick. Heights read from an image are
  approximate.
- Note any threshold line the tool draws, and where it sits.
- **Note that the tool's dendrogram may not be average linkage.** Optimal Workshop's and UXtweak's
  methods report agreement rather than distance. You are transcribing the tool's picture, not
  reproducing its method.

## Confirm before using it

Show the transcription back as a table, and ask the user to confirm it. Name the specific cells
or joins that matter most for the decision, and ask them to check those against the screen. Do not
use the table until they agree. If they correct anything, redo the table and show it again.

## Cross-check against the data

If the user also supplied an export that lets the matrix be recomputed, compute it and compare it
with the transcription. Report the cells that differ by more than one band. A disagreement means
either a transcription error or a tool method you have not matched (a different unsorted-card
setting, standardised names changing groups, or a different denominator). Say which you think it is
and why, and do not hide it.

## Confidence

- A finding that rests only on a screenshot is **Low** confidence unless the user supplied printed
  values for the cells it depends on, in which case it may be **Medium**.
- A finding supported by the data and consistent with the screenshot keeps its data confidence.
- Mark the basis as `screenshot` in the findings file.

## What not to do

- Do not infer a number from a colour.
- Do not read a dendrogram height as a percentage without the legend saying so.
- Do not fill a gap in a label or a value because it looks obvious.
- Do not treat two views from different tools as comparable. The same percentage can mean different
  things.
- Do not compare a transcribed matrix to a computed one with a plain correlation as if it were a
  measure of accuracy. Compare the cells the decision rests on.

## What the findings file needs

For the report, add to the findings file:

```json
"transcribed": {
  "legend": "darker means more participants grouped the pair (confirmed by the user)",
  "matrix": {
    "cards": ["A", "B", "C"],
    "values_pct": [[100, 70, 10], [70, 100, 20], [10, 20, 100]],
    "approximate": true
  },
  "merges": [
    {"members": ["A", "B"], "value": "about 70%", "meaning": "as confirmed: share who grouped them together"}
  ],
  "note": "Read from screenshots and confirmed by the user on <date>."
},
"screenshots": [
  {"path": "/path/to/matrix.png", "alt": "Similarity matrix from the tool", "caption": "Similarity matrix, as supplied"}
]
```

`"meaning"` should say "unknown, not interpreted" when the user could not confirm what the value
means. Screenshots are embedded in the report under 3 MB each.

---

## Change log

**21 October 2026.** File created.
