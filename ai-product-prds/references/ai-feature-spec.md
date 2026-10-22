# AI Feature Spec Reference (Eval-First Development)

Every rule below serves the brief template in [../assets/ai-feature-brief.md](../assets/ai-feature-brief.md). Thresholds without a measured anchor are labeled `[ASSUMPTION]` with a revisit trigger.

## 1. Golden Dataset Before Model Choice

- **Order of work** — curate the golden dataset first; choose model and prompt second. Teams that pick a model first optimize the wrong thing and lose the ability to compare (Anthropic; OpenAI eval guidance).
- **Shape** — representative real inputs; reference outputs or a scoring rubric per case; provenance (source, date, consent status); stratification over the segments you will read; a holdout split (20-30%) that iteration never touches [ASSUMPTION split; revisit on variance].
- **Size anchor** — start at ~100 goldens for a narrow task (eval-driven-development practice, e.g. Confident AI/DeepEval's EDD recipe); grow toward 300+ as segments and failure cases accumulate [ASSUMPTION; revisit when a segment's CI on pass rate exceeds +/-10pt].
- **Versioning** — the dataset is code: versioned, diffable, with changelog entries for added/relabeled cases.

## 2. Grader Agreement & Human Eval Cadence

- **Grader agreement** — before trusting any auto-grader or LLM-as-judge, dual-grade a calibration sample: require >= 80% pairwise human agreement or Cohen's kappa >= 0.6 [ASSUMPTION anchor: common convention; recalibrate per task], then require the LLM judge to match humans at >= that bar on the same sample.
- **Cadence** — automated evals run on every prompt/model/dataset change (CI gate); human evals sample production output weekly, e.g. 50 sessions/week per surface [ASSUMPTION; scale with traffic and stakes].
- **Drift watch** — disagreement trending up across weekly human samples is a drift signal, not noise (see ai-risks.md §2).

## 3. Quality Bars as Acceptance Criteria

Write each bar as metric + threshold + anchor. Defaults when no measured baseline exists (all `[ASSUMPTION]`, revisit after first eval run):

| Surface stakes | Faithfulness / hallucination bar | Review rule |
| :--- | :--- | :--- |
| High (external, consequential: medical, legal, financial) | ungrounded claims <= 2% on golden holdout | human approval before external effect until cadence proves stability |
| Medium (user-facing, reversible) | ungrounded claims <= 5% | spot review at weekly cadence |
| Low (internal, assistive) | ungrounded claims <= 10% | sampling only |

Also register: task-success rate vs baseline (anchor: current non-AI flow or human reference), format/validity failure rate (e.g. <= 1% [ASSUMPTION]), p95 latency with user-experience anchor, and abstain/refusal behavior (the system must say "can't answer" rather than invent).

## 4. Human-in-the-Loop & Escalation Design

- **Stakes class drives pattern**: low -> post-hoc sampling; medium -> confidence-routed queue (route below threshold t to humans; t = 0.7 default [ASSUMPTION]) + user edit/regenerate surface; high -> human approval before any external effect + named escalation owner and SLA.
- **Escalation ladder** — automated check -> human queue -> named owner with SLA -> incident review when a registered bar is breached in production.
- **User controls** — every generative surface ships edit, regenerate, cite-sources and report paths; the report path feeds the golden dataset.

## 5. LLM Cost per Action as Feasibility Gate

Model cost per action before roadmap commitment:

```
cost/action = (in_tokens * price_in + out_tokens * price_out) / 1,000,000
            + grader/retry overhead factor (use 1.2 until measured [ASSUMPTION])
monthly cost = cost/action * actions/month
gate: cost/action <= margin share * incremental margin/action
```

Worked example (illustrative list prices at time of writing — refresh before deciding; tag `[ASSUMPTION]` if unverified): 1,500 in + 500 out tokens at $3/1M in, $15/1M out = $0.0045 + $0.0075 = $0.012/action; at 1M actions/month = $12k/month. If incremental margin per action is $0.02 and the policy cap is 30% of margin [ASSUMPTION policy], $0.012 > $0.006 -> infeasible at that scope; levers: cheaper tier for the draft pass, trigger/debounce instead of every-event, cache hits, paid-tier-only rollout. Recompute each lever; show the table.

## 6. Prompt / Model Versioning

- Registry entry per shipped behavior: prompt id + content hash, model id + snapshot date, dataset version, grader version, eval results summary.
- **Change rule** — no change ships without an eval diff: all registered bars >= baseline and no guardrail bar regresses > 2pt [ASSUMPTION]; otherwise block or exception-sign.
- **Rollback rule** — pin to last passing registry entry; rollback is a config change, not an incident scramble.
- Provider model deprecations are scheduled work: the registry tells you exactly which behaviors to re-eval when a snapshot retires.

## 7. PII & Liability

- **Data flow inventory** — what enters the context window (user content, retrieved docs, metadata); minimize; state retention and deletion; mask PII in the golden set via a redaction pipeline before it is stored.
- **Consent & disclosure** — where user data feeds the model or training, state the consent basis and the user-facing disclosure; regional residency constraints named.
- **Liability** — name the accountable owner for wrong outputs per stakes class; state the recourse path for affected users. A disclaimer is disclosure, not a control.
- **Regulated domains** — health, finance, legal, minors: involve counsel before the PRD is final. This file is product practice, not legal advice.

## 8. Pushback: Minimal Eval Plan (detail)

For evidence-free "add AI" requests (SKILL.md §5), the 1-week plan in concrete steps: day 1-2 pull 50-100 real cases + draft rubric; day 3 dual-grade 20 (agreement gate); day 4 score candidate prompt on holdout; day 5 cost-per-action from measured tokens + decision memo (fund / refine / kill). Each threshold carries its anchor or `[ASSUMPTION]` tag.

## 9. Sources

- Anthropic — Demystifying evals for AI agents: [anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- OpenAI — Working with evals & evaluation best practices: [platform.openai.com/docs/guides/evals](https://platform.openai.com/docs/guides/evals)
- Eval-driven development practice (~100 goldens, 3-5 metrics): [deepeval.com/blog/eval-driven-development](https://deepeval.com/blog/eval-driven-development)
- Cagan — four product risks framing stakes: [svpg.com/articles](https://svpg.com/articles/)
