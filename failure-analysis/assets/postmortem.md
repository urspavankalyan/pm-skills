# Postmortem & Kill-Retro Template

<!-- Facts cite sources; inferences labeled; mechanisms, not people; every action item falsifiable. -->

```markdown
# Postmortem: [Outcome / Incident] | [YYYY-MM-DD]

**Status line:** [what failed, one sentence, numbers + sources]
**Step-0 (data verdict):** [instrumentation verified / tracking issues found — the failure data itself is checked before the story]

## Timeline (fact vs inference)
| Date | Event | Fact ([source]) or [INFERENCE] |
| :--- | :--- | :--- |
| ... | ... | ... |

## Causal Candidates (one per risk family minimum, then ranked)
| Rank | Candidate | Risk family | Evidence class | Evidence |
| :--- | :--- | :--- | :--- | :--- |

## Mechanism Statement
Given these facts, the system made this outcome likely because [incentives / information flow / tooling / ambiguous authority]. No person is the mechanism.

## Action Items
| Item | Owner | Verifiable-done | Date |
| :--- | :--- | :--- | :--- |

(Entries lacking a verifiable-done are cut or converted. "Be more careful" does not ship.)

## Resolution Write-Back
- `product/decisions.md` entry "[name]" updated: **Resolution** [outcome vs prediction; calibration note in words; sunk-cost audit: was the kill/halt honored on time?]

---
# Kill-Retro Variant (use when a kill criterion fired)

- **Original prediction (verbatim):** [quote] | **Kill criterion (verbatim):** [quote]
- **Outcome:** [observed] | **Kill honored on:** [date, on-time / delayed N days — and the incentive that delayed it]
- **Calibration lesson (words, no small-sample stats):** [which risk family was over/underweighted; evidence class too weak? criterion unanchored?]
- **Relaunch rule:** same idea returns only as a new journal entry with a new evidence bar.
```
