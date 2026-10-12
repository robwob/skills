# UX standards library

The bar `ux-review` measures a design against. Interaction and structure only: visual craft belongs
to `ui-review`, copy belongs to `content-review`.

**This is a first pass and is expected to change.** Adding or amending an entry follows the
approval process in `SKILL.md`. Nothing is written here without the maintainer's explicit approval.

---

## How this is structured

Every entry carries a tier. The tier decides the severity of a finding, so read it before writing one.

| Tier | What it is | A violation is |
|---|---|---|
| **Standard** | A published, citable requirement: a WCAG success criterion, or a regulation in force. Objectively testable. | A defect. Not a matter of taste, and not negotiable by preference. |
| **Evidence** | A quantified finding from a primary research source, with a sample size behind it. | A strong finding. Overriding it needs a stated reason. |
| **Convention** | Widely adopted practice, where established sources may disagree with each other. | A deviation. Fine if deliberate and applied consistently, a finding if accidental. |

Folklore is excluded. See **Excluded, and why** at the end: those entries are kept there
deliberately so nobody re-adds them.

### The boundary with `define-levers`

These two skills both touch usability, and the split is strict.

- `ux-review` owns **compliance**: is this broken against a bar that exists.
- `define-levers` owns **mechanism**: which dimension to dial, and the psychology explaining why
  moving it works.

A Law of UX that *explains* (Hick's, Fitts's, Jakob's, Peak-End, Von Restorff) is a `define-levers`
principle and does not belong here. A Law that *sets a testable threshold* (the Doherty threshold)
appears here. When a review finds a working design that could simply be a better bet, that is not a
finding, it is an angle: say so and hand off.

---

## 1. Nielsen's 10 usability heuristics

The structuring vocabulary for findings. Every UX finding should map to one of these, which is what
stops the report becoming an undifferentiated list. Definitions are Nielsen's own wording.

Source: <https://www.nngroup.com/articles/ten-usability-heuristics/> **[Convention]** as a framework,
though several individual heuristics have Standard-tier criteria sitting underneath them.

1. **Visibility of system status.** "The design should always keep users informed about what is
   going on, through appropriate feedback within a reasonable amount of time."
2. **Match between the system and the real world.** "The design should speak the users' language.
   Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow
   real-world conventions, making information appear in a natural and logical order."
3. **User control and freedom.** "Users often perform actions by mistake. They need a clearly marked
   'emergency exit' to leave the unwanted action without having to go through an extended process."
4. **Consistency and standards.** "Users should not have to wonder whether different words,
   situations, or actions mean the same thing. Follow platform and industry conventions."
5. **Error prevention.** "Good error messages are important, but the best designs carefully prevent
   problems from occurring in the first place. Either eliminate error-prone conditions, or check for
   them and present users with a confirmation option before they commit to the action."
6. **Recognition rather than recall.** "Minimize the user's memory load by making elements, actions,
   and options visible. The user should not have to remember information from one part of the
   interface to another."
7. **Flexibility and efficiency of use.** "Shortcuts, hidden from novice users, may speed up the
   interaction for the expert user so that the design can cater to both inexperienced and
   experienced users."
8. **Aesthetic and minimalist design.** "Interfaces should not contain information that is
   irrelevant or rarely needed. Every extra unit of information in an interface competes with the
   relevant units of information and diminishes their relative visibility."
9. **Help users recognize, diagnose, and recover from errors.** "Error messages should be expressed
   in plain language (no error codes), precisely indicate the problem, and constructively suggest a
   solution."
10. **Help and documentation.** "It's best if the system doesn't need any additional explanation.
    However, it may be necessary to provide documentation to help users understand how to complete
    their tasks."

---

## 2. Response time and feedback

**[Evidence]** The canonical thresholds. Miller (1968), restated by Nielsen, repeatedly re-confirmed.
Source: <https://www.nngroup.com/articles/response-times-3-important-limits/>

| Threshold | What happens | What the design must do |
|---|---|---|
| **0.1s** | Perceived as instantaneous | Nothing. A loader here is itself a defect, it makes the action feel slower than it is. |
| **1.0s** | Flow of thought uninterrupted. Noticeable, tolerable | No loader needed, but the result must actually arrive. |
| **10s** | Limit of attention. Users disengage | A progress indicator **with a time estimate**. A spinner alone is not sufficient past this point. |

**[Convention]** The Doherty threshold puts the productivity target at under 400ms. Useful as a
target, not as a pass/fail bar, since it comes from 1982 mainframe research.
Source: <https://lawsofux.com/doherty-threshold/>

A design that shows no state at all between an action and its result fails heuristic 1 regardless of
actual speed, because a static mock cannot make the wait visible.

---

## 3. Forms

Baymard's findings come from large-scale usability testing of real checkouts, which is why they are
Evidence tier rather than Convention.

- **Field count, not step count. [Evidence]** The average checkout carries about 11.3 fields where
  roughly 8 would do. Number of steps is a red herring; the field count is what degrades performance.
  Count the fields and ask which could be removed, derived, or deferred.
  <https://baymard.com/blog/checkout-flow-average-form-fields>
- **Labels above the field. [Evidence]** Placeholder-as-label causes hesitation, mistyping, and users
  clearing their own input just to re-read the label. Worse on mobile. Labels sit above the field,
  visible at all times, the single exception being mobile landscape.
  <https://baymard.com/blog/mobile-forms-avoid-inline-labels>
- **Inline validation, correctly timed. [Evidence]** 31% of sites have no inline validation, and
  about 20% of those that do get it wrong, either validating before the user has finished typing or
  failing to clear the error once it is fixed. Validate on blur, clear on correction.
  <https://baymard.com/blog/inline-form-validation>
- **Mark required and optional. [Evidence]** Only 14% of sites mark both. Marking only the optional
  fields caused 32% of users to fail to complete a required one. An asterisk alone is acceptable only
  if optional fields also carry "(optional)".
  <https://baymard.com/blog/required-optional-form-fields>
- **Dropdowns are not free. [Evidence]** A dropdown costs open, scroll, select. For a short list of
  mutually exclusive options, exposed radio buttons remove that cost.
  <https://baymard.com/blog/drop-down-usability>
  A widely circulated "25% fewer errors below 7 options" figure comes from Speero, not Baymard. Cite
  the direction, not that number.
- **Redundant Entry, 3.3.7, Level A. [Standard]** Information the user already entered in the same
  process must be auto-populated or offered for selection, unless re-entry is essential.

---

## 4. Errors, prevention and recovery

- **Undo for the frequent and reversible, confirm for the rare and irreversible. [Evidence]** They
  are complementary, not alternatives. <https://www.nngroup.com/articles/user-mistakes/>
- **Confirmation fatigue is real. [Evidence]** Habituation to repeated warnings is replicated in the
  security-warning literature, including fMRI evidence of declining neural response; in some studies
  users fail to read dialogue text more than half the time. A confirmation on a routine action does
  not prevent errors, it trains users to dismiss the one that mattered.
  <https://www.usenix.org/system/files/soups14-paper-bravo-lillo.pdf>
- **Dangerous proximity. [Evidence]** A destructive action placed next to a benign one, Delete beside
  Save, produces mis-clicks. Separate them, or weight them differently.
  <https://www.nngroup.com/articles/proximity-consequential-options/>
- **Error Prevention, 3.3.4, Level AA. [Standard]** For submissions that are legal, financial, or
  that modify user-controlled data, the action must be reversible, checked, or confirmed.

---

## 5. Interaction accessibility

The non-visual half. Visual accessibility, contrast and focus appearance, belongs to `ui-review`.

- **Focus Order, 2.4.3, Level A. [Standard]** Focus order preserves meaning and operability. It
  follows the logical and visual reading order, and does not jump.
- **Keyboard, 2.1.1, Level A, and No Keyboard Trap, 2.1.2, Level A. [Standard]** Every function is
  reachable and escapable by keyboard alone.
- **Focus Not Obscured (Minimum), 2.4.11, Level AA. [Standard]** *New in WCAG 2.2.* The focused
  component is not **entirely** hidden by author-created content. Sticky headers and cookie bars are
  the usual culprits. Partial obscuring passes; total obscuring fails.
- **Dragging Movements, 2.5.7, Level AA. [Standard]** *New in WCAG 2.2.* Anything operable by
  dragging must also be operable by a single pointer without dragging. Sliders, reorderable lists and
  drag-to-upload all need a non-drag path.
- **Consistent Help, 3.2.6, Level A. [Standard]** *New in WCAG 2.2.* Where a help mechanism repeats
  across pages, it appears in the same relative order.
- **Accessible Authentication (Minimum), 3.3.8, Level AA. [Standard]** *New in WCAG 2.2.* No
  cognitive function test (puzzle, memorised password recall without paste, transcription) unless an
  alternative or assistance exists. Blocking paste into a password field fails this.
- **Headings carry navigation. [Evidence]** In WebAIM's screen reader survey, about 72% of
  respondents navigate primarily by headings; only around 4% treat landmarks as their primary method.
  A correct heading hierarchy is higher leverage than landmark markup.
  <https://webaim.org/projects/screenreadersurvey10/>
- **No ARIA is better than bad ARIA. [Evidence]** WebAIM's survey of a million homepages found pages
  using ARIA averaged 41% **more** detected errors than pages without it. Use native semantic HTML
  first; ARIA is a last resort. <https://www.w3.org/TR/using-aria/>
- **Skip link. [Convention]** First tabbable element, visually hidden until focused, unmistakably
  visible when focused.

---

## 6. Information architecture

- **Dan Brown's eight principles. [Convention]** Objects, Choices, Disclosure, Exemplars, Front
  Doors, Multiple Classifications, Focused Navigation, Growth. Useful as a diagnostic vocabulary for
  structural findings.
- **Front doors. [Convention]** Roughly half of visitors do not arrive at the homepage, so every page
  must orient on its own rather than assume the user came through the front.
- **Breadth over depth. [Evidence, dated]** Larson and Czerwinski (CHI 1998) found broad-shallow
  hierarchies beat narrow-deep ones on search time, errors and felt lostness. This is 1990s desktop
  research and its transfer to small screens, where depth is often forced, is contested. Treat as
  directional. <https://www.humanfactors.com/newsletters/breadth_vs_depth_we_revisit_this_question.html>

---

## 7. Mobile and touch

- **Hidden navigation halves discoverability. [Evidence]** NN/g's controlled study, 179 participants
  across 6 sites, found visible navigation was found and used roughly 1.5x more than a hamburger on
  mobile, and hidden navigation was missed almost twice as often on desktop. This is a real
  quantitative study, not the usual hamburger opinion piece.
  <https://www.nngroup.com/articles/hamburger-menus/>
- **Gestures are an accelerator, never the only path. [Evidence]** A gesture has no visible
  affordance and must be learned. Anything achievable only by swipe, long-press or pinch needs a
  visible equivalent. <https://www.nngroup.com/articles/iphone-x/>
- **Thumb zones. [Evidence, single study]** Hoober's field observation of about 1,300 users found
  roughly 49% one-handed use and about 75% of interactions thumb-driven, producing the familiar
  reach-zone model. One field study rather than a replicated body of work, so treat the zone
  boundaries as approximate and the direction, primary actions within easy reach, as sound.

---

## 8. Cognitive load

- **Progressive disclosure. [Convention]** Defer advanced or rarely used functions to a secondary
  surface so the primary one stays simple. The "30 to 50% faster completion" figures attached to this
  online are unsourced; state the principle, never that number.
- **Defaults decide outcomes. [Evidence]** Johnson and Goldstein (Science, 2003) found opt-out organ
  donation systems produce over 90% participation against roughly 10 to 15% for opt-in, on
  populations with the same underlying values. Every pre-selected option in a design is a decision
  made on the user's behalf, so check that each default is the one that serves them.

---

## 9. Required states

A flow is not designed until each state is. Missing states are the most common structural gap in a
design handed over for review, and the easiest to check.

For every screen that loads, submits, or lists anything, confirm the design covers: **empty**
(first-run, and emptied-by-the-user, which are different), **loading**, **partial or slow**,
**error** (both recoverable and terminal), **success or confirmation**, **offline** where relevant,
and **maximum content** (long strings, large counts, the overflow case).

**[Evidence]** An empty state must say why there is nothing here and what to do next, not merely show
a blank panel. <https://www.nngroup.com/articles/empty-state-interface-design/>

---

## 10. Deceptive design

**[Standard]** EU Digital Services Act, Article 25, in force. Prohibits interfaces that deceive,
manipulate, or otherwise materially distort or impair a user's ability to make free and informed
decisions. Enforcement is live: X was fined 120M EUR in December 2025, in part over a deceptive
verification badge design.

Flag on sight: pre-ticked consent, a cancellation path materially harder than the signup path,
confirmshaming, false urgency with no real deadline, costs disclosed only at the final step,
a visually suppressed decline option beside an emphasised accept.

**Do not cite the FTC "click-to-cancel" rule as being in force.** It was vacated by the Eighth
Circuit in 2025. Many sources still describe it as active law. The FTC continues to act under Section
5, so the underlying practice remains actionable, but the rule itself is not current.

---

## Excluded, and why

Kept so they are not re-added.

- **Laws of UX as a whole.** Owned by `define-levers` as its principle library. Importing it here
  would duplicate that layer and blur compliance into strategy. Only the Doherty threshold appears
  here, because it states a number.
- **"Users only read 20% of a page."** Real finding, but it governs copy, so it lives in
  `content-review`.
- **"Progressive disclosure improves task completion by 30 to 50%."** Unsourced restatement, no
  traceable original.
- **"Three clicks to anything."** No supporting evidence; repeatedly contradicted. Click count does
  not predict success, information scent does.
- **The Speero "25% fewer errors" radio-versus-dropdown figure.** Secondary source presented widely
  as Baymard's. The direction holds, the number is not ours to quote.

## Sources

Nielsen Norman Group, Baymard Institute, W3C WAI (WCAG 2.2), WebAIM screen reader survey and
homepage accessibility analysis, Dan Brown's eight principles of information architecture, Larson and
Czerwinski (CHI 1998), Johnson and Goldstein (Science, 2003), Bravo-Lillo et al. (SOUPS 2014),
European Parliament research on the Digital Services Act. Individual URLs sit with each entry above.
