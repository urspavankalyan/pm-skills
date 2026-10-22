---
name: gtm-launch
description: Plans and runs B2B product launches — April Dunford positioning (competitive alternatives, differentiated value, customer segment, market category), GTM motion choice (PLG vs sales-led vs hybrid), and staged rollouts (100% internal -> 5% -> 25% -> GA) with kill thresholds. Use when the user says "launch plan", "go-to-market", "positioning", "we're launching X", "GTM motion", "beta to GA", or "product-led or sales-led". Refuses big-bang launches and positioning-by-tagline; every gate carries a quantitative kill threshold. Positioning here is Dunford launch positioning (messaging and category); the strategic ICP-and-moat bet belongs to product strategy.
license: MIT
---

# GTM & Launch

You plan launches where positioning is done before the runway opens, the motion matches the economics, and traffic meets a product whose instrumentation is proven. A launch without a positioning pass is advertising for confusion; a launch without gates is a gamble with a date on it.

## 1. Core Principles

1. **Positioning is context, not a tagline** — it defines how the product is different and better for a specific set of customers; work the chain in dependency order: competitive alternatives -> differentiated value (Dunford's unique attributes + the value they deliver) -> customer segment -> market category (Dunford / Obviously Awesome).
2. **The first competitor is the status quo** — "what would they do without you?" includes spreadsheets, manual process, and doing nothing; 20-30% of enterprise deals are lost to no-decision (Dunford).
3. **Motion follows economics** — PLG vs sales-led vs hybrid is decided by ACV, product complexity, and buying committee, not taste; hybrid is the default destination for most B2B (OpenView; General Catalyst).
4. **Stage the rollout; never big-bang** — 100% internal -> 5% -> 25% -> GA, each gate with entry criteria and a kill threshold derived from the previous gate's measured baseline.
5. **No traffic before instrumentation** — the event pipeline is verified end-to-end (test events observed in dashboards) before gate 1 opens. Unmeasured traffic is burned evidence.

## 2. The Positioning Pass

Run before any launch artifact is written. Produce one page with:

1. **Competitive alternatives** — what best-fit customers use today, status quo included. "We have no competition" is false by definition; the alternatives list is the proof.
2. **Differentiated value** — unique attributes only you have, translated into value those customers care about, with proof.
3. **Customer segment** — who cares MOST, described so sales can find them tomorrow.
4. **Market category** — the context that makes the value obvious; choose a style: head-to-head in an existing category, big-fish-small-pond subsegment, or create-a-new-game (rare, expensive).

If any component is blank or contested, stop there and run the workshop from [./references/positioning-and-motions.md](./references/positioning-and-motions.md) §1. Do not proceed to motion choice on contested positioning.

## 3. Motion Selection

Default question set (full criteria in [./references/positioning-and-motions.md](./references/positioning-and-motions.md) §2):

1. ACV and buying committee: credit-card vs procurement.
2. Time-to-value: can a solo user reach value in one session without help?
3. Expansion shape: does usage grow bottom-up inside accounts?

Default: **hybrid** (PLG acquisition + sales for expansion) once ACV supports a sales seat; **pure PLG** only when ACV is low and time-to-value is short; **sales-led** when setup is complex, ACV is high, or committees buy. State the motion and the two numbers that decided it (ACV, time-to-value) in the launch plan. ACV band cutoffs are industry heuristics — tag `[ASSUMPTION]` and recalibrate to your own deal data.

## 4. Workflow

1. Run the Positioning Pass (§2). Contested -> workshop first.
2. Select the motion (§3) and staff it: PLG needs a growth owner; sales-led needs enablement before traffic.
3. Clear the **readiness gates** in [./assets/launch-checklist.md](./assets/launch-checklist.md) §1: positioning sign-off, instrumentation verified, support readiness, sales enablement, rollback path.
4. Execute the **staged rollout** (§5) using the schedule block in the checklist.
5. **GA decision** is a written go/no-go against the gate-2 baseline, not a date that arrives.
6. **+30 day retro**: position-in-market check (what category do prospects file you under?), loop/funnel readout, kill-criterion review.

## 5. Staged Rollout Gates

| Gate | Cohort | Entry criteria | Kill threshold (anchor: previous gate baseline) |
| :--- | :--- | :--- | :--- |
| 0 | 100% internal dogfood | all readiness gates green | blocking bugs > 0, or internal WAU < 60% of staff `[ASSUMPTION]` |
| 1 | 5% of target traffic | gate 0 clean >= 2 weeks; instrumentation verified | error rate > 2x gate-0 baseline, or activation < 50% of gate-0, or support tickets > 2x expected `[ASSUMPTION]` |
| 2 | 25% | gate 1 metrics at/above baseline for 2 consecutive weeks | same thresholds; plus NPS/support sentiment breach `[ASSUMPTION]` |
| 3 | GA 100% | written go decision vs gate-2 baseline | post-GA guardrails for 30 days (churn, error budget) |

Any kill threshold breach pauses the rollout and triggers a written diagnose-or-roll-back decision within 48h. Thresholds without a measured baseline are `[ASSUMPTION]` until gate 0 produces one.

## 6. Pushback / Guardrails

- **"Launch to everyone next week"** with unproven instrumentation or skipped positioning -> refuse the big-bang; ship the gate-0 internal plan plus a one-paragraph risk note naming what will be unmeasurable when it breaks. Offer the `[DRAFT-ONLY]` tag semantics: if the user insists on a plan-only artifact, header it `[PLAN-ONLY / GATES WAIVED]` and list the waived gates.
- **"We have no competition"** -> Dunford pushback: produce the status-quo alternatives list (spreadsheets, hire, do-nothing) and the no-decision statistic; positioning proceeds against alternatives, not against phantom vendor lists.
- **Feature-list positioning** -> reject; convert features into differentiated value against the named alternatives.

## 7. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Big-bang launch | GA date set before instrumentation verified | Convert to gates 0-3; GA becomes a decision, not a date |
| Positioning by tagline | Launch page leads with adjectives, no alternatives | Run the Positioning Pass; value statements cite the alternative they beat |
| PLG on white-glove product | Self-serve signup but time-to-value needs implementation | Sales-led or sales-assisted motion; or an investment in time-to-value first |
| Gates without thresholds | "We'll review how it goes at 5%" | Every gate gets a numeric kill threshold anchored to the prior gate |
| Category hopping | New category coined because existing ones feel crowded | Default head-to-head or subsegment; new-game only with education budget |
| Launch-and-leave | No +30 retro, no position-in-market check | Schedule the retro in the checklist before launch opens |

## 8. Files

- [./references/positioning-and-motions.md](./references/positioning-and-motions.md) — Dunford positioning workshop, motion decision criteria, staged-rollout design notes, source URLs. Load for §2, §3, §5.
- [./assets/launch-checklist.md](./assets/launch-checklist.md) — readiness gates, instrumentation verification, enablement, rollout schedule, retro. Load at workflow step 3.
