# Closed and hybrid sorts

Analysis when the researcher supplied the categories, fully (closed) or in part (hybrid).

**Last updated:** 21 October 2026

---

## Closed sorts

**What fits.** Placement agreement: for each card, the share of participants who put it in each
category, with a confidence interval. Tools call the views a results matrix and a popular
placements matrix. `(verified)`

**What does not fit.** A dendrogram or similarity matrix. Optimal Workshop and UXtweak both leave
dendrograms out of closed sorts, because predefined categories bias the result: high agreement may
reflect your labels, not how people think. `(verified)` The script does not compute them for
`--sort-type closed`.

**What it shows and does not.** A closed sort tests how well a set of categories holds up against
how people place cards. NN/g says closed sorts are mainly for validation, and that **tree testing
is usually the better choice for evaluating an existing structure.** `(verified)`

## What the script reports

- **Top placement per card,** its share of the participants who sorted the card, and the 95% Wilson
  interval. MeasuringU's worked example: 32 of 70 gives roughly 35% to 58% (the script's Wilson
  method gives 34.6% to 57.3%, within a point, and the source does not say which interval it
  used). `(verified)`
- **The runner-up** and its share. Sauro: "Items are almost always associated with multiple
  groups", so report the top few placements. `(verified)`
- **A results matrix** of counts per card and category.
- **Stability:** the share of resamples of participants in which the card keeps its top category.
- **Cards no single category settles.** A card is listed when no category holds 50% of
  participants, when the runner-up's 95% interval overlaps the top placement's (a conservative check
  that the top is clearly ahead), or when its top placement is held in under 60% of resamples. The
  50% and 60% figures are the script's defaults, not evidence-based. `(convention)`

**The categories view is different for a closed sort.** The open-sort agreement figure is not used,
because a few misplaced cards drag it down without saying anything about the category. The script
shows the cards each category is the top placement for, and the average share those cards get.

## Chance-corrected agreement

Fleiss' kappa has been used in card sort studies (one review lists seven), and Martin and Macias
implemented it `(verified)`. **No card-sort-specific validation of kappa or Krippendorff's alpha
was found,** so the script does not compute them `(verified, as an absence)`. Do not add one on the
fly.

## Confidence intervals and what to say

- Put the interval next to every share. A share without its number of participants and its interval
  is not reportable.
- MeasuringU's test of whether you have enough people: would the decision change at either end of
  the interval? `(verified)`
- Sample size for precision on one placement (95% confidence, 50% agreement): about 93 participants
  for plus or minus 10 points, about 193 for 7 points. `(verified, MeasuringU)` Most card sorts
  are far smaller, so the intervals will be wide, and saying so is the honest result.

## Hybrid sorts

Participants can create categories as well as use the supplied ones. The open-sort analysis applies,
with a note.

- **Predefined categories can anchor what participants create.** Lyssna (a vendor) says so, and NN/g
  generally recommends against hybrid sorts for the same reason, suggesting them only when you are
  confident about one or two categories. `(verified)`
- Optimal Workshop warns that predefined labels inflate agreement in closed sorts. That the same
  applies to the predefined part of a hybrid sort is an inference. `(unverified)`
- Mark which categories were preset with a `category_preset` column. The script then lists them,
  shows each category's origin, and notes the anchoring risk.
- Review the participant-created groups separately from the preset ones, and standardise only the
  participant-created names.

---

## Sources

- NN/g, [Card Sorting: Uncover Users' Mental Models](https://www.nngroup.com/articles/card-sorting-definition/)
- Optimal Workshop, [Interpret dendrograms](https://support.optimalworkshop.com/en/articles/2626862-interpret-dendrograms-for-open-and-hybrid-card-sorts) and [the results matrix](https://support.optimalworkshop.com/en/articles/2626942-interpret-the-results-matrix-for-closed-card-sorts)
- UXtweak, [Results matrix](https://www.uxtweak.com/help/card-sorting-results/analysis-results-matrix/) and [popular placements matrix](https://www.uxtweak.com/help/card-sorting-results/analysis-popular-placements-matrix/)
- MeasuringU, [Card sorting](https://measuringu.com/card-sorting/) and [Card sorting for IA](https://measuringu.com/card-sorting-ia/)
- Lyssna, [Create a hybrid card sort task](https://help.lyssna.com/en/articles/14113188-create-a-hybrid-card-sort-task)

---

## Change log

**21 October 2026.** File created. Contested-card rule for closed sorts uses interval overlap, not a
fixed margin, after the first version flagged nothing on a sample where a third of participants
disagreed.
