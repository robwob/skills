---
name: option-explorer
description: Use when designing, wireframing or iterating screens in an option-explorer prototype (an HTML file carrying <meta name="generator" content="option-explorer">, usually named *-prototype.html, with one file per screen in prototype/screens/), or when starting a new prototype to compare layout options across several screens. Every iteration is frozen into explorations/ with a record entry (why, aim, outcome, the owner's words), so nothing is lost and nobody has to remember to save. Triggers include "wireframe this", "add an option", "try another direction", "change option B", "set up a prototype for this project", "show me the history", or any edit to a prototype or one of its screen files.
---

# Option explorer

A prototype holds several **screens**, each with several **options** (directions). Each
screen is its own file, so a change to one screen means opening one small file. Next to the
prototype, `explorations/` holds the **record**: every iteration of every option, frozen as it
was, with why it was made, what it aimed for and what happened to it. The owner should never
have to think about saving. This skill is the routine that makes that true.

The template is in `template/` beside this file. Its `README.md` documents the data model.

## Where things are

```
<project>-prototype.html     PROJECT and SCREEN_FILES (the screens, in panel order). Small.
prototype/screens/<name>.js  one screen: its options, render(), notes, questions, controls
prototype/design.css         design styles shared by the screens; one section per screen
prototype/shell.js, .css     the panel and frame. Never edited for a project.
explorations/                the record: freeze.py, records.js, the viewer, frozen copies
```

To change a screen, open its file in `prototype/screens/` and nothing else. The data model
for a screen file is documented at the top of `prototype/shell.js`.

## Setting up a project

1. Copy `template/index.html`, `template/.gitignore`, `template/prototype/` and
   `template/explorations/` into the project (usually `wireframes/`). Rename `index.html` to
   `<project>-prototype.html`. From `explorations/` copy only `freeze.py`, `index.html` and
   `records.js`, never frozen copies or `.autosave/`.
2. Set `PROJECT` and `SCREEN_FILES` in the prototype. Replace the placeholder screen files
   with one file per real screen (start each with the `/* option-explorer screen: <name> */`
   comment the hook looks for). Set `"project"` in `explorations/records.js`.
3. Ask whether the prototype and record go to git. If the repo has a remote and the answer
   is no, add the paths to `.git/info/exclude` and confirm with `git check-ignore -v`.
4. Freeze the starting state: one `freeze.py` run per option that exists (see below), then
   write each entry.

## Every change: the routine

Run this for every iteration the owner asks for. Do not skip it because a change is small.

1. **Check first.** `python3 explorations/freeze.py --check`. If it reports unrecorded
   changes, something was edited outside the routine: freeze the current state first as its
   own entry (title it for what it is, mark `"rebuilt": true` if you are reconstructing it
   from `explorations/.autosave/`), then carry on.
2. **Make the change in the screen's file** (`prototype/screens/<name>.js`, plus its
   section of `design.css` if the styles change). A change to a direction replaces that
   option's latest version. A new direction is a **new option** in the same screen, never a new file.
   Options are never deleted, chosen or not: change their `status`
   (`exploring`, `chosen`, `notchosen`).
3. **Freeze the result.**
   `python3 explorations/freeze.py --screen <key> --option <key> --title "<B3: what changed>"`
   (add `--screen-name "<Name>"` the first time a screen appears). It bundles the prototype
   and every file it loads into one self-contained `explorations/<screen>/NN-<slug>.html`,
   appends an entry, and marks the previous entry for that option `replaced`.
4. **Write the entry** in `explorations/records.js` (it is JSON after the `=`):
   - `why`: what prompted this iteration.
   - `aim`: what it was meant to achieve.
   - `outcome`: for the latest, its status; for the one it replaced, rewrite the generic
     "Replaced by ..." into why it was not kept, from the owner's feedback.
   - `quotes`: the owner's exact words that drove it, verbatim, typos included.
   - `open`: questions carried forward, when an option is chosen.
   - `views`: `[[label, "?param=value"]]` when the frozen copy has states worth jumping to.
   Follow the owner's writing rules (house rules) in entries.
5. **Decisions.** When the owner chooses or rejects an option, update its `status` in
   the screen file and set the latest entry's `status` to `chosen` or `rejected` with the reason.
   That is a record change, not an iteration: no freeze.
6. **Hand back** the prototype's file path, and say which entry was added.

One freeze per iteration the owner sees. Several fixes made in one turn are one iteration.

## The panel (fixed order)

Top bar, sticky: Device (Mobile, Desktop) and Annotations, with a one-line hint that the
notes are at the bottom. Then the header (title, description, link to every iteration),
**Screens**, **Options** (with status tags), any project-specific controls, Readout
(measured values only), Questions, Notes (numbered to match the `mk(n)` markers on the
screen, hidden with Annotations). Do not add copy under Device. Do not move Annotations out
of the top bar.

## Desktop

Add `renderDesktop()` to an option only when there is a desktop design. Without it, Desktop
mode shows the phone screen at phone width, centred, never stretched.

## Never

- Edit a frozen copy in `explorations/<screen>/` or anything in `.autosave/`.
- Edit `prototype/shell.js` or `shell.css` for one project. A need the shell does not meet
  is a change to the template, made there.
- Put a screen's markup or styles in another screen's file.
- Delete an option or a record entry. Status changes carry the history.
- Leave an entry's why, aim or outcome as `TODO` at the end of a turn.

## Safety net

The plugin ships a `PreToolUse` hook (`hooks/option-explorer-autosave.py`) that copies the
prototype, its screen files and its styles into `explorations/.autosave/` just before any of
them is edited, skipping
identical copies. Those snapshots are not record entries. They exist so a missed iteration
can be rebuilt. If you use this skill by symlink rather than as a plugin, add the hook to
your own settings; the README shows how.
