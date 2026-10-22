# Cadence, Health & Bad News Reference

Deep-dive companion to SKILL.md. Load for any health rating, cadence choice, or bad-news draft.

## 1. Audience-by-audience cadence

- **Core team / direct collaborators — weekly.** Full detail: metric movement, Now/Next per initiative, risks, asks. This is the only audience that gets initiative-level texture every period.
- **Execs / sponsors — biweekly or monthly.** One page. Health, North Star vs target, reds with options, asks. Execs scan for "where am I needed"; everything else is appendix.
- **Broader company — monthly.** Outcome highlights: what changed for customers, what was learned. No internal risk laundry.
- **Board — quarterly.** Strategy level: North Star trend across quarters, active focus (Growth/Engagement/Monetization), major bets and formal exceptions. Tactical reds belong in the exec update, not the board deck, unless they change strategy.
- **Deviation criteria:** accelerate (e.g. daily note) only during an incident or crisis, with a stated end date; decelerate when the audience demonstrably does not read (merge into a wider forum instead of shipping unread pages). These cadences are operating defaults, not universal law — `[ASSUMPTION]`-grade anchors a team may recalibrate and record in its strategy doc.
- **Pre-socialization rule:** no red status appears in a broadcast before the affected stakeholders have heard it directly. If that did not happen, the update says "pre-socialization pending" and the update's distribution waits where possible.

## 2. Health criteria (Green / Yellow / Red)

| Color | Criteria |
| :--- | :--- |
| Green | North Star within 5% of target, or trending to hit target by period end `[ASSUMPTION]`; no breached kill criterion; no blocking risk without a mitigation in motion |
| Yellow | North Star 5-15% below target `[ASSUMPTION]`, or one recoverable risk (mitigation exists and is in motion) |
| Red | North Star >15% below target for two consecutive updates `[ASSUMPTION]`, or a kill criterion breached, or a blocking dependency with no mitigation |

- The 5%/15% bands and the two-consecutive rule are this skill's operating defaults — `[ASSUMPTION]`-grade anchors. Recalibrate against the metric's natural variance and record the chosen bands next to the color the first time they are used.
- High-variance metrics (small-traffic experiments, lumpy enterprise ARR) get wider bands; stable high-volume metrics get narrower ones. State the band, do not hide it.
- Borderline between two colors: assign the worse one.
- **Worked Example (Hypothetical: B2B invoicing startup):** week-2 retention target 40%. Actual 38.5% (within 5%) — Green with a trend note. Actual 36% (10% below) — Yellow. Two consecutive updates at 33% (>15% below) — Red even if the team "feels" progress.

## 3. Delivering bad news early, with options

Order rule: reds open the update, before wins. A miss reported early with options reads as control; the same miss reported late reads as concealment.

Format, per red:

1. **What happened** — 2-3 sentences, quantified. No adjectives, no weather metaphors.
2. **Impact** — the metric and the business consequence (revenue, churn, trust, date risk).
3. **Options** — 2-3, each with cost and expected effect, including "accept and reset the target".
4. **Recommendation** — one option, one sentence of rationale.
5. **Ask** — the decision or coverage needed, from whom, by when.
6. **Pre-socialized** — with whom and when, or "pending".

Rules: never ship a red without options; never let the update be the first notice (§1); never bury the miss after the wins section.

**Worked Example (Hypothetical: missed quarter):** "Q3 target +15% NRR; closed +6%. Two of three expansion deals slipped to Q4 because the usage-reporting feature landed six weeks late. Options: (1) re-sequence CSM capacity onto the slipped accounts (cost: onboarding delays for 2 new logos), (2) run a price-pack pilot to lift expansion per account (cost: 1 quarter of data), (3) accept +6% and reset the Q4 target. Recommendation: (1), because the slipped accounts are the ones with measured usage growth. Ask: CFO to approve the re-sequence by Friday. Pre-socialized: CEO and VP Sales on [date]."

## 4. Outcomes, not activity

- **Conversion rule:** every activity line must answer "so which metric moved?" If none does, it is status, not progress. Demote it to the appendix or cut it.
- **Rewrites:** "shipped the CSV export fix" becomes "export error rate 18% -> 4% (Q3 telemetry); export-related support tickets down 31%". "Ran 5 interviews" becomes "5 of 5 churn interviews name failed exports as the trigger; bet upgraded from [ASSUMPTION] to cited".
- **Pre-outcome work:** if the metric cannot move yet (early build), report proximate evidence — discovery signals, hill-chart position — and the date the metric becomes measurable. Label it `[PRE-OUTCOME]`.
- **Vanity guard:** cumulative counts (total signups, total releases) hide decline. Prefer cohort rates and period-over-period movement against an anchored baseline.

## 5. Hill-chart status for Now/Next

- Singer splits every initiative into uphill (figuring out what to do) and downhill (executing the known). Report that, not "80% done": an initiative still uphill past mid-cycle is the risk signal, because the unknown work is what blows the cycle (Singer).
- Statuses: **Uphill** (unsolved unknowns remain), **Downhill** (execution only), **Done**.
- **Worked Example:** Basecamp-style reporting: "reporting dashboard, week 4 of 6, still uphill on query performance" surfaces circuit-breaker risk two weeks before the date slips; "80% done" would have hidden it.

## 6. Sources

- Hill charts, circuit breakers, appetite: Ryan Singer — [basecamp.com/shapeup](https://basecamp.com/shapeup)
- Outcome accountability over output: Marty Cagan — [svpg.com/articles](https://svpg.com/articles/)
- Surfacing bad news early as a management norm: Andy Grove — High Output Management
- Product review governance: First Round Review — [review.firstround.com](https://review.firstround.com/)
