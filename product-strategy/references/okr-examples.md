# OKR Examples & Rewrites

Key results are outcome metrics with baselines, targets, and anchors. This file shows the anatomy, the cascades, and the rewrites.

## 1. Anatomy of a Key Result

`[Metric] moves from [baseline] to [target] by [date]. Anchor: [telemetry / cohort / market source | ASSUMPTION].`

Checks before accepting a KR:

1. Is it measurable without shipping anything? If only "launch" satisfies it, it is an output.
2. Does it have a baseline? No baseline, no movement.
3. Is the target anchored? Historical trend, prior experiment, or `[ASSUMPTION]` with a revisit date.
4. Can one team move it? If it needs three teams with no owner, split it or name a coordinating owner.

## 2. Worked Cascade: Strategy to Team

Strategy states: GEM rank Engagement first; GLEe active horizon Get big; exit metric "40% weekly retention across 50 ICP teams" [ASSUMPTION].

Derived team OKR:

- **Objective:** Make the first week so useful customers come back without being asked.
- **KR1:** Week-2 retention from 22% (anchor: Q3 cohort report) to 35% by [date].
- **KR2:** Time from signup to first value from 3 days to 1 day (anchor: onboarding telemetry).
- **KR3:** Share of activated teams using the core workflow weekly from 30% to 50% [ASSUMPTION baseline — instrument first, revisit in 2 weeks].

No KR mentions shipping; the team chooses solutions.

## 3. Bad-to-Good Rewrites

| Output KR (reject) | Outcome KR (accept) |
| :--- | :--- |
| "Ship SSO by Q3" | "Enterprise deals lost to missing SSO: 3 in last two quarters (anchor: CRM loss codes) to 0 by Q4" |
| "Launch mobile app" | "Weekly active ICP users on mobile from 0 to 30% of WAU by [date]" [ASSUMPTION] |
| "Improve performance" | "p95 load from 4.2s to under 2s (anchor: current APM baseline); task abandonment during load down 50%" |
| "Do 10 customer interviews" | Interviews are activity, not result. KR: "top-3 churn drivers confirmed in at least 70% of discovery calls this quarter" [ASSUMPTION threshold] |

## 4. Anti-Patterns

- **Sandbagging:** targets below last quarter's actuals. Anchor against trend, not amnesia.
- **Metric laundering:** vanity metrics (page views) standing in for value (retention, revenue, margin).
- **KR-as-task-list:** numbered deliverables wearing a KR uniform.
- **Unowned KRs:** metrics no single team can move — split or assign a coordinating owner.

## Sources

- Marty Cagan, SVPG — [svpg.com/articles](https://svpg.com/articles/)
- John Doerr, *Measure What Matters* (OKR mechanics: baselines, stretch, cadence)
