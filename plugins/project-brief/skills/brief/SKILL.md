---
name: brief
description: >
  Use this skill at the start of a project, before any design or code, to define why it is being
  done and derive the plan from that. Interviews for the four opening answers (why now, goal, core
  functions, what success looks like), then the constraints, then writes brief.md containing both
  the brief and a derived stage route: which design stages and which build stages this project
  needs, in what order, with review gates. Triggers include: "write a brief", "start a new project",
  "help me define this", "what should we build", "turn this into a plan", "I have an idea for X",
  or handing over a rough brief or notes and asking what to do with them. Also use to rework an
  existing brief that was written without a plan attached. Produces a single brief.md in the
  project folder. Does not design or build anything.
---

# Brief Skill

## Purpose

A project starts with a brief. The brief is not paperwork. It is the artefact the plan is derived
from, so a brief that cannot produce a plan has failed.

This skill does two things, in order:

1. **Interviews** for the sixteen sections in `references/sections.md`, refusing vague answers on
   the four that always get fudged.
2. **Derives the route** from those answers using `references/stages.md`: which stages this project
   needs, which it skips, in what order, and where the work stops for review.

It writes one file, `brief.md`, into the project folder. It does not design, does not build, and
does not open Paper.

---

## Before starting

Read `references/sections.md` and `references/stages.md` in full, and resolve the house rules. Do
not work from memory. The acceptance tests in the sections file are the whole value of the skill and
they are not guessable.

**The house rules** are the only part of this skill tied to a particular person or workspace. This
skill reads four sections: `## Writing`, `## Reuse`, `## Stages` and `## Constraints`.

**Lookup, per section:** a project `.house-rules.md` (searched upward from the project folder), then
the user file `~/.config/house-rules/house-rules.md`, then the legacy `~/.claude/house.md`, then
`references/house-rules.md`, the bundled fallback and template. The first file with a non-empty
section wins that section whole. Sections are never merged across files. A section may point to
another file for the detail, in which case follow it.

Where a section is absent or empty everywhere, use the default `references/house-rules.md` names
for it and say which default you used. When you hand back the brief, add one line saying what was
used, for example: "Applied: Constraints from project `.house-rules.md`, Writing by default." If
only the bundled fallback was used, add: "`house-rules-setup` can create your own."

If the user has handed over an existing brief, notes or a chat transcript, read it first and
pre-fill every section you can from it. Then interview only for what is missing or vague. Never ask
for something already stated.

---

## The interview

Ask in three rounds. Do not move to the next round until the current one passes its tests.

### Round 1: why

Sections 1 to 4. Ask all four at once, then push back on each answer that fails its test in
`references/sections.md`.

**This round is a gate.** If section 4 cannot be answered, the project is not ready to start and
the honest output is to say so rather than write a brief. Two legitimate ways through: define
success properly, or name the smallest thing that would let success be defined, and make that the
whole project.

The most common failure is a success criterion that restates the goal. "Success is that I can see
if I am getting fitter" is the goal again. "Success is that I open it on a Sunday and know within
five seconds whether to make next week harder or easier" is a criterion, because it can be failed.

### Round 2: shape

Sections 5 to 12. These determine which stages the project needs, so a thin answer here produces a
wrong route, not just a thin brief.

Three that carry the most weight:

- **Section 8, inputs and data.** Ask directly whether a real sample has been seen. Not whether one
  could be obtained. Whether it has been looked at. The answer changes the route more than any
  other single answer in the brief.
- **Section 6, non-goals.** Keep asking until there are at least three. A project with no non-goals
  has no edge, and scope can only grow.
- **Section 7, the load-bearing principle.** One sentence the build must not violate. If the user
  cannot name one, propose the candidate you can see in their answers and let them accept or reject
  it. Do not leave it blank.

### Round 3: derived

Sections 13 to 16. The user does not answer these. You work them out and show them the result.

- **Section 13, reuse audit.** Do the search. Look where the house rules say to look, plus any
  project named in the answers. Report components, utilities and patterns that already do part of
  this job, with paths. "Nothing found" is a valid result only after actually looking, and say
  where you looked.
- **Section 14, stage route.** Apply the rules in `references/stages.md`. State every stage
  included with its activity type, and, just as importantly, every stage skipped with the reason. A
  route that includes everything has not made a decision.
- **Section 15, build order.** Order the stages by the four ordering principles in
  `references/stages.md`, and mark the review gates.
- **Section 16, definition of done.** Derived from section 4, narrowed to phase 1. It must be a
  state that can be observed, not a feeling of completion.

Show sections 13 to 16 back before writing the file. This is where the user disagrees, and it is
cheaper to disagree with a proposed route than with a written one.

---

## After the brief is written

The brief is not permission to start. Two separate approvals, and they are different things.

### 1. Approve the plan

Present the whole route as one thing and get it approved before any stage begins. Not the brief, the
plan: the stages, their order, the phases, the gates. This is the last cheap moment to disagree.

### 2. Approve each stage before it starts

Every stage in the route begins by saying what it is about to do and waiting. Not a summary of the
stage name. State:

- what the stage will produce
- what it will touch or create
- what it needs answered before it can run
- roughly how long it will take

Then stop. Do not begin on the same turn as the announcement, and do not roll the announcement of
the next stage into the delivery of the last one, because the two get read as a single message and
the approval gets skipped.

**This is separate from the gates.** A gate approves the output of a stage that has finished. A start
approval agrees to the stage running at all. Both exist, both stop the work, and the most common
failure is treating a gate as covering the next stage as well.

**If a stage turns out to be larger than announced, stop and re-announce.** The approval was for the
stage as described, not for wherever it leads.

Record both rules in the brief under section 15, so a session that reads `brief.md` without this
skill loaded still runs the plan the same way.

---

## Rules for the route

Read `references/stages.md` for the catalogue and the inclusion rules. Four things override
everything in it:

1. **Anything that could invalidate later work goes first.** Unseen data, an unsettled approach and
   an unverified technical assumption all belong before the first design stage, because designing
   against a guess means designing twice.
2. **The first deliverable is the cheapest thing that can be reviewed.** Not the easiest to build,
   the fastest to get a real reaction to.
3. **One instance, approved, then propagate.** Never route a stage that produces five of something
   before a stage that produces one and stops.
4. **Fragile work is deferred.** Authentication, scheduled jobs, deploys and anything with
   credentials go into phase 2 unless phase 1 is useless without them.

---

## Writing the file

Write `brief.md` in the project folder, using the section order in `references/sections.md`.

- Record the reasoning behind decisions, not just the decision. A brief that says what was rejected
  and why is the one that survives someone asking "why didn't we just...".
- Mark anything unresolved as an open question with what resolves it. Do not smooth over a gap with
  a plausible sentence.
- Follow the writing style in the house rules.
- Use plain stage names, never the internal codes from `stages.md`.
- Keep it as short as the project allows. The sections are required, the length is not.

After writing, update the project's agent instructions file, `CLAUDE.md` or `AGENTS.md`, with the
goal, the load-bearing principle, the route and the current stage. Create one if the project has
none. The brief is the source; that file is how the next session finds it and how it learns to run
the plan the same way.

---

## What this skill does not do

- It does not design. When the route reaches a design stage, the next step is that stage, run by
  whoever or whatever the house rules name for it.
- It does not estimate in days. Section 12 is an effort ceiling, meaning the point past which the
  project is not worth it, which is a different question.
- It does not write a brief for a project that cannot state success. It says so instead.
