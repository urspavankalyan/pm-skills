# Workspace State Contract

Canonical schema for the living workspace that pm-skills sessions share: three files under `product/` that agents read and write across sessions. This document is the single source of truth for their shape; each participating skill restates the slice it touches inline in its own SKILL.md so every skill remains fully self-contained when installed alone. Skills never link to this file at runtime.

## Ownership matrix

| File | Writers | Readers |
| :--- | :--- | :--- |
| `product/strategy.md` | product-strategy (sole writer; offers initialize workspace state) | prioritization (GEM alignment), prd-writing (context gate), failure-analysis (pre-mortem context) |
| `product/bets.md` | prioritization (sole writer) | roadmap-planning (Now column), failure-analysis (kill-criteria context) |
| `product/decisions.md` | prd-writing (on finalization), decision-journal (on logging), failure-analysis (resolutions and kill-retro addenda), one canonical schema | decision-journal (retro, scoring); any session may cite |

Shared mechanics for all three files:

1. **Create on first write.** If the file is absent, the writer creates it; if the filesystem is unavailable, emit the block fenced for the user to file.
2. **Update, never duplicate.** Rows and entries are keyed by name; new information amends the row in place (bets) or appends a dated addendum (decisions); a second record for the same identity is never written.
3. **Last-updated refreshes on every write** where the schema defines it (strategy.md, bets.md).
4. **No silent staleness.** Readers apply the staleness rules below and surface the tag; they never ignore an aged file quietly.

## product/strategy.md

```markdown
# Product Strategy State
Last-updated: YYYY-MM-DD

## ICP
- **Segment:** [who we win with first]
- **Workflows:** [what they do today]
- **Constraints:** [regulatory / privacy / commercial limits]
- **Alternatives:** [what they use instead, including doing nothing]

## Active Strategic Focus (GEM)
- **Rank:** [1st] > [2nd] > [3rd]
- **Justification:** [one line]

## Cycle Appetite
- **Big batch:** [6-week cycles, N teams]
- **Small batch:** [2-week cycles, M slots]

## Stage & Context
- [funding model, runway, market type — one line]
```

Rules:

- Written only by product-strategy, after a finalized strategy doc, focus ranking, or appetite change. The full strategy doc and this state header are distinct artifacts and never merge.
- **Initialize workspace state:** when the file is absent and the user wants cross-session continuity, product-strategy offers to write it from the finalized sections.
- Staleness: readers compute the age from `Last-updated`; older than 90 days appends `[WARNING: strategy.md may be stale]` to any citation.

## product/bets.md

```markdown
# Active Bets
Last-updated: YYYY-MM-DD

| Bet | Evidence class | Appetite | Hill position | Kill criterion | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [name] | [big-batch / small-batch / hygiene-contractual / strategy-driven] | [2-week / 6-week] | [uphill / downhill] | [threshold + anchor + revisit date] | [name] |

## Killed / Superseded
- [YYYY-MM-DD] [bet name] — [killed at criterion / superseded by [name]]
```

Rules:

- Evidence class values mirror the minimum-evidence-weight rule: big-batch (>= 5 ICP interviews or >= 15% friction telemetry), small-batch (1-4 interviews or recurring tickets), hygiene-contractual (the obligation is the evidence), strategy-driven (labeled `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]`).
- Hill position uses hill-chart vocabulary: uphill (figuring out) / downhill (executing).
- A funded bet is exactly one row; reshaping updates the row in place. A killed bet moves to Killed / Superseded with a date, and the kill is also logged in decisions.md as a kill-pivot entry.
- Staleness: an active row past its kill-criterion revisit date is flagged `[RESOLUTION DUE]` by any reader.

## product/decisions.md

One canonical entry schema. All writers — `prd-writing` at finalization, `decision-journal` at logging, `failure-analysis` appending resolutions and kill-retro addenda — emit or amend the full shape (commit fields plus Resolution and Addendum blocks), so an entry written by any is complete for the others.

```markdown
# Decision Journal

## [YYYY-MM-DD] | Type: [PRD commit / prioritization / kill-pivot / strategic bet / launch] | [Decision name]
- **Decision:** [what is being committed, one sentence]
- **Alternatives considered:** [one line each]
- **Predicted outcome:** [metric] moves from [X, anchored to baseline period] to [Y] by [date]
- **Kill criterion:** [threshold + anchor] at [revisit date] -> [kill/pivot action]
- **Confidence:** [NN]%
- **Status:** Pending

### Resolution [YYYY-MM-DD]
- **Actual outcome:** [metric actual, source citation]
- **Prediction correct:** [yes / no — scored against the prediction as written]
- **Kill criterion honored:** [yes / no — if no, state the resource and strategic consequences]
- **Status:** [Resolved / Killed / Superseded (successor: [entry name])]

### Addendum [YYYY-MM-DD]
- [what changed and why; original prediction retained for scoring]
```

Rules:

- **Update, not duplicate.** Match by decision name; new information appends `### Addendum [date]`; resolution appends `### Resolution [date]`; a second `##` heading for the same decision is never written.
- **Commit-time fields are frozen.** Decision, prediction, kill criterion, and confidence are never edited after commit; corrections live in addenda.
- **Staleness.** A Pending entry past its kill-criterion revisit date is flagged `[RESOLUTION DUE]`; resolved entries never age out.
- Bypassed drafts (`[DRAFT-ONLY]` / `[SANDBOX]`) are never written here.
