# Optimal Workshop (OptimalSort)

The widest set of views, and the least documented export.

**Checked:** 21 October 2026, from the Optimal Workshop support centre and blog, fetched through a
tool that summarises pages. Article dates are given where shown.

---

## Sort types

Open, closed and hybrid. `(verified)`

## Views

| View | Notes |
|---|---|
| Participants | Include, exclude and segment. Abandoned and timed-out participants are excluded by default, and so are participants who put every card in one group or each card in its own group. The article does not describe viewing one participant's sort. |
| Cards | Per card, the number of unique categories it went into and their names. |
| Categories and standardisation | Merge participant labels into standardised categories, each with an agreement score. Above 60% is "generally worth keeping". **The formula is not published.** |
| Standardization grid | Open and hybrid. How many times a card appears in each standardised category. |
| Similarity matrix | Open and hybrid. Hovering shows "the exact number of participants" who paired the cards, but the blog says it shows percentage, so **count or percentage is unclear**. Ordering is "similar to the best merge method". |
| Dendrograms | Open and hybrid only. Actual Agreement Method (best with 30 or more sorts) and Best Merge Method (best with fewer). A draggable agreement threshold line. Further left means higher agreement. |
| Participant-centric analysis | The three most popular whole-sort structures, each with a support count. Two sorts support each other if they share 50% or more of their pairings. |
| Results matrix and popular placements matrix | Closed sorts. Counts of participants per card and category. |
| 3D cluster view | A projection of a distance matrix with a grouping slider. The projection and linkage methods are not named. |

`(verified)` for all of the above, from the help articles.

## Export

- **Spreadsheet downloads, five:** Raw data, Participant data, Standardized data, Similarity Matrix
  data, and SynCaps data (for cluster analysis software). `(verified)`
- **"Uncut"** includes all participants, ignores filters and does **not** reflect standardised
  categories. **"Filtered"** honours segments and exclusions and **does** reflect standardised
  categories. `(verified)`
- **File type, columns, what a row means, and how unsorted cards and participant IDs appear are not
  documented.** The article notes the format does not open in Numbers on a Mac, which hints at
  something other than CSV `(unverified, inference)`. Inspect the actual file.
- **The similarity matrix has a spreadsheet download, so it can be compared with the computed one,
  but its layout is not documented.**
- Dendrograms and participant-centric analysis have no documented export.
- An integration and an MCP page exist on the site and were not opened.

## Route

**Data** from the raw data download, once its headers are inspected and mapped. Note which scope
("uncut" or "filtered") the user downloaded. For the tool's dendrogram, use the image route. **The
Actual Agreement Method cannot be reproduced exactly** because two key steps are undefined, and Best
Merge is only an inferred match to single linkage, so the script's dendrogram will not match either
exactly.

## Questions to ask this user

- Uncut or filtered, and were participants excluded in the tool?
- Which dendrogram method was shown, and how many sorts?
- Does the similarity matrix show a count or a percentage on hover?
- What are the headers of the raw data file, and how does it show an unsorted card?

---

## Sources

- Optimal Workshop, [Download your card sorting results as spreadsheets](https://support.optimalworkshop.com/en/articles/2626934-download-your-card-sorting-results-as-spreadsheets) (26 July 2024)
- Optimal Workshop, [Interpret dendrograms](https://support.optimalworkshop.com/en/articles/2626862-interpret-dendrograms-for-open-and-hybrid-card-sorts) (2 April 2020)
- Optimal Workshop, [Understand the similarity matrix](https://support.optimalworkshop.com/en/articles/2626857-understand-the-similarity-matrix) (5 April 2023) and [blog on analysis features](https://www.optimalworkshop.com/blog/the-powerful-analysis-features-in-optimalsort) (2021)
- Optimal Workshop, [Understand and standardize categories](https://support.optimalworkshop.com/en/articles/2626879-understand-and-standardize-categories), [participant-centric analysis](https://support.optimalworkshop.com/en/articles/2626877-interpret-the-participant-centric-analysis-pca), [segmenting participants](https://support.optimalworkshop.com/en/articles/2626854-segment-your-participant-data-in-card-sorting) and [3D cluster view](https://support.optimalworkshop.com/en/articles/3153259-using-the-3d-cluster-view-3dcv-visualization)

---

## Change log

**21 October 2026.** File created. The export's file type and columns are marked not documented
because no help article states them.
