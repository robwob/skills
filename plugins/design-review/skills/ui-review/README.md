# ui-review

Evaluates a design against visual and UI best practices and reports what is broken, how badly, and
what to do instead. Visual craft only: contrast, typography, spacing, hierarchy, grouping, colour,
target size, component states, focus appearance.

Pairs with `ux-review` (interaction) and `content-review` (copy). Run all three at once with
`design-review`.

**Not the same as building one.** Applying visual style to an approved wireframe is a build stage;
a house design system is a separate document. This skill judges an existing design against a
general bar, and on your own work against your own system as well.

## Install

**Claude Code / local.** Symlink this directory into your skills folder:

```
ln -s /path/to/ui-review ~/.claude/skills/ui-review
```

Skills are picked up when a session starts, so start a new session afterwards.

**claude.ai.** Upload `ui-review.skill`. Uploaded copies are read-only, so the skill cannot save an
approved library addition. It will say so and hand you the text to paste in.

## Use

> "Review the UI of this page" plus a screenshot, URL, local file, or Figma/Paper link.

Output is a self-contained `ui-review.html`: a table of measured values, then findings ordered by
severity, then an explicit list of what could not be measured.

## Measure, do not estimate

Most of the bar is numeric, and numbers cannot be read off a render. On anything served, run
`references/measure.js`: paste it into the devtools console or inject it with the browser tool, then
call `__uiMeasure()` or `__uiMeasure('main')`. It computes text contrast (1.4.3), control contrast
(1.4.11), target size (2.5.8), body size, line height and measure, and it lists what it could not
reach rather than guessing. It reads the page and changes nothing.

Focus, hover and active appearance are not measurable this way, since they need the element in that
state. Tab to it and look.

## What is in here

```
SKILL.md                      the process
references/ui-standards.md    the bar: WCAG contrast, typography, spacing, hierarchy,
                              Gestalt grouping, target size, states, colour, elevation
references/measure.js         computes the numeric checks against a rendered page
```

Every entry carries a tier. **Standard** is a citable requirement and a violation is a defect.
**Evidence** is a quantified primary-source finding. **Convention** is adopted practice where systems
disagree. **House** is the owner's own evidenced preferences, read from a file they nominate at
review time rather than copied here, and applied only to their own work.

Folklore is excluded and stays excluded: the golden ratio, 60-30-10, a WCAG-backed minimum font size
and APCA thresholds are all listed in `Excluded, and why` with the reason.

After editing anything here, rebuild the zip:

```
cd ui-review && zip -qr ../ui-review.skill SKILL.md references/
```
