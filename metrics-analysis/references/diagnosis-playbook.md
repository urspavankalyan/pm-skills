# Metrics Diagnosis Playbook

Deep-dive reference for the metrics-analysis skill. Frameworks belong to their authors; sources repeat per framework.

## 1. Diagnostic Step-0: Instrumentation Check & Re-baselining

Before formulating any hypothesis about a metric movement ("activation dropped 15%"), sanity-check the telemetry pipeline.

- **Rule 1:** Never trust a metric change without checking the data pipeline.
- **Rule 2 (Re-baselining):** If an instrumentation bug is found, quantify the measurement error before acting:
  1. *Quantify the error:* error (rate points) ≈ baseline rate × affected traffic share × fraction of the comparison window the outage covered. If baseline activation is 60%, iOS is 66% of events, and an iOS release broke logging for a quarter of the week (0.25), the error ≈ 60 × 0.66 × 0.25 ≈ 10 percentage points of the reported drop.
  2. *Calculate the residual:* reported change minus measurement error (15% - 10% = 5% residual real drop).
  3. *Pivot decision:* residual ~0 → halt the investigation, fix tracking, re-baseline. Residual non-zero → proceed to shape analysis using only the residual.
- **Rule 3 (Decomposition & uncertainty):** state the quantification method explicitly (affected cohort counts vs pre-release baseline, or vs a stable control group) and acknowledge uncertainty (error bands, interaction effects). If the attribution changes between analyses (outage theory ruled out for a mix shift), document the transition with its evidence — never silently overwrite history.
- **Checklist:** 1. *Schema changes:* did event definitions or trigger points change in the code repository? 2. *Logging outage:* are events failing on specific platforms (did an app release break SDK initialization)? 3. *Telemetry latency:* replication or processing pipeline delays? 4. *Double logging:* frontend loops sending events twice? 5. *Deflation direction:* did a dedupe or backfill fix land, so the prior baseline was inflated and the "drop" is the correction taking effect?
- **Worked Example (illustrative numbers):** Reported activation drop 15%; an iOS release broke analytics init for roughly a quarter of the comparison window; iOS share 66%, baseline rate 60% → error ≈ 60 × 0.66 × 0.25 ≈ 10pp → residual ≈ 5pp. The product investigation targets a 5% change, not 15% — gradual-shape causes, not outage causes.
- **Source:** repo diagnostic method synthesized from standard analytics-engineering practice; no external author claimed.

## 2. Diagnostic Step-1: Shape Analysis

Plot the metric over time; the shape selects the cause family.

- **Step change (sudden drop/spike overnight):** technical deploy or outage, third-party API failure, marketing campaign launch/stop, seasonal holiday (e.g. Christmas Day), or tracking bug.
- **Gradual trend (slow decay/growth over weeks):** shifting cohort composition, acquisition mix shift (more low-intent paid traffic), slow competitive erosion, onboarding drift.
- **Rule:** match the investigation to the shape. Treating a gradual mix shift as an incident wastes the incident channel; treating an outage as drift delays the rollback.

## 3. Funnel Separation: AARRR (Dave McClure)

- **Definition:** A linear funnel mapping the user journey: Acquisition, Activation, Retention, Referral, Revenue.
- **When to use:** Localizing a metric movement to one stage; designing telemetry for a new product.
- **When NOT to use:** As a growth strategy by itself in loop-driven products (pair with growth loops, §6).
- **Hardening rule (funnel separation):** keep stages non-overlapping; one distinct telemetry event per stage. Treating "invited a colleague" as both activation and referral makes diagnostic analysis impossible.
  1. *Acquisition:* visitor lands and signs up — `event: signup`.
  2. *Activation:* first experience of core value inside a fixed window — `event: first_project_created` within 24h.
  3. *Retention:* continued active use over subsequent cycles — `event: session_start_week_2`.
  4. *Referral:* user invites others — `event: invite_sent`.
  5. *Revenue:* conversion to paid.
- **Worked Example:** A SaaS tool wires exactly those five hooks; a drop in `first_project_created` with stable `signup` isolates the problem to onboarding-to-value, not acquisition.
- **Origin:** Dave McClure, *Startup Metrics for Pirates* (AARRR coinage).
- **Source URL:** [mindtheproduct.com](https://www.mindtheproduct.com)

## 4. North Star Metric Selection

- **Definition:** The single metric that best captures the core value the product delivers to customers and drives long-term business growth; decomposed into input metrics teams can move.
- **When to use:** Setting product-level strategy and aligning multiple teams on one measurable definition of value.
- **When NOT to use:** Revenue, profit, or stock price as the North Star — lagging financial indicators, not value capture.
- **Worked Example:** Airbnb's North Star is Nights Booked, not revenue: it captures value for both guests and hosts and leads revenue. Pair it with input metrics (search-to-book conversion, listing response time) each team owns.
- **Source URL:** [lennysnewsletter.com](https://www.lennysnewsletter.com)

## 5. Input & Proxy Metrics (Gibson Biddle)

- **Definition:** A proxy metric is a measurable, short-term leading indicator a team can directly influence, correlated with a lagging business outcome (churn, LTV). Input metrics are the controllable components of the North Star.
- **When to use:** Giving teams actionable cycle-length targets that lead the lagging metric.
- **When NOT to use:** When the correlation to the lagging outcome has never been checked against cohort data — validate before targeting.
- **Worked Example:** Netflix. *Lagging:* monthly subscriber retention. *Hypothesis:* members who configure their queue early churn less. *Proxy:* share of members adding >= 3 titles to their queue in the first 30 days.
- **Source URL:** [gibsonbiddle.com](https://www.gibsonbiddle.com)

## 6. Growth Loops vs Funnels (Reforge)

- **Definition:** A closed system where one step's output is reinvested as the next cycle's input, compounding growth without proportional spend.
- **When to use:** Designing sustainable long-term acquisition/retention engines; evaluating whether growth is bought or compounded.
- **When NOT to use:** As a replacement for funnel diagnostics — loops are strategy, funnels are instrumentation.
- **Worked Example:** Pinterest's content loop: user searches and saves a pin (input/action) → search engines index public boards (output) → new users discover via search (reinvestment) → new signups save more pins.
- **Source URL:** [reforge.com/blog](https://reforge.com/blog/)

## 7. Retention Curves & Cohort Analysis (Reforge)

- **Definition:** Group users by signup cohort and plot the share returning at day/week/month X. A curve that flattens parallel to the x-axis indicates a stable retained segment — the primary quantitative signal of product-market fit.
- **When to use:** Measuring PMF, onboarding health, and long-term retention; adjudicating "retention is down" claims.
- **When NOT to use:** A single blended retention number across cohorts — mix shifts masquerade as product change; always split by cohort.
- **Worked Example:** A B2B notes app: weekly retention falls to 20% by week 4 but stays flat at 20% through week 12 → PMF for a 20% segment; the question becomes who the flat 20% are, not how to inflate the curve.
- **Source URL:** [reforge.com/blog](https://reforge.com/blog/)

## 8. Vanity-Metric Detection (Eric Ries)

- **Definition:** A metric that only goes up, lacks a denominator or cohort split, and therefore cannot falsify anything — cumulative signups, total downloads, hits, page views.
- **Detection checklist:** cumulative-only series; no denominator (rate) and no cohort dimension; moves with marketing spend but not with product changes; cannot name the decision it would change.
- **When to use the check:** Any dashboard review, success claim, or board metric proposal.
- **Rectification:** convert to a rate (per eligible session), split by cohort, and state the decision the metric licenses; if none, drop it from decision dashboards.
- **Worked Example:** "1M cumulative signups" is vanity; "week-1 activation rate by acquisition channel, cohort-split, vs last quarter's baseline" is a decision input.
- **Source URL:** [theleanstartup.com](https://theleanstartup.com)

## 9. Sources

- AARRR / funnel separation commentary: [mindtheproduct.com](https://www.mindtheproduct.com)
- North Star metric selection: Lenny Rachitsky — [lennysnewsletter.com](https://www.lennysnewsletter.com)
- Proxy metrics: Gibson Biddle — [gibsonbiddle.com](https://www.gibsonbiddle.com)
- Growth loops, cohort retention: Reforge — [reforge.com/blog](https://reforge.com/blog/)
- Vanity metrics: Eric Ries — [theleanstartup.com](https://theleanstartup.com)
