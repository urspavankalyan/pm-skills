# Prioritization Frameworks Reference

Deep-dive companion to SKILL.md. Load whenever framework selection, scoring, or top-down request handling is involved.

## 1. Prioritization Theater — the critique

- **Definition:** PMs adjust Confidence and Impact multipliers until their pre-selected feature tops the formula; the spreadsheet launders opinion as math. Swapping RICE for T-shirt sizes cures nothing when sizes are assigned without evidence — the favorite is always "High impact, Low effort". Same disease, different costume.
- **How to detect:** scores arrive pre-filled with no source column; changing one stakeholder's mind changes a number; the ranking is identical to last quarter's pet list.
- **The rectification:** forbid subjective scoring. Every Impact, Confidence and Effort rating (or T-shirt size) cites a specific source — telemetry report, interview log, spike note, pipeline doc. No source means the value is tagged `[ASSUMPTION]` and weighs less in debate than any cited number.
- **Worked Example:** *Theater:* a PM rates "SSO support" High impact / Low effort to get it funded. *Rectified:* Impact: L [citing pipeline doc L2 showing 3 enterprise prospects blocked on SSO]; Effort: H [citing tech-lead spike note: Cognito migration required]. The bet may still win — but now it wins on evidence.
- **Source URL:** [lennysnewsletter.com](https://www.lennysnewsletter.com/) (Rachitsky on evidence-gated prioritization); the "prioritization theater" framing is widely associated with Janna Bastow / ProdPad — [prodpad.com](https://www.prodpad.com)

## 2. RICE — definition and honest use

- **Definition:** Score = (Reach x Impact x Confidence) / Effort on Intercom's fixed scales: Reach is a raw count of customers or transactions affected within a named scoring window (e.g. per quarter), estimated from telemetry or pipeline docs — a count, never a normalized score; Impact 0.25-3, Confidence 100/80/50%, Effort in person-months with anything under a month scored 0.5. Sean McBride at Intercom, 2018.
- **When to use:** highly political, large organizations with multiple competing stakeholders where you must defend roadmap choices with numbers; when many teams need one shared quantitative language; when leadership explicitly demands a score audit trail.
- **When NOT to use:** small, high-trust teams where open debate aligns (the formula adds theater, not truth); as a verdict machine where the top score auto-funds; with uncited inputs (that is §1's theater, not RICE).
- **Worked Example (Hypothetical: gaming):** a PM scores their feature Impact 3 / Confidence 100% and a rival Impact 2 / Confidence 60%, neither cited; the rival's numbers come from A/B telemetry, theirs from a hunch. *Rectified:* both rows carry citations; the hunch row drops to Confidence 50% tagged `[ASSUMPTION]`, and the ranking is re-argued at the betting table.
- **Source URL:** [intercom.com](https://www.intercom.com/) (Sean McBride, RICE, 2018)

## 3. T-shirt sizing + open strategic debate — the default

- **Definition:** Impact and Effort sized XS-XL with every size cited (§1), ranked in an open debate against the active strategy. Sizes open the argument; the debate decides.
- **When to use:** the default for most teams; especially small-to-mid, high-trust teams where alignment comes from argument, not spreadsheets.
- **When NOT to use:** when the organization meets §2's RICE criteria (a numeric audit trail is genuinely needed); never as an excuse to skip citations (T-shirt theater).
- **Worked Example:** Basecamp runs no scoring formula at all — shaped pitches are debated at the betting table and funded as bets; the artifacts are the pitch and the decision, not a score (Singer).
- **Source URL:** [basecamp.com/shapeup](https://basecamp.com/shapeup), [lennysnewsletter.com](https://www.lennysnewsletter.com/)

## 4. GEM alignment check

- **Definition:** Gibson Biddle's GEM model force-ranks Growth, Engagement, Monetization, each with a proxy metric; the ranking is the company's active focus. Every bet declares which factor it serves; a bet serving a non-#1 factor requires a **formal exception**: named approver, written rationale, review date (revisit at the next GEM re-rank; Biddle's cadence is roughly every 6 months).
- **When to use:** always, at ranking time. The focus itself is set by stage, not dogma: Netflix in 2005 ranked Monetization #1 to prove profitability to Wall Street, then flipped to Growth #1 by 2008; bootstrapped or premium B2B may legitimately rank Monetization first. The check enforces alignment with the chosen focus, not a consumer-startup default.
- **When NOT to use:** never as an auto-reject for cross-factor bets (a growth experiment that also lifts engagement); declare the primary factor and move on.
- **Worked Example:** Netflix 2005, Monetization #1: lower-priced 1- and 2-DVD plans were funded because they served LTV and margin; a pure growth bet that quarter needed an exception with CFO-level rationale. After the 2008 flip to Growth #1, the same bet funded routinely.
- **Source URL:** [gibsonbiddle.medium.com/9-the-gem-model](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de)

## 5. Sales / CEO-driven requests

- **Definition:** a bet whose origin is a person with power, not evidence. Protocol: route through the same gate; label `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]`; name the unvalidated Value / Usability / Feasibility / Viability leaps; if funded anyway, attach kill criteria and an exception record (requester, displaced bet, review date).
- **When to use:** every time. The protocol has no rank-based exemption.
- **When NOT to use:** there is no off switch — even contractual or compliance demands get the record; their evidence base is the obligation itself, so cite the contract or regulation.
- **Worked Example (Hypothetical: B2B analytics vendor):** the CEO wants an AI chatbot after one conference conversation. Label it; name the leaps (Value: no evidence anyone outside the conversation wants it; Feasibility: LLM cost per conversation unmodeled). Offer a 1-week fake door instead of a full bet: click-through >= 8% of eligible sessions funds a 2-week spike (anchor: median entry-point CTR 6% in last quarter's telemetry); < 4% kills. If funded regardless, the exception row names the displaced bet and the review date.
- **Source URL:** [svpg.com/articles](https://svpg.com/articles/) (Cagan, feature teams vs empowered teams), [lennysnewsletter.com](https://www.lennysnewsletter.com/)

## 6. Kill criteria and circuit breakers

- **Rule:** every funded bet carries threshold + anchor + revisit date. At revisit, a miss kills the bet or re-bets it explicitly at the table — never a silent extension. Shape Up's circuit breaker: a project not finished in its cycle stops; the team moves to cool-down while leadership decides whether to re-bet.
- **Worked Example (Hypothetical):** a 6-week reporting-dashboard bet is still uphill on query performance at week 4; the circuit breaker fires at week 6; the bet returns to the betting table instead of quietly extending two weeks.
- **Source URL:** [basecamp.com/shapeup](https://basecamp.com/shapeup)

## 7. Sources

- Prioritization-theater critique: Lenny Rachitsky — [lennysnewsletter.com](https://www.lennysnewsletter.com/); framing popularized by Janna Bastow / ProdPad — [prodpad.com](https://www.prodpad.com)
- RICE origin: Sean McBride / Intercom, 2018 — [intercom.com](https://www.intercom.com/)
- Appetite, betting, backlog rejection, circuit breakers: Ryan Singer — [basecamp.com/shapeup](https://basecamp.com/shapeup)
- GEM model: Gibson Biddle — [gibsonbiddle.medium.com/9-the-gem-model](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de)
- Empowered vs feature teams: Marty Cagan — [svpg.com/articles](https://svpg.com/articles/)
