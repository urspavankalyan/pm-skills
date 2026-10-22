# Failure Analysis Playbook

Deep-dive reference for the failure-analysis skill. Methods belong to their authors; every entry carries Definition / When to use / When NOT to use / Worked Example / Source URL.

## 1. The Pre-Mortem (Gary Klein)

- **Definition:** A structured exercise in prospective hindsight: before committing, the team assumes the decision has *already* failed ("it is a year from now and the plan collapsed") and generates the history of that failure. Assuming failure as fact loosens overconfidence and surfaces modes that "what could go wrong" brainstorming misses.
- **When to use:** Before any big-batch commitment (6-week bet, launch, price change, strategic pivot); especially when the room is already optimistic and dissent is quiet.
- **When NOT to use:** As a routine for every small bet — reserve it for commitments whose downside is a full cycle or more.
- **Worked Example (real practice):** Klein's lab studies found prospective-hindsight prompts elicit substantially more and more specific failure explanations than standard risk brainstorming; HBR's practitioner write-up made the exercise a portfolio-manager and project-leader staple.
- **Source URL:** [HBR: Performing a Project Premortem (Klein, 2007)](https://hbr.org/2007/09/performing-a-project-premortem); Gary Klein, *Seeing What Others Don't* (the underlying research).

## 2. Blameless Postmortems (Allspaw; Google SRE culture)

- **Definition:** A post-incident review that assumes everyone acted reasonably given their context, information, and incentives, and therefore studies the mechanism — information flow, tooling, ambiguous authority, incentive structure — that made the bad outcome likely. Blame is scoped out because blame suppresses the disclosures the review needs to be true.
- **When to use:** After any significant miss: failed launch, missed quarter, incident, killed bet.
- **When NOT to use:** As a substitute for genuine accountability conversations about repeated negligence or integrity violations — those are management/legal processes, not artifact territory.
- **Worked Example (real):** Etsy's and Google's postmortem cultures publish the pattern: the review asks "how did the system make this action sensible?" and ships action items against mechanisms (alerting, deploy guardrails, ambiguous runbooks), which is why their postmortems compound while blame reviews recidivate.
- **Source URL:** [sre.google workbook: Postmortem Analysis](https://sre.google/workbook/postmortem-analysis/); John Allspaw's writings on incident review and blamelessness.

## 3. The Limits of "Root Cause" and 5 Whys

- **Definition:** The critique (rooted in resilience engineering and Allspaw's "infinite hows") that single-ladder 5-whys inquiry produces one hindsight-coherent story, hides contributory conditions, and ends at an arbitrary stopping point chosen by politics rather than evidence.
- **When to use 5 Whys:** Only tight mechanical chains (a misconfigured flag caused a failed build) where one causal path is verifiable end to end.
- **When NOT to use:** Socio-technical misses — launches, quarters, adoption failures — where several conditions *jointly* suffice and removing any one would have changed the outcome.
- **Rectification:** Emit ranked causal *candidates* across families (see §4), each with its evidence class; reserve "root cause" language for the mechanical submodule of a larger review.
- **Worked Example:** "The launch missed because marketing underperformed" (single ladder) vs candidates: acquisition mix shifted toward low-intent paid (evidence: channel cohorts), onboarding changed in the same window (evidence: deploy log), the success metric's baseline moved (evidence: tracking change log) — jointly explaining the miss and giving three distinct fixes.

## 4. Causal-Candidate Enumeration

Families to cover before ranking any single cause:

1. **Value** — the bet solved a problem too weak or too narrow (interviews, win/loss).
2. **Usability** — the value existed but users couldn't reach it (task success, funnel localized).
3. **Feasibility** — the system didn't actually do what the brief assumed (incidents, capability gaps).
4. **Viability** — economics, legal, or support burden invalidated the bet (unit-economics, DPA, ticket volume).
5. **Execution** — dependencies, staffing, scope creep, integration surprises (delivery record).
6. **Strategy misalignment** — the bet contradicted the active GEM rank or ICP (workspace `product/strategy.md`).

Worked Example (labeled hypothetical): a B2B invoicing startup misses its Week-2 retention target. Candidates: value (churn interviews say invoices went out once, then accounting did it in the ERP — Value, evidence: 6 interviews); usability (setup wizard drop at step 3 — Usability, evidence: funnel telemetry); strategy (sales sold mid-market while the workflow fits freelancers — misalignment, evidence: win/loss notes). Ranked by evidence strength, not by who speaks loudest.

## 5. From Candidates to Instruments

Every surviving candidate ends as exactly one of:

- **A kill criterion** (pre-commit): threshold + anchor + revisit date that would halt or pivot.
- **A detection alert** (live): the leading indicator, instrumented, with owner.
- **A resolution** (post): the mechanism fix with verifiable-done.

A candidate that ends as none of the three is folklore and leaves the artifact.

## 6. Sources

- Pre-mortem / prospective hindsight: Gary Klein — [HBR 2007](https://hbr.org/2007/09/performing-a-project-premortem), *Seeing What Others Don't*
- Blameless postmortems, incident review: John Allspaw; Google SRE — [sre.google/workbook/postmortem-analysis](https://sre.google/workbook/postmortem-analysis/)
- Root-cause / 5-whys critique: resilience-engineering lineage (Allspaw, "The Infinite Hows"); the repo's own Step-0 discipline in metrics-analysis for verifying failure data before narrating it
