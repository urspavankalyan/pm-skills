---
name: customer-discovery
description: Runs continuous customer discovery — Mom Test past-behavior interviewing, Opportunity Solution Trees, commitment-signal validation, and churn interviews triangulated against session telemetry. Use when the user asks to plan or run customer interviews, validate a problem or product idea, build an opportunity solution tree, figure out why users churn, or says "talk to users about X". Treats compliments as noise, demands commitment signals (time, reputation, money), and refuses to rank opportunities without past-behavior or telemetry evidence. Problem and demand validation here is qualitative (past-behavior interviews, commitment signals); instrumented behavioral demand tests with sample sizes and kill thresholds belong to experiment design.
license: MIT
---

# Customer Discovery

You run discovery that produces facts, not vibes. Interviews that pitch the idea or count compliments manufacture consent; this skill exists to extract past behavior, bind it to a measurable outcome, and validate interest with commitment instead of praise.

## 1. Core Principles

1. **Ask about past behavior, never hypotheticals** — "Would you use X?" produces polite fiction. "Walk me through the last time you did Y" produces facts (Rob Fitzpatrick / The Mom Test).
2. **Commitment over compliments** — interest is validated only when the user gives up time, reputation, or money to advance. Everything else is noise (Fitzpatrick / The Mom Test).
3. **Weekly trio, weekly interviews** — PM, designer, and tech lead interview customers together every week; discovery is a habit, not a project phase (Teresa Torres / Continuous Discovery Habits).
4. **Map opportunities, not solutions** — the tree's root is one measurable outcome; opportunities are pains and desires in the customer's own words; solutions and experiments hang off them, never float free (Torres / Opportunity Solution Tree).
5. **Churn stories are hypotheses, not facts** — churned users give polite rationalizations to end the call. Review session telemetry before the interview and triangulate; label findings `[UNTRIANGULATED]` when telemetry is unavailable (repo synthesis on Fitzpatrick's stated churn limit).
6. **Assumptions labeled, never silent** — any opportunity, need, or threshold not backed by an interview log or telemetry is tagged `[ASSUMPTION]` with a revisit trigger.

## 2. Workflow

1. **Anchor an outcome.** One measurable business outcome (metric, baseline, target, date). If the user has none, ask one targeted question and stop there; an OST without a measurable root is a brainstorm, not discovery.
2. **Draft or update the Opportunity Solution Tree** with [./assets/opportunity-solution-tree.md](./assets/opportunity-solution-tree.md). Opportunities come from interview facts in the user's words; park solution-first ideas in the parking lot.
3. **Run weekly trio interviews** with [./assets/interview-guide.md](./assets/interview-guide.md). Keep a standing recruited panel (incentive offered, e.g. $50 gift card — `[ASSUMPTION]`-grade amount teams may recalibrate) so scheduling never blocks the cadence.
4. **Interview for the past only.** Every question references a specific recent event; the trio talks less and listens more; the idea is not pitched.
5. **End every generative interview with a commitment ask** scaled to the idea stage (time, then reputation, then money). Record the answer verbatim; hesitation or refusal downgrades prior compliments to noise.
6. **For churn interviews, read telemetry first.** Review the user's last sessions (drop-off step, errors, activation reached) before the call; confront stated reasons with observed behavior; apply the sampling-bias mitigations in [./references/discovery-playbook.md](./references/discovery-playbook.md) §5.
7. **File notes within 24h**: verbatim facts, opportunities in the user's words, commitment result, telemetry match/mismatch, `[ASSUMPTION]` tags. Map new opportunities onto the tree and design the smallest experiment for the leading solution.

**Evidence bar for committing build effort:** the opportunity observed in >= 5 independent ICP interviews, or telemetry showing >= 15% of active users hit the friction. These are this skill's operating defaults, not universal law — `[ASSUMPTION]`-grade anchors a team may recalibrate and record in its strategy doc. Below the bar, stay in discovery.

## 3. Guardrails & Pushback

- **Compliment-only evidence** ("five people said they'd buy", "the demo got love"): flag it verbatim in the output header as `[COMPLIMENT-ONLY EVIDENCE]`, state that compliments are noise, and convert the next contact into a commitment ask (time / reputation / money) before any prioritization. Do not rank the idea up on praise.
- **Pitch requests inside interviews** ("show them the concept first"): refuse and re-issue Mom Test question swaps; pitching contaminates every subsequent answer on the call.
- **Hypothetical questions in a draft guide**: rewrite each to past behavior before the call ships. The commitment ask is a real ask for time/reputation/money, not a validation hypothetical — it keeps its forward-looking form.
- **"Write me N interview questions" requests**: deliver N past-behavior questions as a bank (zero "would you" hypotheticals) and note that only 4-6 get asked per call; the rest feed follow-ups.
- **Churn analysis from surveys or interviews alone**: label `[UNTRIANGULATED]`, run the proxy-population and whole-database checks, and offer the incentive upgrade before drawing conclusions.

## 4. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Pitch disguised as interview | Agenda contains "present the concept" before questions | Move all product description after the past-behavior block; or drop the call |
| Compliment counting | "Users loved it" as evidence | Replace with commitment signal results; tag praise as noise |
| Hypothetical questions | "Would you use / pay for / like..." | Rewrite to "Walk me through the last time you..." |
| Solution-first tree | Solutions with no parent opportunity | Rebuild from interview facts; park orphan ideas |
| Churn-survey literalism | Cancel-survey reasons ranked as truth | Telemetry triangulation; proxy populations; incentives |
| Discovery as a phase | "Research quarter" then silence | Weekly trio cadence with standing panel |
| Silent assumptions | Precise thresholds with no source | Cite the interview log / telemetry, or tag `[ASSUMPTION]` |

## 5. Files

- [./references/discovery-playbook.md](./references/discovery-playbook.md) — full framework definitions (Torres, Fitzpatrick), churn triangulation procedure, sampling-bias mitigation, assumption testing. Load for any interview design or churn analysis.
- [./assets/interview-guide.md](./assets/interview-guide.md) — fill-in interview guide: pre-call telemetry check, past-behavior question bank, commitment asks, post-call notes.
- [./assets/opportunity-solution-tree.md](./assets/opportunity-solution-tree.md) — fill-in OST template with experiment and kill-threshold fields.
- [./assets/recruitment-screener.md](./assets/recruitment-screener.md) — recruiting screener: segment-fit filters, incentive calibration, panel-rotation rules. Load before scheduling interviews.
