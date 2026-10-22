# Evals: prioritization

## Scenario 1 — RICE demanded to settle a political fight (adversarial)
**Prompt:** "The VP of Sales and I each have a pet feature and we're at war. Run RICE on both, higher score wins, publish to the exec staff Friday."
**Expected behavior:**
- Framework selection permits RICE here (large political org, must defend choices with numbers) — does not refuse RICE itself.
- Evidence-citation rule enforced: every Reach/Impact/Confidence/Effort cell cites a source; stakeholder-supplied uncited numbers are returned, not accepted; uncited inputs become `[ASSUMPTION]` and weigh less.
- Scores published as input to an exec debate, not a verdict: the "higher score wins" rule is explicitly declined (score-as-verdict anti-pattern); memo carries Betting-Table Notes.
- GEM alignment stated per bet; the funded bet gets a kill criterion with anchor and revisit date.
- Must NOT contain an auto-funding rule or uncited numeric cells.

## Scenario 2 — Evidence-free ranking demand
**Prompt:** "Rank these 12 features by tomorrow. We don't have time for research, use your judgment."
**Expected behavior:**
- Default framework: T-shirt + open debate, not RICE; no invented precise RICE numbers from "judgment".
- Every size without a citation tagged `[ASSUMPTION]`; memo labeled `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]` where a mandated bet has none; pushback offers a 1-week discovery plan with quantitative go/kill thresholds.
- Gate asks for capacity (big/small slots) or tags it `[ASSUMPTION]`; refuses to present a ranking without capacity as a commitment.

## Scenario 3 — Sales-driven off-focus bet (GEM contradiction)
**Prompt:** "We're an Engagement-focused startup but Sales says a $200k deal needs custom reporting. Prioritize it."
**Expected behavior:**
- GEM alignment check fires; the bet is flagged off-focus (serves Monetization while active focus is Engagement).
- Bet routed to Formal Exceptions: requester, rationale, displaced bet, review date. The written contract IS evidence — cite it — but the exception record and a kill criterion still apply (e.g. deal signs by [date] AND >= 2 more ICP accounts name the same need within 90 days, else the follow-on build is killed; anchors stated or `[ASSUMPTION]`).
- Must NOT silently insert the deal work at rank 1.

## Scenario 4 — Well-evidenced ranking (happy path)
**Prompt:** "Prioritize next cycle. Focus is Engagement per strategy.md. Bets: (a) fix CSV exports — Q3 telemetry shows 18% of active users hit export errors; (b) referral program — no evidence; (c) dark mode — 2 interviews."
**Expected behavior:**
- Gate cites `[RESOLVED FROM WORKSPACE: product/strategy.md]`; capacity asked if absent.
- Ranked table: (a) top, citation carried, kill criterion anchored to the 18% baseline (e.g. error rate < 5% by [date]); (b) labeled `[NO COMPELLING EVIDENCE]`, ranked low or converted to a 2-week discovery slot with go/kill threshold; (c) small-batch evidence class labeled.
- Every bet states GEM alignment against the Engagement focus; memo matches `assets/prioritization-memo.md` with no bracketed placeholders left.
