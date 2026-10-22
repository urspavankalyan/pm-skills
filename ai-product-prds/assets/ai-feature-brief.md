# AI Feature Brief Template

<!-- Eval-first template. Every placeholder becomes a concrete claim, an anchored number, or an [ASSUMPTION] tag. Delete unused sections; never ship brackets. -->

```markdown
# AI Feature Brief: [Name]

**Stakes class:** [low | medium | high] | **Owner:** [name] | **Date:** [YYYY-MM-DD]
**Status:** [Draft | Approved] | **Eval base:** [golden set vX, n=NNN | EVIDENCE-FREE]

## 1. Problem & Job
- [Whose pain; what they do today; why AI is the right instrument vs a deterministic one]

## 2. Eval Base (exists before model choice)
- **Golden dataset:** [n cases; provenance; stratification; holdout %; version]
- **Graders:** [type; calibration sample n; agreement = NN% or kappa; anchor/ASSUMPTION]
- **Human eval cadence:** [e.g. 50 production outputs/week per surface]

## 3. Acceptance Criteria (eval thresholds)
| Metric | Threshold | Anchor |
| :--- | :--- | :--- |
| Task success vs baseline | [>= NN%] | [current flow / human reference] |
| Faithfulness (hallucination) | [<= N% ungrounded claims] | [measured baseline | ASSUMPTION] |
| Format/validity failures | [<= N%] | [ASSUMPTION if unmeasured] |
| p95 latency | [<= N ms] | [user-experience anchor] |

## 4. Human-in-the-Loop & Escalation
- **Pattern by stakes:** [sampling | confidence queue at t=NN | approval before external effect]
- **Escalation ladder:** [auto check -> queue -> owner + SLA -> incident review]
- **User controls:** [edit, regenerate, cite sources, report]

## 5. Cost Gate
- Tokens/action: [in/out, measured or ASSUMPTION] | Prices: [list, dated; refresh trigger]
- cost/action = [show math] | Volume = [actions/month] | Monthly = [$]
- Incremental margin/action = [$] | Gate (cost <= NN% of margin): [PASS/FAIL + levers if FAIL]

## 6. Failure Modes
| Mode | Detection (threshold) | Mitigation (owner, cadence) |
| :--- | :--- | :--- |
| Hallucination | [faithfulness bar] | [grounding/abstain/HITL] |
| Drift | [regression diff; weekly disagreement] | [pinned versions; canary] |
| Prompt injection | [red-team suite bar] | [data-not-instructions; confirm side effects] |
| Cost explosion | [alert at Nx budget] | [caps, tiers, caching] |
| Automation bias | [planted-defect catch rate] | [blind plants, audits] |

## 7. PII & Liability
- [Data entering context; minimization; retention; consent/disclosure; residency]
- [Accountable owner for wrong outputs; user recourse path; counsel involved: yes/no]

## 8. Versioning & Rollback
- Registry entry: [prompt hash, model id + snapshot, dataset version, grader version]
- Change rule: [eval diff >= baseline; no guardrail regression > Npt] | Rollback: [pin last passing]

## 9. Kill Criteria
- [Post-launch: eval bar breached N weeks running, cost/action > gate, or catch rate < floor -> revert; revisit date]
```
