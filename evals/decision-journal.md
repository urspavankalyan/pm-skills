# Evals: decision-journal

## Scenario 1 — Six resolved decisions, win rate demanded (adversarial)
**Prompt:** "Our journal has 6 resolved decisions. Compute our win rate and Brier score so I can put them in the board update."
**Expected behavior:**
- Refuses statistics: emits `[SMALL SAMPLE: n=6 < 10 — qualitative mode; statistics withheld]`.
- Delivers the qualitative report only: directional optimism-bias check in words (no percentages), kill-criterion/sunk-cost audit, leap-of-faith assumption tracker.
- Must NOT contain any win rate, percentage, or Brier value; explains the false-precision rationale in one line.

## Scenario 2 — Twelve resolved decisions (happy path, quantitative)
**Prompt:** "Run the retro on our journal — 12 resolved decisions, confidences and outcomes attached."
**Expected behavior:**
- Evaluation mode = Quantitative Calibration; computes and displays win rate, calibration curve table by confidence bucket with gaps, Brier score with the 0.0/0.25/1.0 interpretation, and sunk-cost ratio with target 0.0.
- Section 2 lists every triggered kill criterion with honored yes/no; Section 3 capped at 3 takeaways; output matches the reference §4 layout.

## Scenario 3 — Vague logging request (diagnostic)
**Prompt:** "Log that we're going to revamp onboarding because we believe it will help."
**Expected behavior:**
- Pushes to a falsifiable prediction (metric, X-to-Y, date), a kill criterion with anchor and revisit date, and a commit-time confidence; offers the `assets/decision-entry.md` shape.
- If the user insists, logs with `[INCOMPLETE: missing kill criterion]` rather than inventing numbers; never defaults confidence silently.
- A Pending entry past its kill-criterion revisit date is flagged `[RESOLUTION DUE]`; the retro asks for the outcome instead of leaving it dangling.

## Scenario 4 — Update semantics (adversarial)
**Prompt:** "The payments bet from March is now scoped to EU only — log it again as a new entry with the new prediction, and fix my old confidence from 80% to 60% since I was clearly too optimistic."
**Expected behavior:**
- Refuses both moves: no duplicate entry (one entry per decision identity) and no hindsight edit of confidence.
- Produces a dated addendum recording the EU-only scope with a new sub-prediction for scoring, original 80% and original prediction retained verbatim; cites the update-not-duplicate rule.

## Scenario 5 — Cross-writer schema agreement (agreement)
**Prompt:** "Our decisions.md ends with this entry, written at PRD finalization by another session:

## 2026-09-12 | Type: PRD commit | CSV Export Rescue
- **Decision:** ship a 6-week rebuild of the export pipeline.
- **Alternatives considered:** patch the existing serializer; buy a third-party exporter.
- **Predicted outcome:** export failure rate moves from 18% (Q2 telemetry) to < 2% by 2026-12-01.
- **Kill criterion:** failure rate >= 10% at 2026-11-01 -> kill and revert to the patch option.
- **Confidence:** 70%
- **Status:** Pending

The 2026-11-01 check landed at 4%. Resolve it."
**Expected behavior:**
- Consumes the entry as-is: no reformatting, migration, or missing-field flags — Type, Decision, Alternatives considered, Predicted outcome, Kill criterion, Confidence, Status are all present and gradable.
- Appends `### Resolution [date]`: actual 4% with source, prediction correct no (4% missed the < 2% target), kill criterion honored yes (10% never breached), Status Resolved.
- Commit-time lines stay verbatim (70% frozen); no second `##` entry for CSV Export Rescue; cites the update-not-duplicate rule.
