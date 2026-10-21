# Lyssna (formerly UsabilityHub)

Agreement and similarity matrices that download as images only, and a whole-test CSV whose card sort
columns are not documented.

**Checked:** 21 October 2026, from the Lyssna help centre. Page dates are given where shown.
Fetched through a tool that summarises pages.

---

## Sort types

Closed, open and hybrid. Limits are 100 cards and 30 categories per task. `(verified, 29 May 2026)`

## Views

| View | Notes |
|---|---|
| Card view (default) | Each card with the categories it went into, and the count and percentage of participants per category. You can filter to the participants who chose a category. |
| Category view | Each category with its cards and the count and percentage per card. |
| Agreement matrix | **Cards are rows, categories are columns, and each cell is a percentage of participants.** The highest score per card is dark green and ties are light blue. In open and hybrid sorts, cards with no agreement go into a "No agreement" category you can reassign by hand. |
| Similarity matrix | Open and hybrid only, not available for closed sorts. Cards are rows and columns, with colour bands at 30% or more, above 0% and 0%. |
| Dendrogram | **Not found.** |
| Per-participant view | **Not found**, apart from participant filters. |

`(verified, 27 March 2026)`. Note that the agreement matrix is **cards by categories,** so it is the
guide's merged matrix, not a pair-by-pair matrix. The colour here is green and blue and **not a
single-hue scale**, so lightness may not read cleanly in greyscale.

## Export

- **The agreement and similarity matrices download only as images.** Heading, legend, size, file
  type and a transparent background can be set, or the image copied to the clipboard. **There is no
  documented data export of either matrix.** `(verified)`
- **CSV, paid plans only.** An "Export as CSV" button opens a modal for what to include. There is
  no bulk export across tests.
- **Whole-test CSV columns, documented:** A start time (UTC), B total duration (ms), C to L
  demographics, M to P device, Q onward the answer and task duration for each task, with tags in
  their own columns. That implies one row per participant, but the page does not say so.
- **How card sort answers are encoded in the CSV, how participant IDs appear, and how unsorted cards
  are recorded: not found.** Custom variables can export identifiers for self-recruited participants.
- PDF and API: not found.

## Route

**Image** for the matrices. Use the **image route** and note that a Lyssna similarity matrix has
three colour bands, so the values are banded by the tool, not just by your reading. For the cards and
categories views, use the CSV after inspecting how the card sort cells are encoded, or transcribe the
card and category views, which print counts and percentages. A computed dendrogram is the only one,
since the tool offers none.

## Questions to ask this user

- Open, closed or hybrid?
- What do the CSV's card sort columns look like (a few cells will do)?
- Can you send the matrix images at the highest resolution the tool offers?

---

## Sources

- Lyssna, [Card sorting tasks](https://help.lyssna.com/en/articles/6613317-card-sorting-tasks) (29 May 2026)
- Lyssna, [Viewing your card sort task results](https://help.lyssna.com/en/articles/6653714-viewing-your-card-sort-task-results) (27 March 2026)
- Lyssna, [Sharing and exporting results to CSV](https://help.lyssna.com/en/articles/4952944-sharing-and-exporting-results-to-csv)
- Lyssna, [Create an open card sort task](https://help.lyssna.com/en/articles/6613353-create-an-open-card-sort-task)

---

## Change log

**21 October 2026.** File created.
