# Narrative Techniques: JTBD, Story Mapping, Outcomes

Companion to SKILL.md §2. Load whenever an epic is being decomposed or a story's narrative is being written.

## 1. JTBD job story

- **Definition:** Customers hire products to make progress in a situation. The job story compresses a job into one sentence: "When [situation], I want to [motivation], so I can [expected outcome]." The situation clause is the load-bearing part — it anchors the story in observable circumstance instead of a persona stereotype. Theory: Clayton Christensen & Bob Moesta; the When/I-want/so syntax was popularized at Intercom (Alan Klement).
- **When to use:** whenever a story is written; it is the default narrative form for this skill; especially when stakeholders keep proposing solutions, because the situation clause drags the argument back to the customer's circumstance.
- **When NOT to use:** as a substitute for evidence — a job story is a hypothesis format, not proof; and not for pure technical enablers, which get an experiment note but no fake customer voice.
- **Worked Example (real):** Christensen's canonical case: a fast-food chain studied why milkshakes sold before 8am. Job: "When I'm driving a long boring commute, I want something to do with one hand that keeps me full until lunch, so I can get through the morning." The job — not the demographic — redesigned the product (thicker shake, fruit flecks, faster card). McDonald's, per Christensen.
- **Source URL:** [christenseninstitute.org/key-concepts/jobs-to-be-done](https://www.christenseninstitute.org/key-concepts/jobs-to-be-done/), [hbr.org/2016-09/know-your-customers-jobs-to-be-done](https://hbr.org/2016-09/know-your-customers-jobs-to-be-done)

## 2. Story mapping (Jeff Patton)

- **Definition:** A two-dimensional backlog: the backbone reads left-to-right as the user's activities in narrative order; under each activity sit its steps; under each step sit candidate stories in priority order. Slices cut horizontally across the map are releases. The first slice is the walking skeleton: one thin end-to-end path through every backbone activity, proving the whole shape works before any part gets depth.
- **When to use:** any epic, any "write stories for X" request, any backlog that has become an unreadable flat list; the map is also the artifact that makes the Volume-Demand Protocol productive.
- **When NOT to use:** for a single small story (map overhead exceeds value); and never as a Gantt substitute — slices are learning bets, not committed dates.
- **Worked Example (Hypothetical: B2B invoicing startup):** backbone "draft invoice → send → get paid → reconcile." Walking skeleton: one invoice, one PDF email, one manual bank-line match, one reconciliation flag — end to end, ugly, real. Only after that does "bulk invoice import" earn a slot under "draft invoice," because the skeleton already showed where import fits and which metric (days-to-payment) it probes.
- **Source URL:** [jpattonassociates.com](https://www.jpattonassociates.com/) (Jeff Patton, *User Story Mapping*)

## 3. Outcome-over-output framing

- **Definition:** Success is a change in customer or business behavior (an outcome), not an artifact shipped (an output). Every story therefore states the outcome it probes: a metric with baseline and target, or a job-progress statement. Outputs are spend; outcomes are return. Cagan's empowered-team contract and Perri's Build Trap critique both hinge on this inversion.
- **When to use:** always, at story level and at epic level; an epic is an outcome hypothesis ("enterprise deals stall on security review"), not a bucket ("admin dashboard").
- **When NOT to use:** as an excuse to skip delivery artifacts — outcomes still need outputs; the discipline is that outputs are chosen by the outcome, not the reverse.
- **Worked Example (real):** Netflix's GEM practice makes the framing operational: a bet is argued as moving the active focus factor's proxy (an outcome surface), and the shipped feature is merely the means. A 2005 Monetization-#1 bet was funded on LTV/margin movement, not on "ship cheaper plans" as an output. Gibson Biddle.
- **Source URL:** [svpg.com/articles](https://svpg.com/articles/), [gibsonbiddle.medium.com/9-the-gem-model-65c89face5de](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de)

## 4. How stories plug into outcome briefs

An outcome brief (this skill's condensed contract, self-contained) holds: problem statement, ICP, outcome metric with baseline and target, kill criteria, and the evidence each claim cites. Stories connect to it by three rules:

1. **Every story cites the brief's outcome.** The template's "Outcome it serves" line carries the metric and the delta the story probes; no orphan stories.
2. **A story is one experiment toward the outcome.** Its acceptance criteria define the build; its experiment note defines the learning: which signal (metric delta, usage event, interview finding) counts as evidence, and the kill-or-iterate decision if absent. Release slices in the story map are ordered by evidence value, not by build convenience.
3. **Epics rename to hypotheses.** If the "epic" cannot state a falsifiable outcome, write the outcome stub first, tagged `[ASSUMPTION - outcome unvalidated]` with a revisit trigger (e.g. "revisit after 5 discovery interviews"), and let the first slice of the map be a discovery slice rather than a build slice.

Condensed outcome-stub format, for use when no brief exists:

```markdown
**Outcome stub:** [ICP] currently [baseline behavior/metric, anchored]; we expect [target behavior/metric] by [date] if [hypothesis]. Kill if [threshold + anchor] missed at [revisit date]. [ASSUMPTION tags as needed]
```

## 5. Sources

- JTBD: Clayton Christensen Institute — [christenseninstitute.org/key-concepts/jobs-to-be-done](https://www.christenseninstitute.org/key-concepts/jobs-to-be-done/)
- Job-story syntax: Intercom / Alan Klement — [alanklement.com](https://www.alanklement.com/)
- Story mapping: Jeff Patton — [jpattonassociates.com](https://www.jpattonassociates.com/)
- Outcomes over outputs, empowered teams: Marty Cagan — [svpg.com/articles](https://svpg.com/articles/); Melissa Perri, *Escaping the Build Trap* (O'Reilly)
- GEM as outcome discipline: Gibson Biddle — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/)
