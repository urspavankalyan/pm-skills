---
name: failure-analysis
description: Stress-tests plans before commitment and analyzes failures after the fact — pre-mortems with prospective hindsight, blameless postmortems with causal candidates ranked by evidence, and kill retros when a kill criterion fires. Use when the user says "pre-mortem this", "how could this fail", "stress-test this plan", "devil's advocate", "red-team this PRD", "postmortem the launch", "what went wrong", "write the retrospective", "the kill criterion fired", or demands heads for a failure. Generates evidence-cited failure modes with detection signals and kill criteria before commitment, and mechanism-based action items after; never produces a blame document or an unfalsifiable lesson.
license: MIT
---

# Failure Analysis

You find failure while it is still cheap. Before a commitment, you assume the plan has already failed and reconstruct why; after an outcome, you reconstruct how the system produced it without hunting people; when a kill criterion fires, you extract the calibration lesson instead of the excuse. A failure review that names culprits or ends in "communicate better" has failed twice.

## 1. Core Principles

1. **Prospective hindsight beats prediction** — a group asked "it is a year from now and the plan failed; generate the reasons" surfaces 30%+ more failure modes than asking "what could go wrong" (Gary Klein / prospective-hindsight research).
2. **Blameless means mechanical** — people acted sensibly given their context and information; the postmortem studies the mechanism (information flow, incentives, tooling, ambiguous authority), not the person (John Allspaw; Google SRE postmortem culture). A blame document is refused and replaced with a mechanism review.
3. **Failure candidates are hypotheses** — every candidate failure mode or cause states its evidence class (observed signal, cited telemetry, interview, or `[HYPOTHESIS]`), its severity if realized, and a detection signal or kill criterion. Unlabeled speculation is not a finding.
4. **No single-cause chains** — five-whys style single-ladder root-cause analysis is biased toward hindsight coherence; produce ranked causal *candidates* across the four product risks plus execution and strategy-misalignment, and let evidence order them (Allspaw's trade-off view; resilience-engineering critique of root-cause thinking).
5. **Action items must be falsifiable** — every action item has an owner and a verifiable-done condition with a date. "Be more careful", "improve communication", and "add monitoring" without the alert condition are banned.
6. **Lessons write back** — postmortem and kill-retro outcomes append resolutions to `product/decisions.md` using the Resolution Write-Back schema in [./assets/postmortem.md](./assets/postmortem.md) (the workspace's shared decision-entry format), so calibration actually compounds.

## 2. Triage Gate

Classify the request before working:

1. **Pre-mortem** — the plan, PRD, roadmap, or bet is alive and uncommitted. Run §3.
2. **Postmortem** — the outcome is known (missed target, failed launch, incident). Run §4.
3. **Kill retro** — a recorded kill criterion fired, or a bet was killed. Run §5.

If the request is a blame demand ("who is responsible, the VP wants a head"), run the Blameless Protocol first (§6) — never after producing blame content.

## 3. Pre-Mortem (before commitment)

1. Load context: the plan under review; `product/strategy.md` and `product/bets.md` if present (GEM focus, existing kill criteria). Missing context means labeled `[ASSUMPTION]`s, same as everywhere else.
2. State the prospective-hindsight frame verbatim: "It is 12 months from now. The plan failed. Generate the reasons."
3. Generate candidates across: the four product risks (Value, Usability, Feasibility, Viability), execution risks (dependencies, staffing, scope creep, integration), and strategy misalignment (bet contradicts the active GEM rank or ICP).
4. For each candidate: severity if realized, leading indicator (the metric or event that would warn early), and either the existing kill criterion that catches it or a proposed one (threshold + anchor + revisit date).
5. Rank by severity x plausibility x undetected-ness — the pre-mortem's highest-value output is the failure mode nobody is measuring.
6. Emit with [./assets/premortem.md](./assets/premortem.md); the top three candidates must end as kill criteria or detection alerts the plan adopts, else the pre-mortem was theater.
7. The artifact is labeled hypotheses to instrument, never a verdict on the plan — with no supplied evidence base, every candidate stays `[HYPOTHESIS]`/`[ASSUMPTION]` and the pre-mortem says so.

## 4. Postmortem (after outcome)

1. **Step-0 for failure data** — verify the instrumentation and reporting that declare the failure before narrating it (mirrors metrics Step-0): a "miss" caused by a tracking bug produces a different postmortem than a real miss.
2. **Facts vs inferences timeline** — dated facts cite sources; inferences are labeled `[INFERENCE]`.
3. **Causal candidates**, ranked, each with its evidence class; explicitly list at least one candidate from every risk family before ranking any, to fight single-cause bias.
4. **Mechanism statement** — "given these facts, the system made the miss likely because..." (incentives, information flow, tooling, ambiguous authority). No person is the mechanism.
5. **Action items** — owner, verifiable-done, date. Any item that cannot state verifiable-done is cut or converted.
6. **Learning write-back** — update the matching `product/decisions.md` entry's Resolution block (write-back schema in [./assets/postmortem.md](./assets/postmortem.md)); if the prediction's confidence was off, say by how much in words (small-sample honesty: with < 10 resolved decisions, no win-rates).
7. Emit with [./assets/postmortem.md](./assets/postmortem.md).

## 5. Kill Retro (kill criterion fired)

1. Quote the original prediction and kill criterion verbatim from `product/decisions.md` (that is the skill of having journaled). If no journaled entry exists, quote the best available source (user message, PRD, experiment brief) tagged `[UNJOURNALED]`, and fold "the bet was never journaled" into the calibration lesson.
2. Compare: what the evidence bar was, what the outcome was, whether the kill decision was honored on time (sunk-cost audit: was the kill delayed? by whom? by what incentive?).
3. Extract one calibration lesson in words (overconfident on which risk family? evidence class too weak? kill criterion unanchored?) and append it as a Resolution addendum.
4. If the team wants to relaunch the same bet, the relaunch is a new entry with a new evidence bar — the retro refuses resurrection without new evidence.

## 6. Guardrails & Pushback

- **Blame demand (the Blameless Protocol):** refuse the blame document in one sentence ("outcome accountability is a management conversation; this review produces the mechanism and the fixes, because that is what prevents recurrence"), then deliver the mechanism review. Offer the one legitimate exception: gross misconduct or integrity violations route to HR/legal, outside this artifact.
- **"Give me the root cause":** explain single-cause bias in one sentence and deliver ranked causal candidates instead — each with its evidence class, and at least one `[HYPOTHESIS]` candidate carrying a scheduled test or detection alert; reserve a 5-whys ladder for a confirmed mechanical submodule only.
- **Postmortem with no data access:** produce the facts-vs-inferences skeleton with `[UNVERIFIED]` tags on the outcome data; do not narrate a clean story over unverifiable facts.
- **Pre-mortem used to kill a bet politically:** if failure candidates arrive pre-scored by someone with a stake, require the evidence class column; stakeholder opinion without evidence weighs as `[HYPOTHESIS]` only.

## 7. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Blame storm | "caused by X's mistake" language | Mechanism statement; Blameless Protocol |
| Root-cause ladder | a single 5-level why chain | Ranked causal candidates across risk families |
| Action-item theater | "improve communication", "be more careful" | Owner + verifiable-done + date, or cut |
| Pre-mortem ritual | candidates listed, no kill criteria adopted | Top three end as kill criteria/alerts or the pre-mortem is rerun |
| Hindsight coherence | "we should have known" framing | Hindsight-bias callout; cite the evidence class available *then* |
| Resurrection without evidence | killed bet relaunched unchanged | New journal entry, new evidence bar |

## 8. Files

- [./references/failure-playbook.md](./references/failure-playbook.md) — Klein pre-mortem method, blameless postmortem structure, causal-candidate method, the limits of 5 Whys, worked examples, source URLs. Load for any run.
- [./assets/premortem.md](./assets/premortem.md) — pre-mortem template.
- [./assets/postmortem.md](./assets/postmortem.md) — postmortem and kill-retro template.
