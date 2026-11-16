# check.py

Arithmetic and checks for the analysis, so nothing is computed in the model's head. Python 3.9 or
later, standard library only. Reads CSV. For Excel, export to CSV first.

Run from the skill folder with `-I`, passing the results file as an argument.

| Command | Does |
|---|---|
| `columns results.csv` | Lists the columns, a sample value and a guessed type. A starting point for the mapping, never the mapping itself. |
| `pseudonymise results.csv --participant COL --out anon.csv --key key.csv` | Renames participants P1, P2 ... in order of appearance, replaces their full names inside answers, and lists first names that may still identify someone. The key stays private. |
| `ratings anon.csv --participant COL --question Q [--question Q2] --scale 1-7 [--json out.json]` | Per question: answered, blanks, values outside the scale, distribution, median, mean, each participant's rating, and the working. `--question` takes the exact text or, in the wide layout, the column number from `columns`. |
| `completion 4 6` | 95% adjusted-Wald interval for 4 of 6 completing a task. |
| `quotes anon.csv --participant COL --quotes quotes.json` | Checks every quote appears verbatim under the participant it is attributed to. Exits 1 if any does not. |

**Layouts.** Wide (one row per participant, the default) or long (`--layout long --question-col Q
--answer-col A`, one row per answer).

**What `quotes` forgives:** case, runs of spaces, and typographic quote marks and dashes. `...`
marks a cut, and the pieces must appear in order. Nothing else. A quote found under a different
participant is reported with who said it; a quote found nowhere shows the closest text, so it can be
replaced with the real words.

`quotes.json`:

```json
[{"quote": "I gave up and said I'd ring them.", "participant": "P4"}]
```

## Tests

```
python3 -m unittest discover tests
```

The completion tests reproduce two published worked examples: Sauro's 1 of 5 (about 2% to 64%) and
Lewis and Sauro's 7 of 10 (39.2% to 89.7%).
