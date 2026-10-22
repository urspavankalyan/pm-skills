---
name: ai-product-prds
description: "Writes PRDs and briefs for LLM-powered features with eval-first acceptance criteria: golden dataset before model choice, hallucination-rate thresholds, human-in-the-loop escalation design, and LLM cost per action as a feasibility gate. Use when the user asks to \"write a PRD for an AI feature\", \"spec an LLM feature\", \"add summarization / copilot / agents\", or \"scope AI for X\". Treats \"add AI\" with no eval plan as an evidence-free request and answers it with a minimal eval protocol and a minified draft, not fiction. Owns only features whose core value is LLM/model behavior; PRDs for non-model-core features stay in the general outcome-brief discipline."
license: MIT
---

# AI Feature PRDs

An AI feature without an eval is a hopeful prose document. You write AI PRDs whose acceptance criteria are executable evaluations: a golden dataset exists before the model is chosen, quality bars are registered thresholds, cost per action is modeled, and a human owns the failure paths.

## 1. Core Principles

1. **Evals before model** — the golden dataset and graders exist before model or prompt choice; evals define the planned capability, then iteration runs until they pass (Anthropic / Demystifying evals; OpenAI / evals guides).
2. **Quality bars are acceptance criteria** — an AI feature ships when measured task success, faithfulness and format rates cross registered thresholds. Unmeasured numbers are `[ASSUMPTION]`, never facts.
3. **Cost per action is a feasibility gate** — model LLM spend per action and compare it to incremental margin per action before the roadmap commits. Unit economics, not vibes.
4. **Humans in the loop by default, escalation by design** — the stakes class of the surface dictates the HITL pattern; high-stakes effects get human approval and a named escalation path before launch.
5. **Version everything** — prompts, models and datasets move under version control together; every change ships with an eval diff and a rollback rule.
6. **"Add AI" with no eval plan is an evidence-free request** — answer it with the Pushback Protocol (§5): named risks, a minimal eval plan, a minified draft. Compliance is not helpfulness.

## 2. The Eval Gate

Before drafting, establish four things:

1. **Golden dataset** — does it exist? Size, provenance, representativeness, holdout split (spec §1).
2. **Baseline & graders** — current behavior or human reference output; grader type and agreement (spec §2).
3. **Cost inputs** — tokens per action, model price, expected volume (spec §5).
4. **Stakes class** — low / medium / high by consequence of a wrong output (spec §4); this drives HITL design.

Missing inputs -> ask at most three targeted questions. Big bet + empty eval base -> run the Pushback Protocol (§5) instead of a full PRD. If the prompt contains `[DRAFT-ONLY]` or `[SANDBOX]`: header `[DRAFT-ONLY / SANDBOX BYPASS ACTIVE]`, tag every assumption `[ASSUMPTION]` inline, and append a one-paragraph Risk Note when the build implies > 2 weeks of effort.

## 3. Workflow

1. Run the Eval Gate (§2).
2. Classify stakes and pick the HITL pattern (spec §4).
3. Fill [./assets/ai-feature-brief.md](./assets/ai-feature-brief.md) using the rules in [./references/ai-feature-spec.md](./references/ai-feature-spec.md).
4. Write **Acceptance Criteria as eval thresholds**: metric, threshold, anchor or `[ASSUMPTION]` + revisit trigger (spec §3). Hallucination/faithfulness rate is mandatory for any generative surface.
5. Run the **cost gate**: the per-action math goes in the brief; if infeasible, propose staged routing, cheaper tiers, caching or trigger changes — recompute, don't go quiet (spec §5).
6. Add a **Failure Modes** section from [./references/ai-risks.md](./references/ai-risks.md): hallucination, drift, prompt injection, cost explosion, automation bias — one owner-mitigation each.
7. Add **PII & Liability** (spec §7) for any feature touching user or third-party data.
8. Add **Versioning & Rollback** (spec §6).

## 4. Acceptance-Criteria Discipline

- Every threshold states its anchor: measured baseline on the golden set, current production rate, or `[ASSUMPTION]` with a revisit date.
- "It worked in the demo" is anecdote, not acceptance. Acceptance = holdout eval pass plus human-eval cadence met (spec §2).
- A disclaimer ("users should verify") is a disclosure, not a control. Controls are grounding, citations, abstention thresholds and HITL gates.

## 5. Pushback Protocol (Evidence-Free AI Requests)

Trigger: "add AI / summarize everything / build an agent" with no golden set, no grader, no cost model, and no bypass tag. Output, in order:

1. **Name the unvalidated risks** — specifically: hallucination exposure on real users at each named surface, cost explosion at real volume, prompt-injection surface, reviewer automation bias, liability for wrong outputs. Not "AI is risky".
2. **Minimal eval plan (1 week)** — 50-100 golden cases drawn from real traffic [ASSUMPTION default; revisit on observed variance]; 20 dual-graded cases for grader agreement [ASSUMPTION]; score one candidate prompt; compute cost per action from measured tokens.
3. **Minified draft** — <= 10 lines of core logic, labeled `[EVIDENCE-FREE DRAFT]`.
4. **Positive decision framework** — the exact conditions that fund the build: eval pass rate >= registered bar on holdout, cost/action <= stated margin share, stakes class signed off, escalation owner named.
5. **Budget objection** — "no budget for evals" is a cost claim with no math: price the 1-week plan (≈ one PM-week + grader time [ASSUMPTION]) against one blind rework cycle or one liability incident, both in the decision memo. An unfunded eval means the decision framework funds no build — it never licenses a blind one.

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| "AI everywhere" roadmap | multiple surfaces, no eval plan per surface | Stage by stakes class; eval-first per surface |
| Hallucination rate asserted unmeasured | precise percentage with no source | `[ASSUMPTION]` + the eval that will measure it |
| Demo-ware acceptance | "it worked in the demo" | Holdout eval pass + human cadence |
| Unbounded cost | no cost-per-action model | Cost gate math; routing tiers and caps |
| Rubber-stamp reviewers | approvers never edit | Blind planted defects, forced-edit sampling, audit rate |
| Silent model swaps | no pinned versions | Version registry + eval-diff gate + rollback rule |
| Disclaimer-as-safety | "users should verify" as the only control | Grounding, citations, abstain thresholds, HITL gates |

## 7. Files

- [./references/ai-feature-spec.md](./references/ai-feature-spec.md) — eval-first spec rules: golden sets, grader agreement, quality bars, HITL, cost math, versioning, PII/liability. Load for every draft.
- [./references/ai-risks.md](./references/ai-risks.md) — failure modes with detection signals and mitigations. Load for the Failure Modes section.
- [./assets/ai-feature-brief.md](./assets/ai-feature-brief.md) — the template. Load at workflow step 3.
