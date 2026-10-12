# UI standards library

The bar `ui-review` measures a design against. Visual craft only: interaction and structure belong to
`ux-review`, wording belongs to `content-review`.

**This is a first pass and is expected to change.** Adding or amending an entry follows the approval
process in `SKILL.md`. Nothing is written here without the maintainer's explicit approval.

---

## How this is structured

Every entry carries a tier. The tier decides the severity of a finding.

| Tier | What it is | A violation is |
|---|---|---|
| **Standard** | A published, citable requirement, in practice a WCAG success criterion. Objectively measurable. | A defect. Not negotiable by taste. |
| **Evidence** | A quantified finding from a primary research source. | A strong finding. Overriding it needs a stated reason. |
| **Convention** | Widely adopted practice where established systems disagree with each other. | A deviation. Fine if deliberate and consistent, a finding if accidental. |
| **House** | The owner's own evidenced preferences, from `~/.claude/house.md`. Applies only to their work. | A defect in their work, irrelevant in anyone else's. |

Folklore is excluded. Several things every designer "knows" are in **Excluded, and why** at the end,
because they have no source and should not be re-added.

**Measure, do not estimate.** Most of the Standard tier is numeric. Contrast, type size, line height
and target size cannot be assessed by looking at a render, and a guessed ratio in a report is worse
than no ratio. Use `measure.js` on anything served, and say so when a value could only be estimated.

**A page with two palettes has two sets of numbers.** A run of `measure.js` only ever sees the scheme
the browser is currently in, so a clean result proves nothing about the other one. Where a design
defines a `prefers-color-scheme` block, **measure both**, either by flipping the scheme or by
computing the token pairs directly, and report per palette. A real failure found this way on the
first run of this skill: a page whose text passed everywhere in dark had an accent fill at 2.82:1 in
light, visible only once both were computed. `measure.js` now detects a second palette and warns when
it has not been measured, but the warning is a prompt, not a substitute for doing it.

---

## The House tier

For the owner's own work, read `~/.claude/house.md`: a document of their evidenced visual
preferences, built up from repeated observations rather than written in one sitting. It may point
elsewhere for the detail, in which case follow it.

**Do not copy those rules into this file.** The house file is the single copy and it changes as
observations accumulate. Read it at review time.

A house file tends to converge on a few entries that produce most findings. One worth naming, because
it recurs across every house file I have seen, is relational spacing: a gap is set from a measured
relationship to a neighbouring gap, never from a value that merely looks close. Treat the house file
as the authority for the rest.

- Spacing and size are stated as **relationships** between elements, not numbers. A value that merely
  looks close is a defect, because the relationship was the requirement.
- **Siblings must match.** A new colour, weight, size or position is a defect unless it was asked for.
- **Colour is a closed system.** An introduced colour reads as a bug, and weight travels with colour.
- **Competing weights are a defect**, especially a secondary heading fighting a primary one.

Where a House rule and a Convention entry disagree on your own work, House wins. Where House
disagrees with a Standard, the Standard wins: taste does not override an accessibility requirement.

---

## 1. Contrast

- **Contrast (Minimum), 1.4.3, Level AA. [Standard]** Normal text at least **4.5:1**. Large text at
  least **3:1**, where large means 18pt/24px regular or 14pt/18.67px bold and above.
  <https://www.w3.org/WAI/WCAG20/Understanding/contrast-minimum.html>
- **Contrast (Enhanced), 1.4.6, Level AAA. [Standard]** Normal text 7:1, large text 4.5:1. Report as
  an enhancement, not a failure, unless AAA was the stated target.
- **Non-text Contrast, 1.4.11, Level AA. [Standard]** UI component boundaries that identify a control,
  input borders, toggle states, and icons that carry meaning, at least **3:1** against what sits
  adjacent. Applies in every interactive state except disabled.
  <https://dequeuniversity.com/resources/wcag2.1/1.4.11-non-text-contrast>
- **The text-label exception to 1.4.11. [Standard, and routinely misapplied]** The criterion covers
  the visual information *required to identify* a control. Where a control carries its own visible
  text label, W3C treats it as identified by that text, and the **text** contrast requirement applies
  instead of the boundary one. A filled button reading "Add another option" whose fill measures 2.8:1
  is therefore contested, not a clean failure, if its label clears 4.5:1.

  **Report these as contested and say so.** A boundary under 3:1 on a labelled control is worth
  fixing, and worth raising, but calling it a certain Blocker overstates what the criterion says and
  invites a correction that discredits the rest of the review. An **unlabelled** control, an icon
  button, a bare input, has nothing but its boundary, so there the 3:1 is unambiguous.
- **A border on one edge is still a boundary.** An underline under a text field identifies it as
  a field. Check all four edges and take the strongest, rather than assuming a box. Where the
  boundary is drawn by a wrapper rather than the control itself, a segmented stepper being the usual
  case, that has to be confirmed by eye: it is not a failure, and it is not automatically a pass.
- **Placeholder text is text.** It is held to 4.5:1 like any other text, which is the most common
  quiet failure in a form design.
- **Text over an image** must be measured against the lightest and darkest region it actually crosses,
  not against an average. A scrim or gradient is the usual fix.

**APCA and WCAG 3 are not a bar yet. [Excluded as premature]** APCA is one candidate algorithm inside
a Working Draft. W3C has not adopted it, no regulation references it, and specific Lc thresholds
circulating online are not settled. Do not fail a design against APCA, and do not cite an Lc number
as a requirement. <https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html>

---

## 2. Typography

- **Line length 50 to 75 characters. [Evidence]** Converged across Baymard, NN/g and Bringhurst, with
  about 66 the most cited single target. Long measures cost the reader the line return.
  <https://baymard.com/blog/line-length-readability>
- **Text Spacing, 1.4.12, Level AA. [Standard]** The design must not break when the user sets line
  height to 1.5x font size, paragraph spacing to 2x, letter spacing to 0.12em and word spacing to
  0.16em. This is a resilience requirement, not a styling one: fixed-height containers holding text
  are what fail it. <https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html>
- **Visual Presentation, 1.4.8, Level AAA. [Standard]** Line height at least 1.5 within paragraphs, no
  full justification, and no more than 80 characters per line, 40 for CJK.
- **Body size floor. [Convention]** No WCAG minimum exists. 16px is the de facto floor on the web, and
  is also the point below which iOS Safari auto-zooms a focused input. Apple HIG sets 11pt as its
  minimum with 17pt recommended for body; Material 3 sets 14sp minimum, 16sp preferred. Report text
  below 16px on a touch surface as a Convention finding, not a Standard failure.
- **Letter-spacing tracks inversely with size. [Convention]** Tighten large display type, roughly -1%
  to -3%; leave body near 0 to 2%; add 5 to 12% to anything set in capitals.
- **Type scale ratios. [Convention]** 1.25 and 1.333 are the common modular ratios. There is no
  perceptual research behind them, so a design using a different scale consistently is not wrong. A
  design using no scale at all, with sizes that do not relate, is.

---

## 3. Spacing and layout

- **Spacing scale. [Convention]** 4pt and 8pt grids come from Material and are justified by
  divisibility and clean scaling across 1x, 1.5x, 2x and 3x densities. That is engineering
  convenience, not perception research. The finding is never "this is not on an 8pt grid", it is
  "these values do not belong to any consistent scale."
- **Proximity does the grouping.** Space between groups must exceed space within a group. When it does
  not, the eye groups the wrong things, and no amount of styling repairs it. This is the single most
  common spacing defect and it is checkable: measure the gaps and compare.
- **Optical over mathematical alignment. [Convention]** Equal bounding boxes do not read as equal
  weight: a filled square looks heavier than a circle at the same pixel size. Icon sets and
  established systems compensate rather than centring mathematically.
- **Reflow, 1.4.10, Level AA. [Standard]** Content reflows to a single column with no two-dimensional
  scrolling at a viewport width of 320 CSS px, equivalent to 400% zoom at 1280px.
  <https://www.w3.org/WAI/WCAG21/Understanding/reflow.html>
- **Breakpoints. [Convention]** No body owns them. Material uses 480/600/840/960/1280/1440/1600dp,
  Bootstrap 5 uses 576/768/992/1200/1400px, and the cross-industry convergence is roughly 320, 768,
  1024, 1440. Consistency within a product matters; matching any particular system does not.

---

## 4. Visual hierarchy

**[Convention, but checkable]** Hierarchy is built from size, weight, colour, position, density and
whitespace. The failure is not ugliness, it is that the eye has nowhere to land first.

Testable markers of a flat or competing hierarchy:

- More than one element carrying dominant visual weight in the same view, unless spatially separated.
- Three or more headings at the same size and weight, doing different jobs.
- More than one true accent colour competing for the same attention.
- Primary and secondary actions at the same visual weight, which makes the primary action a choice
  rather than a recommendation.
- Everything emphasised, which is the same as nothing emphasised.

For your own work this sits alongside the House rule that competing weights are a defect.

---

## 5. Gestalt grouping

**[Evidence]** The principles that govern how the eye groups elements. Useful because they explain
*why* a layout misreads, which turns a vague "feels cluttered" into a specific fix.

- **Proximity**: near equals related. Strong enough to override colour and shape similarity.
  <https://www.nngroup.com/articles/gestalt-proximity/>
- **Common region**: a shared boundary, a card or panel, overrides both proximity and similarity. A
  border drawn in the wrong place regroups the content regardless of spacing.
  <https://www.nngroup.com/articles/common-region/>
- **Similarity**: same colour, shape or size reads as same category. Styling two unrelated things
  alike asserts a relationship that does not exist.
- **Uniform connectedness**: a connecting line or rule ties elements together even at a distance, and
  overrules minor visual differences.
- **Closure**: the eye completes incomplete shapes, which is what makes outline iconography legible.

---

## 6. Target size

- **Target Size (Minimum), 2.5.8, Level AA. [Standard]** *New in WCAG 2.2.* At least **24x24 CSS px**,
  or sufficient spacing. Exceptions: inline links in a sentence, targets controlled by the user
  agent, an equivalent larger control elsewhere on the page, and cases where the presentation is
  essential.
- **The spacing exception, stated precisely. [Standard]** An undersized target passes if a **24px
  diameter circle centred on its bounding box** does not intersect another target, nor the circle of
  another undersized target. It is not "24px of gap", and the difference matters: two 20px-tall nav
  links 20px apart, with centres 73px apart, **pass**, because the circles never meet.

  **Compute this before reporting.** `measure.js` now does it, and the check is why a page of small
  but well-separated nav links is not a page of Blockers. Reporting every undersized target as a
  failure without applying the exception is the fastest way to produce a review nobody trusts.
- **Target Size (Enhanced), 2.5.5, Level AAA. [Standard]** At least 44x44 CSS px.
- **Platform guidance disagrees with the floor. [Convention]** Apple HIG says 44x44pt, Material says
  48x48dp with 8dp between adjacent targets. Report 24px as the accessibility minimum and 44 to 48 as
  the comfortable minimum, and say which bar is being applied. The disagreement is real; picking one
  silently is what to avoid.

---

## 7. States and focus

**Every interactive element needs a visually distinct treatment for: default, hover, focus,
active/pressed, disabled, and where applicable error and loading.** A cursor change is not a state. A
design handed over with only a default state is incomplete, and that is a finding in itself.

- **Focus Visible, 2.4.7, Level AA. [Standard]** Keyboard focus has a visible indicator. Removing the
  browser outline without replacing it is the most common serious failure in a styled component set.
- **Focus Not Obscured (Minimum), 2.4.11, Level AA. [Standard]** *New in WCAG 2.2.* The focused
  element is not entirely hidden behind sticky headers, footers or cookie bars. Partial obscuring
  passes, total obscuring fails.
- **Focus Appearance, 2.4.13, Level AAA. [Standard]** *New in WCAG 2.2.* The indicator is at least as
  large as a 2px-thick perimeter of the component, and has at least 3:1 contrast between focused and
  unfocused states. <https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html>
- **Disabled controls are exempt from 1.4.11**, but a disabled control the user cannot distinguish
  from an enabled one is still a defect. Exempt from the ratio, not from being legible.

---

## 8. Colour beyond contrast

- **Use of Color, 1.4.1, Level A. [Standard]** Colour is never the only means of conveying
  information, indicating an action, prompting a response, or distinguishing an element. Pair it with
  text, an icon, a pattern or a shape. Required-field marking in red alone, a red form border with no
  message, and a chart legend distinguished only by hue all fail this.
  <https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html>
- **Semantic colour. [Convention]** Red for error and destructive, green for success, amber for
  warning. Industry convention rather than a written standard, but inverting it without cause costs
  the user a translation on every glance.
- **Accent restraint. [Convention]** The 60-30-10 split is an interior-design heuristic adopted into
  UI with no accessibility citation behind it. The usable corollary: more than one true accent colour
  on a screen is a smell, because a second accent halves the meaning of the first.

---

## 9. Elevation and iconography

- **Elevation is an ordinal system, not decoration. [Convention]** Material's dp scale runs cards and
  buttons at 2, app bar 4, snackbar 6, menus 8, nav drawer 16, modal dialog 24. Whatever scale is
  chosen, the same elevation must map to the same shadow token throughout. Two different shadows on
  two things at the same level is the finding. Material 3 has moved toward tonal elevation, a colour
  shift, rather than literal shadow.
- **Icons share one grid and one stroke weight. [Convention]** 24x24px is Material's standard grid,
  with 20, 24 and 32 the common sizes. Mixed stroke weights or mixed fill and outline styles inside
  one set is the most visible icon defect, and it is easy to check.

---

## Excluded, and why

Kept so they are not re-added.

- **A WCAG-backed minimum font size.** Does not exist. 16px is convention and should be reported as
  such, never as a failure.
- **60-30-10, and "3 to 5 accent colours maximum".** Studio heuristics with no research or
  accessibility citation. The restraint corollary is kept; the numbers are not.
- **Type scale ratios and 8pt-grid divisibility as rules.** Conventions widely presented as laws. The
  checkable version is internal consistency, not adherence to a specific ratio or grid.
- **APCA Lc thresholds.** WCAG 3 contrast maths is unresolved. Not a bar.
- **The golden ratio in layout.** No perceptual evidence for interface layout.
- **"Above the fold" as a hard rule.** Repeatedly disproven as an absolute; people scroll when there
  is scent to follow. Information scent is a `ux-review` concern.

## Sources

W3C WAI (WCAG 2.1 and 2.2 Understanding documents), Nielsen Norman Group Gestalt series, Baymard
Institute, Apple Human Interface Guidelines, Material Design 2 and 3, Adrian Roselli on WCAG 3
contrast status, and `~/.claude/house.md` for the House tier. Individual URLs sit with
each entry above.
