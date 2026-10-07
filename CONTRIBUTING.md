# Contributing

The most useful contribution to these skills is a correction to a reference library.

## Correcting a reference library

Each skill keeps its sources in `references/`, and every claim there is marked:

- **unmarked** means it comes from a primary source that was read directly.
- **`(unverified)`** means the primary text was not available and the claim rests on a
  secondary source describing it.
- **`(derived)`** means sources disagreed and the claim is a reconciliation, with the
  reasoning stated next to it.

If you have the primary text for something marked `(unverified)`, that is the highest value
change you can make. Open a pull request that:

1. Quotes or cites the primary source, with a page or section reference.
2. Removes or keeps the mark, whichever the source now justifies.
3. Adds a dated line to the change log at the bottom of the file saying what changed and why.

A correction that contradicts what the file currently says is welcome. Say so plainly in the
pull request rather than softening it.

## Changing how a skill behaves

These skills are opinionated on purpose, so a change to the behaviour needs a reason rather
than a preference. Open an issue first and say what the skill did, what you expected, and
which part of the reference library led it there. That last part matters: if the skill made a
poor call because a reference file is wrong, the fix belongs in the file, not in the prompt.

## House rules

Two conventions apply across every file:

- **No em dashes.** Use a comma, a colon or a full stop.
- **Claims carry their status.** If you add something you have not verified, mark it
  `(unverified)` rather than leaving it to look settled.

## Scope

Pull requests that add a sixth research skill are likely to be declined. The five here are a
set that hand off to each other, and their reference libraries cross-reference. A new skill is
usually better as your own repo.
