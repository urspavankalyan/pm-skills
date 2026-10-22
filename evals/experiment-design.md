# Evals: experiment-design

## Scenario 1 — Underpowered A/B demand (adversarial)
**Prompt:** "Design an A/B test for the new checkout. We get about 200 weekly users. I want a readout in two weeks."
**Expected behavior:**
- Triage gate fires: traffic check computes required n per cohort (~3,840/arm for a 10% -> 12% MDE at alpha .05, power .8) vs ~200/week and states the infeasibility with the arithmetic shown (~38 weeks).
- Delivers the small-traffic package: qualitative plan (5-8 ICP interviews), a one-day test option (fake door or walkthrough) with CI-based thresholds, and a `[DIRECTIONAL READ - UNDERPOWERED]` label for any directional number.
- Must NOT emit a p-value, must NOT silently produce an A/B brief, must NOT answer only "you need more traffic".

## Scenario 2 — Peeking pushback
**Prompt:** "The variant has been +9% and significant since day 3. Let's ship it now."
**Expected behavior:**
- Refuses the early call; explains peeking inflation with an anchor (Microsoft finding: 5 treatments lift a 2.5% nominal false-positive rate to ~12%, or the sequential-testing rationale).
- Asks whether a sequential rule or always-valid CI was pre-registered; offers the registered-horizon or sequential path; names guardrails to watch until stop.

## Scenario 3 — Adequate traffic, per-cohort read (happy path)
**Prompt:** "We do 40k conversions/week. We want to test a one-line change on the pricing page, and we need to read it per platform."
**Expected behavior:**
- Loads references/experiment-menu.md; sizes per platform cohort with the shown computation (not aggregate n); picks A/B with stated justification.
- Pre-registers via assets/experiment-brief.md: hypothesis, metric + threshold + anchor, per-cohort n, stopping rule, guardrails with veto floors, owner, dates, novelty/primacy check for the UI change.

## Scenario 4 — Untested demand, nothing built
**Prompt:** "Should we build a scheduling feature? Nothing exists yet and we have no users."
**Expected behavior:**
- Routes to references/one-day-tests.md: Torres assumption mapping picks the leap-of-faith assumption; Savoia market engagement hypothesis written as "X% of Y will do Z" with anchors or [ASSUMPTION] tags.
- Selects X-vertisement / fake door / walkthrough with a stated why and why-not for alternatives; kill-vs-fund thresholds registered before running; no full experiment brief for a question that has no baseline behavior.
