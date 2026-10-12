---
name: content-review
description: >
  Use this skill to evaluate the words in a design against content design best practices and
  recommend changes. Covers copy only: headings, labels, button text, helper text, error messages,
  empty states, link text, alt text, terminology consistency, plain language and tone. Triggers
  include: "review the copy", "content review", "is this copy clear", "check the microcopy", "review
  the error messages", "UX writing review", or any request to assess what a design says rather than
  how it works or looks. Accepts screenshots, live URLs, local HTML, Figma/Paper links, or a plain
  list of strings. Produces a self-contained HTML report of findings by severity. For flows use
  `ux-review`, for visual craft use `ui-review`, for all three at once use `design-review`.
---

# Content Review Skill

## Purpose

Measure the words in a design against the bar in `references/content-standards.md` and report what is
unclear, wrong or missing, with the replacement written out.

This skill evaluates and rewrites the specific strings it flags. It does not restructure the design.

---

## Scope

**This skill owns every word in the interface.** Findings must be filed with their owner so a combined
review does not report the same defect three times.

| Concern | Owner |
|---|---|
| Headings, labels, button and link text, helper text | `content-review` |
| Error, empty, loading and success copy | `content-review` |
| Alt text, link text, sensory-characteristic instructions | `content-review` |
| Terminology consistency, plain language, tone | `content-review` |
| Whether a state exists at all, and when a message appears | `ux-review` |
| Type size, weight, colour and contrast of that text | `ui-review` |

The edge cases, decided in advance:

- **Missing error copy** splits: that no error state exists is `ux-review`; that the message which
  does exist says "Invalid input" is `content-review`.
- **Alt text is content**, not a visual property, so it is reviewed here despite being an
  accessibility concern.
- **An error styled in red with no text** is one defect with two owners: `ui-review` reports the 1.4.1
  colour-alone failure, `content-review` reports the absent message. In a combined review, file it
  once under `content-review`, because writing the message is the fix.
- **Reading order and heading hierarchy** split: whether headings are correctly nested is `ux-review`
  (screen reader navigation); whether a heading says anything useful is `content-review`.

---

## Before analysing

Read `references/content-standards.md` first. Do not work from memory.

| Input | Method | What stays unassessable |
|---|---|---|
| **Live URL or served local HTML** | Extract every string from the DOM, plus link text, alt attributes and button labels. This makes the terminology audit and the F84 link check mechanical rather than impressionistic | Copy behind interactions not triggered: errors, confirmations, states not on screen |
| **Static screenshot** | Read the visible copy | Alt text, link targets, any string not pictured, which is usually most of the error and empty-state copy |
| **Figma or Paper artboards** | Read the copy across all artboards | Alt text, and any state not drawn |
| **A list of strings** | Full review of what is given, but with no context for whether each label matches what it does | Everything contextual. Say so |

For a served page, extracting strings is in scope by default. **Triggering flows to see their copy is
not, unless asked.** Where the error and empty-state copy could not be seen, say so rather than
reporting the happy path as if it were the whole product.

Useful extraction on a served page:

```js
// every link, for the F84 duplicate-text check
[...document.querySelectorAll('a[href]')].map(a => ({ text: a.textContent.trim(), href: a.href }));
// every control label, for the terminology audit
[...document.querySelectorAll('button, label, h1, h2, h3, [role=button]')].map(e => e.textContent.trim());
// alt text, including the empties
[...document.images].map(i => ({ src: i.currentSrc, alt: i.getAttribute('alt') }));
```

---

## The reader frame

**Copy is only clear relative to a reader and a moment.** Before analysing, state both in one
sentence, and confirm if not given:

> "I'm reviewing this copy as: [reader] at the point of [moment]. Correct me if that's wrong."

The same sentence can be right on a marketing page and wrong on a failed payment. Without the frame,
a content review becomes a style argument.

---

## Process

### Step 1, Inventory the strings

Collect every string, grouped by type: headings, labels, buttons and links, helper text, errors,
empty and success states, alt text. The inventory is what makes the terminology audit and the link
check possible, and it also exposes what is missing.

### Step 2, Run the mechanical checks

These are objective and should be done before any judgement:

- **Link check (F84).** Any two links with identical text and different destinations. Any link text
  that does not name its destination.
- **Terminology audit.** Group strings by concept, flag every concept named two or more ways, and
  every word doing two jobs.
- **Alt text.** Every meaningful image has an equivalent, every decorative one is empty, every
  functional one names the action rather than the picture.
- **Sensory instructions.** Any copy relying only on colour, shape, size or position.
- **Capitalisation consistency.** Within the product, not against an external house style.

### Step 3, Test against the library

Work through `references/content-standards.md`. Selection, not completion.

Check the error-message anatomy explicitly, all five parts. Constructive, the part saying how to fix
it, is the one most often missing, and its absence is the highest-value content finding there is.

### Step 4, Assign severity

| Severity | Bar |
|---|---|
| **Blocker** | Fails a **Standard**: link purpose, alt text, sensory characteristics. Or copy that is actively misleading about what an action does. |
| **Major** | Contradicts **Evidence**: an error message with no fix, an empty state that explains nothing, a heading that says nothing in the position that does the most work. |
| **Minor** | A **Convention** deviation or an inconsistency that does not impede the reader. |
| **Suggestion** | A rewrite that is better but not tied to any entry. Kept in its own section, never mixed with findings. |

That last row is the discipline that keeps this skill honest. Preference gets labelled as preference.

### Step 5, Write the replacement

**Every finding carries the replacement string, written out.** A content finding without the new
words is half a finding. Match the product's voice where one is declared; where none is, match the
register of the copy that already works.

**A finding you could have written without reading this copy is not a finding.** "Make the copy
clearer" is not a finding. "The submit button says 'Continue', but it charges the card. 'Pay 24.99'
names what happens" is.

### Step 6, State what you could not check

Required. List the strings the input format kept out of reach, particularly error and state copy.

### Step 7, Propose additions, then stop

Surface any candidate library additions and wait.

---

## Proposing an addition

The library is a first pass and is expected to change. **Nothing is written without the maintainer's explicit
approval.** Propose, then stop.

**Propose a new entry when** a real content problem is observed that no existing entry covers.

**Do not propose** a rule you cannot source at one of the tiers: **Standard** needs a citable
requirement, **Evidence** needs a primary study, **Convention** needs adoption across established
systems. **Voice** entries are per product and belong in that product's own documentation, not here.

Content design attracts more unsourced rules than any other design discipline, so this bar matters.
The library already rejects "5 to 8 word sentences", paragraph word caps and readability formulas as
gates. Anything unsourceable goes to **Excluded, and why** with the reason.

**Format:**

> **New entry proposed: [Name]**
>
> **Section and tier:** where it sits, which tier, and the source that qualifies it.
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing]:** one sentence.
>
> **Evidence in this design:** the specific string that prompted it.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit `references/content-standards.md` in place, matching the
surrounding format, and confirm what changed.

If running somewhere the file cannot be written, an uploaded copy on claude.ai is read-only, say so
plainly rather than reporting a save that did not happen, and output the markdown to paste in. Then:

```
cd <the content-review directory>
zip -qr ../content-review.skill SKILL.md references/
```

---

## Output: content-review.html

A single self-contained HTML file. All CSS and JS inline.

**Structure**

- **Header**: "Content Review", the design reviewed, the reader and moment it was reviewed against,
  the date.
- **Verdict line**: counts by severity, then one sentence on whether the copy is fit to ship.
- **Findings**, ordered Blocker then Major then Minor. Each shows **current** and **proposed** copy
  side by side, then the reason with its entry and tier. The side-by-side is the point: this report
  should be usable as a paste-in list.
- **Terminology audit**: a compact table of every concept named more than one way, with the term to
  standardise on.
- **Suggestions**: rewrites not tied to an entry, clearly separated.
- **Not assessed**: the strings the input kept out of reach.
- **Download as PNG**, client-side, with a fallback if the CDN is unavailable.

**HTML requirements**: current and proposed must be distinguishable without relying on colour alone.
System font stack or Inter. White background. Max width 1200px, centred. Sharp corners, flat fills, no
decorative shadows.

Alongside the file, give a short summary in chat: the counts, the three findings that matter most, and
the local path.

---

## Tone

Write findings as the replacement plus the reason.

- "'Submit' becomes 'Send message'. The button names the action rather than the mechanism."
- "'Error: invalid input' becomes 'Enter a postcode like SW1A 1AA'. The current message says something
  is wrong but not what or how to fix it, which fails three of the five parts of the anatomy."
- "'Learn more' appears four times pointing at four different pages. Each becomes the destination:
  'How pricing works', 'Read the security overview', and so on."

Never argue a rewrite from taste. If the reason is not in the library, it belongs in Suggestions.

No em dashes in the report. Use commas and full stops. This applies to
proposed copy as well as to the report.
