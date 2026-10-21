# A tool not listed here

How to proceed when the card sort was run in a tool without its own profile, or when a profile is
unverified.

**Last updated:** 21 October 2026

---

## The principle

**Trust the user's file over any profile, and never assume a layout.** No tool profile in this
library was written from a real export of that tool, apart from the documented UXtweak columns. The
profiles describe what documentation says.

## Procedure

1. **Ask what the tool shows and what it exports.** Which views does it have (cards, categories,
   a matrix of cards by categories, a similarity matrix, a dendrogram)? What can be downloaded?
2. **Ask for the headers and the first few rows,** or a small export. Say it can be dummy data.
3. **Propose a column mapping** to `participant_id`, `card` and `category` (see `input-format.md`)
   and ask the user to confirm it.
4. **Find out how the tool shows unsorted cards,** if any exist.
5. **For any matrix or dendrogram, ask the four questions** in `image-route.md`: what a darker cell
   means, whether values are printed, what the dendrogram's axis shows and which way is more similar,
   and which method produced it.
6. **Choose the route** from what the user can supply (data, image or combined).
7. **Tell the user the profile is generic,** so the findings from a screenshot carry lower
   confidence, and name what you could not confirm.

## What to record

If the user's file or screenshots show something this library lacks (a tool's export columns, a
view's colour meaning), offer to add a profile. Use the proposal format in `SKILL.md`. Do not write
one without approval, and mark anything you could not read from a primary source as unverified.

---

## Change log

**21 October 2026.** File created.
