---
name: interview-analysis
description: >
  Use this skill to analyse user interview transcripts and write up what was said, the findings,
  opportunities and recommendations. Triggers include: 'analyse my interviews', 'interview
  transcripts', 'synthesise these interviews', 'what did the interviews show', 'write up the
  interview findings', 'interview synthesis', 'find themes in these transcripts', or one or more
  transcript files (usually CSV, one row per turn with speaker, timestamps and text) from user or
  customer interviews. Works standalone, or after discussion-guide and ux-research-brief, taking
  their research questions. Codes every excerpt by how strong the evidence is, checks each
  participant's claims against their own account of a specific occasion, verifies every quote word
  for word with its timestamp, grades every finding, opportunity and recommendation High, Medium or
  Low with the working shown, and pauses for the designer to approve the opportunities and
  recommendations before producing a final HTML or Word file. For usability test results use
  usability-test-analysis instead.
---

# Interview Analysis Skill

## Purpose

Turn a set of user interview transcripts into a report the team can act on: an **overview summary**
for people who read one page, and a **detailed report** that backs every line of it.

Four things set the report apart from a plain summary:

- **Every piece of evidence is traceable.** Each quote and each coded excerpt carries its participant
  ID and timestamp, and every quote is verified word for word against the transcript.
- **Evidence is weighed, not just counted.** An account of a specific occasion counts for more than
  a habit, an opinion or a prediction, and each participant's general claims are checked against
  their own occasions.
- **Every finding, opportunity and recommendation carries a confidence**: High, Medium or Low, from
  a rule adapted from GRADE-CERQual, with the basis stated.
- **The designer approves the opportunities and recommendations.** The skill drafts them and stops.

---

## The library

**Read the file for the step you are on before doing it. Do not work from memory.**

| File | Read it when |
|---|---|
| `references/input.md` | Before opening the transcripts. The expected layout and what to watch for. |
| `references/analysis.md` | Before coding. What interviews can show, evidence types, claim against occasion, coding, saturation, quote integrity. |
| `references/confidence.md` | Before grading anything. The four components and the rule. |
| `references/opportunities.md` | Before drafting opportunities and recommendations. |
| `templates/report.md` | Drafting the report. The structure is fixed; the number of items is not. |
| `templates/report.html` | Producing the final HTML file. |
| `scripts/README.md` | Before running the script. |

Claims in the library carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`,
`(house)`. Do not quote an `(unverified)` figure as established.

---

## House rules

These are the author's standing practice and they outrank any source that disagrees.

- **Check every claim against an occasion.** "I always send it when I get the reminder", followed by
  "I swiped it away and haven't done it yet", is a contradicted claim, and the contradiction is the
  finding. `(house)`
- **Six participants is the floor for a qualitative round**, per audience segment. Below it, say so
  in the limits. Never present it as a pass or fail. `(house)`
- **One round is a step in a sequence.** Interviews find and explain needs. They do not measure how
  common a need is or show that a solution works. Say what the next round should be. `(house)`
- **Nothing floats free of the data.** Every recommendation names its opportunity, every opportunity
  its findings, every finding its evidence. `(house)`

---

## Input

Before analysing, you need:

- **The transcripts**: CSV, one row per turn, with speaker, timestamps and text. One file per
  interview, or one file with an interview column.
- **Who the interviewer is** in the speaker column, and anyone else who speaks.
- **The research questions**, or what the team wanted to learn.
- **The audience**: one group or several, and which participant is in which.
- **How the interviews ran**: remote or in person, length, whether a discussion guide was used, and
  whether the transcripts are automatic and corrected.

**Called from `discussion-guide` or `ux-research-brief`**, or given their documents: take the
research questions, audience and the guide's topics from them and do not ask again. Confirm in one
line: "I'll answer the brief's three research questions and organise what was said by the guide's
topics. Right?"

**Standalone**: ask for what is missing, two questions at a time at most. If the designer does not
know something, infer it from the transcripts and **mark it *(inferred)* in the report**. Never
present a guess as a fact.

---

## Process

### Step 1, Intake

Ask for what the Input section lists and the designer has not given.

### Step 2, Map the transcripts, and confirm it

**Never assume a file's layout.** Read `references/input.md`, then:

`python3 -I scripts/check.py columns interview-01.csv [interview-02.csv ...]`

Propose which column is the speaker, the text, the start and end times, and (if one file holds
several) the interview, and which speaker values are the interviewer. **Get it confirmed.**

Without the script, open each file, show the headers and the first few rows, and propose the same.

### Step 3, Pseudonymise

Replace participant names with P1, P2 and so on before writing anything. Keep the key out of the
report.

`python3 -I scripts/check.py pseudonymise interview-*.csv --speaker "<col>" --text "<col>" --start "<col>" [--end "<col>"] [--interview "<col>"] --interviewer "<value>" --out anon.csv --key key.csv`

It combines the interviews into one file, replaces speakers' names inside the text, and lists first
names that may still identify someone. Show those to the designer. Names of other people, employers
and places are not touched, so read for them while coding. Every later step works on `anon.csv`.

### Step 4, Read, and check the interviewing

Read every transcript in full before coding. Then:

- `python3 -I scripts/check.py stats anon.csv`: length, turns and each participant's share of the
  words. Note any interview where the interviewer did most of the talking.
- `python3 -I scripts/check.py prompts anon.csv`: interviewer turns worded as hypothetical or
  leading. Read each; the answers to the real ones are weighed down in Step 5.

### Step 5, Code

Read `references/analysis.md`. For every participant turn that says something relevant, record a
row in a coding file:

```
participant,at,code,theme,evidence,stance
P1,00:01:13,estimated bill nearly double,Estimated bills arrive as a surprise,occasion,for
```

- `code`: short, close to the participant's words.
- `evidence`: `shown`, `occasion`, `general`, `opinion` or `hypothetical`.
- `stance`: `for` or `against` the theme.
- `at`: the start time of the turn.

Group codes into themes as you go and revise them once everything is coded. Write the file to the
working directory, not into the report.

### Step 6, Count

`python3 -I scripts/check.py tally coding.csv --transcripts anon.csv [--segments segments.csv] --json tally.json`

It counts participants (not mentions) for and against each theme, gives each supporter's strongest
evidence type and the spread across segments, checks that every row points to a real turn by that
participant, and suggests a concern on three of the confidence components. **Fix every row it
reports as a problem.**

Without the script, build the same table by hand, one row per theme with the participants listed,
and show it.

### Step 7, Claim against occasion

For each participant, pair every checkable general claim with their own account of a specific
occasion on the same subject, and classify it **Held**, **Contradicted** or **No occasion
described** (`references/analysis.md`). Use their words for both sides, each with its timestamp.

### Step 8, Findings, and what was said

- **What was said:** for each research question or guide topic, a short summary, the themes with
  counts, quotes, who said otherwise, and what participants asked for (marked as hypotheticals).
- **Findings:** the patterns across the interviews. Each with a plain statement, "x of n", who was
  against, 1 to 3 pieces of evidence with timestamps, and a labelled interpretation. Include what
  works well, to the same standard. Keep the one-off that matters, at its true count.
- **Answer each research question**, pointing to the findings. "Not answered by these interviews" is
  a valid answer.

**Never write a percentage for fewer than 20 participants.** Write "4 of 6".

### Step 9, Opportunities and draft recommendations

Read `references/opportunities.md`. Write each opportunity as a need with no solution inside it,
for the people the evidence covers, naming its findings. Draft two or three recommendations at most
per opportunity, each naming its opportunity, its expected impact, and what research would raise its
confidence.

### Step 10, Confidence

Read `references/confidence.md`. For every finding, judge the four components (adequacy, coherence,
evidence, relevance), starting from the `tally` suggestions, with a reason for anything above
"none". Write them to `assessments.json` with the opportunities and recommendations (format in
`scripts/README.md`), then:

`python3 -I scripts/check.py confidence assessments.json --json levels.json`

Use its levels and working in the report. **Fix every problem it reports.** Without the script,
apply the rule by hand in a table and show it.

### Step 11, Verify

Before showing anything, check every quote, on both sides of every claim against occasion too:

1. Write the quotes to a file: `[{"quote": "...", "participant": "P3", "at": "00:03:11"}, ...]`
2. `python3 -I scripts/check.py quotes anon.csv --quotes quotes.json`

Fix every quote that is not `VERBATIM`: use the participant's exact words, the right participant and
the right timestamp, or drop it. A quote flagged **INTERVIEWER'S WORDS** is never evidence. Cut only
with "...". Never tidy grammar or spelling.

**Without the script**, find each quote in the transcript yourself and confirm it character for
character and its timestamp, then tell the designer the quotes were checked by reading, not by
script.

Check every count in the draft against `tally` too.

### Step 12, Draft and pause

Fill `templates/report.md`: the overview summary, then the detailed report. Mark the opportunities
and recommendations as drafts. Show the whole draft **in the chat**, as markdown, and end with the
template's closing prompt, inviting the designer to change, remove or add opportunities and
recommendations.

**Stop and wait.** Do not present the opportunities or recommendations as final until the designer
has replied.

### Step 13, Finalise

Fold in the designer's changes. Their recommendations are theirs: record them as given and do not add
evidence they did not cite. If one comes from no finding, say so once, mark it "not assessed"
(`"designer_only": true` in the assessments), and leave it in if they want it. Re-run `confidence`
after any change to the findings, opportunities or recommendations.

Then ask what the final report should be: **an HTML file, a Word document, or stay as markdown**.
Produce it from the agreed draft, so the formats cannot disagree.

- **HTML**: fill `templates/report.html`. Self-contained, no external requests.
- **Word**: use the docx skill (in Claude Code, invoke `anthropic-skills:docx`; on claude.ai,
  read `/mnt/skills/public/docx/SKILL.md`; elsewhere, a docx skill if installed, otherwise
  python-docx, and say which). Arial 12pt, A4, 1 inch margins, Heading 1 per section, proper
  bullet lists and tables, quotes as indented paragraphs.

**Filename:** `Interview Findings - [Project name].html` or `.docx`.

Hand back the **absolute file path**. Do not start a server.

---

## Rules the skill does not break

1. **No untraceable evidence.** Every quote and excerpt has a participant ID and, where the
   transcript has them, a timestamp.
2. **No unverified quote**, and never the interviewer's words as evidence.
3. **No claim on its own.** Every checkable general claim sits next to its claim-against-occasion
   result.
4. **No ungraded finding, opportunity or recommendation.** Each has a level and a basis.
5. **No percentages below 20 participants.** Counts out of the total.
6. **No names.** Participant IDs only. The key stays out of the report.
7. **No fixed number of findings.** The data decides how many.
8. **No silent inference.** Anything not read from the data or confirmed by the designer is marked
   *(inferred)*.
9. **No final opportunities or recommendations without the designer.** Draft, then stop.
10. **Never invent a file layout.** Inspect it or ask.

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose** a tool profile for a transcript export that comes up often, a correction to the input
notes, a source that confirms or contradicts an `(unverified)` claim, or a change to the confidence
rule the designer asks for. **Do not propose** a restatement of an existing entry, or a preference
dressed as a finding. A designer's own standing practice is `(house)`.

**Format:**

> **New [tool profile / source / correction / rule change] proposed: [Name]**
>
> **What it is:** one sentence.
>
> **Source:** a named source and whether it was read directly or through a summary, or "none, this
> would be `(house)` or `(convention)`".
>
> **Evidence in this session:** what prompted it.
>
> Add this to the library?

**Wait for the answer.** After approval, edit the file in place, match the surrounding format, tag
every claim, add a dated line to its change log, and confirm what changed. A change to the rule is
made in `references/confidence.md` and in `scripts/check.py`, with a test, so the two cannot
disagree.

**If this skill is running somewhere the files cannot be written** (an uploaded copy on claude.ai
is read-only), say so plainly rather than reporting a save that did not happen, and output the
exact markdown to paste in.

---

## Tone and language

- UK English throughout.
- Plain statements. "4 of 6 participants had an estimated bill they did not expect" beats "users
  were frustrated by billing".
- No em dashes in anything the user will read, send or publish, including generated files.

---

## Standalone usage

If invoked directly, open with:

> "I'll analyse your interviews and write up the findings. Can you share the transcript files, tell
> me who the interviewer is, and what you wanted to learn? If you have the research brief or the
> discussion guide, share those too and I'll use their research questions."

Then follow the Process.
