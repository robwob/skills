# Useberry

**UNVERIFIED.** No Useberry help-centre page could be reached, and the product page says nothing
about sort types, analyses or exports. Most of what is below comes from a vendor blog post and from
user feature requests on a feedback board, which could not be fetched directly. **Trust the user's
file and screen over this profile.**

**Checked:** 21 October 2026.

---

## Sort types

Open and closed. Hybrid was not found. `(verified for the blog, which is dated 27 September 2022 and
may be out of date)`

## Views

From a vendor blog post on card sorting updates. `(verified for the blog)`

| Sort | View | What was reported |
|---|---|---|
| Closed | Cards view, categories view | Cards view has sortable columns. |
| Closed | Matrix analysis | The count of times each card went into each preset category, with a percentage toggle. |
| Open | Cards view, categories view | A "Standardize" merge button and an agreement rate on categories. |
| Open | Standardization grid | Counts of cards per standardised category. |
| Open | Similarity matrix | The percentage of respondents who grouped any two cards together. |
| Either | Dendrogram | **Not found.** |

## Export `(unverified)`

**There is no official export documentation.** Two requests on a feedback board were seen only as
search summaries:

- One says the card sort CSV stores **each participant's sort in a single field as nested JSON,**
  mapping each category to a list of card names, and that matching responses to user IDs is tedious.
- The other asks for a symmetrical similarity-matrix export that respects filters, and the requester
  built one with a Python script.

The status of either request is not visible, so the file may have changed.

## Route

**Ask for the export and look at it before deciding.** If a cell holds a whole sort, agree a reading
with the user and write a short throwaway conversion to one row per placement (see
`input-format.md`), showing the first rows of the result before analysing. Otherwise use the image
route. There is no known dendrogram to read, so a computed one is the only one.

## Questions to ask this user

- What does a row of the card sort CSV contain, and can you send one row?
- Is a participant's sort stored in a single cell, and in what format?
- How does the file show an unsorted card?
- Is this an open or a closed sort?

---

## Sources

- Useberry, [Card sorting updates](https://www.useberry.com/blog/card-sorting-updates/) (27 September 2022)
- Useberry feedback board requests (not fetched, snippets only)

---

## Change log

**21 October 2026.** File created, marked unverified.
