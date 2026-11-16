# usability-test-analysis

Analyses the results of a usability test and writes the summary report. Built for the usual export: a
spreadsheet of rating-scale questions and open-text answers or transcripts, from Playbook UX or any
other tool.

It checks every rating against what the same participant did or said, verifies every quote word for
word against the data, reports counts rather than percentages, and drafts the report in chat. Then it
stops, so you can shape the recommendations, before producing a final HTML or Word file.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions`, `desk-research` and `card-sort-analysis`. It analyses results, so it does not plan
or run the test. Given the plan from `usability-test-plan` it answers that plan's research questions.
Each skill works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/usability-test-analysis ~/.claude/skills/usability-test-analysis
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/usability-test-analysis/SKILL.md ] && echo OK || echo BROKEN
```

The script needs Python 3.9 or later and nothing else. Without Python the skill does the arithmetic in
a visible table and checks quotes by reading, and tells you it did.

**claude.ai.** Upload `usability-test-analysis.skill`. Uploaded copies are read-only, so the skill
cannot save an approved addition to its library, and it may not be able to run the script. It will
say so.

## Use

> "Here's the export from our Playbook UX test of the new checkout. Can you write it up?"

> "Analyse these results against the test plan I made last week."

It asks for what it needs (the tool, what was tested, what you wanted to learn), maps the columns
with you, and replaces names with P1, P2 and so on. It then works through the ratings, the stated
against observed check, the themes and the findings, and shows you the draft. You review the
recommendations, then choose HTML, Word or markdown.

## What the report looks like

1. Research overview, including what this number of participants can and cannot show
2. Summary and key findings, with answers to the research questions if a plan supplied them
3. Stated against observed: which ratings held, which the evidence contradicted
4. Question by question: distributions and themes, with verbatim quotes
5. Recommendations and next steps, drafted with you
6. Limits of this round

## How solid the library is

The rules on small numbers (no percentages, adjusted-Wald intervals for completion, report a
problem seen once) and on AI synthesis (verify every quote, transcripts are not observation) come from
MeasuringU and NN/g pages read directly. There is no published threshold for how many participants a
theme needs, and the library says so. **The Playbook UX profile is provisional**: it was written
without a real export, so your file wins wherever they differ.

Every claim in the library is tagged with how well it is sourced:

```
(verified)    retrieved and read
(unverified)  a named source, reached through a secondary summary
(convention)  widely repeated practice, no primary source
(derived)     the library's own inference
(house)       the author's standing practice, not citable and not overridden by a source
```

Two house rules apply across the family: a minimum of 6 participants for any qualitative round, and
every stated preference is checked against a specific piece of evidence that could disprove it.

## What is in here

```
SKILL.md                         the process
README.md                        this file
references/analysis.md           the library
references/tools/playbook-ux.md  Playbook UX profile (provisional)
references/tools/_generic.md     any other tool
templates/report.md              the report structure
templates/report.html            the final HTML report
scripts/check.py                 columns, pseudonymise, ratings, completion, quotes
examples/sample-results.csv      six made-up participants, to try the script on
tests/                           python3 -m unittest discover tests
```

When the skill meets something the library lacks, such as an export that differs from a profile, it
proposes an addition and waits. Nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd usability-test-analysis && zip -qr ../usability-test-analysis.skill SKILL.md README.md references/ templates/ scripts/ examples/
```
