# Design skills

Claude skills for design and UX research. Each one is self-contained: install the plugins
you want and ignore the rest.

What they have in common is that they choose from a written, cited reference library rather
than from memory. The method, the question type, the sample size, the source weighting, the
contrast threshold: each comes from a file in that skill's `references/`, with citations, so the
reasoning is inspectable and correctable instead of improvised differently every session.

Claims in those libraries carry their status. `(unverified)` means the primary text was not
available and the claim rests on a secondary source. `(derived)` means sources disagreed and
the claim is a stated reconciliation. Correcting one of those is the most useful contribution
you can make, and [CONTRIBUTING.md](CONTRIBUTING.md) says how.

## Design review

Checks a design against a bar. Every finding carries a severity and the measured value behind it.

| Skill | What it does |
|---|---|
| [`design-review`](plugins/design-review/skills/design-review/) | Runs all three lenses at once, removes the findings they duplicate, and returns one prioritised list. Start here if you do not want to pick a lens. |
| [`ux-review`](plugins/design-review/skills/ux-review/) | Interaction and structure: flows, states, forms, navigation, information architecture, error recovery, deceptive patterns. |
| [`ui-review`](plugins/design-review/skills/ui-review/) | Visual craft: contrast, typography, spacing, hierarchy, grouping, target size, component states. Computes the numeric checks against the rendered page rather than reading them off a screenshot. |
| [`content-review`](plugins/design-review/skills/content-review/) | The words: headings, labels, buttons, errors, empty states, terminology consistency, plain language. |

Entries in the review libraries are tiered. **Standard** is a citable requirement and a violation
is a defect. **Evidence** is a quantified primary-source finding. **Convention** is adopted practice
where established systems disagree. **House** is your own evidenced preferences, read at review time
from `~/.claude/house.md`, and applied only to your own work, never to a competitor's. With no such
file the House tier does not apply and the other three still do.

Folklore is excluded and stays excluded. The golden ratio, 60-30-10, a WCAG-backed minimum font
size and APCA thresholds are each listed in `Excluded, and why` with the reason.

## Design strategy

Decides what to bet on. There is no right answer here, only positions, which is what separates
these from the review skills.

| Skill | What it does |
|---|---|
| [`analyse-themes`](plugins/design-strategy/skills/analyse-themes/) | Works out which strategic themes a page or interface uses to solve its user problem, and compares pages on that basis. |
| [`define-levers`](plugins/design-strategy/skills/define-levers/) | Narrows themes to the levers a designer can consciously dial, the psychology principles that explain why moving each one works, and the methods that move it. |

`define-levers` can follow an `analyse-themes` session or run on its own if you name the themes
yourself.

## Project brief

| Skill | What it does |
|---|---|
| [`brief`](plugins/project-brief/skills/brief/) | Defines why a project is being done before any design or code, then derives the plan from that: which stages it needs, in what order, with review gates. |

`brief` needs one workspace-specific thing: where shared components live, which stages you run, your
writing conventions. It reads `~/.claude/house.md` when that exists, and falls back to the
`references/house-rules.md` template, which ships with every section documented. Leave a section
empty and the skill uses its stated default and tells you it did.

## UX research

| Skill | What it does |
|---|---|
| [`ux-research-brief`](plugins/ux-research/skills/ux-research-brief/) | Scopes a research project through intake, definition and method selection, choosing from a library of 20 methods, then hands execution to the others. |
| [`discussion-guide`](plugins/ux-research/skills/discussion-guide/) | Drafts an interview script. Pairs every attitude question with a follow-up that can contradict it. |
| [`usability-test-plan`](plugins/ux-research/skills/usability-test-plan/) | Plans a moderated or unmoderated test, sizes the sample, and reports every stated rating next to the observed record. |
| [`survey-questions`](plugins/ux-research/skills/survey-questions/) | Drafts a survey, or audits an existing one for bias and for coverage against a brief. |
| [`desk-research`](plugins/ux-research/skills/desk-research/) | Competitor and landscape research, weighted by what each source type can and cannot show. Returns hypotheses, not findings about users. |

`ux-research-brief` can orchestrate the other four, or you can run any of them on its own.

## Install

Add the marketplace once, then install the plugins you want:

```
claude plugin marketplace add robwob/skills
claude plugin install design-review@design
claude plugin install design-strategy@design
claude plugin install project-brief@design
claude plugin install ux-research@design
```

Skills appear namespaced to their plugin, as `design-review:ui-review` and so on, and you can also
just describe what you need and let Claude pick the right one.

To install without adding the marketplace first:

```
/plugin install design-review --marketplace robwob/skills
```

Prefer not to use plugins? Each skill is a plain directory, so you can symlink one straight in:

```
ln -s "$PWD/plugins/design-review/skills/ui-review" ~/.claude/skills/ui-review
```

Skills load when a session starts, so start a new one afterwards. **A broken symlink fails
silently**: the skill simply does not appear, with no error anywhere. Confirm it loaded:

```
[ -e ~/.claude/skills/ui-review/SKILL.md ] && echo OK || echo BROKEN
```

Each skill's own README covers its use and what it produces in more detail.

## A note on what is not here

`design-review` and `brief` both mention build stages: wireframes, interaction states, visual
styling. The skills I use for those stages depend on a local design system and a house visual
language, so they would not work for anyone else and are not published. Where a skill refers to a
build stage it means the stage, not a skill you are missing.

## Licence

MIT. See [LICENSE](LICENSE).
