# option-explorer

Compare layout options across several screens in one HTML prototype, and keep a record of
every iteration without anyone having to remember to save.

**What you get**

- **A prototype** (`template/index.html` plus `template/prototype/`): a panel of screens and
  options beside the screen in a phone or browser frame, with annotations, measured readouts
  and open questions. Each screen is its own file, so a change touches one small file. Plain
  HTML and JavaScript, no dependencies, opened straight from disk.
- **A record** (`template/explorations/`): every iteration of every option, frozen as it was,
  with why it was made, what it aimed for, what happened to it and the owner's own words.
  Browse it in `explorations/index.html`.
- **A routine** (this skill): after every change, freeze the new version, mark the old one
  replaced and write the entry. A new direction becomes a new option in the same screen file;
  options are never deleted, only given a status.
- **A safety net** (the plugin's hook): a snapshot of the prototype just before every edit,
  so an iteration made outside the routine can still be rebuilt.

**Use it** by asking to set up a prototype, or by asking for a change to a file built from
the template. The template's own `README.md` documents the data model, the URL parameters and
`freeze.py`.

**Without the plugin.** If you symlink the skill instead of installing the plugin, the hook
is not installed. Add it to `~/.claude/settings.json` yourself, pointing at
`hooks/option-explorer-autosave.py` in this plugin:

```json
"PreToolUse": [{ "matcher": "Edit|Write|MultiEdit",
  "hooks": [{ "type": "command", "command": "python3 \"<path to>/option-explorer-autosave.py\"" }] }]
```
