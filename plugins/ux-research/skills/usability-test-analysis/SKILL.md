---
name: usability-test-analysis
description: >
  Use this skill to analyse the results of a usability test and write the summary report.
  Triggers include: 'analyse my usability test', 'usability test results', 'summarise the test
  sessions', 'synthesise these transcripts', 'what did the usability test show', 'write up the
  usability findings', 'average the ratings', or a results spreadsheet (CSV or Excel) from Playbook
  UX, Maze, Lyssna, UserTesting, Useberry or any other tool, mixing rating-scale questions with
  open-text answers or transcripts. Works standalone, or after usability-test-plan and
  ux-research-brief, taking their research questions and success criteria. Checks every rating
  against what the same participant did or said, verifies every quote word for word against the
  data, drafts the report in chat, and pauses for the designer to shape the recommendations before
  producing a final HTML or Word file. Does not plan or run the test, which belongs to
  usability-test-plan.
---

# Usability Test Analysis Skill

## Purpose

Turn the raw results of a usability test into a summary report the team can act on. The data is
usually a spreadsheet mixing rating-scale questions with open-text answers or transcripts.

Three things set the report apart from a plain summary:

- **A rating is never reported on its own.** It is checked against what the same participant did
  or said on the same task, and a rating that the evidence contradicts is a finding in its own
  right.
- **Every quote is verified word for word** against the data before it goes in the report.
- **The designer writes the recommendations with you.** The skill drafts them and stops. Nothing
  is final until the designer has reviewed them.

---

## The library

**Read the file for the step you are on before doing it. Do not work from memory.**

| File | Read it when |
|---|---|
| `references/analysis.md` | Before analysing. Ratings at small numbers, stated against observed, task success, severity, coding open text, quote integrity, and what a round of this size supports. |
| `references/tools/<tool>.md` | After the user names the tool. `_generic.md` if it is not listed. |
| `templates/report.md` | Drafting the report. The structure is fixed; the number of findings is not. |
| `templates/report.html` | Producing the final HTML file. |
| `scripts/README.md` | Before running the script. |

Claims in the library carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`,
`(house)`. Do not quote an `(unverified)` figure as established.

---

## House rules

These are the author's standing practice and they outrank any source that disagrees.

- **Corroborate every stated rating against the observed record.** Someone who rates a task 7 out
  of 7 after saying "I wasn't sure it had saved, so I did it again" has given a claim that failed,
  not a satisfaction score. The contradiction is the result, not noise. `(house)`
- **Six participants is the floor for a qualitative round**, per audience segment. Below it, say
  so in the report's limits. Never present it as a pass or fail. `(house)`
- **One round is a step in a sequence.** A formative round finds problems; it does not measure how
  common they are. Say what the next round should be rather than calling the gap a defect.
  `(house)`

---

## Input

Before analysing, you need:

- **The results**: a CSV or Excel export, or pasted text. Transcripts may be separate files.
- **The tool** the test ran in, to load its profile.
- **What was tested**: the product, flow or prototype, and its fidelity.
- **Moderated or unmoderated**, and whether participants thought aloud.
- **The research questions**, or what the team wanted to learn.
- **The audience**: one group or several, and which participant is in which.

**Called from `usability-test-plan` or `ux-research-brief`**, or given their documents: take the
research questions, assumptions, audience, tasks and success criteria from them and do not ask
again. Confirm in one line: "I'll answer the plan's three research questions and judge success
against its criteria. Right?"

**Standalone**: ask for what is missing, two questions at a time at most. If the user does not
know the methodology, infer it from the data and **mark it *(inferred)* in the report**. Never
present a guess as a fact.

---

## Process

### Step 1, Intake

Ask for what the Input section lists and the user has not given. Load the tool profile. If the
profile is marked provisional, say so: "My notes on Playbook UX are written from its help pages,
not a real export, so your file wins wherever they differ."

### Step 2, Map the data, and confirm it

**Never assume a file's layout.** Open it, read the headers, and propose what each column is:

| Type | Examples |
|---|---|
| Participant | name, email, ID |
| Segment | device, user type, screener answer |
| Rating | SEQ, ease, confidence, SUS item, NPS |
| Task outcome | success, completed, gave up, time on task, clicks, misclicks |
| Open text | follow-up answers, comments |
| Transcript | think-aloud for a task, or a whole session |
| Ignore | timestamps, tool metadata |

Pair each rating with the task it belongs to, and each task with its open text, transcript and
outcome columns. **This pairing is what Step 5 runs on, so show it and get it confirmed.**

With the script: `python3 -I scripts/check.py columns results.csv` lists the columns with a
guessed type. The guesses are a starting point only.

An Excel file: ask the user to export it as CSV, or read it with whatever spreadsheet tool you
have. Say which you did.

### Step 3, Pseudonymise

Replace participant names with P1, P2 and so on, in the order they appear, before writing
anything. Keep the key out of the report.

`python3 -I scripts/check.py pseudonymise results.csv --participant "<column>" --out anon.csv --key key.csv`

It replaces full names inside answers too, and lists first names that may still identify
someone. Show those to the user. Names of colleagues, employers and places inside answers are
not touched, so read for them while coding.

### Step 4, Ratings

For each rating question: the number who answered, the full distribution, the median, and the
mean. **Lead with the distribution.** The mean is there for comparison with a published benchmark,
where one applies, and the library says which ones do.

`python3 -I scripts/check.py ratings anon.csv --participant "<column>" --question 3 --question 5 --scale 1-7`

`--question` takes the exact question text or its number from `columns`. The script prints its
working so it can be checked.

**Without the script**, compute in a table with one row per participant, then the counts, and
show the working. Do not compute a mean in your head.

Never average a scale that was not asked as a scale, and never average success levels (see the
library).

### Step 5, Stated against observed

For every rating, from every participant, find the paired evidence from Step 2: their task
outcome, their think-aloud for that task, their follow-up answer. Classify it:

- **Held**: the evidence is consistent with the rating.
- **Contradicted**: the evidence points the other way. A high ease rating with a backtrack, a
  restart, a wrong end state, "I wasn't sure", "took a while", or a gave-up. A low rating with a
  smooth, fast, unremarked completion is a contradiction too.
- **No paired evidence**: nothing else about that task from that participant.

Record each contradiction with its evidence. **Use the participant's words, not your reading of
their tone.** If the study holds no paired evidence at all, say so: every rating in the report is
then an unchecked claim, and the next plan should pair each rating with an observed measure.

Read `references/analysis.md` for borderline cases.

### Step 6, Task success, where recorded

If the data has task outcomes, report them as levels, not a score: complete, complete with a minor
issue, complete with a major issue, gave up, and **thought they had finished but had not**. Report
the count at each level. Do not convert levels to numbers or average them.

If the tool records only a self-reported "did you complete it?", it is a stated measure and gets
the Step 5 treatment, not this one.

### Step 7, Code the open text

Read every answer and transcript in full. Then, per question:

1. Code each response with short descriptive labels, close to the participant's words.
2. Group codes into themes. **Count participants, not mentions.** One person repeating something
   five times is one participant.
3. Keep the cases against each theme. A theme four people support and two contradict is a split,
   and the report says so.
4. Keep the one-off that matters. One participant meeting a blocking problem is a finding even
   when nobody else did, with its count stated plainly.

Then build findings across questions: a finding is a pattern across tasks and question types, not
a restatement of one column.

### Step 8, Findings and severity

For each finding: a plain statement of the pattern, how many participants it was seen in ("4 of
6"), and 1 to 3 pieces of evidence (a count, an observed behaviour, or a verbatim quote with its
participant ID).

For problems, a severity on Nielsen's 0 to 4 scale, weighing frequency, impact and persistence as
the library describes. Include what worked, with the same evidence standard.

Where research questions were supplied, answer each one and point to the findings behind the
answer. "Not answered by this round" is a valid answer.

**Never write a percentage for fewer than 20 participants.** Write "4 of 6". A summative or
benchmarking round of 20 or more may use percentages, always with an interval, and the report says
which rule it used.

### Step 9, Verify

Before showing anything, check every quote:

1. Write the quotes to a file: `[{"quote": "...", "participant": "P3"}, ...]`
2. `python3 -I scripts/check.py quotes anon.csv --participant "<column>" --quotes quotes.json`

Fix every quote that is not `VERBATIM`: use the participant's exact words, attribute it to the
right participant, or drop it. Cut only with "...". Never tidy grammar or spelling.

**Without the script**, find each quote in the data yourself and confirm it character for
character, then tell the user that the quotes were checked by reading, not by script.

Check every count in the draft against the coding and the ratings output too.

### Step 10, Draft and pause

Fill sections 1 to 4 and 6 of `templates/report.md`, and draft section 5 with two or three
recommendations, each tied to the finding it comes from. Show the whole draft **in the chat**, as
markdown, and end with the template's closing prompt, inviting the designer to change, remove or
add recommendations.

**Stop and wait.** Do not present section 5 as final until the designer has replied.

### Step 11, Finalise

Fold in the designer's changes. Their recommendations are theirs: record them as given and do not
add evidence they did not cite, but say if one is not supported by any finding, once, and leave it
in if they want it.

Then ask what the final report should be: **an HTML file, a Word document, or stay as markdown**.
Produce it from the agreed draft, so the formats cannot disagree.

- **HTML**: fill `templates/report.html`. Self-contained, no external requests.
- **Word**: use the docx skill (in Claude Code, invoke `anthropic-skills:docx`; on claude.ai,
  read `/mnt/skills/public/docx/SKILL.md`; elsewhere, a docx skill if installed, otherwise
  python-docx, and say which). Arial 12pt, A4, 1 inch margins, Heading 1 per section, proper
  bullet lists and tables, quotes as indented paragraphs.

**Filename:** `Usability Test Summary - [Project name].html` or `.docx`.

Hand back the **absolute file path**. Do not start a server.

---

## Rules the skill does not break

1. **No rating on its own.** Every rating sits next to its stated-against-observed result.
2. **No unverified quote.** Every quote is checked word for word and attributed to the right
   participant.
3. **No percentages below 20 participants.** Counts out of the total.
4. **No names.** Participant IDs only. The key stays out of the report.
5. **No fixed number of findings.** The data decides how many.
6. **No silent inference.** Anything not read from the data or confirmed by the user is marked
   *(inferred)*.
7. **No final recommendations without the designer.** Draft, then stop.
8. **Never invent a file layout.** Inspect it or ask.
9. **Flag a provisional tool profile** when you use one.

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose** a new tool profile, a correction to one (the user's export differs from it), a measure,
or a source that contradicts a claim. **Do not propose** a restatement of an existing entry, or a
preference dressed as a finding. A user's own standing practice is `(house)`.

**Format:**

> **New [tool profile / measure / correction] proposed: [Name]**
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
every claim, add a dated line to its change log, and confirm what changed.

**If this skill is running somewhere the files cannot be written** (an uploaded copy on claude.ai
is read-only), say so plainly rather than reporting a save that did not happen, and output the
exact markdown to paste in.

---

## Tone and language

- UK English throughout.
- Plain statements. "4 of 6 participants could not change the address" beats "users struggled".
- No em dashes in anything the user will read, send or publish, including generated files.

---

## Standalone usage

If invoked directly, open with:

> "I'll analyse your usability test and draft the summary. Can you share the results file, and
> tell me which tool you ran it in and what you wanted to learn? If you have the test plan, share
> that too and I'll use its research questions."

Then follow the Process.
