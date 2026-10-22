# Metrics Review Template

<!-- Periodic review with an instrumentation verdict before any product verdict. Every baseline and threshold states its anchor or is tagged [ASSUMPTION]. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Metrics Review: [YYYY-MM-DD to YYYY-MM-DD]

**North Star:** [metric] = [value] vs target [target] (anchor: [baseline period or control])
**Instrumentation status (Step-0):** [clean / issues found — list schema, logging, latency, double-log checks and their results]
**Output status:** [CLEAN / UNVERIFIED-INSTRUMENTATION / TRACKING-BUG-QUANTIFIED — applies to the whole diagnosis until Step-0 clears]

## North Star & Input Metrics
| Metric | AARRR stage | Baseline (anchored) | This period | Delta vs noise band | Signal? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [NS metric] | [stage] | [value, period] | [value] | [band + how estimated, or [ASSUMPTION]] | [yes/no] |
| [input metric 1] | [stage] | ... | ... | ... | ... |
<!-- One distinct event per stage; if stages overlap, flag and separate before reading deltas. -->

## Diagnosis (fill only for metrics that moved beyond the noise band)
- **Reported change:** [X pp / %, direction, first-observed date]
- **Step-0 verdict:** [checklist outcomes with refs: schema diffs, release dates, pipeline tickets]
- **Quantified tracking error:** [Y pp; method: affected cohort vs pre-release baseline / stable control; uncertainty: [band]]
- **Residual real change:** [X - Y = Z pp] — [if Z ~ 0: halt, tracking fix only, re-baseline on date]
- **Shape:** [step on [date] / gradual since [date]] → cause family: [deploys, API, campaign, season | mix shift, competition, onboarding drift]
- **Cohort evidence:** [retention curve by cohort: flattening at [n%] since week [k] / continued decay; segment notes]
- **Verdict:** [real change: hypothesis + smallest test + owner | tracking artifact: fix ticket + re-baseline date]
- **Attribution changes:** [if the diagnosis flipped since a prior review: date, old theory, new theory, evidence for the transition]

## Vanity-Metric Flags
- [metric] — why vanity: [cumulative-only / no denominator / no cohort / no licensed decision]; substitute: [rate or cohort alternative]

## Decisions & Kill Criteria
| Decision | Threshold (anchor) | Revisit date | Kill/pivot action |
| :--- | :--- | :--- | :--- |
| [what we will do] | [quantitative threshold + anchor or [ASSUMPTION]] | [date] | [action] |
```
