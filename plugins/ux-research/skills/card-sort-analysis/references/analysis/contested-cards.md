# Cards no single group settles

Contested cards are often the most useful finding of a card sort. This file covers how to flag
them, what might cause them, and what to do about each cause.

**Last updated:** 21 October 2026

---

## Why a card is contested

Spencer and Warfel list four reasons disagreement happens: participants did not understand the
content, it fits several areas, there are alternative paths to it, or different types of
participant see it differently. `(verified)` **The data cannot tell these apart.** NN/g suggests
running a few moderated sessions to find out whether a card was hard to place because the label
was unclear or because it genuinely fits several topics. `(verified)`

Nawaz found that the choice of analysis affects contested cards most: "the choice of analysis for
card sorting affects these cards most of all where users do not agree". So a contested card is also
the one most sensitive to your settings. `(verified)`

## What the script flags

**Open and hybrid sorts.** At the chosen cut, a card is listed when it:
- does not join any group at the cut,
- is only weakly similar to its own group (below the cut),
- is within 15 points of another group (its average similarity to the nearest other group is nearly
  as high as to its own), or
- often moves group when participants are resampled (retention under 60%).

**Closed sorts.** A card is listed when no category holds 50% of participants, the runner-up's
interval overlaps the top placement's, or the top placement is held in under 60% of resamples.

**The 15-point margin, the 50% and the 60% are the script's defaults, not evidence-based.** `(convention)`
Other tools use other numbers. UXtweak suggests dropping matches below 50% and re-sorting, and
Nawaz used 60%, but neither is empirically justified. `(verified, as an absence of justification)`
Lamantia flags cards that appear in six or more categories, with thresholds that assume nine
participants. `(verified)`

## What to do, by cause

| If the cause is | Then |
|---|---|
| An unclear label | Reword the card and test it again. |
| It fits several areas | Consider cross-listing it, sparingly, or splitting the concept. |
| Different user groups sort it differently | Analyse the groups separately, if each has enough people (Katsanos et al.). |
| You cannot tell | Run a few moderated sessions or ask where people would look for it, and put the candidate homes into a tree test. |

Notes from a write-up of a talk by Carol Righi, passed on second-hand `(unverified)`: keep
categories distinct and mutually exclusive, avoid a "junk drawer", and cross-link sparingly. Righi
et al. (2013) itself was not read.

## What to say in the report

For each flagged card give:
- the numbers (share in each candidate group, and the interval for a closed sort),
- what the settings were,
- the possible causes, and which one the data cannot rule out,
- a specific follow-up. "Ask three participants where they would look for it and what they expect
  next to it" is better than "investigate".

Do not force a contested card into a group to make the structure look complete. Show it apart, as
the sample report does.

---

## Sources

- Spencer and Warfel, [Card sorting: a definitive guide](https://boxesandarrows.com/card-sorting-a-definitive-guide/) (2004)
- NN/g, [Card Sorting: Uncover Users' Mental Models](https://www.nngroup.com/articles/card-sorting-definition/)
- Nawaz, [A comparison of card-sorting analysis methods](https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf) (2012)
- Katsanos et al., [Card sorting reliability across studies](https://arxiv.org/abs/1903.08644) (2019)
- Lamantia, [Analyzing card sort results with a spreadsheet template](https://boxesandarrows.com/analyzing-card-sort-results-with-a-spreadsheet-template/) (2003)
- UXtweak, [Analysis of Card Sorting Results](https://www.uxtweak.com/card-sorting/results/)

---

## Change log

**21 October 2026.** File created.
