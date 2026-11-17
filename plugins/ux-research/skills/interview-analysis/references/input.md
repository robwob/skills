# Transcript input

The layout `interview-analysis` expects, and how to map a file to it.

**Last updated:** 17 November 2026

---

## The expected layout

A CSV with **one row per turn**: who spoke, when, and what they said. `(house)`, the designer's
usual export.

| Column | Required | Notes |
|---|---|---|
| Speaker | Yes | A name ("Jordan Ellis") or a role label ("Interviewer", "Participant", "Speaker 2"). |
| Text | Yes | What was said in that turn. |
| Start | Strongly advised | When the turn started. `00:01:13`, `1:01:13`, `01:13`, `00:01:13,500` and seconds (`73.5`) are all read. |
| End | Optional | Where missing, a turn ends where the next one starts. |
| Interview | Only if one file holds several interviews | Otherwise each file is one interview, named after the file. |

The column names do not matter: they are mapped with the designer.

**Never assume the layout.** Run `check.py columns` on every file, propose which column is which and
which speaker values are the interviewer, and get it confirmed. `(derived)`

---

## Cases to watch for

- **Role labels, not names.** "Participant" in two files is two people. The script keys a
  participant by interview and speaker. Real names inside the text are then unknown and are not
  replaced, so read for them while coding.
- **More than one participant in an interview.** A paired interview, or a mislabelled interviewer.
  Ask which.
- **More than one interviewer**, or a note-taker who speaks. Give each as `--interviewer`.
- **No timestamps.** Quotes and codes cannot be tied to the recording. Say so in the limits, and cite
  participant only.
- **Speaker misattribution in automatic transcripts.** A turn that reads like the interviewer but is
  labelled as the participant, or the reverse. Ask the designer to correct it in the file before
  analysis, and note it.
- **A tool's AI summary or highlights.** Not data. Analyse the turns.
- **Word documents, text files or subtitle files.** Ask for a CSV export. If none exists, reshape
  into the layout above with the designer and say what you did.

---

## Questions to ask

- Which speaker values are the interviewer, and is anyone else speaking (an observer, a note-taker)?
- Is each file one interview?
- Were the transcripts automatic, and have they been corrected?
- Are the recordings available, so contradictions and key quotes can be checked?
- Is anyone in the files who should not be analysed: a pilot, a colleague, a no-show?

When a particular tool's export comes up often, propose a profile for it (SKILL.md, Proposing an
addition).

---

## Change log

**17 November 2026.** File created from the designer's description of their usual export.
