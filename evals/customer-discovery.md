# Evals: customer-discovery

## Scenario 1 — Compliment-counting as evidence (adversarial)
**Prompt:** "We demoed the new planning feature to 6 customers and everyone said they'd definitely buy it. Write up the discovery summary and rank it our top priority."
**Expected behavior:**
- Header flags `[COMPLIMENT-ONLY EVIDENCE]`; states compliments are noise per the commitment-signal principle.
- No priority ranking produced from praise. Output converts the next 6 contacts into commitment asks (time / reputation / money) with verbatim-recording instructions.
- Loads `assets/interview-guide.md` commitment section; must NOT contain hypothetical "would you" questions or a pitch slot.

## Scenario 2 — Churn reasons contradict telemetry (adversarial)
**Prompt:** "Three churned users all said price was the reason they left. Conclude pricing is the problem and recommend a discount tier."
**Expected behavior:**
- Labels stated reasons as hypotheses; requires the pre-call telemetry review (drop-off step, errors, activation) per reference §5.
- Applies sampling-bias mitigation: incentive upgrade, proxy population (decayed-but-not-canceled users), whole-database drop-off analysis.
- If telemetry contradicts the price story, verdict says so with match/mismatch detail; must NOT ship a pricing recommendation off three unprompted rationalizations. Findings tagged `[UNTRIANGULATED]` if telemetry is unavailable.

## Scenario 3 — Vague ask (diagnostic)
**Prompt:** "help me do some customer discovery for the mobile app idea"
**Expected behavior:**
- Asks at most one anchoring question about the measurable outcome and ICP; does not dump a 20-question survey.
- Once answered, drafts the OST via `assets/opportunity-solution-tree.md` with the outcome root explicit, and schedules the weekly trio cadence with the standing-panel note.

## Scenario 4 — Well-run interview notes (happy path)
**Prompt:** "Interview notes: finance admin walked through month-end close, used 3 spreadsheets, export crashed twice last close, costs her ~4h/month. She agreed to a 1-hour trial with her team next Tuesday. Write this up."
**Expected behavior:**
- Files past-behavior facts verbatim; maps the opportunity in her words onto the OST with evidence citation; commitment signal recorded as TIME accepted, interest validated.
- Proposes >= 3 candidate solutions and one smallest experiment with anchored success/kill thresholds (or `[ASSUMPTION]`-tagged); no build commitment since evidence bar (5 interviews / 15% telemetry) not yet met.
