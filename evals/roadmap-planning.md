# Evals: roadmap-planning

## Scenario 1 — Exec demands dated Gantt (adversarial)
**Prompt:** "The CEO wants a 12-month roadmap with dates for every initiative by Friday, including the AI features we haven't researched."
**Expected behavior:**
- Refuses fake precision: no 12-month dated Gantt over undiscovered work.
- Delivers in pushback order: NNL roadmap; Commitments strip limited to Now + contractual; cost-of-fake-dates note; reforecast offer (monthly cadence default tagged `[ASSUMPTION]`).
- Later rows carry no dates; evidence column present with citations or `[ASSUMPTION]`.
- If `product/bets.md` is in play, Now rows draw from active bets only: an unmatched Now row is flagged `[NOT AN ACTIVE BET]`, and any bet past its kill-criterion revisit date is flagged `[RESOLUTION DUE]` with a cut-scope-or-kill decision rather than a silent carry.

## Scenario 2 — Contractual dates (justified deviation)
**Prompt:** "Two enterprise contracts promise audit logs by Nov 1 and EU data residency by Jan 15. Everything else is normal discovery work. Build the roadmap."
**Expected behavior:**
- Keeps NNL; the dated Commitments strip contains exactly the two contractual items with contract clauses cited; all other rows horizon-based and undated.

## Scenario 3 — Quarterly roadmap, good evidence (happy path)
**Prompt:** "We're a 3-team B2B SaaS. 9 churn interviews cite failed exports; telemetry shows 18% of actives hit export errors. Build the quarter's roadmap."
**Expected behavior:**
- Problems, not features ("export reliability" as the problem); Now capped at 3 in-flight problems (one per team); evidence column cites the interview set and telemetry; Now rows carry hill position + circuit-breaker date; exec uncertainty block present.

## Scenario 4 — Percent-complete status review (diagnostic)
**Prompt:** "Status update: the dashboard is 60% done, the API is 40%."
**Expected behavior:**
- Converts to hill language: asks which scopes are still uphill; flags percent-complete as banned; proposes cut-or-kill decisions for anything uphill past the window midpoint; cites the circuit-breaker rule.
