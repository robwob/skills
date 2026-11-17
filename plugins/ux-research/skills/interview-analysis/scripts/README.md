# check.py

Arithmetic and checks for the analysis, so nothing is counted or graded in the model's head. Python
3.9 or later, standard library only. Reads CSV. For Excel, export to CSV first.

Run from the skill folder with `-I`, passing the files as arguments.

| Command | Does |
|---|---|
| `columns a.csv [b.csv ...]` | Lists each file's columns, a sample value, a guessed type, and the distinct values of any column that looks like the speaker. A starting point for the mapping, never the mapping itself. |
| `pseudonymise a.csv [b.csv ...] --speaker COL --text COL [--start COL] [--end COL] [--interview COL] --interviewer VALUE [--interviewer VALUE2] --out anon.csv --key key.csv` | Combines the interviews into one file with the columns `interview, turn, participant, role, start, end, text`. Renames participants P1, P2 ... in order of appearance, replaces speakers' names inside the text, and lists first names that may still identify someone. The key stays private. |
| `stats anon.csv` | Per interview: length, turns and words by interviewer and participant, and the participant's share of the words. Flags interviews where the interviewer spoke more. |
| `prompts anon.csv` | Interviewer turns worded as hypothetical ("would you...") or leading ("..., right?"), with who answered and when. Matches wording, so read each. |
| `quotes anon.csv --quotes quotes.json` | Checks every quote appears verbatim in that participant's turns, at the timestamp given. Exits 1 if any does not. |
| `tally coding.csv --transcripts anon.csv [--segments segments.csv] [--json out.json]` | Per theme: participants for and against, each supporter's strongest evidence type, the spread across segments, and suggested concerns for adequacy, coherence and evidence. Checks every row points to a real turn. Exits 1 on a bad row. |
| `confidence assessments.json [--json out.json]` | Applies the rule in `references/confidence.md` to findings, opportunities and recommendations, and prints the working. Exits 1 on a missing reason, an unknown source or an invalid override. |

**A participant** is a non-interviewer speaker within one interview, so "Participant" in two files is
two people. **Timestamps** are read as `1:02:03`, `01:02:03.500`, `00:01:02,500`, `62:03` or seconds.
Where a turn has no end time, it ends where the next turn starts.

## quotes.json

```json
[{"quote": "I put a reminder in my own calendar", "participant": "P3", "at": "00:03:11"}]
```

`at` is optional; given, it must fall within the turn the quote is in. Results:

| Result | Means |
|---|---|
| `VERBATIM` | Found in that participant's turns, at that time. |
| `TIMESTAMP WRONG` | Their words, at a different time, which is printed. |
| `INTERVIEWER'S WORDS` | Said by the interviewer. Never evidence. |
| `WRONG PARTICIPANT` | Said by someone else, who is named. |
| `NOT FOUND` | Not said. The closest text is printed so it can be replaced with the real words. |

**What it forgives:** case, runs of spaces, typographic quote marks and dashes. `...` marks a cut,
and the pieces must appear in order. A quote may run across consecutive turns by the same
participant. Nothing else.

## coding.csv

```
participant,at,code,theme,evidence,stance
P1,00:01:13,estimated bill nearly double,Estimated bills arrive as a surprise,occasion,for
```

Required: `participant`, `theme`, `evidence` (`shown`, `occasion`, `general`, `opinion`,
`hypothetical`) and `stance` (`for`, `against`). `at` and `code` are advised. Extra columns are
ignored.

## segments.csv

```
participant,segment
P1,Manual readings
```

## assessments.json

```json
{
  "findings": [
    {"id": "F1", "title": "...",
     "adequacy":  {"concern": "none",  "why": ""},
     "coherence": {"concern": "minor", "why": "P6 is on a fixed payment."},
     "evidence":  {"concern": "none",  "why": ""},
     "relevance": {"concern": "none",  "why": ""}}
  ],
  "opportunities": [{"id": "O1", "title": "...", "from": ["F1", "F2"]}],
  "recommendations": [
    {"id": "R1", "title": "...", "from": ["O1"]},
    {"id": "R2", "title": "...", "from": ["O2"], "shown_in_behaviour": "P1, P2 and P5 already ..."},
    {"id": "R3", "title": "...", "designer_only": true}
  ]
}
```

A concern is `none`, `minor`, `moderate` or `serious`; anything above `none` needs a `why`. Any item
can take `"override": "Low", "override_why": "..."` to lower its level by judgement. An override
cannot raise one. `shown_in_behaviour` lifts the Medium cap on a recommendation and must cite the
occasions. `designer_only` marks the designer's own recommendation with no finding behind it.

The examples folder has a full set to try: six interviews, a coding file, segments, assessments and
quotes.

## Tests

```
python3 -m unittest discover tests
```
