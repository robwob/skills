---
name: discussion-guide
description: >
  Use this skill to draft a discussion guide or interview script for UX research. Triggers include:
  'discussion guide', 'interview guide', 'interview script', 'moderator guide for interviews',
  'user interview questions', or when the ux-research-brief orchestrator hands off a user
  interviews activity. Works standalone (just provide the research context) or as part of the full
  brief flow. Every attitude question is paired with a specific follow-up that can contradict it,
  and the questions are drawn from a reference library of question craft, not from memory.
  Always use this skill when someone needs a structured guide for conducting user interviews or
  research conversations.
---

# Discussion Guide Skill

## Purpose

Draft a complete discussion guide for user interviews or research conversations, grounded in the
research questions and assumptions provided. Works standalone or when invoked by the
`ux-research-brief` skill.

The guide's defining feature is that **no stated opinion stands alone**. Every question that asks
what someone thinks, likes or wants is paired with a specific question about a real occasion that
could prove or disprove it.

---

## The library

**`references/question-craft.md` holds the craft of writing, ordering and probing interview
questions, with each claim tagged for how well it is sourced. Read it before drafting.**

Do not work from memory. Two things about it you need to know before you start:

- **It is prose, not a taxonomy.** No canonical classification of interview question types exists
  in UX, and the file says so. It is organised by task. Do not impose a structure on it, and do
  not describe its contents as a framework. Four named techniques have their own entries: the
  funnel, critical incident, grand tour, and laddering.
- **Its claims carry tags**: `(verified)`, `(unverified)`, `(convention)`, `(derived)`, `(house)`.
  Where an entry is `(unverified)`, such as anything attributed to Portigal, Rubin and Rubin or
  Indi Young, do not quote it.

---

## House rules

These come from Rob's standing practice and outrank any source that disagrees.

- **Corroborate every stated preference inside the session.** A claim the follow-up questions do
  not support is not a finding, and the contradiction is the result. It is not a sign the
  participant was confused.
- **Minimum 6 participants** per audience segment. Say this in the guide's front matter so the
  recruit is sized correctly. Not 5.

This is not NN/g's triangulation, which means combining several methods across a study. It runs
inside one session, against one claim. Do not use the two names interchangeably.

---

## Input

You need the following before drafting. If invoked standalone, ask for anything missing:

- **Research questions**: what the session needs to find out
- **Assumptions to test**: what the team believes but has not validated
- **Audience**: who will be interviewed (affects tone, terminology and depth)
- **Session length**: default to 60 minutes if not specified
- **Product or service context**: what the research is about

If called from the `ux-research-brief` orchestrator, the context is passed in. Use it directly
without re-asking. It will include the phase and the confirmed placement of each question.

---

## Process

### Step 1, Choose the question roles

Every question in the guide has a **role**: opener, main, follow-up or probe, closer. This is the
one faceting the library supports. Main questions begin a discussion about one part of a research
question. Follow-ups pursue what an answer opened. Probes manage the conversation without adding
content.

### Step 2, Write the main questions

Map each main question to a research question or assumption. **Align each interview question
directly to the research question it serves**, and show that mapping in a moderator note, never
read aloud.

Apply the writing rules from the library:
- Open, not closed, with closed questions kept for clarification and for the very end of a funnel
- **Ask about the past, never the future.** No "would you use this", no predictions, no
  hypotheticals
- Ask for the problem, not the solution
- One thing per question
- No assumed facts, no interface or product vocabulary the participant has not used, no adjectives
  or examples that set the answer's scale

### Step 3, Pair every attitude question

For each main question that asks what someone thinks, likes, wants or finds easy, add a
**corroborating pair**: a critical-incident question about a specific recent occasion that would
show whether the claim is true.

| The claim | The pair |
|---|---|
| "I like using it" | "Tell me about the last time you used it. What were you trying to do?" |
| "It's easy to find things" | "Think of the last thing you looked for. Walk me through how you found it." |
| "I'd definitely buy that" | "When did you last buy something like it? What made you choose that one?" |

Mark each pair in the moderator notes. In the write-up, the claim and the pair are read together:
if the pair does not support the claim, **record the contradiction as the finding**.

A guide containing attitude questions with no pair is incomplete. Do not output it.

### Step 4, Order with the funnel

Within each theme, go broad to narrow: a broad open question first, open follow-ups and probes
next, closed questions last. The reason is the one the library gives: broad before narrow stops
your closed questions revealing what you care about before the participant has answered freely.

Group questions by theme, not by research question order. Order logically, ideally
chronologically or by phase of experience, with reflective questions later.

### Step 5, Self-check before output

Read every question against this list and fix any that fail:

- Does it ask about a hypothetical or a prediction?
- Is it double-barrelled?
- Does it lead, or carry an interpretation the participant is likely to agree with?
- Does it ask the participant to design a solution?
- Is the opening question closed, or screener-like?
- Does it assume a fact?
- Does any attitude question lack its pair?

---

## Guide structure

Draft the guide with these sections in order.

### 1. Introduction (about 5 mins)
- Welcome and thank the participant
- Explain the purpose: this is research, not a test of them, and there are no wrong answers
- Confirm recording consent if applicable
- Ask them to say if anything is unclear
- One easy opening question, for example "Can you tell me a bit about your role, or how you use
  [product]?"

### 2. Warm-up (about 5 to 10 mins)
- Two or three open questions to establish context and rapport
- Related to the topic, but not diving into the research questions
- Example: "Walk me through a typical week when it comes to [relevant activity]"

### 3. Core questions (about 30 to 40 mins)
- Main questions in funnel order within each theme
- Each main question labelled with the research question it serves, in a moderator note
- Each attitude question followed by its pair
- Follow-up and probe prompts beneath each:
  - "Can you tell me more about that?"
  - "What did you do next?"
  - "You said [their words]. When was that?"
  - "Has that always been the case?"
- Echo the participant's own words back. Do not substitute your interpretation of them.

### 4. Closing (about 5 to 10 mins)
- "Is there anything you expected me to ask that I haven't?"
- "Is there anything else about [topic] you'd like to share?"
- Explain what happens to the research and how the findings will be used
- Thank and close

### 5. Moderator notes (a short section for the person running the session)
- Use the guide as a checklist, not a script. Do not stick to it rigidly and do not change the
  flow abruptly.
- The more you talk, the less the participant will talk.
- Where a participant's stated view and their account of a specific occasion disagree, do not
  resolve it in the room. Note both.

### 6. Reporting note
One paragraph for whoever writes up the sessions: report each claim **and whether its pair
supported it**, never the claim alone.

---

## Timing

Add approximate timings to each section based on the session length provided. For a 60-minute
session, a working allocation is intro 5, warm-up 10, core 35, close 10.

**This allocation is a convention, not a standard.** The library records that no authoritative
split exists and that the commonly quoted figures come from vendor blogs. Present the timings as
a starting point, and recommend piloting the guide to check them.

---

## Tone and language

- Match the language to the audience. Avoid technical jargon for general consumers.
- Write as if speaking. Contractions are fine.
- Moderator notes in italics or [brackets] to distinguish them from spoken content.
- UK English throughout.
- No em dashes in anything the user will read, send or publish.

---

## Output

Produce the guide as a Word document. Use the docx skill (in Claude Code, invoke
`anthropic-skills:docx`; on claude.ai, read `/mnt/skills/public/docx/SKILL.md`) before writing any
document code.

**Filename:** `Discussion Guide - [Project Name].docx`

**Formatting:**
- Font: Arial, 12pt
- Page size: A4, 1 inch margins
- Section headers as Heading 1
- Question numbers in bold
- Probe prompts indented as a bullet list beneath each question
- Moderator notes in italics
- UK English throughout

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose a new technique or rule when** a question-writing problem comes up that the library does
not cover, and a named source supports it. **Do not propose** a restatement of an existing entry
in new words, or a personal preference presented as a finding. If it is the user's own standing
practice, it is `(house)` and is recorded as such, not dressed up with a citation.

**Format:**

> **New [technique / rule / bias] proposed: [Name]**
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing entry]:** one sentence on the distinction.
>
> **Source:** a named source, or "none, this would be `(house)` or `(convention)`".
>
> **Evidence on this guide:** the situation that prompted it.
>
> Add this to the library?

**Wait for the answer.** If declined, handle the situation within the existing entries.

### Adding an approved entry

Only after explicit approval. Edit `references/question-craft.md` in place, matching the
surrounding format, tag every claim with its provenance, add a line to the change log, and confirm
what changed and where.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai
is read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown for the user to paste into `references/question-craft.md`, and note that the skill needs
repackaging:

```
cd <the discussion-guide directory>
zip -qr ../discussion-guide.skill SKILL.md README.md references/
```

---

## Standalone usage

If invoked directly (not from the brief orchestrator), open with:

> "I'll draft a discussion guide for you. Can you share the research questions you're trying to
> answer, who you'll be interviewing, and roughly how long each session will run?"

Then proceed once you have sufficient context.
