---
name: roadmap-planning
description: Builds and communicates product roadmaps as Now/Next/Later confidence horizons with an evidence-citation column and hill-chart progress, dating only what certainty or contract justifies. Use when the user asks for a roadmap, quarterly plan, sequencing of ranked bets, "when does X ship", or when an exec demands a dated plan or "my boss wants dates on everything". Defaults to Now/Next/Later, refuses fake precision on undiscovered work, and communicates uncertainty explicitly instead of shipping Gantt-shaped fiction. When the ask is which bets rank first, the evidence-cited ranking happens in the prioritization discipline; when the ask is the written periodic update, that is stakeholder-update work — this skill produces the plan artifact both report on.
license: MIT
---

# Roadmap Planning

A roadmap is a communication about confidence, not a promise about calendars. Now is what you know, Next is what you are learning, Later is what you bet on — and a date on a Later item is fiction dressed as commitment. This skill builds roadmaps a stakeholder can read in ten seconds and trust.

## 1. Core Principles

1. **Horizons are confidence, not quarters** — Now: validated and in flight, well understood. Next: problems in discovery/shaping, medium confidence. Later: strategic bets, intentionally hazy (Bastow / ProdPad).
2. **Dates are commitments; commitments require certainty or contract** — only Now items and contractual obligations carry dates. Dating undiscovered work converts every status meeting into an apology (Bastow; Singer).
3. **Every row cites evidence or assumption** — the evidence-citation column: impact and effort ratings cite an interview, telemetry, or spike source, else `[ASSUMPTION]`. Unsourced scores are prioritization theater (Rachitsky's RICE critique).
4. **Progress is hill position, not percent complete** — hill charts split work into uphill (figuring out) and downhill (executing). "60% done" on unsolved unknowns is a lie with a decimal (Singer / Shape Up).
5. **Uncertainty is communicated, not hidden** — execs get per-horizon confidence, the evidence behind Now, and the decision dates for Next. Admitted unknowns with a reforecast cadence build more trust than fake precision (Bastow; Singer's circuit breaker).

## 2. Format & Deviation Criteria

Default: Now/Next/Later via [./assets/now-next-later.md](./assets/now-next-later.md). Deviate only when:

- **Contractual or regulatory dates exist** — keep NNL and add a dated Commitments strip listing only the contractual/regulatory items, each with the obligation source (contract clause, regulation, signed order form).
- **Org runs Shape Up cycles** — Now holds this cycle's bets; hill charts for in-flight status; circuit breaker at cycle end.
- **Exec demands a dated annual Gantt** — do not fabricate. Run §4 pushback.

## 3. Workflow

1. Gather initiatives as **problems**, not features; tie each to a business objective (Bastow).
2. Load [./assets/now-next-later.md](./assets/now-next-later.md).
3. If `product/bets.md` exists, read it (§6): the Now column is drawn from active bets only; each Now row inherits the bet's hill position and kill criterion; a Now row with no matching bet is flagged `[NOT AN ACTIVE BET]`.
4. Assign horizons by confidence (§1.1). Each row: outcome target, evidence citation, confidence, decision date. Now rows add hill position + circuit-breaker date.
5. Capacity check: Now holds at most one in-flight problem per team; overflow sits in Next regardless of importance ([ASSUMPTION] until you have measured one cycle of your team's throughput).
6. Status reviews use hill charts: a Now item still uphill past the window midpoint triggers a cut-scope-or-kill decision, not an auto-extension (Singer).
7. Attach the Uncertainty Communication block (§4) for exec audiences — one paragraph, not a slide deck.

## 4. Pushback / Guardrails

- **Date-based Gantt demand on undiscovered work** — refuse fake precision. Deliver, in order: (1) the NNL roadmap; (2) a dated Commitments strip limited to Now + contractual items; (3) a short cost-of-fake-dates note (dates become commitments, broken commitments become micromanagement); (4) a reforecast offer — horizon review at a stated cadence, monthly default [ASSUMPTION].
- **Backlog-dump roadmap** (dozens of rows) — compress to problem level; cap Later at 5 strategic themes [ASSUMPTION cap — tune to org]; park the rest in an ideas inbox that is not the roadmap.
- **RICE/T-shirt theater** — strip scores that lack citations; demand a citation or `[ASSUMPTION]` per rating before debating rank.

## 5. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Date theater | 12-month Gantt over undiscovered work | NNL + dated Now/contractual only |
| Quarters as horizons | "Now = Q3" | Horizons move with confidence, not the calendar |
| Percent-complete status | "60% done" with unknowns unsolved | Hill position (uphill/downhill) |
| Feature-list roadmap | Rows are features | Rewrite as problems with outcome targets |
| Unsourced scores | "High impact" with no citation | Evidence-citation column or `[ASSUMPTION]` |
| Stadium roadmap | Later holds 30 items | Cap Later themes; park the rest |

## 6. Workspace State

This skill reads `product/bets.md` to ground the Now column; it never writes the file. If absent, build from user input and note the bets file was not present.

Schema as found on disk (restated here so this skill stays self-contained):

```markdown
# Active Bets
Last-updated: YYYY-MM-DD

| Bet | Evidence class | Appetite | Hill position | Kill criterion | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
```

Mapping rules: a Now row must match a row by bet name; hill position (uphill / downhill) carries into the Now row's status; the evidence-citation column is satisfied by the bet's evidence class plus its cited source; a bet past its kill-criterion revisit date is flagged `[RESOLUTION DUE]` and gets a cut-scope-or-kill decision at the status review, not a silent carry.

## 7. Files

- [./references/horizons.md](./references/horizons.md) — NNL rules (Bastow), hill charts and circuit breakers (Singer), evidence-citation rules, exec uncertainty scripts. Load when justifying the format, running status, or writing exec communication.
- [./assets/now-next-later.md](./assets/now-next-later.md) — fill-in template with evidence column, commitments strip, and exec uncertainty block.
