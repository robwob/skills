---
name: survey-questions-v2
description: >
  Use this skill to draft a new survey from a research brief, evaluate an existing survey for
  biased questions, or evaluate an existing survey against a research brief. Triggers: 'survey',
  'survey questions', 'questionnaire', 'evaluate this survey', 'check survey for bias', 'write me
  a survey', 'does this survey cover my brief'. When a research brief is shared alone, drafts a new
  survey. When an existing survey is shared alone, evaluates for bias. When both a brief and an
  existing survey are shared, evaluates the survey for both brief coverage and bias. Bias is
  checked against a reference library organised by where the error enters the survey. Also invoked
  by the ux-research-brief orchestrator for the survey activity.
---

# Survey Questions Skill v2

## Purpose

Three modes depending on what the user shares:

1. **Draft mode**: create a structured survey from a shared research brief
2. **Bias evaluation mode**: review a shared survey for biased questions and propose rewrites
3. **Brief evaluation mode**: review a shared survey against a shared research brief, checking
   coverage of the research questions and bias

---

## The library

**`references/bias-types.md` holds the bias entries, response-scale guidance, screener design and
length evidence, each tagged for how well it is sourced. Read it before drafting or evaluating.**

Do not work from memory. Know three things about it before you start:

- **It is organised on two axes, and the cross between them is imposed.** Total Survey Error says
  where in the survey lifecycle an error enters, and Tourangeau's response-process model says
  where it enters the respondent. Both are real published frameworks. Pairing them is this
  library's own classification and the file says so. Do not describe it as a standard.
- **Several terms are borrowed from outside survey methodology.** Anchoring and framing come from
  judgment research, survivorship bias from finance, and "leading question" is practitioner usage.
  The file marks which.
- **It is the least-verified library in the family.** Most citations are `(unverified)`, and it
  carries its own verification queue. Do not quote a figure from it as established. The 52% versus
  42% acquiescence figure in particular is the weakest-sourced number anywhere in this family.

Its claims carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`, `(house)`.

---

## House rules

- **A survey cannot corroborate itself.** Rob's standing rule is that a stated preference must be
  checked by a specific question that could disprove it. A survey measures attitude and nothing
  else, so it has nothing inside it that can do the checking. A survey is therefore **never the
  sole instrument behind a claim about behaviour**, and its findings are written up as
  "respondents say X", never "users do X".
- **The minimum of 6 participants does not apply here.** It is a floor for qualitative rounds.
  A survey is sized to the precision wanted.

---

## Mode detection

On invocation, determine which mode to use:

- **Research brief only**: Draft mode
- **Existing survey only**: Bias evaluation mode
- **Both a brief and an existing survey**: Brief evaluation mode
- **Invoked by the `ux-research-brief` orchestrator**: use the context passed in. The mode will be
  clear.
- **Unclear**: ask "Are you sharing a research brief to draft a new survey, an existing survey to
  check for bias, or both a brief and a survey to evaluate together?"

---

## Draft mode

### Input

Accept the shared research brief. Extract:

- Research questions and assumptions
- Audience
- **Distribution method** (email, in-product, social and so on). Ask if it is not stated, since it
  decides who can answer at all.
- Estimated completion time (default 5 to 7 minutes)
- Whether this complements qualitative research

### Step 1, Check the questions can be answered by a survey

Before drafting, test each research question against what a survey can establish. A survey measures
**attitude, quantitatively**. It answers "how many" and "how much" about what people say.

Flag any research question that is **behavioural**, such as how people actually do something, or a
*why* question that needs probing. A survey cannot answer it. Tell the user, name the method that
would, and keep only the part of the question that is genuinely attitudinal.

### Step 2, State who cannot answer

From the distribution method, name the **representation** problems before they are baked in:

- **Open links and opt-in panels** produce a self-selected sample, and no sampling method fully
  removes that
- **Surveying current users only** leaves out everyone who left. Call it survivorship in the
  survey, because the name is recognisable, and note it is borrowed terminology
- A low response rate does not by itself imply bias, and a high one does not guarantee its absence

Put this in the survey notes, so whoever reads the results knows what they cannot generalise to.

### Step 3, Draft the survey

#### Opening
- One or two sentences on the purpose and the estimated completion time
- Confirm anonymity and how the data will be used
- No questions on the opening screen

#### Screener questions (if needed)
- Only if certain respondents should be excluded. Keep to one or two.
- **Do not telegraph the qualifying answer.** Embed the criterion among plausible decoys, and
  avoid a yes or no on the exact qualification.
- Disqualifying logic goes in the notes only, never shown to the respondent

#### Core question sections
- Two to four thematic sections, each with a short header
- Each section maps to a research question or assumption from the brief

#### Closing
- One optional open text field: "Is there anything else you'd like to share?"
- A thank you message

### Question types

| Type | Use when |
|---|---|
| Multiple choice (single answer) | Categorical data, one answer |
| Multiple choice (multi-select) | Select all that apply |
| Rating scale | Measuring an attitude. See the scale rules below. |
| Ranking | Prioritising options |
| Open text (short) | Brief reasons or labels |
| Open text (long) | Rich responses. Use sparingly, since coding costs. |
| NPS (0 to 10) | Likelihood to recommend. A relationship measure, not a usability measure. |

### Scale and wording rules, from the library

- **Prefer item-specific response options to agree or disagree.** "How satisfied are you with X?"
  not "I am satisfied with X: agree or disagree". It is the main mitigation for acquiescence.
- **Label every point.** Fully labelled scales are more reliable than numeric-only.
- About **7 points for bipolar** scales and about **5 for unipolar**, with diminishing returns
  beyond. This is `(unverified)`, so state it as the working default and not as settled.
- **Include a midpoint on bipolar scales** unless there is a reason to force a choice.
- Keep scale direction **consistent** throughout. Do not randomise an ordinal scale. Randomise
  unordered options.
- One idea per question, never double-barrelled
- Neutral phrasing, balanced stems
- No negation, no absolutes such as "always" or "never"
- **Specify the reference period.** "In the past 7 days", not "recently"
- Options **mutually exclusive and exhaustive**, with "Other (please specify)", "Not applicable" or
  "I don't know" where relevant
- Use a **filter question** before any question that assumes a behaviour
- No jargon. Match the audience's language.
- Keep open text optional where possible

### Length

| Target time | Approximate questions |
|---|---|
| 3 minutes | 8 to 10 |
| 5 minutes | 12 to 15 |
| 7 minutes | 18 to 22 |

Err shorter. The one verified result: in an opt-in web survey, announced lengths of 10, 20 and 30
minutes gave start rates of 75%, 65% and 62%, so a longer announced length meant fewer people
started at all. No clean "X minutes gives Y% drop-off" benchmark with a primary source exists, so
treat any such rule as convention.

### Draft question format

For each question:

**Q[N]: [Question text]**
*Type:* [Question type]
*Maps to:* [Research question or assumption it addresses]
*Options:* [If applicable]
*Note:* [Guidance on interpreting responses. Not shown to the respondent.]

### Output

Produce the question set as a Word document. Use the docx skill (in Claude Code, invoke
`anthropic-skills:docx`; on claude.ai, read `/mnt/skills/public/docx/SKILL.md`) before writing any
document code.

**Filename:** `Survey Questions - [Project Name].docx`

**Formatting:**
- Font: Arial, 12pt
- Page size: A4, 1 inch margins
- Section headers as Heading 1
- Question numbers in bold
- Answer options as a bullet list
- Notes in italics
- UK English throughout

**Include on the first page** a short "What this survey can and cannot tell you" box: it measures
what respondents say, who it cannot reach, and the behavioural method that should accompany it.

---

## Bias evaluation mode

### Input

Accept the shared survey: a list of questions, with or without answer options.

### What to check

Check every question against the library's entries. Note both the bias and **where it enters**.

- **Question wording:** leading and loaded, double-barrelled, negation, absolutes, assumed
  behaviour, false dichotomy, unspecified reference period, options not mutually exclusive and
  exhaustive
- **Response styles:** acquiescence, social desirability, extreme and midpoint responding,
  satisficing, straightlining
- **Order and context:** question-order effects, primacy and recency, anchoring and framing
- **Memory:** recall and telescoping
- **Who answers:** coverage, nonresponse, self-selection
- **After the answers:** coding of open responses

Not every entry applies to every survey. Check what is actually present.

### Evaluation output

Present the evaluation inline, not as a document, so the user can review and discuss before
deciding whether to export.

For each biased question:

**Q[N]: [Original question text]**
*Bias type:* [Type, and where it enters: wording, response style, order, memory, who answers]
*Why it's biased:* [One sentence]
*Improved version:* [Rewritten with neutral phrasing]
*Changes made:* [Brief note on what changed and why]

Then a "Questions with no bias found" section listing only the number and text.

Where a rewrite rests on an `(unverified)` or `(convention)` rule, say so in a few words, so the
user can weigh it.

### Summary

- Total questions reviewed
- Number with bias identified
- Most common bias type
- One sentence recommendation, for example "Focus on removing leading language, which appears in
  X of Y questions"
- **One sentence on what the survey cannot establish**, and what would

### Export

If the user wants to export, produce the corrected question set as a Word document in the same
format as Draft mode.

**Filename:** `Survey Evaluation - [Project Name or date].docx`

---

## Brief evaluation mode

### Input

Accept both the brief and the survey. Extract from the brief the research questions and
assumptions, the intended audience and the stated objectives.

### Check 1, Coverage

Map every survey question to the research questions and assumptions. Identify:

- **Gaps:** research questions no survey question addresses
- **Orphaned questions:** survey questions that map to nothing in the brief
- **Thin coverage:** research questions addressed by only one question
- **Wrong instrument:** research questions that are behavioural, or need a *why* answered by
  probing, which no survey question can address however many there are

Open with a coverage table:

| Research question or assumption | Questions that address it | Rating |
|---|---|---|
| [RQ1] | Q3, Q7 | Good |
| [RQ2] | Q5 | Thin |
| [RQ3] | None | Gap |
| [RQ4] | None possible | Wrong instrument |

Ratings: **Good** is two or more questions adequate to it. **Thin** is only one. **Gap** is none.
**Wrong instrument** is a question a survey cannot answer, with the method that can.

After the table, list orphaned questions and suggest removing them or naming which assumption they
serve.

### Check 2, Bias

Run the bias check from Bias evaluation mode on every question, in the same format.

### Summary

- Total questions reviewed
- Coverage: how many research questions are good, thin, gap or wrong instrument
- Bias: how many questions, and the most common type
- Top recommendation, for example "Add two or three questions for RQ2, remove Q8, and pair the
  survey with usability testing for RQ4"

### Export

If the user wants to export, produce a revised survey as a Word document with gaps filled and bias
corrected.

**Filename:** `Survey Review - [Project Name or date].docx`

---

## Tone and language

- UK English throughout
- No em dashes in anything the user will read, send or publish

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose a new entry when** a bias or design problem is present that the library lacks and a named
source supports it. Use the survey-methodology term where one exists. **Do not propose** a
restatement of an existing entry, or a borrowed term from another field presented as a survey
term. If it is the user's own standing practice, it is `(house)`.

**Format:**

> **New [bias / scale rule / screener rule] proposed: [Name]**
>
> **Where it enters:** the TSE component and, if on the measurement side, the response stage.
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing entry]:** one sentence.
>
> **Source:** a named source, or "none, this would be `(convention)`".
>
> **Evidence in this survey:** the question that prompted it.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit `references/bias-types.md` in place, matching the surrounding
format including both tags, tag every claim, add a line to the change log, and confirm what
changed.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai is
read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown to paste into `references/bias-types.md`, and note the skill needs repackaging:

```
cd <the survey-questions-v2 directory>
zip -qr ../survey-questions-v2.skill SKILL.md README.md references/
```

---

## Standalone usage

If invoked directly with no content shared, open with:

> "I can help in three ways:
> - Share a **research brief** and I'll draft a survey from it
> - Share an **existing survey** and I'll check every question for bias and propose rewrites
> - Share **both a brief and a survey** and I'll evaluate whether the survey covers your research
>   questions and flag any bias
>
> What would you like to do?"
