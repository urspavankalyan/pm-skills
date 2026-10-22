# Experiment Menu & Statistical Guardrails

Pick the cheapest instrument that answers the question. Every method entry carries the five-part shape: definition, when to use, when NOT to use, sizing caution, worked example, source.

## 0. Selector

| Question | Default method | Evidence you get |
| :--- | :--- | :--- |
| Do users of an existing product want this feature? | Fake door | Revealed interest (clicks) in-product |
| Will a new product/positioning attract intent? | Landing page | Ad-driven visits -> signups |
| What job does it do; will the workflow accept it? | Concierge | Deep behavioral evidence, tiny n |
| Can users understand and use it? | Prototype | Task success in moderated sessions |
| What is the causal effect of a change to an existing flow? | A/B | Unbiased effect estimate + CI |

## 1. Fake-Door Test

- **Definition** — an entry point (button, card, menu item) for a feature that does not exist; clickers see an honest "not here yet — join the waitlist" screen. Measures revealed interest inside a live product (Savoia / Fake Door pretotype).
- **When to use** — existing traffic; the question is interest/salience; the entry point can be shown without burning trust; clickers can be followed up qualitatively.
- **When NOT to use** — the click itself burns trust (payments, medical, compliance flows); or the decision needs willingness-to-pay (a click is not money — add a commitment step or relabel).
- **Sizing caution** — read the interest rate with a binomial CI. ~300 exposures at a true rate of 8% give a 95% CI of about +/-3.1pt; 100 exposures widen it to +/-5.3pt. If you will read a segment, size the segment, not the whole. Recompute for your rate; these margins are arithmetic, not folklore.
- **Worked example** — Nubank painted a "pay boleto with credit card" door into the payment flow of a 120k-user rollout: 77k reached the screen, 9.7k clicked, 3.6k joined the waitlist; follow-up interviews re-aimed the value proposition at spend-concentrators (Elyss / Experimentation at Nubank).
- **Sources** — [pretotyping.org](https://www.pretotyping.org/) (Savoia, Fake Door); [amandaelyss.com/experimentation-at-nubank](https://www.amandaelyss.com/experimentation-at-nubank).

## 2. Concierge (Mechanical Turk)

- **Definition** — deliver the service by hand to a handful of customers — humans standing in for the unbuilt machine — to learn the job, the workflow, and willingness to pay (Savoia / Mechanical Turk; Ries / concierge).
- **When to use** — problem/solution fit is unvalidated; learning-per-customer is high; manual delivery is feasible for dozens of users.
- **When NOT to use** — to validate scale economics or unit costs at volume; after fit is already established.
- **Sizing caution** — n = 5-10 deep engagements per segment for saturation-aware qualitative signal [ASSUMPTION: repo default; revisit against your interview log]. Count behavioral evidence — repeat usage, money, referrals — not satisfaction claims.
- **Worked example** — Zappos: Nick Swinmurn photographed shoes in local stores, listed them, and bought and shipped each sold pair by hand to test whether people would buy shoes online (Ries / The Lean Startup). IBM simulated speech recognition with a hidden typist to test whether people would talk to a machine (Savoia).
- **Sources** — [theleanstartup.com](https://theleanstartup.com); [pretotyping.org](https://www.pretotyping.org/).

## 3. Prototype (Click-through, Video, Pinocchio)

- **Definition** — a non-production artifact — click-through, demo video, wooden block — that tests comprehension and usability before engineering spend (Savoia / Pinocchio; Ries / video MVP).
- **When to use** — the risk is "will they understand and use it"; you need task-level evidence before build costs.
- **When NOT to use** — as evidence of real-world behavior; stated intent in a demo is not revealed behavior.
- **Sizing caution** — 5 moderated sessions per variant surface ~85% of usability problems (Nielsen / NN/g); add 5 per additional segment you must read. Anchor: [nngroup.com 5-user rule](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/).
- **Worked example** — Dropbox validated demand with a three-minute demo video that grew the beta waitlist from ~5,000 to 75,000 overnight (Ries / The Lean Startup).
- **Sources** — nngroup.com; theleanstartup.com; pretotyping.org.

## 4. Landing-Page Test

- **Definition** — a standalone page describing a not-yet-existing product, fed real ad traffic, with a CTA (email, notify-me, pre-order) that measures acquisition intent and positioning (Savoia / ad-coupled Fake Door, the "X-vertisement" pattern; see [./one-day-tests.md](./one-day-tests.md)).
- **When to use** — no existing audience; the question is demand/positioning for a new product; value propositions are comparable variants.
- **When NOT to use** — when the team will read email capture as payment; add a commitment step (preorder deposit) if the decision needs money evidence.
- **Sizing caution** — ~400 visitors per variant at a 20% signup rate give a +/-3.9pt margin; at a 2% ad CTR that costs ~20k impressions per variant — compute before spending. B2B social CTR anchor ~0.5-2% ([SameLogic LinkedIn runs](https://samelogic.com/blog/fake-door-testing-our-figma-integration-using-linkedin/)); tag `[ASSUMPTION]` without your own campaign baseline.
- **Worked example** — Buffer validated in stages: page 1 measured signup intent from a tweet; page 2 added pricing to test willingness to pay; only then was code written (Gascoigne / [buffer.com/resources](https://buffer.com/resources/idea-to-paying-customers-in-7-weeks-how-we-did-it/)).
- **Sources** — buffer.com/resources; pretotyping.org.

## 5. A/B Test (Online Controlled Experiment)

- **Definition** — users randomized to control/treatment; the between-group difference in a metric is the causal effect of the change (Kohavi et al.).
- **When to use** — an existing flow with baseline behavior; enough traffic per cohort (§6); the decision scales with effect size.
- **When NOT to use** — brand-new value questions with no baseline behavior; small traffic (§10); one-off strategic calls.
- **Sizing caution** — per-cohort power math, worked in §6. Expect a humbling base rate: roughly one-third of ideas tested at Microsoft improved their target metric (Kohavi et al.) — budget for mostly null results.
- **Worked example** — Bing/Microsoft's experimentation program: durable revenue came from a minority of tests; OEC and guardrail discipline made the wins trustworthy (Kohavi et al. / KDD papers).
- **Sources** — [exp-platform.com](https://www.exp-platform.com); [KDD 2013 paper](https://dl.acm.org/doi/10.1145/2487575.2488217).

## 6. Per-Cohort Sizing (Not Folklore)

For proportions, per arm: n = (1.96 + 0.84)^2 * (p1(1-p1) + p2(1-p2)) / (p2 - p1)^2, i.e. 7.84 * (p1q1 + p2q2) / delta^2 at alpha = 0.05 (two-sided), power = 0.80. Worked: baseline 10%, MDE +2pt absolute -> 7.84 * (0.090 + 0.106) / 0.0004 ~= 3,840 per arm, ~7.7k total. At 2,000 conversions/week that is ~4 weeks; at 200/week it is ~38 weeks — infeasible (§10).

Rules:

1. **Read per cohort -> size per cohort** (country, platform, new vs returning). Aggregate n does not power a segment read; an underpowered segment read is how false negatives ship.
2. **MDE = smallest effect worth shipping**, anchored to amortized engineering cost or a guardrail floor. Never set MDE to "what traffic allows"; that inverts the instrument.
3. **Duration >= one full weekly cycle**, commonly 2-4 weeks [ASSUMPTION: 4-week cap; revisit for seasonality]; always complete full weeks to absorb weekday effects.
4. **If the math exceeds the cap -> §10**, no exceptions.

## 7. The Peeking Problem & Pre-Registered Stopping Rules

- **The problem** — data arrives sequentially; checking "is it significant?" every day violates the one-look assumption. Microsoft's measurement: five treatments raise a nominal 2.5% false-positive rate to ~12%; six iterations of such experiments give >50% chance of at least one false win (Kohavi et al. / KDD 2013).
- **Pre-register before launch**: primary metric, alpha, sample or date horizon, and an interim policy. The interim policy is either "no look until horizon" or a sequential method — always-valid confidence intervals / alpha spending (Johari, Koomen, Pekelis & Walsh / [arXiv:1512.04922](https://arxiv.org/abs/1512.04922)).
- **Stopping for harm** is always allowed if the guardrail boundary is pre-registered (e.g. stop when revenue/user falls >X% with the CI below zero at any interim).
- "Significant on day 3" without a registered sequential rule is not a result. Pushback format lives in SKILL.md §5.

## 8. Guardrail Metrics

- **Definition** — metrics that must not degrade for a win to count: revenue per user, latency, crashes, support contacts, unsubscribes, downstream activation (Kohavi et al. / OEC + guardrails).
- **Rule** — every brief names at least one guardrail with a veto threshold; primary up + guardrail down = do not ship, investigate.
- **Worked example** — a checkout change lifts conversion but raises support contacts per order past the anchored floor: hold. The overall evaluation criterion should fold in long-term value, not just the click (Kohavi et al.).
- **Sources** — exp-platform.com; the KDD papers cited below.

## 9. Novelty & Primacy Effects

- **Novelty** — a new UI draws attention and produces a temporary bump that fades as habituation sets in. Detection: slice the effect by weeks-since-exposure; a decaying curve is novelty, not value (Kohavi et al.).
- **Primacy** — users habituated to the old flow resist at first; the treatment reads worse early and recovers. Detection: the same slice, curve inverted.
- **Rule** — run >= 2 full weeks (commonly 4 [ASSUMPTION anchor; revisit per surface]) before reading; never declare a UI winner from week 1.
- **Sources** — Kohavi et al. / exp-platform.com.

## 10. When NOT to A/B

1. Required n per cohort > four weekly cycles of available traffic -> qualitative + directional read (SKILL.md §4).
2. No baseline behavior exists (new feature, new product) -> fake door / landing page / concierge first.
3. The decision is binary and strategic (enter a market, kill a line) -> evidence portfolio, not one p-value.
4. Asymmetric cost of being wrong (safety, compliance) -> guardrail/veto design, not optimization.

The small-traffic deliverable is a `[DIRECTIONAL READ]`: point estimate + CI + converging qualitative evidence + a labeled decision rule. Never a p-value.

## 11. Reading Out Results

A readout that overclaims converts one experiment into a year of bad decisions. Report in this order:

1. **The pre-registered verdict first** — the pass/fail threshold decided in [../assets/experiment-brief.md](../assets/experiment-brief.md), then the observed value against it. No post-hoc threshold moves; a moved threshold is a new experiment.
2. **Interval, not point** — report the effect with its confidence interval (or paired Bayesian credible range); a point estimate without spread is a rumor. If the test ran underpowered on purpose, header the readout `[DIRECTIONAL READ - UNDERPOWERED]` and say what it licenses (a follow-on test or qualitative deep-dive, not a ship decision).
3. **Guardrails table** — every pre-registered guardrail metric with its observed value; a win with a breached guardrail is not a win.
4. **Segment caution** — segment readouts multiply false positives; only read segments that were pre-registered, and label exploratory segments as hypothesis-generating.
5. **Novelty and primacy windows** — for UI or flow changes, compare the second full cycle after launch against the first; a first-week lift that decays is novelty, not value.
6. **Peeking confession** — if anyone looked early and the stopping rule was not followed, say so and downgrade the result to directional.

Record the verdict in the decision journal with the confidence and the kill criterion from the brief.

## 12. Sources

- Kohavi, Tang & Xu — Trustworthy Online Controlled Experiments (Cambridge, 2020); [exp-platform.com](https://www.exp-platform.com)
- Kohavi et al. — Online Controlled Experiments at Large Scale (KDD 2013): [dl.acm.org/doi/10.1145/2487575.2488217](https://dl.acm.org/doi/10.1145/2487575.2488217)
- Kohavi & Chen — False Positives in A/B Tests (KDD 2024): [dl.acm.org/doi/10.1145/3637528.3671631](https://dl.acm.org/doi/10.1145/3637528.3671631)
- Johari et al. — Always Valid Inference: [arxiv.org/abs/1512.04922](https://arxiv.org/abs/1512.04922)
- Torres — Continuous Discovery Habits: [producttalk.org](https://www.producttalk.org)
- Savoia — Pretotype It / The Right It: [pretotyping.org](https://www.pretotyping.org)
- Ries — The Lean Startup: [theleanstartup.com](https://theleanstartup.com)
- Nielsen Norman Group — testing with 5 users: [nngroup.com](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- Nubank fake-door case: [amandaelyss.com](https://www.amandaelyss.com/experimentation-at-nubank)
- Buffer landing-page case: [buffer.com/resources](https://buffer.com/resources/idea-to-paying-customers-in-7-weeks-how-we-did-it/)
