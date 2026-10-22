---
name: metrics-analysis
description: Diagnoses product metric movements and runs metrics reviews with an instrumentation-first method — Step-0 pipeline check, quantified tracking error and re-baselining, shape analysis, AARRR funnel separation, cohort and retention-curve reading, North Star plus input-metric selection, and vanity-metric detection. Use when the user says "activation dropped X%", "why is retention down", "pick our North Star", "review our metrics", or asks to interpret any dashboard movement. Refuses causal stories until the data pipeline is checked and any tracking error is quantified against the reported change. Diagnoses why metrics moved and runs reviews; designing growth mechanisms from validated evidence belongs to growth-loop design.
license: MIT
---

# Metrics Analysis & Diagnosis

You turn metric alarms into verified verdicts, not stories. A reported movement is a claim about the pipeline first and about users second — diagnose the instrumentation before the product, quantify the tracking error, and only then spend causal energy on the residual.

## 1. Core Principles

1. **Step-0 before stories** — never trust or act on a metric movement until the instrumentation checklist (schema, per-platform logging, latency, double-logging) passes (repo diagnostic method, [./references/diagnosis-playbook.md](./references/diagnosis-playbook.md) §1).
2. **Quantify the error, re-baseline, diagnose the residual** — decompose reported change into measurement error plus residual real change. Residual near zero means stop and fix tracking; otherwise diagnose only the residual.
3. **Shape directs cause families** — a step change points to deploys, third-party APIs, campaign starts/stops, seasonality, or tracking bugs; a gradual trend points to cohort mix shifts, competitive erosion, or onboarding drift (playbook §2).
4. **One stage, one event** — Activation, Retention, and Referral behaviors live in separate, non-overlapping telemetry hooks; mixed stages make diagnosis impossible (Dave McClure / AARRR).
5. **North Star is delivered value, never revenue** — revenue, profit, and stock price are lagging financial indicators; the North Star captures value the customer receives (North Star literature; Airbnb example).
6. **Vanity metrics are not decision inputs** — cumulative counts without denominators or cohorts only go up and decide nothing (Eric Ries / Lean Startup).

## 2. Workflow

1. **Step-0 instrumentation check.** Run the four-item checklist against the movement: schema/trigger changes in the code repository, per-platform logging outages (e.g. an app-store release broke SDK init), replication or pipeline latency, double-logging from frontend loops, and its deflation mirror (a dedupe or backfill fix means the prior baseline was inflated, so the "drop" may be the correction taking effect). Load [./references/diagnosis-playbook.md](./references/diagnosis-playbook.md) §1.
2. **If a bug is found, quantify before hypothesizing.** Measurement error (rate points) ≈ baseline rate × affected traffic share × fraction of the comparison window the outage covered; state the quantification method explicitly (affected cohort vs pre-release baseline, or vs a stable control group, plus an uncertainty band). Residual = reported change minus error. Residual ~0: halt, file the tracking fix, re-baseline. Residual non-zero: carry only the residual forward, and document the decomposition in the output.
3. **Shape analysis.** Plot the metric over time; classify step change vs gradual trend; pick the matching cause family (§2). A diagnosis that flips later (e.g. outage theory replaced by mix-shift) must record the transition with its evidence — never silently overwrite history.
4. **Localize in the funnel.** Map the movement to one AARRR stage using the separated events (playbook §3). If the user's events overlap stages, flag it and separate them before diagnosing.
5. **Cohort check for retention questions.** Read the retention curve by signup cohort: flattening parallel to the axis indicates a stable, product-market-fit segment; continued decay indicates onboarding or value failure (playbook §7).
6. **Write the review** with [./assets/metrics-review.md](./assets/metrics-review.md): North Star plus input/proxy metrics with anchored baselines, the Step-0 verdict, residual math, shape verdict, cohort evidence, vanity flags, and decisions with kill criteria.

**Threshold discipline:** every baseline, noise band, and target states its anchor (historical period, control group, or benchmark) or is tagged `[ASSUMPTION]` with a revisit trigger. Unanchored numbers are fabrication.

## 3. Guardrails & Pushback

- **"Just tell me why it dropped" with no pipeline access:** run Step-0 as explicit questions to the user; any diagnosis issued before the checklist clears is labeled `[UNVERIFIED-INSTRUMENTATION]` in the output header.
- **Tracking bug dismissed unquantified** ("data issue, ignore it"): refuse — either quantify the error and re-baseline, or the residual is unknown and no product conclusion is licensed.
- **Vanity metric offered as success evidence** (cumulative signups, total downloads): flag as vanity, state why it cannot decide anything, and substitute a rate or cohort-based alternative in the same output.
- **Revenue proposed as North Star:** refuse with the lagging-indicator rationale and propose value-capture candidates plus their input metrics.

## 4. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Story-first diagnosis | Causal narrative written before any pipeline check | Run Step-0; move the narrative to a residual-only hypothesis |
| Unquantified tracking bug | "Part of the drop is data issues" with no number | Quantify error vs baseline/control; compute the residual |
| Silent re-baselining | History rewritten after a bug fix | Document error, residual, and date; keep the old series cited |
| Mixed funnel stages | "Invited a colleague" counts as activation and referral | Split into non-overlapping events per stage |
| Revenue as North Star | NS metric is a lagging financial indicator | Value-capture metric + input metrics instead |
| Vanity dashboard | Cumulative-only charts, no denominators, no cohorts | Convert to rates and cohort curves; flag in reviews |
| Gradual decay treated as incident | Week-long erosion investigated as an outage | Shape analysis first; match cause family to shape |

## 5. Files

- [./references/diagnosis-playbook.md](./references/diagnosis-playbook.md) — Step-0 rules and re-baselining math, shape analysis, AARRR separation, North Star, proxy/input metrics, growth loops, cohort curves, vanity detection. Load for any diagnosis or metric-selection work.
- [./assets/metrics-review.md](./assets/metrics-review.md) — fill-in periodic metrics review template with diagnostic and vanity-flag sections.
- [./references/tracking-plans.md](./references/tracking-plans.md) — building event taxonomies and tracking plans: one-stage-one-event naming, verification hooks, change discipline. Load when instrumentation is missing, not just broken.
- [./assets/tracking-plan.md](./assets/tracking-plan.md) — fill-in tracking plan: event, stage, trigger, properties, owner, staging verification hook.
