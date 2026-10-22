# Growth Loops Reference

## 1. Loop Mechanics

**Definition.** A growth loop is a closed system where inputs, through some process, generate an output that can be reinvested as the next cycle's input (Balfour, Winters, Kwok, Chen / Reforge). Four parts: **input** (a cohort of users or a dollar) -> **action** (something meaningful done in the product) -> **output** (an asset: new leads, indexed content, margin, referrals) -> **reinvestment** (output feeds the next input without starting from zero).

**When to use.** As the unit of growth strategy: it answers "how does one cohort of users lead to the next?" and makes compounding visible. Use funnels only as the diagnostic tool for where a stage leaks.

**When NOT to use.** As decoration on a funnel deck — a diagram whose output does not measurably re-enter as input is a funnel with a circle drawn on it. Also not for one-off campaigns (a launch spike leaves no reinvestable output).

**Worked Example (real).** Pinterest, per Reforge: user signs up/returns -> activates on relevant content -> saves/repins, producing quality signals -> Pinterest distributes that content to search engines -> search users discover it and sign up (back to input). The content the action produces IS the acquisition asset.

**Source URL.** [Reforge: Growth Loops are the New Funnels](https://www.reforge.com/blog/growth-loops)

## 2. Loop Taxonomy

| Type | Mechanism | Real example (Reforge lineage) |
| :--- | :--- | :--- |
| Viral | Users expose or invite others; subtypes: word-of-mouth, organic, casual contact, incentivized | Dropbox (organic file-sharing + incentivized referrals); Loom (organic video links); Drift/Lime (casual contact); Uber/Airbnb (incentivized) |
| Content | User or company action creates content that search/distribution turns into acquisition | Yelp reviews indexed in search; the Pinterest loop above |
| Paid-reinvestment | Revenue margin funds more acquisition; efficiency compounds if payback holds | Headspace: trial revenue reinvested into ads that fund the next cohort |
| Product-integration | Product output lives inside other surfaces (links, embeds, marketplace apps), turning usage into distribution | Calendly scheduling links spreading through email; Notion's public template gallery; Slack/Zoom integrations exposing the platform in other tools' workflows |

Reforge additionally names a **sales loop** for B2B (closed revenue funds more sales capacity) — use it when ACV makes human motion the reinvestment vehicle.

**When each fits.** Viral: natural, frequent sharing triggers and a large target fraction in invitees' networks. Content: usage leaves public, indexable artifacts. Paid-reinvestment: proven retention and a payback period the runway survives. Product-integration: the product's output naturally travels outside the account.

**When NOT.** Viral without a natural trigger (outbound invites feel like spam); content loops based on user-generated artifacts in products whose output is private by nature (compliance, payroll) — company-authored content (benchmarks, templates, regulatory calendars) still fits such products and is the default there; paid loops before retention validates (GEM, §5).

**Source URLs.** [Reforge: Map your acquisition loops](https://www.reforge.com/guides/map-your-acquisition-loops) | [Reforge: Viral growth loops deep-dive](https://www.reforge.com/guides/go-deeper-on-viral-growth-loops)

## 3. Virality Coefficient k & Anchor Cautions

**Definition.** k (cohort K-factor) = invites sent per new user x invite-to-user conversion. k >= 1 means each cohort fully replaces itself and growth is self-sustaining; k < 1 means the viral loop boosts but does not carry growth.

**Anchor cautions (violating these produces fake virality):**
1. **Per cohort, always** — all-time cumulative k inflates as early adopters keep inviting; measure k per acquisition cohort and expect decay.
2. **Saturation caps** — k is bounded by the fraction of each user's network that is in-target and not already using the product; niche B2B targets a small slice, so organic viral k ceilings are low regardless of UI effort.
3. **k >= 1 is exceptional** — durable k above 1 is rare outside consumer network products; treat any internal target at or above 1 as `[ASSUMPTION]` needing cohort proof. Industry lore places strong consumer viral loops far below 1 (`[ASSUMPTION]` — no canonical published constant; recalibrate per cohort).
4. **Trigger frequency matters** — a one-time setup invite is a weaker loop than a repeated usage share (Quip comparison, Reforge).

**Worked Example (hypothetical).** Hypothetical: team wiki sends 2.0 invites per activated user, 12% convert -> cohort k = 0.24. That is a booster: every 100 acquired users yield 24 more. Scaling decisions must rest on the other loops; a plan that assumes k compounds to 1.0 in two quarters is fabrication unless cohorts show rising k.

**Source URL.** [Reforge: Map your acquisition loops (cohort K-factor)](https://www.reforge.com/guides/map-your-acquisition-loops)

## 4. Activation & Aha Discipline

**Definition.** An aha/activation metric is an early action that *causally* predicts retention in your product, found by cohort comparison and confirmed by intervention.

**The folklore record.** Facebook "7 friends in 10 days", Twitter "30 follows", Slack "2,000 messages" are rounded rallying cries — memorable averages, not scientific tipping points (Stancil / Mode; Geckoboard). They worked as focus devices *inside* those companies, after internal analysis; exported as universal thresholds they are correlation dressed as law.

**Method.** (1) Compare retained vs lost cohorts; rank candidate actions. (2) Intervene: nudge a randomized group toward the top candidate. (3) If retention lifts and the correlation holds, promote it; if not, the correlation broke — discard and repeat. Correlation that survives intervention is the only acceptable evidence.

**When to use.** Setting onboarding targets and activation rates. **When NOT to use.** Borrowing thresholds from talks or teardown threads; optimizing the proxy after the causal link breaks (Goodhart).

**Worked Example (real).** Facebook's number survived because Facebook tested interventions around friend-creation and watched retention move; companies that copied the number without the test bought folklore, not causation.

**Source URLs.** [Mode: Facebook's "Aha" Moment Was Simpler Than You Think](https://mode.com/blog/facebook-aha-moment-simpler-than-you-think/) | [Geckoboard: 7 friends in 10 days and correlation/causation](https://www.geckoboard.com/blog/how-facebooks-7-friends-in-10-days-got-everyone-confused-about-correlation-and-causation/)

## 5. The GEM Rule

**Definition.** GEM = Growth, Engagement, Monetization — the three pillars a product must keep in view (Gibson Biddle formalized the model from his Netflix practice; Nir Eyal's TechCrunch essay popularized the GEM name, relaying an unverified LinkedIn-origin story). The ranking is stage-dependent (early-stage default: Engagement → Monetization → Growth; bootstrapped or premium B2B may monetize first). The operating rule this skill enforces: engagement (retention) must flatten before growth scales — the engagement-to-growth gate holds under every ranking. "An amazing growth strategy using the latest viral hacks is pointless without a way to retain and profit from the growth."

**When to use.** Every scaling decision: paid spend, viral programs, launch volume. The gate artifact is the cohort retention curve, not total signups.

**When NOT to use (narrow).** Time-boxed network-effect land-grabs (winner-take-most markets) may spend ahead of global retention — but retention must hold within each atomic network (one campus, one city) before the next is opened (Chen / The Cold Start Problem). Global curve diving while atomic networks hold is a different diagnosis than a leaking product.

**Worked Example (real).** Biddle's Netflix per the GEM record: 2005 ranked Monetization first to prove profitability while retention held as the engagement proxy; by 2008, profitability proven, the rank flipped to Growth-first. Sequencing followed evidence, not doctrine; contrast the 2010s app-store graveyard of products that bought growth on diving retention curves.

**Source URLs.** [TechCrunch: 3 pillars of the most successful tech products (GEM)](https://techcrunch.com/2016/10/19/3-pillars-of-the-most-successful-tech-products/) | [Andrew Chen: The Cold Start Problem](https://andrewchen.com/) | [Reforge: Growth Loops](https://www.reforge.com/blog/growth-loops)

## 6. Sources

- Reforge (Balfour, Winters, Kwok, Chen) — [reforge.com/blog/growth-loops](https://www.reforge.com/blog/growth-loops), [reforge.com/guides/map-your-acquisition-loops](https://www.reforge.com/guides/map-your-acquisition-loops)
- Andrew Chen, *The Cold Start Problem* — [andrewchen.com](https://andrewchen.com/)
- Benn Stancil (Mode) — [mode.com/blog/facebook-aha-moment-simpler-than-you-think](https://mode.com/blog/facebook-aha-moment-simpler-than-you-think/)
- GEM framework — Gibson Biddle ([gibsonbiddle.medium.com/9-the-gem-model](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de)); popularization and the LinkedIn-origin rumor: [TechCrunch 2016, Nir Eyal](https://techcrunch.com/2016/10/19/3-pillars-of-the-most-successful-tech-products/)
