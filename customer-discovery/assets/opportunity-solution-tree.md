# Opportunity Solution Tree Template

<!-- One measurable outcome at the root. Opportunities in the customer's words, each with evidence or an [ASSUMPTION] tag. No solution without a parent opportunity. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Opportunity Solution Tree: [Product / area]

**Desired outcome:** [metric] moves from [baseline, anchored to period] to [target] by [date]
<!-- "Ship X" is not an outcome. If the metric has no baseline, fix that first. -->

## Opportunity 1: "[pain or desire in the user's words]"
- **Evidence:** [interview log YYYY-MM-DD, n=; telemetry ref] or `[ASSUMPTION]` + revisit trigger
- **Segment:** [ICP slice this opportunity belongs to]
- **Severity:** [what it costs them per week/month, from interviews] or `[ASSUMPTION]`

### Candidate solutions (list >= 3; first idea is never the only idea)
1. [Solution A]
2. [Solution B]
3. [Solution C]

### Experiments (smallest test for the leading solution)
| Solution | Experiment | Success threshold (anchor) | Kill threshold | Owner / date |
| :--- | :--- | :--- | :--- | :--- |
| [A] | [e.g. mock button in live UI, measure CTR for 5 days] | [e.g. CTR >= 8%; anchor: median entry-point CTR 6% last quarter] | [e.g. < 4% kills] | [name / date] |

## Opportunity 2: "[user's words]"
- **Evidence:** [...]
### Candidate solutions
1. [...]
### Experiments
| ... |

<!-- Repeat per validated opportunity. Three solutions minimum keeps the tree honest. -->

## Parking lot (ideas with no mapped opportunity)
- [Idea] — parked because [no parent opportunity / outside ICP / contradicts outcome]
<!-- Review parking lot monthly against new interview facts; unpark with evidence only. -->
```
