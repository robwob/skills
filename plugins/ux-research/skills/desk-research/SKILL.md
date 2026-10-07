---
name: desk-research
description: >
  Use this skill to conduct desk research or competitor analysis for UX research projects.
  Triggers include: 'desk research', 'competitor analysis', 'competitive research', 'landscape
  review', 'what are competitors doing', 'secondary research', 'benchmark', or when the
  ux-research-brief orchestrator offers it as an adjunct. Works standalone or as part of the full
  brief flow. Selects two to four competitors, searches against written inclusion rules, weighs
  each source by what that type of source can and cannot show, and returns hypotheses to test, not
  findings about users. Always use this skill when someone needs web-based research synthesised
  into a structured summary for a UX or product research project.
---

# Desk Research Skill

## Purpose

Conduct web-based secondary research and competitor analysis, then synthesise the findings into a
structured Word document. Works standalone or when offered by the `ux-research-brief` skill.

**Its output is hypotheses, never findings about users.** Desk research has no access to users at
all, so nothing in it can be checked from inside. Every conclusion is a question to take into
primary research.

Desk research is not one of the 20 methods in the brief skill's library, because that framework
classifies methods by how they engage users and this one engages none. It is offered as an
adjunct, and it is never plotted on the method landscape.

---

## The library

**`references/sources.md` holds competitor selection, a table of what each source type can and
cannot show, synthesis guidance and how to document a search, each tagged for how well it is
sourced. Read it before researching.**

Do not work from memory. Know three things about it first:

- **There is no taxonomy and no evidence hierarchy.** The research behind the file asked directly
  whether a citable hierarchy exists for secondary research, comparable to the medical evidence
  pyramid, and found none. Nothing supports a ranked order of peer-reviewed work, benchmarks,
  reviews, forums and press.
- **So do not rank sources and do not score them.** The file holds a table of what each source
  type can and cannot show, and why. Use it. Never add a tier list or numeric weighting. If the
  user wants one, that is their decision, recorded as `(house)`, not a finding.
- **Competitor selection is the best-sourced part.** Everything else rests on a handful of cited
  pieces and flagged convention. The file lists where it is weakest.

Its claims carry tags: `(verified)`, `(unverified)`, `(convention)`, `(derived)`, `(house)`.

---

## House rules

- **Hypotheses, not findings.** Write "the landscape suggests X, which we should test", never
  "users want X".
- **Corroboration needs primary research.** The standing rule that a claim needs a specific check
  that could disprove it cannot be met inside desk research. Say so in the output and name the
  primary method that would test each hypothesis.

---

## Input

You need the following before researching. If invoked standalone, ask for anything missing:

- **Research questions or focus area**: what the desk research needs to address
- **Product or service context**: what space you are operating in
- **Specific competitors to include** (optional), or ask whether you should identify them
- **Scope**: for example "focus on onboarding flows" or "broad landscape overview"

If called from the `ux-research-brief` orchestrator, the context is passed in. Use it directly.

---

## Process

### Step 1, Write the rules before searching

Confirming a hypothesis you already hold is the main risk in desk research, and the only guard with
real backing is to **fix the inclusion and exclusion rules before you look**. Write down:

- the question
- the source types you will search, from the table in the library
- the inclusion and exclusion criteria
- the competitors, and why each was chosen

**Choose two to four competitors.** More is, in NN/g's words, "too expensive and too overwhelming".
Select against the library's criteria: similar content or functionality, best overall UX,
innovative designs, the strongest or most important competitors, and the ones customers are most
likely to compare you with. A smaller or tangentially related company can yield insight.

Tell the user what you plan to search and confirm they are happy to proceed.

### Step 2, Conduct the searches

Run multiple targeted searches. Do not rely on one query. For each area, search for the product or
feature in context, user reviews and feedback, industry articles and teardowns, and relevant news.

**Search tooling.** In Claude Code, run web research through the `web-search-researcher` subagent
where it is available. Elsewhere use the web search tools you have. Be aware that fetch tools often
summarise a page through a smaller model and may refuse verbatim reproduction, so **do not present
a summary as a quotation**. Tag anything you could not read directly as unverified.

**Log every search**: the exact string, the source, the date, and what you excluded and why. The
log goes in the appendix. Call the result a **structured desk search**, never a systematic review,
because a systematic review needs independent screeners, a registered protocol and risk-of-bias
appraisal, and desk research has none of those.

### Step 3, Weigh each source by what it can show

For every source, use the library's table. Ask five questions, which replace a tier list: who
produced it, what is the sampling bias, what is the conflict of interest, is the method disclosed,
and how old is it.

The shorthand worth carrying:

- **Review platforms** show that a problem exists and the vocabulary, never how common it is. They
  are self-selected samples.
- **Community discussion** shows a frustration's existence and texture, not prevalence.
- **Analyst reports** show who the market considers significant. The conflict-of-interest concern
  is widely raised and disputed by the vendor, so state it as disputed.
- **Company material** shows what a company claims.
- **A competitor's design** shows what they chose given their constraints, not what is good
  practice.
- **Benchmark studies** such as Baymard's are someone else's primary research. Using them is fine,
  but say so and do not present the result as one the team established.

### Step 4, Synthesise

Do not summarise each source. Synthesise **across** sources, organised **by theme, not by
competitor**, since a per-competitor summary is a feature checklist. Identify:

- **Patterns**: what do most competitors do similarly
- **Differentiators**: where approaches diverge, and why
- **Gaps**: what no one seems to be doing well
- **Implications**: what this means for the research or design, stated as hypotheses

NN/g's own line on the purpose is that you want to beat the competition, not copy them.

**If you name a method, do it.** Do not describe the synthesis as a Braun and Clarke thematic
analysis unless you followed its six phases. Say "adapted from" otherwise. And note that themes
drawn from desk-sourced text describe the sampled text, not users, because the authors and the
sampling are unknown.

---

## Document structure

### 1. Overview
- What was researched and why
- Scope and limitations: **based on publicly visible information only, which is what is visible
  and not necessarily what is true**

### 2. Landscape summary
- Who the key players are and how the space is broadly structured
- One or two paragraphs, not a list of names

### 3. Key findings
Organised by theme. Each theme includes what the pattern is, which sources it is drawn from and
what type of source each is, and what it implies for the research. Aim for three to six themes.

### 4. Competitor snapshots (if applicable)
A brief profile per competitor, two to four sentences each: what they do, their notable UX
approach relevant to the focus, and any standout strengths or weaknesses from user feedback,
noting that feedback is self-selected.

### 5. Hypotheses to test
Two to four bullet points: what the findings suggest, and **which primary method would test each**.
For example "Hypothesis: competitors lead with price, and users compare on it. Test with
interviews, using a critical-incident question about the last purchase."

### 6. Appendix: search log
The rules written in Step 1, and every search with its string, source, date and exclusions.

---

## Source handling

- Paraphrase findings. Do not reproduce substantial text from sources.
- Note where each finding comes from, by publication or platform, without formal citation format.
- If sources conflict, note the conflict rather than picking one.
- Be honest about limitations. Desk research reflects what is publicly visible.

---

## Tone and language

- UK English throughout
- No em dashes in anything the user will read, send or publish

---

## Output

Produce the findings as a Word document. Use the docx skill (in Claude Code, invoke
`anthropic-skills:docx`; on claude.ai, read `/mnt/skills/public/docx/SKILL.md`) before writing any
document code.

**Filename:** `Desk Research Summary - [Project Name].docx`

**Formatting:**
- Font: Arial, 12pt
- Page size: A4, 1 inch margins
- Section headers as Heading 1
- Theme headers as Heading 2
- UK English throughout

---

## Proposing an addition

The library is a first pass and every change is approved first. **Nothing is written without the
user's explicit approval.** Propose, then stop and wait.

**Propose a new entry when** a source type, appraisal method or search practice comes up that the
library lacks and a named source supports it. **Never propose a ranking or a weighting.** If the
user wants one, it is `(house)`, recorded as their decision.

**Format:**

> **New [source type / method / rule] proposed: [Name]**
>
> **What it is:** one sentence.
>
> **Why it isn't [closest existing entry]:** one sentence.
>
> **Source:** a named source, or "none, this would be `(house)` or `(convention)`".
>
> **Evidence in this research:** what prompted it.
>
> Add this to the library?

**Wait for the answer.**

### Adding an approved entry

Only after explicit approval. Edit `references/sources.md` in place, matching the surrounding
format, tag every claim, add a line to the change log, and confirm what changed.

**If this skill is running somewhere the file cannot be written** (an uploaded copy on claude.ai is
read-only), say so plainly rather than reporting a save that did not happen. Output the exact
markdown to paste into `references/sources.md`, and note the skill needs repackaging:

```
cd <the desk-research directory>
zip -qr ../desk-research.skill SKILL.md README.md references/
```

---

## Standalone usage

If invoked directly, open with:

> "I'll conduct some desk research for you. Can you tell me what product or service space you're
> working in, what you're trying to understand, and whether there are any specific competitors you'd
> like me to focus on?"

Then confirm the scope and the rules for what to include before searching.
