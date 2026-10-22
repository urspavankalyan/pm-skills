# Evals: metrics-analysis

## Scenario 1 — "Diagnose this 20% activation drop" (adversarial)
**Prompt:** "Activation dropped 20% week over week. Tell me why it happened and what we should fix. I need answers for the exec sync in an hour."
**Expected behavior:**
- First move is the Step-0 instrumentation checklist (schema change, per-platform logging outage, latency, double-logging), not a causal narrative.
- If the user supplies a concurrent SDK/release change, quantifies tracking error (affected share vs baseline/control), computes the residual, and diagnoses only the residual; residual ~0 halts the product investigation.
- Any narrative issued before the checklist clears is labeled `[UNVERIFIED-INSTRUMENTATION]`. Must NOT contain an unqualified "the cause is X" story or improvement recommendations built on the raw 20%.

## Scenario 2 — Vanity metric as success evidence (adversarial)
**Prompt:** "Cumulative signups just passed 1M, put that at the top of the board deck as proof the new onboarding is working."
**Expected behavior:**
- Flags the metric as vanity (cumulative-only, no denominator, no cohort, cannot falsify the onboarding claim).
- Substitutes decision inputs in the same output: week-1 activation rate and cohort-split retention vs an anchored baseline; states the decision each licenses.

## Scenario 3 — Gradual retention decay (diagnostic)
**Prompt:** "Week-4 retention has been sliding ~1% a month since spring. Nothing broke, no deploys correlate. Where do we look?"
**Expected behavior:**
- Shape analysis classifies gradual trend; cause family: acquisition mix shift, cohort composition, competitive erosion, onboarding drift — not incident causes.
- Requests cohort-split curves and channel mix over the same window; compares flat-vs-decaying segments; output uses `assets/metrics-review.md` diagnosis section with anchors or `[ASSUMPTION]` tags.

## Scenario 4 — North Star selection (happy path)
**Prompt:** "We're a two-sided marketplace for local services. Help us pick a North Star and the input metrics for each team."
**Expected behavior:**
- Refuses revenue as North Star; proposes value-capture candidates (e.g. completed bookings) with the Airbnb-style rationale.
- Decomposes into per-team input metrics (search-to-book conversion, provider response time), each with a stated anchor or `[ASSUMPTION]`; notes the proxy-correlation check against cohort data before targeting.
