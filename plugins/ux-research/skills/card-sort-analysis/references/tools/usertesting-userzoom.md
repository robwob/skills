# UserTesting and UserZoom

**UNVERIFIED.** Every UserTesting help page returned an access error (HTTP 403) when fetched, so
everything below comes from search snippets and AI summaries of those pages. Treat each claim as
something to confirm with the user, and **trust the user's file and screen over this profile.**

**Checked:** 21 October 2026.

---

## Sort types

UserZoom is now part of UserTesting. The classic experience supports closed, open and hybrid. In the
"new experience" closed is in closed beta, and open and hybrid are "coming soon", so they remain
classic-only. `(unverified)`

## Views `(unverified)`

| View | What was reported |
|---|---|
| Metrics tab | Category merging for open and hybrid sorts. |
| Raw numbers and percentages tables | The percentages table hides results below a threshold, 5% by default. |
| **Distance matrix** | **Each cell is the number of contributors who did NOT group the two cards together, so lower means more similar.** This is the opposite direction to most tools. |
| MDS | A multidimensional scaling view. |
| Dendrogram | Open and closed sort tasks. An agreement-threshold line can be adjusted for open sorts. Images on cards are not shown on the MDS or dendrogram tabs. |

**Whether the percentage or distance on the dendrogram means what it does in other tools is not
confirmed.** Ask what the axis shows.

## Export `(unverified)`

- A **Raw Data report in Excel**, organised per participant, with a `CardSort_Categories` tab listing
  task number, participant ID, category name and the cards placed in each, for open and closed sorts.
  Exact column headers and how unsorted cards appear are not known.
- A search summary said raw numbers, percentages, grouped percentages and the distance matrix can be
  downloaded as XLS or CSV but not the dendrogram or MDS. A second search could not confirm the
  distance matrix download.
- An "Export a Dendrogram" article exists, and its format was not seen. A condensed report in Excel
  or SPSS also exists.
- API: not found.

## Route

**Ask for the export and inspect it.** If it holds categories with their cards per participant, it
can be converted to one row per placement, and the data route can run. Otherwise use the image route.
**Before reading any matrix, confirm the direction:** a high number in the distance matrix means
people did not group the cards together.

## Questions to ask this user

- Is this the classic or the new experience?
- What are the sheets and headers of the raw data file, and how does it show an unsorted card?
- Is the matrix a distance matrix (counting people who did not group) or a similarity one?
- What does the dendrogram's axis show?

## Known unknowns

Everything above is unverified. In particular the file layout, the matrix direction and whether the
matrices download as data.

---

## Sources (reached only through snippets)

- UserTesting help, Card Sort results as a dendrogram (article 360000660158) and the agreement threshold article (360000661158)
- UserTesting help, Card Sort results as data tables (article 360001467357) and the Raw Data report (article 360000663358)
- UserTesting help, card sort analysis (article 11880354198429) and the export section (section 12573402538013)

---

## Change log

**21 October 2026.** File created, marked unverified because the help pages could not be read.
