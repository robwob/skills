---
name: usability-test-plan
description: >
  Use this skill to draft a usability test plan for UX research. Triggers include: 'usability
  test', 'usability testing', 'test plan', 'moderated test', 'unmoderated test', 'task scenarios',
  'moderator guide for testing', 'usability benchmarking', or when the ux-research-brief
  orchestrator hands off a usability testing activity. Works standalone (just provide the research
  context) or as part of the full brief flow. Asks whether the test is moderated or unmoderated,
  sizes the sample from a reference library, and reports every stated rating next to the observed
  record. Always use this skill when someone needs to plan or script a usability testing session.
---

# Usability Test Plan Skill

## Purpose

Draft a complete usability test plan: objectives, methodology, task scenarios, a moderator guide,
an analysis plan, and an observer note-taking template. Works standalone or when invoked by the
`ux-research-brief` skill.

The plan's defining feature is that **a participant's stated rating is never reported on its
own**. It sits next to what they actually did, and where the two disagree, the disagreement is the
finding.

---

## The library

**`references/task-design.md` holds task-scenario writing, sample size, think-aloud, moderated and
unmoderated testing, success measures, satisfaction instruments and severity rating, with each
claim tagged for how well it is sourced. Read it before drafting.**

Do not work from memory. It is in two halves and they are not equally solid:

- **Sample size, success measures, satisfaction instruments and severity** have real published
  structure, with formulas, named scales and benchmark numbers.
- **Task-scenario writing has no taxonomy.** It is a flat list of principles that independent
  sources agree on. Treat it as a checklist, not a framework.

Its claims carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`, `(house)`. Do not
quote an `(unverified)` figure as established.

---

## House rules

These are Rob's standing practice and they outrank any source that disagrees.

- **Minimum 6 participants** per audience segment. Not 5. The five-user rule is contested rather
  than settled, and the library lays the argument out. Nielsen's 85% is an average, and Faulkner
  found that groups of 5 range from 55% to 99% of problems. Six is the hedge.
- **Corroborate stated ease against the observed record.** Someone who says a task was easy after
  backtracking twice and taking three minutes has given you a failed claim, not a satisfaction
  score.

---

## Input

You need the following before drafting. If invoked standalone, ask for anything missing:

- **Research questions or assumptions**: what the test needs to evaluate
- **What is being tested**: prototype, live product, a specific flow or feature
- **Fidelity**: low-fi wireframes, hi-fi prototype, or live product
- **Audience**: who the participants are
- **Moderated or unmoderated**: **always confirm this with the user, even when it is passed in**
- **Session length**: default to 60 minutes if not specified
- **Formative or summative**: finding problems to fix, or measuring performance against a
  baseline or a competitor. It changes the sample size entirely.

If called from the `ux-research-brief` orchestrator, the context is passed in and may include a
recommendation on moderation, derived from the question's placement and the project's phase.
**Treat that as a default and confirm it** with one line, for example: "The brief points to
moderated, since you need to know why people stall. Is that right, or do you need unmoderated?"
This skill also runs standalone and the user may have a constraint the orchestrator does not know
about, so it asks. It does not re-interrogate the rest.

---

## Process

### Step 1, Settle the participant count

**Qualitative and formative, the default case:** minimum **6 per audience segment**. For two
distinct audience groups, 6 each. For three or more, 6 each where the budget allows and never
fewer than 4.

State what that buys, so the user is choosing with their eyes open. From the library, the chance
that at least one participant meets a given problem:

| Problem affects | Chance of seeing it with 5 | With 18 |
|---|---|---|
| 33% of users | 97% | over 99% |
| 10% of users | 41% | 85% |
| 5% of users | 23% | 61% |

Six sits just above the first column. It catches the common problems well and is close to blind to
anything affecting one user in twenty. Say that. Also say that **running several small rounds beats
one large one**, which is Nielsen's own caveat and usually gets dropped.

**Summative or benchmarking:** the qualitative floor does not apply. Use the library's table: 20
for a quantitative study, 30 to 60 for GOV.UK's service benchmarking, around 93 for a 10% margin
of error on completion rate. Where these disagree, **lay them out and say why**. Do not pick one
silently.

### Step 2, Write the tasks

**3 to 5 tasks.** The only authority-backed upper bound is GOV.UK's: no more than 5 tasks per
participant, up to 10 minutes each. Go beyond 5 only if the user insists, and say why it is a
risk.

For each task:

**Task [N]: [Short label]**
*Objective:* [Which research question or assumption this addresses]
*Scenario:* [The realistic framing given to the participant, second person, present tense]
*Task:* [The specific thing they are asked to do]
*Success criteria:* [What counts as complete, and how the levels below are judged]
*Things to watch for:* [Moderator note: behaviours, hesitations, errors to observe]

**Task writing rules**, from the library:
- **Give context and a goal, not instructions.** "Imagine you've just received an invoice..."
  not "Click on invoices".
- **Realistic.** If the participant would never do it, they will complete it without engaging with
  the interface.
- **Actionable.** "Use [site] to find a film you'd like to see on Sunday", not "Tell me where
  you'd click next". Do not let a task collect a claim where it could collect a behaviour.
- **No clues and no steps.** Step descriptions contain hidden hints. **Check the task wording
  against the interface's own labels**: if the task says "find the admission form" and the nav
  item says "Admission forms", the task has been completed by reading it.
- **A clear end state.** The participant must know when they are done.
- **One goal per task.** Do not combine steps.
- Brief, in the participant's language, and challenging enough to find problems.

### Step 3, Define success

Success has **levels**, not a score.

- Complete success
- Success with a minor issue
- Success with a major issue
- Failure, split into **gave up** and **thought they had finished but had not**

That last category is invisible in a binary measure and it is the one that reaches production.

**Report the distribution across levels. Do not assign numbers to the levels and average them.**
The common practice of scoring partial success as 0.5 is warned against by Nielsen's own article,
because the levels are ordinal labels and not interval values.

### Step 4, Choose the stated measures

- **Per task:** SEQ, the Single Ease Question. "Overall, how difficult or easy was the task to
  complete?" Seven points, labelled at the endpoints, asked straight after each task. The published
  average is about 5.5.
- **Per session:** SUS if the session can afford ten items, UMUX-Lite if two is all it can.
  SUS average is 68.
- **Do not use NPS** as a usability measure. It is a loyalty measure and answers a different
  question.

Keep SEQ's endpoint labelling even though scale-design literature favours labelling every point.
The 5.5 benchmark depends on that format and changing it breaks comparability.

### Step 5, Choose the think-aloud protocol

Use the **plain instruction**: "keep talking, say whatever comes to mind." Do not ask participants
to explain or describe their thinking, because that is the version the evidence says changes
performance. Moderator interjections during a task are limited to a neutral reminder to keep
talking. **Save every probe for after the task**, since poorly timed questions are the main way
facilitators bias a test.

**Task times collected under think-aloud are inflated** by something in the order of 20 to 40%,
and the size is unpredictable. Do not compare them across a think-aloud and a silent condition,
and do not benchmark them against published norms collected under a different protocol.

### Step 6, Plan the analysis

- **Severity.** Nielsen's 0 to 4 scale: 0 not a problem, 1 cosmetic, 2 minor, 3 major, 4
  catastrophe. Weigh **frequency, impact and persistence**. These are factors to consider, not a
  formula. Do not present them as multiplied together.
- **Stated against observed.** For every task, compare the SEQ rating with the success level, time
  and errors. Flag every task where they disagree, and report that disagreement as a finding.

---

## Document structure

### 1. Test objectives
Restate the research questions or assumptions as evaluative objectives. Example: "Determine
whether users can complete onboarding without assistance."

### 2. Methodology
- Moderated or unmoderated, and why
- Remote or in-person
- What is being tested, and at what fidelity
- Formative or summative
- Participant count, with the reasoning from Step 1, and profile
- Think-aloud protocol

### 3. Task scenarios
As Step 2.

### 4. Moderator guide

**Before the session:**
- Setup checklist: prototype or product ready, recording software, consent form
- Brief the observers on their role, including that they note behaviour and do not interrupt

**Opening script:**
- Welcome and introduce yourself
- Explain the purpose: testing the product, not the participant
- Confirm recording consent
- Explain think-aloud: "As you go, please keep talking. Say whatever comes to mind, what you're
  looking at, thinking or feeling. There are no wrong answers."
- Run a short practice think-aloud on something unrelated, for example "Tell me what you'd do to
  make a cup of tea"

**During tasks:**
- Introduce each task by reading the scenario aloud
- If the participant goes quiet: "Please keep talking."
- **No other prompts during a task.** Probes wait until it ends.
- Intervene only if the participant is completely stuck for a long stretch or distressed, and
  note that you did
- After each task, ask SEQ, then probes: "What did you expect to happen there?", "Was anything
  unclear?"

**Closing:**
- "What was your overall impression?"
- "Was anything surprising or confusing?"
- "Is there anything you'd change?"
- SUS or UMUX-Lite, if used
- Thank and close

**For an unmoderated test**, replace the above with: task wording that cannot be misread, since
there is no one to recover from it; a note that no follow-up is possible; and a recommendation for
which tool to use. Unmoderated suits specific elements, not a comprehensive design review.

### 5. Observer note-taking template

One row per task per participant. **The stated rating and the observed record sit side by side.**

| Task | Success level | Time on task | Errors and backtracks | SEQ (stated) | Stated and observed agree? | Severity (0 to 4) | Quotes | Observations |
|---|---|---|---|---|---|---|---|---|
| Task 1 | Complete / minor / major / gave up / thought done | | | 1 to 7 | Y / N | | | |

A plan that collects SEQ or SUS without the paired behavioural record is incomplete.

---

## Tone and language

- UK English throughout
- Moderator notes in italics
- No em dashes in anything the user will read, send or publish

---

## Output

Produce the plan as a Word document. Use the docx skill (in Claude Code, invoke
`anthropic-skills:docx`; on claude.ai, read `/mnt/skills/public/docx/SKILL.md`) before writing any
document code.

**Filename:** `Usability Test Plan - [Project Name].docx`

**Formatting:**
- Font: Arial, 12pt
- Page size: A4, 1 inch margins
- Section headers as Heading 1
- Task labels as Heading 2
- Moderator notes in italics
- Tables using proper docx table formatting, never plain text grids
- UK English throughout

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose** a new measure, scale or protocol when a named source supports it and the library lacks
it. **Do not propose** a restatement of an existing entry, or a personal preference dressed as a
finding. A user's own standing practice is `(house)` and is recorded as such.

**Format:**

> **New [measure / protocol / rule] proposed: [Name]**
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing entry]:** one sentence.
>
> **Source:** a named source, or "none, this would be `(house)` or `(convention)`".
>
> **Evidence on this plan:** what prompted it.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit `references/task-design.md` in place, matching the surrounding
format, tag every claim, add a line to the change log, and confirm what changed.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai is
read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown to paste into `references/task-design.md`, and note the skill needs repackaging:

```
cd <the usability-test-plan directory>
zip -qr ../usability-test-plan.skill SKILL.md README.md references/
```

---

## Standalone usage

If invoked directly, open with:

> "I'll draft a usability test plan for you. Can you tell me what's being tested, who the
> participants are, whether it'll be moderated or unmoderated, and what you're trying to find out?"

Then proceed once you have sufficient context.
