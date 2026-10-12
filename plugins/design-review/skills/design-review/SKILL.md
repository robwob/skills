---
name: design-review
description: >
  Use this skill to review a design across every lens at once: UX, UI and content. It routes to
  `ux-review`, `ui-review` and `content-review`, removes the duplicate findings the three lenses
  produce, and returns one prioritised report. Triggers include: "review this design", "give me a
  full design review", "audit this page", "what's wrong with this screen", "critique this", or any
  review request that does not name a single lens. Accepts screenshots, live URLs, local HTML, or
  Figma/Paper links. Also decides when a design does not need a review at all but a strategic
  re-think, and hands off to `analyse-themes` and `define-levers` when so.
---

# Design Review Skill

## Purpose

One design, three lenses, one prioritised list. This skill exists because running the three review
skills separately produces three reports that overlap, disagree on severity, and leave the reader to
work out what to fix first.

It routes, deduplicates and prioritises. The substantive bars live in the three skills it calls, not
here.

---

## The map

Three families of design skill. Knowing which family a request belongs to is most of the routing.

```
  BUILD                    REVIEW                    STRATEGY
  make the thing           check it against a bar    decide what to bet on

  wireframes               ux-review                 analyse-themes
    v                        does it work              what strategy is
  interaction states       ui-review                   this page playing
    v                        does it look right             v
  visual styling           content-review            define-levers
                             does it read right        which dimension to
                                   ^                     dial, and the
                                   |                     psychology behind it
                            design-review
                            (this skill: routes,
                             dedupes, prioritises)
```

The BUILD column is design stages, not skills. REVIEW and STRATEGY are skills, and this
marketplace publishes both families.

**The distinction that matters most**, because it is the one that gets blurred:

- **Review answers "is this broken?"** There is a right answer. A contrast failure is a defect
  whoever built it. Findings carry severity, and the output is a fix list.
- **Strategy answers "is this the right bet?"** There is no right answer, only positions. Both poles
  of every lever are real. The output is a direction, not a defect list.

A design can pass every review and still be the wrong design. A design can be strategically sharp and
still fail WCAG. These are different questions and this skill does not let one answer the other.

---

## Before starting

Establish four things. Three of them are the same frames the individual skills need, and gathering
them once here is most of the value of running the coordinator.

1. **The artefact.** A screenshot, URL, local file, or Figma/Paper link.
2. **The task.** What the user is trying to do. `ux-review` cannot produce a meaningful finding
   without it.
3. **The reader and moment.** Who is reading, and at what point. `content-review` needs it.
4. **Whose bar.** The owner's own work, where `ui-review` applies the House tier from their
   `~/.claude/house.md` and any project design system, or someone else's, where it does not.

Then confirm the lenses:

> "I'll review this across all three lenses: UX (does it work), UI (does it look right), content
> (does it read right). Say if you only want one or two."

Default to all three. A single-lens request should go straight to that skill rather than through here.

---

## Deciding whether this is a review at all

Before running anything, check the request is a review. Two common cases are not:

- **"Is this the right approach?"** or "how should this page work?" is a strategy question. Route to
  `analyse-themes`, then `define-levers`. Running a heuristic review on a design whose basic strategy
  is in question produces a tidy list of fixes for the wrong page.
- **"Make this better"** on something not yet built is a build request. Route it to a build stage,
  or ask.

Say which you are doing and why, in one line, before starting.

---

## Process

### Step 1, Establish input capability once

Each skill carries its own input table. Work out here, once, what this artefact supports, and tell the
reader up front:

| Input | Supports | Does not, without more |
|---|---|---|
| **Served, but not driven** | `ui-review` at full depth via `measure.js`, `content-review` on every string in the initial render, `ux-review` on semantics, heading outline, table associations and tab order | **Every state behind an interaction**: validation, errors, empty states, confirmations. On an interactive tool this is most of the UX surface |
| **Served and driven** | All three lenses at full depth | Little, though flows behind auth or a payment need permission |
| **Static screenshot** | Layout, hierarchy, visible copy, apparent structure | Computed values, semantics, alt text, link targets, any state not pictured |
| **Figma or Paper artboards** | Structure, visual relationships, copy, and whichever states were drawn | Rendered behaviour, computed values, alt text. A missing state artboard is itself a `ux-review` finding |

**Say which mode you are in before starting, and name what it costs.** "Served but not driven" reads
as full access and is not: on anything interactive it hands you a complete-looking review of the happy
path while the error and empty states go unexamined. If the review is static by instruction, that is
fine, but the gap belongs in the opening summary, not only in **Not assessed**.

**If the design defines more than one colour scheme, `ui-review` must measure each.** One run of
`measure.js` sees one palette. It warns when a second exists, and acting on the warning is the
reviewer's job.

**Reading a served page is in scope by default. Driving it is not, unless asked.** Extracting computed
styles, strings and structure is reading. Clicking through a flow, submitting a form or triggering an
error is driving.

### Step 2, Run the lenses

Run each in turn, inline, in this order: **UX, then UI, then content.** The order matters, because a
structural finding often explains a visual or verbal one, and knowing the structure is wrong stops you
writing three findings about a component that should not be there.

Follow each skill's own process fully, including reading its reference library. Do not shortcut them
from memory just because they are being run together.

For a multi-screen flow, running the three lenses as parallel subagents is reasonable, one per lens
across all screens. For a single screen it is not worth it, and it costs the cross-lens context that
makes deduplication possible.

### Step 3, Deduplicate

The three lenses will report the same underlying defect more than once. **One defect, one finding,
filed with the owner of the fix.**

The ownership rules, in priority order:

1. **If the fix is words, it is `content-review`.** An error styled red with no message is one finding:
   write the message.
2. **If the fix is a number, it is `ui-review`.** Contrast, size, spacing, weight.
3. **If the fix is structural, it is `ux-review`.** A missing state, a wrong order, an extra field.
4. **If two lenses both have a real and separate fix, keep both, and cross-reference them.** A button
   that is both 18px tall and labelled "OK" genuinely needs two changes.

Where the lenses disagree on severity, **take the highest**, and say which lens set it. A Standard-tier
failure is never demoted because another lens saw it as minor.

### Step 4, Prioritise as one list

Not three sections by lens. One list, ordered:

1. **Blockers**, accessibility Standards first, then anything preventing task completion.
2. **Majors**, ordered by how directly each obstructs the stated task.
3. **Minors**, grouped where they share a fix, because twelve spacing inconsistencies with one cause
   is one piece of work.

Tag each finding with its lens, so the list stays traceable without being organised by lens.

### Step 5, Separate the angles

Anything that works but might be a weaker strategic bet is **not a finding**. Collect these into an
**Angles** section, named but not scored, and offer the hand-off:

> "These aren't defects, they're positions the page has taken. If you want to look at whether they're
> the right bets, `analyse-themes` will name the strategy this page is playing and `define-levers`
> will show which dimensions you could move and the psychology behind moving them. Want me to run
> that?"

**Offer, do not run.** The strategic pass is a different question and the user should choose to ask it.

### Step 6, State what was not assessed

Consolidate the three "Not assessed" lists into one. This is required. A combined review that silently
drops what it could not check reads as far more thorough than it was.

---

## Output: design-review.html

One self-contained HTML file. All CSS and JS inline. The three skills do not each write their own file
when run through here.

**Where it goes.** Alongside the artefact reviewed, so it is findable from the thing it describes: a
review of `Personal projects/X/preview.html` writes `Personal projects/X/design-review.html`. If the
artefact is not a local file, a live URL or a Paper link, write it to the project the review belongs
to, and say where. Never leave the only copy in the chat.

**Check the counts before handing over.** The verdict states counts by severity and by lens, and they
are trivially wrong after a late edit. Count the rendered findings, do not carry forward a number
written earlier.

**Structure**

- **Header**: "Design Review", the artefact, the task frame, the reader frame, whose bar, the date.
- **Verdict**: counts by severity and by lens, then two sentences on whether this is fit to ship for
  the stated task, and what the single most important fix is.
- **The list**: every finding, prioritised as in Step 4, each tagged with its lens, carrying the
  element, what is true now, the fix, the severity, and the entry with its tier. Content findings show
  current and proposed copy side by side.
- **Measured values**: what `ui-review` computed, so the numeric claims can be checked.
- **Terminology audit**: from `content-review`, if anything was found.
- **Angles**: strategic observations, unscored, with the hand-off offer.
- **Not assessed**: consolidated.
- **Download as PNG**, client-side, with a fallback if the CDN is unavailable.

**HTML requirements**: severity and lens must both be separable without relying on colour alone.
System font stack or Inter. White background. Max width 1200px, centred. Sharp corners, flat fills, no
decorative shadows, consistent with the sibling reports from `analyse-themes` and `define-levers`.

Alongside the file, give a short summary in chat: counts by severity, the three findings that matter
most, and the local path. Hand back the path rather than a served link: it opens directly in any editor.

---

## What this skill does not do

- **It does not apply fixes.** The output is a list. Applying it is a separate request, and on your
  own work that means the build stages, or a direct edit.
- **It does not invent a bar.** Every finding traces to an entry in one of the three libraries. If
  something is wrong and no entry covers it, the owning skill proposes a library addition and waits,
  it does not quietly invent a standard mid-review.
- **It does not run the strategy skills.** It offers them.
- **It does not soften.** A Standard-tier failure is reported as a defect regardless of how much work
  the design clearly took.

---

## Tone

The report is read by the person who made the thing. Findings are observations with fixes attached,
never verdicts on the designer.

State the fix, not the failing. "Body copy is 3.5:1 against a required 4.5:1, #6E6E6E clears it" does
the whole job without a sentence about how this was missed.

Lead the verdict with what works, in one sentence, then the count. Not as flattery, but because a
review that opens with fourteen failures is one the reader argues with rather than acts on.

No em dashes in the report. Use commas and full stops.
