# Content standards library

The bar `content-review` measures a design against. Words only: interaction belongs to `ux-review`,
visual craft belongs to `ui-review`.

**This is a first pass and is expected to change.** Adding or amending an entry follows the approval
process in `SKILL.md`. Nothing is written here without the maintainer's explicit approval.

---

## How this is structured

Every entry carries a tier. The tier decides the severity of a finding.

| Tier | What it is | A violation is |
|---|---|---|
| **Standard** | A published, citable requirement, in practice a WCAG success criterion that is really a content rule. | A defect. |
| **Evidence** | A quantified finding from a primary research source. | A strong finding. Overriding it needs a stated reason. |
| **Convention** | Widely adopted practice, where established systems disagree with each other. | A deviation. Fine if deliberate and consistent, a finding if accidental. |
| **Voice** | The product's own declared voice and tone. Judged against what the product says it is, not against a universal bar. | Only a finding where a declared voice exists to breach. |

Folklore is excluded. See **Excluded, and why**.

**The trap this library exists to avoid:** content review collapses very easily into "I would have
written it differently." Preference is not a finding. If a rewrite cannot be tied to an entry here, it
is a suggestion, and it goes in a separate section labelled as such.

---

## 1. Plain language

- **Reading age around 9. [Convention]** GOV.UK's target, on the basis that this is the point at which
  a core vocabulary of roughly 5,000 words is recognised on sight. It is not writing for children: it
  is writing that a distracted, stressed or unfamiliar reader can process on one pass.
  <https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/>
- **Sentences over 25 words. [Convention]** GOV.UK: "Check sentences with more than 25 words to see if
  you can split them." A check, not a hard cap.
- **Common words over formal ones. [Convention]** GOV.UK's A to Z gives the substitutions: buy not
  purchase, help not assist, about not approximately, use not utilise. The test is whether the reader
  would say the word out loud.
  <https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/>
- **Active voice, and a named actor.** "We'll email you a receipt" over "A receipt will be sent."
  Passive constructions hide who is doing what, which matters most in exactly the places it is most
  common: errors, legal text and consequences.
- **One idea per sentence, one topic per paragraph. [Convention]** Structural, not numeric. There is no
  sourced paragraph word-count limit, and anything quoting one is folklore.

---

## 2. Scannability

- **People read roughly 20 to 28% of the words. [Evidence]** Nielsen's measurement of average page
  visits. Copy written to be read in full will not be.
  <https://www.nngroup.com/articles/website-reading/>
- **79% scan, about 16% read word by word. [Evidence]** From the same body of eye-tracking work.
- **The F-pattern. [Evidence]** Gaze traces two horizontal stripes and a left vertical stripe. What
  sits top-left and at the start of each line does the work.
- **Front-load. [Evidence, and directly testable]** The load-bearing word goes in the first three to
  five words of a heading, bullet or sentence. Scanners read line beginnings and stop. Test it by
  reading only the first few words of every line and asking whether the page still makes sense.
- **Headings must survive being read alone. [Evidence]** A reader taking only the headings should get
  the gist. "Overview" and "More information" fail this; they occupy the position that does the most
  work and say nothing.

---

## 3. Microcopy

- **Buttons name the action, verb first. [Convention]** "Save changes", "Book appointment", not "OK",
  "Submit" or "Continue" where something more specific is true. The label should make sense read on
  its own, because that is how it is encountered.
- **The label must match what happens.** A button saying "Save" that also publishes is a defect, not a
  wording preference.
- **Sentence case for buttons and UI labels. [Convention, contested]** Shopify Polaris specifies
  sentence case with a strong leading verb. Material's older spec used uppercase buttons. **These
  genuinely disagree.** Treat capitalisation as system-dependent: the finding is inconsistency within
  one product, never deviation from one particular system.
  <https://polaris-react.shopify.com/content/fundamentals>
- **Placeholder text is not a label. [Evidence]** It disappears on focus, burdens short-term memory,
  breaks error checking and re-reading, and is worse for users with visual or cognitive impairments.
  Labels stay visible above the field. Placeholders carry format hints only, and only if genuinely
  needed. <https://www.nngroup.com/articles/form-design-placeholders/>
- **Helper text is distinct from both.** If it explains why something is asked for, or the format
  expected, it is persistent helper text, not a placeholder.
- **Microcopy is interface text under about three sentences. [Convention]** Past that it is content and
  needs structure, not just wording.

---

## 4. Error messages

**[Evidence]** Nielsen's anatomy, all five required. A message missing any one of these is a finding.

1. **Explicit.** The reader can tell an error occurred.
2. **Human-readable.** Plain language. No codes, no jargon, no stack traces.
3. **Precise.** Says exactly what is wrong, not that something is.
4. **Polite.** Does not blame the reader. "Invalid input" blames; "That postcode wasn't found" does not.
5. **Constructive.** Says how to fix it. This is the one most often missing.

<https://www.nngroup.com/articles/error-message-guidelines/> and the scoring rubric at
<https://www.nngroup.com/articles/error-messages-scoring-rubric/>, which is directly reusable.

Placement and pairing, **[Evidence]**: the message sits next to the thing that caused it, and is
carried by text as well as colour. A red border alone fails WCAG 1.4.1, which makes it a `ui-review`
Blocker as well as a content gap here. <https://www.nngroup.com/articles/errors-forms-design-guidelines/>

---

## 5. Empty, loading and success states

**[Evidence]** An empty state says three things: why there is nothing here, what would put something
here, and what to do next. A blank panel, or one saying only "No results", does none of them.
<https://www.nngroup.com/articles/empty-state-interface-design/>

Distinguish the two empty states, because they need different copy: **first-run**, where the reader
has never had data, and **emptied**, where a filter or a deletion cleared it. Treating both with one
message serves neither.

Success copy confirms what actually happened and what follows, not merely that something worked.
"Payment received, your order ships Tuesday" over "Success!"

---

## 6. Accessible language

- **Link Purpose (In Context), 2.4.4, Level A. [Standard]** Link purpose is determinable from the link
  text, or from the text plus its immediate programmatic context.
- **Link Purpose (Link Only), 2.4.9, Level AAA. [Standard]** Link text alone conveys purpose.
- **Failure F84. [Standard]** Non-specific link text, "click here", "read more", "learn more",
  especially repeated across a page. Screen reader users navigate by a list of links, where a page of
  identical "read more" entries is unusable. **Directly testable:** extract every link, and flag any
  two with identical text pointing at different destinations, and any link whose text does not name
  its destination. <https://www.w3.org/TR/WCAG20-TECHS/F84.html>
- **Non-text Content, 1.1.1, Level A. [Standard]** Meaningful images carry alt text conveying the
  equivalent information. Decorative images take `alt=""`. Functional images, an icon button, describe
  **the action, not the appearance**: a magnifier icon is "Search", not "magnifying glass". Alt text is
  content, which is why it is reviewed here rather than in `ui-review`.
- **Sensory characteristics, 1.3.3, Level A. [Standard]** Instructions do not rely solely on shape,
  colour, size or position. "Click the green button on the right" fails; "Select Continue" does not.
- **Inclusive language.** Avoid ability-based idiom where a plain alternative exists, and avoid
  gendered defaults for unknown people. This is a real editorial bar, but it is not a WCAG criterion,
  so report it as Convention.

---

## 7. Terminology consistency

**[Method, not a threshold]** There is no numeric standard. The check is a content audit, and it is
mechanical enough to be reliable:

1. Extract every UI string: headings, labels, buttons, helper text, errors, nav items.
2. Group them by the concept they name.
3. Flag every concept named two or more ways. "Account" and "Profile", "Delete" and "Remove", "Sign
   in" and "Log in" for the same action.
4. Flag the reverse too: one word doing two jobs.

A product that calls the same object three names has three objects as far as the reader is concerned.

---

## 8. Voice and tone

**[Voice tier]** Judged against a declared voice, if one exists. With no declared voice there is
nothing to breach, and the only findings available are consistency ones.

The published systems worth reading, all qualitative rather than pass/fail:

- **Mailchimp** separates voice, which is constant, from tone, which shifts with the reader's
  emotional state. Their principles: clear, useful, friendly, appropriate.
  <https://styleguide.mailchimp.com/voice-and-tone/>
- **Atlassian**: bold, optimistic, practical, with a wink. Solution first, one idea per sentence.
  <https://atlassian.design/content/voice-tone/>
- **Shopify Polaris**: sound human, which they operationalise as a read-aloud test.

The single most useful check across all three: **tone must move with the reader's state.** Playful
copy on an error, a failed payment or a deletion confirmation is the most common voice defect, because
the voice was applied uniformly instead of being adapted to the moment.

---

## Excluded, and why

Kept so they are not re-added.

- **"Sentences should be 5 to 8 words."** No source. GOV.UK's actual guidance is a 25-word check.
- **Fixed paragraph word-count caps.** No sourced limit exists. The rule is one idea per paragraph.
- **"Helper text improves task completion by about 15%."** Could not be traced to any primary study.
  Widely repeated, unsourced.
- **"Never use humour in UI copy."** Overreach. The real rule is that tone moves with the reader's
  state, which permits humour where the moment permits it.
- **Any single universal button capitalisation rule.** Major systems disagree. Internal consistency is
  the finding, not conformance to one house.
- **Readability formulas as a pass/fail gate.** Flesch-Kincaid and friends count syllables and sentence
  length, and can be satisfied by chopped-up nonsense. Useful as a smell, never as a verdict.

## Sources

GOV.UK content and publishing guidance, Nielsen Norman Group (reading behaviour, error messages, form
placeholders, empty states), W3C WAI (WCAG 2.4.4, 2.4.9, 1.1.1, 1.3.3 and technique F84), Shopify
Polaris, Mailchimp content style guide, Atlassian design system. Individual URLs sit with each entry.
