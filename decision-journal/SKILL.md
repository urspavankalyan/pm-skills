---
name: decision-journal
description: Keeps a calibration-scored product decision journal — logs decisions with falsifiable predictions, kill criteria and confidence at commit time, scores resolutions against the prediction as written, and runs retros that stay strictly qualitative below 10 resolved decisions and compute win rate, calibration gap, Brier score and sunk-cost ratio at 10 or more. Use when the user asks to log a decision, review past bets, run a decision retro, check forecasting calibration, or says "were our calls right?". Refuses percentages and Brier scores over small samples and updates entries in place instead of duplicating them.
license: MIT
---

# Decision Journal & Calibration Retro

You keep the record that makes judgment improvable. A decision without a falsifiable prediction and a kill criterion cannot be scored; a score computed from six data points is false precision. This skill enforces both disciplines.

## 1. Core Principles

1. **Write at commit, score at resolve** — prediction, kill criterion, and confidence are frozen when the entry is logged. Resolution appends facts; it never edits the prediction (hindsight editing destroys the dataset).
2. **Falsifiable predictions only** — "improve onboarding" is not a prediction. Every entry names a metric, a movement from X to Y, and a date.
3. **Kill criteria are hard boundaries** — a quantitative threshold with an anchor and a revisit date that terminates the bet, not a warning sticker.
4. **Small-sample rule: under 10 resolved = qualitative only** — no win rates, no percentages, no Brier scores. Statistics over fewer than 10 resolved decisions are invalid and manufacture false confidence (statistical safeguard).
5. **At >= 10 resolved = quantitative calibration** — win rate, calibration gap by confidence bucket, Brier score, and sunk-cost ratio, computed exactly as defined in [./references/calibration.md](./references/calibration.md) §3 and reported in its §4 layout.
6. **Update, not duplicate** — one entry per decision. New information amends the entry with a dated addendum; the original prediction stays verbatim.

## 2. Entry Format

Log every commitment decision (PRD approved, priority bet, kill/pivot call, strategic exception) via [./assets/decision-entry.md](./assets/decision-entry.md):

1. **Date** — commit date.
2. **Type** — one of: PRD commit, prioritization, kill/pivot, strategic bet, launch.
3. **Decision** — one sentence of what is being committed.
4. **Predicted outcome** — metric moves from X (anchored) to Y by date.
5. **Kill criterion** — threshold + anchor + revisit date + the action it triggers.
6. **Confidence** — 0-100% probability, at commit time, that the prediction as written comes true.
7. **Status** — Pending, then Resolved / Killed / Superseded at resolution.

If the user's input lacks a kill criterion or confidence, ask for them or flag the entry `[INCOMPLETE: missing kill criterion]` — never invent a default confidence.

## 3. Workflow

1. **Log.** Create or append `product/decisions.md` (if no filesystem, emit the fenced entry for the user to file). Match by decision name first: an existing entry gets a dated addendum, never a second entry.
2. **Resolve.** On the revisit date or triggering event, append the Resolution block: actual metric, prediction correct yes/no scored against the prediction as written, kill criterion honored yes/no. A bet killed at its kill criterion scores the prediction incorrect but counts as discipline in the sunk-cost audit.
3. **Retro.** Count resolved decisions; choose the mode; load [./references/calibration.md](./references/calibration.md); produce the report in its §4 layout with at most 3 takeaways.
4. **Act.** Feed takeaways into the next cycle's evidence and kill-criterion habits; record any recalibrated operating thresholds as dated addenda.

## 4. Guardrails & Pushback

- **Statistics demanded on a small sample** ("what's our win rate?" with 6 resolved): refuse with the line `[SMALL SAMPLE: n=6 < 10 — qualitative mode; statistics withheld]` and deliver the qualitative report instead (optimism-bias check, kill-criterion audit, assumption tracker — no percentages anywhere in it).
- **Hindsight edit requests** ("update my old prediction to what we now know"): refuse; offer a dated addendum that leaves the original verbatim.
- **Narrative-only predictions** ("we believe this will help"): push to metric + target + date before logging; log as `[INCOMPLETE]` only if the user insists.
- **Retro with zero resolved decisions:** produce the audit header and a pending-list nudge; no assessment section, no numbers.

## 5. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Hindsight editing | Prediction text changed after resolution | Restore original; move corrections to a dated addendum |
| Narrative prediction | No metric, target, or date in the prediction | Require metric X-to-Y-by-date; else `[INCOMPLETE]` |
| Percentages at n=6 | Win rate or Brier printed under 10 resolved | Qualitative mode only; withhold statistics with the small-sample line |
| Kill criterion as warning | Threshold met but bet kept alive | Count in sunk-cost ratio; surface consequences in the audit |
| Duplicate entries | Same decision logged twice after new info | Merge: one entry, dated addenda |
| Confidence creep | Confidence field edited post-commit | Confidence is frozen at commit; addenda only |

## 6. Workspace State

This skill owns `product/decisions.md`, shared with PRD-finalization writers; every writer uses the one canonical schema below. Create on first write; no filesystem means emitting the entry fenced for the user to file.

Canonical entry (identical to [./assets/decision-entry.md](./assets/decision-entry.md); restated here so this skill stays self-contained):

```markdown
## [YYYY-MM-DD] | Type: [PRD commit / prioritization / kill-pivot / strategic bet / launch] | [Decision name]
- **Decision:** [what is being committed, one sentence]
- **Alternatives considered:** [one line each]
- **Predicted outcome:** [metric] moves from [X, anchored to baseline period] to [Y] by [date]
- **Kill criterion:** [threshold + anchor] at [revisit date] -> [kill/pivot action]
- **Confidence:** [NN]%
- **Status:** Pending
```

Update-not-duplicate: match by decision name; new information appends `### Addendum [YYYY-MM-DD]`; resolution appends `### Resolution [YYYY-MM-DD]` (actual outcome, prediction correct yes/no against the prediction as written, kill criterion honored yes/no, Status Resolved / Killed / Superseded). Commit-time fields are frozen forever. Staleness: a Pending entry past its kill-criterion revisit date is flagged `[RESOLUTION DUE]`.

## 7. Files

- [./references/calibration.md](./references/calibration.md) — entry semantics, small-sample qualitative report, large-sample statistics (Brier, calibration gap, win rate, sunk-cost ratio), retro output layout. Load for any retro or scoring question.
- [./assets/decision-entry.md](./assets/decision-entry.md) — fill-in entry template with resolution block and addendum rules.
