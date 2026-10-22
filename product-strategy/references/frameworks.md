# Product Strategy Frameworks

Every framework entry carries Definition / When to use / When NOT to use / Worked Example / Source URL. The ICP-first rule (§1) is the gate all other frameworks run behind.

## 1. The ICP-First Rule

- **Definition:** The Ideal Customer Profile is the specific segment that experiences the highest problem intensity and receives the maximum value from your product, defined by workflows, constraints, and alternatives — not demographics alone.
- **When to use:** Before any other framework; as the first section of every strategy document; as the lens for the DHM regulatory stress-test (§2).
- **When NOT to use:** Never skipped. Even platform strategies name their first-side beachhead ICP before ecosystem design.
- **Application rule:** Open the document with "Who do we win with first?" and answer with their workflows, their constraints, and what they do today instead of you.
- **Worked Example:** Netflix 1999-2005: the ICP was not "everyone who watches movies" but US early adopters with DVD players who hated video-store late fees. That beachhead set DVD-by-mail economics and funded the later expansion (Gibson Biddle was VP Product through this period).
- **Source URL:** [svpg.com/articles](https://svpg.com/articles/) (Cagan on target customer); [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/) (Biddle's strategy series).

## 2. The DHM Model & Moat Mechanisms

- **Definition:** A product strategy must **D**elight customers in **H**ard-to-copy, **M**argin-enhancing ways — all three simultaneously (Gibson Biddle, former Netflix VP Product). Two of three is a feature, not a strategy.
- **When to use:** Defining or auditing a strategy's defensibility and business value.
- **When NOT to use:** Cycle execution, backlog prioritization, operational troubleshooting. Prerequisite: ICP defined (§1).
- **Moat mechanisms:** "Hard to copy" is accepted only by naming one of these plus how scale strengthens it:
  1. **Network effects** — each new user raises the product's value for existing users.
  2. **Proprietary data loop** — usage data improves the algorithm, which improves experience, which generates more data.
  3. **Switching costs** — deep workflow integration (custom APIs, migrated data) makes leaving cost-prohibitive.
  4. **Scale economies** — volume drives marginal cost below what competitors can match.
- **Rule (ICP regulatory stress-test):** Every mechanism is stress-tested against the chosen ICP's regulatory, privacy, and commercial constraints. A cross-company "data sharing loop" is legally and commercially impossible in regulated segments (B2B fintech, healthcare) under SOC2, HIPAA, or PCI-DSS constraints. A mechanism that cannot survive its own ICP's constraints is **moat theater**: replace it, or document the constraint and pick a different mechanism.
- **Worked Example:** Netflix recommendation engine. Delight: members find something to watch in under a minute instead of browsing. Hard-to-copy: the viewing-data loop compounds — a new entrant with a better algorithm but zero history cannot close the gap. Margin: better match lowers churn, the dominant cost in subscription economics.
- **Source URL:** [gibsonbiddle.substack.com/p/how-to-delight-customers-in-hard](https://gibsonbiddle.substack.com/p/how-to-delight-customers-in-hard) (Biddle; mirrored at [medium.com/@gibsonbiddle](https://medium.com/@gibsonbiddle/how-to-delight-customers-in-hard-to-copy-margin-enhancing-ways-ee53e77b214d)).

## 3. The GLEe Model

- **Definition:** Multi-year sequencing: **G**et big on a beachhead, **L**ead that space, **E**xpand into adjacencies (Biddle).
- **When to use:** Explaining a 5-15 year vision to boards, investors, and the company; sequencing major initiatives.
- **When NOT to use:** Near-term quarterly roadmaps or single-cycle planning.
- **Rule (quantitative phase-exit criteria):** Every horizon carries a quantitative exit metric that triggers the transition; unwritten exit criteria turn horizons into vibes. Examples (each `[ASSUMPTION]` unless anchored to your cohort or market data):
  1. *Get big exit:* validated initial PMF — e.g. "40% weekly retention across 50 active ICP teams" [ASSUMPTION].
  2. *Lead exit:* dominant position — e.g. "25% share of the target segment" [ASSUMPTION].
  3. *Expand exit:* adjacency pull — e.g. "15% of ARR from expansion products, 3 adjacent integrations live" [ASSUMPTION].
- **Worked Example:** Netflix's stated vision in the Biddle era: Get big on DVDs (by mail), Lead downloading/streaming as bandwidth improves, Expand worldwide. Each phase's economics funded the next; worldwide expansion waited on the lead phase's cash engine.
- **Source URL:** [gibsonbiddle.medium.com/6-the-glee-model-6af740bdf3b1](https://gibsonbiddle.medium.com/6-the-glee-model-6af740bdf3b1) (Biddle).

## 4. The GEM Model & Sequencing

- **Definition:** Forces an explicit ranking of **G**rowth, **E**ngagement (retention), and **M**onetization. The ranking is context-dependent and shifts as the company matures (Biddle).
- **When to use:** Quarterly/annual planning to align product, marketing, finance, and engineering on one primary focus.
- **When NOT to use:** Prioritizing individual features; that is roadmap work, not strategy sequencing.
- **Default sequencing rule:** Engagement first for early-stage software (prove PMF — growing a leaky bucket burns acquisition spend), then Monetization (prove willingness to pay and unit economics), then Growth.
- **The monetization-first conflict:** Bootstrapped founders and premium B2B teams argue willingness to pay is the sharpest validator and the survival constraint. Decision criteria:
  - **Choose Engagement first (Biddle default) if:** VC-backed with runway, or consumer/network-effect product where scale drives value.
  - **Choose Monetization first if:** bootstrapped or low runway (cash is the constraint), or premium B2B/enterprise where willingness to pay is the primary signal of value.
  State the chosen rank in one line with justification; silent deviation from the default is an unanchored bet.
- **Worked Example:** Netflix in 2005 ranked Monetization first to prove profitability to Wall Street during Blockbuster's price war, mid-scale-up — context, not doctrine, set the rank (Biddle was in the room).
- **Source URL:** [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/) (Biddle's strategy series; GEM covered alongside DHM and GLEe).

## 5. Aggregation Theory

- **Definition:** In digital markets with near-zero marginal distribution costs, value accrues to firms that aggregate demand through superior user experience; supply becomes modularized and captured by the aggregator (Ben Thompson).
- **When to use:** Analyzing market structure, designing business models, evaluating competitive threats from digital giants.
- **When NOT to use:** User research or single-feature usability design. Prerequisite: digital market with near-zero marginal distribution and transaction costs.
- **Worked Example:** Google Search aggregates demand with the best index; because consumers search on Google, publishers must optimize for Google, which deepens Google's lead. The aggregator's power is on the demand side, not in supply contracts.
- **Source URL:** [stratechery.com/aggregation-theory](https://stratechery.com/aggregation-theory/) (Thompson).

## 6. Platform vs Product Strategy

- **Definition:** A **product** is a closed, end-to-end solution delivered directly to users; a **platform** is infrastructure on which third parties build their own products and businesses.
- **When to use:** Designing API/ecosystem strategy; deciding how to compete against a dominant aggregator.
- **When NOT to use:** Early MVP work before the core value proposition is proven — a platform with nothing worth building on is an empty mall.
- **Decision criteria:** Choose **platform** when third parties can build differentiated value on your infrastructure and you can win without owning the end-user relationship. Choose **product** when controlling the end-to-end experience is itself the moat.
- **Worked Example:** Shopify is a platform: checkout, inventory, and storefront APIs let merchants build independent brands; Shopify's revenue is a function of merchant success. Contrast a vertical retailer that owns the whole experience and the whole margin.
- **Source URL:** [stratechery.com/concepts](https://stratechery.com/concepts/) (Thompson's aggregation and platform concepts).

## 7. OKRs in Product Strategy

- **Definition:** Objectives (qualitative, directional) and Key Results (quantitative outcome metrics) map strategy onto empowered teams so direction is set without micro-management.
- **When to use:** Coordinating a product organization; translating the active GLEe horizon and GEM focus into team-level ownership.
- **When NOT to use:** As individual performance evaluation, or as a task checklist ("ship X" is an output, not a key result).
- **Rules:** Every key result has a baseline, a target, an anchor (telemetry baseline or `[ASSUMPTION]`), and a check date. 1-3 objectives per team per cycle, 2-5 key results each; more is theater.
- **Worked Example (illustrative):** A Spotify-style search team: Objective "make it effortless to find the music you want"; KR1 "reduce search-to-play time from 12s to 8s" [illustrative numbers — anchor to your telemetry]; KR2 "raise autocomplete click-through 15%" [ASSUMPTION]. The shape is the lesson: outcome metrics with baselines, not "ship better search".
- **Source URL:** [svpg.com/articles](https://svpg.com/articles/) (Cagan on objectives for empowered teams); rewrites and anchoring in [./okr-examples.md](./okr-examples.md).
