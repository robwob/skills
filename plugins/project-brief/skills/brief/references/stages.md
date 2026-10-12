# Stage catalogue and routing rules

The route in section 14 is built from this catalogue. Two lanes, design and build, in one ordered
list. A project that needs data plumbing gets the plumbing stages in the same route as the design
stages, ordered against each other, not kept in a separate plan.

---

## Activity types

Every stage carries one, and it appears in the brief next to the stage. It tells the reader what
kind of work a step is before they read what it is, which is what makes a plan skimmable by someone
who was not in the conversation.

| Type | What it is | Ends with |
|---|---|---|
| **Research** | Finding out something not currently known. Data, precedent, feasibility | A written finding, with sources or the artefact itself |
| **Define** | Deciding something, where the options are known and the choice is not | A decision recorded with its rejected alternative |
| **Design** | Making the thing visible before it is real. Structure, states, visual | An artefact that can be reacted to |
| **Build** | Writing the thing | Working software |
| **Ship** | Putting it where it is used | Something reachable by the person who needs it |

Two rules that fall out of the types:

- **A stage has exactly one type.** A step that is both research and build is two steps that have
  not been separated, and separating them is nearly always the right move because the research
  usually changes the build.
- **Research before Define before Design.** Defining without research is guessing, and designing
  without a definition is decorating. Where a route breaks this order, say why in the brief.

## The codes are internal

`G1`, `D3`, `B2` and the rest exist so the inclusion and ordering rules in this file
can refer to stages precisely. **They never appear in a written brief.** Section 14
and section 15 use plain names: "get a real sample", "discovery wireframe", "read
layer", "deploy".

A brief that needs a decoder is a brief its reader will skim. If a stage has no
plain name that fits the project, write what it actually does instead of falling
back to the code.

## Ordering principles

These override any default order below.

1. **Anything that could invalidate later work goes first.** Unseen data, an unsettled approach and
   an unverified technical assumption all come before the first design stage. Designing against a
   guess means designing twice.
2. **The first deliverable is the cheapest reviewable thing.** Not the easiest to build. The
   fastest to get a real reaction to.
3. **One instance, approved, then propagate.** Never place a stage that produces many of something
   before a stage that produces one and stops.
4. **Fragile work is deferred.** Auth, scheduled jobs, credentials and deploys go to phase 2 unless
   phase 1 is useless without them.

---

## Groundwork stages

Placed before everything by principle 1.

### G1. Get a real sample  *(Research)*

**Include when:** section 8 says no real sample has been seen.
**Skip when:** a sample is already in hand and has been looked at.
**Produces:** the actual data, in the actual format, in the project folder.

This is the single most commonly skipped stage and the most expensive to skip. It nearly always
takes under an hour and it invalidates schema guesses before they become code.

### G2. Resolve a blocking unknown  *(Research)*

**Include when:** section 10 holds a question whose answer changes what gets built.
**Skip when:** every open question is a preference that can be decided later.
**Produces:** an answer written into the brief, not a conversation.

One stage per blocking unknown. A question that only changes a detail is not blocking and stays in
section 10.

### G3. Spike the risky assumption  *(Research)*

**Include when:** the project rests on something technical that has not been proven to work here.
**Skip when:** every piece has been done before in this workspace.
**Produces:** the smallest thing that proves it works or proves it does not. Thrown away after.

### G4. Gather references  *(Research)*

**Include when:** the project builds a screen type not built before in this workspace, and an
established form for it exists in the wild. Dashboards, feeds, settings, onboarding, pricing tables,
data tables and calendars all qualify.
**Skip when:** the thing has no precedent worth looking at, or the reuse audit already found an
internal instance to follow.
**Produces:** a written set of references with what is being borrowed from each, covering three
questions separately:

- **What to build.** Which panels or modules earn their place, and which ones every example includes
  out of habit.
- **How it works.** Ordering, grouping, density, what is on screen at rest versus behind an
  interaction, how time ranges are chosen.
- **How it looks.** Type scale, chart treatment, use of colour for meaning rather than decoration.

Runs alongside G1 rather than after it, because neither blocks the other. Both must finish before
D3, since a wireframe drawn without either is drawn from imagination.

Name the sources. A reference stage that produces adjectives instead of links has not been done.

---

## Design stages

Each maps to an existing skill. Do not re-derive what the skill does, just route to it.

### D1. Strategy: what problem is being solved  *(Research)*

Run by `analyse-themes` where `house-rules.md` names it.

**Include when:** the approach is contested or unknown, meaning section 9 holds no decision on how
the problem is solved, or section 3 lists functions with no agreed shape.
**Skip when:** the concept is settled and only the execution is open. Most personal tools skip it.

### D2. Direction: what to dial up or down  *(Define)*

Run by `define-levers` where `house-rules.md` names it.

**Include when:** themes are named but there is no direction on what to dial up or down.
**Skip when:** D1 was skipped, unless the user names themes directly.

### D3. Structural wireframes  *(Design)*

Greyscale, shape only, no styling. Run by `discovery` where `house-rules.md` names it.

**Include when:** any new screen or layout is needed.
**Skip when:** the reuse audit found an existing layout or template this is an instance of. Note
which one it is an instance of instead.
**Produces:** greyscale structural wireframes, one artboard per screen.

### D4. Interaction states  *(Design)*

Run by `interaction` where `house-rules.md` names it.

**Include when:** there is any state beyond static display. Loading, empty, error, selected,
filtered, hovered.
**Skip when:** the output genuinely renders once and never changes. Rare. Check section 11 before
skipping, because the failure modes listed there are states.
**Requires:** D3 approved.

### D5. Visual styling  *(Design)*

Run by `ui` where `house-rules.md` names it.

**Include when:** anyone other than the builder will see it, or the builder will look at it often
enough for it to matter.
**Skip when:** it is a throwaway or a spike.
**Requires:** D4 approved.

### D6. Review  *(Design)*

**Include:** an interaction review after D4, a visual review after D5, and a copy review when the
thing carries meaningful copy such as labels, errors or empty states. Where `house-rules.md` names
review skills, route to them. Where it does not, say what is being reviewed against.
**Skip when:** the piece is small enough that the review costs more than the defects.

---

## Build stages

### B1. Define the schema  *(Define)*

**Include when:** the project owns any structured data of its own.
**Skip when:** it only reads someone else's format unchanged.
**Requires:** G1, always. A schema defined before the real data has been seen is a draft.

### B2. Read layer  *(Build)*

**Include when:** the thing loads data from anywhere.
**Produces:** data in memory, proven, with nothing rendered yet. Keep it separate from B3 so a
rendering bug and a parsing bug cannot be confused.

### B3. Build the first view  *(Build)*

**Include:** always, when there is an interface.
**Produces:** one view, the one serving the highest-value core function from section 3. Stop here.
This is the review gate that matters most.

### B4. Build the remaining views  *(Build)*

**Include when:** section 3 holds more than one function needing its own view.
**Requires:** B3 approved. Principle 3.

### B5. Logic and reconciliation  *(Build)*

**Include when:** the project compares, derives or computes rather than just displaying.
**Placed:** after the views it feeds, so the output can be seen while the logic is being got right.

### B6. Failure and empty states  *(Build)*

**Include when:** section 11 is non-empty, which is always.
**Placed:** before phase 1 is called done, not after. An empty state discovered in use is a bug;
one built deliberately is a feature.

### B7. Automation  *(Build)*

**Include when:** the thing needs to happen without being asked.
**Placed:** phase 2. Principle 4.

### B8. Deploy  *(Ship)*

**Include when:** it is needed somewhere other than this machine.
**Placed:** phase 2. Principle 4.
**Check `house-rules.md` first.** Some paths must never leave the machine, and a route that would
deploy one is wrong regardless of what the project wants.

---

## Default order

Stages that survive their inclusion test, in this order, minus the ones skipped:

```
Research  G1  get a real sample
Research  G2  resolve blocking unknowns
Research  G3  spike the risky assumption
Research  G4  gather references          <- runs alongside G1
Research  D1  strategy
Define    D2  direction
Define    B1  define the schema
Design    D3  structural wireframes      <- gate: wireframe approved
Design    D4  interaction states        <- gate: states approved
Design    D6  interaction review
Design    D5  visual styling            <- gate: one styled instance approved
Design    D6  visual + copy review
Build     B2  read layer
Build     B3  first view                 <- gate: the highest-value view, alone
Build     B5  logic and reconciliation
Build     B4  remaining views
Build     B6  failure and empty states
--- phase 1 done ---
Build     B7  automation
Ship      B8  deploy
```

B1 sits between the design strategy stages and Discovery because the schema shapes what can be put
on screen, and it is cheap to change before a wireframe exists and expensive after.

Reorder freely when the ordering principles say to. Record any departure from this default in
section 15 with its reason, so the next session does not read it as an error.

---

## Checkpoints

Two kinds, and conflating them is the most common way a plan stops being followed.

**Start approval, before every stage.** What the stage will produce, what it touches, what it needs
answered first, roughly how long. Then stop. Applies to every stage in the route without exception,
including the small ones and including research.

**Output gate, after some stages.** The work is shown and the question is asked. Only where the
output shapes everything after it.

A gate never carries permission for the next stage. Approving a wireframe approves the wireframe.

## Gates

Every gate is a named step in section 15 with the thing being shown and the question being asked.
Four gates are standard. Add others where principle 3 applies.

| Gate | Shown | Question |
|---|---|---|
| After D3 | One wireframe | Is this the right structure? |
| After D4 | The state map for one screen | Is anything missing? |
| After D5 | One styled instance | Is this right before it goes on the other screens? |
| After B3 | The single highest-value view, with real data | Does this answer the function it exists for? |
