# interview-analysis

Analyses user interview transcripts and writes the report: an overview summary on one page, then a
detailed report that backs every line of it with quotes and timestamps. Built for the usual export: a
CSV per interview, one row per turn, with who spoke, when, and what they said.

It codes every excerpt by how strong the evidence is, checks each participant's general claims
against their own account of a specific occasion, verifies every quote word for word at its
timestamp, and grades every finding, opportunity and recommendation **High, Medium or Low** with the
working shown. Then it stops, so you can approve the opportunities and recommendations, before
producing a final HTML or Word file.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`usability-test-analysis`, `survey-questions`, `desk-research` and `card-sort-analysis`. Given the
brief or the discussion guide it answers their research questions. For usability test results, use
`usability-test-analysis`.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/interview-analysis ~/.claude/skills/interview-analysis
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/interview-analysis/SKILL.md ] && echo OK || echo BROKEN
```

The script needs Python 3.9 or later and nothing else. Without Python the skill counts and grades in
visible tables and checks quotes by reading, and tells you it did.

**claude.ai.** Upload `interview-analysis.skill`. Uploaded copies are read-only, so the skill cannot
save an approved addition to its library, and it may not be able to run the script. It will say so.

## Use

> "Here are the six transcripts from our billing interviews. Can you write them up?"

> "Analyse these interviews against the research brief from last week."

It asks for what it needs (who the interviewer is, what you wanted to learn, the audience), maps the
columns with you, and replaces names with P1, P2 and so on. It reads everything, codes it, counts
participants per theme, checks claims against occasions, grades confidence, verifies every quote,
and shows you the draft. You approve or change the opportunities and recommendations, then choose
HTML, Word or markdown.

## What the report looks like

**Part 1, Overview summary:** headline, answers to the research questions, key findings,
opportunities and recommendations, each with its confidence, and the limits in one line.

**Part 2, Detailed report:**

1. Research overview, including what this number of interviews can and cannot show
2. What was said, by research question or topic, with themes, counts and quotes
3. Findings, each with its count, confidence and evidence
4. Claim against occasion: which claims held, which participants' own accounts contradicted
5. Opportunities, framed as needs, each naming its findings
6. Recommendations and next steps, agreed with you
7. Limits
8. Appendices: participant summaries, and the confidence working

## How confidence is graded

Adapted from GRADE-CERQual, the published method for grading confidence in qualitative findings.
Each finding is judged on four components: **adequacy** (enough data, rich enough), **coherence**
(does the data fit, or are there counter-cases), **evidence** (specific occasions, or opinions and
predictions) and **relevance** (do the participants match who the finding is about). It starts at
High and comes down for concerns. Opportunities take the lowest level of their findings.
Recommendations are capped at Medium, because interviews show a need, not that a particular answer
meets it, unless participants' own behaviour already shows it working. Every item says what would
raise its confidence.

## How solid the library is

The rules on quotes, small numbers and what interviews can show come from NN/g pages read directly
when the sibling skills were written. **The GRADE-CERQual papers, the saturation studies and the
opportunity framing were reached only through search summaries**, because the network this skill was
written on could not fetch them. They are tagged `(unverified)`, and the confidence rule is this
library's own adaptation, tagged `(derived)`.

Every claim in the library is tagged with how well it is sourced:

```
(verified)    retrieved and read
(unverified)  a named source, reached through a secondary summary
(convention)  widely repeated practice, no primary source
(derived)     the library's own inference
(house)       the author's standing practice, not citable and not overridden by a source
```

## What is in here

```
SKILL.md                         the process
README.md                        this file
references/input.md              the transcript layout and what to watch for
references/analysis.md           evidence types, claim against occasion, coding, quotes
references/confidence.md         the four components and the rule
references/opportunities.md      opportunity statements and recommendations
templates/report.md              the report structure
templates/report.html            the final HTML report
scripts/check.py                 columns, pseudonymise, stats, prompts, quotes, tally, confidence
examples/                        six made-up interviews and a worked set of files
tests/                           python3 -m unittest discover tests
```

When the skill meets something the library lacks, such as a transcript export it does not know, it
proposes an addition and waits. Nothing is written without your approval.

After editing anything here, rebuild the zip:

```
cd interview-analysis && zip -qr ../interview-analysis.skill SKILL.md README.md references/ templates/ scripts/ examples/
```
