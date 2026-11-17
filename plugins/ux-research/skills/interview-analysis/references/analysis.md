# Interview analysis

The library `interview-analysis` reads from. What interviews can and cannot show, reading a
transcript, evidence types, claim against occasion, coding and themes, what a set of interviews
supports, and quote integrity. Confidence is in `confidence.md`; opportunities and recommendations
are in `opportunities.md`.

**Last updated:** 17 November 2026

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source, reached through a secondary summary |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's own inference |
| `(house)` | The author's standing practice. Not citable, and not overridden by a source that disagrees |

`(verified, via X)` means the source was read when the named sibling file was written, and the
claim is carried over from it.

**Not read in primary form for this file:** the GRADE-CERQual papers, Guest, Bunce and Johnson
(2006), Hennink and Kaiser (2022), Malterud, Siersma and Guassora (2016), Nielsen's *Interviewing
Users*, Fitzpatrick's *The Mom Test*. When this file was written, the session's network could not
reach NN/g, PubMed Central, Product Talk or itamargilad.com, so everything taken from them is
`(unverified)`. Do not quote their figures as established.

---

## House rules

### Six participants is the floor, per segment

For a qualitative round. Below it, say so in the limits. Never present it as a pass or fail.
`(house)`, shared with the research family.

### Check every claim against an occasion

A participant's general claim ("I always send it on time", "it's easy") is checked against their own
account of a specific occasion in the same interview. If the occasion does not support the claim,
**the contradiction is the finding**, not noise. `(house)`, the write-up half of the rule in
`discussion-guide`, which pairs every attitude question with a critical-incident question so this
check is possible.

### One round is a step in a sequence

Interviews find needs and explain them. They do not measure how common a need is, or show that a
solution works. Say what the next round should be rather than calling the gap a defect. `(house)`

---

## What interviews can and cannot show

- **Interviews give accounts, not behaviour.** "What people typically do ... and what they think they
  typically do may be different things." NN/g, *6 Mistakes When Crafting Interview Questions*,
  6 March 2022. `(verified, via discussion-guide/references/question-craft.md)`
- Interviews "do not produce reliable data about user behavior", and teams misuse them for
  "hypotheticals and future scenarios". NN/g, *Why User Interviews Fail*, 9 June 2019. `(verified,
  via question-craft.md)`
- People "are bad at predicting their future behavior or choices, but they'll likely have a good
  answer". NN/g, *6 Mistakes*. `(verified, via question-craft.md)` The answer sounds usable and is
  not.
- Nielsen, *Interviewing Users* (NN/g): memories of past use and predictions of future use are both
  unreliable; in a test, participants gave detailed feedback on features that did not exist.
  `(unverified)`
- Fitzpatrick, *The Mom Test* (2013): ask about specifics in the past, not generics or opinions about
  the future; compliments and hypotheticals are weak signals. `(unverified)`
- Participants "want to be liked" and "want to demonstrate their smarts". Erika Hall, *Interviewing
  Humans*, A List Apart, 10 September 2013. `(verified, via question-craft.md)`

**The reconciliation the library uses:** an account of a specific past occasion is the strongest
thing an interview yields, and it is still an account. A habit, an opinion or a prediction is
weaker, in that order. `(derived)` This is what the evidence types below encode.

---

## Reading a transcript

1. **Read every transcript in full before coding anything.** `(derived)`
2. **The interviewer's words are never participant data.** A quote, a code or a theme can only come
   from a participant turn. AI tools have been seen failing to separate them (Liu and Moran,
   *AI-Powered Tools for UX Research*, NN/g, 2 July 2023). `(verified, via
   usability-test-analysis/references/analysis.md)` `check.py quotes` catches it.
3. **Weigh the answer by the question.**
   - An answer to a **hypothetical** question ("would you use...?") is a prediction, whatever words
     it uses. Code it `hypothetical`.
   - An answer to a **leading** question ("that must have been frustrating, right?") is weaker than
     an unprompted remark: a bare "yes" to it is agreement, not evidence. Leading questions make
     people "more likely to agree with the question or succumb to priming" (NN/g, *6 Mistakes*,
     mistake 4). `(verified, via question-craft.md)` Code the substance only if the participant
     goes on to say something of their own.
   - `check.py prompts` lists interviewer turns worded like either. It matches wording, so read each.
4. **Notice who did the talking.** `check.py stats` gives each participant's share of the words. An
   interview where the interviewer spoke more is worth reading for leading questions before its
   evidence is weighted. "The more you talk, the less the participant will talk." `(convention)`, in
   the moderator notes of `discussion-guide`. The 50% line the script flags is `(derived)`.
5. **Automatic transcripts make mistakes**, including misattributed speakers (Moran and Rosala, 2024).
   `(verified, via usability-test-analysis/references/analysis.md)` Where a quote carries a finding
   on its own, recommend the designer checks it against the recording at its timestamp.

---

## Evidence types

Every coded excerpt gets one. From strongest to weakest: `(derived)`, from the sources above.

| Type | What it is | Example |
|---|---|---|
| `shown` | The participant showed it during the session: shared a screen, opened the app, read out a real message. | "Here, look, this is the text they sent." |
| `occasion` | An account of a specific past occasion: when, what happened, what they did. The critical incident. | "In October the bill was nearly double. I went down and took a photo of the meter." |
| `general` | A habit or generalisation with no occasion attached. | "I always do it when I get the reminder." |
| `opinion` | An attitude, preference or judgement. | "It's fine. It does what it needs to." |
| `hypothetical` | A prediction, wish or answer to a "would you" question. | "I'd use that every month." |

The critical incident technique asks participants to "recall and describe a time when a behavior,
action, or occurrence impacted (either positively or negatively) a specified outcome." NN/g, *The
Critical Incident Technique in UX*, after Flanagan (1954). `(verified, via question-craft.md)` Its
weakness is that it "relies heavily on memory". `(verified, via question-craft.md)` So `occasion` is
the strongest **account**, and `shown` sits above it only because it was seen in the session.

**Code a hypothetical as a hypothetical even when it is emphatic.** "Oh definitely, I'd use that
every month" is a prediction. `(derived)`

---

## Claim against occasion

For each participant, list their general claims (`general` or `opinion` excerpts that say something
checkable), and find their own account of a specific occasion on the same subject. Classify:

| Result | When |
|---|---|
| **Held** | The occasion is consistent with the claim. |
| **Contradicted** | The occasion points the other way. |
| **No occasion described** | Nothing specific on that subject from that participant. |

Example: "I always do it when I get the reminder" (P1), then about the last reminder: "I swiped it
away, and I haven't done it yet, now that I think about it." Contradicted. **Use the participant's
own words for both sides**, each with its timestamp, never your reading of their tone. `(house)`

### Borderline cases `(derived)`

- **An occasion that is the exception they mention as an exception** ("I'm usually fine, apart from
  that one time in March"). Held, with the exception kept as evidence for any finding it supports.
- **A claim about other people** ("everyone in the house forgets"). Not checkable against the
  participant's own occasion. Record it as `general` evidence on the theme, not as a claim to check.
- **An occasion prompted by a leading question.** Weigh it as above. If the only support for a claim
  is "yes" to a leading prompt, the result is "no occasion described".
- **Contradiction across interviews** (P1 says one thing, P5 the opposite). Not this check. That is
  a split on a theme, reported under the theme.

If no participant described an occasion for most of their claims, say so: the report then rests on
claims, and the next discussion guide should pair each attitude question with a critical-incident
question (`discussion-guide` does).

---

## Coding and themes

There is no published threshold for how many participants a theme needs, and no rule on counting
codes. NN/g's *Thematic Analysis* (17 August 2022, reviewed 2026) gives neither, and asks that
themes are tested against the data and, where possible, checked by a second analyst. `(verified, via
usability-test-analysis/references/analysis.md)` So the steps below are this library's. `(derived)`

1. **Code close to the words.** "Reminder arrived during a meeting", not "poor notification timing".
   The abstraction comes at the theme step.
2. **Record each code with participant, timestamp, evidence type and stance** (`for` or `against`
   the theme) in a coding file. That file is what `check.py tally` counts.
3. **Count participants, not mentions.** One person saying it five times is one participant.
4. **Keep the cases against.** A theme four people support and two contradict is a split, and the
   report says so. A participant coded both for and against is reported by what they said, not
   assigned a side.
5. **Keep the one-off that matters.** One participant describing a serious problem is a finding,
   with its count of 1 stated plainly. "If we observe even one person having a problem that is an
   exemplar of a known principle, we are able to be reasonably confident that it is a real
   problem," while "we still won't be able to say precisely how many people will encounter that
   problem." Laubheimer, *Data Is More than Numbers*, NN/g, 1 August 2021. `(verified, via
   usability-test-analysis/references/analysis.md)`
6. **Generalise only as far as the evidence.** One participant wishing for a feature is not "users
   want it". `(verified, via usability-test-analysis/references/analysis.md)`, Liu and Moran's
   example of an AI tool doing exactly this.
7. **Build findings across questions.** A finding is a pattern across the interview, not a summary
   of one question's answers.

### Observation, finding, interpretation, opportunity, recommendation

Keep them apart in the report. `(derived)`

- **Observation:** what a participant said or showed, with its timestamp.
- **Finding:** the pattern across participants, with its count and confidence.
- **Interpretation:** why you think it happens. Labelled.
- **Opportunity:** the need the finding reveals, framed without a solution (`opportunities.md`).
- **Recommendation:** what to do about it. A judgement, agreed with the designer.

---

## Numbers and what a set of interviews supports

**Never write a percentage for fewer than 20 participants.** Write "4 of 6". `(derived)`, from
Budiu, *Why You Cannot Trust Numbers from Qualitative Usability Studies*, NN/g, 23 May 2021, where
"70% of the users" from a small study is "misleading". `(verified, via
usability-test-analysis/references/analysis.md)` Counts describe these participants; they do not
estimate how common something is.

### Saturation

- Guest, Bunce and Johnson, *How Many Interviews Are Enough?*, Field Methods 18(1), 2006, 59 to 82:
  in a fairly homogeneous group, most themes appeared within the first 12 interviews (about 92% is
  the figure secondary sources give), and the high-level themes were present by 6. `(unverified)`
  The six-interview percentage differs between summaries (70% and 73%), so do not quote it.
- Hennink and Kaiser (2022) systematically reviewed empirical tests of saturation. `(unverified)`
  The search summaries did not confirm the sample-size range commonly quoted from it, or its
  journal, so do not cite a number from it until the paper is read.
- Malterud, Siersma and Guassora, *Sample Size in Qualitative Interview Studies: Guided by
  Information Power*, Qualitative Health Research 26(13), 2016: the more relevant information a
  sample holds, the fewer participants it needs, weighed on five dimensions (aim, sample
  specificity, established theory, quality of dialogue, analysis strategy). It gives no fixed
  number. `(unverified)`

**What the library takes from them:** saturation depends on how varied the people are and how
narrow the aim is, so it cannot be claimed from a count. `(derived)` Do not write "we reached
saturation". Write what was seen: "the last two interviews added no new themes", if that is true,
and leave the reader to weigh it. With six participants per segment, broad themes are likely to have
surfaced; a need held by a small minority may well not have. `(derived)`

---

## Quote integrity

Every quote is the participant's exact words, attributed to the right participant at the right
timestamp, and checked against the transcript before the report is shown. `(house)`

Why it is a rule: NN/g found AI research tools giving quotes with no session, timestamp or clip to
check them against, and that "AI systems have a dangerous tendency to provide incorrect information
that sounds plausible" (Liu and Moran, 2023). `(verified, via
usability-test-analysis/references/analysis.md)`

Allowed: cutting with "...", fixing a typographic quote mark. Not allowed: correcting grammar,
merging two remarks into one quote, removing fillers without "...", smoothing a transcription error
without saying so.

---

## Change log

**17 November 2026.** File created for `interview-analysis`. House rules carried over from the
research family. Evidence types, claim against occasion and the treatment of prompted answers added.
Saturation sources reached through search summaries only, as the session could not fetch them.
