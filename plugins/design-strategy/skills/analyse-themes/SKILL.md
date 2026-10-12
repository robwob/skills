---
name: analyse-themes
description: >
  Use this skill to analyse the design strategy themes used on any page or interface, how it
  approaches solving a user problem. Triggers include: 'analyse themes', 'what themes does this
  page use', 'how does this solve the problem', 'what's the design strategy here', 'compare these
  pages', 'theme analysis', or any request to understand the strategic approach behind a design.
  Accepts screenshots, live URLs, or Figma/Paper links. Produces a self-contained HTML report with
  a Venn diagram and per-page theme breakdown.
---

# Analyse Themes Skill

## Purpose

Analyse one or more pages or interfaces to identify the design strategy themes they use, how they
approach solving a user problem. The goal is not to describe what a page is for, but to name the
strategic moves it makes: what it leads with, what it supports, and what it ignores.

Output is a self-contained `theme-analysis.html` file containing a Venn diagram of all themes
across all pages analysed, plus a per-page summary.

---

## Theme vocabulary

The 12 themes live in `references/themes.md`. Read that file before analysing. Do not work from
memory: the vocabulary changes over time and the file is the only current version.

Use it as a guide, not a constraint. Detect themes from what you actually observe, and if a
prominent signal fits nothing in the list, follow **Proposing new themes** below.

## Input

Accept any combination of:
- **Screenshots or images**: analyse directly from the image
- **Live URLs**: fetch the page and analyse what's visible and prominent
- **Figma or Paper links**: use MCP if available; if not, ask the user to share a screenshot instead

If multiple pages are provided, analyse each one individually before comparing.

If no input is provided, ask:
> "Share the page you'd like to analyse, a screenshot, a URL, or a Figma/Paper link."

---

## Analysis process

### Step 1, Observe

For each page, note what is present and prominent:
- What does the user see first?
- What takes up the most space or visual weight?
- What copy, patterns, and interactions are present?
- What is absent that you might expect?

Do not interpret yet, just observe.

### Step 2, Map to themes

For each observation, identify which theme it belongs to. A single element can serve multiple
themes (e.g. a free trial is both Ease and Trust). Note the primary theme for each signal.

If a signal is present and prominent but does not fit any existing theme, and is not clearly a
subtype of one, flag it as a candidate for a new theme. Do not force it into an existing category.
Handle it using the process in **Proposing new themes** below.

### Step 3, Identify dominant theme

Identify the one theme that the page leads with, the strategy it has committed to most strongly.
This is the theme that the visual hierarchy, copy, and interactions centre on. There is always one
dominant theme, even if others are present.

### Step 4, Identify supporting themes

List the other themes present and what specific signals support each one. Be specific, name the
element, not just the category.

### Step 5, Note absences

Identify which themes from the vocabulary are entirely absent. Absences are as strategic as
presences, a page that ignores Delight or Control has made a choice.

---

## Proposing new themes

When Step 2 identifies a signal that doesn't fit the existing vocabulary, pause before producing
the main output and surface the candidate theme to the user.

**When to propose:**
- The signal is present and visually or rhetorically prominent, not a minor detail
- It represents a distinct strategic move, not a variation of an existing theme
- Forcing it into an existing category would misrepresent what the page is doing

**Do not propose** if the signal is a subtype or execution of an existing theme. For example:
a countdown timer is Momentum, not a new theme; a star rating is Validation, not a new theme.

**How to present a proposal:**

> **New theme detected: [Name]**
>
> **What it is:** One sentence defining the strategy.
>
> **Why it's not [closest existing theme]:** One sentence explaining the distinction.
>
> **Evidence on this page:** The specific element(s) that prompted the proposal.
>
> Would you like to add this to the vocabulary?

Wait for the user's response before proceeding with the analysis. If they agree, follow the
**Adding an approved theme** process below, then continue. If they decline, either absorb the
signal into the nearest existing theme or note it as an observation without a theme label.

---

## Adding an approved theme

Only after the user has explicitly approved it. Never write on your own judgement.

1. Add a row to the table in `references/themes.md`:
   `| **[Name]** | [Definition. Includes: specific examples.] |`

2. Tell the user the theme touches two files, and ask whether to do the second now:
   a new theme has no levers, so `define-levers` cannot act on it until levers exist in
   `define-levers/references/levers.md`.

3. Confirm: "Added **[Name]** to the theme vocabulary. It has no levers yet."
   Then continue the analysis.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on
claude.ai is read-only), say so plainly rather than reporting a save that did not happen.
Output the exact row for the user to paste into `references/themes.md`, and tell them the skill
needs repackaging afterwards:

```
cd <the analyse-themes directory>
zip -qr ../analyse-themes.skill SKILL.md references/
```

---

## Output: theme-analysis.html

Produce a single self-contained HTML file. All CSS and JS must be inline. No external dependencies.

### Structure

**Header**
- Title: "Theme Analysis"
- Subtitle: page name(s) or URL(s) analysed
- Date

**Venn diagram (inline SVG)**
- All themes detected across all pages are shown as overlapping circles
- The dominant theme across all pages is visually larger and bolder
- Where a theme appears on multiple pages, the circles overlap
- Themes that appear on only one page sit more peripherally
- Each circle is labelled with the theme name and a short descriptor
- Use a muted, professional colour palette, one colour per theme, consistent across the diagram and summaries below
- The diagram must be legible at 1200px wide

**Per-page summaries**
For each page analysed, show:
- Page name or URL
- Dominant theme (bold, with the theme colour)
- Supporting themes (listed, with brief evidence for each, name the specific element)
- Absent themes (listed, with a one-line note on what that absence signals)

**Download controls**
- Button: "Download report as PNG", triggers a client-side PNG export of the full page
- Button: "Download diagram as SVG", triggers download of the Venn diagram SVG alone

### HTML requirements
- Use `<canvas>` + JS or pure SVG for the Venn diagram, no charting libraries
- PNG export via `html2canvas` CDN is acceptable only if loaded from a reliable CDN with a fallback message if unavailable
- SVG download must work via a Blob URL, not a data URI
- Font: system-ui or Inter (Google Fonts CDN acceptable)
- Background: white
- Max content width: 1200px, centred

---

## Tone and framing

Write analysis as strategic observation, not evaluation. The goal is to understand the approach, not
to judge whether it is good or bad. Use language like:

- "This page leads with Trust…"
- "Ease is the dominant strategy here, the page removes every decision that isn't essential."
- "Clarity is absent, the page assumes familiarity rather than building it."

Do not describe what the product does. Describe how the page is trying to solve the user's problem.

---

## Multi-page comparison

When multiple pages are provided, add a comparison section after the individual summaries:

- Which themes are shared across all pages?
- Which themes are unique to one page?
- What does the dominant theme reveal about each page's strategic bet?
- Are there any themes that no page in the set uses, and is that a gap or a deliberate choice?

Keep the comparison to 150–200 words. Make it analytical, not a list of facts.
