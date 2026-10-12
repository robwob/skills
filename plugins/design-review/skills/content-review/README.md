# content-review

Evaluates the words in a design against content design best practices and reports what is unclear,
wrong or missing, with the replacement written out. Copy only: headings, labels, buttons, helper text,
errors, empty states, link text, alt text, terminology, plain language, tone.

Pairs with `ux-review` (interaction) and `ui-review` (visual craft). Run all three at once with
`design-review`.

## Install

**Claude Code / local.** Symlink this directory into your skills folder:

```
ln -s /path/to/content-review ~/.claude/skills/content-review
```

Skills are picked up when a session starts, so start a new session afterwards.

**claude.ai.** Upload `content-review.skill`. Uploaded copies are read-only, so the skill cannot save
an approved library addition. It will say so and hand you the text to paste in.

## Use

> "Review the copy on this page" plus a screenshot, URL, local file, Figma/Paper link, or just a list
> of strings.

Give it the reader and the moment. The same sentence can be right on a marketing page and wrong on a
failed payment, and the skill will ask if you do not say.

Output is a self-contained `content-review.html`: findings with current and proposed copy side by
side, a terminology audit table, suggestions kept separate from findings, and a list of the strings
the input format kept out of reach.

## What is in here

```
SKILL.md                          the process
references/content-standards.md   the bar: plain language, scannability, microcopy,
                                  error-message anatomy, states, accessible language,
                                  terminology, voice and tone
```

Every entry carries a tier. **Standard** is a citable requirement, in practice a WCAG criterion that
is really a content rule. **Evidence** is a quantified primary-source finding. **Convention** is
adopted practice where systems disagree. **Voice** is judged against a product's own declared voice,
and where none is declared there is nothing to breach.

There is a fourth severity, **Suggestion**, for a rewrite that is better but not tied to any entry. It
is kept in its own section and never mixed with findings. That separation is what stops a content
review becoming an argument about taste.

Content design attracts more unsourced rules than any other design discipline, so the library keeps a
firm `Excluded, and why`: "5 to 8 word sentences", paragraph word caps, the unsourced helper-text
statistic and readability formulas as a pass/fail gate are all rejected there with the reason.

After editing anything here, rebuild the zip:

```
cd content-review && zip -qr ../content-review.skill SKILL.md references/
```
