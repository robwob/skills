# Desk research sources and method

The library `desk-research` reads from. How competitors get selected, what each source type can
and cannot establish, how findings get synthesised, and what to write down about the search.

**Last updated:** 7 October 2026

---

## There is no taxonomy here, and this file does not invent one

The research pass behind this file was asked directly whether a citable hierarchy of evidence
exists for secondary research in a design or market context, comparable to the medical evidence
pyramid. **It does not.** Nothing found supports ranking peer-reviewed research above benchmark
studies above review platforms above forums above press. That ordering is convention, and any
version of it this library shipped would be invention wearing a citation.

So this file is a small set of **cited method cards** plus a **mechanism table**: for each source
type, what it can and cannot show, and why. That is defensible. A tier scheme is not.

**Do not add a numeric weighting or a ranked tier list to this file.** If a future session wants
one, it is a `(house)` decision for Rob to make, recorded as such, not a finding.

**Desk research is also not one of Rohrer's 20 methods**, and
`../../ux-research-brief/references/methods.md` says why: that framework classifies methods by
how they engage users, and desk research engages none. So this skill is offered when a brief
needs landscape context, and it is never plotted on the landscape chart.

---

## Provenance

| Tag | Means |
|---|---|
| `(verified)` | Source retrieved and read |
| `(unverified)` | Named source and citation, reached through a secondary summary |
| `(convention)` | Widely repeated practice, no primary source |
| `(derived)` | This library's inference |
| `(house)` | Rob's own standing practice |

---

## House rules

### Desk research produces hypotheses, never findings about your users

The standing corroboration rule says a claim needs a specific check that could disprove it.
Desk research has no access to users at all, so **nothing in it can be corroborated from
inside**. Every output is a question to take into primary research. `(house)`

This is the same position the one genuinely relevant government source takes:

> "There is no way of knowing for certain that the data you're looking at is about your users.
> You will be making a lot of assumptions at this stage."

DfE Digital, *Desk research in discovery*, 20 December 2023. `(verified)`

So a desk research output is written as "the landscape suggests X, which we should test",
never as "users want X". `(house)`

---

## What each source type can and cannot show

The mechanism table. Five questions decide how much weight a source carries, and they replace a
tier scheme: **who produced it, what the sampling bias is, what the conflict of interest is,
whether the method is disclosed, and how old it is.** Those map onto AACODS and CRAAP and the
synthesis is `(derived)`.

| Source type | Can establish | Cannot establish | Why |
|---|---|---|---|
| **Peer-reviewed research** | That an effect held under stated conditions | That it holds for your users or product | Publication bias: Nielsen notes "freak findings" get published while confirming studies stay obscure `(verified)` |
| **Benchmark studies** (Baymard, NN/g) | Patterns across many sites, with a disclosed method | A score for your product, and not a statistical conclusion | Baymard states its goal is "not to arrive at final statistical conclusions" but to find patterns, and its benchmark results are how-to examples rather than definitive scores `(verified)` |
| **Analyst reports** (Gartner, Forrester) | Who the market considers significant | Independent product quality | Conflict of interest is widely alleged and Gartner disputes it. State it as disputed, not as fact `(verified)` on both the allegation existing and Gartner's denial |
| **Review platforms** (G2, Capterra, Trustpilot, app stores) | That a problem exists, and its vocabulary | How common anything is | Two documented biases, acquisition and under-reporting, producing a J-shaped distribution. When everyone in an experiment was made to review, distributions came out roughly normal `(verified)` Hu, Zhang and Pavlou, *CACM*, October 2009. Note it is 2009 Amazon product data; generalising to G2 or app stores is `(derived)` |
| **Community discussion** (Reddit, forums, support boards) | The existence and texture of a frustration | Prevalence, or who the people are | Self-selected and self-organising. No source found; the mechanism is the same as review platforms `(derived)` |
| **Company-published material** | What a company claims and how it positions | Anything about how the product performs | Grey literature. AACODS (Tyndall, Flinders University, 2010) is the appraisal framework built for exactly this `(verified)` |
| **Press coverage** | That something happened, and when | Significance or accuracy of detail | Mostly derived from company material `(derived)` |
| **A competitor's own design** | What they chose, given their constraints | What is good practice | Nielsen: "Usability is highly context-dependent; what's good for one set of users might be terrible for other people" `(verified)` |

**The nearest thing to an evidence principle**, and it is one author's opinion rather than a
validated ranking: Nielsen, *UX Research Evidence*, NN/g, 14 April 2013. `(verified)`

> "Usability findings derived from a broad base of diverse studies have higher credibility than
> those based on many users with a single stimulus."

He names three weaknesses of large-sample single-study evidence: poor methodology, poor
generalisation, publication bias. And recommends diversity across user types, tasks, sites,
countries and methods. **Note what this says: diversity beats sample size.** It is about primary
studies, so applying it to desk sources is `(derived)`.

---

## Competitor selection

The best-sourced part of this library. NN/g, *Competitive Usability Evaluations: Definition*,
5 January 2024. `(verified)`

Definition: "Comparing your product against several competing designs", run either as an expert
**competitive review** or as **competitive testing** with users.

**How many: 2 to 4.** More is "too expensive and too overwhelming". `(verified)`

**Selection criteria**, as NN/g states them: `(verified)`

- similar content or functionality
- best overall UX
- innovative designs
- strongest or most important competitors
- the ones your customers are most likely to compare you against

It adds that smaller, innovative or tangentially related companies can yield insight.

**What to compare:** specific features or content areas, whole-site experiences, design
approaches to a common problem, information architecture, task workflows. `(verified)`

**The anti-checklist line, and it is the point of the whole method:** "You want to beat the
competition, not copy them", and the goal is improving your design rather than declaring
winners. `(verified)`

### Competitor categories

**Direct, indirect, substitute, aspirational is not NN/g's taxonomy.** NN/g uses the criteria
above instead. The four-category split is widely repeated in practitioner content with no primary
source. `(convention)` Use it as convenient vocabulary, not as a framework, and do not attribute
it.

Erika Hall's *Just Enough Research* covers competitive research including direct and indirect
competitors, but the text was not readable, so **do not quote her**. `(unverified)`

### Porter's five forces

Porter, *Harvard Business Review*, 1979, updated 2008. `(unverified)` It is an industry-structure
framework for business strategy. **It does not belong in a UX research brief** unless the brief
is explicitly about market positioning, and no UX source was found that uses it. `(derived)`
Recorded here so it gets declined with a reason rather than included to look thorough.

### Baymard, as a special case

Baymard's own method: 25 rounds of qualitative think-aloud testing across 4,400+ participant and
site sessions, 54 rounds of manual benchmarking of 344 top-grossing ecommerce sites against 810
guidelines, 34,000+ usability issues consolidated, each guideline carrying severity and
frequency ratings. `(verified)`

**That is primary research with expert scoring, not desk research.** Using its output is
legitimate secondary use of someone else's primary study, and the brief should say so rather than
citing it as though the team had established it. `(derived)`

---

## Synthesis

### Organise by theme, not by competitor

A per-competitor summary is a feature checklist. The synthesis has to say what the pattern is,
which sources it is drawn from, and what it implies. `(convention)` This is already the
instruction in `SKILL.md` and it has no primary source.

### Thematic analysis, if you name it, do it

Braun and Clarke 2006, "Using thematic analysis in psychology", *Qualitative Research in
Psychology* 3(2), pp. 77-101. `(verified)` citation. They describe thematic analysis as "a poorly
demarcated, rarely acknowledged, yet widely used" method, give step-by-step guidance, and tie it
to no single theoretical position. Their 2019 work renames their approach **reflexive thematic
analysis** and distinguishes it from codebook and coding-reliability approaches. `(unverified)`

**Applicability to desk research is qualified, and the qualification matters.** Documents are
within the method's stated scope. `(unverified)` But reflexive TA assumes the researcher
understands how the data was generated, and desk-sourced text has unknown authors and unknown
sampling. So themes describe **the sampled text**, not users. `(derived)`

**Do not claim "a Braun and Clarke thematic analysis" unless the six phases were actually
followed**: familiarisation, coding, generating themes, reviewing, defining, writing up. Say
"adapted from" otherwise. Their later writing is explicit about misuse of the label.
`(unverified)`

### Triangulation, in NN/g's sense

Whitenton, NN/g, 21 February 2021. `(verified)` "Using multiple sources of data or multiple
approaches to analyzing data, to enhance the credibility of a research study." It **mitigates
rather than eliminates** limitations, and higher-stakes decisions warrant more of it.

The article is about combining UX methods, so applying it to combining desk sources is
`(derived)`. Keep it distinct from the house corroboration rule, which operates inside a single
session against a single claim.

### Affinity mapping

No citable primary source found. `(convention)`

### Confirmation bias in source selection

The guard with any real backing is the systematic-review one: **predefined inclusion and
exclusion criteria, written before searching.** `(derived)` from the standards below. "Seek
disconfirming sources" is widely repeated with no UX source. `(convention)`

Lateral reading has actual evidence behind it, though not for this use case. Wineburg and
McGrew, Stanford, 2017: 45 participants, 10 historians, 10 professional fact-checkers, 25
undergraduates. Fact-checkers read laterally, leaving the source to check it against others, and
judged legitimacy accurately. Historians and students often did not. One reported result: all
fact-checkers identified the American Academy of Pediatrics as the legitimate organisation,
against 50% of historians and 20% of students. `(unverified)`, reached via Stanford's coverage
rather than the paper. It tests political and health misinformation, not vendor or review
content, so applying it here is `(derived)`.

---

## Documenting the search

### Borrow the discipline, not the label

**PRISMA 2020 is a reporting guideline, not a method for conducting a review.** `(verified)`
Its relevant items: specify inclusion and exclusion criteria, and present full search strategies
including filters and limits. PRISMA-S extends it to search reporting.

**What to write down**, borrowed without overclaiming: `(derived)`

- the question
- the sources searched
- the exact search strings
- the dates searched
- the inclusion and exclusion rules, written before searching
- what was excluded, and why

**Call the result a structured desk search, never a systematic review.** A systematic review
needs multiple independent screeners, a registered protocol and risk-of-bias appraisal. Desk
research has none of those. `(derived)`

### The closest real precedent

Garousi, Felderer and Mäntylä, "Guidelines for including grey literature and conducting
multivocal literature reviews in software engineering", *Information and Software Technology*
106, 2019, pp. 101-121. `(verified)` citation, content not read in detail.

It covers search, source selection, quality assessment, data extraction and synthesis for blogs,
white papers and videos **alongside** peer-reviewed work. This is the best citable precedent for
mixing source types in a software-adjacent field. Fetch it before citing any specifics.

---

## Source-evaluation checklists, and what they are worth

Included because they come up, with their actual status attached.

**CRAAP** (Currency, Relevance, Authority, Accuracy, Purpose). Sarah Blakeslee and librarians at
Meriam Library, CSU Chico, 2004, designed for first-year students. `(unverified)` Documented
criticisms: it gets applied as a checklist; it evaluates a source from inside the source rather
than reading laterally; it is vulnerable to confirmation bias; it was not built for scholarly
problems like predatory venues or retractions. `(unverified)`

**SIFT** (Stop, Investigate the source, Find better coverage, Trace claims to the original).
Mike Caulfield, 19 June 2019, taught from about 2017. `(verified)` It is a teaching heuristic
for students and general web users and **makes no empirical validation claim**. The evidence is
for lateral reading, not for SIFT as a package.

**AACODS** (Authority, Accuracy, Coverage, Objectivity, Date, Significance). Jess Tyndall,
Flinders University, 2010, built specifically for appraising **grey literature**. `(verified)`
This is the closest fit to the material desk research actually handles: company blogs, white
papers, vendor pages.

**No evidence was found that any of the three is used in UX or market research practice.**
They appear in library guides and classrooms. `(derived)` Use AACODS's six dimensions as prompts
if a source needs appraising, and do not present any of them as industry method.

---

## Where this library is weakest

Stated plainly so it is not mistaken for solid ground.

1. **No evidence hierarchy exists**, and the negative finding is moderately confident rather
   than certain. The pass ran about a dozen web queries; an academic database search for "grey
   literature appraisal UX" or "competitor analysis method HCI" might turn something up.
2. **Nothing on Forrester's independence** was checked at all.
3. **The review-platform bias evidence is 2009 Amazon data.** Its application to G2, Capterra,
   Trustpilot and app stores is an assumption.
4. **Not read in primary form:** Erika Hall's book, the GOV.UK Service Manual's own pages,
   Braun and Clarke in full, the PRISMA statement, Wineburg's paper, NN/g's competitive testing
   and benchmarking articles.

---

## Change log

**7 October 2026.** File created. Built as cited method cards plus a mechanism table rather than
a source hierarchy, because the research pass established that no citable hierarchy exists for
this material. Competitor selection is the best-sourced section; the rest rests on a handful of
cited pieces and a good deal of flagged convention. A standing instruction not to add a tier
scheme is recorded at the top.
