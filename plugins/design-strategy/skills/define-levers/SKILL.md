---
name: define-levers
description: >
  Use this skill to select which themes to focus on for improving a specific page or journey
  (called "angles"), then identify the levers within each angle, the dimensions a designer can
  consciously dial up or down, the psychology principles that explain why moving each lever
  works, and the methods that move it. Triggers include: "define the levers", "what angles
  should we focus on", "what can we influence here", "what psychology applies here", "narrow
  down the themes", or any request to move from theme analysis to actionable design direction.
  Can follow an analyse-themes session or be run standalone when themes are named directly.
  Produces a self-contained HTML report with angles, levers, principles, methods and inventories.
---

# Define Levers Skill

## Purpose

Take the themes identified on a page or journey and narrow them to a focused set of **angles**.
For each angle, select the **levers** in play, place the page on each one, name the **psychology
principles** that explain why moving it works, and propose the **methods** that would move it.

The output moves from strategic observation (what themes are present) to actionable direction
(which dimensions to move, in which direction, why that works on people, and what to change).

---

## Terminology

| Term | Definition |
|---|---|
| **Theme** | A design strategy. One of the 12 in the `analyse-themes` vocabulary. |
| **Angle** | A theme selected for focused improvement. Choosing an angle is a strategic bet. |
| **Lever** | A dimension the team can consciously adjust. Always a spectrum with two poles. Selected from the library, not invented. |
| **Principle** | The psychological mechanism explaining why moving a lever works. Taken from the library, never generated. |
| **Method** | A named design move that shifts a lever. Generic and reusable. |
| **Inventory** | This page's concrete instance of a method. Produced here, not stored. |

Principles explain, methods act.

---

## The library

**`references/levers.md` holds 48 levers across the 12 themes, each with its principles and
methods. Read it before doing anything else in this skill.**

Do not work from memory. The library changes over time and the file is the only current version.

Three rules from the library that govern how you use it:

- A principle may sit under several levers, and a lever may serve more than one theme.
  `Decision transparency` is currently shared by Control and Personalisation.
- Both poles of every lever are real positions. Neither end is correct by default. Principles
  marked *(counter)* explain the cost of the active pole, and you must surface them when a page
  is at risk of overshooting.
- The library is a preset list to select from, not a checklist to complete. A page will be
  sitting on a handful of these levers, not all of them.

---

## Input

Accept any of:
- Output or findings from a previous `analyse-themes` session
- A page, screenshot, URL, or Figma/Paper link to analyse directly
- Themes named explicitly by the user ("focus on Trust and Ease")

If themes are named directly, skip Step 1 and go straight to Step 2.

If no input is provided, ask:
> "Share the page or theme analysis you'd like to work from, a screenshot, URL, Figma/Paper
> link, or the output of an analyse-themes session."

---

## Process

### Step 1, Recommend angles

From the themes provided or observed, identify 2–4 with the most room for meaningful
improvement. Consider:

- Which themes are present but weak: strategic enough to matter, underdeveloped enough to move
- Which themes are absent but relevant to this page's goal
- Where the gap between current experience and user need is largest

Present them, one sentence of rationale each:

> "I'd suggest focusing on **[Theme]**: [why it has room to move and why it matters here]."

Then ask:
> "Do these feel like the right angles, or would you like to swap any out?"

**Wait for confirmation before proceeding.**

---

### Step 2, Select the levers in play

For each confirmed angle, read that theme's levers from `references/levers.md` and identify
which are **actually in play on this page**.

**This is selection, not invention.** Do not write new levers here. A theme has four or five in
the library and a page will typically be sitting on two or three of them. Choosing all of a
theme's levers is a sign you are describing the theme rather than reading the page.

A lever is in play if it is observable on this page, either present or conspicuously absent, and
if the team could actually move it. Skip the rest without comment.

If a dimension is clearly in play that no library lever covers, do not force it into the nearest
one and do not quietly invent a lever. Go to **Proposing an addition** below.

---

### Step 3, Place the page on each lever

For each selected lever:

1. **Current position**: where the page sits today, in one sentence, described against the two
   poles as the library states them.
2. **Direction of opportunity**: which way to move and why, given this page's goal and the
   user's context at this moment in the journey.

Evaluate position relative to the page's goal, not in isolation. The passive pole is sometimes
the right answer.

---

### Step 4, Attach the principles

For each selected lever, take its principles from the library. **Never generate a principle that
is not in the file, and never restate a definition.** Say how this specific page engages that
mechanism.

Weak: "Hick's Law: decision time increases with the number of choices."
Strong: "Hick's Law is the cost here. Eleven plans on one screen, with no recommended option,
puts the whole comparison on the user."

Where a page risks overshooting toward the active pole, surface the *(counter)* principle. That
is the main protection against this skill producing a list of things to maximise.

---

### Step 5, Propose the methods

From each lever's methods line, name the ones viable on this page. Methods are generic moves.
Skip any that this page's constraints rule out.

If the page uses a method that works and is not in the library, that is a candidate addition.
See **Proposing an addition**.

---

### Step 6, Build the inventory

For each angle, list the specific things on this page that could be added, removed, reworded or
redesigned. These are this page's instances of the methods above.

Keep it specific to what is actually present or absent here. Do not produce a generic checklist
of everything the theme could include.

---

### Step 7, Propose additions, then stop

Surface any candidate additions found along the way, and wait. Details below.

---

## Proposing an addition

The library is a first pass at every layer. Themes, levers, principles and methods are all
expected to change. But **nothing is written without the user's explicit approval.** Propose, then
stop and wait.

**Propose a new lever when:**
- A dimension is observably in play and the team could move it
- No existing lever in that theme covers it, and forcing it into the nearest one would
  misrepresent what the page is doing
- It is a genuine spectrum with two meaningful poles, not an on/off

**Do not propose a lever** that is a method in disguise. "Add a progress bar" is a method under
`Progress visibility`, not a new lever. If it names a thing to build rather than a dimension to
dial, it is a method.

**Propose a new method when:** the page uses a move that shifts a library lever and the lever's
methods line does not list it. This bar is much lower than for a lever, and it is the layer most
likely to be incomplete.

**Propose a new principle** only from a real, citable source. The library's sources are NN/g's
psychology study guide, Laws of UX, Cialdini's seven and MINDSPACE. It excludes practitioner
biases that act on the researcher rather than the user, and design heuristics with no
psychological mechanism.

**Format:**

> **New [lever / method / principle] proposed: [Name]**
>
> **Theme and lever:** where it would sit.
>
> **What it is:** one sentence. For a lever, state both poles.
>
> **Why it isn't [closest existing]:** one sentence on the distinction.
>
> **Evidence on this page:** the specific element that prompted it.
>
> Add this to the library?

**Wait for the answer.** If declined, absorb the signal into the nearest existing entry or note
it as an observation without a label, and continue.

---

## Adding an approved item

Only after explicit approval.

1. Edit `references/levers.md` in place. Match the surrounding format exactly: a lever is a
   `### Name` heading, a poles line using `->`, a bulleted principle list, then a
   `**Methods:**` line.
2. If it is a new lever, add it to that theme's section, and update the theme's lever count
   wherever the file states one.
3. Confirm what changed and where.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai
is read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown block for the user to paste into `references/levers.md`, and note that the skill needs
repackaging afterwards:

```
cd <the define-levers directory>
zip -qr ../define-levers.skill SKILL.md references/
```

---

## Output: define-levers.html

A single self-contained HTML file. All CSS and JS inline. No external dependencies.

### Structure

**Header**: title "Define Levers", page name or context, date.

**Angles overview**: a row of cards, one per angle, each with the angle name and its
one-sentence rationale.

**Per-angle section**, in its own section with a muted colour accent:

- **Angle name** as the section header
- For each lever:
  - Lever name as a subheading
  - A spectrum bar in pure HTML/CSS: pole A label left, pole B label right, a marker showing
    current position
  - One sentence on the current position
  - One sentence on the direction of opportunity
  - **Why this works**: the principles, each named in bold with its application to this page.
    Counter-principles visually distinguished, since they warn rather than recommend.
  - **Methods**: the viable moves, as a compact list
- **Inventory**: the specific things that could change on this page

**Download controls**: "Download as PNG", client-side via html2canvas from a CDN, with a
fallback message if unavailable.

### HTML requirements

- Spectrum bars: pure HTML/CSS, a track div with a filled bar and pole labels. No JS to render.
- Each angle uses a distinct muted colour, consistent across its card, section header and
  spectrum accent. Professional and low-contrast, no saturated primaries.
- Principles and counter-principles must be visually separable at a glance.
- Font: system-ui or Inter. Background: white. Max content width 1200px, centred.

---

## Tone and framing

Write levers, principles and inventories as design observations: what is true now, and what
could be different. Not instructions, not evaluations.

- "This page sits toward the passive end, risk is unaddressed at the point of decision."
- "There is room to move toward near-peer validation, the current testimonial is unattributed
  and role-agnostic."
- "The flow requires five fields before commitment. This lever could move most of the way toward
  single-gesture action."

Name the principle, then apply it. Do not lecture on the psychology.

No em dashes in anything the user will read, send or publish. Use commas and full stops.
