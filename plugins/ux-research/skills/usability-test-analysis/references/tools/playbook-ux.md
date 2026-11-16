# Playbook UX

**PROVISIONAL.** Written without a real export, and without reading Playbook's own pages: every
Playbook page returned an error to the research tool, so everything below comes from search-engine
summaries of those pages and one third-party listing. **Trust the user's file over this profile.**

**Checked:** 16 November 2026.

---

## Test types

Moderated interviews and unmoderated testing are separate products. `(unverified)` Both are
confirmed by a third-party listing (User Interviews, 2022). `(verified)`

## Question and task blocks in unmoderated tests

The marketing page lists "verbal response questions, tasks, multiple choice, rating scale and
written response". `(unverified)` The labels in the builder may differ.

| Block | Treat it as |
|---|---|
| Rating scale | Rating. **The range and labels are not documented**: read them from the data and ask the user for the exact wording, before comparing with any benchmark. |
| Written response | Open text. |
| Verbal response | Open text, transcribed. A spoken answer to a question, not a recording of the task. |
| Task | The task itself. Pair its rating and responses with it. Whether a success flag, time or path is recorded is **not documented**. |
| Multiple choice | Category. Count it; never average it. |

## Export

- An **Excel** file per project, from the project's three-dot menu, then Export. Covers moderated,
  unmoderated, card sort, tree test and survey projects. `(unverified)`
- **Not documented:** what a row is, the column headings, whether transcripts are in it, and how
  participants appear (name, email or ID). Assume names may be present and pseudonymise.
- Transcripts are generated automatically with timestamps and are editable in the tool.
  `(unverified)` If they are not in the export, ask the user to copy the task transcripts in, one
  file or column per participant.

## Playbook's own AI

AI summaries of sessions, tasks and whole projects, auto-tagging, and executive reports built from
quotes. AI features appear to be Enterprise only. `(unverified)`

**Do not take an AI summary or tag as data.** It is a summary of the data. Analyse the responses and
transcripts themselves, and if the user pastes a Playbook summary, use it only as a cross-check.
NN/g's assessment of such tools is in `references/analysis.md`. `(derived)`

## Route

1. Ask for the export as CSV (Excel, then Save As or Download as CSV), or the headers and a few rows.
2. Run `check.py columns` and map the columns with the user. Expect either one row per participant
   (wide) or one row per answer (long). Both are handled.
3. Ask whether task transcripts or recordings exist outside the export. Without them, the only
   paired evidence for a rating is the participant's written or verbal answer, and the report says
   so.

## Questions to ask this user

- What are the export's columns? A few rows will do.
- What exactly did the rating question say, and what were its endpoints?
- Were task responses verbal (think-aloud) or written?
- Does the export include transcripts, or do they need copying in?
- Is a task success or completion recorded anywhere?

## Known unknowns

The rating scale's range and labels, the export layout, transcript export, participant identity in
the export, any task success, time or click data, and which plans include export.

---

## Sources

All reached through search summaries, not opened:

- Playbook UX, [Export results](https://help.playbookux.com/en/articles/4157474-export-results)
- Playbook UX, [Unmoderated testing](https://www.playbookux.com/unmoderated-testing/)
- Playbook UX, [User testing software features](https://www.playbookux.com/user-testing-software-features/)
- Playbook UX, [Pricing](https://www.playbookux.com/pricing/)

Opened: User Interviews, [Playbook UX listing](https://www.userinterviews.com/2022-tools/playbookux), 2022.

---

## Change log

**16 November 2026.** File created, marked provisional. To be replaced from a real export.
