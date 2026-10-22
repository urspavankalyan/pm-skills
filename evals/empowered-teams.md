# Evals: empowered-teams

## Scenario 1 — "Empowered" plus a feature list (adversarial)
**Prompt:** "We're moving to empowered teams. Here's the list of 25 features they must ship this quarter, with dates."
**Expected behavior:**
- `[CHARTER CONTRADICTION]` fires: quotes the list against the claimed mode.
- Converts the top three items into problem statements with candidate outcome metrics; refuses to label the list empowered.
- Asks for leadership's written problem commitment; offers the Transition Protocol with a pilot team and 90-day checkpoint.
- Must NOT produce an "empowered team charter" whose objectives are 25 features.

## Scenario 2 — Regulated shop (legitimate feature team)
**Prompt:** "We're a bank. Regulators mandate the new reporting format by June. Should this team be 'empowered'?"
**Expected behavior:**
- Cites the legitimacy criteria: dictated what/when means honest feature charter; dates as commitments; no feature shame.
- May offer a mixed charter for the non-dictated slice; must NOT force empowerment on mandated work.

## Scenario 3 — Transition request (happy path)
**Prompt:** "Our feature team wants to move to outcomes. Leadership is open but nervous. Give us a transition plan and a charter."
**Expected behavior:**
- Loads the reference and the charter template.
- Transition Protocol: pilot team, written problem commitment, top-three rewrite as problems with baselines, discovery capacity, 90-day checkpoint tagged `[ASSUMPTION]`.
- Charter carries an outcome metric with baseline/anchor, authority, constraints, evidence access, and the outcome review question.

## Scenario 4 — Accountability question (diagnostic)
**Prompt:** "If the team picks its own solutions, how do I hold them accountable?"
**Expected behavior:**
- Answers with outcome evidence: owned metric with baseline/target, review question "which outcome moved", checkpointed cut-or-kill cadence; rejects "accountable = shipped the list".
- Names the manager's real job: staffing, coaching, constraints (Cagan).
