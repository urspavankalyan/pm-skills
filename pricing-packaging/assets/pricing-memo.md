# Pricing Memo Template

<!-- Deliverable for any pricing or packaging decision. Delete unused sections; never ship bracketed placeholders. Every number cites WTP research, billing telemetry, or a previous gate — or carries [ASSUMPTION] with a revisit date. -->

```markdown
# Pricing Memo: [Product / Change Name]

**Status:** [Draft / Approved / WTP-EVIDENCE PENDING / MONETIZATION DEFERRED] | **Bypass tag:** [none / DRAFT-ONLY / SANDBOX] | **Owner:** [Name] | **Date:** [YYYY-MM-DD]
**WTP evidence:** [e.g. Van Westendorp, n=240/segment, 2026-Q3 | 12 seller quotes | NONE — see pushback section]
**Sequencing case:** [default engagement-first | bootstrapped | B2B-premium — one sentence justification]

## 1. Value Metric
- **Metric:** [unit, e.g. active seats / events processed / records stored]
- **Why it tracks value:** [one sentence: usage of this unit grows as the customer succeeds because ...]
- **Abuse/gaming risk:** [how customers could game it, and the fence against that]

## 2. WTP Evidence & Willingness Profiles
- **Instrument:** [Van Westendorp (n per segment, date) | seller quotes | competitive audit]
- **Acceptable range:** [$X - $Y, anchor: survey intersections PMC/PME]
- **Optimal/indifference points:** [OPP $A, IPP $B]
- **Profile map:** which profile dominates each segment —
  - Value buyers: [share/notes, what proof they need]
  - Status buyers: [present? what exclusivity they buy]
  - Convenience seekers: [default behavior to design for]
  - Budget buyers: [entry offer, cannibalization fence]

## 3. Packaging (Good-Better-Best)
| Tier | Price | Value-metric limit | Fenced differentiator | Target profile |
| :--- | :--- | :--- | :--- | :--- |
| Good | [$] | [limit] | [what is withheld] | [budget / entry] |
| Better (hero) | [$ at OPP band] | [limit] | [core value complete] | [value buyers] |
| Best | [$ anchor] | [higher limit] | [killer feature + support] | [status / power] |
| Enterprise | negotiated | custom | [SSO, security, SLA] | [procurement] |

- **Self-selection check:** [why each profile lands on its tier, not the one below]

## 4. Sequencing Decision
- **Engagement state:** [retention curve status, activation rate, anchor/telemetry cite]
- **Decision:** [monetize now | defer — [MONETIZATION DEFERRED] until <criterion>]
- **If deviating from engagement-first:** [bootstrapped / B2B-premium justification]

## 5. Price Rise & Grandfathering (only for rises)
- **Rise size vs corridor:** [+N% against WTP corridor and substitute costs]
- **Value justification:** [shipped capability tied to the value metric]
- **Grandfathering policy:** [migrate with N-day notice | grandfather N months with sunset date + migration incentive]
- **Kill criterion:** [logo churn 90d post-notice <= trailing baseline + N pts; anchor: trailing-90d churn telemetry; breach action: revise migration offer]

## 6. Kill Criteria & Revisit
| Check at | Threshold (with anchor) | Decision |
| :--- | :--- | :--- |
| [date] | [e.g. self-serve upgrade rate >= X% of eligible accounts; anchor: current rate] | [hold / repackage] |
| [date] | [e.g. Van Westendorp re-run OPP within +/-10% of shipped hero price; anchor: this memo] | [hold / reprice] |

## 7. Assumptions Log
- [ASSUMPTION] [claim] — revisit trigger: [event/date]
```
