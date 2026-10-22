# Evals: product-strategy

## Scenario 1 — Moat hand-waving (adversarial)
**Prompt:** "Write our strategy doc. Our moat is our AI and our amazing UX, and competitors can't match our brand."
**Expected behavior:**
- Pushback fires before drafting: `[MOAT-THEATER]` findings — AI/UX/brand are adjectives, not mechanisms; demand which of the four mechanisms applies and how scale strengthens each.
- ICP Gate fires (no ICP given): ask at most three questions or emit a max-10-line `[ICP-UNDEFINED DRAFT]`.
- Any doc produced carries a stress-test row per claimed advantage showing FAIL/unknown until evidenced; exit metrics anchored or `[ASSUMPTION]`.
- Must NOT produce a polished full strategy doc that repeats "AI moat" as hard-to-copy.

## Scenario 2 — Strategy for everyone (adversarial)
**Prompt:** "We serve every business that uses software. Write the vision."
**Expected behavior:**
- Beachhead refusal: "everyone" flagged as not-a-strategy; asks who hurts most first.
- Produces a max-10-line `[ICP-UNDEFINED DRAFT]` plus a positive decision framework (which segmentation evidence would pick the beachhead).
- Under `[DRAFT-ONLY]`, all downstream claims tagged `[ASSUMPTION]`.

## Scenario 3 — Bootstrapped B2B, monetization first (happy path with justified deviation)
**Prompt:** "Bootstrapped B2B invoicing tool, 8 months runway. ICP: freelance agencies of 5-20 who chase late invoices in spreadsheets today. We want monetization first. Write the strategy."
**Expected behavior:**
- GEM rank accepted with the one-line justification matching the monetization-first criteria (bootstrapped, low runway); justification line present in doc.
- DHM names a mechanism that survives the ICP stress-test (e.g. switching costs via migrated client history; no cross-company data loop).
- GLEe horizons carry quantitative exit metrics, `[ASSUMPTION]`-tagged where unanchored; OKRs are outcome-based with baselines.

## Scenario 4 — Output-OKR audit (diagnostic)
**Prompt:** "Review our OKRs: KR1 ship SSO in Q3, KR2 launch the mobile app, KR3 do 10 interviews."
**Expected behavior:**
- Loads the OKR reference; rewrites each as an outcome KR with baseline/target/anchor; interviews flagged as activity, not result.
- Must NOT accept any deliverable-shaped KR unchanged.
