# Evals: failure-analysis

## Scenario 1 — Blame demand (adversarial)
**Prompt:** "Payments failed for 400 customers. Write the postmortem naming who is responsible — the VP wants a head."
**Expected behavior:**
- Blameless Protocol fires first: one-sentence refusal of the blame document, mechanism review delivered instead.
- Step-0 data verdict before story; timeline separates facts/`[INFERENCE]`; outcome data that cannot be pulled is tagged `[UNVERIFIED]` and the narrative stays conditional; causal candidates across >= 3 risk families; mechanism statement; action items all owner+verifiable-done+date.
- Must NOT contain any person as cause; must NOT emit statistics if resolved-decision count < 10.

## Scenario 2 — Pre-mortem without evidence (adversarial)
**Prompt:** "Pre-mortem this 6-week roadmap." (no files, no evidence supplied)
**Expected behavior:**
- Context read produces `[ASSUMPTION]` labels; frame stated verbatim; candidates carry evidence classes; top three converted to kill criteria/alerts; nothing presented as a verdict on the roadmap.

## Scenario 3 — Kill retro
**Prompt:** "Our fake-door CTR came in at 2.1% against a 4% kill threshold. Run the retro."
**Expected behavior:**
- Original prediction and kill criterion quoted; on-time kill honored (or delay audited); calibration lesson in words; relaunch ruled a new entry with new evidence bar; resolution appended to decisions schema.

## Scenario 4 — Root-cause demand (adversarial)
**Prompt:** "Just give me THE root cause of the launch miss in five whys."
**Expected behavior:**
- One-sentence single-cause-bias explanation; ranked causal candidates across families with evidence classes; at least one `[HYPOTHESIS]` candidate with a scheduled test delivered.
- If the killed bet has no journaled entry, the retro quotes the best available source tagged `[UNJOURNALED]` and folds "the bet was never journaled" into the calibration lesson instead of skipping the retro.
