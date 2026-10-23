---
name: house-rules-setup
description: >
  Use this skill to create, update or migrate the house rules that personalise the design skills.
  House rules are an optional markdown file holding your own evidenced preferences (visual,
  interaction, writing), where shared components live, your stage-to-skill routing and your
  constraints, at user level or per project. Triggers include: "set up my house rules", "personalise
  the design skills", "create a house rules file", "add a house rule", "update my house rules",
  "why isn't ui-review using my preferences", "what are my house rules", or when a review reports
  "no house rules, defaults only" and the user wants to fix that. Interviews the user, shows the draft,
  and writes only after approval. It does not review or build designs.
---

# House Rules Setup Skill

## Purpose

Create the file that adapts the design skills to one person or one project, without anyone editing a
skill. The skills stay generic. This skill writes the personal part.

Read `references/house-rules-spec.md` for the format, locations and resolution rules, and
`references/house-rules-template.md` for the blank file. Do not work from memory.

This skill writes one markdown file. It does not review a design, build one, or touch any skill.

---

## Before starting

Establish three things, one question at a time.

**1. Which level.**

| Level | Path | Choose when |
|---|---|---|
| **User** | `~/.config/house-rules/house-rules.md` | The rules are yours and follow you across projects |
| **Project** | `.house-rules.md` in the project root | The rules belong to this project: a brand, a client, a team. It can be committed and shared |

If unsure, default to user level and say that a project file can override any section later.

**2. What already exists.** Check the project path, the user path, and the legacy `~/.claude/house.md`.
Read any that exist and say what is in them. Then offer, as relevant:

- **Update**: add or change sections in the existing file.
- **Migrate**: a legacy file keeps working, but its headings may not match the six names the skills
  look for. Offer to write a new file with the correct headings, keeping the content, and leave the
  legacy file in place. Never delete it.
- **Start fresh**: only if the user asks.

**3. Which sections they want.** Six are available and every one is optional:
`## Visual`, `## Interaction`, `## Writing`, `## Reuse`, `## Stages`, `## Constraints`. Say what each
one changes (the spec's table), and let the user skip any. An absent section costs nothing: the
skills use their own defaults.

---

## The interview

Go section by section. Ask a few questions at a time, never a form of twenty.

### Rules come from evidence, not taste

For `Visual`, `Interaction` and `Writing`, do not ask "what do you like". Ask what has gone wrong:

> "What have you seen go wrong in your own work, more than once, that a reviewer should catch?"

Then ask for the reason behind each answer, because a rule with its reason is checkable and a bare
preference is not. If the user has no history yet, say so plainly and suggest leaving the section
empty: a sparse file that grows from real corrections beats a long file of guesses.

Write each rule as one line, with its reason after it. Where the rules already exist in a document
the user keeps, write a pointer instead of copying: "Read `path/to/craft.md` at review time." One copy
only.

| Section | Prompt |
|---|---|
| `Visual` | Spacing, colour, weight, density rules that were rejected in your own work. Applies to your work only, never above an accessibility standard |
| `Interaction` | Behaviours you always want: how destructive actions confirm, when forms validate, which states every flow must cover |
| `Writing` | Voice and style: punctuation you avoid, tone, reading level, terms to use or ban. It applies to your own copy and to any replacement copy the review writes |

### Reuse, Stages, Constraints

These are facts, not taste.

- **Reuse.** Ask where shared tokens, components and sibling projects live. **Check every path exists
  before writing it.** Offer to look in the project's `CLAUDE.md` or `AGENTS.md` and its folder
  structure to propose candidates, and present them as candidates for the user to confirm.
- **Stages.** Only for a user who has their own skills for design stages. List the skills actually
  installed and ask which stage each covers. Never invent a skill name. Leave the section out
  otherwise.
- **Constraints.** Facts about the setup that override a generic route: folders that must never leave
  the machine, plain HTML over a build step, how finished work is handed back. Ask for real examples
  from their setup.

---

## Writing the file

1. **Show the full draft** in the chat before writing anything, in the exact file format. Headings
   must be exactly the six names, each a level-two heading.
2. **Wait for approval.** Take edits and show the draft again.
3. **Write it.** For the user level, create `~/.config/house-rules/` if it is missing. If the target
   file already exists, show what changes and get explicit approval first. Never overwrite silently.
4. **Project files can be committed.** Before writing one, say so, and keep credentials and personal
   paths out of it. Personal material belongs in the user file. Do not edit `.gitignore` or commit
   anything unless asked.
5. **Remove empty sections** rather than leaving placeholder comments. An empty section is the same
   as an absent one.

---

## After writing

Read the file back and check the headings match exactly. Then tell the user, in a few lines:

- the path written, and the level
- which sections it has
- what each skill will now do with it, using this map:

| Section | Read by |
|---|---|
| `Visual` | `ui-review`, `design-review` |
| `Interaction` | `ux-review`, `design-review` |
| `Writing` | `content-review`, `design-review`, `brief` |
| `Reuse` | `ui-review`, `ux-review`, `brief` |
| `Stages`, `Constraints` | `brief` |

- that each review ends with an "Applied:" line saying which rules it used, so they can see it working
- how to grow it: when a review turns up a repeated correction, run this skill again to add a single
  rule

---

## Adding one rule

When the user asks to add a rule, do not rerun the interview. Find the right section, state the rule
as one line with its reason, show the line in place, and write it on approval. If the rule has no
reason or no evidence, say so and ask whether to add it anyway.

---

## What this skill does not do

- It does not invent rules. Every line comes from the user.
- It does not merge files. Each section resolves from one file, as the spec says.
- It does not delete a legacy file or edit any skill.
- It does not review designs. For that use `ui-review`, `ux-review`, `content-review` or
  `design-review`.

---

## Tone

Plain and brief. One question at a time. Say what a choice changes in the reviews, not how the file
is parsed.

No em dashes in the file or in chat. Use commas and full stops.
