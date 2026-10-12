# House rules

**This is the only file in the skill tied to a particular person or workspace. Everything else is
generic. What follows is a template: replace each section with your own and the rest of the skill
works unchanged. Leave a section empty and the skill uses the stated default instead of guessing.**

The skill reads this file before writing anything.

---

## Where to look during the reuse audit

The audit in section 13 needs to know where shared things live. List real paths.

- `design-system/` for shared tokens and components
- Sibling project folders, if your projects sit next to each other on disk
- The nearest `CLAUDE.md` or `AGENTS.md`, which names what a project is wired to

**Default when this section is empty:** read the nearest `CLAUDE.md` or `AGENTS.md` for named
shared locations, then search sibling directories of the project folder. Report where you looked.

---

## Design stages and the skills behind them

The catalogue in `stages.md` describes design stages generically. If named skills exist for them,
route to those instead of describing the work. Fill in whichever rows you have skills for and
delete the rest.

| Stage | Skill |
|---|---|
| Strategy, what problem is being solved | `analyse-themes` |
| Direction, what to dial up or down | `define-levers` |
| Structural wireframes, greyscale | |
| Interaction states | |
| Visual styling | |
| Review | `ux-review`, `ui-review`, `content-review`, `design-review` |

**Default when this section is empty:** describe what the stage produces and let whoever runs it
choose the method. Never invent a skill name.

---

## Writing style

Replace with your own. These are the defaults the skill assumes.

- No em dashes anywhere in a written brief. Use a period or a comma.
- Plain names for stages, never internal codes.
- Short. The sections are required, the length is not.

---

## Constraints that override a route

Things true of your setup that a generic route would get wrong. Examples of the kind of thing that
belongs here, not prescriptions:

- Which directories, if any, must never be deployed, pushed to a remote, or backed up off the
  machine. If a route would put such a path into a deploy or a repo with a remote, the route is wrong.
- Whether to prefer a build step or plain HTML, CSS and JS.
- How finished work should be handed back: a file path, a served link, a pull request.

**Default when this section is empty:** no overrides. Ask before anything that leaves the machine.
