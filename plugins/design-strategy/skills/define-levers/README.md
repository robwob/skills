# define-levers

Turns design strategy themes into actionable direction. It selects the **levers** in play on a
page, places the page on each one, names the **psychology principles** that explain why moving
that lever works, and proposes the **methods** that would move it.

Follows `analyse-themes`, or runs on its own if you name the themes yourself.

## The model

```
Theme  ->  Lever  ->  Principle  ->  Method  ->  Inventory
```

- **Theme** is the strategy. 12 of them, from `analyse-themes`.
- **Lever** is a dimension you can dial. Always a spectrum with two poles. 49 in the library.
- **Principle** is the psychological mechanism that explains why moving it works.
- **Method** is a named design move that shifts the lever.
- **Inventory** is this page's instance of a method, produced at run time.

Principles explain, methods act.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/define-levers ~/.claude/skills/define-levers
```

Skills are picked up when a session starts, so start a new session afterwards.

**claude.ai.** Upload `define-levers.skill`. Uploaded copies are read-only, so the skill cannot
save an approved addition to the library. It will tell you and hand you the text to paste in.

## Use

> "Define the levers for this page" plus a screenshot, URL, Figma/Paper link, or the output of
> an `analyse-themes` session.

Or name the themes directly: *"focus on Trust and Ease."*

It recommends two to four themes worth acting on and stops for your confirmation before going
further. Output is a self-contained `define-levers.html` with spectrum bars showing where the
page sits on each lever, the principles behind each one, viable methods, and a page-specific
inventory.

## What is in here

```
SKILL.md              the process
references/levers.md  48 levers, their principles and their methods
```

## The library is meant to change

Every layer is a first pass. When the skill finds a dimension in play that no lever covers, or a
method the library does not list, it proposes the addition and **stops**. Nothing is written
without your explicit approval.

`references/levers.md` documents its own sources, the filter used to decide what counts as a
principle, and its known weak points. Read those before extending it.

Sources: Nielsen Norman Group's psychology study guide, Laws of UX, Cialdini's seven principles
of persuasion, and MINDSPACE. Practitioner biases, the ones that act on the researcher rather
than the user, are deliberately excluded.

After editing anything here, rebuild the zip:

```
cd define-levers && zip -qr ../define-levers.skill SKILL.md references/
```
