# survey-questions

Drafts a survey from a brief, checks an existing survey for bias, or checks a survey against a brief for both coverage and bias. It also says what the survey cannot establish.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions` and `desk-research`. Each works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/survey-questions ~/.claude/skills/survey-questions
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/survey-questions/SKILL.md ] && echo OK || echo BROKEN
```

**claude.ai.** Upload `survey-questions.skill`. Uploaded copies are read-only, so the skill cannot save an
approved addition to its library. It will say so and hand you the text to paste in.

## Use

> "Check this survey for bias."  or  "Draft a survey from this brief."

Share a brief, a survey, or both, and it picks the mode. A research question a survey cannot answer is flagged as the wrong instrument, with the method that can.

## How solid the library is

**The least-verified library in the family.** Total Survey Error is the canonical framework and is citable, but it classifies where an error enters the survey and is not a list of named biases. The library crosses it with Tourangeau's response-process model, and that cross is its own imposed classification. Most citations are `(unverified)`, and the file carries a verification queue. The 52% versus 42% acquiescence figure is the weakest-sourced number in the family.

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
SKILL.md                          the process
README.md                         this file
references/bias-types.md          the library
```

`references/bias-types.md` holds bias entries, response scales, screener design and length evidence. It lives in its own file so it can be amended without touching
the process. It is a first pass and expected to change. When the skill meets something the library
lacks, it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd survey-questions && zip -qr ../survey-questions.skill SKILL.md README.md references/
```
