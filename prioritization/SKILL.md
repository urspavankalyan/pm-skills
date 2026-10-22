---
name: prioritization
description: Ranks product bets into evidence-cited prioritization memos and kills prioritization theater before it ships a roadmap. Use when the user asks to prioritize a roadmap, rank features or ideas, run RICE or ICE scoring, T-shirt size a backlog, settle a prioritization dispute, or says "what should we build next", "the backlog is out of control", or "everything is P0". Defaults to T-shirt sizing plus open strategic debate with a mandatory evidence citation on every score, treats RICE as a political instrument only for large organizations, and checks every bet against the active GEM focus and a falsifiable kill criterion before it ranks. Produces the ranked list and kill decisions; turning ranked bets into horizons and dates belongs to roadmap work.
license: MIT
---

# Evidence-Based Prioritization

You rank bets against strategy and evidence, not against whoever shouts loudest. A ranking whose scores cite nothing is prioritization theater — opinion laundered through math — and this skill exists to prevent it.

## 1. Core Principles

1. **Every score cites evidence** — every Impact, Confidence, Effort rating or T-shirt size names a specific source (telemetry report, interview log, spike note, pipeline doc) or is tagged `[ASSUMPTION]`. An uncited score is an opinion, and opinions do not outrank evidence (Rachitsky / Lenny's Newsletter).
2. **Framework honesty** — RICE is gameable; it is a political instrument, not a truth machine. The default is T-shirt sizing plus open strategic debate; RICE only when the organization genuinely needs numbers to defend choices (§3) (Rachitsky; Singer / Shape Up).
3. **Bets must match the active focus** — every ranked bet declares which Growth / Engagement / Monetization (GEM) focus it serves. Off-focus bets require a formal strategic exception: named approver, written rationale, review date (Biddle / GEM).
4. **Appetite before ranking** — bets are sized in fixed appetite slots (2-week small batch, 6-week big batch) so ranking is a choice of bets, not a sum of estimates (Singer / Shape Up).
5. **No bet without a kill criterion** — every funded bet carries a falsifiable threshold with an anchor and a revisit date. A ranking that cannot die is a sunk-cost trap (Singer / circuit breakers).

## 2. The Prioritization Gate

Before ranking anything, establish three things. Do not guess silently.

1. **Active GEM focus** — which of Growth / Engagement / Monetization is rank #1 this quarter? If the workspace has `product/strategy.md`, read it and cite it: `[RESOLVED FROM WORKSPACE: product/strategy.md (updated YYYY-MM-DD)]`; if older than 90 days append `[WARNING: strategy.md may be stale]`. If absent, ask one question or tag the focus `[ASSUMPTION]`.
2. **Candidate bets with evidence** — each candidate arrives with at least one cited source or is labeled `[NO COMPELLING EVIDENCE]`.
3. **Capacity** — how many big (6-week) and small (2-week) slots exist this cycle. A ranking without capacity is a wish list.

## 3. Framework Selection

| Default: T-shirt + open strategic debate | Choose RICE instead, only if |
| :--- | :--- |
| Small-to-mid, high-trust team; alignment comes from open debate | Large, political organization with multiple competing stakeholders where you must defend choices with numbers |
| Bets are few enough to debate in one room | A shared quantitative language is needed across many teams |
| Leadership accepts "we debated and bet" as the answer | Leadership explicitly demands a score audit trail |

Whichever framework runs, two rules never suspend: every input cites evidence (§1.1), and scores are an input to the betting debate, never a verdict — the highest score does not auto-fund. Full decision criteria and the theater critique: [./references/frameworks.md](./references/frameworks.md).

## 4. Workflow

1. Run the Prioritization Gate (§2).
2. Select the framework (§3) and load [./references/frameworks.md](./references/frameworks.md) for scoring rules and worked examples.
3. Score every bet with evidence citations; run the GEM alignment check on each. Off-focus bets move to Formal Exceptions, never silently into the ranked list.
4. Route sales/CEO-driven requests through §5 before they touch the ranking.
5. Emit the memo with [./assets/prioritization-memo.md](./assets/prioritization-memo.md): ranked bets table (Bet | Evidence citation | GEM alignment | Appetite | Kill criterion), formal exceptions, rejected/deferred with one-line reasons.
6. Attach a kill criterion to every funded bet: threshold + anchor (historical baseline or labeled assumption) + revisit date.
7. Sync the workspace state (§7): append or update every funded bet in `product/bets.md`, keyed by bet name; refresh `Last-updated`.

## 5. Sales / CEO-Driven Requests

A top-down request is a bet like any other and goes through the same gate. Compliance is not helpfulness.

1. **Label it.** No evidence base means `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]` in the memo.
2. **Name the unvalidated risks** — the specific Value / Usability / Feasibility / Viability leaps, not "more research is needed".
3. **Attach kill criteria to any funded exception** — e.g. "enterprise SSO exception funds a 2-week spike; converts to a full bet only if >= 3 ICP accounts name it a blocker in written pipeline notes (anchor: current pipeline review), else killed at review date". Every number states its anchor or is `[ASSUMPTION]`.
4. **Record the cost** — the exception entry names the requester, the displaced bet, and the review date. A favor with no displaced bet is a hidden tax on the roadmap.

If the request is large and evidence-free, propose a 1-week discovery plan with a quantitative go/kill threshold instead of a full bet.

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| RICE theater | Confidence/Impact hand-tuned until the pet feature tops | Re-score with cited evidence only; uncited inputs become `[ASSUMPTION]` and drop the bet's rank |
| T-shirt theater | Same disease, new costume: "High impact, low effort" with no citation | Every size cites a source or is `[ASSUMPTION]` |
| Score-as-verdict | The highest RICE number auto-funds without debate | Scores open the debate; the betting table decides |
| Off-focus slip-in | An Engagement-stage company ranks a Monetization favor in its top 3 | GEM check; formal exception with approver, displaced bet, review date |
| Backlog hoarding | A 200-item groomed backlog nobody will ever build | Bets are shaped and chosen at the betting table, or discarded; what matters resurfaces (Singer) |
| Phantom kill criteria | "We will measure success" with no threshold or date | Threshold + anchor + revisit date, or delete the bet |

## 7. Workspace State

This skill reads `product/strategy.md` and writes `product/bets.md`.

Read — `product/strategy.md` (compact state header; if absent, ask one question or tag the focus `[ASSUMPTION]` per §2):

```markdown
# Product Strategy State
Last-updated: YYYY-MM-DD

## Active Strategic Focus (GEM)
- **Rank:** [1st] > [2nd] > [3rd]
```

Cite it `[RESOLVED FROM WORKSPACE: product/strategy.md (updated YYYY-MM-DD)]`; age > 90 days appends `[WARNING: strategy.md may be stale]`. Every bet declares alignment with the rank-1 focus; off-focus bets require a formal exception (§1.3).

Write — `product/bets.md`: every funded bet becomes exactly one row; an existing row for the same bet name is updated in place, never duplicated; refresh `Last-updated` on write; no filesystem means emitting the table fenced for the user to file.

Schema (keep exactly this shape):

```markdown
# Active Bets
Last-updated: YYYY-MM-DD

| Bet | Evidence class | Appetite | Hill position | Kill criterion | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [name] | [big-batch / small-batch / hygiene-contractual / strategy-driven] | [2-week / 6-week] | [uphill / downhill] | [threshold + anchor + revisit date] | [name] |
```

Evidence class mirrors the evidence weight rule: big-batch (>= 5 ICP interviews or >= 15% friction telemetry), small-batch (1-4 interviews or recurring tickets), hygiene-contractual (the obligation is the evidence), strategy-driven (`[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]`). A killed bet leaves the table for a dated Killed / Superseded list, and the kill is logged in the decision journal file as a kill-pivot entry.

## 8. Files

- [./references/frameworks.md](./references/frameworks.md) — the theater critique, RICE vs T-shirt decision criteria, GEM alignment rules, top-down request handling, kill criteria. Load whenever scoring or framework choice is involved.
- [./assets/prioritization-memo.md](./assets/prioritization-memo.md) — the ranked-bets memo template. Load at output time.
