# The similarity matrix and the dendrogram

How the matrix is computed, how a dendrogram is built from it, and what each can and cannot be
read as. Read it before interpreting either, and before reading one from a screenshot.

**Last updated:** 21 October 2026

---

## The similarity matrix

**Definition.** For a pair of cards, the share of participants who put them in the same group.
Katsanos et al.: "If all participants grouped two content items together then these items have 100%
similarity, whereas if no users placed them together then they have 0% similarity." Distance is
1 minus similarity. `(verified)`

**What it ignores.**
- **Group names.** A dark cell means "often together", not "agreed what the group is called".
- **Nesting.** It records pairs only. Nawaz (2012) shows two different datasets can give the same
  pair counts. `(verified)`
- **Different mental models.** An average can hide two camps of users who sort differently.
- **Order.** Tools reorder the matrix so similar cards sit along a diagonal, so blocks of dark cells
  come from the reordering and not from named categories.

**Unsorted cards.** No source handles them rigorously. Ballpark excludes them from its similarity
metrics `(verified for Ballpark)`. The script offers two settings and reports which was used:
`singleton` (the default: not together with every card, the participant stays in the denominator)
and `pairwise` (the participant is left out of any pair involving the card). Never treat "unsorted"
as a group. `(derived)`

**Comparing two matrices.** Do not use a plain correlation of cells. The cells are not independent,
and Katsanos et al. recommend a Mantel test. `(verified)`

## Reading a tool's matrix

- Ask which way the colour runs. UserTesting's distance matrix counts people who did **not** group
  two cards, so lower means more similar `(unverified)`.
- Ask whether the cell shows a count or a percentage. Optimal Workshop's help article says hovering
  shows "the exact number of participants" while its blog says percentage, so the documentation
  disagrees with itself `(verified, as a conflict)`.
- Maze's formula is (count in pairing x 100) / total participants. `(verified)`
- Lyssna's similarity matrix is open and hybrid only, with colour bands at 30% or more, above 0%,
  and 0%. `(verified)`

## The dendrogram

**What it is.** A tree that joins the most similar cards first, then joins those groups. The script
uses hierarchical clustering on the distance matrix.

**Linkage.** The method for measuring distance between two groups.
- **Average** is the convention. Katsanos et al. say it "usually produces balanced clusters that are
  easier to interpret", citing a data-mining textbook, not a card sort study. `(verified for the
  claim, convention in practice)`
- **No card sort study found shows average linkage beats the others.** Macias (2021) compares
  distance and linkage choices on card sort data and says the choice "greatly" changes the
  dendrogram, but its full text could not be opened `(unverified)`.
- The script offers average, complete and single, and by default shows the same cut under complete
  linkage so the user can see whether the grouping depends on the choice. Single linkage gives
  chained groups and complete gives compact ones.
- Ward is not offered. It needs Euclidean distances, and a transformation that would make it valid
  here is the researcher's inference only `(unverified)`.

**With average linkage, the average pairwise similarity inside each group is at least the cut.**
`(derived)`. It follows because average linkage's join heights never fall as groups grow, and it is
checked by a test. With complete linkage, every pair inside a group is at least the cut.

**Where to cut.** There is no agreed rule, and it changes the structure.
- Katsanos et al.: "Given the same dendrogram, two people can produce different content structures."
  They used the elbow criterion as one objective option. `(verified)`
- Paea et al. (2022) ran six methods for the number of groups on one dataset and got between 2 and
  18. `(verified)`
- Nawaz (2012): one dataset gave 4, 9 or 8 groups depending on the method and the cut. `(verified)`
- Sauro: interpreting dendrogram groups is "notoriously subjective", especially when agreement is
  low. `(verified)`

So the script reports the number of groups across a sweep of cuts and the share of card pairs
treated the same way at each. **The cut is shown as a judgement, never as a finding.**

**It is not a taxonomy.** Hudson: "the hierarchy is based entirely on how often items appeared
together in the same groups, it is not a taxonomic hierarchy", and it takes no notice of group
names. Spencer warns against using it as the site hierarchy. `(verified)`

## The tools' own dendrograms

Optimal Workshop and UXtweak offer two methods, both of which report agreement rather than a
distance. `(verified)`

- **Actual Agreement Method.** "X% of participants agree with this exact grouping." Recommended with
  30 or more sorts.
- **Best Merge Method** (UXtweak: Best Match). "X% agree with parts of this grouping", so it can
  credit a group that no participant made. Recommended with fewer than 30 sorts. Nawaz shows it can
  give identical output for two different datasets.
- **The 30-sort guidance is vendor advice** with no cited evidence. Nawaz's own subsampling suggests
  more than 15 for Best Merge and more than 25 for Actual Agreement, from a single study of 25
  participants. `(verified)`
- Neither tool names a distance measure, and neither lets you choose the algorithm.

**The skill does not reproduce these.** Best Merge is published precisely enough to reimplement
(Paea et al., Appendix 3), and the researcher's inference is that it equals single linkage on the
co-occurrence counts, but that is untested `(unverified)`. Actual Agreement is underspecified: two
key steps are undefined. So **a tool's dendrogram may differ from the one the script draws,** and
the report says so.

**Axis direction differs.** Optimal Workshop: further left is higher agreement. UXtweak: higher
branches mean higher agreement. R-style plots show a distance height where lower means more similar
(an inference from standard practice, not stated in the sources). Playbook UX documents none of
this `(unverified)`.

## Stability

The script resamples participants with replacement 1,000 times, re-clusters each time, and reports
for each group the mean Jaccard overlap with its best match. The bands (0.75 stable, 0.60 to 0.75
doubtful, below 0.60 unstable) come from the `fpc::clusterboot` documentation, written for
clustering in general, not for card sorts `(convention)`. **Applying a bootstrap over participants
to a card sort is the researcher's own method, not a published procedure** `(derived)`. With fewer
than 10 participants the script warns that the figures are unreliable.

Katsanos et al. found that similarity matrices replicated across studies better than the final
structures did (matrices Mantel r 0.61 to 0.93, structures 63% to 93% agreement). So stability of
groups is more informative than the matrix looking steady. `(verified)`

## Not computed

Multidimensional scaling, factor analysis, edit distance between whole sorts, and Optimal
Workshop's participant-centric and UXtweak's respondent-centric analyses. Their exact formulas are
not published. The script reports a per-participant alignment score as a lighter signal.

---

## Sources

- Katsanos et al., [Card sorting reliability across studies](https://arxiv.org/abs/1903.08644) (CHI 2019, late-breaking work)
- Nawaz, [A comparison of card-sorting analysis methods](https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf) (2012)
- Paea et al., Interacting with Computers 33(6) (2022), Appendix 3 for Best Merge
- Optimal Workshop, [Dendrograms](https://support.optimalworkshop.com/en/articles/2626862-interpret-dendrograms-for-open-and-hybrid-card-sorts) and [the similarity matrix](https://support.optimalworkshop.com/en/articles/2626857-understand-the-similarity-matrix)
- UXtweak, [Dendrogram](https://www.uxtweak.com/help/card-sorting-results/analysis-dendrogram/) and [similarity matrix](https://www.uxtweak.com/help/card-sorting-results/analysis-similarity-matrix/)
- Hudson, SynCaps card sorting analysis slides, Syntagm
- MeasuringU, [Card sorting](https://measuringu.com/card-sorting/)
- Fincher and Tenenberg, [Making sense of card sorting data](https://faculty.washington.edu/jtenenbg/publications/fincherMakingSenseOfCardSorting-expSys2005.pdf) (2005)
- Maze, [The similarity matrix](https://help.maze.co/articles/7641589577-what-is-the-similarity-matrix)

---

## Change log

**21 October 2026.** File created. Marks as unverified the linkage comparison (full text not
opened), the Best Merge equivalence and the Ward transformation, and as derived the bootstrap and
the average-linkage guarantee.
