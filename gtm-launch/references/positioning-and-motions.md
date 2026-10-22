# Positioning & GTM Motions Reference

## 1. Dunford Positioning

**Definition.** "Positioning is the act of deliberately defining how you are the best at something that a defined market cares a lot about." It is context-setting, decomposed into five components with a dependency chain: competitive alternatives -> unique attributes -> value those attributes deliver -> target customer characteristics -> market category (-> relevant trends as an amplifying layer). Get the order wrong and the chain collapses: you cannot pick a category before you know what you uniquely do and for whom.

**When to use.** Before any launch, rebrand, or category change; when sales cycles are long because reps must "explain" the product; when prospects compare you to the wrong alternatives; when price pressure persists despite a good product.

**When NOT to use.** As a messaging exercise after the launch page is written; when the real problem is pricing or product (positioning cannot fix an offer nobody needs); as a solo-founder whiteboard session — Dunford prescribes a cross-functional team with deliberate open-mindedness.

**Key discipline.** Define competition as *competitive alternatives*, not vendor lists: the status quo (spreadsheet, manual process, do-nothing) is the deal you must actually win, and no-decision takes 20-30% of enterprise deals. Exclude "phantom competitors" no customer ever mentions — positioning against them waters you down.

**Worked Example (real).** Early Salesforce: alternatives = on-prem CRM (Siebel-era) and spreadsheets; unique attributes = browser delivery, zero installation, per-user subscription; value = CRM live in days at a fraction of the cost; segment = sales teams underserved by on-prem economics; category = head-to-head CRM, re-framed as "cloud CRM" ("the end of software"). The category made the value obvious without explanation.

**Source URLs.** [aprildunford.com](https://www.aprildunford.com/) | [Obviously Awesome](https://www.aprildunford.com/obviously-awesome) | [Positioning and Competition](https://www.aprildunford.com/post/positioning-and-competition)

### 1b. Market category styles

| Style | When to use | When NOT to use |
| :--- | :--- | :--- |
| Head-to-head | Existing category, you can be top-3 on a dimension customers care about | Category leader entrenched; your advantage not category-critical |
| Big fish, small pond | You can own a subsegment quickly and expand later | Subsegment too small to matter; no expansion path |
| Create a new game | Existing categories genuinely misfit; you can fund market education | Most cases — "unique" products with no education budget |

## 2. GTM Motions: PLG vs Sales-Led vs Hybrid

**Definition.** A motion is how the product reaches revenue: **PLG** — the product drives acquisition, conversion, expansion (self-serve, freemium/trial); **sales-led** — human motion drives qualification, demo, procurement; **hybrid** — PLG acquires and qualifies, sales expands and closes enterprise.

**Decision criteria.**

| Signal | Favors PLG | Favors sales-led |
| :--- | :--- | :--- |
| ACV | Low, credit-card (commonly cited band: under ~$5-10K/yr `[ASSUMPTION]`) | High, procurement (commonly cited band: over ~$25K/yr `[ASSUMPTION]`) |
| Time-to-value | Solo user reaches value in one session | Requires implementation, configuration, expertise |
| Buying committee | End user decides | Multi-stakeholder, security review, legal |
| Expansion shape | Bottom-up usage growth inside accounts | Top-down account contracts |

Hybrid is the default destination once ACV supports a sales seat: pure PLG tops out at enterprise, pure sales-led leaves cheap acquisition on the table (OpenView; General Catalyst). The middle ACV band (~$10-25K/yr) is where hybrid most commonly wins (`[ASSUMPTION]` — industry heuristic; recalibrate to your deal data).

**PLG prerequisites (refuse PLG without them):** product delivers discoverable value fast; low-friction signup; usage data you can act on (PQLs). "Deliver value before capturing value" is the operating rule.

**Worked Examples (real).** PLG: Calendly and Slack — self-serve adoption, bottom-up spread. Sales-led: Snowflake and enterprise Salesforce — complex buying, high ACV, procurement. Hybrid: HubSpot and Atlassian — free/self-serve entry with sales layered for enterprise expansion.

**Source URLs.** [OpenView: Product-Led Growth](https://openviewpartners.com/product-led-growth) | [OpenView: Pillars of PLG](https://openviewpartners.com/blog/pillars-of-plg-growth) | [General Catalyst: Sales-Led vs Product-Led Growth](https://www.generalcatalyst.com/stories/sales-led-vs-product-led-growth)

## 3. Staged Rollout Design

**Definition.** A cohort-laddered release — 100% internal dogfood, then 5%, 25%, GA — where each gate's kill thresholds are derived from the previous gate's measured baseline, so "how it went" is always a number, not a feeling.

**When to use.** Every product launch with real users at stake; mandatory when the change touches billing, data, or compliance surfaces.

**When NOT to use.** Purely internal tooling with a willing captive team (gate 0 alone suffices); emergency security fixes (ship with a rollback path, not a rollout ladder).

**Design notes.**
- Gate 0 exists to produce the baseline: error rate, activation, support-ticket rate, internal WAU. Thresholds at gates 1-2 that lack a measured baseline are `[ASSUMPTION]` until gate 0 supplies one.
- Instrumentation verification is a gate, not a checkbox: fire test events and observe them in every dashboard and alert that the rollout will rely on.
- Every breach pauses the ladder and forces a written diagnose-or-roll-back decision within 48h; silent breaches are the failure mode.
- GA is a written go decision against the gate-2 baseline, followed by 30 days of post-GA guardrails.

**Worked Example (hypothetical).** Hypothetical: self-serve analytics add-on. Gate 0 (4 weeks internal) yields baseline: 0.4% error rate, 55% activation, 0.8 tickets per 100 sessions. Gate 1 at 5% kills if error rate > 0.8%, activation < 28%, or tickets > 1.6/100. Gate 1 runs two clean weeks; gate 2 repeats thresholds at 25%; GA decision cites the gate-2 readout.

**Worked Example (real).** Staged cohort rollouts are canonical infrastructure practice (canary releases at Google-scale companies); the same discipline applied to product launches is what converts "launch week" from theater into a controlled experiment.

**Source URLs.** [OpenView: Navigating your SaaS product launch](https://openviewpartners.com/blog/navigating-your-saas-product-launch-lead-generation-and-enterprise-sales-starting-from-the-bottom-up) | [OpenView: PLG benchmarks](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks)

## 4. Sources

- April Dunford, *Obviously Awesome* — [aprildunford.com](https://www.aprildunford.com/)
- OpenView (PLG coinage, Blake Bartlett) — [openviewpartners.com](https://openviewpartners.com/product-led-growth)
- General Catalyst — [generalcatalyst.com/stories/sales-led-vs-product-led-growth](https://www.generalcatalyst.com/stories/sales-led-vs-product-led-growth)
