# Usability test design

The library `usability-test-plan` reads from. Task scenarios, sample size, think-aloud,
moderation, success measures and severity.

**Last updated:** 7 October 2026

---

## This library is in two halves, and they are not equally solid

**Published structure, with formulas, named scales and benchmark numbers:** sample size,
success measures, satisfaction instruments, severity rating. These can be stated with citations
and numbers.

**No taxonomy at all:** task-scenario writing. NN/g, GOV.UK and the academic course pages give
near-identical heuristics, but they share no names, cite no evidence and do not cite each other.
That half is a flat checklist of principles and should not be classified.

One thing sits oddly between them: **think-aloud** has a real named structure, classic versus
relaxed, but it comes from cognitive psychology rather than usability practice, and the evidence
on its effects is genuinely inconsistent.

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source and citation, reached through a secondary summary |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's inference |
| `(house)` | Rob's own standing practice. Not citable, and not to be overwritten by a source that disagrees. |

**Not read in primary form:** Rubin and Chisnell *Handbook of Usability Testing* (2008), Krug
*Rocket Surgery Made Easy* (2010), Tullis and Albert *Measuring the User Experience* (2013),
Faulkner 2003, Schmettow 2012 (abstract only), Ericsson and Simon 1984, Boren and Ramey 2000.
Anything attributed to those is `(unverified)`.

---

## House rules

### Minimum 6 participants

Per audience segment, for qualitative rounds. `(house)` Not 5. The reasoning is the whole of
the **Sample size** section below: Nielsen's 85% is an average, and Faulkner's work shows you do
not get the average, you get one draw from a range that starts at 55%. Six is the hedge.

For two distinct audience groups, 6 each. For three or more, 6 each where the budget allows and
never fewer than 4. `(house)` and `(derived)` on the degradation.

This is a floor for formative work. Summative and quantitative studies need far more, and those
numbers are in the table below.

### Corroborate stated ease against the observed record

A participant who says a task was easy after backtracking twice and taking three minutes has
given you a failed claim, not a satisfaction score. `(house)`

So every post-task rating is reported **next to** the behavioural record for that task, never on
its own. Where they disagree, the disagreement is the finding.

The quantitative support: SUS correlates with task performance at only about 6% shared variance.
`(unverified)` So the stated measure and the observed measure are close to independent, and
treating one as a proxy for the other is unfounded.

**What this requires of a test plan:** the note-taking template has a column for the observed
record and a column for the stated rating, side by side per task, and the analysis compares
them. A plan that collects SEQ or SUS without the paired behavioural record is incomplete.
`(house)`

---

## Task scenarios

No canonical taxonomy. Seven principles, consistent across independent sources.

### Give context and a goal, not instructions

> "Rather than simply ordering test users to 'do X' with no explanation, it's better to situate
> the request within a short scenario that sets the stage for the action and provides a bit of
> explanation and context."

NN/g, Marieke McCloskey, *Write Better Qualitative Usability Tasks*, 12 January 2014.
`(verified)` All three good/bad pairs below are NN/g's own.

### Make it realistic

| Poor | Better |
|---|---|
| "Purchase a pair of orange Nike running shoes." | "Buy a pair of shoes for less than $40." |

> "Asking a participant to do something that he wouldn't normally do will make him try to
> complete the task without really engaging with the interface."

`(verified)`

### Make it actionable, not self-reported

| Poor | Better |
|---|---|
| "Tell me where you'd click next." | "Use [the site] to find a movie you'd be interested in seeing on Sunday afternoon." |

> "People's self-reported data is not as accurate as when they actually use a system."

`(verified)` This is the same principle as the corroboration house rule, one level earlier: do
not let the task itself collect a claim where it could collect a behaviour.

### Give no clues and no steps

| Poor | Better |
|---|---|
| "Go to the website, sign in, and tell me where you would click to get your transcript." | "Look up the results of your midterm exams." |

> "Step descriptions often contain hidden clues as to how to use the interface."

`(verified)` GOV.UK: tasks must not give away "the answer" or "hint at how a participant might
complete them". `(verified)`

**Including interface vocabulary is the most common form of this.** If the task says "find the
admission form" and the nav item says "Admission forms", the task has been completed by reading
it. No source found names this failure, so the label is this library's. `(derived)`

### Give it a clear end state

The participant has to know when they are done. GOV.UK: "set a clear goal for participants to
try and achieve". `(verified)` Carlson, University of Minnesota Duluth: clarity "including a
clear end point". `(verified)`

### Keep it brief, and in the participant's language

Carlson: brevity, because "People read at different rates", and familiar language with no
jargon. `(verified)`

### Make it hard enough to find problems, and fit the time

GOV.UK: tasks should be "challenging enough to uncover usability issues" and "relevant and
believable to participants". `(verified)` Carlson: scope that fits the time available.
`(verified)`

### Order and count

GOV.UK: either "one long or complex task" or "several smaller tasks", arranged "in a logical
order" and worked through "one at a time". `(verified)`

No more than 5 tasks per participant, up to 10 minutes per task. GOV.UK. `(verified)` This is
the only authority-backed upper bound found. Blog figures of "2 to 7" or "5 to 10 in 60 to 90
minutes" are `(convention)`.

---

## Sample size

The numbers have real published structure. The **conclusions are contested**, and this library
lays out the disagreement rather than resolving it, because the house rule already resolves it
for practice.

### Nielsen's formula and claim

Nielsen, *Why You Only Need to Test with 5 Users*, NN/g, 18 March 2000. `(verified)`

    problems found = N(1 - (1 - L)^n)

N is the total number of problems, L the proportion one user finds, n the number of users.
Typical L = 31%, averaged across projects. With L = 0.31 and n = 5, that gives 84%, which is the
"about 85%" claim.

His recommendations: 5 users for one homogeneous group, 3 to 4 per group for two groups, 3 per
group for three or more. And the caveat that usually gets dropped: **run several small rounds
rather than one large study**, and the rule is for qualitative testing only. `(verified)`

Origin: Nielsen and Landauer, CHI 1993, 11 studies, Poisson-based. `(unverified)` Virzi
1990-92 found the first 4 to 5 users find about 80%, p ≈ 0.32. `(unverified)` Lewis 1994 found a
lower p of 0.16 and questioned the severity assumptions. `(unverified)`

### What the formula actually means

Sauro's correction matters more than the number. With 5 users you do not know you have seen 85%
of **all** problems. You have seen about 85% of problems affecting roughly 31% or more of users.
`(unverified)`

MeasuringU, *What Do You Gain from Larger-Sample Usability Tests?*, 2 September 2020:
`(verified)`

| Problem affects | n = 5 | n = 18 |
|---|---|---|
| 33% of users | 97% chance of seeing it | over 99% |
| 10% of users | 41% | 85% |
| 5% of users | 23% | 61% |

So the five-user rule is a claim about common problems only, and it is near-blind to anything
affecting one user in twenty.

### The counter-arguments

**Faulkner 2003**, *Behavior Research Methods* 35(3), pp. 379-383. `(unverified)` Tested 60
users, then drew random subsets. Groups of 5 found between **55% and 99%** of problems, mean
about 85%. With 10 users the worst group found 80%. With 20, the worst found 95%.

This is the strongest counter because it does not dispute Nielsen's arithmetic. It accepts the
85% average and attacks the variance: you get one draw, and you cannot tell which one.
`(derived)`

**Spool and Schroeder**, CHI 2001 Extended Abstracts, pp. 285-286. `(unverified)` 49
participants across 4 sites, open-ended purchase tasks. The first 5 found only **35%** of
problems, and serious purchase-blocking problems did not surface until the 13th and 15th
participant.

The likely reason, and it is a useful distinction: Nielsen and Landauer used well-defined tasks,
so users covered the same ground. Spool used goal-directed, self-selected tasks, so users
covered different parts of the site. `(unverified)` **So the five-user rule holds better for
focused tasks than for whole-site evaluation.** `(derived)`

**Schmettow 2012**, *Communications of the ACM* 55(4), pp. 64-70. `(unverified, abstract only)`
Practitioners rely on "magic numbers or the geometric series formula", both are inaccurate, and
both **underestimate** the sample needed, because problem-detection probabilities are
heterogeneous across users and problems. No recommended number was obtainable, so do not
attribute one to him.

**Sauro's position:** 5 is not wrong but is narrow. It finds problems affecting 30% or more. For
a problem affecting 10% you need about 21. `(verified)`

### Summative and quantitative

| Number | For | Source |
|---|---|---|
| 20 | quantitative studies | Nielsen 2000, 2012 `(verified)` |
| 15 per group | card sorting | Nielsen 2012 `(verified)` |
| 39 | stable eyetracking heatmaps | Nielsen 2012 `(verified)` |
| 30 to 60 | benchmarking a service | GOV.UK `(verified)` |
| 93 | benchmark at ±10% margin, 95% confidence, on completion rate | MeasuringU 2015 `(verified)` |
| 426 to 614 | between-subjects comparison detecting a 10 to 12% difference | MeasuringU 2015 `(verified)` |
| 93 | within-subjects comparison, same power | MeasuringU 2015 `(verified)` |

Nielsen's 20 and GOV.UK's 30 to 60 are far below MeasuringU's 93. No source reconciles them. The
difference is almost certainly the margin of error each is willing to accept, since completion
rate is the most variable metric. `(derived)`

A concrete sense of the cost: across about 100 summative tests, n = 5 gives a mean margin of
error of about 58% on completion rates, and n = 20 about 20%. `(unverified)`

---

## Think-aloud

### The variants

Sauro and Lewis, *The Many Ways of Thinking Aloud*, MeasuringU, 21 June 2022. `(verified)`

1. **Concurrent.** Moderator present, may prompt when the participant goes quiet. Based on
   speech communication theory rather than strictly on Ericsson and Simon.
2. **Retrospective from video.** Participant works silently, then narrates over the recording.
   Roughly doubles session time.
3. **Retrospective from memory.** Cheaper, relies on recall. McDonald, Zhao and Edwards 2013
   found it "produced more verbalizations that were relevant to usability analysis".
4. **Unmoderated remote.** Carries the professional-tester concern.

**Classic versus relaxed** is the distinction that matters. The classic Ericsson and Simon
protocol (*Protocol Analysis*, 1984) uses neutral reminders only, "keep talking", with no
interaction and no requests for explanation. `(unverified)` The relaxed version practitioners
actually run has the facilitator probing during the task. Boren and Ramey, *IEEE Transactions on
Professional Communication* 43(3), 2000, is the citation for the gap: "TA practice often does not
conform to the theoretical basis most often cited for it". `(unverified)`

### What it does to the data

The evidence is inconsistent, and the library says so rather than picking a line.

**Fox, Ericsson and Best 2011**, *Psychological Bulletin*. `(unverified)` About 3,500
participants. The think-aloud effect on performance is indistinguishable from zero (r = -.03).
All verbal reporting lengthens task time. Crucially: procedures that ask people to **describe or
explain** their thinking are reactive and do change performance, while plain "just think aloud"
does not. Their recommendation is the plain instruction. Caveat: mostly cognitive tasks, not
usability tests. `(derived)`

**Hertzum, Hansen and Andersen 2009**, *Behaviour & Information Technology*. `(unverified)`
Classic TA "has little or no effect on behavior apart from prolonging tasks". Relaxed TA
produced longer tasks, more distributed visual behaviour, more navigation commands and higher
mental workload. Quantified elsewhere as 37% longer for classic and 85% slower for relaxed, but
with only 8 participants. No difference in task success.

**Task-time studies, which disagree with each other.** `(verified)` via Sauro's summary:
Bowers and Snyder 1990, no significant difference (n = 48). Berry and Broadbent 1990, 62% slower
(n = 24). Wright and Converse 1992, 43% **faster** with fewer errors (n = 24).
Olmsted-Hawala et al. 2010, no significant difference (n = 80).

**The largest single dataset**, MeasuringU, 6 December 2022: `(verified)` 10 unmoderated
studies, 423 participants. Successful task time 20% longer with think-aloud, 337s versus 279s.
Standard deviation about 27% higher. The effect appeared in 9 of 10 studies but only 3 were
individually significant.

### What follows for a test plan

Use the plain instruction, not "explain your thinking", because that is the version the evidence
says is non-reactive. `(derived)` from Fox et al.

**Do not compare task times across a think-aloud and a silent condition**, and do not benchmark
against published time norms collected under a different protocol. The inflation is real,
somewhere around 20 to 40%, and its size is unpredictable. `(derived)`

NN/g, *Thinking Aloud: The #1 Usability Tool*, 15 January 2012: inexpensive, no equipment, and
Nielsen's position since 1993 that it is the single most valuable method. Caveats he names: it is
unnatural, users may filter their thoughts, and facilitators can bias results with poorly timed
questions. `(verified)`

---

## Moderated or unmoderated

The orchestrator can pass a recommendation, derived from the question's placement on the
qual/quant axis and the phase. **The skill still asks and confirms**, because it also runs
standalone and because the user may have a constraint the orchestrator does not know about.
`(house)`

NN/g, *Remote Usability Tests: Moderated and Unmoderated*, 12 October 2013. `(verified)`

**Moderated remote.** Back-and-forth, clarifying and probing, real-time recovery from technical
problems, can draw out a quiet participant. Weaknesses: hard to know when to intervene, since
silence is ambiguous, and non-verbal cues are partial. Best for a general usability review that
needs follow-up.

**Unmoderated.** Participants work on their own schedule, many at once, good for tight timeframes
and distributed audiences. Weaknesses: no follow-up questions, no awareness of technical
problems or abandoned sessions, and participants often stop thinking aloud. NN/g's own
positioning is that it suits **specific elements**, widgets and minor changes, and not a
comprehensive design review.

Unmoderated wrong choices, built from the above: `(derived)`

- early or low-fidelity prototypes that cannot guide someone unaided
- complex multi-decision workflows
- anything where the answer needed is "why"
- anything where a facilitator would have to recover from a failure

The line "moderated helps you understand, unmoderated helps you measure" is vendor-blog
shorthand. `(convention)` It is roughly right and should not be cited.

---

## Success measures

### Task success

NN/g, *Success Rate: The Simplest Usability Metric*, 17 February 2001, reviewed 2021.
`(verified)`

Success rate is "the percentage of users who were able to complete a task in a study". Binary.

Levels of success, for when binary is too coarse: complete success; success with minor issue;
success with major issue; failure.

**And the correction this library exists to carry:** Nielsen explicitly warns against assigning
numbers to those levels and averaging them, because they are ordinal labels and not interval
values. `(verified)` The widespread practice of scoring partial success as 0.5 is therefore
contradicted by the source it is usually attributed to. `(convention)` Report the distribution
across levels, not a mean. `(derived)`

Tullis and Albert add a finer set: complete with or without assistance, partial with or without
assistance, and failure split into gave up versus **thought it was complete but was not**.
`(unverified)` That last category is worth keeping, because it is invisible in a binary measure
and it is the one that reaches production.

**Benchmark.** Average completion rate 78%, from 1,189 tasks across 115 tests and 3,472 users.
92% or above is the top quartile; below 49% is the bottom quartile. MeasuringU, 21 March 2011.
`(verified)` The data skews toward commercial software, so it is a soft benchmark. What counts as
good depends on stakes: near 100% for safety or financial risk, around 70% for a consumer app.
`(verified)`

**GOV.UK's measure set**, for a benchmarking study: task success, time to completion,
abandonment including incorrectly believing you succeeded, perceived difficulty 1 to 5,
confidence 1 to 5, and whether it took more or less time than expected 1 to 5. `(verified)`

No benchmark values were found for time on task or error rate. `(verified)` as a negative.

### Satisfaction instruments

**SEQ**, the Single Ease Question. The default per-task measure. `(verified)`
Wording: "Overall, how difficult or easy was the task to complete?" 7 points, labelled at the
endpoints, asked immediately after each task. Average about 5.5, from over 400 tasks and 10,000
users. Midpoint is 4, so the average sits above it.

**SUS**, the System Usability Scale. Brooke, 1986. `(verified)`
10 items, 5 response options. Scoring: for odd items subtract 1 from the response; for even
items subtract the response from 5; sum and multiply by 2.5 for a 0 to 100 score.
Average **68**. Grades: above 80.3 is an A and the top 10%; about 74 is a B-; 68 is a C; below
51 is an F and the bottom 15%.
Not diagnostic, and reliable at small samples. Correlation with task performance is modest, about
6% shared variance, which is the basis of the corroboration house rule. `(unverified)` on that
figure.

**UMUX-Lite**, when two items is all the session can afford. `(verified)`
"[This system's] capabilities meet my requirements" and "[This system] is easy to use".
Correlates with SUS at r = .83, reliability alpha .86 against SUS's .91.
To predict a SUS score: `SUS = 0.65 x ((item1 + item2 - 2) x (100/12)) + 22.9`

**NPS.** 0 to 10 likelihood to recommend; promoters 9 to 10, detractors 0 to 6; NPS = %promoters
minus %detractors.

**Do not use it as a usability measure.** It is a loyalty and relationship measure, so it is
answering a different question. `(derived)` Sauro's five documented criticisms, *Should the Net
Promoter Score Go?*, 22 July 2014: `(verified)` it overlaps with satisfaction; the 11-point
scale is unnecessarily complex; stated intent poorly predicts behaviour; it should use different
questions; and converting to categories inflates the margin of error. The category cutoffs also
hide real movement, since a mean rising from 2 to 5 is still entirely "detractor".
`(unverified)` Sauro himself defends much of it for benchmark comparability and recommends using
the raw mean for statistics. `(verified)`

---

## Severity rating

Nielsen's scale, NN/g. `(verified)`

| | |
|---|---|
| **0** | Not a usability problem |
| **1** | "Cosmetic problem only: need not be fixed unless extra time is available" |
| **2** | Minor usability problem, low priority |
| **3** | "Major usability problem: important to fix, so should be given high priority" |
| **4** | "Usability catastrophe: imperative to fix this before product can be released" |

Three factors to weigh: **frequency** (common or rare), **impact** (how hard to overcome when it
happens), **persistence** (one-off or repeated). Market impact is a fourth consideration, for
problems that are easy to fix but affect how the product is received. `(verified)`

**These are factors to consider, not a formula.** Nielsen does not multiply them, and presenting
"frequency x impact x persistence" as an equation is a simplification this library does not
make. `(derived)`

Other scales exist (Dumas and Redish, Rubin, Molich) but none was verified, so none is cited
here. No source was found on how two raters reconcile a disagreement, which is a real gap.
`(verified)` as a negative.

---

## Session structure

GOV.UK: `(verified)`

- Sessions usually 30 to 60 minutes
- No more than 6 one-hour sessions per day, at least 15 minutes between them, plus lunch
- No more than 5 tasks per participant, up to 10 minutes per task
- Discussion guide: intro script, task descriptions, planning checklist

Krug's cadence, "a morning a month", 3 participants per round, three tests in a morning with a
debrief over lunch. `(unverified)` Note this is 3 per round where the house minimum is 6, and
Krug's model depends on running rounds frequently rather than making any single round
sufficient. The two are compatible only if the rounds actually recur. `(derived)`

A 60-minute allocation of roughly 5 to 10 minutes intro and consent, 35 to 40 minutes on tasks,
5 to 10 minutes debrief and SUS: **no source gives this.** `(convention)` Present it as an
illustration.

NN/g's *Usability Testing 101* gives no task counts or timings at all, but does stress that task
wording primes and that facilitation must not influence the participant. `(verified)`

---

## Change log

**7 October 2026.** File created. Split into a sourced half (sample size, measures, severity) and
an unsourced half (task scenarios), because the research pass found no taxonomy for the latter.
Two house rules at the top: minimum 6 participants, overriding the five-user default the skill
previously carried, and stated ease reported against the observed record. The partial-credit
0.5 convention is recorded as contradicted by its own usual source.
