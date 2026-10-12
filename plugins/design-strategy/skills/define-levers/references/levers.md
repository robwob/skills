# Theme Levers and Psychology

The library `define-levers` reads from. 49 levers across the 12 themes in `analyse-themes`,
each with the psychology principles that explain why moving it works and the methods that move
it.

**Last updated:** 21 September 2026

---

## How this is structured

    Theme  ->  Lever  ->  Principle  ->  Method  ->  Inventory

- **Theme** is the design strategy. The 12 come from the `analyse-themes` vocabulary.
- **Lever** is a dimension the team can dial. Always a spectrum with two poles. Its
  `**What it is:**` line names the dimension in one sentence, and stays neutral about which pole
  is right, because both are real positions.
- **Principle** is the psychological mechanism that explains why moving the lever works.
- **Method** is a named design move that shifts the lever. Chunking, progressive disclosure,
  autosave, a decoy tier. Generic and reusable.
- **Inventory** is this page's instance of a method, and it is produced by `define-levers` at
  run time rather than stored here.

Principles explain, methods act. A lever with principles but no methods is an argument with
nothing to do about it. A lever with methods but no principles is a checklist.

Four rules govern the structure:

1. **A principle may sit under any number of levers.** If it acts on two dimensions it belongs
   to both. No principle is forced into a single home. The same is true of methods.
2. **A lever may serve more than one theme.** Currently only `Decision transparency` does, shared
   by Control and Personalisation.
3. **Both poles are real positions.** Neither end is correct by default. Several levers carry a
   counter-principle that explains the cost of the active pole, and those are marked
   *(counter)*.
4. **Every layer is expected to change, and every change is approved first.** Themes, levers,
   principles and methods are all first passes. The skill may propose an addition at any layer,
   but it stops and waits: nothing is written into this file until the user has approved it. The
   library grows through use, never silently.

The library is a preset list to select from, not a checklist to complete. A page in review will
be sitting on a handful of these, not all of them.

---

## Trust

Confidence in the product and the company behind it. Risk, transparency and reliability.
Everything social moved to Validation.

### Risk reversal
Buyer carries the full commitment burden -> risk is named and eliminated at the decision point.

**What it is:** How much of the commitment risk the page takes off the visitor before they
decide, rather than leaving it with them.

- **Loss Aversion**: a loss is felt roughly twice as strongly as an equivalent gain, so removing
  a downside beats adding an upside
- **Zero Risk Bias**: people over-prefer eliminating a small risk entirely over reducing a larger
  one, which is why "cancel anytime" outperforms a partial guarantee
- **Endowment Effect**: a trial creates a sense of ownership before any payment is made
- **Reactance**: a hard, irreversible commitment provokes resistance for its own sake
- **Status Quo Bias**: doing nothing is the safe default the page is arguing against

**Methods:** free trial, money-back guarantee, cancel-anytime copy, no-card-required signup, pilot or proof of concept.

### Exchange order  *(new)*
The page asks before it gives -> substantial value is delivered before anything is asked.

**What it is:** Whether the page gives something worth having before it asks for anything, or
asks first and delivers afterwards.

- **Reciprocity** *(Cialdini)*: receiving something creates an obligation to give back, and the
  obligation is felt even when the gift was unrequested
- **Endowment Effect**: value already received is owned, and walking away becomes a loss
- **Loss Aversion**: with nothing given up there is nothing to lose by starting
- **Labor Illusion**: visible effort spent on the user's behalf raises the sense of debt
- **Commitment and Consistency** *(Cialdini)*: accepting something small predicts accepting
  something larger
- **Reactance** *(counter)*: a gift with a visible hook attached reads as a transaction, and the
  obligation inverts into resistance

**Methods:** free tool or calculator, ungated content, usable free tier, sample or preview before signup, value delivered inside the first session.

### Disclosure upfrontness
Material terms buried in fine print -> surfaced in plain language before commitment.

**What it is:** How early, and in what language, the terms that would change someone's mind are
put in front of them.

- **Framing Effect**: the same terms accepted or rejected depending on wording
- **Cashless Effect**: cost that is abstracted or deferred is felt as smaller
- **Sunk Cost Effect** *(counter)*: late disclosure works commercially precisely because
  investment already made keeps people in
- **Deceptive Patterns**: the named failure mode at the passive pole
- **Trust and Credibility**: the accumulated judgement this lever feeds

**Methods:** all-in pricing table, plain-language terms summary, total cost shown before checkout, renewal terms stated at point of sale.

### Behavioural consistency  *(new)*
System behaves unpredictably or differently between sessions -> the same action produces the
same result every time.

**What it is:** How reliably the same action produces the same result, between sessions and
across the rest of the product.

- **Jakob's Law**: people expect your product to work like the others they already use
- **Mental Model**: reliability is the gap between expected and actual behaviour
- **Expectations Bias**: a set expectation shapes how the actual experience is perceived
- **Doherty Threshold**: consistent sub-400ms response reads as competence, not just speed
- **Postel's Law**: accept varied input, behave predictably in output

**Methods:** shared component library, consistent action placement, predictable loading and empty states, stable URLs.

### Data and privacy signalling  *(new)*
What happens to the user's data is unstated -> stated explicitly and specifically, before
collection.

**What it is:** How explicitly the page says what happens to the data it collects, and at what
point it says it.

- **Negativity Bias**: one privacy failure outweighs many assurances
- **Salience** *(MINDSPACE)*: a privacy commitment nobody sees does no work
- **Authority Bias**: certifications and compliance marks borrow credibility from the certifier
- **Privacy Paradox**: stated concern and actual behaviour diverge, so signalling matters more
  than the setting itself

Note: signalling what happens to data is Trust. Giving the user actual control over it is
Control's `Data portability and exit`.

**Methods:** privacy note at the point of collection, certification badges, data-use statement beside the field, explicit no-resale statement.

---

## Informative

Teaching the user. If they understand, they will act.

### Disclosure timing
All information presented at once -> revealed as the user signals need.

**What it is:** When the page hands over its information: all of it up front, or in pieces as
the reader signals they want it.

- **Cognitive Load**: total mental effort demanded at one moment
- **Miller's Law**: working memory holds about seven items, fewer under pressure
- **Choice Overload**: more options reduces the likelihood of any choice
- **Decision Fatigue**: decision quality degrades over a sequence
- **Information Scent**: a hidden section still needs a cue that it exists
- **Tesler's Law** *(counter)*: complexity is conserved, so hiding it moves it rather than
  removing it

**Methods:** progressive disclosure, accordions, show-more, staged forms, on-demand tooltips, advanced options collapsed behind defaults.

### Explanation depth
Label only -> full explanation with worked examples.

**What it is:** How far the page goes beyond naming a thing, from a bare label to a worked
example.

- **Curse of Knowledge**: the author cannot un-know what the reader does not know
- **Picture Superiority Effect**: images are remembered far better than text
- **Storytelling Effect**: narrative is retained where facts are not
- **Labor Illusion**: showing the work raises perceived value of the result

**Methods:** worked examples, annotated screenshots, explainer video, glossary, before-and-after comparison.

### Knowledge assumption
Assumes expertise and skips foundations -> assumes none, scaffolds fully.

**What it is:** How much the page assumes the reader already knows, and therefore how much
groundwork it lays before the substance.

- **Curse of Knowledge**
- **Mental Model**: build on what the user already believes is true
- **Jakob's Law**
- **Paradox of the Active User**: people will not read the explanation, however good it is
- **Dunning-Kruger Effect**: novices misjudge their own competence, so self-selected depth fails

**Methods:** onboarding tour, first-use inline hints, jargon removal pass, sample data, plain-language glossary.

### Format density
Undifferentiated prose -> tables, diagrams and step sequences.

**What it is:** How much structure the page gives its information, from continuous prose to
tables, diagrams and numbered steps.

- **Chunking**: grouping raises the amount that can be held
- **Law of Proximity**: nearness implies relationship
- **Law of Similarity**: shared appearance implies shared kind
- **Law of Common Region**: a shared boundary groups more strongly than proximity
- **Law of Prägnanz**: the simplest available reading is the one taken
- **Serial Position Effect**: first and last items are recalled, the middle is not

**Methods:** chunking, tables, comparison matrices, numbered steps, diagrams, whitespace grouping.

### Reference framing  *(new)*
Value stated in isolation -> framed against an explicit reference point.

**What it is:** Whether a value is left to stand on its own or is given a reference point to be
judged against.

- **Anchoring Bias**: the first number seen sets the scale for every number after it
- **Decoy Effect**: a third, deliberately inferior option changes which of the other two wins
- **Framing Effect**: gain-framed and loss-framed statements of the same fact are not equivalent
- **Contrast Effect**: value is judged relative to what sits beside it, not absolutely
- **Weber's Law**: a difference has to exceed a threshold before it registers at all

**Methods:** anchor price shown first, three-tier pricing with a decoy option, was-and-now pricing, comparison against the alternative, per-unit breakdown.

---

## Momentum

Keeping the user moving. Reduced from four levers to three: the old `Friction at moment of
action` was the same dimension as Ease's interaction cost, and `Step continuity` and
`Interruption frequency` were two halves of one thing.

### Urgency basis
No time or quantity pressure -> an authentic hard constraint.

**What it is:** What, if anything, makes acting now better than acting later, and whether that
constraint is real.

- **Scarcity** *(Cialdini)*: limited availability raises perceived value
- **Loss Aversion**: urgency works by framing inaction as a loss
- **Hyperbolic Discounting**: a near reward outweighs a larger distant one
- **Salience** *(MINDSPACE)*: a deadline nobody notices applies no pressure
- **Reactance** *(counter)*: manufactured urgency, once detected, reverses the effect and
  damages Trust

**Methods:** real deadline, live stock count, cohort start date, offer with an honest expiry.

### Path integrity
State is lost between steps and exits are everywhere -> state carries forward and distractions
are removed.

**What it is:** How well a multi-step path holds the user's state and attention between one
step and the next.

- **Cognitive Load**: re-orientation at each step is pure overhead
- **Working Memory**: anything the user must hold between screens is at risk
- **Default Bias**: a carried-forward value is usually accepted
- **Selective Attention**: competing elements pull attention off the path
- **Decision Fatigue**: every incidental decision spends a finite budget
- **Goal Gradient Effect**: effort rises as the goal nears, so late friction costs most
- **Flow**: the absorbed state these principles combine to produce: challenge matched to skill,
  uninterrupted, with immediate feedback. An outcome rather than a dial, kept here because it
  names what the lever is aiming at

**Methods:** autosave, carried-forward state, navigation removed from checkout, single-column flow, resume where you left off.

### Forward pull  *(new)*
Nothing draws the user to the next step -> each step opens a loop the next one closes.

**What it is:** How much each step does to make the next one wanted rather than merely
available.

- **Curiosity Gap**: a known gap in knowledge compels closing
- **Zeigarnik Effect**: incomplete tasks stay mentally active
- **Variable Reward**: unpredictable payoff sustains engagement past novelty
- **Goal Gradient Effect**: visible proximity to the goal accelerates effort
- **Fresh Start Effect**: a temporal landmark restarts motivation

**Methods:** nudge, juxtaposition of current state against desired state, teaser of the next step, partially revealed content, next-up prompt, unlockables, streak prompt.

---

## Ease

Reducing the effort required to act. `Physical effort` renamed to `Interaction cost`, the
established term, and it now absorbs Momentum's friction lever. `Intent accommodation` added
21 September 2026, distinct from `Expertise accommodation`, which is about skill growing over
repeated use rather than differing intent on a first visit.

### Cognitive demand
User evaluates many options and makes many decisions -> defaults handle most, the user acts on
exceptions.

**What it is:** How many judgements the page leaves to the user, against how many its defaults
have already made.

- **Hick's Law**: decision time rises with the number and complexity of choices
- **Choice Overload**: beyond a point more options reduce action and satisfaction
- **Cognitive Load**
- **Decision Fatigue**
- **Defaults** *(MINDSPACE)* / **Default Bias**: most people never change a default
- **Satisficing**: users take the first adequate option, not the best one
- **Compensatory vs Noncompensatory Strategies**: under load, users drop to single-attribute
  elimination rather than weighing trade-offs

**Methods:** sensible defaults, one option flagged as recommended, reduced option count, smart filtering, progressive choice.

### Interaction cost
Many taps, clicks or fields to reach the goal -> minimum gestures, pre-fill and autofill.

**What it is:** How much physical work reaching the goal takes: the taps, the fields, and
everything the user has to supply themselves.

- **Interaction Cost**: the sum of physical and mental effort to reach a goal
- **Fitts's Law**: acquisition time depends on target size and distance
- **Tesler's Law**: irreducible complexity sits either with the system or the user
- **Decision Sludge**: friction that serves the organisation rather than the user
- **Doherty Threshold**: below 400ms the interaction holds attention

**Methods:** autofill, single sign-on, larger tap targets, fewer form fields, one-click repeat actions, address lookup.

### Memory load
User must recall from earlier or from outside the system -> the system surfaces what is needed.

**What it is:** How much the user has to hold in their head, against how much the system puts
back in front of them.

- **Recognition Over Recall**: recognising is far cheaper than retrieving
- **Working Memory**: capacity is small and decays in seconds
- **Miller's Law**
- **Spatial Memory**: people remember where things were, so stable position is a memory aid
- **Serial Position Effect**

**Methods:** recently viewed, saved items, earlier answers shown inline, persistent summary panel, autocomplete.

### Error recovery
Errors punish, the form clears, the process restarts -> inline correction with input preserved.

**What it is:** What a mistake costs, from losing the work and starting again to correcting it
in place.

- **Postel's Law**: be liberal in what you accept
- **Negativity Bias**: a bad moment weighs more than several good ones
- **Peak-End Rule**: the worst moment and the last moment define the memory
- **Loss Aversion**: losing entered work is felt as a real loss
- **Reactance**: blame-assigning error copy provokes resistance

**Methods:** inline validation with input preserved, undo, draft autosave, forgiving input parsing, a clear next step inside the error.

### Expertise accommodation  *(new)*
The same path for everyone forever -> accelerators and shortcuts appear as skill grows.

**What it is:** Whether the path stays the same for everyone forever, or opens shortcuts as the
user gets better at it.

- **Power Law of Learning**: task time falls predictably with practice, and a fixed path caps it
- **Paradox of the Active User**: people never go looking for the faster route
- **Spacing Effect**: repeated exposure over time is what builds the skill
- **Recognition Over Recall** *(counter)*: shortcuts that must be recalled are used by almost
  nobody

**Methods:** keyboard shortcuts, command palette, bulk actions, saved views, templates, API access.

### Intent accommodation  *(new)*
One path serves every visitor -> parallel routes matched to the intent the visitor arrived with.

**What it is:** Whether the page offers a single way forward for everyone, or several that lead
to genuinely different destinations, matched to the state the visitor arrived in. Two routes to
the same destination do not move this lever.

- **Jakob's Law**: visitors expect the route they already know from elsewhere in the category
- **Information Scent**: a second route only works if its label says where it goes, or it reads
  as a weaker version of the first
- **Decision Sludge**: friction that serves the organisation rather than the user, which is what
  a single route becomes when it was chosen for internal reasons
- **Reactance**: being funnelled into the only available route provokes resistance in the
  visitor it was not built for
- **Satisficing**: people take the first adequate route rather than the best one, so ordering
  and prominence decide which gets used
- **Hick's Law** *(counter)*: decision time rises with the number and complexity of choices
- **Choice Overload** *(counter)*: beyond a point more options reduce action and satisfaction,
  so every added route costs certainty on the primary one

**Methods:** parallel primary and secondary calls to action, entry points by starting material, route selection ahead of a form, a named alternative channel, separate templates per intent.

---

## Validation

Signals from others, and from the system, that the user is choosing correctly. Now owns all
social proof, including the two levers that were sitting in Trust. `Proof proximity` and
`Social distance of source` were the same dimension and are merged.

### Source similarity
A distant celebrity or a generic customer -> a near-peer in the user's exact role and situation.

**What it is:** How close the people vouching for the product are to the person reading, in
role and in situation.

- **Social Proof** *(Cialdini)*: proof from similar others is materially stronger than proof
  from dissimilar ones
- **Liking** *(Cialdini)*: similarity produces liking, and liking produces compliance
- **Unity** *(Cialdini)*: shared identity is stronger still than similarity
- **Messenger** *(MINDSPACE)*: who says it changes whether it lands
- **Group Attractiveness Effect**: a group is rated above the average of its members

**Methods:** role-filtered testimonials, industry case studies, named job titles, customer logos by sector.

### Proof scale
A single testimonial -> an aggregate crowd signal.

**What it is:** Whether the evidence is one person's account or the weight of a crowd.

- **Social Proof** *(Cialdini)*
- **Bandwagon Effect**: adoption rises with visible adoption
- **Norms** *(MINDSPACE)*: stating what most people do changes what people do
- **Unit Bias**: a stated total is taken as the appropriate amount
- **Singularity Effect** *(counter)*: one identified individual moves people more than a
  statistic, so scale can be the weaker pole

**Methods:** usage counts, aggregate review score, live activity counts, adoption statistics.

### Verification level
Unattributed claim -> platform-verified or independently audited. Absorbs Trust's old
`Signal source`.

**What it is:** How much of the proof is checkable, from a claim the page makes about itself to
one an outside party has confirmed.

- **Authority** *(Cialdini)* / **Authority Bias**: credentials are taken as a shortcut to truth
- **Halo Effect**: a known certifier's reputation transfers to the claim
- **Noble Edge Effect**: demonstrated social responsibility raises credibility generally
- **Messenger** *(MINDSPACE)*

**Methods:** verified-purchase badges, third-party review widgets, audit certifications, named and attributed quotes.

### System validation  *(new)*
No confirmation the action registered -> immediate, specific confirmation of what happened.

**What it is:** How clearly the system confirms that what the user just did actually
registered.

- **Feedback Loop**: action without response reads as failure
- **Response Time Limits**: 0.1s feels instant, 1s holds flow, 10s loses attention
- **Doherty Threshold**
- **Zeigarnik Effect**: an unconfirmed action stays an open loop
- **Peak-End Rule**: confirmation is often the end the whole task is remembered by

**Methods:** success toasts, inline confirmations, receipt screens, status indicators, completion confirmation.

---

## Identity

Aligning with who the user believes they are or wants to be.

### Self alignment target
Appeals to the actual current self -> appeals to the aspirational self.

**What it is:** Which version of the reader the page speaks to: the one they are now, or the
one they would like to be.

- **Ego** *(MINDSPACE)*: people act in ways that support a good self-image
- **Cognitive Dissonance**: a gap between self-image and action must resolve one way or other
- **Barnum-Forer Effect**: general statements are read as personally specific
- **Halo Effect**

**Methods:** aspirational imagery, values-led copy, outcome framing, designed-for-X positioning.

### Group signal breadth
Universal positioning, "for everyone" -> tribal specificity, explicitly for a defined in-group.

**What it is:** How specifically the page names who it is for, from everyone to a defined in-
group.

- **Unity** *(Cialdini)*: shared identity, not just similarity
- **Group Attractiveness Effect**
- **Norms** *(MINDSPACE)*
- **In-group Bias**: membership itself changes evaluation
- **Spotlight Effect**: people overestimate how much others notice their choices

**Methods:** named audience in the headline, community spaces, segment-specific landing pages, in-group language.

### Commitment depth
No identity commitment asked -> an explicit declaration or joining act.

**What it is:** How much of an identity commitment the page asks for, from none at all to an
explicit act of joining.

- **Commitment and Consistency** *(Cialdini)*: a small stated commitment predicts a larger one
- **Commitments** *(MINDSPACE)*: a promise made, and especially one made in public, pulls later
  behaviour into line with it
- **Cognitive Dissonance**: the declaration pulls behaviour into line
- **IKEA Effect**: self-assembled things are valued above their objective worth
- **Reactance** *(counter)*: demanding a declaration too early reads as a price, not a choice

**Methods:** role selection at signup, goal setting, profile completion, a public pledge or plan.

### Identity continuity
A one-off transactional moment -> an ongoing marker, tier or earned status.

**What it is:** Whether the relationship ends with the transaction or leaves a standing marker
the user carries forward.

- **Endowment Effect**: accumulated status is owned, and giving it up is a loss
- **Sunk Cost Effect**: invested history keeps people in
- **IKEA Effect**
- **Ego** *(MINDSPACE)*
- **Unity** *(Cialdini)*

**Methods:** tiers and levels, badges, membership number, anniversary moments, visible saved history.

---

## Orientation

Telling the user where they are, what they can do, and what matters now. `Next action clarity`
and `Visual priority hierarchy` were the same dimension and are merged into `Action priority`.

### Location signal
No indication of where the user is -> explicit position at every level.

**What it is:** How clearly the page tells the user where they currently are within it.

- **Spatial Memory**: people navigate by remembered position, so stability is the mechanism
- **Serial Position Effect**
- **Mental Model**: the user's map of the system, which the signal either confirms or breaks
- **Law of Common Region**: a bounded area reads as "the place you are in"

**Methods:** breadcrumbs, step indicators, section headers, active navigation state, page titles.

### Information scent  *(new)*
Links and labels give no clue what lies behind them -> every path signals its destination.

**What it is:** How much a link or a label tells the user about what they will find behind it.

- **Information Scent**: users judge a link by how strongly it smells of the goal
- **Information Foraging**: users abandon a patch when scent weakens, not when content runs out
- **Mental Model**
- **Curiosity Gap** *(counter)*: deliberately weak scent buys a click and spends trust

**Methods:** descriptive link text, section previews, category descriptions, result counts, hover previews.

### Action priority
Every option carries equal weight and the next step must be found by scanning -> one primary
action, unmistakably weighted.

**What it is:** How unequally the page weights its options, from all of them alike to one
unmistakable next move.

- **Von Restorff Effect**: the item that differs is the item remembered and chosen
- **Centre-Stage Effect**: the middle item in a row is disproportionately picked
- **Selective Attention**: users see what they are looking for and little else
- **Salience** *(MINDSPACE)*
- **Law of Prägnanz**: the simplest reading of the hierarchy is the one taken

**Methods:** a single primary button, suppressed secondary actions, size and colour weighting, placement in the reading path.

### Context persistence
Returns to a blank or reset state -> the system restores where the user was.

**What it is:** Whether coming back starts from scratch or picks up where the user left off.

- **Spatial Memory**
- **Working Memory**: anything not restored has to be reconstructed
- **Zeigarnik Effect**: an interrupted task is still live in the user's head
- **Default Bias**
- **Endowment Effect**: saved work is owned work

**Methods:** session restore, saved filters and sorts, back-navigation state, draft recovery.

---

## Personalisation

Adapting to what the system knows about the user. The thinnest theme in the library: two levers
of its own plus one shared with Control. `Adaptation basis` and `Depth of adaptation` were the
same spectrum and are merged. `Signal source` renamed to `Inference source` to end the name
collision with Trust's old lever.

### Adaptation depth
Identical for every user -> structurally different flows, hierarchies and defaults per segment.

**What it is:** How far the experience differs between one user and another, from identical to
structurally different.

- **Barnum-Forer Effect**: surprisingly general content is read as personally specific, which is
  why shallow personalisation often outperforms its cost
- **Ego** *(MINDSPACE)*
- **Familiarity Bias**: adapted content feels known, and known feels correct
- **Endowment Effect**: a shaped environment becomes the user's own
- **Filter Bubble** *(counter)*: narrowing to inferred preference removes the discovery that
  made the product valuable

**Methods:** recommended content, role-based dashboards, segment-specific defaults, adaptive navigation.

### Inference source
Explicitly stated preferences only -> passively inferred from behaviour and history.

**What it is:** Where the personalisation gets its information: what the user said, or what the
user did.

- **Reactance**: inference the user did not consent to reads as surveillance
- **Negativity Bias**: one uncomfortable inference outweighs many accurate ones
- **Default Bias**: an inferred default is accepted far more often than a stated preference is set
- **Labor Illusion**: showing the inference working makes it feel earned rather than taken

**Methods:** onboarding preference questions, explicit interest picker, behaviour-based recommendations, an editable preferences surface.

### Decision transparency
*Shared with Control. See Control below.*

---

## Control

Meaningful agency over environment, output and data. `Scope of agency` and `Override
availability` were the same dimension and are merged.

### Configurability
The system dictates outputs and defaults are locked -> the user can override any meaningful
parameter.

**What it is:** How much of the system's behaviour the user is allowed to change.

- **Autonomy** *(Self-Determination Theory)*: control is a basic motivational need, not a
  preference
- **Reactance**: removing an option produces desire for it
- **IKEA Effect**: a configured environment is valued above an equivalent given one
- **Default Bias** *(counter)*: most users will never touch any of it, so defaults still carry
  the experience
- **Paradox of the Active User** *(counter)*: configuration that must be discovered is not found

**Methods:** settings, theme choice, notification controls, custom views, reorderable elements.

### Reversibility
Actions are permanent or hard to undo -> undo is always one step away.

**What it is:** How easily an action can be taken back once it has been done.

- **Loss Aversion**
- **Zero Risk Bias**: complete reversibility is valued out of proportion to the actual risk
- **Negativity Bias**
- **Postel's Law**
- **Reactance**

**Methods:** undo, trash with restore, version history, edit after submit, cancel an in-flight action.

### Decision transparency
*(shared with Personalisation)*
The system decides opaquely -> every automated decision is explainable.

**What it is:** How much the system explains about the decisions it made on the user's behalf.

- **Labor Illusion**: visible reasoning raises perceived quality of the output
- **Trust and Credibility**
- **Reactance**: an unexplained decision is experienced as one imposed
- **Backfire Effect** *(counter)*: a poorly framed explanation entrenches disagreement rather
  than resolving it
- **ELIZA Effect**: people over-attribute understanding to systems that appear to reason

**Methods:** why-am-I-seeing-this explanations, ranking rationale, confidence indicators, source citations, user-adjustable weightings.

### Data portability and exit  *(new)*
Data is locked in with no way to leave -> export, delete and leave at any time.

**What it is:** How freely the user can take their data and leave.

- **Endowment Effect**: accumulated data is owned, and lock-in is felt as confiscation
- **Loss Aversion**
- **Sunk Cost Effect** *(counter)*: lock-in retains commercially and costs in trust
- **Autonomy** *(Self-Determination Theory)*
- **Reactance**

**Methods:** CSV or JSON export, account deletion, full data download, cancellation without a retention flow.

---

## Delight

Craft beyond the functional task.

### Expectedness
Anticipated or conventional -> genuinely surprising in timing and form.

**What it is:** How far the moment departs from what the user was expecting, in timing as well
as in form.

- **Von Restorff Effect**
- **Expectations Bias**: surprise only exists relative to a set expectation
- **Variable Reward**: unpredictability sustains what predictability habituates
- **Peak-End Rule**: a surprise is a candidate peak
- **Affect** *(MINDSPACE)*: emotional state changes judgement of everything around it

**Methods:** unexpected animation, easter eggs, celebratory moments, surprising empty states, personality in error copy.

### Processing level
Visceral only, a good-looking moment that fades -> reflective, connected to the user's
self-narrative.

**What it is:** How deep the pleasure goes: a good-looking moment, or something that connects
to how the user sees themselves.

- **Three Levels of Emotional Processing**: visceral, behavioural and reflective, and only the
  third is retold to other people
- **Aesthetic-Usability Effect**: attractive interfaces are perceived as easier to use
- **Sensory Appeal**: texture, sound, weight and motion are processed before any of it is read,
  and they set the emotional tone the rest of the page is judged against
- **Storytelling Effect**
- **Ego** *(MINDSPACE)*

**Methods:** original illustration, distinctive voice, meaningful sound, narrative onboarding.

### Longevity
One-time novelty that habituates after first exposure -> new layers revealed over time.

**What it is:** Whether the moment is spent on first exposure or keeps returning something on
the visits after it.

- **Hedonic Adaptation**: response to a fixed stimulus decays to baseline
- **Variable Reward**
- **Spacing Effect**
- **Curiosity Gap**
- **Familiarity Bias** *(counter)*: some things should habituate, and novelty in a core path is
  a cost

**Methods:** seasonal variation, details unlocked over time, rotating copy, evolving illustration.

### Functional integration
Decorative, remove it and nothing changes -> serves a purpose, communicates state or reduces
anxiety.

**What it is:** Whether the flourish is doing a job as well as being one, such as showing state
or easing a wait.

- **Aesthetic-Usability Effect**
- **Feedback Loop**
- **User Delight Pillars**: delight that resolves a real friction outlasts delight that decorates
- **Affect** *(MINDSPACE)*

**Methods:** loading animation that communicates state, success animation confirming the action, motion showing where something went.

---

## Progress

Making advancement visible.

### Progress visibility
No indication the user is advancing -> a continuously visible metric.

**What it is:** How visible advancement is while it is happening, rather than only once it is
finished.

- **Goal Gradient Effect**: effort accelerates as the goal comes into view
- **Zeigarnik Effect**
- **Feedback Loop**
- **Salience** *(MINDSPACE)*

**Methods:** progress bar, step counter, completion percentage, checklist.

### Starting position
Begins at zero, so the distance feels maximal -> pre-seeded at a non-zero point.

**What it is:** Where the count begins, and therefore how far the user believes they still have
to go.

- **Endowed Progress Effect**: artificial initial progress substantially raises completion
- **Goal Gradient Effect**
- **Commitment and Consistency** *(Cialdini)*
- **Sunk Cost Effect**

**Methods:** first step pre-completed, profile-percentage framing, pre-filled fields counted as progress, loyalty card issued with stamps already on it.

### Reward cadence
Acknowledgement only at final completion -> micro-acknowledgements at every step.

**What it is:** How often the system acknowledges progress, from once at the end to something
at every step.

- **Variable Reward**: an unpredictable schedule sustains behaviour longer than a fixed one
- **Shaping**: reinforcing successive approximations rather than only the finished behaviour
- **Incentives** *(MINDSPACE)*: people respond to rewards in predictable but non-linear ways, and
  a small reward given now outweighs a larger one given later
- **Hyperbolic Discounting**: a near, small reward beats a distant, large one
- **Peak-End Rule**

**Methods:** step confirmations, micro-celebrations, incremental unlocks, milestone messages.

### Granularity
Binary, done or not done -> percentage, points, streak or level.

**What it is:** How finely progress is measured, from done or not done to a running score.

- **Weber's Law**: a change must exceed a proportional threshold before it is noticed, which is
  what makes a coarse bar feel stuck
- **Unit Bias**: a defined unit is taken as the right amount to complete
- **Pseudo-Set Framing**: arbitrary items grouped into a set create a drive to complete the set
- **Goal Gradient Effect**
- **Chronoception**: perceived duration, which granularity manipulates directly

**Methods:** percentage, points, streak counter, sub-steps within a step, levels.

---

## Clarity

Removing ambiguity about what an action will do.

### Action label specificity
Generic verb, "Submit" or "Continue" -> outcome-specific phrase, "Start my free trial".

**What it is:** How much a control's label says about what pressing it will actually do.

- **Information Scent**: a label is the scent for the action behind it
- **Framing Effect**
- **Curse of Knowledge**: internal vocabulary leaks into labels
- **Priming**: the label sets expectation for what follows

**Methods:** outcome-named buttons, verb-plus-object labels, cost stated on the button itself.

### Consequence preview
Outcome unknown until after commitment -> full outcome described before it.

**What it is:** How much the user knows about the outcome before they commit to it.

- **Feedforward**: showing what an action will do before it is taken
- **Loss Aversion**: uncertainty about cost is read as risk of loss
- **Cashless Effect**
- **Framing Effect**
- **Deceptive Patterns**: the named failure mode at the passive pole

**Methods:** charge stated before confirm, dialogs naming the effect, preview before publish, dry-run mode.

### Signifier strength
Affordance implied, no cue the element is interactive -> shape, colour or position states it
unambiguously.

**What it is:** How plainly an element announces that it can be interacted with.

- **Affordances and Signifiers**: the perceived action possibility versus the cue that
  advertises it
- **Jakob's Law**
- **Mental Model**
- **Banner Blindness**: anything shaped like an advert is not seen at all
- **Aesthetic-Usability Effect** *(counter)*: a beautiful control that reads as decoration is
  not used

**Methods:** button styling, underlined links, cursor changes, icon plus label, hover and focus states.

### Error prevention
Mistakes are discovered after the fact -> disabled states, format hints and inline validation.

**What it is:** How much the design does to stop a mistake happening, rather than reporting it
afterwards.

- **Postel's Law**
- **Cognitive Load**: validation after the fact forces reconstruction of intent
- **Negativity Bias**
- **Selective Attention**: a hint nobody looks at prevents nothing
- **Tesler's Law**

**Methods:** disabled until valid, format hints, input masks, constrained pickers, confirmation on destructive actions.

---

## How this library was built

The levers came first, written from design practice as 48 spectrums across the 12 themes. The
principles were then mapped onto them from the sources below, and the mapping was used to
validate the levers rather than just decorate them.

**The test: two levers that attract an identical set of principles are one lever.** That turned
seven suspected duplicates into merges without a judgement call. Momentum's "friction at moment
of action" and Ease's "physical effort" both returned interaction cost, Fitts, Tesler and sludge,
so they are one lever. Reuse this test whenever the library is revised.

The same pass ran in reverse. Principles that fit no lever pointed at dimensions that were
missing, which is how `Reference framing` and `Exchange order` arrived: anchoring, the decoy
effect and reciprocity are among the strongest effects in the set and the original 48 had nowhere
to put any of them.

The result was 48 levers again, but a substantially different 48: seven merges, two moves, two
renames and nine additions. Six of the additions came from theme definitions in `analyse-themes`
describing something no lever covered. Delight, Progress and Clarity came through untouched.

Trust and Validation were separated in the process. Everything social moved to Validation, and
Trust keeps risk, transparency and reliability. The two had been overlapping since the first
pass.

---

## Excluded, and why

Roughly 40 entries from the source lists are deliberately absent.

**Practitioner biases.** These act on the designer or researcher, not on the user of the
interface: Law of the Instrument, Survivorship Bias, Survey Bias, Observer-Expectancy Effect,
Hawthorne Effect, Hindsight Bias, False Consensus Effect, Self-Serving Bias. They belong in a
research-practice skill, not here.

**Methods, previously excluded, now reinstated as their own layer.** Progressive Disclosure,
Chunking, Visual Hierarchy, Provide Exit Points, Temptation Bundling, Investment Loops, Spark
Effect, External and Internal Triggers, Discoverability and Method of Loci are things a designer
does. That made them wrong as principles but right as methods, and they now sit on the
`**Methods:**` line of the levers they move. Nudge and Juxtaposition are both under Momentum's
`Forward pull`: a nudge makes the next step the path of least resistance, and juxtaposition sets
current state beside desired state so the gap itself does the pulling. Only Skeuomorphism stayed
out, as a style choice rather than a lever move.

**States and outcomes.** The Aha! moment is designed toward, not dialled. Flow was excluded on
the same reasoning and has been put back under Momentum's `Path integrity`, labelled as the
outcome those principles produce, because naming what a lever aims at is worth more than the
consistency of the rule.

**Design heuristics without a psychological mechanism.** Occam's Razor, Pareto Principle,
Parkinson's Law.

**Low design leverage.** Availability Heuristic, Change Blindness, Streisand Effect and
Spotlight Effect are real but rarely give a designer anything to move.

---

## Known weak points

Stated plainly so they are corrected rather than inherited.

- **The 12 themes are a first pass too.** Trust and Validation needed separating in this
  revision and the same may be true elsewhere. EAST (Easy, Attractive, Social, Timely, from the
  UK Behavioural Insights Team) sits at theme altitude rather than lever altitude and is the
  obvious cross-check when the theme vocabulary is next revised.
- **Methods are the least researched layer.** Principles came from four curated sources. Methods
  were written from practice. They are the layer most likely to be wrong and the cheapest to fix.
- **Personalisation is thin**, at two levers of its own plus one shared, against four or five
  elsewhere. This looks like a property of the theme rather than a gap in the library, but it
  has not been tested.
- **Nothing here has been validated against outcomes.** The principles are well evidenced
  individually. Their assignment to these particular levers is a considered mapping, not a
  measured one.

---

## Sources

- Growth.design, *106 Cognitive Biases and Principles That Affect Your UX*: used as an index of
  names. Roughly 45 of its 114 entries have written content, the rest are stubs. Its four
  categories classify by which cognitive problem a bias solves, which is the wrong axis for this
  mapping, so only the item list was used.
- Laws of UX, Jon Yablonski, canonical names, tightly curated.
- Nielsen Norman Group, *Psychology for UX: Study Guide*: the most rigorous source, and the only
  one covering information scent and foraging, self-determination theory, interaction cost,
  decision sludge and the three levels of emotional processing.
- Cialdini's seven principles of persuasion.
- MINDSPACE, Behavioural Insights Team, the one diagnostic framework included, because unlike
  Fogg's B=MAP, COM-B and EAST its nine elements are dimensions rather than diagnoses.

Excluded as sources: UX cognitive bias card decks, which are roughly half practitioner biases.
Fogg, COM-B and EAST, which diagnose rather than describe mechanisms. EAST is worth revisiting
later as a cross-check on the 12 themes, since Easy, Attractive, Social and Timely sit at theme
altitude rather than lever altitude.
