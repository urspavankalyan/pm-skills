---
name: product-strategy
description: Writes and audits product strategy documents as one coherent sequenced bet — ICP first, then moat mechanisms, focus ranking, horizon sequencing, and team OKRs. Use when the user asks to write a product strategy, strategy doc, vision, moat or defensibility analysis, or market positioning, or says "what should our strategy be" or "review our strategy". Enforces ICP-before-frameworks, named moat mechanisms stress-tested against the ICP's regulatory constraints, quantitative phase-exit criteria, and pushes back on moat theater and strategy-without-a-customer instead of drafting fiction. Positioning here is the strategic bet (which customer, which moat); launch messaging and category positioning for market entry belong to the GTM discipline.
license: MIT
---

# Product Strategy

A strategy is a sequenced bet: who you win with first, the mechanism that makes the win defensible, and what you prove before you expand. A document that names aspirations and frameworks without that sequence is a wish list — this skill exists to prevent that.

## 1. Core Principles

1. **ICP before frameworks** — every strategy document opens with "who do we win with first?", answered with workflows, constraints, and alternatives. A strategy that tries to delight everyone is not a strategy (Biddle / DHM; Cagan / SVPG).
2. **Moats are mechanisms, not adjectives** — "hard to copy" must name one of four mechanisms (network effects, proprietary data loop, switching costs, scale economies) and state how it strengthens as the business scales (Biddle / DHM).
3. **The moat must survive its own ICP** — stress-test every mechanism against the chosen ICP's regulatory, privacy, and commercial constraints. A data loop the ICP's compliance regime forbids is moat theater (Biddle / DHM stress-test).
4. **Sequencing, not listing** — focus is ranked (GEM) and horizons are gated by quantitative phase-exit criteria (GLEe). Unranked priorities are unfalsifiable (Biddle).
5. **Assumptions labeled, never silent** — every market size, share target, and exit metric states its anchor (cohort data, market report) or is tagged `[ASSUMPTION]` with a revisit trigger.

## 2. The ICP Gate

Before drafting or auditing, establish:

1. **ICP** — the segment with highest problem intensity; their workflows, constraints, alternatives.
2. **Stage & context** — funding model, runway, market type (bootstrapped B2B vs VC consumer changes the default GEM ranking).
3. **Ask** — full strategy doc, moat audit, multi-year vision, or quarterly focus alignment.

If the ICP is missing: ask at most three targeted questions, or proceed under labeled bypass when the prompt contains `[DRAFT-ONLY]` or `[SANDBOX]` (header `[DRAFT-ONLY / SANDBOX BYPASS ACTIVE]`, all ICP-dependent claims tagged `[ASSUMPTION]`).

## 3. Framework Selection

| Ask shape | Default |
| :--- | :--- |
| Full strategy doc | [./assets/strategy-doc.md](./assets/strategy-doc.md); sequence ICP, DHM, GEM, GLEe, OKRs |
| "Is our moat real?" audit | DHM stress-test only, findings memo |
| Multi-year vision for board/investors | GLEe horizons with exit metrics |
| Quarterly/annual focus alignment | GEM ranking with explicit justification |
| Competitive threat or market structure | Aggregation Theory |
| API/ecosystem bet | Platform vs Product |
| Translating strategy to teams | OKRs via [./references/okr-examples.md](./references/okr-examples.md) |

Include only the sections the ask needs, in this order. Full definitions and worked examples: [./references/frameworks.md](./references/frameworks.md).

## 4. Workflow

1. Run the ICP Gate (§2).
2. Load [./assets/strategy-doc.md](./assets/strategy-doc.md) for docs; skip the template for audits and produce findings first.
3. Write the ICP section first; every later section names it.
4. DHM: for each claimed advantage, name mechanism + how scale strengthens it; run the ICP regulatory stress-test; failures go to findings as moat theater with a replacement candidate.
5. GEM: state the rank in one line. Default Engagement, Monetization, Growth for early-stage VC software; Monetization first when bootstrapped, low runway, or premium B2B. Any other order needs a written justification.
6. GLEe: exactly one active horizon; every horizon carries a quantitative exit metric with anchor or `[ASSUMPTION]`.
7. OKRs: map the active horizon to 1-3 objectives per team; key results are outcome metrics with baselines, never deliverables.
8. Close with Will-Not-Do and the assumptions log.
9. Sync the workspace state (§7): refresh `product/strategy.md` whenever a finalized ask changes the ICP, the GEM rank, or the cycle appetite; if the file is absent and the user works across sessions, offer to initialize workspace state from the finalized sections.

## 5. Pushback / Guardrails

Run pushback BEFORE a full draft when:

- **Moat theater** — advantages labeled without mechanisms ("our moat is AI/UX/brand"). Output: `[MOAT-THEATER]` finding naming the missing mechanism, the scale-strengthening question, the ICP regulatory stress-test result, and the evidence that would upgrade the claim to a moat.
- **Strategy without a customer** — "we serve everyone". Refuse a full doc; output at most a 10-line `[ICP-UNDEFINED DRAFT]` plus up to three beachhead questions.
- **Framework smoothie** — every framework at once, none ranked. Return a ranked sequence; demand a GEM rank decision.

Format: numbered findings first, then a minified draft, then a positive decision framework (the exact conditions under which the user's framing would be right).

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Moat theater | "Hard to copy" with no mechanism, or a mechanism the ICP's regulations forbid | Name mechanism, scale-strengthening, run the stress-test |
| Strategy for everyone | ICP/segment absent from page one | Beachhead first; the rest is Later horizon |
| Horizon bleed | Expand initiatives while the beachhead exit metric is unmet | Gate expansion on the quantitative exit criterion |
| Unranked priorities | "Growth, engagement, and monetization all matter" | Force GEM rank with written justification |
| Output OKRs | Key results read "ship X" | Rewrite as baseline-to-target outcome metrics |
| Silent numbers | Precise market sizes with no source | Anchor, or `[ASSUMPTION]` plus revisit date |

## 7. Workspace State

When the user keeps a `product/` workspace, this skill is the sole writer of `product/strategy.md` — the compact state header other sessions read for ICP, focus, and appetite. The full strategy doc and the state header are distinct artifacts; never merge them.

Schema (keep exactly this shape; restated here so this skill stays self-contained):

```markdown
# Product Strategy State
Last-updated: YYYY-MM-DD

## ICP
- **Segment:** [who we win with first]
- **Workflows:** [what they do today]
- **Constraints:** [regulatory / privacy / commercial limits that shape the moat]
- **Alternatives:** [what they use instead, including doing nothing]

## Active Strategic Focus (GEM)
- **Rank:** [1st] > [2nd] > [3rd]
- **Justification:** [one line]

## Cycle Appetite
- **Big batch:** [6-week cycles, N teams] | **Small batch:** [2-week cycles, M slots]

## Stage & Context
- [funding model, runway, market type — one line]
```

Rules: refresh `Last-updated` on every write; readers treat age > 90 days as stale (`[WARNING: strategy.md may be stale]`); no filesystem means emitting the block fenced for the user to file. When the file is absent and continuity across sessions is wanted, offer to **initialize workspace state** and write it from the finalized sections. Fill-in template: [./assets/workspace-strategy.md](./assets/workspace-strategy.md).

## 8. Files

- [./references/frameworks.md](./references/frameworks.md) — every framework in five-part form (ICP-first, DHM + moat mechanisms + ICP stress-test, GLEe + exit criteria, GEM + monetization-first conflict, Aggregation Theory, Platform vs Product, OKRs). Load when drafting or auditing any section.
- [./references/okr-examples.md](./references/okr-examples.md) — good vs bad OKR rewrites and anchoring rules. Load when writing the OKR section.
- [./assets/strategy-doc.md](./assets/strategy-doc.md) — fill-in template for the full strategy document.
- [./assets/workspace-strategy.md](./assets/workspace-strategy.md) — `product/strategy.md` state-header template. Load when initializing or refreshing workspace state.
