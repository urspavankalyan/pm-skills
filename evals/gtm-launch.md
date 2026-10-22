# Evals: gtm-launch

## Scenario 1 — Big-bang demand (adversarial)
**Prompt:** "Board wants GA for everyone next Tuesday. Skip the beta stuff, marketing is ready."
**Expected behavior:**
- Refuses the big-bang; ships the gate-0 internal plan plus a risk note naming what will be unmeasurable when it breaks; offers `[PLAN-ONLY / GATES WAIVED]` header if the user insists on an artifact.
- Asks for instrumentation status and positioning status; missing instrumentation blocks gates 1-3 explicitly.
- Must NOT produce a GA-day comms plan as if the rollout were approved.

## Scenario 2 — "We have no competition" (adversarial)
**Prompt:** "Our AI tool is category-defining, there is no competition. Write the positioning."
**Expected behavior:**
- Dunford pushback fires: produces the status-quo alternatives list (spreadsheet, hire, do-nothing), cites the 20-30% no-decision statistic, excludes phantom vendors.
- Positioning page completed against alternatives with category style chosen (default head-to-head or small-pond; new-game requires education-budget justification).
- Must NOT accept "no competition" as a completed component.

## Scenario 3 — Vague ask (diagnostic)
**Prompt:** "help with our launch please"
**Expected behavior:**
- Asks at most three targeted questions (positioning state, motion economics: ACV + time-to-value, instrumentation/readiness) or offers the checklist as `[PLAN-ONLY]`.
- Does not dump the full template before the gate inputs exist.

## Scenario 4 — Well-prepared launch (happy path)
**Prompt:** "Positioning signed off last week (alternatives: spreadsheet + two incumbents; category: subsegment). ACV $8K, solo user reaches value in one session. Instrumentation live. Build the rollout."
**Expected behavior:**
- Motion = PLG or hybrid with the two deciding numbers stated (ACV band tagged `[ASSUMPTION]` if using industry cutoffs).
- Checklist loaded; gates 0-3 scheduled with kill thresholds anchored to gate-0 baseline; +30 retro with position-in-market check present.
- No bracketed placeholders remain in the delivered plan.
