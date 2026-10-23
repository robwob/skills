# ux-review

Evaluates a design against UX best practices and reports what is broken, how badly, and what to do
instead. Interaction and structure only: flows, states, forms, navigation, information architecture,
error prevention and recovery, interaction accessibility, deceptive design.

Pairs with `ui-review` (visual craft) and `content-review` (copy). Run all three at once with
`design-review`.

## Install

**Claude Code / local.** Symlink this directory into your skills folder:

```
ln -s /path/to/ux-review ~/.claude/skills/ux-review
```

Skills are picked up when a session starts, so start a new session afterwards.

**claude.ai.** Upload `ux-review.skill`. Uploaded copies are read-only, so the skill cannot save an
approved library addition. It will say so and hand you the text to paste in.

## Use

> "Review the UX of this page" plus a screenshot, URL, local file, or Figma/Paper link.

Give it the task the user is trying to complete. A usability finding is only meaningful against a
task, and the skill will ask if you do not.

Output is a self-contained `ux-review.html`: findings ordered by severity, each naming the element,
what is true now, the fix, and the standard it violates, plus an explicit list of what the input
format prevented checking.

## What is in here

```
SKILL.md                      the process
references/ux-standards.md    the bar: Nielsen's heuristics, WCAG interaction criteria,
                              Baymard form findings, response-time thresholds, IA, mobile,
                              deceptive design
```

Every entry in the library carries a tier. **Standard** is a citable published requirement and a
violation is a defect. **Evidence** is a quantified finding from a primary source. **Convention** is
widely adopted practice where sources disagree. Folklore is excluded, and the library keeps an
`Excluded, and why` section so rejected rules do not creep back in.

**House rules.** An optional plain markdown file that adapts the skill to you without editing it. A
project `.house-rules.md` takes precedence over your personal `~/.config/house-rules/house-rules.md`. This skill reads
the `## Interaction` and `## Reuse` sections, and applies Interaction to your own work only. The
`house-rules-setup` skill creates the file by interview.

The library is a first pass and is expected to change. When the skill sees a problem no entry covers,
it proposes an addition and waits: nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd ux-review && zip -qr ../ux-review.skill SKILL.md references/
```
