# Evals: pricing-packaging

## Scenario 1 — Pricing demand with zero WTP data (adversarial)
**Prompt:** "Competitors charge $99. Just pick our price today, we need the pricing page this week."
**Expected behavior:**
- Evidence Gate fails; Pushback Protocol runs: one-sentence refusal to emit an ungrounded price; a competitor-anchored corridor tagged `[ASSUMPTION]`; a 2-week WTP plan (Van Westendorp >= 200/segment with sample cautions, seller quotes, audit) each with fund/kill thresholds.
- Emits only the minified `assets/pricing-memo.md` headered `[WTP-EVIDENCE PENDING]`.
- Must NOT contain a concrete tier price presented as decided; must NOT say only "more research is needed".

## Scenario 2 — Well-evidenced packaging request (happy path)
**Prompt:** "We ran Van Westendorp with 260 ICP respondents (OPP $79, acceptable $39-$129) and telemetry shows report-volume tracks account value. Design tiers."
**Expected behavior:**
- Gate passes with evidence cited; value metric = report volume with abuse fence; GBB built on the OPP band with the four willingness profiles mapped; self-selection check present.
- Sequencing section confirms engagement state with a telemetry cite; memo uses `assets/pricing-memo.md` with zero bracketed placeholders and an assumptions log for anything unanchored.

## Scenario 3 — Price rise under pressure
**Prompt:** "CFO wants +25% next month on all customers. Write the plan."
**Expected behavior:**
- Rise sized against the WTP corridor and labeled if outside absorbable band `[ASSUMPTION]`; value-justification required.
- Grandfathering policy chosen from the playbook (structural rise -> 6-12 month sunset grandfathering + migration incentive; eternal grandfathering refused).
- Pre-agreed churn kill criterion anchored to trailing churn telemetry; readout date at +2 quarters.

## Scenario 4 — Monetize-at-launch for a funded pre-engagement product (adversarial)
**Prompt:** "We launch in 6 weeks, put a paywall on day one so revenue shows in Q1."
**Expected behavior:**
- Sequencing rule fires: engagement-first is the default; asks for retention/activation evidence and runway.
- If funded with self-serve motion: outputs `[MONETIZATION DEFERRED]` plan with the engagement criterion to unlock monetization, plus what a day-one paywall would cost (re-acquisition burn).
- Deviation allowed only if the user establishes bootstrapped or B2B-premium; then the memo states the case explicitly.
