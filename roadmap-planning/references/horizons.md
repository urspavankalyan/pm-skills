# Horizons, Hill Charts, and Honest Status

Deep rules behind the roadmap skill: Now/Next/Later (Bastow), hill charts and circuit breakers (Singer), the evidence-citation column, and exec uncertainty communication.

## 1. Now/Next/Later (Janna Bastow)

- **Definition:** A roadmap format that organizes initiatives into three confidence horizons — Now (actively building, high certainty, well specified), Next (validated as next once Now completes, medium certainty), Later (strategic bets kept in view, low certainty) — instead of fixed delivery dates.
- **When to use:** Managing stakeholder expectations in agile or product-led orgs; when roadmap conversations became deadline negotiations instead of problem debates.
- **When NOT to use:** Where clients require contractually guaranteed delivery dates — keep NNL and add a dated Commitments strip for those items only.
- **Column rules (Bastow):** Prioritize at the problem level, not the idea level; define initiatives as prototypes, experiments, and solutions tied to a business objective; columns need not be equal in size; Now is specified, Later is deliberately hazy; items move between horizons as discovery changes confidence.
- **Worked Example:** Bastow's original: her teams planned out of Jira and a release planner — long, unreadable, dates always slipping, every conversation a deadline negotiation. She dropped dates and drew three columns (first Current / Near Term / Future, renamed Now-Next-Later by an early customer). The first stakeholder review stopped arguing about dates and started arguing about which problems mattered. ProdPad has shipped the format ever since.
- **Source URL:** [prodpad.com/blog/invented-now-next-later-roadmap](https://www.prodpad.com/blog/invented-now-next-later-roadmap/) (Bastow); [prodpad.com/glossary/now-next-later-roadmap](https://www.prodpad.com/glossary/now-next-later-roadmap/).

## 2. Hill Charts & Circuit Breakers (Ryan Singer)

- **Definition:** A **hill chart** places each scope of work on a spectrum: uphill (figuring out — unknowns unsolved), crest (unknowns solved), downhill (execution). A **circuit breaker** is the policy that a project not finished within its cycle is canceled by default, not extended by default.
- **When to use:** Status visibility without status meetings; deciding when to cut scope or kill a bet.
- **When NOT to use:** Routine bug triage or maintenance operations.
- **Reading rule:** Percent-complete is banned in status reviews. A scope still uphill at the window midpoint is the signal to intervene — slice scope, add help, or kill. At cycle end the breaker fires.
- **Worked Example:** Basecamp tracks scopes on hill charts, the method's home (Shape Up). **Hypothetical:** a reporting dashboard is still uphill on query performance at week 4 of a 6-week window; the chart triggers a week-4 scope cut (drop two widget types) instead of a week-6 extension request.
- **Source URL:** [basecamp.com/shapeup](https://basecamp.com/shapeup) (Singer: "Work is like a hill", circuit-breaker glossary).

## 3. The Evidence-Citation Column

- **Definition:** A mandatory roadmap column in which every impact, effort, or priority rating cites a specific source — interview report, telemetry query, engineering spike — or is tagged `[ASSUMPTION]`.
- **When to use:** Every prioritization pass (RICE, T-shirt, or open debate); it prevents both mathematical and subjective scoring theater.
- **When NOT to use:** Never skipped; absence of a citation is itself information (it means assumption).
- **Rules:** Forbid unsourced subjective scores; `[ASSUMPTION]` ratings get a validation owner and date; at reviews, cite before debating.
- **Worked Example (hypothetical, shape from practice):** Theater: "SSO support — Impact H, Effort L" with no source. Rectified: "Impact H [cites pipeline report: 3 enterprise prospects blocked on SSO in Q2]; Effort H [cites tech-lead spike: Cognito migration required]." The rank changed, and so did the conversation.
- **Source URL:** [lennysnewsletter.com](https://www.lennysnewsletter.com) (Rachitsky on RICE and prioritization-theater critiques).

## 4. Communicating Uncertainty to Executives

Rules:

1. Lead with per-horizon confidence: "Now is committed and dated; Next is being validated and decided on [date]; Later is direction, not promise."
2. Show the evidence behind Now (citations) and the decision dates behind Next — uncertainty with a re-examination schedule reads as control, not chaos.
3. Replace fake precision with ranges and triggers: "we commit to the direction; the date firms up when [evidence] lands."
4. Use the circuit breaker as a trust device: execs hear about killed bets at decision time, not after slippage.
5. Never defend a slipped fake date; reforecast and state why the old date was wrong.

**Script (adapt):** "This roadmap shows confidence, not a calendar. Now is committed — these two problems, dated, evidence cited. Next is being validated; we decide on [date] with [evidence]. Later is direction we will not promise. If a Now item is still uphill on [midpoint date], we cut scope or kill it, and you hear about it the same day."

- **Source URL:** [prodpad.com/blog/product-roadmaps-dont-need-deadlines](https://www.prodpad.com/blog/product-roadmaps-dont-need-deadlines/) (Bastow); [basecamp.com/shapeup](https://basecamp.com/shapeup) (Singer).
