# Tracking Plans & Event Taxonomies Reference

Step-0 diagnoses broken instrumentation; this file builds instrumentation that cannot silently break. A tracking plan is a contract between product and data: every event has one stage, one owner, and one verification hook.

## 1. One Stage, One Event (AARRR discipline)

**Definition.** Each funnel stage maps to exactly one distinct telemetry event; stages never overlap. "Invited a colleague" counting as both activation and referral makes diagnosis impossible (Dave McClure / AARRR; the separation rule in [./diagnosis-playbook.md](./diagnosis-playbook.md) §3).

**When to use.** Designing telemetry for a new product or restructuring a mixed one. **When NOT to use.** As a growth strategy; the plan is instrumentation, loops are strategy.

**Worked Example.** A SaaS tool wires `signup` (acquisition), `first_project_created` within 24h (activation), `session_start_week_2` (retention), `invite_sent` (referral), `converted_to_paid` (revenue). A drop in one event isolates to one stage.

**Source URL.** [mindtheproduct.com](https://www.mindtheproduct.com)

## 2. Naming & Ownership Rules

- Event names are `object_action` snake_case, stable forever; renaming an event is a schema change and must run through the change discipline (§4), because history comparison dies with renames.
- Every event names an **owner** (a person, not a team) and a **verification hook**: the staging test or assertion that fails if the event stops firing or double-fires.
- Properties are additive-only by default; removing or re-defining a property is a schema change.

## 3. Verification Hooks

An event without a verification hook is unauditable. Minimum set:

1. **Staging fire test** — the event appears in the staging stream within the test run (CI assertion where possible).
2. **Volume floor** — a daily monitor alerts when volume falls outside the expected band vs the prior 4 weeks (per platform, to catch SDK outages that Step-0 looks for).
3. **Duplication check** — session-level dedupe assertion on the highest-stakes events (activation, revenue).

## 4. Change Discipline (the flip side of Step-0)

Every schema/trigger change lands as a dated entry in the tracking plan: date, event, change, author, expected metric impact. When Step-0 runs, this log is the first artifact consulted — the change that explains a movement is usually in the last two weeks of this file. Silent tracking changes are the root cause of most phantom "product" diagnoses.

## 5. Sources

- AARRR & stage separation: Dave McClure — [mindtheproduct.com](https://www.mindtheproduct.com)
- Schema-change discipline mirrors analytics-engineering practice (dbt-style test-on-staging); no external author claimed.
