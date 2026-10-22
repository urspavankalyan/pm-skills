# Pre-Mortem Template

<!-- Frame verbatim first; candidates carry evidence classes; top three end as kill criteria or alerts. -->

```markdown
# Pre-Mortem: [Plan / Bet Name] | [YYYY-MM-DD]

**Frame:** It is 12 months from now. The plan failed. Generate the reasons.
**Context read:** [product/strategy.md citation or [ASSUMPTION]; GEM rank; existing kill criteria from product/bets.md]
**Evidence base of the plan under review:** [citations or [STRATEGY-DRIVEN ONLY]]

## Failure Candidates

| # | Candidate failure mode | Risk family | Evidence class | Severity if realized | Leading indicator (instrumented where possible) | Killer today? (kill criterion / alert, threshold + anchor + revisit) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [e.g. app-store review rejects the sync entitlement; no fallback] | Feasibility | [eng memory of prior rejection — [[HYPOTHESIS]] until release notes confirmed] | High | [review status of pilot build, weekly] | [2-day spike by [date]; rejection => pivot to web-first] |
| 2 | ... | ... | ... | ... | ... | ... |

## Adopted Kill Criteria / Alerts (top three, mandatory)
1. [threshold + anchor + revisit date + owner]
2. ...
3. ...

## Instruments We Must Build To See These Coming
- [signal, owner, date]
```
