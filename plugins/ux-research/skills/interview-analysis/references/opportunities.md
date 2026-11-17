# Opportunities and recommendations

How `interview-analysis` turns findings into opportunity statements, and opportunities into
recommendations, without losing the thread back to the evidence.

**Last updated:** 17 November 2026

Tags as in `analysis.md`.

---

## The chain

```
Evidence (quotes, occasions, with timestamps)
  -> Finding (pattern, x of n, confidence)
    -> Opportunity (a need, framed without a solution)
      -> Recommendation (what to do about it, agreed with the designer)
```

Every link names the one before it. A recommendation names its opportunity, an opportunity names
its findings, a finding names its evidence. Nothing in the report floats free of the data.
`(house)`

---

## Opportunity statements

### What an opportunity is

In Teresa Torres's opportunity solution tree, the opportunity space holds the customer needs, pain
points and desires that would drive the outcome if addressed, and it is kept apart from the
solution space. She advises checking that each opportunity is framed as a need, pain point or desire
rather than a solution, and phrasing it as something a customer might say. `(unverified)`, from
Product Talk pages reached through search summaries; the site could not be fetched.

### The format

> **O[n]. [Who] need(s) [what], [when or in what situation].**
> From: F[n], F[n]. Confidence: [level], [basis].

Examples, from the sample data:

> **O1. Manual readers need to send a reading at a moment they can act on it, before an estimate is
> issued.** From F1 and F2.

> **O2. People need to show that the reading they sent is correct without a separate email or
> call.** From F3.

### The rules `(derived)`

1. **No solution inside.** "People need a photo upload" is a solution. Test: could at least two
   quite different solutions meet it? If only one could, rewrite it as the need behind it.
2. **Who is the people the evidence covers.** If the support is from manual readers, the
   opportunity is for manual readers, not "users".
3. **Comes from at least one finding**, named. An opportunity built only from hypotheticals ("would
   use a photo feature") is not an opportunity: look for the occasion behind it, or leave it out
   and list the hypothetical under "what participants asked for" with its evidence type.
4. **A need, a pain or a desire, in plain words.** No "leverage", "streamline" or "empower".
5. **Confidence is the lowest of its findings** (`confidence.md`).
6. **The number is set by the data.** Several findings often feed one opportunity; a finding with no
   need behind it (something that works well, say) may feed none.

---

## Recommendations

### The format

> **R[n]. [What to do, as a change or an action].**
> From: O[n]. Confidence: [level], [basis]. To raise it: [the research that would].
> Expected impact: [what should change, and for whom].

### The rules

1. **Drafted, then the designer decides.** The skill drafts two or three per opportunity at most,
   and stops. `(house)`
2. **Confidence is capped at Medium** unless participants' own behaviour already shows the thing
   working (`confidence.md`). `(derived)`
3. **Name what would raise its confidence.** Usually `usability-test-plan` for a design change, or
   a survey or analytics for how common the need is. `(derived)`
4. **Do not pass off participants' suggestions as recommendations.** "I'd like to upload a photo" is
   a hypothetical. If it is the right answer, it is because of the need behind it, and the
   recommendation cites that. `(derived)`, from the sources on predictions in `analysis.md`.
5. **The designer's own recommendations are theirs.** Record them as given. If one has no finding
   behind it, say so once and mark it "not assessed". `(house)`

---

## Change log

**17 November 2026.** File created. Opportunity framing after Torres, reached through search
summaries. Format and rules are this library's.
