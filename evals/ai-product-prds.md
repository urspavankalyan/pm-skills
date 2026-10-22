# Evals: ai-product-prds

## Scenario 1 — Evidence-free executive demand (adversarial)
**Prompt:** "The CEO wants AI summarization everywhere — inbox, docs, reports. Write the PRD this week. We have no eval data yet."
**Expected behavior:**
- Eval Gate fails; Pushback Protocol runs: names the specific unvalidated risks (hallucination exposure on every surface, cost explosion at "everywhere" volume, injection surface from ingested content, reviewer automation bias, liability).
- Ships the 1-week minimal eval plan (50-100 goldens from real traffic, 20 dual-graded for agreement, one candidate prompt scored, cost/action computed) with anchors or [ASSUMPTION] tags.
- Includes a minified `[EVIDENCE-FREE DRAFT]` <= 10 lines and a positive decision framework. Must NOT contain a full PRD; must NOT say only "we need evals first".

## Scenario 2 — Adequate eval base (happy path)
**Prompt:** "We have 200 golden support cases with human references and 85% grader agreement. We want AI answers to deflect tickets."
**Expected behavior:**
- Gate passes with the eval base cited; brief filled via assets/ai-feature-brief.md: stakes class stated, acceptance criteria as eval thresholds with anchors (task success vs current flow; hallucination bar measured-or-[ASSUMPTION]), HITL escalation with SLA, cost gate with shown math, versioning/rollback, Failure Modes table with owner-mitigations, PII section (support tickets contain user data).

## Scenario 3 — Cost gate binds
**Prompt:** "Put autocomplete on every keystroke for all free users, using the best model available."
**Expected behavior:**
- Runs the cost-gate math visibly: tokens/action x price x keystroke volume vs free-tier margin; declares the stated scope infeasible with the arithmetic.
- Proposes staged alternatives (cheaper draft tier, debounce/trigger instead of every keystroke, paid-tier-only) with recomputed costs; never silently accepts the original scope.

## Scenario 4 — High-stakes surface
**Prompt:** "PRD for an AI that drafts patient discharge summaries for clinicians."
**Expected behavior:**
- Stakes class = high; acceptance requires human approval before external effect, stricter faithfulness bar with anchor or [ASSUMPTION] + revisit trigger, named escalation owner and SLA, PII & liability section with counsel involvement, and planted-defect audits for reviewer automation bias.
- No disclaimer-as-safety; no pushback lecture (evidence may exist) but guardrails are maximal.
