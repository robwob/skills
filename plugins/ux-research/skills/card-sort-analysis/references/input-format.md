# Input format

The shape the analysis script reads, and how to get a tool's export into it. **Never assume a
file's layout.** Open it, read the headers, propose a mapping, and get the user to confirm.

**Last updated:** 21 October 2026

---

## The shape

One row per card placement, as a CSV in UTF-8:

| Column | Meaning |
|---|---|
| `participant_id` | any stable ID |
| `card` | the card's title |
| `category` | the name the participant gave the group, or the preset category in a closed sort. **Blank means the card was left unsorted.** |
| `order` | optional, ignored by the analysis |
| `category_preset` | optional, `true` when the researcher supplied the category (hybrid sorts) |

This is UXtweak's documented raw-results shape, generalised. `(verified)` for UXtweak's columns, in
`tools/uxtweak.md`.

## Mapping columns

If the headers differ, map them with `--col-participant`, `--col-card` and `--col-category`. The
script lists the columns it found when one is missing.

1. Read the headers and the first rows.
2. **Say what you think each column is, and why,** then ask the user to confirm or correct. A
   column called "Category" could be the standardised name or the raw one.
3. Do not compute anything until they confirm.

## Checks after mapping

Report these back before analysing:

- the number of participants and cards found, against what the user said
- the number of rows, against participants times cards. If it is lower, some cards were not sorted
  or were not exported, and you need to know which
- a short list of the distinct category names (`--list-categories`), which also shows whether
  names need standardising
- any category called "Unsorted" or similar. If it means a card was left unsorted, rerun with
  `--unsorted-label`. Otherwise it would be counted as a real group, which would make any two
  unsorted cards look similar

## Layouts you may meet

**Wide grid** (one row per card, one column per participant, each cell a category name). This is
the layout the guide uses for spreadsheet work. Convert it with:

```
python3 -I scripts/to_long.py grid.csv --out results.csv
```

Add `--card-col NAME` if the card column is not the first. Blank cells stay blank, meaning unsorted.

**Standardised and raw names both present** (UXtweak). Use the raw name as `category`, because the
similarity matrix uses each participant's own groups. Build the merge file from the pairs of raw and
standardised names, so the user's own standardising carries across. Check with the user first: their
tool's standardisation is theirs to confirm, not yours.

**A filtered export.** Some tools export all participants and some export only those left in the
analysis (Optimal Workshop's "uncut" and "filtered" downloads, UXtweak's "everyone included in
analysis" option). Ask which was used, because the participant count changes.

**Excel files.** Save as CSV UTF-8 first. Check merged cells and header rows did not shift the
columns.

**One cell holding a whole sort** (nested text mapping categories to lists of cards). A feedback
request for Useberry describes its CSV like this `(unverified)`. Do not guess a parser. Look at the
cell, agree a reading with the user, and write the conversion as a short throwaway script, showing
the user the first rows of the result before analysing.

**Percentages only** (a tool exports agreement percentages but not placements). The data route
cannot run, because the similarity matrix needs who put what where. Use the image route for the
views, and use the export for the cards and categories views as the tool computed them.

## Unsorted cards

Blank `category` means unsorted. How a card left unsorted counts toward a pair is a setting, not
a fact:

- `singleton` (the script's default): the card counts as "not together" with every other card and
  the participant stays in the denominator.
- `pairwise`: the participant is left out of any pair involving the card.

No source settles which is right. State the choice in the report. **Never treat "unsorted" as a
group.**

---

## Change log

**21 October 2026.** File created.
