# User Story Template

<!-- Default narrative is the JTBD job story. Delete unused sections; never ship bracketed placeholders. -->

```markdown
# Story: [Short outcome-oriented title, e.g. "One-click picking lists for high-volume mornings"]

**Outcome it serves:** [metric from outcome brief, baseline -> target, e.g. Week-2 merchant retention 31% -> 40% by Q3]
**Experiment of:** [one-line hypothesis this story tests]
**Evidence:** [interview log / telemetry citation, e.g. 4 of 7 churn interviews cited morning packing delays] <!-- no evidence? tag [ASSUMPTION - outcome unvalidated] -->

## Narrative (JTBD job story — default)
When [situation, observable circumstance],
I want to [motivation / behavior],
so I can [expected progress, the outcome in the customer's words].

<!-- Alternate form only if the user asks for it; keep the situation clause:
As a [persona], I want [behavior], so that [outcome]. -->

## Acceptance criteria (Gherkin)
Scenario: [primary path name]
Given [context, including data scale and preconditions]
When [single triggering action]
Then [observable, measurable result]
And [edge condition or bound, each with anchor or [ASSUMPTION]]

Scenario: [edge / failure path name]
Given [context]
When [trigger]
Then [observable fallback behavior]

## INVEST check
- [ ] Independent — can be scheduled and released alone
- [ ] Negotiable — card invites conversation; detail not frozen
- [ ] Valuable — delivers a slice of customer/outcome value by itself
- [ ] Estimable — understood enough to size against the team's cadence
- [ ] Small — fits the team's horizon ([stated cadence, e.g. one sprint / fraction of a 6-week cycle]; unknown cadence = [ASSUMPTION])
- [ ] Testable — Gherkin above can falsify it
<!-- Any unchecked box: split using craft.md patterns before this story enters a slice. -->

## Split record (fill only if split)
**Pattern used:** [by workflow / by business rule / by data variation / by interface variation / by spike]
**Children:** [titles of child stories; each must pass Valuable and Testable alone]

## Experiment note
**Signal:** [metric delta, usage event, or interview finding expected; anchor stated or [ASSUMPTION]]
**Window:** [observation period after release]
**Decision if absent:** [kill / pivot / iterate — named, dated]
```
