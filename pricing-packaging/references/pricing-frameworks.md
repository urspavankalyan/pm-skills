# Pricing Frameworks Reference

## 1. Value Metric

**Definition.** The unit a customer pays for, whose consumption grows as the customer extracts more value — the axis along which price scales (Ramanujam & Tacke's "pricing metric aligned to value"; Price Intelligently's "value metric"). A strong one is flexible with value, easy to understand, hard to game, and predictable enough to forecast.

**When to use.** Always — every pricing design starts by choosing or auditing the metric. Per-seat fits collaboration tools (value scales with team size); usage units (events, records, compute credits) fit infrastructure and data products; outcome units fit workflow automation.

**When NOT to use a usage metric.** When usage is invisible to the buyer's mental model (e.g. billing per API call to a business user), or when cost-to-serve is flat while usage spikes (abuse-prone metrics). Then fall back to seats or tiers with soft limits.

**Worked Example (real).** Snowflake charges compute credits: a customer running more queries consumes more credits, so revenue tracks value and expansion is automatic. Contrast a per-seat data platform whose revenue stays flat while the customer automates more workloads through fewer seats — the metric decoupled from value.

**Source URLs.** [monetizinginnovation.com](https://www.monetizinginnovation.com/) | [Simon-Kucher: Monetizing Innovation](https://www.simon-kucher.com/en/insights/monetizing-innovation) | [Stripe: SaaS pricing & packaging guide](https://stripe.com/resources/more/saas-pricing-and-packaging-strategy)

## 2. Willingness-to-Pay Research & Van Westendorp

**Definition.** Van Westendorp's Price Sensitivity Meter asks four open questions — at what price is this (1) a bargain, (2) cheap but good value, (3) getting expensive, (4) too expensive. Cumulative curves intersect at the point of marginal cheapness (PMC) and marginal expensiveness (PME), bounding the acceptable range, and at the indifference price point (IPP) and optimal price point (OPP), suggesting hero prices.

**When to use.** Single-product or single-tier pricing decisions where you need an acceptable range quickly; concept-stage price testing; sanity-checking a planned rise.

**When NOT to use.** Multi-attribute bundle design (use conjoint/choice-based trade-off analysis instead); samples under 100 per segment (intersections are noise); markets where respondents have no budget ownership (they answer fantasy prices).

**Sample-size cautions.** Common practitioner guidance is 200-300 completed responses per segment, with >= 100 as a bare minimum (survey-method vendor guidance: IntoTheMinds, SurveyKing). These are `[ASSUMPTION]`-grade anchors — vendor heuristics, not statistical law; recalibrate when segment variance is high. Never run one survey across segments and pool the curves.

**Worked Example (hypothetical).** Hypothetical: B2B invoicing startup surveys 240 ICP respondents. Curves yield an acceptable range of $39-$119/mo and OPP ~ $69. The hero tier is priced $69-$79, the entry tier inside PMC at $39, and a premium tier anchors at $119 with the killer feature fenced in.

**Source URLs.** [Wikipedia: Van Westendorp's Price Sensitivity Meter](https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter) | [Sawtooth Software: Van Westendorp PSM](https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter)

### 2b. The Four Willingness Profiles (pricing archetypes)

Ramanujam & Tacke segment buyers by needs + WTP into four archetypes; each implies different packaging:

| Profile | Behavior | Packaging implication |
| :--- | :--- | :--- |
| Value buyers | Know what they want and what it is worth; buy when price matches proven value | Transparent feature-to-value mapping; the hero middle tier lives here |
| Status buyers | Want the best; price is a quality signal | A premium tier with genuine exclusivity; never discount it |
| Convenience seekers | Pay to avoid shopping; default-driven | Make the middle tier the default; one-click annual upgrade |
| Budget buyers | Minimum needs, lowest price | Entry tier or self-serve; fence it so it cannot cannibalize the middle |

**When to use.** When designing tier content and fences; when a tier "sells but at the wrong ASP" (usually a profile mismatch). **When NOT to use.** As a substitute for survey data — the profiles interpret WTP data, they do not replace it.

**Worked Example (real).** Porsche (a Simon-Kucher case lineage): status buyers get the exclusive high line, value buyers the configurable core, budget-conscious buyers the entry model — distinct offers per profile, one brand.

**Source URL.** [monetizinginnovation.com](https://www.monetizinginnovation.com/)

## 3. Good-Better-Best Packaging

**Definition.** Three tiers straddling the WTP distribution: Good captures budget/entry demand, Better (the hero) captures value buyers at the OPP, Best anchors high and serves status buyers. Fences between tiers are value-metric limits and the killer feature; price gaps must be coherent enough that each segment self-selects. GBB dominates B2B packaging — 40.8% of B2B SaaS used it in Price Intelligently's 2023 state-of-pricing survey.

**When to use.** One dominant land-and-expand path, one core product line, segments that stratify by sophistication or volume.

**When NOT to use.** Multiple natural entry points or divergent sophistication directions (Simon-Kucher's Joshua Bloom: GBB "assumes one land-and-expand path" and breaks otherwise); then use use-case/persona packaging. Also not for portfolios where a two-package lineup reads cleaner.

**Worked Example (real).** Zoom: Basic (free) acquires, Pro is the hero for small teams, Business/Enterprise fence by host counts, SSO, and negotiated terms — each tier maps to a willingness profile.

**Source URLs.** [Price Intelligently / ProfitWell: State of B2B SaaS Pricing 2023](https://www.profitwell.com/) | [Monetizely on GBB with Simon-Kucher](https://www.getmonetizely.com/blogs/three-pricing-bigwigs-weigh-in-on-the-good-better-best-packaging-approach)

## 4. Monetization Sequencing

**Definition.** The order in which a product asks for money relative to proven engagement. Default: prove engagement (retention flattens, activation cohorts hold), then monetize. OpenView's PLG pillars phrase it "deliver value before capturing value."

**When to use (default).** Funded companies with self-serve motions: a paywall before validated engagement converts poorly and consumes the user's one chance to learn the value.

**When NOT to use (deviations).** (a) Bootstrapped — no capital funds free usage; charge early at a premium niche price. (b) B2B-premium — small reachable market, high ACV, procurement expects contracts; free tiers add little distribution. State the deviation explicitly.

**Worked Example (real).** Slack ran freemium for years, monetizing after daily-active engagement was proven; its 2020 reprice then moved billing to active usage. Conversely, bootstrapped niche compliance vendors charge from the first contract because runway, not distribution, is the constraint.

**Source URLs.** [OpenView: Pillars of PLG](https://openviewpartners.com/blog/pillars-of-plg-growth) | [OpenView: Product-Led Growth](https://openviewpartners.com/product-led-growth)

## 5. Price-Rise & Grandfathering Playbook

**Definition.** A sequenced procedure for raising prices while controlling churn and trust: justify with value added, size against the WTP corridor, choose a grandfathering policy, pre-agree a churn kill criterion, and measure expansion vs churn after.

**Steps.**

1. **Justify with value** — tie the rise to value-metric growth or shipped capability; value-added increases are accepted far more often than bare ones (Gartner 2021, via Monetizely).
2. **Size against the corridor** — rises inside ~10% of current price are usually absorbable; above that, expect active re-evaluation (`[ASSUMPTION]` — recalibrate to your churn baseline).
3. **Choose the grandfathering policy.** Small rise: existing customers migrate with 60-90 days notice. Structural rise or repackaging: grandfather 6-12 months (`[ASSUMPTION]`) with a sunset date and a migration incentive (extra months at the new tier). Eternal grandfathering is banned — it is permanent MRR erosion and a two-codebase billing system.
4. **Pre-agree the kill criterion** — e.g. logo churn in the 90 days post-notice <= trailing 90-day baseline + 2 pts (anchor: your own trailing churn telemetry); breach triggers a migration-offer revision, not silence.
5. **Clean shelfware** — retire entitlements nobody uses in the new packaging instead of carrying them forever.
6. **Read out at +2 quarters** — expansion MRR gained vs churn MRR lost; write the net number into the next pricing review.

**Worked Example (real).** Adobe moved perpetual Creative Suite to Creative Cloud subscription (2013): existing customers were not frozen on old licenses forever; they were migrated with discounted first-year membership — a forced-but-subsidized migration with a clear end state for the old price model.

**Source URLs.** [ProfitWell](https://www.profitwell.com/) | [Wingback: Grandfathering in SaaS](https://www.wingback.com/blog/everything-you-need-to-know-about-grandfathering-in-saas) | [Monetizely: Grandfathering strategies](https://www.getmonetizely.com/articles/grandfathering-strategies-managing-legacy-pricing-gracefully-in-the-saas-world)

## 6. Sources

- Ramanujam & Tacke, *Monetizing Innovation* — [monetizinginnovation.com](https://www.monetizinginnovation.com/), [Wiley](https://www.wiley.com/en-us/Monetizing+Innovation-p-9781119240860), [HBR: Your New Hit Product Might Be Underpriced](https://hbr.org/2016/05/your-new-hit-product-might-be-underpriced)
- Price Intelligently / ProfitWell (OpenView ecosystem) — [profitwell.com](https://www.profitwell.com/)
- OpenView PLG — [openviewpartners.com](https://openviewpartners.com/product-led-growth)
