---
name: ux-review
description: >
  Use this skill to evaluate a design against UX best practices and recommend changes. Covers
  interaction and structure only: flows, states, forms, navigation, information architecture, error
  prevention and recovery, interaction accessibility, and deceptive design. Triggers include:
  "review the UX", "is this usable", "what's wrong with this flow", "UX audit", "heuristic
  evaluation", "check this against usability best practice", or any request to assess whether a
  design works rather than how it looks or reads. Accepts screenshots, live URLs, local HTML, or
  Figma/Paper links. Produces a self-contained HTML report of findings by severity. For visual craft
  use `ui-review`, for copy use `content-review`, for all three at once use `design-review`.
---

# UX Review Skill

## Purpose

Measure a design against the usability bar in `references/ux-standards.md` and report what is broken,
how badly, and what to do instead.

This skill evaluates. It does not redesign, and it does not build. Findings name a fix; applying the
fix is a separate job.

---

## Scope

**This skill owns interaction and structure.** Two sibling skills own the rest, and findings must be
filed with their owner so a combined review does not report the same defect three times.

| Concern | Owner |
|---|---|
| Flow, task completion, navigation, information architecture | `ux-review` |
| Required states: empty, loading, error, success, overflow | `ux-review` |
| Form structure, field count, validation timing, required marking | `ux-review` |
| Keyboard, focus order, semantic structure, ARIA, target *behaviour* | `ux-review` |
| Contrast, typography, spacing, hierarchy, target *size*, focus *appearance* | `ui-review` |
| Wording of any kind: labels, errors, headings, alt text, tone | `content-review` |
| Which strategic dimension to dial, and the psychology behind it | `define-levers` |

The edge cases, decided in advance so they are not re-argued each run:

- A form field with a wrongly worded label is one finding, owned by `content-review`. Its position,
  validation timing and necessity are `ux-review`.
- A focus indicator that is invisible is `ui-review` (appearance). A focus order that jumps around is
  `ux-review` (behaviour).
- A touch target 18px tall is `ui-review` (size against 2.5.8). A touch target sitting under the
  keyboard on mobile is `ux-review` (reachability).
- A design that works but bets on the wrong strategy is **not a finding**. That is an angle. Say so
  and hand off to `define-levers`.

---

## Before analysing: what the input allows

Read `references/ux-standards.md` first. Do not work from memory; the library changes and the file is
the only current version.

Then establish what this input format can actually support, because claiming a check you could not
perform is the worst failure this skill has.

| Input | Can assess | Cannot assess without more |
|---|---|---|
| **Static screenshot** | Layout, structure, visible states, field count, action prominence, apparent hierarchy | Focus order, keyboard operation, validation timing, response time, semantics, any state not pictured |
| **Served, but not driven** | Everything the initial render exposes: DOM semantics, heading outline, table associations, tab order, reflow, the whole happy path | **Every state reached by interacting.** Validation, errors, empty states, confirmations, disabled states, anything behind a click |
| **Served and driven** | All of the above plus the states behind interaction | Little, though flows behind auth or a payment need permission |
| **Figma or Paper artboards** | Structure, and every state that has been drawn | Real behaviour, timing, semantics. Absence of a state artboard is itself a finding |
| **A described flow, no artefact** | Structural and sequencing issues only | Anything requiring the artefact. Say so plainly |

**Served but not driven is the mode most likely to mislead**, because it looks like full access. On an
interactive tool, most of what this skill exists to catch, error handling, empty states, recovery
paths, lives behind an interaction. A static pass over a calculator or a form will produce a
confident-looking report about the happy path and silently omit the risky half. When working in this
mode, say up front which half is out of reach, and make the **Not assessed** section carry it rather
than burying it at the end.

If given a live page, read the DOM and computed values rather than eyeballing a render: heading
outline, tab order, form markup. **Do not click through flows, submit forms, or exercise
interactions unless asked.** Extracting structure is not the same as driving the UI, and only the
first is in scope by default.

If nothing is provided, ask:
> "Share the design you'd like reviewed: a screenshot, a URL, a local file, or a Figma/Paper link.
> Tell me the task the user is trying to complete, and I'll review against that."

---

## The task frame

**A usability finding is only meaningful against a task.** Before analysing, state the task the
design serves, in one sentence, and confirm it if it was not given:

> "I'm reviewing this as: a user trying to [task]. Correct me if that's the wrong frame."

Without a task, a review degenerates into a list of things that could be different. With one, every
finding can be tested against whether it obstructs that task.

---

## Process

### Step 1, Observe before judging

Inventory what is present: the actions available, their prominence, the fields, the states shown, the
navigation, the path from entry to task completion. Note what is conspicuously absent. Do not write
findings yet. This step exists because findings written during first-pass observation tend to be
about the reviewer's expectations rather than the design.

### Step 2, Walk the task

Trace the path a user takes from arrival to task completion. At each step ask: what does the user
need to know here, what can they do, what happens if they get it wrong, and how do they know it
worked. Breaks in that chain are the highest-value findings this skill produces.

### Step 3, Test against the library

Work through `references/ux-standards.md` and check what applies. Selection, not completion: a design
sits on a handful of these, not all of them. Reporting against every section is a sign of describing
the library rather than reading the design.

Check the required-states list explicitly (section 9), because missing states are the most common
structural gap and the easiest to miss when reviewing a happy-path mock.

### Step 4, Assign severity

| Severity | Bar |
|---|---|
| **Blocker** | Fails a **Standard**-tier entry, or prevents task completion outright. Accessibility failures land here by default. |
| **Major** | Contradicts an **Evidence**-tier finding, or measurably obstructs the task without stopping it. |
| **Minor** | A **Convention** deviation, or friction that is real but survivable. |

Severity comes from the tier plus the task impact, not from how strongly the reviewer feels.

### Step 5, Write the findings

Every finding carries: the specific element, what is true of it now, what it should be instead, the
entry it violates with its tier, and the heuristic it maps to.

**A finding you could have written without looking at this design is not a finding.** If it does not
point at a specific element, delete it. "Consider improving the error handling" is not a finding.
"The postcode field validates on every keystroke, so an error appears after the first character and
stays until the field is complete" is.

### Step 6, State what you could not check

List what this input format prevented assessing, from the table above. This is required, not
optional. A review that silently omits what it could not see reads as a clean bill of health it has
not earned.

### Step 7, Propose additions, then stop

Surface any candidate library additions and wait. See below.

---

## Proposing an addition

The library is a first pass at every layer and is expected to change. **Nothing is written without
the maintainer's explicit approval.** Propose, then stop.

**Propose a new entry when** a real usability problem is observed that no existing entry covers, and
forcing it into the nearest one would misrepresent it.

**Do not propose** an entry that is a restatement of an existing one at a different altitude, or a
rule you cannot source. The tier decides the bar: a **Standard** needs a citable published
requirement, **Evidence** needs a primary study with a sample behind it, **Convention** needs
adoption across established design systems. Anything you cannot source at one of those three levels
is folklore and belongs in **Excluded, and why** instead, with a note on why it was rejected.

**Format:**

> **New entry proposed: [Name]**
>
> **Section and tier:** where it would sit, and which of the three tiers, with the source that
> qualifies it.
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing]:** one sentence on the distinction.
>
> **Evidence in this design:** the specific element that prompted it.
>
> Add this to the library?

**Wait for the answer.** If declined, fold the observation into the nearest entry or report it
without a label, and continue.

### Adding an approved entry

Only after explicit approval. Edit `references/ux-standards.md` in place, matching the surrounding
format exactly, and confirm what changed and where.

If the skill is running somewhere the file cannot be written, an uploaded copy on claude.ai is
read-only, say so plainly rather than reporting a save that did not happen. Output the markdown to
paste in, and note that the skill needs repackaging:

```
cd <the ux-review directory>
zip -qr ../ux-review.skill SKILL.md references/
```

---

## Output: ux-review.html

A single self-contained HTML file. All CSS and JS inline. No external dependencies beyond an optional
CDN for PNG export.

**Structure**

- **Header**: "UX Review", the design reviewed, the task frame it was reviewed against, the date.
- **Verdict line**: counts by severity, then one sentence on whether the design is fit to ship for
  the stated task.
- **Findings**, ordered Blocker then Major then Minor, never grouped by heuristic. Each finding is a
  card carrying: the element, what is true now, what it should be, the severity, the tier and source,
  and the Nielsen heuristic it maps to as a small label.
- **Not assessed**: what the input format prevented checking.
- **Angles, if any**: things that work but could be a better strategic bet, named and handed to
  `define-levers` rather than dressed up as defects.
- **Download as PNG**, client-side, with a fallback message if the CDN is unavailable.

**HTML requirements**: severity must be separable at a glance without relying on colour alone. System
font stack or Inter. White background. Max width 1200px, centred. Sharp corners, flat fills, no
decorative shadows.

Alongside the file, give a short summary in chat: the counts, the three findings that matter most,
and the local path. Hand back the path rather than a served link: it opens directly in any editor.

---

## Tone

Write findings as observations with a fix attached, not as criticism and not as instruction.

- "The form asks for 14 fields where the task needs 6. Address lookup would remove 5 of them."
- "There is no empty state drawn for the results list, so it is not clear what a first-run user sees."
- "The Delete control sits 8px from Save, which is where mis-clicks come from. Separating them, or
  demoting Delete to a secondary weight, removes the risk."

Never soften a Standard-tier failure into a suggestion. An accessibility failure is a defect, and
saying "consider adding" understates it.

No em dashes in the report. Use commas and full stops.
