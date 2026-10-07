# discussion-guide

Drafts a discussion guide for user interviews. Every question that asks what someone thinks is paired with a specific question about a real occasion that could contradict it.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions` and `desk-research`. Each works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/discussion-guide ~/.claude/skills/discussion-guide
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/discussion-guide/SKILL.md ] && echo OK || echo BROKEN
```

**claude.ai.** Upload `discussion-guide.skill`. Uploaded copies are read-only, so the skill cannot save an
approved addition to its library. It will say so and hand you the text to paste in.

## Use

> "Draft a discussion guide for our onboarding research."

Share the research questions, the audience and the session length. The guide comes back with each attitude question paired, each question mapped to a research question in a moderator note, and a self-check against the common mistakes.

## How solid the library is

**Prose, not a taxonomy, and deliberately so.** No canonical classification of interview question types exists in UX, and the file says so. It is organised by task, with four named techniques: the funnel, critical incident, grand tour and laddering. Anything attributed to Portigal, Rubin and Rubin, Young or Spradley is tagged `(unverified)`, since none could be read directly.

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

## What is in here

```
SKILL.md                         the process
README.md                        this file
references/question-craft.md     the library
```

`references/question-craft.md` holds how to write, order and probe interview questions. It lives in its own file so it can be amended without touching
the process. It is a first pass and expected to change. When the skill meets something the library
lacks, it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd discussion-guide && zip -qr ../discussion-guide.skill SKILL.md README.md references/
```
