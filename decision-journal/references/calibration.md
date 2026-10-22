# Decision Journal Calibration Reference

Methodology for logging, resolving, and retrospectively scoring product decisions. Quantitative calibration statistics are licensed only at >= 10 resolved decisions; below that, qualitative assessment only.

## 1. Entry Format & Semantics

Fields, in order, per entry:

1. **Date** — commit date (YYYY-MM-DD).
2. **Type** — PRD commit | prioritization | kill/pivot | strategic bet | launch.
3. **Decision** — one sentence committing resources or direction; alternatives considered in one line each.
4. **Predicted outcome** — `[metric] moves from [X, anchored] to [Y] by [date]`. Unanchored X is fabrication; anchor to a baseline period or tag `[ASSUMPTION]`.
5. **Kill criterion** — `[threshold + anchor] at [revisit date] -> [kill/pivot action]`. Hard boundary by definition.
6. **Confidence** — integer 0-100: probability, at commit time, that the prediction as written comes true. Frozen forever after.
7. **Status** — Pending | Resolved | Killed | Superseded.

**Resolution block (append-only):** resolved date, actual outcome, prediction correct (yes/no, scored against the text as written), kill criterion honored (yes/no with consequences if no), final status. A kill executed at the kill criterion: prediction scores incorrect, discipline scores positive in the sunk-cost audit.

**Update-not-duplicate rule:** one entry per decision identity (name + date). Revisited decisions get dated addenda ("2026-03-01: scope halved after churn spike; original prediction retained for scoring"). Superseded decisions keep their entry; status Superseded records the successor entry's name.

## 2. Small-Sample Rule (Resolved < 10)

Statistical significance safeguard: with fewer than 10 resolved decisions, NEVER compute win rates, calibration percentages, or Brier scores — over small samples they are statistically invalid and create false precision.

The retro instead produces a **Qualitative Calibration Report**:

1. **Optimism-bias check** — compare predicted vs actual outcomes directionally: consistent over- or under-estimation, described in words and magnitude-of-impression ("predicted activation lifts ran consistently above actuals, roughly an order of magnitude in the worst case"), never as a percentage.
2. **Sunk-cost / kill-criterion audit** — list every decision whose kill criterion was met or exceeded but which shipped or stayed active anyway; state the strategic and resource consequences of ignoring the boundary.
3. **Leap-of-faith assumption tracker** — implicit or logged `[ASSUMPTION]` tags proven false during delivery, and which evidence step would have caught them earlier.

## 3. Large-Sample Rule (Resolved >= 10)

Compute and display all four statistics:

1. **Win rate** — resolved decisions scored correct / resolved decisions. Report alongside the base-rate context (bet type mix), not alone.
2. **Calibration gap (calibration curve)** — group predictions into confidence buckets (50-60%, 70-80%, 90%+...); compare stated confidence to actual success rate per bucket. Gap = stated minus actual. Overconfidence: 90% buckets succeeding ~40% of the time. Underconfidence: 60% buckets succeeding ~95% of the time. (Bucketing practice per forecasting literature, Tetlock / Good Judgment.)
3. **Brier score** — mean squared error of probabilistic forecasts: Brier = (1/N) * sum over t of (f_t - o_t)^2, where f_t is the stated confidence as a probability (0.0-1.0) and o_t is 1 if the prediction came true else 0. Interpretation: 0.0 perfect; 0.25 the coin-flip baseline for binary outcomes predicted at 50%; 1.0 total miscalibration. (Brier, 1950 — originally for weather forecasts.)
4. **Sunk-cost ratio** — bets kept active after meeting kill criteria / total bets that met kill criteria. Target 0.0 (every failing bet terminated). A high ratio means kill criteria are treated as warnings and runway is being spent on sunk cost. (Repo methodology.)

## 4. Retro Output Layout

No decorative symbols; plain headers.

```markdown
# Decision Journal Retro

- **Audit date:** [YYYY-MM-DD]
- **Total logged decisions:** [n]
- **Total resolved decisions:** [n]
- **Evaluation mode:** [Qualitative Observations (resolved < 10) | Quantitative Calibration (resolved >= 10)]
- [SMALL SAMPLE: n=[k] < 10 — qualitative mode; statistics withheld]  <!-- include in qualitative mode -->

## Section 1 — Calibration Assessment
<!-- <10: directional optimism/pessimism read in words, no percentages.
     >=10: win rate, calibration curve table (bucket | stated | actual | gap), Brier score with interpretation. -->

## Section 2 — Kill Criteria & Sunk-Cost Audit
<!-- Each bet whose kill criterion triggered: outcome, honored yes/no, consequences; >=10 adds the sunk-cost ratio. -->

## Section 3 — Key Calibration Takeaways
<!-- At most 3 actionable recommendations on estimation, scoping, or evidence habits. -->
```

## 5. Sources

- Brier score: Glenn W. Brier (1950), "Verification of Forecasts Expressed in Terms of Probability", Monthly Weather Review — [journals.ametsoc.org](https://journals.ametsoc.org)
- Confidence calibration buckets, forecasting discipline: Philip Tetlock / Good Judgment research — [goodjudgment.com](https://goodjudgment.com)
- Kill criteria and sunk-cost ratio: repo methodology (no external author claimed).
