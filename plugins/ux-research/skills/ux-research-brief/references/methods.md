# UX research methods library

The library `ux-research-brief` reads from. 20 methods, each placed on three dimensions and
assigned to a product-development phase, with what it answers, what it cannot answer, what it
needs, and which skill executes it.

**Last updated:** 7 October 2026

**Source:** "A Guide to Using User-Experience Research Methods", content by Christian Rohrer,
Nielsen Norman Group. Article published 17 July 2022, last reviewed 15 July 2026.
https://www.nngroup.com/articles/which-ux-research-methods/
Poster design by Kelley Gordon, extracted from
https://s3.amazonaws.com/media.nngroup.com/media/articles/attachments/User_Research_Methods_A4-compressed.pdf

---

## How this is structured

    Phase  ->  Question  ->  Dimensions  ->  Method  ->  Protocol

- **Phase** is where the project sits in product development. Three of them, and it decides
  whether the research is generative, formative or summative.
- **Question** is a single research question. A project has several and they rarely sit in the
  same place, so each one is placed separately.
- **Dimension** is an axis a question and a method both sit on. Three of them, below. Each is a
  spectrum, and **neither end is correct by default**: qualitative is not better than
  quantitative, it answers a different question.
- **Method** is one of the 20. Selected from this file, never invented.
- **Protocol** is this project's instance of a method, and it is produced by the specialist
  skills at run time rather than stored here.

Four rules govern the structure:

1. **A method may sit mid-axis.** The source puts usability studies and field studies in the
   middle of the attitudinal/behavioural axis on purpose, because they "utilize a mixture of
   self-reported and behavioral data". A question may sit mid-axis too. Forcing a side is the
   most likely way to get a recommendation wrong.
2. **A question may be in more than one phase.** Projects are commonly in two at once.
3. **Both poles are real positions.** The `Cannot tell you` field exists to state the cost of a
   method's position, and it must be surfaced whenever that method is being recommended. A
   library of 20 methods with no stated limits collapses into recommending the familiar three.
4. **Every layer is expected to change, and every change is approved first.** Methods, placements
   and limits are all amendable. The skill may propose an addition, but it stops and waits:
   nothing is written into this file until the user has approved it.

This is a preset list to select from, not a checklist to complete. A project will run two to four
of these, not twenty.

---

## Provenance

Every claim below carries a tag, because the fields are not equally well sourced and the
difference is invisible otherwise.

| Tag | Means |
|---|---|
| `(NN/g, verbatim)` | Quoted from the poster or article |
| `(NN/g, stated)` | The source states this, paraphrased |
| `(derived)` | Reasoned from the method's axis placement or definition. Not a published claim. |
| `(convention)` | Widely repeated practitioner practice with no primary source |
| `(unverified)` | A named source and citation, but reached through a secondary summary rather than read |
| `(house)` | Rob's own standing practice. Not citable, and not to be overwritten by a source that disagrees. |

`(house)` outranks the others in practice. Where a source and a house rule conflict, the
library states both and follows the house rule, because the house rule is a decision and the
source is an input to it.

**The `Cannot tell you` field is almost entirely `derived`.** The source classifies methods but
does not publish per-method limits. The reasoning is sound and follows from the axes, but it is
this library's inference and not NN/g's claim. When a `derived` line is the reason a method is
being ruled out, the skill must say so rather than presenting it as a finding.

**Exact chart coordinates could not be extracted.** The article's chart is a raster image. The
poster is vector and gave up its labels, its axis definitions and its context-of-use key, but not
per-method positions. Six methods are placed explicitly on the poster's "Dimensions Explained"
diagrams and are tagged `(NN/g, stated)`. The rest are placed from the method definition and are
tagged `(derived)`. If someone later reads positions off the chart image, those tags should be
promoted.

---

## House rules

These are decisions, not inputs, and they apply across every method below. Where a source
disagrees, the library states both and follows the rule.

### Corroborate every stated preference inside the session

Anywhere a method asks someone what they think of something, the instrument must also ask the
specific question that would prove or disprove it. A claim the follow-up does not support is not
a finding, and **the contradiction is the result** rather than a sign the participant was
confused. `(house)`

This is not NN/g's triangulation, which means combining several methods across a study
(Whitenton, NN/g, 21 February 2021) and is handled separately by the triangulation check in
`SKILL.md`. This rule runs inside one session, against one claim. Keep the two names apart.

What it looks like per method:

| Method | The claim | What checks it |
|---|---|---|
| Interviews | "I like X" | A critical-incident question about the specific last occasion |
| Usability Testing, Remote Moderated, Unmoderated | "That was easy" | The observed record: time, backtracks, task success |
| Desirability Studies | The chosen attribute | What in the design they can point to that produced it |
| Concept Testing | Stated enthusiasm | The specific current behaviour the concept would displace |
| Surveys | A stated preference at scale | A behavioural measure, which means a second method |
| Focus Groups | A group position | Individually, before the discussion, or not at all |

The sources support the need without naming the fix. Sauro's finding that SUS shares only about
6% of its variance with task performance is the quantitative version: the stated measure barely
tracks the observed one. `(unverified)` Hall on participants wanting to be liked, and NN/g on
what people do differing from what they think they do, are the qualitative version. `(verified)`

**Customer Feedback and Analytics are exempt**, for opposite reasons. Customer feedback is all
claim and has nothing to check it against inside the method, which is why it produces leads
rather than findings. Analytics is all observation and carries no claim. `(derived)`

### Minimum 6 participants

Per audience segment, for any qualitative round. `(house)` The contested five-user rule and the
numbers behind it are in `usability-test-plan/references/task-design.md`.

---

## The three dimensions

### 1. Attitudinal <-> Behavioral

> "This distinction can be summed up by contrasting 'what people say' versus 'what people do'
> (very often the two are quite different)." `(NN/g, verbatim)`

> "Between these two extremes lie the two most popular methods we use: usability studies and
> field studies. They utilize a mixture of self-reported and behavioral data." `(NN/g, verbatim)`

Explicitly placed by the poster: card sorting and surveys toward attitudinal; usability studies
and field studies in the middle; A/B testing and eyetracking toward behavioral.

**To place a question on this axis:** is it about what someone believes, prefers, remembers or
would say, or about what they actually did?

### 2. Qualitative <-> Quantitative

The poster labels the poles Qualitative **(Direct)** and Quantitative **(Indirect)**. The split
is the collection mechanism, not the sample size.

> "Studies that are qualitative in nature generate data about behaviors or attitudes based on
> observing them directly. These methods are better suited for answering questions about why or
> how to fix a problem. In quantitative studies, the data about the behavior or attitudes are
> gathered indirectly, through a measurement and answer how many and how much types of
> questions." `(NN/g, verbatim)`

**To place a question on this axis:** is it a *why* or *how to fix* question, or a *how many* or
*how much* question?

### 3. Context of product use

Four categories. On the chart this is marker shape and colour rather than an axis.
`(NN/g, stated)`

| Category | What it means |
|---|---|
| **Natural** | Natural use of product. Minimise interference from the study so behaviour is as close to reality as possible. |
| **Scripted** | Scripted, often lab-based use of product. Focuses insight on specific areas, with varying degrees of control. |
| **Limited** | Limited use of product. A limited or abstracted form of the product, to study one specific aspect. |
| **Decontextualized** | Not using the product at all. For issues broader than usage, such as brand or aesthetic attributes. |

This dimension does not filter candidates. It is reported, because a set of methods that are all
`scripted` has learned nothing about natural use, and that is worth saying in the brief.

---

## The three phases

From the article. `(NN/g, stated)`

| Phase | Goal | Research type |
|---|---|---|
| **Strategize** | Find new directions and opportunities | Generative |
| **Design** | Improve usability of design | Formative |
| **Launch and assess** | Measure product performance against itself or its competition | Summative |

The phase comes from what exists today: nothing yet means strategize, a design that needs
improving means design, something live to measure means launch and assess.

Methods the article names per phase:

- **Strategize:** field studies, diary studies, interviews, surveys, participatory design,
  concept testing
- **Design:** card sorting, tree testing, usability testing, remote moderated testing,
  unmoderated testing
- **Launch and assess:** usability benchmarking, unmoderated testing, A/B testing, clickstream
  analytics, analytics, surveys

Five methods are not assigned a phase by the article: customer feedback, desirability studies,
eyetracking, focus groups, contextual inquiry. Their phase lines below are `(derived)`.

---

## The source's own caveat

Carry this into any output built on this file.

> The classifications are "general guidelines, rather than rigid classifications."
> `(NN/g, verbatim)`

> "While many user-experience research methods have their roots in scientific practice, their
> aims are not purely scientific and still need to be adjusted to meet stakeholder needs."
> `(NN/g, verbatim)`

And the article's guidance on combining: teams should use complementary methods rather than lean
on the one or two they are familiar with. `(NN/g, stated)` This is what the triangulation check
in `SKILL.md` enforces.

---

## A second framework, deliberately not blended in

The UX Research Cheat Sheet, Susan Farrell, 12 February 2017,
https://www.nngroup.com/articles/ux-research-cheat-sheet/, organises methods as
discover / explore / test / listen. It is a different framework by a different author, not a
refinement of this one, and mixing the two produces a taxonomy neither source supports. It is
recorded here so that a future session recognises it rather than importing it.

Its headline guidance is worth knowing and does not conflict: "If you can do only one activity
and aim to improve an existing system, do qualitative (think-aloud) usability testing."

---

# The 20 methods

Ordered by phase, then by how commonly they are reached for.

---

## Strategize (generative)

### Interviews

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                decontextualized     (derived)
    Phase:                         strategize           (NN/g, stated)

**What it is:** "A researcher meets with participants one-on-one to discuss in depth what the
participant thinks about the topic in question." `(NN/g, verbatim)`

**Answers:** Why, and how to fix it. Motivations, mental models, how someone describes their own
decision, what they are trying to achieve and what gets in the way. `(derived)`

**Cannot tell you:** How many people think this, or what any of them actually do. It is
self-report at a remove from the product, so it will surface a stated preference and miss the
behaviour that contradicts it. It cannot establish a frequency, and it cannot tell you whether a
design works, only what someone says about it. `(derived)`

**Needs:** Nothing built. **Minimum 6 participants** per audience segment, 60 minutes each.
`(house)` Every attitude question needs a paired critical-incident follow-up, per the
corroboration rule above. `(house)`

**Executed by:** `discussion-guide`

### Field Studies

    Attitudinal <-> Behavioral:    mixed                (NN/g, stated)
    Qualitative <-> Quantitative:  qualitative          (NN/g, stated)
    Context of use:                natural              (NN/g, stated)
    Phase:                         strategize           (NN/g, stated)

**What it is:** "Researchers study participants in their own environment (work or home), where
they would most likely encounter the product or service being used in the most realistic or
natural environment." `(NN/g, verbatim)`

**Answers:** Why, in the setting that actually produces the behaviour. What the real constraints
are, what else is competing for attention, what workaround already exists. The method that finds
the problem nobody reported. `(derived)`

**Cannot tell you:** How many, or how often. Natural use means you see what happened to happen
while you were there, so a rare but important event may not occur. Expensive per participant,
which caps the sample hard. `(derived)`

**Needs:** Access to participants in their own environment, travel, a day or more per
participant. The most costly method here in time. `(derived)`

**Executed by:** none yet

### Contextual Inquiry

    Attitudinal <-> Behavioral:    mixed                (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                natural              (derived)
    Phase:                         strategize           (derived)

**What it is:** "Researchers and participants collaborate together in the participants own
environment to inquire about and observe the nature of the tasks and work at hand."
`(NN/g, verbatim)` The article notes it was developed to study complex systems and in-depth
processes. `(NN/g, stated)`

**Answers:** Why, for work that is too complex to describe from memory. The actual sequence of a
task, the tacit knowledge the person cannot articulate unprompted, where the real system differs
from the documented one. `(derived)`

**Cannot tell you:** How many, how often. The collaboration that makes it work also means the
researcher is in the loop, so it is not a clean observation of unaided behaviour. `(derived)`

**Needs:** Access in the participant's own environment, and a domain complex enough to justify
it. Overkill for a consumer checkout. `(derived)`

**Executed by:** none yet

### Diary Studies

    Attitudinal <-> Behavioral:    mixed                (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                natural              (derived)
    Phase:                         strategize           (NN/g, stated)

**What it is:** "Participants are given a mechanism (diary or camera) to record and describe
aspects of their lives that are relevant to a product or service or simply core to the target
audience. Diary studies are typically longitudinal and can be done only for data that is easily
recorded by participants." `(NN/g, verbatim)`

**Answers:** Why, over time. How something fits into a life or a week rather than a session.
Behaviour that is too spread out to observe in one sitting, and change in attitude across a
period. `(derived)`

**Cannot tell you:** Anything the participant did not think to record, or found hard to record.
The source's own constraint is the binding one: it works "only for data that is easily recorded
by participants". Participation decays over the study, so late data is thinner than early data.
`(derived)`

**Needs:** Weeks, not days. A recording mechanism, and participants willing to keep at it.
`(derived)`

**Executed by:** none yet

### Participatory Design

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                limited              (NN/g, stated)
    Phase:                         strategize           (NN/g, stated)

**What it is:** "Participants are given design elements or creative materials in order to
construct their ideal experience in a concrete way that expresses what matters to them most and
why." `(NN/g, verbatim)`

**Answers:** Why, and what someone prioritises when forced to choose. What matters most, made
concrete rather than stated. Useful when a person cannot rank their own priorities in the
abstract but can arrange them on a table. `(derived)`

**Cannot tell you:** What to build. What someone constructs is a statement of priority, not a
design, and treating the artefact as a specification is the standard misuse of this method.
It is also not behaviour: nobody is using anything. `(derived)`

**Needs:** Materials, a workshop slot, a facilitator. Participants in the same room or a
workable remote equivalent. `(derived)`

**Executed by:** none yet

### Concept Testing

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  either               (derived)
    Context of use:                limited              (NN/g, stated)
    Phase:                         strategize           (NN/g, stated)

**What it is:** "A researcher shares an approximation of a product or service that captures the
key essence (the value proposition) of a new concept or product in order to determine if it meets
the needs of the target audience. It can be done one-on-one or with larger numbers of
participants, and either in person or online." `(NN/g, verbatim)`

**Answers:** Whether the value proposition lands at all, before anything is built properly. Which
of several directions resonates. Scales either way, so it can answer *why* with a few people or
*how many* with a lot. `(derived)`

**Cannot tell you:** Whether anyone will use it, or whether it is usable. A reaction to a
proposition is not a prediction of behaviour, and the approximation is not the product. This is
the method most often over-read: enthusiasm for a concept routinely fails to convert.
`(derived)`

**Needs:** An approximation of the concept. **Rules itself out if there is nothing to show
yet.** `(derived)`

**Executed by:** none yet

### Focus Groups

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                decontextualized     (NN/g, stated)
    Phase:                         strategize           (derived)

**What it is:** "Groups of 3 to 12 participants are led through a discussion about a set of
topics, giving verbal and written feedback through discussion and exercises."
`(NN/g, verbatim)` The article is explicit that focus groups "tend to be less useful for
usability purposes" while giving top-of-mind views on brand or concept. `(NN/g, stated)`

**Answers:** Top-of-mind reaction to a brand, a concept or a category, and the vocabulary people
use when talking to each other about it. `(derived)`

**Cannot tell you:** Anything about usability, which the source says outright. Group dynamics
contaminate individual opinion, so the output is a group position rather than eight independent
ones, and the loudest participant distorts it. Not a substitute for interviews. `(NN/g, stated)`
and `(derived)`

**Needs:** 3 to 12 participants simultaneously, a skilled moderator, a room.
`(NN/g, verbatim)` on the count.

**Executed by:** none yet

---

## Design (formative)

### Usability Testing

    Attitudinal <-> Behavioral:    mixed                (NN/g, stated)
    Qualitative <-> Quantitative:  qualitative          (NN/g, stated)
    Context of use:                scripted             (NN/g, stated)
    Phase:                         design               (NN/g, stated)

**What it is:** "Participants are brought into a lab, one-on-one with a researcher, and given a
set of scenarios that lead to tasks and usage of specific interest within a product or service."
`(NN/g, verbatim)`

**Answers:** Why, and how to fix it. Whether someone can complete a task, where they stall, what
they expected instead. The default answer to "is this design working", and the Cheat Sheet's
single recommendation if only one activity is possible. `(NN/g, stated)`

**Cannot tell you:** How many people hit the problem, or whether a fix worked at scale. Scripted
use is not natural use, so it will not tell you whether anyone wants the task at all, or whether
they would have persisted without a researcher watching. `(derived)`

**Needs:** A working artefact, from wireframe upward. A moderator. **Minimum 6 participants**
per segment. `(house)` The five-user rule is contested rather than settled, and the argument is
laid out in `usability-test-plan/references/task-design.md`. `(derived)`

**Executed by:** `usability-test-plan`

### Remote Moderated Testing

    Attitudinal <-> Behavioral:    mixed                (derived)
    Qualitative <-> Quantitative:  qualitative          (derived)
    Context of use:                scripted             (derived)
    Phase:                         design               (NN/g, stated)

**What it is:** "Usability studies conducted remotely, with the use of tools such as video
conferencing, screen-sharing software and remote-control capabilities." `(NN/g, verbatim)`

**Answers:** The same questions as usability testing, with wider geographic reach and lower cost
per session. `(derived)`

**Cannot tell you:** The same limits as usability testing, plus you lose the room: body language
is partial, the participant's real environment is out of frame, and connection problems eat
session time. `(derived)`

**Needs:** A working artefact, a moderator, screen sharing the participant can actually operate.
`(derived)`

**Executed by:** `usability-test-plan`

### Unmoderated Testing

    Attitudinal <-> Behavioral:    mixed                (derived)
    Qualitative <-> Quantitative:  either               (NN/g, stated)
    Context of use:                scripted             (derived)
    Phase:                         design, launch and assess   (NN/g, stated)

**What it is:** "An automated method that can be used in both quantitative and qualitative
studies and that uses a specialized research tool to capture participant behaviors and attitudes,
usually by giving participants goals or scenarios to accomplish with a site, app, or prototype."
`(NN/g, verbatim)`

**Answers:** Either side of the qual/quant axis, which is what makes it unusual here. With a
large sample it answers how many completed and how long it took; with a small one and think-aloud
recordings it answers why. Runs overnight and across time zones. `(derived)`

**Cannot tell you:** Why, reliably, because nobody can ask a follow-up. Unexpected behaviour goes
unexplained, participants misread tasks with no one to correct them, and you cannot probe the one
interesting thing that happens. The data arrives already shaped by whatever the task text said.
`(derived)`

**Needs:** A working artefact robust enough to survive unsupervised use, a research tool, and
task wording that cannot be misread, since there is no moderator to recover from it. `(derived)`

**Executed by:** `usability-test-plan`

### Card Sorting

    Attitudinal <-> Behavioral:    attitudinal          (NN/g, stated)
    Qualitative <-> Quantitative:  either               (NN/g, stated)
    Context of use:                limited              (NN/g, stated)
    Phase:                         design               (NN/g, stated)

**What it is:** "A quantitative or qualitative method that asks users to organize items into
groups and assign categories to each group. This method helps create or refine the information
architecture of a site by exposing users' mental models." `(NN/g, verbatim)`

**Answers:** How people group your content, and what they would call each group. Builds or
refines an information architecture. Quantitative with enough participants, qualitative with few.
`(derived)`

**Cannot tell you:** Whether anyone can then find anything, which is tree testing's job. It works
on items out of context, so a grouping that makes sense on cards can still fail in a navigation
bar. It is attitudinal: this is where people say things belong, not where they look for them.
`(derived)`

**Needs:** A set of content items. No design required, which is why it comes before one.
`(derived)`

**Executed by:** none yet

### Tree Testing

    Attitudinal <-> Behavioral:    behavioral           (derived)
    Qualitative <-> Quantitative:  quantitative         (NN/g, stated)
    Context of use:                limited              (NN/g, stated)
    Phase:                         design               (NN/g, stated)

**What it is:** "A quantitative method of testing an information architecture to determine how
easy it is to find items in the hierarchy. This method can be conducted on an existing
information architecture to benchmark it and then again after the information architecture is
improved with card sorting to demonstrate improvement." `(NN/g, verbatim)`

**Answers:** How many people find a given item, and where the ones who fail go instead. The
quantitative counterpart to card sorting, and the source explicitly pairs them: tree test to
benchmark, card sort to improve, tree test again to prove it moved. `(NN/g, stated)`

**Cannot tell you:** Why someone went the wrong way. It tests the hierarchy stripped of visual
design, so a structure that passes a tree test can still fail once labels compete with layout.
`(derived)`

**Needs:** An existing or proposed hierarchy, and enough participants for the numbers to mean
something. `(derived)`

**Executed by:** none yet

### Eyetracking

    Attitudinal <-> Behavioral:    behavioral           (NN/g, stated)
    Qualitative <-> Quantitative:  quantitative         (derived)
    Context of use:                scripted             (derived)
    Phase:                         design               (derived)

**What it is:** "An eyetracking device is configured to precisely measure where participants look
as they perform tasks or interact naturally with websites, applications, physical products, or
environments." `(NN/g, verbatim)`

**Answers:** What was looked at, in what order, and for how long. Whether something was seen at
all, which is the question no other method answers cleanly. `(derived)`

**Cannot tell you:** What any of it meant. Gaze is not comprehension and not intent, and the
standard failure is reading a heatmap as a preference. Needs a large sample before aggregate
patterns are trustworthy. `(derived)`

**Needs:** Hardware, calibration, a lab, and a specific question about attention. Hard to justify
otherwise. `(derived)`

**Executed by:** none yet

### Desirability Studies

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  either               (NN/g, stated)
    Context of use:                decontextualized     (NN/g, stated)
    Phase:                         design               (derived)

**What it is:** "Participants are offered different visual-design alternatives and are expected
to associate each alternative with a set of attributes selected from a closed list. These studies
can be both qualitative and quantitative." `(NN/g, verbatim)`

**Answers:** What a visual direction communicates, in words, and which of several directions
communicates the intended thing. The method for settling a brand or aesthetic argument with
evidence rather than taste. `(derived)`

**Cannot tell you:** Whether anyone can use it. Decontextualized means nobody is doing a task, so
a design that tests as "trustworthy, modern, calm" can still be unusable. The closed attribute
list caps what can be discovered: you only learn about attributes you thought to offer.
`(derived)`

**Needs:** Two or more visual alternatives, and a closed attribute list that someone has to
write. `(derived)`

**Executed by:** none yet

---

## Launch and assess (summative)

### Analytics

    Attitudinal <-> Behavioral:    behavioral           (derived)
    Qualitative <-> Quantitative:  quantitative         (derived)
    Context of use:                natural              (NN/g, stated)
    Phase:                         launch and assess    (NN/g, stated)

**What it is:** "Analyzing data collected from user behavior like clicks, form filling, and other
recorded interactions. It requires the site or application to be instrumented properly in
advance." `(NN/g, verbatim)`

**Answers:** How many and how much, over everyone, continuously, at no marginal cost once it is
running. Where people drop out, what proportion complete, how that changes week to week.
`(derived)`

**Cannot tell you:** Why any of it happened. It records what was clicked, not what was wanted or
expected, so it will locate a problem precisely and explain it not at all. It also only ever
answers questions someone anticipated: the source's own condition is that instrumentation has to
exist "in advance". `(NN/g, stated)` and `(derived)`

**Needs:** Instrumentation already in place, and live traffic. Cannot be run retrospectively on
events nobody logged. `(derived)`

**Executed by:** none yet

### Clickstream Analytics

    Attitudinal <-> Behavioral:    behavioral           (derived)
    Qualitative <-> Quantitative:  quantitative         (derived)
    Context of use:                natural              (derived)
    Phase:                         launch and assess    (NN/g, stated)

**What it is:** "A particular type of analytics that involves analyzing the sequence of pages that
users visit as they use a site or software application." `(NN/g, verbatim)`

**Answers:** Route rather than rate. The paths people actually take, where a journey diverges
from the designed one, which page precedes an exit. `(derived)`

**Cannot tell you:** Why a path was taken, or whether it succeeded in the person's own terms. A
sequence looks like intent and is not: a loop may be confusion or may be comparison shopping.
`(derived)`

**Needs:** Instrumentation and live traffic, as analytics. `(derived)`

**Executed by:** none yet

### A/B Testing

    Attitudinal <-> Behavioral:    behavioral           (NN/g, stated)
    Qualitative <-> Quantitative:  quantitative         (NN/g, stated)
    Context of use:                natural              (derived)
    Phase:                         launch and assess    (NN/g, stated)

**What it is:** "A method of scientifically testing different designs on a site by randomly
assigning groups of users to interact with each of the different designs and measuring the effect
of these assignments on user behavior." `(NN/g, verbatim)`

**Answers:** Which of two designs performs better on one measure, with a causal claim behind it.
The only method here that establishes causation rather than association. `(derived)`

**Cannot tell you:** Why the winner won, or whether the measure you chose was the right one. It
compares the options you had, so it cannot find the better third option, and it optimises toward
whatever was instrumented, which is how local maxima get defended with data. Needs real traffic
volume before a result means anything. `(derived)`

**Needs:** **Two or more live designs.** Rules itself out when there is only one. Plus traffic
volume and a single agreed success measure. `(derived)`

**Executed by:** none yet

### Usability Benchmarking

    Attitudinal <-> Behavioral:    mixed                (derived)
    Qualitative <-> Quantitative:  quantitative         (derived)
    Context of use:                scripted             (NN/g, stated)
    Phase:                         launch and assess    (NN/g, stated)

**What it is:** "Tightly scripted usability studies are performed with several participants, using
precise and predetermined measures of performance." `(NN/g, verbatim)`

**Answers:** How many and how much, on task performance. Whether a redesign actually improved
anything, or how you compare with a competitor, with numbers that survive a stakeholder meeting.
`(derived)`

**Cannot tell you:** Why, and not much that you did not predetermine. The tight script that makes
the numbers comparable also means an unanticipated problem has nowhere to show up. The measures
have to be fixed before you start, so it answers last quarter's question. `(derived)`

**Needs:** Many more participants than qualitative testing, a fixed script, predetermined
measures, and ideally a prior baseline to compare against. The heaviest method here to run well.
`(derived)`

**Executed by:** `usability-test-plan`

### Surveys

    Attitudinal <-> Behavioral:    attitudinal          (NN/g, stated)
    Qualitative <-> Quantitative:  quantitative         (NN/g, stated)
    Context of use:                decontextualized, or natural when intercepted   (NN/g, stated)
    Phase:                         strategize, launch and assess                   (NN/g, stated)

**What it is:** "A quantitative measure of attitudes through a series of questions, typically more
closed-ended than open-ended." `(NN/g, verbatim)` Intercept surveys are triggered during site use
and so sit in natural context. `(NN/g, stated)`

**Answers:** How many and how much, on attitude. Scale for a stated preference, sentiment
tracked over time, and the relative size of things you already know qualitatively.
`(derived)`

**Cannot tell you:** What anybody does. It is the furthest method here from behaviour, and the
usual error is reading a stated intention as a forecast. It can only measure what the questions
asked, so it confirms and sizes existing hypotheses rather than finding new ones, and every
answer is subject to the bias taxonomy in
`survey-questions-v2/references/bias-types.md`. `(derived)`

**Needs:** A hypothesis worth sizing, enough respondents, and a distribution route. Should
normally follow qualitative work rather than precede it. `(NN/g, stated)` on complementarity.

**Executed by:** `survey-questions-v2`

### Customer Feedback

    Attitudinal <-> Behavioral:    attitudinal          (derived)
    Qualitative <-> Quantitative:  either               (derived)
    Context of use:                natural              (derived)
    Phase:                         launch and assess    (derived)

**What it is:** "Open-ended and/or close-ended information provided by a self-selected sample of
users, often through a feedback link, button, form, or email." `(NN/g, verbatim)`

**Answers:** What the people who chose to tell you are telling you. Continuous, cheap, already
running in most products, and good at surfacing a problem's existence. `(derived)`

**Cannot tell you:** How common anything is. The source's own phrase is the whole limitation:
a **self-selected sample**. It over-represents the very angry and the very pleased and says
nothing about the silent majority, so counting it produces a confident wrong number. Read it for
leads to investigate, never as a measure. `(NN/g, stated)` and `(derived)`

**Needs:** A feedback channel and a live product. Effectively free, which is why it is
over-trusted. `(derived)`

**Executed by:** none yet

---

## Methods not in this library

Recorded so a future session does not mistake an omission for an oversight.

**Dropped from the 2014 version of the chart** and deliberately not carried forward, since this
library follows the current article: true-intent studies, email surveys, camera studies,
unmoderated remote panel studies, usability-lab studies, intercept surveys as a separate method
(now a mode of Surveys).

**Commonly used but not in Rohrer's 20**, so not selectable here until proposed and approved:
accessibility evaluation, expert or heuristic review, competitive usability evaluation, desk
research and competitive analysis, stakeholder interviews, journey mapping, personas, task
analysis, search query analysis, service blueprinting, first-click testing, five-second tests,
preference tests, Wizard of Oz testing, longitudinal cohort analysis.

**Note on desk research.** `desk-research` is an installed specialist skill in this family, and
desk research is not one of Rohrer's 20, because the framework classifies methods by how they
engage *users* and desk research engages none. It should be offered when the brief needs
landscape context, and it should not be presented as one of the 20 or plotted on the chart.
`(derived)`

**Executed by:** `desk-research` (not a method in the 20, offered as an adjunct when the brief
needs landscape context)

---

## Change log

**7 October 2026.** File created. 20 methods from the 2022 revision of Rohrer's article, replacing
the four-activity table that previously lived inline in `SKILL.md`. Placements for six methods are
source-stated; the rest are derived from method definitions because the chart is a raster image.
All `Cannot tell you` fields are derived and tagged as such.
