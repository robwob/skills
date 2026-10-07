# Skills

Claude skills I use for UX research. Each one is self-contained: install the ones you want
and ignore the rest.

What they have in common is that they choose from a written, cited reference library rather
than from memory. The method, the question type, the sample size, the source weighting: each
comes from a file in that skill's `references/`, with citations, so the reasoning is
inspectable and correctable instead of improvised differently every session.

Claims in those libraries carry their status. `(unverified)` means the primary text was not
available and the claim rests on a secondary source. `(derived)` means sources disagreed and
the claim is a stated reconciliation. Correcting one of those is the most useful contribution
you can make, and [CONTRIBUTING.md](CONTRIBUTING.md) says how.

## UX research

| Skill | What it does |
|---|---|
| [`ux-research-brief`](skills/ux-research-brief/) | Scopes a research project through intake, definition and method selection, choosing from a library of 20 methods, then hands execution to the others. |
| [`discussion-guide`](skills/discussion-guide/) | Drafts an interview script. Pairs every attitude question with a follow-up that can contradict it. |
| [`usability-test-plan`](skills/usability-test-plan/) | Plans a moderated or unmoderated test, sizes the sample, and reports every stated rating next to the observed record. |
| [`survey-questions-v2`](skills/survey-questions-v2/) | Drafts a survey, or audits an existing one for bias and for coverage against a brief. |
| [`desk-research`](skills/desk-research/) | Competitor and landscape research, weighted by what each source type can and cannot show. Returns hypotheses, not findings about users. |

`ux-research-brief` can orchestrate the other four, or you can run any of them on its own.

## Install

Add the marketplace once, then install the plugins you want:

```
claude plugin marketplace add robwob/skills
claude plugin install ux-research@newport
```

That installs all five research skills together. They appear as `ux-research:ux-research-brief`,
`ux-research:discussion-guide` and so on, and you can also just describe what you need and let
Claude pick the right one.

To install without adding the marketplace first:

```
/plugin install ux-research --marketplace robwob/skills
```

Prefer not to use plugins? Each skill is a plain directory, so you can symlink one straight in:

```
ln -s "$PWD/plugins/ux-research/skills/ux-research-brief" ~/.claude/skills/ux-research-brief
```

Skills load when a session starts, so start a new one afterwards. **A broken symlink fails
silently**: the skill simply does not appear, with no error anywhere. Confirm it loaded:

```
[ -e ~/.claude/skills/ux-research-brief/SKILL.md ] && echo OK || echo BROKEN
```

Each skill's own README covers its use and what it produces in more detail.

## Licence

MIT. See [LICENSE](LICENSE).
