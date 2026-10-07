# usability-test-plan

Drafts a usability test plan: objectives, methodology, task scenarios, moderator guide, analysis plan and an observer template. Asks whether the test is moderated or unmoderated, sizes the sample, and reports every stated rating next to the observed record.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions-v2` and `desk-research`. Each works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/usability-test-plan ~/.claude/skills/usability-test-plan
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/usability-test-plan/SKILL.md ] && echo OK || echo BROKEN
```

**claude.ai.** Upload `usability-test-plan.skill`. Uploaded copies are read-only, so the skill cannot save an
approved addition to its library. It will say so and hand you the text to paste in.

## Use

> "I need a usability test plan for the new checkout."

Share what is being tested, the audience and the research questions. It confirms moderated or unmoderated with you even when the brief skill has already suggested one.

## How solid the library is

**Two halves.** Sample size, success measures, satisfaction instruments and severity have real published structure. Task-scenario writing has none, and is a flat list of principles independent sources agree on. The five-user argument is laid out rather than resolved, and the house minimum of 6 participants overrides the old default of 5.

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
SKILL.md                           the process
README.md                          this file
references/task-design.md          the library
```

`references/task-design.md` holds task writing, sample size, think-aloud, moderation, success measures, satisfaction instruments and severity. It lives in its own file so it can be amended without touching
the process. It is a first pass and expected to change. When the skill meets something the library
lacks, it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd usability-test-plan && zip -qr ../usability-test-plan.skill SKILL.md README.md references/
```
