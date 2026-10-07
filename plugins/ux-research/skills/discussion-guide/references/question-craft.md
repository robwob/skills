# Interview question craft

The library `discussion-guide` reads from. How to write interview questions, how to order them,
how to probe, and the mistakes with their fixes.

**Last updated:** 7 October 2026

---

## This library is prose, and that is deliberate

Unlike `ux-research-brief/references/methods.md`, which classifies 20 methods on three published
axes, **there is no canonical taxonomy of interview question types in UX.** NN/g, GOV.UK, Hall
and Portigal each publish their own short list of tips and mistakes. The lists overlap, none
cites a shared framework, and none cites the others.

Two narrow exceptions have real named structure and are given their own entries below:
**laddering**, which has a theory and a fixed attribute-consequence-value chain, and **the
funnel**, which NN/g has formalised. Question-type taxonomies do exist (Spradley, Kvale and
Brinkmann) but they come from academic social science, and UX borrows their vocabulary loosely
rather than adopting the framework.

So this file is organised by the task at hand, not by a classification. The one faceting worth
keeping is a question's **role in the guide**: opener, main, follow-up or probe, closer. That is
Rubin and Rubin's structure and NN/g's, and it is the only split both support.

Do not impose a three-axis structure on this material. It would be invented.

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source and citation, reached through a secondary summary |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's inference |
| `(house)` | Rob's own standing practice. Not citable, and not to be overwritten by a source that disagrees. |

`(house)` outranks the rest in practice. Where a source and a house rule conflict, state both
and follow the house rule.

**Not read in primary form:** Portigal *Interviewing Users*, Rubin and Rubin *Qualitative
Interviewing*, Indi Young *Time to Listen*, Spradley *The Ethnographic Interview*, Reynolds and
Gutman 1988. Anything attributed to those is `(unverified)`. Do not quote them.

---

## House rules

These come first because they are decisions, not inputs.

### Corroborate every stated preference inside the session

A claim that the follow-up questions do not support is not a finding. `(house)`

Take the claim, then ask for the specific occasion. If someone says they like the product and
cannot describe the last time they used it willingly, the stated preference is unreliable and
**the contradiction is the result**, not a sign the participant was confused.

This is the practical mitigation for two things the sources name separately but never connect to
a fix:

- Participants "want to be liked" and "want to demonstrate their smarts". Erika Hall,
  *Interviewing Humans*, A List Apart, 10 September 2013. `(verified)`
- "What people typically do ... and what they think they typically do may be different things."
  NN/g, *6 Mistakes When Crafting Interview Questions*, 6 March 2022. `(verified)`

**What this requires of a guide:** every attitude question carries at least one paired
specific-incident question that could contradict it. A guide with attitude questions and no
corroborating pairs is incomplete. `(house)`

**What this requires of a write-up:** report the claim *and whether it held*. Never the claim
alone. `(house)`

**Not the same as NN/g's triangulation**, which means combining several methods or data sources
across a study. Kathryn Whitenton, NN/g, 21 February 2021. `(verified)` This rule runs inside one
session. Keep the two names apart.

### Minimum 6 participants

Per audience segment, for qualitative rounds. `(house)` The reasoning and the contested
five-user rule are in `usability-test-plan/references/task-design.md`.

---

## Writing the questions

### Open, not closed

Open questions are the primary instrument. `(verified)` NN/g, *Open-Ended vs. Closed Questions
in User Research*, 26 January 2024:

- "the greatest benefit of open-ended questions is that they allow you to find more than you
  anticipate"
- "closed questions stop the conversation"
- closed questions "eliminate surprises: what you expect is what you get"

Closed questions still have two jobs: clarification, and anything destined for counting.
`(verified)`

Hall's contrast pair: `(verified)`

| Closed | Open |
|---|---|
| "Do you communicate with the marketing department often?" | "Tell me about the internal groups you communicate with." |

GOV.UK's phrasings: "how do you...?", "what are the different ways you...?"
`(verified)`

### Ask about the past, never the future

The strongest rule in the sources, and the most violated.

> "people are bad at predicting their future behavior or choices, but they'll likely have a good
> answer"

NN/g, *6 Mistakes*, mistake 3. `(verified)` The danger is in the second clause: the answer
sounds usable and is not.

NN/g, *Why User Interviews Fail*, 9 June 2019: interviews "do not produce reliable data about
user behavior", and teams misuse them for "hypotheticals and future scenarios where observation
would be more appropriate". `(verified)`

Teresa Torres, Product Talk, 19 August 2014: replace "Would you pay for this?" with "Have you
ever paid for a similar service?" `(verified)`

So "would you use this" is out, and so is every variant of it. `(convention)` on that exact
phrasing being named as a rule; the principle is `(verified)`.

### Ask for the problem, not the solution

*Why User Interviews Fail* lists asking about "needed features" among the things interviews
cannot answer reliably. `(verified)` Indi Young's problem-space position is the same, but was
not readable. `(unverified)`

### One thing per question

> the participant "has to store the question in their working memory while they answer part of it"

NN/g, *6 Mistakes*, mistake 5, on double-barrelled questions. `(verified)`
Smashing lists the same under "stacked multiple questions at once". `(verified)`

### Do not assume facts

"What was the last book you read?" presumes recent reading. NN/g, *User Interviews 101*.
`(verified)` Portigal's reported example: ask "How long have you worked here?" rather than "Do
you like it here?" `(unverified)`

### Remove your own interest from the wording

Smashing, *12 Ways To Improve User Interview Questions*, 9 June 2020: `(verified)`

- strip "explanations embedded in questions"
- avoid "selfish questions" using "our" and "we"
- "ground general questions in recent experiences"
- ask the participant to "quantify vague generalizations" in their own terms

GOV.UK: "avoid generalities and talking about how things 'should' happen." `(verified)`

### Shut up

> "conducting a good interview is actually about shutting up"

Hall. `(verified)` GOV.UK: "The more you talk, the less your participant will talk."
`(verified)`

---

## Named techniques

### The funnel

The one ordering technique with a formalised source. NN/g, *The Funnel Technique in Qualitative
User Research*, 24 July 2022. `(verified)`

Three steps:

1. A broad open question. "Tell me about the last time you ordered movie tickets."
2. Open follow-ups and probes.
3. Closed questions, last.

Stated benefits: it "gets the participant comfortable with talking", "allows the participant to
begin sharing stories", "generates lots of new, unanticipated information" and "avoids the
researcher priming the participant". `(verified)`

That last one is the reason it reduces bias, and it is the only reasoned ordering claim in any
primary source found: **broad before narrow, so your closed questions do not reveal what you
care about before the participant has answered freely.**

NN/g says the funnel "has been around since qualitative interviews emerged" and gives no earlier
citation. `(verified)`

**The inverted funnel is not an established technique.** No source found defines or endorses one
for interviews. Do not present it as a method. `(derived)`

### Critical incident

The corrective for the grand tour's drift toward the typical. NN/g, *The Critical Incident
Technique in UX*. `(verified)`

Definition: participants "recall and describe a time when a behavior, action, or occurrence
impacted (either positively or negatively) a specified outcome." `(verified)`

Origin: Flanagan, 1954, *Psychological Bulletin*, from WWII aviation psychology. `(verified)`

Seek both positive and negative incidents, and often open with positive ones. `(verified)`

Strength: it "captures incidents over a long timeframe". Weakness: it "relies heavily on memory,
which can be fallible and may cause participants stress". `(verified)`

**This is the question type the house corroboration rule depends on.** A specific incident is
what a stated preference gets tested against.

### Grand tour and mini tour

Origin: Spradley, *The Ethnographic Interview*, 1979. `(unverified)` Four grand-tour forms:
general overview, specific, guided, task-related. The mini tour covers a much smaller slice.
Spradley's three question families are descriptive, structural and contrast.

NN/g uses the shape without the name: "Walk me through a typical day for you." "Tell me about
the last time you [did something]." `(verified)`

Good at surfacing structure you did not know to ask about, and at building rapport.
`(verified)` Bad at one thing, and it matters: **it elicits the typical**, which NN/g's mistake 2
warns is not the actual. Follow every grand tour with a critical incident. `(derived)`

Calling these "grand tour" in a UX context is a loose borrowing. `(convention)`

### Laddering

The only place in this library where a classified structure is warranted, because the technique
has one.

Origin: means-end chain theory, and Reynolds and Gutman, "Laddering Theory, Method, Analysis, and
Interpretation", *Journal of Advertising Research* 28(1), 1988, pp. 11-31. `(unverified)`

The chain: **attribute -> consequence -> value**. People choose a product because its attributes
deliver consequences that satisfy values. `(unverified)`

Mechanics: elicit the attribute first, then repeat "Why is this important to you?" up the chain
until a value is reached. Establish a "no right or wrong answers" tone first. `(unverified)`

Soft laddering is the one-to-one interview. Hard laddering is self-administered and "has been
viewed critically". `(unverified)`

Worked example, Michael Hawley, UXmatters, 6 July 2009: `(verified)`
"convertible car" (attribute) -> "feels young and free" (consequence) -> "attractiveness"
(value).

Hawley's pitfalls: `(verified)`

- repeated "why" is tedious and can frustrate participants
- abstract reasoning is hard to articulate
- the interviewer has to hold several threads at once
- abstract product talk gives weaker answers than personal experience narratives

His fixes: explain the method up front, and switch to negative framing ("what would you lose
if...") when a participant stalls. `(verified)`

**A real disagreement, left unresolved.** Laddering depends on repeated "why". Indi Young's
listening-session approach moves away from "why" toward "how" and non-directive prompting, and
Portigal's position is that people often cannot say why they do something. `(unverified)` on
both. NN/g and GOV.UK use "why" as a follow-up without addressing the conflict. `(verified)`

Both positions are defensible and this library does not pick one. Laddering is the right
technique when you need the value behind a choice. Non-directive listening is right when the
"why" would be confabulated. `(derived)`

### Main, follow-up, probe

Rubin and Rubin's responsive interviewing structure, *Qualitative Interviewing: The Art of
Hearing Data*, 3rd ed., SAGE, 2011. `(unverified)` Main questions "begin a discussion about each
separate part of your research question". Follow-ups pursue what the answer opened. Probes manage
the conversation rather than add content.

This is one author's model, not a field standard, but it is the faceting this library uses for a
question's role in the guide.

GOV.UK's equivalent: starter and follow-up questions per topic. `(verified)`
GOV.UK's follow-up phrasings: "you said... when/why/who was that?", "can you tell me more
about...?" `(verified)`

---

## Structuring the session

### Three parts

Hall: "Introduction and warm-up, the body of the interview, and the conclusion." `(verified)`

- **Warm-up** uses easy questions. Hall's example: "Oh, you live in San Diego. What do you like
  to do for fun there?" `(verified)` NN/g: "Tell me a little about yourself." `(verified)`
  Do not open with screener-style closed questions. NN/g mistake 1. `(verified)`
- **Body.** Order logically, ideally chronologically or by phase of experience, with reflective
  questions later. NN/g, *Writing an Effective Guide for a UX Interview*, 28 February 2021.
  `(verified)`
- **Close.** Hall: "That's it for my questions. Is there anything else you'd like to tell me
  about what we discussed?" `(verified)` GOV.UK: clarifying questions, thanks, and an
  explanation of what happens to the research. `(verified)`

### The guide is a checklist, not a script

Hall: use the questions "more as a checklist than as a script". `(verified)`
GOV.UK: "Do not stick to your discussion guide rigidly", and "Do not change the flow of the
interview abruptly." `(verified)`
NN/g: "interviewers don't need to move through questions linearly." `(verified)`

### Length

GOV.UK: "between 30 minutes and 2 hours". `(verified)` 60 minutes is the working default.
`(convention)`

**No authoritative time split exists.** NN/g and GOV.UK both decline to give one. The commonly
quoted 5 intro / 5-10 warm-up / 25-40 core / 5 wrap-up appears only on vendor blogs.
`(convention)` Present it as an illustration, never as a standard.

Roughly 5 to 8 open questions with follow-ups is a reasonable guide length. `(unverified)`

**Pilot the guide to check timing.** NN/g. `(verified)`

### Map each question to a research question

NN/g: "Align each interview question directly to your research questions", and show the research
question alongside the interview questions in the guide. `(verified)`

**"Never ask the research question directly" is not a sourced rule.** It is a reasonable
synthesis, since a research question is about the team's inquiry and an interview question is
about the participant's experience, but no source found states it. `(derived)`

---

## Biases that act on the interview

No primary source lists these together for interviews. NN/g covers acquiescence, social
desirability and recency in its **survey** material, so applying them here is this library's
transfer, marked accordingly.

| Bias | Shows up as | Mitigation | Provenance |
|---|---|---|---|
| **Leading** | The question carries the answer. NN/g: clarifying questions that "introduce an interpretation" make people "more likely to agree with the question or succumb to priming". | Neutral open wording. Echo the participant's own words back, not your reading of them. | `(verified)` NN/g mistake 4, GOV.UK |
| **Acquiescence** | The participant agrees with the question rather than answering it. | Open questions. No yes/no, no agree-framed statements. | `(verified)` in surveys, `(derived)` for interviews |
| **Social desirability** | "the desire to report views that will be regarded favorably by others". | Concrete past behaviour over opinion. Skip questions "likely to feel personal or judgmental". Build rapport. Non-judgemental tone. **And corroborate: see the house rule.** | `(verified)` NN/g, Hall |
| **Interviewer confirmation bias** | Questions narrow toward your hypothesis. Findings get "colored by personal biases", and teams favour what confirms existing beliefs. | Broad-first funnel. Code all the data, not the memorable bits. More than one analyst. | `(verified)` for the problem, `(convention)` for multiple analysts |
| **Recency** | The participant over-weights recent events. | Critical-incident prompts across several timeframes, not just the last one. | `(verified)` bias named, `(derived)` mitigation |
| **Question-order effects** | Early questions prime later answers. | The funnel. Do not reveal your interest early. | `(verified)` rationale, `(derived)` label |
| **Anchoring in wording** | Numbers, examples or adjectives in the question set the scale of the answer. | Remove examples, adjectives and embedded explanations. Ask them to quantify in their own terms. | `(verified)` Smashing items, `(derived)` label |

---

## Where the sources disagree

Recorded rather than resolved.

1. **"Why".** Laddering is built on repeated "why". Young and Portigal move away from it. NN/g
   and GOV.UK use it as a follow-up without comment.
2. **Interpreting questions.** Kvale and Brinkmann list "interpreting" ("Is it correct that you
   feel that...?") as a legitimate question type. `(unverified)` NN/g's mistake 4 warns against
   exactly that. The audiences differ, academic interviewing versus UX, so this is a context
   difference rather than a contradiction. `(derived)`
3. **Interviews as a method.** *Why User Interviews Fail* says interviews do not give reliable
   data on behaviour. Hall, NN/g and GOV.UK all still say to ask about past behaviour. The
   reconciliation: ask for reported accounts of specific past events and treat them as
   **accounts**, not as behaviour data. `(derived)` This is also why the house corroboration rule
   exists.

---

## Change log

**7 October 2026.** File created. Organised as prose by task, because no canonical taxonomy
exists for this material. Two house rules added at the top: minimum 6 participants, and within-session
corroboration of stated preferences. Primary text was not available for Portigal, Rubin and
Rubin, Young, Spradley or Reynolds and Gutman, so those carry `(unverified)`.
