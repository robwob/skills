# Survey bias and question design

The library `survey-questions` reads from, in all three of its modes: drafting from a brief,
evaluating an existing survey for bias, and evaluating one against a brief.

**Last updated:** 7 October 2026

---

## How far the structure goes, and where it stops

**Total Survey Error is the canonical framework**, and it is citable: Groves 1989; Groves et al.,
*Survey Methodology*, 2nd ed., 2009; Groves and Lyberg, *Public Opinion Quarterly* 74(5), 2010,
pp. 849-879.

**But TSE is not a taxonomy of named biases.** It sorts errors by *where in the survey lifecycle
they arise*. It does not enumerate or standardise terms like "acquiescence" or "leading
question". Groves and Lyberg say themselves that TSE "has largely remained a theoretical taxonomy
and is rarely implemented empirically". `(unverified)`

The practical consequence: coverage, sampling, nonresponse and processing sort cleanly, and then
roughly three quarters of the entries below all land in **measurement**, which is too coarse to
filter on. So this library adds a second tag from Tourangeau, Rips and Rasinski's model of the
response process (*The Psychology of Survey Response*, 2000): comprehension, retrieval,
judgment, response mapping. `(unverified)`

**That pairing is this library's own classification, not a published one.** TSE says where the
error enters the survey; Tourangeau says where it enters the respondent's head. Both are real
frameworks and nobody has crossed them for this purpose. The cross is useful and it is imposed,
and the file says so rather than implying a standard exists.

**Several terms in common use are not survey-methodology terms at all**, and are marked where
they appear:

- **Anchoring** and **framing** are Kahneman and Tversky judgment-and-decision terms (1974, 1981)
- **Survivorship bias** is general statistics and finance
- **Central tendency bias** is psychometrics and practitioner usage; the survey term is nearer
  "midpoint responding" under response styles
- **Leading** and **loaded question** are practitioner and legal usage; the literature says
  "question wording effects" and "balanced versus unbalanced questions"

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source and citation, reached through a secondary summary rather than read |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's inference |
| `(house)` | Rob's own standing practice. Not citable, and not to be overwritten by a source that disagrees. |

**This is the least-verified library in the family.** The research pass behind it read search
snippets, not full sources. Only four things were confirmed against retrieved text: the TSE
component list, the Groves and Lyberg citation, Pew's 2003 order-effect figures, and Galesic and
Bosnjak's start rates. Everything else carrying a citation is `(unverified)`.

**Before quoting any number from this file, check it.** The two most load-bearing unverified
figures are flagged inline.

---

## House rules

### A survey cannot corroborate itself

The standing rule is that a stated preference must be checked by a specific question that could
disprove it. `(house)` A survey measures attitude and nothing else, so **it has nothing inside
it that can do the checking**. The corroboration has to come from a second method with a
behavioural measure.

So: a survey is never the sole instrument behind a claim about behaviour, and a survey finding is
written up as "respondents say X", never as "users do X". `(house)`

This agrees with NN/g's own positioning, that surveys complement rather than replace qualitative
work. `(verified)` It is stricter than that, because it also rules out a survey standing alone
behind an attitudinal claim that is being used to predict action.

### Minimum 6 does not apply here

The house floor of 6 participants is for qualitative rounds. Surveys are quantitative and need a
sample sized to the precision wanted, not a floor. `(derived)`

---

## Total Survey Error: the components

Confirmed against retrieved text. `(verified)`

**Representation side**, the non-observational gaps:

| Component | The gap |
|---|---|
| **Coverage error** | target population to sampling frame |
| **Sampling error** | frame to sample |
| **Nonresponse error** | sample to respondent pool |
| **Adjustment error** | listed by Groves 2009, less commonly cited `(unverified)` |

**Measurement side**, the observational gaps:

| Component | The gap |
|---|---|
| **Measurement error** | the ideal measure to the response obtained. Groves splits respondent, interviewer and instrument sources. |
| **Processing error** | the response to the variable used in estimation: coding, editing, data entry |

One distinction to keep explicit, because it is routinely blurred: **sampling error is random
variance, not bias.** A bigger sample shrinks it. No sample size fixes a biased instrument.
`(derived)`

---

## The bias entries

Each carries its TSE component and, where it sits on the measurement side, its response-process
stage.

### Question wording

#### Leading and loaded questions
`TSE: measurement` · `Stage: comprehension, judgment`

Wording that suggests a preferred answer or embeds an assumption. Shows up as "Don't you agree
that...", evaluative adjectives, and unbalanced stems.

**Mitigation:** neutral phrasing, balanced stems ("favor or oppose" rather than "do you
favor"), and cognitive interviews to test. `(unverified)` Sudman and Bradburn, *Asking
Questions*, 1982; Pew questionnaire-design guidance. The label "leading" is `(convention)`.

#### Double-barrelled questions
`TSE: measurement` · `Stage: comprehension`

One item asks about two things, so the answer cannot be attributed to either.
**Mitigation:** split it. `(unverified)` Bradburn, Sudman and Wansink, *Asking Questions*, 2004.

#### Assumed behaviour (missing filter)
`TSE: measurement` · `Stage: comprehension`

Asks how often someone does something without first confirming they do it ("How often do you use
this feature?"). Forces a false answer from everyone who does not. **Mitigation:** a filter
question first, and routing around the follow-up. `(convention)` Carried over from an earlier
version of this skill, where it was an unsourced check; kept because it is a real and
common failure, tagged for what it is.

#### False dichotomy
`TSE: measurement` · `Stage: response mapping`

A forced binary where more options exist ("Do you prefer A or B?" with nothing else). Overlaps
with the exhaustive-options rule below and is the same failure seen from the question side.
**Mitigation:** add "neither", "both" or "other", or ask an open question. `(convention)` Carried
over from the previous version, as above.

#### Negation and double negatives
`TSE: measurement` · `Stage: comprehension`

**Mitigation:** rewrite positively. The rule is well attested; the reasoning, that negation
raises comprehension errors, is plausible and not specifically sourced. `(convention)`

#### Absolutes
`TSE: measurement` · `Stage: judgment`

"Always", "never". Pushes respondents toward disagreement or the extremes. No primary source
found. `(convention)`

#### Unspecified reference period
`TSE: measurement` · `Stage: retrieval`

"Recently" invites telescoping. **Mitigation:** "in the past 7 days". `(unverified)` Sudman and
Bradburn.

#### Response options that are not mutually exclusive and exhaustive
`TSE: measurement` · `Stage: response mapping`

**Mitigation:** check for overlap, include "other" and "none" where they apply.
`(convention)` on the label, textbook-standard in substance.

### Response styles

#### Acquiescence
`TSE: measurement (respondent)` · `Stage: response mapping, cross-cutting`

The tendency to agree regardless of content. The way it is detected: compare agreement with a
statement against disagreement with its logical opposite. If content alone drove the answer the
two would match.

**The number: across ten studies, 52% agreed with an assertion while 42% disagreed with its
opposite.** That ten-point gap is the effect. `(unverified)` and **this is the weakest-sourced
figure in the library**: it came from a search snippet of a SAGE *Encyclopedia of Survey Research
Methods* entry, itself summarising ten unnamed studies. Verify before quoting it. The rule it
supports stands without it.

**Mitigation, and it is the main one:** use **item-specific response options** instead of
agree/disagree. Ask "How satisfied are you with X?" rather than "I am satisfied with X: agree or
disagree". `(unverified)` Krosnick and Presser 2009. Balanced keying is the older, weaker
mitigation and can confuse some respondents. `(derived)`

#### Social desirability
`TSE: measurement (respondent)` · `Stage: judgment, response mapping`

Over-reporting desirable behaviour and under-reporting undesirable.
**Mitigations:** self-administered mode, forgiving wording ("many people..."), indirect
questions, randomised response. `(unverified)` Tourangeau and Yan 2007, *Psychological
Bulletin*, "Sensitive Questions in Surveys". **Their effectiveness is mixed in that source**, so
do not state forgiving wording as reliably effective. `(derived)`

#### Extreme and midpoint responding
`TSE: measurement (respondent)` · `Stage: response mapping`

Habitual use of the end points, or of the midpoint, independent of content.
**No single fix.** Options: more scale points, full labelling, statistical correction.
`(unverified)` Baumgartner and Steenkamp 2001; Greenleaf 1992. "Central tendency bias" as a
label is `(convention)`.

#### Satisficing
`TSE: measurement (respondent)` · `Stage: cross-cutting`

Krosnick 1991, "Response strategies for coping with the cognitive demands of attitude measures
in surveys", *Applied Cognitive Psychology*. `(unverified)` Strong satisficing means skipping
the optimising steps and taking the first acceptable answer.

It is the **mechanism** behind several entries that look separate: acquiescence,
"don't know" selection, straightlining, non-differentiation, and primacy.
**Mitigations:** shorter surveys, easier items, no long grids. Attention checks are
`(convention)`.

#### Straightlining
`TSE: measurement (respondent)` · `Stage: response mapping`

The same response down a grid. Krosnick's term is non-differentiation.
**Mitigations:** break up grids, and exclude on a response-variance index. Varying scale
direction is sometimes suggested and the evidence is mixed. `(convention)` except the link to
satisficing, which is `(unverified)`.

### Order and context

#### Question-order and context effects
`TSE: measurement (instrument)` · `Stage: judgment`

**Verified, and the strongest single demonstration in this file.** Pew states that a question's
placement can matter more than its wording. Their 2003 example: support for legal agreements
giving same-sex couples the same rights as marriage was **45%** when asked after a question about
marriage, and **37%** without that preceding context. `(verified)`

The literature's terms are assimilation and contrast effects. `(unverified)` Schwarz and Sudman;
Tourangeau.
**Mitigations:** rotate or randomise question order across respondents, go general to specific,
and test.

#### Primacy and recency in response options
`TSE: measurement (instrument)` · `Stage: response mapping`

Pew: descending, positive-first scales generate more positive responses than ascending.
`(verified)` The rule of thumb: primacy in visual, self-administered modes; recency in aural,
interviewer-administered modes. `(unverified)` Krosnick and Alwin 1987.

**Mitigation:** randomise option order where options are unordered. **Do not randomise an
ordinal scale**, keep it in logical order and consistent in direction throughout the
instrument. `(convention)`

#### Anchoring and framing
`TSE: measurement` · `Stage: judgment`

Borrowed terms, not core survey vocabulary. `(unverified)` Tversky and Kahneman 1974, 1981. In
surveys they appear as numeric examples in open estimation items, and as how an issue is
presented.
**Mitigations:** neutral descriptions, no numeric examples, vary the frame across split ballots.

### Memory

#### Recall bias and telescoping
`TSE: measurement (respondent)` · `Stage: retrieval`

Telescoping is dating events closer to the present than they were (forward telescoping).
`(unverified)` Sudman and Bradburn 1973; Tourangeau et al. 2000.
**Mitigations:** bounded recall, shorter reference periods, anchoring to landmark events, aided
recall. `(convention)` on the specific techniques.

### Who answers

#### Nonresponse bias
`TSE: nonresponse`

**The corrective that matters most here, and state it explicitly:** bias depends on the response
rate **and** on how different respondents are from nonrespondents. A low response rate does not
by itself imply bias, and a high one does not guarantee its absence. `(unverified)` Groves 2006,
*Public Opinion Quarterly*, "Nonresponse rates and nonresponse bias in household surveys".
**Mitigations:** follow-up, incentives, weighting, nonresponse follow-up studies.

#### Self-selection and volunteer bias
`TSE: nonresponse in probability samples; closer to coverage in opt-in panels`

Opt-in panels and open links produce a self-selected sample, and in that case the *frame itself*
is self-selected, which is why the TSE placement is not uniform in the literature.
`(unverified)`
**Mitigations:** probability-based panels, quotas, weighting. **None of them fully removes it.**
`(derived)`

#### Coverage error
`TSE: coverage`
Gap between the target population and the frame you can actually reach. `(verified)`
**Mitigations:** better frames, multiple or dual frames.

#### Sampling error
`TSE: sampling`
Random variance from measuring a subset. `(verified)` Not a bias.
**Mitigation:** larger probability samples and correct variance estimation.

#### Survivorship bias
`TSE: coverage, approximately`

Not a survey-methodology term. `(convention)` In surveys it appears as surveying only current
users, so everyone who left is absent. Worth keeping under its borrowed name because the failure
is common and the name is recognisable. `(derived)`

### After the answers

#### Coding error in open responses
`TSE: processing`

**Mitigations:** a codebook, double coding, agreement checks. `(convention)` Cost is high
relative to closed items and no figures were found. `(derived)`

---

## Response scales

**This whole section is `(unverified)`.** None of it was retrieved this session. Check before
quoting any figure.

**Likert versus Likert-type.** A true Likert scale is a summated scale across multiple
agree/disagree items (Likert 1932). A single rating item is "Likert-type". The distinction is
widely noted and mostly pedantic in practice. `(convention)` on the last clause.

**Number of points.** The findings are mixed and should be presented as such.

- Preston and Colman 2000: reliability and discriminating power best at about 7 points and
  above. 10 and 11-point scales performed well but respondents disliked them.
- Krosnick and Presser 2009: reliability and validity generally best at about **7 points for
  bipolar** scales and about **5 for unipolar**, with diminishing returns beyond.
- Practitioner position, that point count barely moves the averages, is `(convention)`.

**Midpoint.** Including one avoids forcing a position; it also attracts satisficers (Krosnick
1991). O'Muircheartaigh, Krosnick and Helic 2000 found adding a midpoint did not harm data
quality and helped respondents who genuinely held a neutral view.
**Default: include a midpoint on bipolar scales** unless there is a specific reason to force a
choice. `(derived)`

**Label every point.** Fully labelled scales are more reliable than numeric-only or
endpoint-only. Krosnick and Presser 2009; Alwin and Krosnick 1991. Numeric labels carry meaning
of their own: 0 to 10 and -5 to +5 behave differently (Schwarz et al. 1991).

Note the tension with SEQ in `../../usability-test-plan/references/task-design.md`, which is
endpoint-labelled by design and has a published average of 5.5 that depends on that format.
Changing SEQ's labelling to follow this rule would break comparability with the benchmark.
`(derived)`

**Agree/disagree versus item-specific.** The methodologists' preference is item-specific, on
three grounds: acquiescence; the extra cognitive step of mapping a statement onto a scale before
answering; and that item-specific wording asks for the construct directly. Saris et al. 2010,
*Survey Research Methods*, found item-specific gave better data quality. Fowler 1995 argued the
same. Pew's guidance agrees about avoiding agreement scales where respondents rush.
`(verified)` on the Pew point only.

**Direction.** Keep it consistent within an instrument. `(convention)`

---

## Screener design

**The weakest-sourced section in the family.** Almost entirely practitioner convention, and no
targeted search was run for it. `(convention)` unless marked.

- **Do not telegraph the qualifying answer.** Embed the criterion among plausible decoys in a
  multi-select. Avoid a yes/no on the exact qualification ("Do you use X?"). Ask about a
  category, then qualify on the answer.
- **Do not reveal criteria in the invitation.**
- **Professional and fraudulent respondents.** Consistency checks across items, trap items,
  speeding thresholds, open-response quality, duplicate IP or device fingerprinting, and
  re-asking a qualifier later to catch inconsistency.
- ESOMAR publishes the *ESOMAR/GRBN Guideline on Online Research* and *20 Questions to Help
  Buyers of Online Samples*; AAPOR's opt-in panel reports cover fraud and data quality.
  `(unverified)`, existence only, content not retrieved.
- **Highest-risk design:** a single yes/no qualifier attached to an obvious incentive.
  `(derived)`

---

## Open versus closed

`(unverified)` Krosnick and Presser 2009; Schuman and Presser, *Questions and Answers in
Attitude Surveys*, 1981, is the classic source for the experiments.

**Closed** is cheaper, comparable and easier to analyse, and it constrains answers to what you
offered, so the options shape the responses.

**Open** is for exploration, for an answer space you cannot enumerate in advance, and for
questions where listing options would prime the answer, the classic case being "the most
important problem". `(derived)` from Schuman and Presser's logic.

Coding open responses is a **processing error** source in TSE terms. `(derived)`

---

## Length and completion

**Verified.** Galesic and Bosnjak 2009 announced lengths of 10, 20 and 30 minutes in an opt-in
web survey. Start rates were **75%, 65% and 62%**. Longer announced length meant fewer people
started and fewer completed. `(verified)` They also reported worse response quality later in
longer questionnaires, but that part was not confirmed. `(unverified)`

**No clean "X minutes gives Y% drop-off" benchmark exists** with a primary source. Practitioner
rules like "keep it under 10 minutes" are `(convention)`. A *Survey Practice* article,
"Breakoffs in an Hour-Long Online Survey", exists and its numbers were not read. `(unverified)`

---

## To verify, in priority order

1. The acquiescence 52/42 figure. Weakest source, supports an actionable rule.
2. Krosnick and Presser 2009 on scale points. The 7-bipolar / 5-unipolar recommendation would
   otherwise be an unchecked default.
3. Saris et al. 2010 on item-specific scales, which is the evidence behind the main acquiescence
   mitigation.
4. Groves 2006 on nonresponse, for the "low response rate does not imply bias" corrective.
5. The Galesic and Bosnjak data-quality claim, as distinct from the start rates.

Not searched at all: NN/g's survey articles, MeasuringU's rating-scale articles, ESOMAR and
AAPOR documents.

---

## Change log

**7 October 2026.** Assumed behaviour and false dichotomy added from the previous skill's inline checklist, both `(convention)`. File created. Organised on TSE as the first axis and Tourangeau's
response-process model as the second, with the cross between them flagged as this library's own
classification rather than a published one. Terms borrowed from outside survey methodology are
marked. The house rule that a survey cannot corroborate itself is recorded at the top. This is
the least-verified library in the family and carries a verification queue.
