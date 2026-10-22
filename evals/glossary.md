# Evals: glossary

## Scenario 1 — Out-of-vocabulary term in a roadmap doc (adversarial)
**Prompt:** "My CEO's roadmap memo keeps saying 'DMU'. What does DMU mean in a roadmap context?"
**Expected behavior:**
- Normalization finds no DMU entry in [../glossary/references/terms.md](../glossary/references/terms.md); Unknown-Term Protocol fires.
- Agent supplies the real external definition (DMU = Decision-Making Unit, the set of people who participate in a B2B purchase decision; B2B sales standard), tagged `[NOT IN CANONICAL GLOSSARY]`, with a named field/source.
- If a looked-up term carries two schools' meanings in the corpus, both are surfaced under `[USAGE FORK]`; if no sourced definition exists anywhere, the stipulated meaning ships tagged `[STIPULATED - NOT SOURCED]` and the user is asked where they met the term.
- Agent names the nearest canonical term (ICP) and the consequence (DMU shapes who discovery interviews target).
- Must NOT invent a product-author attribution, must NOT present the definition as canonical, must NOT silently skip the "not in glossary" statement.

## Scenario 2 — Forked term (adversarial: silent resolution trap)
**Prompt:** "Engineering says we're a feature team and they mean it as a compliment. Cagan says feature teams are bad. Who is right? Just tell me what feature team means."
**Expected behavior:**
- Fork table fires: both meanings printed with attribution (Scrum: healthy cross-functional end-to-end team; Cagan/SVPG: pejorative for list-execution with no outcome accountability).
- Agent runs the disambiguation test (outcome accountability vs list accountability) against the user's situation instead of picking a side silently.
- Must NOT declare one school "right" without the test; must NOT omit either attribution.

## Scenario 3 — Decode mode with a misuse buried in it
**Prompt:** "Decode this standup note: 'We will track cumulative signups as our North Star and treat weekly active installs as the input metric. GEM says growth first this quarter.'"
**Expected behavior:**
- Decode mode returns in-order one-line decodes for North Star, input metric, GEM.
- Misuse Flags block fires: cumulative signups fails Ellis's core-value test (`[MISUSE: North Star — cumulative vanity count, not core value delivered — canonical alternative: an activity metric expressing value, e.g. weekly completed exports]`); "weekly active installs" is flagged as an activation/output-leaning proxy unless tied to a controllable input.
- GEM decode carries attribution (Gibson Biddle) and the stage-flip note. Must NOT rewrite the whole note; must NOT pass the vanity metric unflagged.

## Scenario 4 — Draft mode picking canonical terms
**Prompt:** "I'm writing our team charter. We're an empowered team in Cagan's sense. Give me the canonical terms for: the person we build for, the one metric we align on, and the team type — and tell me which synonyms to avoid."
**Expected behavior:**
- Draft mode emits `canonical: X (avoid: y, z)` lines: ICP (avoid "target audience", "user segment" as rotation), North Star metric (avoid "main KPI", "OMTM" rotation), empowered team (avoid "feature team", "squad" without definition).
- Vocabulary choice justified by the declared Cagan operating model in one line.
- Every canonical term carries attribution; no bracketed placeholders left in the answer.
