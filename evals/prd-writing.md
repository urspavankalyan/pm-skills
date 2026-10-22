# Evals: prd-writing

## Scenario 1 — Evidence-free executive demand (adversarial)
**Prompt:** "The CEO wants a PRD for an AI chatbot in our B2B analytics app. Write it today."
**Expected behavior:**
- Context Gate fires; no ICP/evidence supplied.
- Pushback Protocol runs: names the four unvalidated risks specifically; 1-week discovery plan with quantitative kill criteria (anchors stated or `[ASSUMPTION]`-tagged); minified `[EVIDENCE-FREE DRAFT]` <= 10 lines; positive decision framework; the unbacked big bet is explicitly labeled `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]`.
- Must NOT contain a full PRD, must NOT say only "more research is needed".

## Scenario 2 — Vague request (diagnostic)
**Prompt:** "write me a spec for improving onboarding"
**Expected behavior:**
- Asks at most 3 targeted gate questions (ICP, evidence, appetite) OR offers `[DRAFT-ONLY]` bypass; does not dump a template immediately.
- Once answered, selects a school with stated justification and loads the matching asset.

## Scenario 3 — Bypass tag
**Prompt:** "[DRAFT-ONLY] PRD for calendar sync, we have zero research, 6-week appetite"
**Expected behavior:**
- Output headered `[DRAFT-ONLY / SANDBOX BYPASS ACTIVE]`; assumptions tagged `[ASSUMPTION]` inline; Risk Note paragraph present (>2-week effort); Shape Up school plausible given fixed appetite; no decision-journal entry written.

## Scenario 4 — Well-evidenced request (happy path)
**Prompt:** "We have 7 churn interviews citing failed CSV exports and telemetry showing 18% of active users hit export errors. Write a 6-week pitch."
**Expected behavior:**
- Gate passes with evidence cited; if a `product/` workspace exists, the strategy file is read silently and the header carries `[RESOLVED FROM WORKSPACE: product/strategy.md …]`; a request contradicting the active focus instead leads with `[STRATEGIC CONTRADICTION DETECTED]` and a justify-or-pivot ask. School = Shape Up (fixed appetite) using `assets/shaped-pitch.md`; evidence weight class stated (big batch, meets 5-interview + 15% rule); kill criteria with anchors; decision-journal entry appended/updated.

## Scenario 5 — Finalizing against a journal-written decisions.md (agreement)
**Prompt:** "Finalize the CSV export PRD (7 churn interviews, 18% telemetry, 6-week appetite). Our decisions.md already has a 'CSV Export Rescue' entry logged by a calibration-journal session last quarter, with Type, Decision, Alternatives considered, Predicted outcome, Kill criterion, Confidence and Status all filled."
**Expected behavior:**
- Does NOT append a second `## ... | CSV Export Rescue` heading: matches by decision name and appends `### Addendum [YYYY-MM-DD]` recording the finalized PRD (school, appetite, kill criteria), original prediction and confidence verbatim.
- A brand-new feature still gets the full canonical entry: `## [date] | Type: PRD commit | [name]` with Decision, Alternatives considered, anchored Predicted outcome, Kill criterion, Confidence, Status — complete enough for calibration scoring to consume unchanged.
- If an existing entry lacked a field this skill writes (e.g. no Type line), the addendum records the PRD commit without rewriting history; the canonical schema in `references/evidence-and-pushback.md` §4 is authoritative.
