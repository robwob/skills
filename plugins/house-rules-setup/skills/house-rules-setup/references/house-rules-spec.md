# House rules specification

The house rules are how a person or a team adapts the design skills to their own preferences without
editing the skills. The skills stay generic. The house rules hold everything personal.

A skill that reads it must work without it. An absent file, or an empty section, means the skill's
own stated default applies.

---

## Where it lives

Two levels, plus one legacy path.

| Level | Path | Holds | Committed? |
|---|---|---|---|
| **Project** | `.house-rules.md` in the project root | Rules for this project only: its brand, its design system, its constraints | Can be, so a team shares it |
| **User** | `~/.config/house-rules/house-rules.md` | Your own defaults across everything you build | No. It is personal and sits outside any repo |
| **Legacy** | `~/.claude/house.md` | Read as a user-level file if the path above does not exist | No |

**Project lookup:** start in the folder of the artefact under review and look upward for `.house-rules.md`,
stopping at the repository root or the home directory.

---

## Sections

Six sections, each a level-two heading with exactly this name. Any may be absent or empty.

| Heading | What goes in it | Read by |
|---|---|---|
| `## Visual` | Evidenced visual preferences: spacing, colour, weight, density. Checked against the owner's own work only | `ui-review`, `design-review` |
| `## Writing` | Voice and style rules: banned punctuation, tone, reading level, terms to use or avoid. Checked against the owner's own copy, and used for any replacement copy written | `content-review`, `brief` |
| `## Interaction` | Evidenced behaviour preferences: how destructive actions confirm, when forms validate, what every flow must handle. Checked against the owner's own work only | `ux-review`, `design-review` |
| `## Reuse` | Real paths where shared components, tokens and sibling projects live, so a reuse audit knows where to look | `ui-review`, `ux-review`, `brief` |
| `## Stages` | Which skill handles which design stage, for a person who has their own build skills | `brief` |
| `## Constraints` | Facts about the setup that override a generic route: what must never leave the machine, build preferences, how work is handed back | `brief` |

A section may point to another file instead of holding the rules ("Read `design/craft.md` at review
time"). The skill follows the pointer. Prefer this when the rules already exist elsewhere, so there
is one copy.

---

## Resolution

For each section separately:

1. Use the section from the **project** file if it exists and is non-empty.
2. Otherwise from the **user** file, then the **legacy** file.
3. Otherwise the skill's documented default.

**A section is never merged across files.** The first non-empty one wins whole. Merging produces
rules nobody wrote, and the reader cannot tell where a rule came from.

---

## Reporting

Every skill that reads the file ends its output with one line saying what it used:

> Applied: Visual from project `.house-rules.md`, Reuse from user file, Writing by default.

If no file was found at all:

> Applied: no house rules, defaults only. `house-rules-setup` can create one.

Say it once and move on. Do not question the user about a file they may not know exists.

---

## Contract for a consuming skill

A skill that reads the file carries a short, self-contained block, because plugins install
separately and cannot rely on this document being present. The block states:

- the lookup order above, in one sentence
- which sections the skill reads
- the default for each when empty
- the reporting line

`ui-review` is the reference instance.

---

## Rules for the file's content

- **Evidence over taste.** A rule records something that was observed to go wrong, ideally more than
  once. "I like it" is a weak entry. "Cards with mismatched gaps were rejected three times" is a
  strong one.
- **Visual rules apply to the owner's own work.** Never to a competitor's, and never above a
  Standard: taste does not override an accessibility requirement.
- **No secrets.** A project file can be committed. Do not put credentials or private paths in it.
  Keep personal material in the user file.
- **Short.** The sections are optional, the length is not a goal.
