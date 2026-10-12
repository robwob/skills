# analyse-themes

Identifies the design strategy themes a page or interface uses. Not what the product does, but
the strategic moves the page makes: what it leads with, what it supports, what it ignores.

Pairs with `define-levers`, which turns the themes into actionable direction. Either can be used
on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/analyse-themes ~/.claude/skills/analyse-themes
```

Skills are picked up when a session starts, so start a new session afterwards.

**claude.ai.** Upload `analyse-themes.skill`. Note that uploaded copies are read-only, so the
skill cannot save an approved new theme. It will tell you and hand you the text to paste in.

## Use

> "Analyse the themes on this page" plus a screenshot, URL, or Figma/Paper link.

Multiple pages can be compared in one pass.

Output is a self-contained `theme-analysis.html`: a Venn diagram of themes across all pages, a
per-page breakdown of dominant, supporting and absent themes, and a comparison section.

## What is in here

```
SKILL.md              the process
references/themes.md  the 12 themes and what each one means
```

The vocabulary lives in `references/themes.md` so it can be amended without touching the
process. It is a first pass and is expected to change. When the skill sees a prominent signal
that fits nothing in the list, it proposes a new theme and waits: nothing is written without
your approval.

After editing anything here, rebuild the zip:

```
cd analyse-themes && zip -qr ../analyse-themes.skill SKILL.md references/
```
