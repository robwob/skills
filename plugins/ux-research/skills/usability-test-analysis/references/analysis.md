# Usability test analysis

The library `usability-test-analysis` reads from. Ratings at small numbers, stated against
observed, task success, severity, coding open text, quote integrity, and what one round supports.

**Last updated:** 16 November 2026

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source, reached through a secondary summary |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's inference |
| `(house)` | The author's standing practice. Not citable, and not overwritten by a source that disagrees. |

**Not read in primary form:** Sauro and Lewis, HFES 2005; Lewis and Sauro, *Journal of Usability
Studies*, 2006 ("When 100% Really Isn't 100%"); Tullis and Albert, *Measuring the User Experience*.
Anything attributed to those is `(unverified)`.

**This library shares ground with `usability-test-plan/references/task-design.md`**, which holds the
fuller treatment of sample size, satisfaction instruments and severity. Each skill carries its own
copy so it works on its own. If one changes, check the other.

---

## House rules

### Corroborate every stated rating against the observed record

A rating is a claim. The check is what the same participant did or said on the same task. Where
they disagree, the disagreement is the finding, not noise to average away. `(house)`

The quantitative support: SUS shares only about 6% of its variance with task performance, so a
stated measure and an observed one are close to independent. `(unverified)`

NN/g on the same point from the other side: in usability testing "what people do is more important"
than what they say. Moran and Rosala, *Accelerating Research with AI*, NN/g, 27 September 2024,
reviewed 21 January 2026. `(verified)`

### Six participants, per segment

The floor for a qualitative round. `(house)` Below it, say so in the limits. Above it, say what the
number buys (below). Never a pass or fail line.

### One round is a step in a sequence

A formative round finds problems and their causes. It does not say how common they are. Name the
round that would, rather than calling the gap a defect. `(house)`

---

## Stated against observed

### What counts as paired evidence

For a rating on task T from participant P, anything else about task T from participant P:

- a recorded outcome (success, gave up, time, misclicks, path)
- their think-aloud transcript for that task
- their follow-up open-text answer for that task
- a moderator's or observer's note

General comments at the end of the session count only where they name the task. `(derived)`

### Classifying

| Result | When |
|---|---|
| **Held** | The evidence is consistent with the rating. A 6 or 7 with a smooth, unremarked completion. A 2 with visible struggle. |
| **Contradicted** | The evidence points the other way. |
| **No paired evidence** | Nothing about that task from that participant. |

Signals that contradict a high ease rating: a backtrack, a restart, a workaround through another part
of the product, a wrong end state, doing the same step twice, uncertainty ("I wasn't sure it had
saved"), effort ("took a while", "eventually"), or giving up. `(derived)`

A low rating with a fast, smooth, unremarked completion is a contradiction too, and usually means
the participant rated something other than the task: the product, the prototype's fidelity, or the
test itself. Say which, if they said so. `(derived)`

### Borderline cases

- **Mild effort with a high rating.** "Found it, but had to scroll a long way" with a 6. Record it
  as contradicted only if the participant's own words describe difficulty. Otherwise held, with the
  remark kept as evidence for a minor finding. Do not upgrade tone into contradiction. `(derived)`
- **The rating is on a different scale from what the words describe.** Someone who calls a task
  "fine" and rates it 4 of 7 may be using the scale differently. Hold it, and note it. `(derived)`
- **Transcript only, no recording.** Words about doing are not doing. Analysing a usability test
  from transcripts alone is "not reliable" (Liu and Moran, *AI-Powered Tools for UX Research*,
  NN/g, 2 July 2023 `(verified)`), and AI cannot "properly 'watch' usability tests" (Moran and
  Rosala, 2024 `(verified)`). So when the only paired evidence is a transcript, say so in the
  limits, and recommend the designer checks the recordings behind every contradiction before
  acting on it.

---

## Rating questions

### Report the distribution first

At six participants one person moves a 7-point mean by up to a whole point. The distribution shows
that; the mean hides it. So the report leads with the full distribution and the median, and gives the
mean for comparison with a benchmark. `(derived)`

Sauro's own view is that the mean is the best average for rating scales at every sample size.
*Best Practices for Using Statistics on Small Sample Sizes*, MeasuringU, 13 August 2013.
`(verified)` The library keeps the mean for that reason and puts the distribution first for the one
above. The two are compatible.

### Benchmarks

| Measure | Benchmark | Source |
|---|---|---|
| SEQ, 7 points, "Overall, how difficult or easy was the task to complete?" | Mean about 5.5 | MeasuringU, *The Evolution of the Single Ease Question*, 6 August 2024, and *There are 70+ UX Metrics*, 2025 `(verified)`. The two pages give the base as "several hundred tasks" and 500 tasks, so state the figure as about 5.5 and give no count. |
| SUS, 10 items | Mean 68 | MeasuringU `(verified, via task-design.md)` |
| UMUX-Lite, 2 items | Converts to a SUS estimate | `task-design.md` |

**Compare with a benchmark only when the question was asked in the benchmark's exact form**: same
wording, same number of points, same endpoint labels. A 5-point "how easy was that?" is not SEQ and
has no 5.5. `(derived)`

**Never use NPS as a usability measure.** It measures loyalty. `(derived)`, with Sauro's criticisms
in `task-design.md`.

### What not to do

- Do not average a set of options that was not asked as a scale (multiple choice, ranking).
- Do not average across different questions to make a single score, unless the instrument defines
  one (SUS does).
- Do not compare ratings collected under think-aloud with ratings collected silently. `(derived)`

---

## Task success

### Levels, not a score

Complete; complete with a minor issue; complete with a major issue; failed, split into **gave up**
and **thought they had finished but had not**. `(unverified)` Tullis and Albert, for the split.

Nielsen warns against assigning numbers to the levels and averaging them, because they are ordinal
labels. *Success Rate: The Simplest Usability Metric*, NN/g, 2001, reviewed 2021. `(verified, via
task-design.md)` Report the count at each level.

### A completion rate at small numbers

If the team wants a rate, give the count and a 95% adjusted-Wald interval, never the point
percentage alone. Sauro: compute a confidence interval "using the adjusted Wald confidence interval.
It is accurate for any sample size." *10 Things To Know About Completion Rates*, MeasuringU,
6 September 2011. `(verified)` His example: 1 of 5 gives roughly 2% to 64%. `(verified)`

`python3 -I scripts/check.py completion 4 6` gives 30% to 91%. Six of six gives 56% to 100%: a
perfect score from six people is consistent with a real rate barely above half.

Without the script, use this table. 95%, generated by the script's own function and rounded to
whole percentages:

| Completed | of 5 | of 6 | of 8 | of 10 |
|---|---|---|---|---|
| all | 51% to 100% | 56% to 100% | 63% to 100% | 68% to 100% |
| all but 1 | 36% to 98% | 42% to 99% | 51% to 100% | 57% to 100% |
| half | n/a | 19% to 81% | 22% to 78% | 24% to 76% |

For any other count, run the script or the formula: add 1.92 to the successes and 3.84 to n, take
that proportion p, and the interval is p ± 1.96 × √(p(1 − p) / (n + 3.84)), clipped to 0% and 100%.

### A self-reported "did you complete it?"

Is a stated measure. It goes through stated against observed, not here. `(derived)`

---

## Numbers from a small round

**Never write a percentage for fewer than 20 participants.** Write "4 of 6". `(derived)` from:

- Budiu, *Why You Cannot Trust Numbers from Qualitative Usability Studies*, NN/g, 23 May 2021:
  "70% of the users are able to complete the task" is "misleading", because "when the sample size in
  a study is small, the measurement error will be big". `(verified)`
- Nielsen's 20 as the floor for a quantitative study. `(verified, via task-design.md)`
- Lewis and Sauro's advice to always adjust a proportion when n is below 20. `(unverified)`

The 20 is the line this library draws from those sources. None of them states it as a reporting rule.

### What a round of six can see

The chance at least one participant meets a problem, from MeasuringU, 2 September 2020
`(verified, via task-design.md)`:

| Problem affects | With 5 | With 18 |
|---|---|---|
| 33% of users | 97% | over 99% |
| 10% of users | 41% | 85% |
| 5% of users | 23% | 61% |

So six sees nearly every problem that affects a third of users and is close to blind to one that
affects one in twenty. Say that in the report's limits. And a problem nobody met is not shown to
be absent.

---

## Severity

Nielsen, *Severity Ratings for Usability Problems*, NN/g, 1 November 1994. `(verified)`

| | |
|---|---|
| **0** | Not a usability problem |
| **1** | Cosmetic only |
| **2** | Minor, low priority |
| **3** | Major, high priority |
| **4** | Catastrophe, fix before release |

Weigh **frequency**, **impact** and **persistence**, and market impact where it applies. Factors to
consider, not a formula: do not multiply them. `(derived)`

**A problem seen once can still be real and severe.** Laubheimer: "If we observe even one person
having a problem that is an exemplar of a known principle, we are able to be reasonably confident
that it is a real problem," while "we still won't be able to say precisely how many people will
encounter that problem." *Data Is More than Numbers*, NN/g, 1 August 2021. `(verified)` So report
the one-off with its count of 1, rate its impact on its merits, and do not inflate its frequency.

---

## Coding open text

There is no published threshold for how many participants a theme needs, and no rule on counting
codes. NN/g's *Thematic Analysis* (17 August 2022, reviewed 2026) gives neither, and asks instead
that themes are tested against the data and, where possible, checked by a second analyst.
`(verified)` So the steps below are this library's. `(derived)`

1. **Read everything before coding anything.**
2. **Code close to the words.** "Looked for edit button on address", not "poor discoverability".
   The abstraction comes at the theme step.
3. **Count participants, not mentions.**
4. **Keep the cases against.** Report a split as a split.
5. **Separate the participant from the moderator.** Moderator prompts and notes are not participant
   data. AI tools have been seen failing to separate them (Liu and Moran, 2023). `(verified)`
6. **Generalise only as far as the evidence.** One participant using a filter is not "users want
   filters". NN/g's own example of an AI tool doing exactly this is in Liu and Moran, 2023.
   `(verified)`

### Observation, finding, interpretation, recommendation

Keep them apart in the report. `(derived)`

- **Observation**: what a participant did or said.
- **Finding**: the pattern across participants, with its count.
- **Interpretation**: why you think it happens. Labelled.
- **Recommendation**: what to change. A judgement, tied to a finding, and agreed with the designer.

---

## Quote integrity

Every quote is the participant's exact words, attributed to the right participant, and checked
against the data before the report is shown. `(house)`

Why it is a rule and not a reminder: NN/g found AI research tools giving quotes with no session,
timestamp or clip to check them against, and observes that "AI systems have a dangerous tendency to
provide incorrect information that sounds plausible" (Liu and Moran, 2023). AI notetakers also
misattribute speakers (Moran and Rosala, 2024). NN/g's advice is to verify every quote and
recommendation against the original data. `(verified)`

Allowed: cutting with "...", fixing a typographic quote mark. Not allowed: correcting grammar,
merging two remarks, smoothing a transcription error without saying so.

---

## Change log

**16 November 2026.** File created, from a Gemini Gem's instructions and the evidence gathered for
this skill. House rules carried over from the research family. Adjusted-Wald interval, the
no-percentage line at 20, the one-off-is-real rule, and quote verification added.
