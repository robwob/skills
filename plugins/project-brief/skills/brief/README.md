# brief

Defines a project before any design or code, then derives the plan from that definition.

Interviews for why it is being done, what the goal is, what it must do and what success looks like,
then works out which stages the project needs, research through to ship, in what order, with
approval points. Writes one file, `brief.md`, into the project folder.

Designs nothing and builds nothing.

## Install

Symlink or copy this directory into your skills folder:

```
ln -s /path/to/brief ~/.claude/skills/brief
```

Skills are picked up when a session starts, so start a new session afterwards. A broken skill
symlink fails silently, so confirm it loaded:

```
[ -e ~/.claude/skills/brief/SKILL.md ] && echo "brief OK" || echo "brief BROKEN"
```

## If someone has shared this with you

**Make your own house rules.** Run `house-rules-setup`, or write `.house-rules.md` in the project or
`~/.config/house-rules/house-rules.md` for yourself. `references/house-rules.md` is the bundled
fallback and template. Your rules are the only part tied to a particular person or workspace, and
they hold four things:

1. where shared components live, so the reuse audit knows where to search
2. which design skills you have, if any, so the route can name them
3. writing style
4. any constraint that overrides a route, such as paths that must never be deployed

Every section of it has a documented default, so the skill works with the file emptied out. It will
tell you which defaults it used rather than quietly guessing.

Nothing else needs editing. `SKILL.md`, `sections.md` and `stages.md` are generic.

## Use

> "I want to build X, help me write the brief"

or hand over existing notes, a rough brief or a chat transcript:

> "Turn this into a proper brief and plan"

Existing material is read first and used to pre-fill. It only asks for what is missing or vague.

## What it produces

`brief.md`, in sixteen sections:

- **Part A, why.** Why now, goal, core functions, what success looks like. Asked first. Section 4 is
  a gate: a project that cannot state success does not get a brief, it gets told so.
- **Part B, shape.** Who, when and on what platform, non-goals, the load-bearing principle, inputs
  and data, decisions with their rejected alternatives, open questions, failure modes, effort
  ceiling.
- **Part C, derived.** Reuse audit, stage route, the plan with activity types and gates, definition
  of done. These are worked out rather than asked, and shown back before the file is written.

Plus an update to the project's `CLAUDE.md` or `AGENTS.md`, so the next session finds the brief and
runs the plan the same way.

## How the plan is run

Two separate approvals, and one does not imply the other:

- **Before every stage**, it says what the stage will produce, what it touches, what it needs
  answered and roughly how long, then stops.
- **At a gate**, it shows the output and asks the question before building further.

## Activity types

Every stage in the plan is one of five, shown in its own column:

| Type | What it is |
|---|---|
| Research | Finding out something not currently known |
| Define | Deciding something, where the options are known and the choice is not |
| Design | Making the thing visible before it is real |
| Build | Writing the thing |
| Ship | Putting it where it is used |

## Files

| File | |
|---|---|
| `SKILL.md` | The interview, the gates, the approval rules |
| `references/sections.md` | The sixteen sections, with the test each answer must pass |
| `references/stages.md` | Stage catalogue, activity types, inclusion rules, ordering principles |
| `references/house-rules.md` | Bundled fallback and template for the house rules. Your own rules take precedence |
