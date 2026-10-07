# ux-research-brief

Plans UX research. Takes a vague research need to an approved plan and a justified set of methods, chosen from a library of 20 rather than from memory, then hands each method to the skill that can run it. Produces a Word brief, an HTML report with a method landscape chart, or both, as you choose at the start.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions-v2` and `desk-research`. Each works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/ux-research-brief ~/.claude/skills/ux-research-brief
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/ux-research-brief/SKILL.md ] && echo OK || echo BROKEN
```

**claude.ai.** Upload `ux-research-brief.skill`. Uploaded copies are read-only, so the skill cannot save an
approved addition to its library. It will say so and hand you the text to paste in.

## Use

> "I want to do some research on our checkout flow."

It asks for context and the output format together, then works through the project, the research questions and the audience. It places each research question on the dimensions and **stops for you to confirm the placement** before filtering the library, because that step is the weakest in the skill.

## How solid the library is

**Strongest library in the family.** A real taxonomy: three published axes from NN/g (Rohrer, 2022) and 20 classified methods. Six methods are placed as the source states; the rest are placed from their definitions, because the source chart is an image with no extractable coordinates. Every `Cannot tell you` line is the library's own reasoning, tagged `(derived)`.

Every claim in the library is tagged with how well it is sourced:

```
(verified)    retrieved and read
(unverified)  a named source, reached through a secondary summary
(convention)  widely repeated practice, no primary source
(derived)     the library's own inference
(house)       Rob's standing practice, not citable and not overridden by a source
```

Two house rules apply across the family: a minimum of 6 participants for any qualitative round,
and every stated preference is checked inside the session by a specific question that could
disprove it.

## Adding your own skill for a method

The library's `Executed by:` field on each method is the only place a specialist skill's name
appears. To connect a new skill, change that one line in `references/methods.md`. Nothing else
needs editing, and the orchestrator reads the field at run time.
## What is in here

```
SKILL.md              the process
README.md             this file
references/methods.md the library
```

`references/methods.md` holds the 20 methods, three dimensions, three phases, and what each method cannot tell you. It lives in its own file so it can be amended without touching
the process. It is a first pass and expected to change. When the skill meets something the library
lacks, it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd ux-research-brief && zip -qr ../ux-research-brief.skill SKILL.md README.md references/
```
