# AI Failure Modes & Mitigations

One entry per failure mode: definition, detection signal, mitigation, source. Every brief's Failure Modes section pulls from this list; each mitigation gets an owner and a check cadence.

## 1. Hallucination

- **Definition** — confident, fluent output ungrounded in retrieved sources or facts; the default failure mode of generative surfaces.
- **Detection** — faithfulness evals against source documents on the golden holdout; citation-presence and citation-support checks; weekly human sampling (ai-feature-spec.md §2).
- **Mitigation** — grounding (retrieval with citations), abstain thresholds ("can't answer" over invention), stakes-based review rules (spec §3-4). Never a disclaimer as the only control.
- **Source** — Anthropic and OpenAI eval guidance (see spec §9).

## 2. Drift (Model & Distribution)

- **Definition** — behavior changes without a product change: provider model updates, snapshot deprecations, or input distribution shifting under the prompt.
- **Detection** — regression evals on every deploy; pinned-version eval diff; weekly human sample disagreement trending up.
- **Mitigation** — pin model snapshots in the version registry; treat provider deprecations as scheduled re-eval work; canary a share of traffic on new snapshots before full cutover (spec §6).
- **Source** — OpenAI model lifecycle/deprecation docs; Anthropic evals (spec §9).

## 3. Prompt-Injection Surface

- **Definition** — attacker-controlled text (direct user input, or indirect via retrieved pages, emails, tickets) steering the model into unauthorized behavior or data exfiltration.
- **Detection** — red-team suite in CI; treat injection resistance as a registered eval bar for any surface that reads external content (OWASP LLM Top 10, LLM01).
- **Mitigation** — treat retrieved content strictly as data, not instructions; least-privilege tool access; require explicit user confirmation for side effects (send, pay, delete); separate guardrail calls from the core model where stakes demand.
- **Source** — OWASP LLM Top 10: [owasp.org/www-project-top-10-for-large-language-model-applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## 4. Cost Explosion

- **Definition** — spend grows non-linearly: retry loops, context bloat, per-keystroke triggers, viral adoption on unpriced tiers.
- **Detection** — cost telemetry per action, per user, per surface; alert at 2x the modeled budget [ASSUMPTION multiple; revisit after first month].
- **Mitigation** — the cost gate before commitment (spec §5); per-user and per-surface caps; model routing tiers (cheap draft, strong final); caching; debounce/triggers instead of every-event calls.
- **Source** — unit-economics practice; Anthropic evals note cost-per-task tracking via eval suites.

## 5. Automation Bias in Reviewers

- **Definition** — humans over-trust machine output and rubber-stamp it; the HITL layer degrades into a formality, silently removing the control you designed.
- **Detection** — approver edit rate near zero while planted-defect catch rate falls; error rate on approved items rising in audits.
- **Mitigation** — blind planted defects in review queues at a registered rate (e.g. 5% [ASSUMPTION]); forced-edit or forced-justification sampling; monthly audit of reviewer catch rates; rotate reviewers.
- **Source** — automation bias research (Parasuraman & Molloy); human-AI decision-making literature on overreliance.

## 6. Using This File

For each surface in the brief, list the applicable modes with: detection metric + registered threshold (anchor or `[ASSUMPTION]`), mitigation owner, and check cadence. If a mode is claimed "not applicable", say why in one line — silence is not an assessment.
