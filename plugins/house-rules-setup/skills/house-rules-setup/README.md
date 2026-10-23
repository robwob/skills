# house-rules-setup

Creates the house rules that personalise the design skills. House rules are an optional markdown file
holding your own evidenced preferences, where your shared components live, and the constraints of your
setup. The skills stay generic and read the file when it exists.

Works with `ui-review`, `ux-review`, `content-review`, `design-review` and `brief`.

## Use

> "Set up my house rules" or "add a house rule".

The skill asks whether the rules are yours (user level) or belong to a project, reads anything that
already exists, then interviews you section by section. It shows the full draft and writes only after
you approve it.

## Where the file lives

| Level | Path |
|---|---|
| Project | `.house-rules.md` in the project root |
| User | `~/.config/house-rules/house-rules.md` |

A project file overrides the user file, section by section. Sections are never merged. A section that
is absent falls back to the skill's default.

## Sections

| Section | What it holds | Read by |
|---|---|---|
| `## Visual` | Evidenced visual preferences | `ui-review`, `design-review` |
| `## Interaction` | Evidenced behaviour preferences | `ux-review`, `design-review` |
| `## Writing` | Voice and style rules | `content-review`, `design-review`, `brief` |
| `## Reuse` | Where shared components and sibling projects live | `ui-review`, `ux-review`, `brief` |
| `## Stages` | Which skill handles which design stage | `brief` |
| `## Constraints` | Facts that override a generic route | `brief` |

Every review ends with an "Applied:" line saying which rules it used.

## Install

**Claude Code / local.** Symlink the skill directory into your skills folder:

```
ln -s /path/to/house-rules-setup ~/.claude/skills/house-rules-setup
```

Skills are picked up when a session starts, so start a new session afterwards.

## Files

```
SKILL.md                           the interview and the rules for writing the file
references/house-rules-spec.md     the format, locations and resolution rules
references/house-rules-template.md the blank file
```
