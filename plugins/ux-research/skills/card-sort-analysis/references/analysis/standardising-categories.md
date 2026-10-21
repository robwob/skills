# Standardising category names

Merging the names people gave their groups, in open and hybrid sorts, and the agreement figure
that goes with it.

**Last updated:** 21 October 2026

---

## Merge by contents, not by name

People rarely use identical words. "Loans", "Books" and "Borrowing" may be one idea, and "What's on"
may sound like "Events" while holding opening hours.

- Optimal Workshop: "Multiple participants may have created the same category label, but what lies
  beneath could be a very different story."
- Fincher and Tenenberg (2005), describing Deibel et al.: participants using labels like "difficult"
  or "hard" may mean quite different things, with little similarity between the cards they put
  there. `(verified for the editorial, Deibel's own paper not read)`
- Spencer and Warfel: if a participant changed a card's label, record the new label and keep the old
  one in brackets.

## Procedure

1. List the names with `--list-categories`. Note how many participants used each.
2. **For each candidate merge, look at the cards inside each name,** not only the name. Two names
   with overlapping cards are candidates. Two names that sound alike but hold different cards are
   not.
3. Show the user each proposed merge **with the cards each name held,** and let them approve, change
   or reject it.
4. Write the approved merges to a CSV with the columns `raw,standard`. The script warns about any
   entry that matches no category in the data, which usually means a typo.
5. Rerun with `--merge-file`.

Lamantia's procedure, for reference: sort the raw labels alphabetically, strip common prefixes,
cluster by root word, word order or meaning, choose a representative label, add synonyms, then
assign the rest. His warning applies: **if a large share of raw categories stays unique,
participants may hold very different mental models,** and you may need to rethink the card set or
the approach.

## What standardising changes

- **The cards view and the categories view.** Yes.
- **The similarity matrix and the dendrogram.** **No.** They use each participant's own groups, and
  names do not enter them. This is a design decision made when the skill was built `(house)`, and a
  test enforces it. The reasoning: the matrix then records what participants did and cannot be changed
  by the analyst's choices. Published sources describe a similarity matrix as ignoring group names
  (Fincher and Tenenberg on Martine and Rugg, Hudson).
- **An optional later step:** treating a merge as redefining groups, so a participant who split one
  idea across two names is credited with one group. It makes the matrix depend on the analyst's
  choices. **Offer it only after the user has read what participants actually did, and only if they
  want it.** The skill does not do it by default.

**Unknown for the tools.** Optimal Workshop says its "filtered" exports reflect standardised
categories. Whether a tool's own matrix changes when categories are merged is not documented for
Playbook UX. A matrix from a tool and the one computed here could differ for that reason, and the
report should say so if the user has merged names in their tool.

## Agreement

For a standardised category the script reports the mean, across the unique cards in it, of the share
of that category's participants who put each card there:

    agreement = sum(participants who placed card k there) / (unique cards x participants who used the category)

This is Kuric, Demcak and Krajcovic's definition. `(verified for the formula, unverified as an exact
match to any tool's own figure)` UXtweak describes its version as "the average of the percentages
of respondents who placed each unique card into the original categories", with a worked example of
(100 + 50 + 50) / 3 = 66. Maze's per-card agreement rate divides by all participants instead.
Optimal Workshop's formula is not published `(verified, as an absence)`.

**Bands are conventions.** UXtweak: 80% and above great, 60% and above good, below 60% bad.
Optimal Workshop treats above 60% as generally worth keeping. No source gives evidence for any of
these cut-offs `(convention)`. Report them as vendor conventions, never as findings.

**A category used by one participant has an agreement of 100% and means nothing.** Say so when it
appears in the table.

## No automatic merging

Merging is manual in every tool examined. Lyssna merges only exact spellings, ignoring case, and
leaves typos for you. No validated text-similarity or embedding method for card sort labels was
found `(verified, as an absence)`. The skill proposes merges for the user to approve and does not
merge on its own.

---

## Sources

- Optimal Workshop, [Understand and standardize categories](https://support.optimalworkshop.com/en/articles/2626879-understand-and-standardize-categories)
- UXtweak, [Categories analysis](https://www.uxtweak.com/help/card-sorting-results/analysis-categories/)
- Lamantia, [Analyzing card sort results with a spreadsheet template](https://boxesandarrows.com/analyzing-card-sort-results-with-a-spreadsheet-template/) (2003)
- Spencer and Warfel, [Card sorting: a definitive guide](https://boxesandarrows.com/card-sorting-a-definitive-guide/) (2004)
- Fincher and Tenenberg, [Making sense of card sorting data](https://faculty.washington.edu/jtenenbg/publications/fincherMakingSenseOfCardSorting-expSys2005.pdf) (2005)
- Kuric, Demcak and Krajcovic, [Card sorting with random subsets of cards](https://arxiv.org/abs/2509.03232)
- Lyssna, [Create an open card sort task](https://help.lyssna.com/en/articles/6613353-create-an-open-card-sort-task)

---

## Change log

**21 October 2026.** File created. Records the decision that standardising names does not change the
similarity matrix, and that treating merges as redefining groups is an optional later step.
