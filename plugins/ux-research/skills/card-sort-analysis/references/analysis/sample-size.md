# Sample size

What the number of participants supports in a card sort. The sources disagree because they answer
different questions, and the skill never writes a pass or fail line.

**Last updated:** 21 October 2026

---

## The question decides the number

| Question | Figure | Source and status |
|---|---|---|
| How many before the similarity matrix stops changing much? | Correlation with a 168-person result: 5 participants 0.75, 15 participants 0.90, 30 participants 0.95, 60 participants 0.98. Nielsen recommends 15, or about 30 for large projects, and has seen good results with as few as 12. | Nielsen (NN/g, 2004), reanalysing Tullis and Wood (2004). **The original was not available, so second-hand.** `(unverified)` Nielsen's caveats: one study, analysed only quantitatively, and he does not recommend designing an architecture from similarity scores alone. |
| How many for the best estimate of the similarity matrix? | 10 to 15, with minimal gains beyond | Lantz et al. 2019, abstract only `(unverified)` |
| How many before the final structure replicates? | Matrices from different studies agreed (Mantel r 0.61 to 0.93) but structures cut from the dendrograms agreed less (63% to 93%) | Katsanos et al. 2019, 16 to 34 participants per study, tech-savvy sample `(verified)` |
| How many before the dendrogram's groups are stable? | 30 or more for Actual Agreement, fewer than 30 for Best Merge | Optimal Workshop and UXtweak. **Vendor guidance with no cited evidence.** Nawaz's single study of 25 suggests more than 15 and more than 25. `(verified)` |
| How precisely do you need one card's placement? | 10 participants plus or minus 27 points, 30 plus or minus 17, 93 plus or minus 10, 193 plus or minus 7 (95% confidence, 50% agreement) | MeasuringU `(verified)` |
| A general rule of thumb | NN/g: at least 15 for qualitative sorts, 30 to 50 for quantitative. Spencer and Warfel: 7 to 10 individuals, or 5 groups of 3 | `(verified)` |
| A vendor minimum | Maze: 10 unmoderated or 5 moderated | Vendor help page `(verified)` |

Kuric et al.'s bootstrap study found 14 to 25 participants gave a stable similarity matrix
(correlation of 0.90 or more) depending on the study design, but it also found that matrices
agreeing did not guarantee the same themes. `(verified)`

## What it means for the report

- **State the number of participants and which question it can answer.** "19 participants: enough
  for the matrix to be steady by NN/g's reasoning, not enough to pin one card's placement within
  10 points."
- **Say how stable the groups are** (the bootstrap), because a stable matrix does not guarantee a
  stable structure.
- **The house floor of 6 participants for qualitative rounds does not apply here.** It is for
  interviews and usability tests. Card sort sources put the figure at 15 or more, and a sort of 6
  supports almost nothing about structure. `(house)`
- **A small sample is a finding.** With 5 participants a share of 60% has an interval of 23% to 88%.
  Print the interval and let it speak.
- **Never write a threshold** ("enough" or "not enough"). Give the figures and what each supports.
- **If there are several user groups,** each needs enough people to analyse alone.

## The bootstrap warning

The script's stability check resamples participants. With fewer than 10 it warns that the figures
are unreliable, because resampling a handful of people mostly reproduces them. This threshold is the
script's own. `(derived)`

---

## Sources

- NN/g, [Card Sorting: How Many Users to Test](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/) (Nielsen, 2004)
- NN/g, [Card Sorting: Uncover Users' Mental Models](https://www.nngroup.com/articles/card-sorting-definition/)
- Katsanos et al., [Card sorting reliability across studies](https://arxiv.org/abs/1903.08644) (2019)
- Lantz et al., Journal of Classification 36(3) (2019), [abstract](https://ideas.repec.org/a/spr/jclass/v36y2019i3d10.1007_s00357-018-9292-8.html)
- Kuric, Demcak and Krajcovic, [Card sorting with random subsets of cards](https://arxiv.org/abs/2509.03232)
- Nawaz, [A comparison of card-sorting analysis methods](https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf) (2012)
- MeasuringU, [Card sorting](https://measuringu.com/card-sorting/)
- Spencer and Warfel, [Card sorting: a definitive guide](https://boxesandarrows.com/card-sorting-a-definitive-guide/) (2004)
- Maze, [Understanding your card sorting results](https://help.maze.co/hc/en-us/articles/5813625557139-Understanding-your-card-sorting-results)

---

## Change log

**21 October 2026.** File created. The original Tullis and Wood paper was not available, so the
headline figures rest on NN/g's and MeasuringU's accounts of it and are marked unverified.
