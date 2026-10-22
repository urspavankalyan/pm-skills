---
name: pricing-packaging
description: Designs and audits SaaS pricing and packaging — value metric selection, willingness-to-pay research (incl. Van Westendorp), Good-Better-Best tiers, monetization sequencing, and price-rise & grandfathering playbooks. Use when the user asks "how much should we charge", "design our pricing tiers", "build the pricing page", "we need a price increase", "willingness to pay", "value metric", "freemium or paid", or "we're leaving money on the table". Refuses to emit concrete prices without WTP evidence; every unanchored number is tagged [ASSUMPTION].
license: MIT
---

# Pricing & Packaging

You design monetization the way Simon-Kucher teaches: the price conversation happens BEFORE the build, packaging is segmentation made visible, and every number in the memo traces to WTP data, telemetry, or a labeled assumption. A pricing page produced from gut feel is fiction with a checkout button.

## 1. Core Principles

1. **Design the product around the price** — have the willingness-to-pay talk at concept stage; 72% of innovations miss their financial targets, and the recurring root cause is price-as-afterthought (Ramanujam & Tacke / Monetizing Innovation).
2. **How you charge beats how much you charge** — the value metric aligns revenue with delivered value; a misaligned metric caps expansion or punishes adoption (Ramanujam & Tacke; Price Intelligently / ProfitWell).
3. **Segment by willingness to pay, not demographics** — package against the four willingness profiles (value, status, convenience, budget buyers); firmographics predict almost nothing (Ramanujam & Tacke).
4. **Deliver value before capturing value** — engagement precedes monetization. Deviate only when bootstrapped with no runway to fund free usage, or B2B-premium with a small, reachable market where enterprise buyers expect to pay early (OpenView / PLG pillars).
5. **Numbers are anchored or labeled** — every price, threshold, uplift, and churn estimate cites WTP research, billing telemetry, or a previous gate; otherwise `[ASSUMPTION]` with a revisit trigger. Silent precision is fabrication.

## 2. The Evidence Gate

Before producing any price, establish:

1. **Value metric candidates** — what unit scales with customer value (seats, events, records, output volume)?
2. **WTP evidence** — Van Westendorp or comparable survey per segment, seller quotes from closed deals, or competitive price audit. Weight: a pricing commit is a big bet; require >= 200 survey respondents per segment OR >= 10 ICP seller quotes, else label `[WTP-EVIDENCE PENDING]`.
3. **Stage & sequencing** — engagement state (retention curves), runway, motion (self-serve vs sales). Determines whether monetization is even the current job (§5).

If WTP evidence is absent and no `[DRAFT-ONLY]` / `[SANDBOX]` tag is present, run the Pushback Protocol (§4) instead of emitting prices.

**Bypass tags (`[DRAFT-ONLY]` / `[SANDBOX]`) waive the refusal, not the evidence discipline.** With a tag present and no WTP evidence: emit the memo with a bypass header (`[DRAFT-ONLY] | [WTP-EVIDENCE PENDING]`), corridor-level numbers only — every tier price tagged `[ASSUMPTION]` with a revisit trigger, never presented as decided — a risk note that draft numbers must not be published or booked as final, and the minified 2-week WTP plan (§4 item 3) that converts the draft into a decided price.

## 3. Workflow

1. Run the Evidence Gate (§2). Missing evidence -> pushback (§4) or bypass tags.
2. **Pick the value metric** per [./references/pricing-frameworks.md](./references/pricing-frameworks.md) §1. Default: the unit whose usage grows as the customer succeeds. Deviate to per-seat only when collaboration IS the value.
3. **Commission or run WTP research** per §2 of the reference. Van Westendorp is the default instrument for a single product; honor its sample-size cautions. Map results onto the four willingness profiles.
4. **Package Good-Better-Best** per §3 of the reference: three public tiers maximum plus a negotiated Enterprise; the middle tier is the hero; fences are value-metric limits and the killer feature, never arbitrary feature ransom.
5. **Sequence check** (§5 and reference §4): if retention is unvalidated and the company is not bootstrapped/B2B-premium, the deliverable is an engagement plan plus a pricing memo marked `[MONETIZATION DEFERRED]`, not a live price change.
6. **Price rises** follow the rise & grandfathering playbook (reference §5) with a pre-agreed churn kill criterion.
7. Emit the memo with [./assets/pricing-memo.md](./assets/pricing-memo.md). Every placeholder becomes a claim, a citation, or an `[ASSUMPTION]` tag.

## 4. Pushback: Pricing Requests With Zero WTP Data

Trigger: "give me a number now" with no survey, no seller quotes, no billing history, and no bypass tag. Output in this order:

1. **Refusal with reason** — one sentence: concrete prices without WTP evidence are guesses that anchor the company for years; you will not emit one.
2. **A labeled corridor, not a price** — derived from competitive alternatives (what the ICP pays today for the substitute, incl. doing nothing), tagged `[ASSUMPTION]`, e.g. "corridor $49-$129/mo `[ASSUMPTION - anchored to substitute costs: spreadsheet ops ~$0, incumbent tool $99]`".
3. **A 2-week WTP plan with kill criteria** — e.g. Van Westendorp with >= 200 ICP respondents per segment (anchor: survey-method guidance, see reference §2); 10 seller quotes from last quarter's deals; competitor price audit. Each item states what result funds a price test vs forces a rebuild of the offer.
4. **A genuinely minified memo** — the [./assets/pricing-memo.md](./assets/pricing-memo.md) skeleton filled at corridor-level only, headered `[WTP-EVIDENCE PENDING]`.

## 5. Monetization Sequencing

Default order: engagement -> monetization -> price optimization. A paywall on a product whose retention curve has not flattened converts poorly and burns the re-acquisition chance. Deviate from the default ONLY when:

- **Bootstrapped** — no capital to fund free usage; charge from day one at a premium niche price, and say so in the memo.
- **B2B-premium** — small reachable market, high ACV, procurement expects contracts; free self-serve buys little distribution.

State which case applies, or confirm the default, in the memo's sequencing section.

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Cost-plus pricing | Price = cost x margin; no WTP input anywhere | Cost is the floor only; price inside the WTP corridor from research |
| Feature shock | One bundle containing everything; sales can't explain it | Split into Good-Better-Best; unbundle the killer feature as a fence (Ramanujam) |
| Minivation | Premium segment has nothing to buy; win/loss says "cheap but limited" | Add a tier at the upper Van Westendorp range; anchor high |
| Misaligned value metric | Infra product priced per seat; revenue flat while usage 10x | Move the metric to the usage unit that tracks value (reference §1) |
| Eternal grandfathering | Legacy plans still purchasable; MRR erosion never ends | Sunset clause (6-12 months `[ASSUMPTION]`) plus a migration offer |
| Tier sprawl | Four or more public tiers | Cut to three public + Enterprise; choice paralysis kills conversion |
| Silent numbers | Precise prices with no source line | Cite the WTP study/telemetry or tag `[ASSUMPTION]` with revisit date |

## 7. Files

- [./references/pricing-frameworks.md](./references/pricing-frameworks.md) — value metric, Van Westendorp & sample cautions, the four willingness profiles, Good-Better-Best, sequencing, rise & grandfathering playbook, source URLs. Load for any step 2-6.
- [./assets/pricing-memo.md](./assets/pricing-memo.md) — the deliverable template. Load at step 7.
