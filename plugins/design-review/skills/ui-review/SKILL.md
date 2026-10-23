---
name: ui-review
description: >
  Use this skill to evaluate a design against visual and UI best practices and recommend changes.
  Covers visual craft only: contrast, typography, spacing, visual hierarchy, grouping, colour, target
  size, component states and focus appearance. Triggers include: "review the UI", "review the visual
  design", "is this accessible", "check the contrast", "why does this look off", "visual audit",
  "does this match the design system", or any request to assess how a design looks rather than how it
  works or reads. Accepts screenshots, live URLs, local HTML, or Figma/Paper links. Produces a
  self-contained HTML report of findings by severity. For flows and usability use `ux-review`, for
  copy use `content-review`, for all three at once use `design-review`.
---

# UI Review Skill

## Purpose

Measure a design against the visual bar in `references/ui-standards.md` and report what is broken,
how badly, and what to do instead.

This skill evaluates. It does not restyle and it does not build.

**Distinct from building.** Applying visual style to an approved wireframe is a build stage, and a
house design system is a separate document. This skill judges an existing design against
a general bar, and, on your own work, against your own system as well.

---

## Scope

**This skill owns visual craft.** Findings must be filed with their owner so a combined review does
not report the same defect three times.

| Concern | Owner |
|---|---|
| Contrast, colour use, palette discipline | `ui-review` |
| Typography: size, weight, line height, measure, scale | `ui-review` |
| Spacing, alignment, grouping, layout, reflow | `ui-review` |
| Visual hierarchy and emphasis | `ui-review` |
| Target *size*, focus *appearance*, state *styling* | `ui-review` |
| Flow, task completion, IA, validation timing, keyboard *behaviour* | `ux-review` |
| Wording of any kind | `content-review` |

The edge cases, decided in advance:

- A focus indicator that is invisible or too low-contrast is **`ui-review`**. A focus order that jumps
  is `ux-review`.
- A 18px-tall button is **`ui-review`** (2.5.8, size). A button hidden under the mobile keyboard is
  `ux-review` (reachability).
- An error message styled in red only is **`ui-review`** (1.4.1, colour alone). Its wording is
  `content-review`. Whether it appears at the right moment is `ux-review`.
- A missing hover state is **`ui-review`** (state styling). A missing empty state is `ux-review`
  (required states), because that is a structural gap, not a styling one.

---

## Before analysing: measure, do not estimate

Read `references/ui-standards.md` first. Do not work from memory.

Most of the Standard tier is numeric, and numbers cannot be read off a render. **A guessed contrast
ratio in a report is worse than no ratio**, because it will be trusted.

| Input | Method | What stays unmeasurable |
|---|---|---|
| **Live URL or served local HTML** | Run `references/measure.js`. It computes text contrast (1.4.3), control contrast (1.4.11), target size (2.5.8), body size, line height and measure, and lists what it could not reach | Focus, hover and active appearance, which need the element in that state. Tab to it and look |
| **Static screenshot** | Sample pixel values for the contrast pairs that matter and say they were sampled. Assess hierarchy, grouping, alignment and rhythm, which a screenshot supports well | Exact type sizes, computed spacing, any state not pictured, reflow |
| **Figma or Paper artboards** | Read the layer values where the tooling allows. Assess hierarchy, spacing relationships and state coverage across artboards | Rendered behaviour, reflow, real focus styling |

Running `measure.js`: paste it into the devtools console, or inject it with the browser tool, then
call `__uiMeasure()` or `__uiMeasure('main')`. It reads and changes nothing. **Reading a page's
computed values is in scope by default. Clicking through the UI is not, unless asked.**

Anything the method could not reach goes in **Not assessed**. Never let an unmeasured thing pass
silently as if it had been checked.

---

## Whose bar

Establish this before writing findings, because it decides which tiers apply.

- **The owner's own work**: apply the **House rules** tier from the `## Visual` section of the house rules
  (see Personalisation below), alongside Standard, Evidence and Convention. A project file applies to
  artefacts in that project. A user-level file applies to the owner's own work wherever it is.
- **Anyone else's work**: Standard, Evidence and Convention only. House rules are one team's taste and
  are not a defect in someone else's design.
- **No house rules found**: the House rules tier does not apply. Say so once in the report and carry on.

If unclear whose work it is, ask. Applying House rules to a competitor's site produces confident
nonsense.

### Personalisation

This skill reads two sections of the house rules: `## Visual` and `## Reuse`.

**Lookup, per section:** a project `.house-rules.md` (searched upward from the artefact's folder), then
the user file `~/.config/house-rules/house-rules.md`, then the legacy `~/.claude/house.md`. The first file with a
non-empty section wins that section whole. Sections are never merged across files. A section may
point to another file for the detail, in which case follow it.

| Section | Used for | Default when empty |
|---|---|---|
| `## Visual` | The House rules tier | No House rules tier |
| `## Reuse` | Where to look for shared tokens and components when checking system conformance | The nearest `CLAUDE.md` or `AGENTS.md`, then sibling directories. Report where you looked |

End the report with one line saying what was used, for example: "Applied: Visual from project
`.house-rules.md`, Reuse by default." With no file at all: "Applied: no house rules, defaults only.
`house-rules-setup` can create one." Do not question the user about a file they may not know exists.

### Find the design system the file actually declares

**Do not assume which design system applies.** A person or team usually has more than one.
Before reviewing, look for which system this artefact follows, in this order:

1. **A comment in the source naming it.** This is the most reliable signal and it is easy to miss.
   A file may open with something like "styled to match the marketing site, the
   `--bg`/`--ink`/`--muted` token set", which names both the system and the tokens, and tells you
   where to go and read it.
2. **A token block in the file itself**, a `:root` or component-scoped custom property set. The tokens
   are the system for review purposes even if nothing external documents them.
3. **A project `design-system/components.css`**, or the project's own `CLAUDE.md`. The house rules'
   `## Reuse` section names where these live.
4. **A house visual-system skill or document**, if one exists and the artefact belongs to that house.

Then check conformance against **that** system and report it as its own section, marked as system
conformance rather than general best practice. A token used against its own stated purpose is a
finding; a token whose value differs from a different project's system is not.

If the file names a system you cannot locate, say so rather than silently substituting a different
one, and review against the general bar only.

---

## Process

### Step 1, Look before measuring

Note what the eye does first, second, third. Where does it land, what competes, what gets lost. This
has to happen before the numbers, because once you have a contrast table in front of you it is very
hard to see the design again.

### Step 2, Measure, and measure every palette

Run the method for the input type. Collect the numbers.

**If the design defines more than one colour scheme, measure each of them.** A `measure.js` run sees
only the scheme the browser is in, so a clean pass in dark says nothing about light. The script
detects a `prefers-color-scheme` block and warns when a second palette has gone unmeasured, but
acting on that warning is the reviewer's job. Two ways, either is fine:

- Flip the scheme and re-run, by forcing the other palette's token values with an injected stylesheet.
- Compute the token pairs directly from the source values, which is faster when the palette is a
  small token set and gives the same answer.

Report per palette wherever the two differ. "Passes in dark, 2.82:1 in light" is the finding; "passes"
is not.

### Step 3, Test against the library

Work through `references/ui-standards.md` and check what applies. Selection, not completion.
Reporting against every section is a sign of describing the library rather than reading the design.

Check state coverage explicitly (section 7). A component set delivered with only a default state is a
finding, and it is the one most often missed because the missing thing is not on screen.

### Step 4, Assign severity

| Severity | Bar |
|---|---|
| **Blocker** | Fails a **Standard**-tier entry. Contrast, target size, colour-alone, focus visibility and reflow failures land here. |
| **Major** | Contradicts **Evidence**, or breaks hierarchy or grouping badly enough that the design misreads. On your own work, a **House rules** violation is Major. |
| **Minor** | A **Convention** deviation, or a craft inconsistency that does not change how the design reads. |

Severity comes from the tier plus the impact, not from strength of feeling.

### Step 5, Write the findings

Every finding carries: the specific element, the measured value against the required one, what it
should be instead, the severity, and the criterion or entry with its tier.

**A finding you could have written without looking at this design is not a finding.** "Improve the
visual hierarchy" is not a finding. "The section heading and the card titles are both 20px/600, so the
cards read as peers of the section rather than contents of it. Dropping the card titles to 16px/500
restores the level" is.

Where a value was estimated rather than computed, say so in the finding itself.

### Step 6, State what you could not check

Required, not optional. List what the input format and the method left unmeasured.

### Step 7, Propose additions, then stop

Surface any candidate library additions and wait.

---

## Proposing an addition

The library is a first pass and is expected to change. **Nothing is written without the maintainer's explicit
approval.** Propose, then stop.

**Propose a new entry when** a real visual problem is observed that no existing entry covers.

**Do not propose** a rule you cannot source at one of the tiers: **Standard** needs a citable
published requirement, **Evidence** needs a primary study, **Convention** needs adoption across
established design systems. Anything else is folklore and belongs in **Excluded, and why** with a note
on why it was rejected. This library already rejects the golden ratio, 60-30-10 and a minimum font
size, so the bar is real.

**House rules** additions are different: they are promoted from the owner's own house rules, not proposed
here. If a review turns up a repeated preference that the house rules have not recorded, suggest
recording it there rather than adding it to this file.

**Format:**

> **New entry proposed: [Name]**
>
> **Section and tier:** where it sits, which tier, and the source that qualifies it.
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing]:** one sentence.
>
> **Evidence in this design:** the specific element that prompted it.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit `references/ui-standards.md` in place, matching the surrounding
format, and confirm what changed.

If running somewhere the file cannot be written, an uploaded copy on claude.ai is read-only, say so
plainly rather than reporting a save that did not happen, and output the markdown to paste in. Then:

```
cd <the ui-review directory>
zip -qr ../ui-review.skill SKILL.md references/
```

---

## Output: ui-review.html

A single self-contained HTML file. All CSS and JS inline.

**Structure**

- **Header**: "UI Review", the design reviewed, whose bar was applied, the date.
- **Verdict line**: counts by severity, then one sentence on whether the design is fit to ship.
- **Measured values table**: what was computed, contrast pairs with their ratios, sizes, spacing.
  This is the evidence behind the findings and it goes near the top, because it is the part a reader
  will want to check.
- **Findings**, ordered Blocker then Major then Minor. Each carries the element, measured against
  required, the fix, the severity, and the criterion with its tier.
- **System conformance**, only for your own work, kept separate from general best practice.
- **Not assessed**: what the input and method left unmeasured.
- **Applied**: the one-line house rules statement from Personalisation.
- **Download as PNG**, client-side, with a fallback if the CDN is unavailable.

**HTML requirements**: severity separable without relying on colour alone, because a UI review that
fails 1.4.1 in its own report is an embarrassment. System font stack or Inter. White background. Max
width 1200px, centred. Sharp corners, flat fills, no decorative shadows.

Alongside the file, give a short summary in chat: the counts, the three findings that matter most,
and the local path.

---

## Tone

Write findings as measured observations with a fix attached.

- "Body copy is #8A8A8A on #FFFFFF, 3.54:1, against a required 4.5:1. #6E6E6E clears it at 4.61:1."
- "The card gap and the gap between card groups are both 24px, so the two groups read as one set of
  six. Taking the group gap to 48px separates them."
- "Primary and secondary buttons are both solid fills at the same weight, so the primary is not
  reading as the recommended action."

Never soften a Standard-tier failure into a suggestion. A contrast failure is a defect.

No em dashes in the report. Use commas and full stops.
