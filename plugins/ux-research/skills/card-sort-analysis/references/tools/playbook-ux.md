# Playbook UX

**PROVISIONAL.** Written from the tool's help centre. No export from the tool was available, so the
file layout is not described, and what is said about the export contradicts the user's report in one
place (below). **Trust the user's file over this profile.**

**Checked:** 21 October 2026. Sources are the help-centre pages named at the end, read through a
fetch tool that summarises pages, so quotations are second-hand.

---

## Sort types

Open, closed and hybrid. Maximum 60 cards per study. Participants can create categories in open and
hybrid sorts but cannot add cards. `(verified)`

## Views

A Participants tab and an Analytics tab with five views. `(verified)`

| View | What it shows | How to read it |
|---|---|---|
| Participants | Click a participant to see their categories and the cards in each | Per-person sorts. Use for the cleaning step. |
| Cards | Each card and the categories participants sorted it into | Equivalent to the cards view in the guide. A marketing page adds how often each card went into unique categories. |
| Categories | Each category and its cards. Open and hybrid sorts can merge categories here | Merging is a feature of the tool. |
| Merged Matrix | How often cards were sorted into each category. Darker cells mean more participants. A Count / Percentage toggle | Cards down the side and categories across the top (from a glossary, `(unverified)`). The guide calls it the merged matrix. |
| Similarity Matrix | How often pairs of cards were grouped together. Darker means higher, white means 0 participants, hovering shows the percentage | **Values appear on hover, so a screenshot shows shading, not numbers.** White meaning 0 is `(unverified)`. |
| Dendrogram | Cards listed on the left, related cards join closer to the Y axis | **Method, linkage, distance measure and axis meaning are not documented.** |

## Export

- The documented export is a single **Excel** file per project, from the project's three-dot menu.
  `(verified)`
- **The user reports a CSV that covers only part of the analysis, with the similarity matrix and
  dendrogram available only as screenshots.** The docs mention no CSV, no PDF and no image export,
  and say nothing about what the file contains. The user's report wins, and the two may differ
  because of the export format or the documentation's age.
- **Not documented:** sheets or columns, what a row represents, how categories and unsorted cards
  appear, participant ID format, whether any matrix or dendrogram data is included.
- Whether card sort analytics can be put into a Report is not documented.
- An Enterprise API with MCP is advertised, with a published scope of videos, transcripts and
  insights. Card sort data is not mentioned. `(verified)`

## Route

**Combined by default.**
1. Ask for the export (or its headers and first rows) and map it. If it holds one row per card
   placement per participant, the data route can compute the cards view, the categories view and
   the similarity matrix.
2. **If the matrix can be recomputed, compute it and compare it with the screenshot,** and report
   any cell that differs by more than a shading band. A difference may mean the tool merges
   category names before building its matrix, which is not documented.
3. If the export cannot give per-participant sorts, use it for the views it covers and read the
   matrix and dendrogram from screenshots (`image-route.md`).

## Questions to ask this user

- What is the export's format and its headers? A few rows will do.
- How does the file show a card a participant left unsorted?
- Does the matrix in the tool change when you merge categories? (Unknown.)
- Is there a legend or axis label on the dendrogram, and does it show a percentage or a distance?
- Can you hover the cells that matter and send the values?

## Known unknowns

The clustering method and distance measure, whether the matrix reacts to merging, the file layout,
unsorted-card handling, and current plan gating for card sorting and exports (the pricing page and a
2021 help article disagree). Whether a tool hides the dendrogram's method is itself a finding to
report.

---

## Sources

- Playbook UX, [Analyzing your card sort](https://help.playbookux.com/en/articles/5366057-analyzing-your-card-sort) (4 April 2025)
- Playbook UX, [Export results](http://help.playbookux.com/en/articles/4157474-export-results) (5 April 2025)
- Playbook UX, [Setting up a card sort](http://help.playbookux.com/en/articles/5354087-setting-up-a-card-sort) (13 April 2026)
- Playbook UX, [What is card sorting](https://help.playbookux.com/en/articles/5366048-what-is-card-sorting-a-guide-to-card-sorting) (7 April 2025)
- Playbook UX, [card sorting page](https://playbookux.com/card-sorting) and [AI page](https://www.playbookux.com/ai/)

---

## Change log

**21 October 2026.** File created, marked provisional. Documentation describes the views but not the
export contents or the clustering method, and mentions only an Excel export where the user reports a
CSV.
