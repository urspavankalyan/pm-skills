# Experiment Brief Template

<!-- Pre-registration template. Fill every placeholder with a concrete claim, an anchored number, or an [ASSUMPTION] tag; delete unused sections; never ship brackets. -->

```markdown
# Experiment Brief: [Name]

**Method:** [fake door | concierge | prototype | landing page | A/B] | **Owner:** [name]
**Decision date:** [YYYY-MM-DD] | **Status:** [pre-registered | running | decided]
**Cohort(s) read:** [e.g. all users; read per: country, platform]

## 1. Hypothesis
For [cohort], [change] moves [primary metric] from [baseline] to [target] because [reason].

## 2. Primary Metric & Thresholds
- **Metric:** [name; where instrumented]
- **Baseline:** [value] (anchor: [Q3 telemetry | historical median | ASSUMPTION])
- **Fund threshold:** [value or lift] | **Kill threshold:** [value]
- **MDE justification:** [smallest effect worth shipping; anchored to eng cost or guardrail floor]

## 3. Sample & Stopping Rule
- **n per cohort/arm:** [number] (alpha 0.05, power 0.80; math: [show the computation])
- **Traffic check:** [conversions/week in narrowest cohort] vs required [n]; feasible within <= 4 weekly cycles: [yes/no]
- **Start:** [date] — **Stop:** [date or n reached]
- **Interim policy:** [no looks until horizon | always-valid CI with registered boundaries]

## 4. Guardrails (veto thresholds)
| Guardrail | Floor (anchor) | Instrument |
| :--- | :--- | :--- |
| [revenue/user] | [>= baseline value] | [billing telemetry] |
| [p95 latency] | [<= X ms; anchor: current p95] | [APM] |

## 5. Decision Rule (Kill vs Fund)
- **Fund:** primary >= fund threshold AND all guardrails hold at stop.
- **Kill:** primary <= kill threshold OR any guardrail veto.
- **Between:** [iterate once / qualitative follow-up]; decide by [date].
- **If underpowered:** label [DIRECTIONAL READ - UNDERPOWERED]; decide on CI + qualitative convergence, no p-value.

## 6. Novelty / Primacy Check
- Slice effect by weeks-since-exposure; require [2] stable weeks before funding a UI win.

## 7. Outcome Log (fill at decision)
- **Result:** [estimate + CI] | **Decision:** [kill | pivot | fund] | **Confidence:** [NN]% | **Next review:** [date]
```
