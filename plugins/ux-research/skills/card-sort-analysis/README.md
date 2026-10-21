# card-sort-analysis

Analyses the results of a card sort and reports what they support. Adapts to the tool the study was
run in, works from an export, from screenshots of the tool's own matrix and dendrogram, or from
both, and returns a two-layer HTML report with the confidence in each finding stated. It proposes a
draft structure and says plainly that a card sort gives ideas, not a validated structure.

It also teaches. A guide shows how to do each analysis by hand, view by view, and the report points
to the relevant section next to each piece of evidence.

Part of the research family, with `ux-research-brief`, `discussion-guide`, `usability-test-plan`,
`survey-questions` and `desk-research`. It analyses results, so it does not plan or run the card
sort. Each skill works on its own.

## Install

**Claude Code / local.** Put this directory anywhere and symlink it into your skills folder:

```
ln -s /path/to/card-sort-analysis ~/.claude/skills/card-sort-analysis
```

Skills are picked up when a session starts, so start a new session afterwards. **A broken symlink
fails silently**: the skill just does not appear, with no error. Confirm it loaded:

```
[ -e ~/.claude/skills/card-sort-analysis/SKILL.md ] && echo OK || echo BROKEN
```

**The data route needs Python 3.9 or later with numpy and scipy:**

```
python3 -m pip install numpy scipy
```

The report builder, the converter and the image route use only the standard library. Without Python
the skill can still read screenshots, but the matrix, dendrogram and stability figures cannot be
computed, and the guide shows how to do the small cases by hand.

**claude.ai.** Upload `card-sort-analysis.skill`. Uploaded copies are read-only, so the skill cannot
save an approved addition to its library, and it may not be able to run the scripts. It will say so.

## Use

> "Here's my card sort export from UXtweak. What does it show?"

> "I ran an open card sort in Playbook UX and only have screenshots of the similarity matrix and the
> dendrogram."

It asks which tool, which kind of sort, and what you can share. It checks the participants and shows
you what looks odd, and you decide who to exclude. It proposes category merges for you to approve,
runs the analysis, and writes the report.

To learn the method behind a view, open
[`guide/how-to-analyse-card-sort-results.md`](guide/how-to-analyse-card-sort-results.md). It has a
six-part section for each view, a worked example small enough to do on paper, spreadsheet formulas,
and exercises with answers.

## How solid the library is

**The evidence base for card sort analysis is thin, and most of it is written by the tools'
vendors.** Independent work exists for sample size and for how reliable a card sort is across
studies. Almost nothing validates the thresholds people use (50%, 60%, 70%, 80% agreement), where to
cut a dendrogram, or which linkage is best. The library says which is which, and the skill states
the settings that change the answer in every report.

**Tool profiles are written from documentation, not from real exports, apart from UXtweak's
documented columns.** Each carries the date it was checked. Playbook UX is provisional. UserTesting,
UserZoom and Useberry are unverified, because their help pages could not be read. **Trust your own
file over a profile.**

**No tool fully documents how its matrix or dendrogram is calculated.** Optimal Workshop and UXtweak
use methods that report agreement rather than distance, and one of them cannot be reproduced from
what is published. A dendrogram computed here uses average linkage and may differ from your tool's.

Every claim in the library is tagged with how well it is sourced:

```
(verified)    retrieved and read
(unverified)  a named source, reached through a secondary summary, or an inference not yet tested
(convention)  widely repeated practice, no primary source
(derived)     the library's own inference
(house)       the author's standing practice, not citable and not overridden by a source
```

Two house rules apply across the family: a minimum of 6 participants for any qualitative round, and
every stated preference is checked inside the session by a specific question that could disprove it.
**The first does not apply to card sorting,** where sources put the figure at 15 or more, and this
skill says so.

## What is in here

```
SKILL.md                         the process
README.md                        this file
guide/                           how to analyse the results yourself, view by view
references/
  intake.md                      the questions asked, in order
  input-format.md                the data shape, and how to map an export to it
  image-route.md                 reading a matrix or dendrogram from a screenshot
  reporting.md                   the report structure and the findings file
  analysis/                      cleaning, standardising, matrix and clustering,
                                 closed sorts, contested cards, sample size
  tools/                         one profile per tool, plus a generic one
scripts/
  analyse.py                     computes the views from per-placement data
  render_report.py               builds the two-layer HTML report
  to_long.py                     converts a wide grid to one row per placement
templates/report.html            the report's page template
examples/                        synthetic datasets, merge files and a sample findings file
tests/                           62 tests, run with python3 -m unittest discover tests
```

The library lives in its own files so it can be amended without touching the process. It is a first
pass and expected to change. When the skill meets something the library lacks, for example a tool
whose export differs from its profile, it proposes an addition and waits: nothing is written without
your approval.

After editing anything here, rebuild the zip:

```
cd card-sort-analysis && zip -qr ../card-sort-analysis.skill SKILL.md README.md guide references scripts templates examples tests
```

All the example data is synthetic.
