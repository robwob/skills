# Confidence

How `interview-analysis` grades every finding, opportunity and recommendation **High**, **Medium**
or **Low**, and how it shows its working.

**Last updated:** 17 November 2026

Tags as in `analysis.md`.

---

## Where the method comes from

**GRADE-CERQual** (Confidence in the Evidence from Reviews of Qualitative research) is the most
developed published method for saying how much confidence to place in a qualitative finding.
`(unverified)` What the library takes from it, through search summaries of the 2018 series in
*Implementation Science* 13 (Suppl 1):

- Confidence is "an assessment of the extent to which a review finding is a reasonable
  representation of the phenomenon of interest". Lewin et al., 2018, paper 2. `(unverified)`
- It is judged **for each finding separately**, after the findings are drafted. `(unverified)`
- It rests on four components: **methodological limitations**, **coherence**, **adequacy of data**
  and **relevance**, each judged as no or very minor, minor, moderate or serious concerns.
  `(unverified)`
- Every finding starts at high confidence and is graded down for important concerns. `(unverified)`,
  through a summary by the Norwegian Institute of Public Health.
- Four levels: high, moderate, low and very low, meaning it is highly likely, likely, possible, or
  not clear that the finding represents the phenomenon. `(unverified)`, wording from a table citing
  Lewin et al. (2015), not checked against the 2018 paper.
- Coherence is "how clear and cogent the fit is between the data ... and a review finding", and is
  in doubt where the data are "contradictory, ambiguous or incomplete" or "competing theories
  exist". Colvin et al., 2018, paper 4. `(unverified)`
- Relevance is how far the data behind a finding apply "to the context (perspective or population,
  phenomenon of interest, setting)" the finding is about. Noyes et al., 2018, paper 6.
  `(unverified)`
- Adequacy covers the richness and the quantity of the data behind a finding. Glenton et al., 2018,
  paper 5. `(unverified)`

**How this library differs, and why.** `(derived)`

- CERQual grades findings **synthesised from several studies**. Here the "studies" are interviews in
  one round, so "methodological limitations" becomes **how the evidence was obtained**: the evidence
  type and whether the question led it.
- CERQual is a structured judgement, not a formula. This library adds a fixed rule (below) so two
  runs on the same coding give the same level and the working can be checked. Judgement can still
  **lower** a level, with a reason. It cannot raise one.
- Three levels, not four, to match `card-sort-analysis` and the designer's choice. CERQual's "very
  low" folds into Low.

**Confidence is not frequency.** "4 of 6" is evidence for a finding, not the confidence in it. A
finding seen in 2 of 6, each from a specific occasion with no counter-case, can be more trustworthy
than one seen in 5 of 6 from opinions. `(derived)`, as `card-sort-analysis` says of agreement.

---

## The four components

Each is judged **none**, **minor**, **moderate** or **serious** concerns, with a one-line reason
for anything above none. `check.py tally` suggests the first three from the coding; every
suggestion is confirmed or changed by the analyst.

### 1. Adequacy: is there enough data, and is it rich enough?

| Concern | Suggested when `(derived)` |
|---|---|
| none | Supported by at least half the participants it is about, and at least 2 |
| minor | 3 or more, but under half |
| moderate | 2 participants |
| serious | 1 participant |

**Scope changes it.** These lines assume the finding claims something about participants in
general. A finding scoped to what it rests on ("one participant's smart meter went offline for two
months and nobody told them") has adequate data for that claim. Lower the concern and say why. A
one-off that matters is reported, at its true count, not inflated to look adequate. `(derived)`

Thin data counts here too: a theme supported only by passing mentions, with no detail, is a minor
concern even at a good count. `(unverified)`, CERQual's richness criterion.

### 2. Coherence: does the data fit the finding cleanly?

| Concern | Suggested when `(derived)` |
|---|---|
| none | No participant against |
| minor | Against by up to a third as many as support it |
| moderate | Against by more than a third as many, but fewer than support it |
| serious | As many or more against as for: it is a split, report it as one |

Also a concern, by judgement: the excerpts are ambiguous, or another explanation fits them as well.
`(unverified)`, CERQual coherence. **A counter-case that comes from a different context is a
relevance question, not a coherence one**, so narrow the finding's scope rather than lowering
coherence. `(derived)`

### 3. Evidence: how was it obtained?

| Concern | Suggested when `(derived)` |
|---|---|
| none | At least half the supporting participants described a specific occasion, or showed it |
| minor | At least one did, but under half |
| moderate | None did, but some described a general habit |
| serious | Only opinions or hypotheticals |

Each participant counts once, at their strongest evidence type (`analysis.md`, Evidence types).
Also a concern, by judgement: support that came in answer to leading or hypothetical questions, or
from interviews where the interviewer did most of the talking (`check.py prompts`, `stats`).

### 4. Relevance: do the participants behind it match who the finding is about?

Always by judgement. `tally --segments` shows which segments the support comes from.

- **none:** the support comes from the people the finding is about, in the setting it is about.
- **minor:** partly from a different setting or segment, or one segment is thinly represented.
- **moderate:** the finding is about everyone and the support comes from one segment of several.
- **serious:** the support comes from people the finding is not about (a pilot, a colleague, the
  wrong audience).

Often the fix is to scope the finding to the segment that supports it, which removes the concern.
`(derived)`

---

## The rule

`(derived)`, modelled on CERQual's start-high-and-grade-down.

**Findings**

| Concerns across the four components | Level |
|---|---|
| Any serious | Low |
| Two or more moderate | Low |
| One moderate | Medium |
| Three or more minor | Medium |
| Otherwise | High |

**Opportunities** take the **lowest** level of the findings they come from. An opportunity is only
as sound as the weakest finding it needs. `(derived)`

**Recommendations** take the lowest level of their sources, and are **capped at Medium**, because
interviews show a need, not that a particular answer meets it. `(derived)`, from the sources in
`analysis.md` on predictions, and from Gilad's Confidence Meter, which ranks opinions and anecdotes
well below tests and experiments as evidence that an idea will work. `(unverified)`

**One exception to the cap:** participants' own behaviour already shows the recommended thing
working. P5 already photographs the meter and a photo settled a dispute in one email, so "accept a
meter photo with the reading" is not a prediction. Cite the occasions. The mechanism must be the
same one the recommendation proposes, not a similar one. `(derived)`

**A designer's own recommendation with no finding behind it** is recorded as given and marked "not
assessed". Say once that no finding supports it. `(house)`, from `usability-test-analysis`.

**Judgement can lower any level** (a lost recording, a doubtful transcript, a key quote that needs
checking against the recording), with the reason written down. It never raises one. `(derived)`

---

## How it reads in the report

Every graded item carries its level and its basis in one line, plain enough for someone who has
not read this file:

> **Confidence: High.** 4 of 6 participants, all describing a specific occasion. One counter-case
> (P6), who is on a smart meter and fixed payments, so the finding is scoped to manual readers.

> **Confidence: Medium.** From O1 (Medium). Interviews show the need, not that this change meets it.
> A usability test of the reminder settings would raise it.

Every Medium or Low recommendation names **what would raise its confidence**: usually a usability
test, a prototype test or a measure of how common the need is (a survey or analytics). `(derived)`

The appendix lists every component judgement with its reason, or the `check.py confidence` output.

---

## Change log

**17 November 2026.** File created. Components and the start-high approach adapted from
GRADE-CERQual, reached through search summaries; the session could not fetch the papers. The rule,
the three levels, the scope adjustment and the recommendation cap are this library's.
