# design-review

Reviews a design across all three lenses at once. Routes to `ux-review`, `ui-review` and
`content-review`, removes the duplicate findings three lenses inevitably produce, and returns one
prioritised list rather than three reports.

Also decides when a request is not a review at all. A design whose basic strategy is in question needs
`analyse-themes` and `define-levers`, not a heuristic audit, and this skill says so rather than
producing a tidy list of fixes for the wrong page.

## Install

**Claude Code / local.** Symlink this directory into your skills folder:

```
ln -s /path/to/design-review ~/.claude/skills/design-review
```

The three lens skills must be installed too, since this one calls them.

**claude.ai.** Upload `design-review.skill` alongside the other three.

## Use

> "Review this design" plus a screenshot, URL, local file, or Figma/Paper link.

It gathers the four frames once, the artefact, the task, the reader and moment, and whose bar applies,
then runs the lenses in order: UX, then UI, then content. Structural findings often explain visual and
verbal ones, which is why that order.

Output is a self-contained `design-review.html`: one prioritised list with each finding tagged by
lens, the measured values behind the numeric claims, a terminology audit, an unscored Angles section,
and a consolidated list of what was not assessed.

## How the three families fit together

```
  BUILD                  REVIEW                  STRATEGY
  make the thing         check it against a bar  decide what to bet on

  wireframes             ux-review               analyse-themes
    v                    ui-review                 v
  interaction states     content-review          define-levers
    v                         ^
  visual styling         design-review
```

The BUILD column is design stages, not skills. This marketplace publishes the REVIEW and
STRATEGY families.

**Review answers "is this broken?"** There is a right answer, findings carry severity, the output is a
fix list. **Strategy answers "is this the right bet?"** There is no right answer, only positions, and
the output is a direction. A design can pass every review and still be the wrong design.

This skill keeps those apart. Anything that works but might be a weaker bet goes into **Angles**,
unscored, with an offer to hand off to `analyse-themes` and `define-levers`. It offers; it does not
run them.

## Deduplication

One defect, one finding, filed with the owner of the fix: words go to `content-review`, numbers go to
`ui-review`, structure goes to `ux-review`. Where two lenses each have a real and separate fix, both
are kept and cross-referenced. Where they disagree on severity, the highest wins, and the report says
which lens set it.

## What is in here

```
SKILL.md    the routing, deduplication and prioritisation process
```

No reference library of its own. The bars live in the three lens skills, which is the point: this
skill has no opinions to drift out of sync with theirs.

After editing, rebuild the zip:

```
cd design-review && zip -qr ../design-review.skill SKILL.md
```
