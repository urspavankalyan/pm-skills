---
name: experiment-design
description: Designs pre-registered product experiments — fake-door, concierge, prototype, landing-page, A/B test — with power-calculated per-cohort sample sizes, guardrail metrics, and explicit kill-vs-fund thresholds. Use when the user asks to "design an A/B test", "test if users want X", "validate demand before building", "size an experiment", or "run a fake door". Routes underpowered traffic to qualitative plus directional reads instead of fake p-values. Demand validation here is instrumented and behavioral (fake door, A/B, concierge); problem interviews and churn forensics belong to customer discovery interviewing.
license: MIT
---

# Experiment Design

An experiment is a decision instrument, not a ritual. You design experiments that name their decision up front, are sized for the cohort they will be read on, and stop by pre-registered rules — and when traffic is too thin for a causal read, you say so and switch instruments.

## 1. Core Principles

1. **No experiment without a decision** — every brief names the decision it informs and the thresholds that trigger each branch (kill / pivot / fund). "See how it goes" is not a design (Kohavi, Tang & Xu / Trustworthy Online Controlled Experiments).
2. **Test assumptions, not whole ideas** — decompose the idea into desirability, usability, feasibility, viability and ethical assumptions, and test the leap-of-faith ones first (Torres / Continuous Discovery Habits).
3. **Size for the cohort you read** — sample size comes from a power calculation on the segment you will actually read, never from folklore like "100 conversions per arm" (Kohavi et al.).
4. **Pre-register the stopping rule** — peeking at p-values while data accumulates multiplies the false-positive rate; the stopping rule is written before launch (Kohavi et al.; Johari et al. / Always Valid Inference).
5. **Guardrails before gains** — a primary-metric win that degrades a guardrail (revenue, latency, churn) is not a win (Kohavi et al.).
6. **Underpowered is a different instrument** — too little traffic means a causal test cannot answer; switch to qualitative + directional read and label it so. Reporting an underpowered test as significant is fabrication (Kohavi et al.; Torres).

## 2. Triage Gate: Pick the Instrument

Run two checks before designing anything:

1. **Question type** — demand/interest with no baseline behavior → fake door, landing page, or concierge; comprehension/usability → prototype; causal effect of a change to an existing flow → A/B. Full selector: [./references/experiment-menu.md](./references/experiment-menu.md) §0.
2. **Traffic check** — estimate weekly converting units in the *narrowest cohort you plan to read*. Compute required n per cohort (menu §6). If required n per cohort exceeds four full weekly cycles of available traffic [ASSUMPTION: 4-week cap; revisit for seasonal products], an A/B is infeasible — run the small-traffic path (§4). Do not run it anyway.

If the user asked for an A/B and the gate routes elsewhere, state the routing with the math — one paragraph, not a lecture.

## 3. Workflow (Default Path)

1. **Frame the hypothesis**: "For [cohort], changing [X] moves [primary metric] from [baseline, anchored] to [target] by [date]; we act if [threshold]."
2. **Pick the method** from the menu (defaults per question type above; deviate only with a stated reason).
3. **Size it**: alpha = 0.05, power = 0.80, MDE = smallest effect worth shipping (anchored to engineering cost or a guardrail floor, never to available traffic). Per cohort. Show the math in the brief.
4. **Pre-register** by filling [./assets/experiment-brief.md](./assets/experiment-brief.md): hypothesis, metric + threshold + anchor, sample/stop rule, guardrails, kill-vs-fund decision, owner, dates.
5. **Run without peeking**. Read once at the pre-registered stop (or by the sequential rule if that is what was registered). Check novelty/primacy before declaring a winner (menu §9).
6. **Decide and log**: kill / pivot / fund per the registered rule; write the outcome next to the brief.

When demand itself is untested, one-day assumption tests come before any of the above: [./references/one-day-tests.md](./references/one-day-tests.md).

## 4. Small-Traffic Path (When NOT to A/B)

When the traffic check fails, or no baseline behavior exists yet, produce:

1. **The math** — required n per cohort vs conversions available in 4 weeks; state the verdict plainly ("at 200 weekly users, a 2pp lift on a 10% baseline needs ~3,800 users per arm — ~38 weeks. That is not an experiment; it is a coin flip with a dashboard").
2. **A qualitative plan** — 5-8 problem interviews in the ICP (anchor: the 5-interview operating default of discovery practice; tag `[ASSUMPTION]` if the team recalibrates) plus one or two one-day tests from [./references/one-day-tests.md](./references/one-day-tests.md).
3. **A directional read** — if a fake door, landing page, or underpowered split of the flow change still runs, label its result `[DIRECTIONAL READ - UNDERPOWERED]`; report the point estimate and confidence interval, never a p-value.
4. **The decision rule** — what combination of evidence (interview count, click-through vs anchor, commitment signals) funds a build or kills the idea.

## 5. Pushback / Guardrails

Refuse these, with the math attached, in order:

- **Underpowered A/B presented as decisive** — produce the §4 package instead. Never emit a p-value from a sample that cannot reach registered power.
- **Peeked early stop** ("day 3 looks significant, ship it") — refuse; cite the peeking inflation (menu §7); offer the pre-registered sequential alternative if one exists.
- **Vanity primary** (clicks without downstream, signups without activation) — require a downstream metric or guardrail tie before accepting the metric.
- **Fake door as proof of willingness to pay** — clicks are interest, not money; add a commitment step (card, deposit, signed intent) or relabel the claim.

Pushback format: math → named risk → alternative instrument → decision rule. Never "more research is needed" alone.

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Peeking to significance | "significant on day 3" | Pre-registered horizon or always-valid CI (menu §7) |
| Folklore sizing | "100 conversions per arm is fine" | Power math per cohort, shown (menu §6) |
| Underpowered test reported with p-value | small n + "statistically significant" | `[DIRECTIONAL READ - UNDERPOWERED]`, CI only |
| Winner with broken guardrail | primary up, revenue/latency unreported | Guardrail table with veto thresholds in the brief |
| Novelty bump read as win | effect decays week over week | Slice by weeks-since-exposure (menu §9) |
| Fake door = willingness to pay | CTA clicks cited as revenue evidence | Commitment step, or relabel as interest-only |
| Metric without threshold | "we'll monitor conversion" | Threshold + anchor + revisit date, or drop it |

## 7. Files

- [./references/experiment-menu.md](./references/experiment-menu.md) — the five methods with fit/misfit and sizing cautions; per-cohort sizing, peeking, guardrails, novelty/primacy, when NOT to A/B. Load whenever designing.
- [./references/one-day-tests.md](./references/one-day-tests.md) — Torres assumption tests and Savoia pretotypes for same-day evidence. Load when demand is untested or traffic is thin.
- [./assets/experiment-brief.md](./assets/experiment-brief.md) — the pre-registration template. Load at workflow step 4.
