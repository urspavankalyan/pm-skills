# Tracking Plan Template

<!-- Fill before build, not after launch. One row per event; every row needs an owner and a verification hook or the event does not ship. -->

```markdown
# Tracking Plan: [Product / Feature]

**Owner:** [person] | **Last-updated:** [YYYY-MM-DD] | **North Star it serves:** [metric]

| Event (`object_action`) | AARRR stage | Trigger (exact) | Properties (additive) | Owner | Verification hook |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `signup` | Acquisition | account created | `channel`, `plan_intent` | [name] | staging fire test + daily volume floor |
| `[first_value_action]` | Activation | first core value within [window] | `source_surface` | [name] | staging fire test + dedupe assertion |
| `[retention_action]` | Retention | session in week 2+ | `cohort_week` | [name] | volume floor per platform |
| `[referral_action]` | Referral | invite sent | `invite_type` | [name] | staging fire test |
| `[revenue_action]` | Revenue | payment confirmed | `mrr_delta` | [name] | dedupe assertion + reconciliation vs billing |

## Change log (schema changes land here, dated, before they ship)
| Date | Event | Change | Author | Expected metric impact |
| :--- | :--- | :--- | :--- | :--- |
| [YYYY-MM-DD] | [event] | [added/renamed/trigger moved] | [name] | [which metric moves, by how much, for how long] |

<!-- Renames and property re-definitions are breaking changes: keep the old event name frozen in history or annotate the breakpoint; never silently overwrite. -->
```
