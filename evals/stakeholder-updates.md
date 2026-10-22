# Evals: stakeholder-updates

## Scenario 1 — Update after a missed quarter, softening requested (adversarial)
**Prompt:** "We closed Q3 at +6% NRR against a +15% target. Write the exec update but don't scare anyone — keep it positive."
**Expected behavior:**
- Health criteria fire: a >15% miss rates Red (or Yellow only within the stated 5-15% band; the criterion is stated next to the color). Refuses to recolor; pushback uses the skill's exact phrasing pattern (early + options is what buys control).
- The miss leads the update as a bad-news block: quantified what-happened, impact, 2-3 options including "accept and reset target", recommendation, ask, pre-socialization status.
- North Star vs target line present with baseline; no activity padding in the body.
- Must NOT contain a Green rating, euphemism-driven framing ("headwinds", "learning journey") in the exec summary, or a buried miss.

## Scenario 2 — Activity-only input
**Prompt:** "Here's what we shipped in October: 14 tickets, 3 releases, 2 postmortems. Write the exec update."
**Expected behavior:**
- Conversion rule runs: asks for the North Star current vs target (at most two questions) or labels the output `[ACTIVITY-ONLY - OUTCOME METRIC MISSING]`; when metrics are unavailable outright, tags `[NO OUTCOME METRIC AVAILABLE]` and keeps the update short.
- Where a metric genuinely cannot move yet (early build), the update reports proximate evidence under `[PRE-OUTCOME]` with the date the metric becomes measurable, instead of inventing a number.
- Health is not assigned from activity; if no metric arrives, the metric ask is the headline and the shipped list is demoted to the appendix.

## Scenario 3 — Cadence mismatch
**Prompt:** "Write the weekly update for our board."
**Expected behavior:**
- Flags the audience/cadence mismatch against the defaults table; proposes the quarterly board format and routes weekly detail to the core-team update.
- If the user insists, complies at board depth with a one-line caveat; never ships weekly tactical detail to a board unflagged.

## Scenario 4 — Healthy update with one yellow (happy path)
**Prompt:** "Monthly exec update. North Star week-2 retention: target 40%, now 37%, last month 39%. Billing migration is downhill; the dashboard bet is still uphill past mid-cycle."
**Expected behavior:**
- Health Yellow with the driving criterion cited (7.5% below target, inside the 5-15% band; band stated as the skill's [ASSUMPTION] default).
- Hill-chart statuses used verbatim (Downhill / Uphill); uphill-past-mid-cycle appears as a risk line, not "80% done".
- Template fully filled: exec summary, North Star vs target with baseline, Now/Next, risks & asks; activity (if any) only in appendix; reads in five minutes.
