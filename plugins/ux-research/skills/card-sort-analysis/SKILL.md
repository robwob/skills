---
name: card-sort-analysis
description: >
  Use this skill to analyse the results of a card sort and report what they support. Triggers
  include: 'analyse my card sort', 'card sort results', 'card sorting analysis', 'what do these
  card sort results mean', 'similarity matrix', 'dendrogram', 'open card sort', 'closed card
  sort', 'hybrid card sort', 'standardise categories', or results exported from Playbook UX,
  UXtweak, Optimal Workshop (OptimalSort), Maze, Lyssna, UserZoom, UserTesting or Useberry.
  Adapts to the tool the results came from. Works from an export, from screenshots of the tool's
  own matrix and dendrogram, or from both, and returns a two-layer HTML report with the
  confidence in each finding stated. Does not plan or run the card sort itself, which belongs to
  ux-research-brief. Always use this skill when someone has card sort results and wants to know
  what they show, what to propose, and how far to trust it.
---

# Card Sort Analysis Skill

## Purpose

Take the results of a card sort, analyse them, and report what they support, what they do not,
and how confident to be in each point. It adapts to the tool the study was run in, because tools
export different things and show different views.

**A card sort gives ideas for groupings and labels. It does not give a validated structure.** The
report proposes a draft, says how firm each part of it is, and names tree testing as the next
round. It never presents a structure as settled.

It also teaches. Every evidence view in the report points to the section of
`guide/how-to-analyse-card-sort-results.md` that shows how to do the same step by hand, so the user
can check the work and learn the method.

---

## The library

**The `references/` folder holds what the skill works from. Read the file for the step you are on
before doing it. Do not work from memory.**

| File | Read it when |
|---|---|
| `references/intake.md` | Starting. The questions, in order. |
| `references/input-format.md` | Getting results into the shape the script reads. |
| `references/tools/<tool>.md` | After the user names a tool. `_generic.md` if it is not listed. |
| `references/analysis/cleaning.md` | Checking participants and deciding exclusions. |
| `references/analysis/standardising-categories.md` | Merging category names (open and hybrid). |
| `references/analysis/matrix-and-clustering.md` | Reading or computing a similarity matrix or dendrogram. |
| `references/analysis/closed-sorts.md` | The categories were supplied by the researcher. |
| `references/analysis/contested-cards.md` | Cards the data does not settle. |
| `references/analysis/sample-size.md` | Saying what the number of participants supports. |
| `references/image-route.md` | The matrix or dendrogram exists only as a screenshot. |
| `references/reporting.md` | Writing the findings and building the report. |

Know four things about the library before you start:

- **The evidence base is thin and mostly written by tool vendors.** Independent work exists for
  sample size and for reliability, but almost nothing validates the thresholds people use (50%,
  60%, 70%, 80% agreement). The library says which is which. **Never present a vendor threshold as
  evidence.**
- **Tool profiles are dated and some are provisional.** Tools change their exports. Each profile
  carries the date it was checked and what could not be read. Playbook UX, UserTesting and
  Useberry are the weakest. Trust the user's actual file over a profile.
- **No tool documents how its matrix or dendrogram is calculated in full.** So a dendrogram read
  from a screenshot is an approximation of a tool's own method, not a reproduction of it.
- **Several things are settled by nobody**: how unsorted cards should count, where to cut a
  dendrogram, and which linkage is best. The skill makes them explicit settings and states them in
  every report.

Claims carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`, `(house)`.

---

## House rules

- **Participant numbers.** A minimum of 6 is the house floor for qualitative rounds such as
  interviews and usability tests. **It does not carry over to card sorting.** Card sort sources put
  the figures at 15 or more, and the matrix, dendrogram and single-card precision each need a
  different number. Report the number of participants and the stability of the groups, and say
  which question that number can answer. Never write a pass or fail line for sample size.
  `(house)`
- **Check a stated claim with a question that could disprove it.** A card sort is people stating
  how they would group things, so its output is a set of stated judgements. The check that could
  contradict them is a tree test or a moderated follow-up, and the report names it as the next
  round. `(house)`
- **One round is a step in a sequence, not a gap.** A card sort establishes how people group
  content. Whether they can find it is a later round. Write that as a sequence, not as a
  deficiency. `(house)`

---

## Input

You need the following before analysing. If invoked standalone, ask for anything missing, using
`references/intake.md`:

- **The tool** the card sort was run in
- **The sort type**: open, closed or hybrid
- **The results**: an export, screenshots of the tool's views, or both
- **The number of participants and cards**
- **The decision the results feed**, so the report answers it rather than describing everything

---

## Process

### Step 1, Intake

Use `references/intake.md`. Ask the questions in order and stop asking once you have what the next
step needs. If the user gave details in their first message, do not ask again.

### Step 2, Pick the route

Read the tool's profile in `references/tools/`, then choose:

| The user can supply | Route |
|---|---|
| An export with one row per card placement, or one that converts to it | **Data**: computed by the script |
| Screenshots of the matrix and dendrogram only | **Image**: transcribed, confirmed by the user, marked lower confidence |
| An export that covers only part of what the tool shows | **Combined**: compute what the data supports, read the rest from screenshots, and cross-check where they overlap |

**If the export lets the similarity matrix be recomputed, compute it and compare it to the
screenshot.** Report any disagreement. If it does not, the screenshot is the only source for the
matrix and the dendrogram, and every finding that rests on it is marked lower confidence.

Tell the user which route you are taking and why, in one or two sentences.

### Step 3, Get the data into shape

Use `references/input-format.md`. **Never assume a file's layout.** Open the file, read the headers,
propose a column mapping, and get the user to confirm it before computing anything. If you cannot
tell what a column means, ask.

### Step 4, Check the data, and let the user decide

Use `references/analysis/cleaning.md`. Run the script's data checks and show the flags. **Flag,
never drop.** A participant who looks odd may simply sort differently. The user decides who to
exclude, and the exclusions appear in the report.

### Step 5, Standardise category names (open and hybrid)

Use `references/analysis/standardising-categories.md`. List the names people typed, propose merges
**by what is inside the categories, not by the names**, show the user each one, and apply only the
ones they approve. Standardising changes the cards and categories views. **It never changes the
similarity matrix**, which uses each participant's own groups. Merging that redefines groups is a
later optional step for the user to choose, after they have read what participants did.

### Step 6, Analyse

**Data route.** Run the script from the skill directory:

```
python3 -I scripts/analyse.py results.csv --out analysis/ [options]
```

`--sort-type closed` for a closed sort, `--merge-file` for approved merges, `--exclude` for approved
exclusions, `--unsorted singleton|pairwise` for how unsorted cards count, `--cut` for the dendrogram
cut. Run it with `-I` and pass the user's file as an argument. The script needs Python 3.9 or later
with numpy and scipy, and prints an install message if they are missing. `scripts/README.md` lists
every option.

**Image route.** Follow `references/image-route.md`. Read each screenshot, transcribe it into a
table, show the table back, and get the user to confirm it before using it. **Never convert shading
to exact percentages**: where a tool prints values only on hover, record shading bands and mark
them approximate.

**Combined route.** Do both, and cross-check.

Then read the analysis reference for each view before interpreting it. In particular
`references/analysis/matrix-and-clustering.md` for what a dendrogram can and cannot be read as.

### Step 7, Interpret

- Read the **cards** and **categories** views first, then the **matrix** and **dendrogram**.
- State the settings that change the answer: how unsorted cards were counted, the linkage, the cut,
  and how much the groups move at neighbouring cuts.
- **Look at the cards no single group settles.** They are often the most useful finding. The data
  cannot say whether a card is contested because the label is unclear, because it fits several
  areas, or because different users see it differently, so name the follow-up that would.
- Say what the number of participants supports, from `references/analysis/sample-size.md`.

### Step 8, Write and render the report

Use `references/reporting.md`. Write the findings file, then build the report:

```
python3 -I scripts/render_report.py --findings findings.json --results analysis/results.json --out report.html
```

Leave `--results` out on the image route. Every finding, recommendation and part of the proposed
structure carries a confidence (High, Medium or Low) and a basis (computed, read from a screenshot
and confirmed, or judgement).

### Step 9, Hand it back

Give the user **the absolute path to the report file** and to the folder of CSV tables. Do not
start a server. Say in a few sentences what the study supports, what it does not, and what the next
round is. Offer the guide for any view they want to check by hand.

---

## Rules the skill does not break

1. **No claim of a validated structure.** A card sort proposes. A tree test checks.
2. **Never read a dendrogram height as a percentage unless the tool's legend says so.** Ask.
   Different tools put different meanings on the same axis, and some document none.
3. **Never invent a file layout.** Inspect it or ask.
4. **Never convert shading to a precise figure.** Record a band and say it is approximate.
5. **Confirm every transcription with the user before using it**, and mark findings that rest on
   a screenshot as lower confidence.
6. **Never drop a participant without the user's decision**, and list exclusions in the report.
7. **State the settings in every report.** Unsorted handling, linkage, cut, and how far the groups
   move.
8. **Present vendor thresholds as conventions,** and say they are not evidence.
9. **Flag a provisional or unverified tool profile** to the user when you use it.
10. **Hand back a file path.** Never a served link.

---

## Source handling

- Paraphrase findings. Do not reproduce substantial text from tool documentation.
- If sources conflict, say so rather than picking one. The library records several conflicts, for
  example whether Optimal Workshop's similarity matrix shows counts or percentages.
- If you do web research to check a tool's current export, run it through the
  `web-search-researcher` subagent where it is available, and tag anything you could not read
  directly as unverified. Fetch tools often summarise a page, so **do not present a summary as a
  quotation**.

---

## Tone and language

- UK English throughout
- No em dashes in anything the user will read, send or publish, including generated files

---

## Output

An HTML report, self-contained, with no external requests. Layer 1 is for the people who decide:
the summary, a proposed structure labelled a draft, findings, contested cards, recommendations with
confidence and basis, what the study cannot tell you, and the next step. Layer 2 is the evidence:
settings, per-card agreement, the matrix as a table of numbers, the dendrogram with a text version,
stability, and participants. Any screenshots are embedded.

Alongside it, a folder of CSV tables the user can re-analyse.

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose a new entry when** a tool changes its export, a tool is missing, or a source contradicts
a claim in the library.

**Format:**

> **New [tool profile / rule / correction] proposed: [Name]**
>
> **What it is:** one sentence.
>
> **Source:** a named source and whether it was read directly or through a summary.
>
> **Evidence in this session:** what prompted it, for example the user's export differing from the
> profile.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit the file in place, match the surrounding format, tag every
claim, add a dated line to the file's change log, and confirm what changed.

**If this skill is running somewhere the files cannot be written** (an uploaded copy on claude.ai is
read-only), say so plainly rather than reporting a save that did not happen, and output the exact
markdown to paste in.

---

## Standalone usage

If invoked directly, open with:

> "I'll help you analyse your card sort. Which tool did you run it in, was it an open, closed or
> hybrid sort, and what can you share: an export, screenshots of the matrix and dendrogram, or
> both?"

Then follow `references/intake.md`.
