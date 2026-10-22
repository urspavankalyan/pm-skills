---
name: empowered-teams
description: Charters product teams as empowered, outcome-owning teams — and tells you honestly when a feature team is the right call instead. Use when the user asks about team structure, feature-factory complaints, team charters, transitioning to empowered teams, assigning OKRs to teams, or says "we want empowered teams" while handing over a feature list. Applies Cagan's decision criteria, runs a feature-to-outcome transition protocol with pilots and checkpoints, and pushes back on empowerment theater with a charter rewrite instead of a rename.
license: MIT
---

# Empowered Teams & Team Charters

An empowered team is given business problems to solve and held accountable for outcomes. A feature team is given a list to ship and held accountable for dates. Both exist; the failure is theater — calling a feature team empowered while keeping its feature list. This skill writes honest charters for both modes.

## 1. Core Principles

1. **Problems, not features** — empowered teams are given a small number of significant problems (objectives) and own the solution; accountability is for business results (Cagan / SVPG).
2. **Empowered is not unmanaged** — managers staff, coach, and set constraints; teams get autonomy inside explicit viability and feasibility guardrails. Empowerment without coaching is abandonment (Cagan).
3. **Feature teams are sometimes right** — where requirements are dictated by contract, regulation, or an execution-only business model, a feature team with honest delivery accountability beats a fake empowered one (Cagan / SVPG).
4. **Transitions happen by charter, not announcement** — renaming a team without rewriting its charter, metric, and authority produces theater. Pilot first, then scale what worked (Cagan; SVPG pilot-teams guidance).
5. **Accountability is outcome evidence** — reviews ask "which outcome moved, on what evidence?", never "did you ship the list?"

## 2. Diagnose the Current Charter

Feature-team signals: roadmap is a stakeholder list; success means on-time delivery; the PM writes backlogs; solutions are assigned by execs; the team cannot say no.
Empowered signals: the team names the problem it owns; it has its own outcome metric; it proposed solutions leadership did not order; it can say no with evidence.
Ask the user for two concrete recent examples (where last quarter's roadmap came from; what the last review asked) before classifying.

## 3. Mode Selection (Decision Criteria)

**Choose empowered teams if:**
- Product-market fit is established, or is being searched for in a dynamic market where the solution is unknown.
- The team has (or is being coached toward) strong product, design, and engineering skill.
- Leadership will hand over problems and accept solutions it did not order.

**Choose feature teams if:**
- Requirements are dictated by signed contracts, regulatory deadlines, or an execution-only business model (custom enterprise builds, compliance rollouts).
- The team lacks discovery skills and no coaching is available — then build skills first or charter honestly as delivery.

State the chosen mode in one line quoting the matching criterion.

## 4. Workflow

1. Diagnose (§2) with the user's concrete examples.
2. Select the mode (§3).
3. Load [./assets/team-charter.md](./assets/team-charter.md) and write the charter: owned problem, outcome metric (baseline/target/anchor), authority and no-gos, constraints, evidence access, review cadence.
4. For transitions, run the Transition Protocol (§5): one pilot team, one problem, checkpointed.
5. If leadership language and leadership behavior disagree ("empowered" + a feature list), run Pushback (§6) before chartering.

## 5. Transition Protocol (Feature to Outcome Charter)

1. Leadership commits in writing to problems, not deliverables, for the pilot team — one page, signed.
2. Rewrite the top three roadmap items as problems with current outcome-metric baselines.
3. Give the team discovery capacity: weekly customer contact and telemetry access; the manager coaches, does not assign.
4. Keep untransitioned teams on honest feature charters — dated, delivery-accountable, no theater there either.
5. Checkpoint at 90 days [ASSUMPTION — tune to your cycle length]: success = the team proposed at least one solution leadership did not order and it moved the owned metric; failure = revert the charter and fix the missing ingredient (skill, authority, or leadership commitment) before retrying.

## 6. Pushback / Guardrails

- **"Empowered" + handed feature list** — emit `[CHARTER CONTRADICTION]`: quote the list against the claimed mode; convert the top three items into problem statements with candidate outcome metrics; refuse to label the list empowered.
- **No leadership commitment available** — recommend an honest feature charter over empowerment theater; name what would change the call (written problem commitment, coaching budget).
- **Empowerment demanded in a contractual shop** — cite the feature-team legitimacy criteria (§3); propose the hybrid: empowered where problems are unknown, feature where they are dictated.

## 7. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Empowerment theater | Team renamed "empowered", roadmap still a stakeholder list | Charter rewrite (§4), pilot first (§5) |
| Outcome laundering | "Outcome" metric is a deliverable count ("ship 6 features") | Metric must move a business/customer number with a baseline |
| Abandoned teams | Autonomy without coaching, constraints, or evidence access | Add manager coaching cadence, guardrails, discovery access |
| Feature shame | Contractual team told it should act empowered | Honest feature charter with delivery accountability |

## 8. Files

- [./references/team-charter.md](./references/team-charter.md) — Cagan's positions, full decision criteria, transition politics, worked examples. Load for any diagnosis or transition.
- [./assets/team-charter.md](./assets/team-charter.md) — fill-in charter templates (empowered and feature variants).
