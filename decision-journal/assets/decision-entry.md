# Decision Entry Template

<!-- One entry per decision identity. Commit-time fields are frozen; resolution and addenda append below. Never duplicate an entry — update it. Delete unused comments; never ship bracketed placeholders. -->

```markdown
## [YYYY-MM-DD] | Type: [PRD commit / prioritization / kill-pivot / strategic bet / launch] | [Decision name]

- **Decision:** [what is being committed, one sentence]
- **Alternatives considered:** [one line each]
- **Predicted outcome:** [metric] moves from [X, anchored to baseline period] to [Y] by [date]
- **Kill criterion:** [threshold + anchor] at [revisit date] -> [kill/pivot action]
- **Confidence:** [NN]%  <!-- probability the prediction above comes true, at commit time; frozen forever -->
- **Status:** Pending

<!-- Append at resolution; never edit the commit-time fields above. -->
### Resolution [YYYY-MM-DD]
- **Actual outcome:** [metric actual, source citation]
- **Prediction correct:** [yes / no — scored against the prediction as written]
- **Kill criterion honored:** [yes / no — if no, state the resource and strategic consequences]
- **Status:** [Resolved / Killed / Superseded (successor: [entry name])]

<!-- Append for context changes, scope revisions, or corrections; originals stay verbatim. -->
### Addendum [YYYY-MM-DD]
- [what changed and why; original prediction retained for scoring]
```
