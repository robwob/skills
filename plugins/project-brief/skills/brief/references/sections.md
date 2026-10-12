# Brief sections

Sixteen sections in three parts. Part A is asked first and gates the rest. Part B determines the
route. Part C is derived, not asked.

Each section below gives the question to ask, the test the answer must pass, and a pass/fail pair
drawn from real briefs.

---

## Part A: why

Nothing in Part B is asked until all four of these pass.

### 1. Why now

**Ask:** What prompted this? What happens if it is not done?

**Test:** The answer names a trigger and a cost. "It would be nice to have" is not a trigger.
"Nothing happens" is a valid cost, and it means the project should not start.

- Fails: "I want a dashboard for my training."
- Passes: "I am eight months out from a 70.3 and training on feel. Garmin holds the data but it is
  spread across five screens, so I only look at it after a session, never before one. Without this
  I will get to race day not knowing whether the block worked."

**Why it is first:** it is the only section that can end the project, and it should be allowed to.

### 2. Goal

**Ask:** In one sentence, what is the single outcome?

**Test:** One sentence, one outcome, no "and". A goal with an "and" is two projects that have not
been separated yet. It should be possible to fail it.

- Fails: "Track my training and fuelling and see my progress and get suggestions."
- Passes: "Know, before each week starts, whether the block is working and what to change."

**If there are genuinely two:** name both, pick the one this project serves, and record the other as
a non-goal in section 6 with a note that it is deferred, not dropped.

### 3. Core functions

**Ask:** What must it do? The jobs it performs, not the features it has.

**Test:** Each item is a job, phrased as something the thing does for someone, and each one traces
to the goal. A function that does not serve section 2 is scope, not a core function, and belongs in
section 6.

- Fails: "Charts, a calendar view, a settings page." Those are features. They describe what it is
  made of, not what it does.
- Passes: "Shows whether fitness is trending up across the block. Shows which sport is lagging.
  Shows what was planned against what actually happened."

**Count:** three to six. Fewer than three usually means the goal is too small to be a project. More
than six means section 6 has not been written yet.

### 4. What success looks like

**Ask:** For each core function, how will you know it worked?

**Test:** Observable, and capable of being failed. If no realistic outcome would count as failure,
it is not a criterion. A criterion that restates the function has failed the test.

- Fails: "I can see if I am getting fitter." That is function 1 with different words.
- Passes: "I open it on a Sunday and within five seconds I know whether to make next week harder or
  easier, without opening Garmin Connect."

**This section is the gate.** If it cannot be answered, stop and say so. Do not write the brief.
The way through is either to define success properly, or to name the smallest piece of work that
would make success definable and let that be the project.

---

## Part B: shape

These do not gate the brief, but they determine the route. A thin answer here produces a wrong
plan, not just a thin brief.

### 5. Who it is for, when, and on what

Three parts. The third is the one that gets assumed instead of asked, and it is the one that
changes the most.

**5a. Who.** "Me" is a fine answer.

**5b. When.** At what moment? What are they doing immediately before and after?

**Test:** Names a moment, not a persona. "Whenever" is not an answer.

The moment sets the constraints: a thing used on a phone mid-session and a thing used on a laptop
on a Sunday are different products with the same content. Where there are two moments, name both.
Two moments is normal and is not a problem, but an unnamed second moment is.

**5c. On what.** Web, installable web app, native mobile, desktop, or something that is not an
interface at all such as a scheduled email or a file.

**Ask it directly.** Do not infer the platform from the device in 5b. A phone moment does not mean
a native app, and a laptop moment does not rule one out.

**Test:** One named target, with the others explicitly rejected and a reason. "Responsive web,
because both moments are covered by one build and it fits a weekend" passes. "It should work on my
phone" does not, because it names a device and not a platform.

This answer decides the whole build lane: the stack, whether there is a deploy stage at all,
whether offline matters, whether anything needs installing, and whether a review stage is even
possible. Getting it wrong is not a detail, it is a different project.

The common options and what each costs:

| Target | Buys | Costs |
|---|---|---|
| **Responsive web, local file** | Fastest to build, no deploy, no accounts, opens in any browser | Only on the machine holding the file. Awkward on a phone |
| **Responsive web, deployed** | Reachable from any device, one build for every moment | Needs a deploy stage, and a host for any private data |
| **Installable web app (PWA)** | Home screen icon, works offline, still plain HTML, CSS and JS | A manifest and a service worker. Real but small extra work |
| **Native mobile** | Best phone feel, device APIs, background work, notifications | A different stack and toolchain entirely. Rarely justified for a personal tool |

If the answer is "web for now, maybe an app later", record the web answer as the decision and the
app as a phase, not as an ambition. An ambition with no phase attached will be built for by
accident.

### 6. Non-goals

**Ask:** What will this deliberately not do?

**Test:** At least three, and at least one of them plausible enough that someone would have assumed
it was in scope. A non-goal nobody would have expected is not doing any work.

Sources to mine: the "and" removed from section 2, functions cut from section 3, anything the user
described as "maybe later".

### 7. The load-bearing principle

**Ask:** What is the one idea the build must not violate?

**Test:** One sentence, stated so that a future decision could be checked against it.

- Passes: "The two data sources never overwrite each other. Garmin is what happened, the plan is
  what was intended, and nothing merges them."

If the user cannot name one, propose the candidate visible in their answers and let them accept or
reject it. Do not leave it blank. The principle is what stops the build drifting once the details
get interesting.

### 8. Inputs and data

**Ask:** What does it need to work? Where does each thing come from? Have you actually looked at a
real sample?

**Test:** The sample question is answered yes or no, not "I can get one".

This changes the route more than any other answer in the brief. No sample seen means acquiring one
becomes stage one, ahead of every design stage, because a schema designed against imagined data is
a schema that gets rebuilt.

Also capture: rough volume, how often it changes, and what is missing or unreliable.

### 9. Decisions already made

**Ask:** What has been decided, and what was rejected?

**Test:** Each decision carries its reasoning and its rejected alternative. A decision recorded
without its alternative will be relitigated.

- Passes: "Manual export first, automated pull later. The unofficial Garmin library authenticates
  as a browser session against undocumented endpoints, so building on it before the shape is
  settled means debugging auth and design at once."

### 10. Open questions

**Ask:** What is still unknown, and what would resolve each one?

**Test:** Every question has a named resolver: a decision to make, a thing to look up, a person to
ask, or a piece of work that answers it. A question with no resolver is a blocker in disguise.

Open questions with work attached become stage one in the route.

### 11. Failure modes

**Ask:** What happens when the input is missing, malformed or empty?

**Test:** Covers the empty state, the partial state and the broken state. The empty state is the
one that gets skipped and the one that gets seen first.

### 12. Effort ceiling and stack

**Ask:** Past what point is this not worth doing? What is it built with?

**Test:** The ceiling is a limit, not an estimate. "A weekend, and if it is more than that I would
rather not have it" is the useful shape.

---

## Part C: derived

The user answers none of these. Work them out, show them back, then write the file.

### 13. Reuse audit

Search before writing. Look where `house-rules.md` says shared things live, plus any project named
in the answers. Report what already does part of this job, with paths.

"Nothing found" is valid only after looking. State where you looked.

### 14. Stage route

Apply `stages.md`. List every stage included with a one-line reason, and every stage skipped with
its reason. A route that includes everything has not made a decision.

### 15. Build order and review gates

The included stages, ordered by the four ordering principles in `stages.md`, with the points marked
where work stops and is shown before continuing.

A gate is a named step, not a hope. "Stop here and show the single reconciled week before building
the other eleven" is a gate.

**Every stage shows its activity type.** Research, Define, Design, Build or Ship, from the table in
`stages.md`, in its own column next to the step. It tells a reader what kind of work a step is
before they read what it is, which is what lets someone who was not in the conversation skim the
plan and still understand its shape.

A run of five Build steps with no Research before them is visible at a glance in a typed plan and
invisible in an untyped one. That is the point of the column.

**Show every phase, not just the first.** Where the project splits into phases, list the activities
for all of them. The later phases are sketched rather than sequenced, but they are named, because a
plan that stops at the current phase cannot show what the current phase is protecting. Any hard
dependency between phases is stated as a dependency, not left implied by the order.

Each phase carries: its activities, the gates inside it, its own definition of done, and what it is
useful for on its own. A phase that is not useful on its own is not a phase, it is the first half of
one.

### 16. Definition of done, phase 1

Section 4 narrowed to what phase 1 delivers. An observable state, not a feeling.

- Fails: "The dashboard is working well."
- Passes: "A local page reads one real Garmin export and one plan file and answers functions 1 and
  3 for the current week. Automation and deploy are not in phase 1."
