# Cleaning the data

Checking each participant's sort before analysing, and who decides what is excluded.

**Last updated:** 21 October 2026

---

## The standing rule

**Flag, never drop.** The skill shows what looks odd and the user decides. Every exclusion is listed
in the report with a reason.

## Why not to drop on a flag

Wolf, Dougherty and Kortemeyer (2012), a physics card sort of 41 participants and 50 cards, found
the largest source of variation was not expertise but whether a person tended to make a few large
groups ("stackers") or many small ones ("spreaders"). Their wording was that card sorting
"most strongly measure[s] how individuals sort". What looks like an outlier may be a legitimate
sorting style, and removing it removes a real perspective.

## What the script flags

| Flag | Meaning |
|---|---|
| everything in one group | One group for all sorted cards. Often a participant who did not engage. |
| every card in its own group | No grouping at all. |
| many more groups than typical | More than twice the median number of groups. |
| N card(s) unsorted | The participant left cards out. |
| vague group name | A name such as "stuff" or "miscellaneous". |
| alignment | The correlation between a participant's pairings and everyone else's. Low means their sort differs from the group's. It is a prompt, not a score. |

**These flags are the script's heuristics, not validated criteria.** The only concrete rules of
thumb found for excluding sorts (number of groups against the average, vague names, unusually short
or long completion time) come from seminar slides of low authority `(unverified)`. No independent
source gives a validated threshold for time, for number of groups, or for anything else
`(verified, as an absence)`. UXtweak lets you include or exclude respondents and filter by
completion time but gives no numbers.

## Completion time

The script does not see time, because most exports do not carry it in the placement file. If the
tool records it, ask the user whether any participants were unusually fast or slow, and treat that
as one more flag for them to judge.

## Process

1. Run the script. Show the participants table with its flags.
2. For each flagged participant, say what the flag is and what it might mean, including the case
   that it is a different sorting style. Where useful, show that person's groups.
3. Ask the user whom to exclude. Do not propose a default.
4. Rerun with `--exclude P3,P7`. The report lists the excluded participants.
5. If a participant was excluded because they put everything in one group, say so in the report, in
   plain words.

## Participants who left cards unsorted

Do not exclude them for that alone. The setting for how unsorted cards count (`singleton` or
`pairwise`) deals with it, and the report states which was used. See
`matrix-and-clustering.md`.

---

## Sources

- Wolf, Dougherty and Kortemeyer, [Empirical card-sorting analysis](https://arxiv.org/abs/1201.6601) (2012)
- UXtweak, [Analysis of Card Sorting Results](https://www.uxtweak.com/card-sorting/results/) and [Respondents tab](https://www.uxtweak.com/help/card-sorting-results/tab-respondents/)
- Blum, card sorting analysis techniques, TU Graz seminar slides (2024), low authority

---

## Change log

**21 October 2026.** File created.
