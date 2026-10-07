# desk-research

Conducts desk research and competitor analysis and synthesises it by theme. Selects two to four competitors, searches against inclusion rules written first, weighs each source by what that type can and cannot show, and returns hypotheses to test, not findings about users.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions-v2` and `desk-research`. Each works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/desk-research ~/.claude/skills/desk-research
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/desk-research/SKILL.md ] && echo OK || echo BROKEN
```

**claude.ai.** Upload `desk-research.skill`. Uploaded copies are read-only, so the skill cannot save an
approved addition to its library. It will say so and hand you the text to paste in.

## Use

> "What are our competitors doing in onboarding?"

Share the space, the focus and any competitors you want included. It confirms the rules for what to include before it searches.

## How solid the library is

**The weakest library in the family, and honest about it.** Asked directly, the research found no evidence hierarchy for secondary research, so the file is a small set of cited method cards and a table of what each source type can and cannot show. It carries a standing instruction never to add a tier list or numeric weighting. Competitor selection, from NN/g, is the best-sourced part.

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
SKILL.md                      the process
README.md                     this file
references/sources.md         the library
```

`references/sources.md` holds competitor selection, what each source type can show, synthesis and search documentation. It lives in its own file so it can be amended without touching
the process. It is a first pass and expected to change. When the skill meets something the library
lacks, it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd desk-research && zip -qr ../desk-research.skill SKILL.md README.md references/
```
