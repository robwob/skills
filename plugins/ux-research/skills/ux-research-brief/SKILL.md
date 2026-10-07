---
name: ux-research-brief
description: >
  Use this skill whenever the user wants to plan, scope, or brief a UX research project.
  Triggers include: any mention of 'research brief', 'UX research', 'user research', 'research
  plan', 'which research method', 'what should we test', 'assumptions to test', or any request to
  figure out what research to run. Also trigger when someone says they want to 'understand users',
  'validate a design', 'test with users', or 'find out if users can do X'. Runs a structured
  conversation through intake, research definition, plan review and method selection, choosing
  from a library of 20 methods rather than from memory, then hands execution to specialist skills.
  Produces a Word brief, an HTML report with a method landscape chart, or both, as the user
  chooses at the start. Use it even when the request is phrased casually, for example 'I want to
  do some research on our checkout flow'.
---

# UX Research Brief Skill

## Purpose

Take a research need from vague to an approved plan and a justified set of methods, then hand
each method to the skill that can execute it.

The skill's real job is **method selection**. It places each research question on a small set of
published dimensions, filters a library of 20 methods against that placement, and states what each
chosen method cannot tell you. It does not recommend from habit, and it does not reach for the
familiar three.

This skill covers Stages 1 to 4 and the handoff. Execution belongs to the specialist skills.

---

## The library

**`references/methods.md` holds 20 UX research methods, each placed on three dimensions and
assigned a phase, with what it answers, what it cannot answer, what it needs, and which skill
executes it. Read it before doing anything else in this skill.**

Do not work from memory. The method set changed in the 2022 revision of the source article, and
the older list is the one most people, and most models, remember. Methods that list includes and
the library does not: true-intent studies, email surveys, camera studies, usability-lab studies.
Methods the library has that the older list lacks: tree testing, contextual inquiry, analytics.
The file is the only current version.

Four rules from the library govern how you use it:

- **A method may sit mid-axis, and so may a question.** Forcing a side is the most likely way to
  get a recommendation wrong.
- **Both poles of every dimension are real positions.** Qualitative is not better than
  quantitative, it answers a different question. The `Cannot tell you` field exists to state the
  cost of a method's position, and you must surface it for every method you recommend.
- **The library is a list to select from, not a checklist to complete.** A project runs two to
  four of the 20, not all of them.
- **Every change to the library is approved first.** See **Proposing an addition**.

The library tags every claim with how well it is sourced: `(verified)`, `(unverified)`,
`(convention)`, `(derived)` or `(house)`. **Almost every `Cannot tell you` line is `(derived)`**,
which means it is this library's reasoning from the method's position and not a published
finding. When one of those lines is the reason a method is being ruled out or flagged, say so in
the same breath, so the user can push back on it.

---

## Terminology

| Term | Definition |
|---|---|
| **Phase** | Where the project sits: strategize (generative), design (formative), or launch and assess (summative). |
| **Question** | One research question. A project has several and they rarely sit in the same place, so each is placed separately. |
| **Dimension** | An axis both a question and a method sit on: attitudinal to behavioural, qualitative to quantitative, and context of product use. |
| **Method** | One of the 20 in the library. Selected from the file, never invented. |
| **Protocol** | This project's instance of a method. Produced by the specialist skills, not stored. |

---

## House rules

These are Rob's standing practice. They are decisions, not inputs, and where a source disagrees
the library says so and the rule still holds. Full statements are in `references/methods.md`.

- **Minimum 6 participants** per audience segment for any qualitative round. Not 5.
- **Corroborate every stated preference inside the session.** Anywhere a method asks what someone
  thinks of something, the instrument must also ask the specific question that would prove or
  disprove it. A claim the follow-up does not support is not a finding, and the contradiction is
  the result.

This is different from the **triangulation check** in Stage 4, which asks whether the *set of
methods* spans more than one kind of evidence. One runs across a study, the other inside a
session. Keep the two names apart when you speak to the user.

---

## Stage 1: Intake

**Open with one turn that asks for the context and the output format together**, so the user is
not asked two things before you know anything about the project:

> "Let's build your research brief. Two quick things first.
>
> Do you have any existing context to share, such as a project brief, problem statement, design
> spec or ticket? Or shall we start from scratch?
>
> And what would you like at the end: a Word brief to share and sign off, an HTML report with the
> method landscape chart and the reasoning behind each choice, or both?"

Record the format. It is confirmed again at Stage 3, so the user has a second chance to change it.
If they choose both, both files are produced from the same approved plan.

Then establish four things. If they shared context, extract what you can and ask only for what is
missing. Summarise and ask them to confirm.

1. **What product or service this is about.**
2. **What has prompted this research right now.**
3. **What exists today:** nothing yet, a design, or something live. This decides the phase in
   Stage 4, so do not skip it and do not infer it from the answer to question 2.
4. **The timeline.** How long until the findings are needed.

**Do not ask about participant access or moderation.** Access is assumed, since someone using this
skill is planning research they can run. Moderation is a property of the method, and asking about
it would let the user pre-select the method before the library has been consulted. Cost and
participant count are reported on each recommended method, not used to filter.

Once confirmed, move to Stage 2.

---

## Stage 2: Define the research

Help the user articulate three things.

### 1. Research questions
Open, neutral questions about user behaviour, needs or experience. Push back gently on questions
framed as business goals.
- Good: "How do users currently decide which plan to choose?"
- Bad: "Does our new onboarding work?" or "Prove our design is better."

**These are the input to Stage 4.** They are placed on the dimensions one at a time, so each needs
to be a single question. Split any that contain two.

### 2. Assumptions to test
What the team believes that research could confirm or challenge. Prompt with: "What are you
assuming about your users that you haven't yet validated?"

### 3. Audience
User type, relevant characteristics, any screening criteria. Participant counts are decided by the
method, so do not ask for one here.

Work through each conversationally. When all three are solid, summarise and ask:
"Does this capture what you're trying to find out? Happy to refine before I draft the plan."

---

## Stage 3: Research plan for review

Present the plan in the chat:

---
**Research Plan: [Project Name]**

**Background and context**
[1 to 2 sentences on the project and what prompted the research]

**Where the project is today**
[Nothing yet / a design / something live]. **Timeline:** [...]

**Research questions**
1. [Question]
2. [Question]

**Assumptions to test**
- [Assumption]

**Audience and recruitment criteria**
[Who, and any screening criteria]

**Output:** [Word brief / HTML report / both]
---

Ask: "Does this look right, including the output format? Tell me any changes and I'll update it
before I work out which methods fit."

**Do not proceed to Stage 4 until the user explicitly approves the plan.**

---

## Stage 4: Method selection

Three passes against the library, then two checks. Nothing here is invented: 20 candidates in,
two to four out.

### Pass A: Place each question, and stop

Place **each research question** on the two main dimensions, using the source's own tests:

- **Say or do?** Is it about what people believe, prefer, remember or would say, or about what
  they actually did? Attitudinal, behavioural, or mid-axis.
- **Why or how many?** Is it a *why* or *how to fix* question, or a *how many* or *how much*
  question? Qualitative, quantitative, or either.

**This is the weakest step in the skill, and it is a gate for that reason.** The classification
tracks how a question is worded as much as what it asks, and a wrong placement produces a
confident wrong recommendation that looks rigorous all the way down. Several questions read
differently by their opening word:

- "Why do users abandon at the plan step?" The "why" says qualitative. But abandonment is
  behaviour, so it also sits behavioural, and the answer may need two methods.
- "Do users understand our pricing?" Understanding is a mental model, so attitudinal. But you would
  find out by watching someone choose a plan, which is behavioural.

So **show your classification and stop**:

> "Before I filter the library, here is how I've read your questions.
>
> Q1 *[question]*: attitudinal, qualitative. [One line on the reading, and where it could be read
> the other way.]
>
> Q2 *[question]*: behavioural, quantitative.
>
> Q3 *[question]*: sits mid-axis. [Which two readings, and that both are being kept open.]
>
> Does that match what you're asking?"

Allow mid-axis placement. The source itself puts usability studies and field studies in the middle
of the attitudinal and behavioural axis, because they mix self-reported and behavioural data.
Do not force a side to make the next pass tidier.

**Wait for confirmation.**

### Pass B: Derive the phase

From Stage 1, not from asking again:

| What exists today | Phase | Research type |
|---|---|---|
| Nothing yet | Strategize | Generative |
| A design that needs improving | Design | Formative |
| Something live, to measure against itself or a competitor | Launch and assess | Summative |

A project can be in two. Say so if it is. This is the dimension the previous version of this skill
had no concept of, and it is what separates generative methods from evaluative ones.

### Pass C: Intersect, then prune

For each question, take the methods whose placement overlaps the question's and whose phase
overlaps the project's. A mid-axis question overlaps methods on either side of it. Then prune on
exactly two things, and no others:

1. **Does the artefact the method needs exist?** Read the `Needs:` field. Concept testing needs an
   approximation of the concept. A/B testing needs two live designs. Analytics needs
   instrumentation already in place. A method that **rules itself out** says so in its entry.
2. **Does the timeline allow it?** Compare the timeline from Stage 1 with the time the `Needs:`
   field implies. Diary studies need weeks and field studies a day or more per participant.

Everything else about a method's cost is **reported, not filtered**: participant count, moderator
needed, specialist tooling. Access is assumed, so a heavy method is not ruled out for being heavy.
State the cost and let the user decide. Where a method is dropped, say which of the two reasons
dropped it.

Then choose. For each question, recommend the method that fits best and, where there is a real
runner-up, name it as the deeper second option. Moderation falls out of this: remote moderated
testing, in-person usability testing and unmoderated testing are three separate entries with
different placements, so the choice between them is made by the passes above and is not asked.

### Check 1: Triangulation across the set

NN/g's own guidance is to combine complementary methods and not lean on the one or two the team
knows. Check that the chosen set **spans more than one quadrant** of the two main dimensions.

- If it does, say so in a line.
- If every method sits in the same corner, say so plainly, name what the set therefore does not
  examine, and offer the nearest method from the opposite corner.

Also report the **context of use** across the set. Four methods that are all `scripted` have
learned nothing about natural use, and the brief should say that.

### Check 2: Corroboration inside each method

For every recommended method that asks people what they think, state which specific question or
observation will check the claim, using the table in the library's house rules. A recommendation
for a method with nothing to check it against, a survey on its own for example, must say that a
second method with a behavioural measure is required to support any claim about behaviour.

### Present the proposed set

For each recommended method:

**[Method name]**
*Placement:* [attitudinal/behavioural, qualitative/quantitative, context of use, phase]
*Why it fits:* [which question, and why, in one or two sentences]
*What it cannot tell you:* [from the library, flagged as derived where it is]
*What it needs:* [artefact, time, participants, including the 6 minimum where it applies]
*Checks its own claims with:* [from Check 2]

Close with the triangulation verdict, and ask:
"Would you like to adjust this set before I move to execution?"

**Do not proceed until the user approves the set.**

### Desk research

Desk research is **not one of the 20**, because the framework classifies methods by how they
engage users and desk research engages none. Offer `desk-research` as an adjunct when the brief
needs landscape context or competitor understanding, and never plot it on the chart. Its outputs
are hypotheses to test, never findings about users.

---

## Stage 5: Handoff

For each approved method, read its **`Executed by:`** field in the library. That field is the only
place a specialist skill's name appears. Do not keep a table of skill names anywhere else, and do
not recall one from memory: skills get added, and the field is how this skill finds out.

- **A skill is named.** Ask the user whether they want it run now. If yes, invoke it and pass the
  full context below.
- **`none yet`.** Say so plainly: "There is no skill for [method] yet." Still write that method's
  section into the brief from the library entry, so the brief is never limited to what happens to
  be automatable.

**Context to pass to a specialist:**
- Research questions, with their confirmed placement
- Assumptions
- Audience
- Phase, and the timeline
- The method and its placement, and any recommendation the passes produced, for example
  moderated or unmoderated, which the specialist confirms rather than takes as final
- The house rules, which still apply

How to invoke: in Claude Code, call the skill by its name. On claude.ai, read that skill's
`SKILL.md` and follow it, passing the context as its input.

---

## Output

The user chose at Stage 1 and confirmed at Stage 3. Produce what they chose. If both, produce
both from the same approved plan, so the two cannot disagree.

### The Word brief

Use the docx skill (in Claude Code, invoke `anthropic-skills:docx`; on claude.ai, read
`/mnt/skills/public/docx/SKILL.md`) before writing any document code.

**Filename:** `UX Research Brief - [Project Name].docx`

**Structure:**
1. Research background and context
2. Research questions, with their placement
3. Assumptions to test
4. Audience and recruitment criteria
5. Proposed methods and rationale, using the per-method block from Stage 4
6. Triangulation: what the set covers and what it does not
7. Appendices, populated by specialist skills where they were run

**Formatting:** Arial 12pt, A4, 1 inch margins, Heading 1 for sections, Heading 2 for subsections,
proper bullet lists (never unicode characters), UK English.

### The HTML report: `research-methods.html`

A single self-contained HTML file. All CSS and JS inline. No external dependencies except where
stated below.

**Header:** title "Research Methods", the project name, the date.

**Landscape chart (inline SVG), the centrepiece:**
- Horizontal axis: qualitative on the left, quantitative on the right.
- Vertical axis: behavioural at the top, attitudinal at the bottom, mid-axis between.
- **All 20 methods are drawn.** The chosen ones are filled in a single accent colour and labelled
  in full. The unchosen ones are small, faint and grey, labelled in a smaller size, so the user
  can see what the brief did not pick and from which corner.
- **Marker shape encodes context of use:** circle for natural, square for scripted, triangle for
  limited, diamond for decontextualized. A legend explains the four.
- Place each method from its placement lines in the library, using this table. Where a library
  line gives two values, such as `either` or `decontextualized, or natural when intercepted`, use
  the first.

| Library value | Position (0 to 1 across the chart) |
|---|---|
| qualitative | x = 0.17 |
| either | x = 0.50 |
| quantitative | x = 0.83 |
| behavioral | y = 0.17 |
| mixed | y = 0.50 |
| attitudinal | y = 0.83 |

- Methods that land in the same cell are spread in a small grid around the cell centre, roughly
  36px apart, so no two markers overlap and no label collides with another.
- **This is this skill's own rendering of the library's classification.** It is not a reproduction
  of NN/g's chart, whose per-method coordinates are not published as data. Say so in a small note
  under the chart.
- The diagram must be legible at 1200px wide.

**Triangulation verdict:** one short paragraph under the chart. Which quadrants the set spans,
which it does not, and the context-of-use spread.

**One card per chosen method**, using the same per-method block as Stage 4: placement, why it
fits, what it cannot tell you, what it needs, how it checks its own claims. Where a limit is
`(derived)`, mark it visibly as an inference.

**Download controls:**
- "Download report as PNG", client-side via `html2canvas` from a reliable CDN, with a fallback
  message if it is unavailable.
- "Download chart as SVG", via a Blob URL, not a data URI.

**HTML requirements:** font system-ui or Inter, white background, max content width 1200px
centred, a muted palette with one accent, and no saturated primaries.

Hand back the **absolute file path**, not a served link.

---

## Proposing an addition

The library is a first pass and is expected to change. **Nothing is written to it without the
user's explicit approval.** Propose, then stop and wait.

**Propose a new method when** a question genuinely sits where no method in the 20 reaches, and
forcing it into the nearest one would misrepresent what the method does.

**Do not propose a method that is a variant of an existing one.** Remote moderated testing is in
the library. Remote moderated testing over a particular tool is not a method, it is a protocol.
If it names a tool or a setting and not a different way of gathering evidence, it is a variant.

The library names methods commonly used but not in the 20, such as first-click testing, heuristic
review and journey mapping. Those are candidates for proposal when they come up, not omissions to
work around.

**Format:**

> **New method proposed: [Name]**
>
> **Placement:** attitudinal/behavioural, qualitative/quantitative, context of use, phase.
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing]:** one sentence on the distinction.
>
> **Source:** where this method is defined. If there is none, say so, and it will be tagged
> `(convention)` or `(derived)`.
>
> **Evidence on this project:** the question that prompted it.
>
> Add this to the library?

**Wait for the answer.** If declined, use the nearest existing method and note the gap.

### Adding an approved method

Only after explicit approval.

1. Edit `references/methods.md` in place, matching the surrounding format exactly: the four
   placement lines, `What it is`, `Answers`, `Cannot tell you`, `Needs`, `Executed by`, each
   claim tagged with its provenance.
2. Add it under its phase, and update the method count wherever the file states one.
3. Add a line to the file's change log.
4. Confirm what changed and where.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai
is read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown block for the user to paste into `references/methods.md`, and tell them the skill needs
repackaging afterwards:

```
cd <the ux-research-brief directory>
zip -qr ../ux-research-brief.skill SKILL.md README.md references/
```

---

## Tone and behaviour

- Conversational and collaborative. This is a dialogue, not a form.
- One or two focused questions at a time. Stage 1's opening turn is the one deliberate exception.
- Summarise and confirm at the end of each stage before moving on.
- Push back constructively when a research question is really a business goal.
- Do not assume the user's experience level. Explain a term if in doubt, without condescension.
- UK English throughout.
- No em dashes in anything the user will read, send or publish. Use commas and full stops.
