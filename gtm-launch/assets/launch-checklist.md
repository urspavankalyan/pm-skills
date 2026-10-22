# Launch Checklist Template

<!-- Fill for every launch. Gates are boolean with named owners; rollout thresholds are numbers anchored to the previous gate's measured baseline, or [ASSUMPTION]-tagged until measured. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Launch Plan: [Product / Feature Name]

**Owner:** [Name] | **Target GA window:** [dates] | **Motion:** [PLG / sales-led / hybrid — decided by ACV $X and time-to-value Y]
**Positioning status:** [signed off YYYY-MM-DD | contested — workshop scheduled]

## 1. Positioning Sign-Off (Dunford)
- **Competitive alternatives (status quo included):** [list; must include do-nothing/spreadsheet/hire]
- **Differentiated value:** [unique attributes -> value, with proof per attribute]
- **Customer segment:** [who cares most, described so sales can find them tomorrow]
- **Market category + style:** [category; head-to-head / small-pond / new-game with one-line justification]
- **Sign-off:** [names of product, marketing, sales leads]

## 2. Readiness Gates
| Gate | Owner | Evidence required | Status |
| :--- | :--- | :--- | :--- |
| Instrumentation verified | [name] | test events observed end-to-end in every dashboard/alert used by gates 1-3 | [green/red] |
| Support readiness | [name] | macros, escalation path, staffing for 5% and 25% cohorts | [green/red] |
| Sales enablement (if motion includes sales) | [name] | pitch vs alternatives, pricing one-pager, demo environment | [green/red] |
| Rollback path | [name] | feature flags + data migration rollback tested | [green/red] |
| Legal/compliance (if regulated surface) | [name] | review complete, cited | [green/red] |

## 3. Rollout Schedule & Kill Thresholds
| Gate | Cohort | Start | Entry criteria | Kill threshold (anchor) | Breach action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 100% internal | [date] | readiness gates green | blocking bugs > 0; internal WAU < 60% `[ASSUMPTION]` | pause + fix |
| 1 | 5% | [date] | gate 0 clean >= 2 wks | [error rate > 2x baseline; activation < 50% of baseline; tickets > 2x expected — anchor: gate-0 measurements] | 48h diagnose-or-rollback |
| 2 | 25% | [date] | gate 1 clean 2 consecutive wks | same thresholds at gate-1 baseline | 48h diagnose-or-rollback |
| 3 | GA 100% | [date] | written go decision vs gate-2 baseline | 30-day guardrails: churn, error budget | rollback plan executes |

<!-- Baseline block: paste gate-0 measured numbers here before gate 1 opens; until then every threshold above is [ASSUMPTION]. -->

## 4. Communications
- **Internal:** [what support/sales hear, when]
- **External:** [launch narrative led by differentiated value vs the named alternatives; no adjective-only claims]

## 5. +30 Day Retro
- **Position-in-market check:** [what category did prospects file us under in N recorded calls]
- **Metrics vs gates:** [actuals vs thresholds]
- **Kill criteria carried forward:** [list with owners and revisit dates]
```
