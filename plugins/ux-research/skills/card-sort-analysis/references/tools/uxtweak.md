# UXtweak

The best-documented export of the tools examined, and the one whose layout the skill's input shape
is based on.

**Checked:** 21 October 2026, from the UXtweak help centre. Pages carry no dates. Fetched through a
tool that summarises pages, so quotations are second-hand.

---

## Sort types

Open, hybrid and closed. `(verified)`

## Views

Overview, Respondents, Questionnaire, Cards, Categories, Comments, Standardization Grid, Similarity
Matrix, Dendrogram (open and hybrid), Respondent-Centric Analysis (open and hybrid), Results Matrix
and Popular Placements Matrix (closed). `(verified)`

| View | Notes |
|---|---|
| Respondents | Per respondent: time taken, answered questions, cards sorted (%), include in analysis. A modal shows each person's own sort. |
| Cards | Per card, the categories it went into, with frequency and average position. |
| Categories | Unique cards, agreement and respondents per category. Agreement is "the average of the percentages of respondents who placed each unique card into the original categories". Bands: great 80% and above, good 60% and above, bad below 60%. These are vendor conventions. |
| Standardization grid | How many times each card went into each standardised category, shaded by percentage. |
| Similarity matrix | A percentage per pair, clustered along the diagonal. Clicking a cell shows the shared categories. **The denominator and ordering are not defined.** |
| Dendrogram | Two methods, below. |
| Respondent-Centric Analysis | Whole sorts that others resemble. Pairing overlap of 50% or more counts as a vote by default, and it is configurable. |

**Dendrogram methods.** Actual Agreement Method ("X% of respondents agreed with this exact group",
works best with 30 or more respondents) and the Best Match Method ("X% agreed with parts of this
group", for fewer than 30). The axis: "The higher the branches, the higher the percentage of people
who agree." No settings for the dendrogram are documented. `(verified)`

## Export

- **Raw results CSV, one row per card placement.** Columns: Respondent ID number, Card ID number,
  Card title, Raw category ID number, Raw category title, Standardized category ID number,
  Standardized category title, Order in category. `(verified)`
- **Respondents CSV, one row per respondent.** Columns: Order, Identifier, Started, IP, Device,
  Operating system, Browser, Location, Time taken, Answered questions (percentage), Cards sorted
  (percentage), Categories created, Categories named (percentage). `(verified)`
- **Questionnaire CSV,** one per question type and stage. `(verified)`
- **PDF report.** Sections can include the similarity matrix, dendrogram, RCA and matrices as
  rendered images. **The similarity matrix and dendrogram export only as PDF images, not as data.**
- Options: "Everyone included in analysis" (the default) or "Everyone who completed", and "Apply
  current filters and presets" (on by default). Exports expire after two days.
- **Not documented:** how unsorted cards appear in the raw results (no row, or a blank category),
  and whether the Respondents "Identifier" equals the raw results "Respondent ID number".

## Mapping to the skill's input

| Skill column | UXtweak column |
|---|---|
| `participant_id` | Respondent ID number |
| `card` | Card title |
| `category` | **Raw category title** |
| `order` | Order in category |

Use the raw title as the category, and build a merge file from the raw and standardised titles if the
user wants their UXtweak standardising carried across, after they confirm it. Check how a card left
unsorted appears before analysing.

## Route

**Data** from the raw results CSV. For the tool's own matrix or dendrogram, use the PDF image and
the image route, and cross-check against the computed matrix. A computed dendrogram may differ from
the tool's, because the tool uses the Actual Agreement or Best Match method and the script uses
average linkage by default.

## Questions to ask this user

- Was the export filtered to "everyone included in analysis" or "everyone who completed"?
- Were current filters and presets applied?
- How does the file show a card a respondent left unsorted?
- Which dendrogram method was used, and what is the participant count?

---

## Sources

- UXtweak, [Export tab](https://www.uxtweak.com/help/card-sorting-results/tab-export/)
- UXtweak, [Results overview](https://www.uxtweak.com/help/cardsort-results/overview-of-content)
- UXtweak, [Dendrogram](https://www.uxtweak.com/help/card-sorting-results/analysis-dendrogram/), [similarity matrix](https://www.uxtweak.com/help/card-sorting-results/analysis-similarity-matrix/), [categories](https://www.uxtweak.com/help/card-sorting-results/analysis-categories/) and [respondent-centric analysis](https://www.uxtweak.com/help/card-sorting-results/analysis-rca/)
- UXtweak, [Respondents tab](https://www.uxtweak.com/help/card-sorting-results/tab-respondents/)

---

## Change log

**21 October 2026.** File created.
