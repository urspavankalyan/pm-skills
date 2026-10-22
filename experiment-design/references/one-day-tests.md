# One-Day Tests & Pretotypes

When demand itself is untested, a weeks-long experiment is the wrong first move. This file compresses testing the riskiest assumption into hours or days: Torres on which assumption to test and how fast; Savoia on staging it with near-zero investment.

## 1. Torres: Assumption-First Testing

- **Decompose, then test** — every idea rests on five assumption types: desirability, usability, feasibility, viability, ethical (Torres / Continuous Discovery Habits, ch. 9). Test assumptions, not whole ideas; a failed idea post-mortem is almost always one untested assumption.
- **Map, then pick the leap-of-faith** — plot assumptions on importance x evidence; test the top-right quadrant (most important, weakest evidence) first (Torres / assumption mapping).
- **Speed rule** — an assumption test is designed and concluded inside the weekly discovery cadence: days, not sprints; as fast as possible while still producing trustworthy evidence (Torres / producttalk.org).
- **Behavior, not opinion** — a test must produce behavior (click, use, pay, return) or observed struggle. "Would you use this?" surveys are not tests.
- **Cadence** — at least one assumption test concluded per week, alongside continuous interviews (Torres).

## 2. Savoia: The Pretotype Contract

- A **pretotype** answers "should we build it?"; a prototype answers "can we build it?" (Savoia / pretotyping.org).
- **Market engagement hypothesis** — state it before running as "X% of Y will do Z"; the number and its anchor are the contract (Savoia / methodology).
- **Think global, test local** — run in one place, one channel, one day; widen ("hypozoom") only after the hypothesis holds locally (Savoia).

## 3. The One-Day Menu

### X-vertisement (Ad-Driven Fake Door)

- **Definition** — an advertisement for a product or feature that does not exist, driving to a one-page site with an intent CTA; measures initial level of interest from real traffic. Savoia's ad-coupled Fake Door pattern (the $50 ad + landing page for the not-written squirrel book in Pretotype It); the "X-vertisement" name is his talk-line for the same move.
- **When to use** — no existing audience; demand/positioning evidence needed for a new product; value propositions comparable as ad variants.
- **When NOT to use** — brand risk from advertising a non-existent product is unacceptable; or channel baselines are unknown and unbudgeted (you would be reading noise).
- **Sizing caution** — budget from the channel CTR anchor: B2B social ~0.5-2% CTR [ASSUMPTION without your own campaign baseline]; $50-100 buys a first interest read on cheap channels (Savoia's worked budget). Threshold example: signup rate of ad visitors >= 2x your median landing-page rate [ASSUMPTION anchor if no median exists].
- **Worked example** — Unwind Media ran small ad campaigns for candidate games into notify-me pages; CTR and signup ranking set build priority within days (Zapier / painted-door roundup). Savoia's own pattern: ad + landing page before writing the book (pretotyping.org).
- **Sources** — [pretotyping.org](https://www.pretotyping.org); [zapier.com/blog/painted-door-test](https://zapier.com/blog/painted-door-test/).

### Walkthrough (Human-Delivered) Pretotype

- **Definition** — a founder or staffer walks a real customer through the simulated service step by step, by hand, on the customer's own data — the human stands in for the product (Mechanical Turk/concierge family: Savoia; Ries).
- **When to use** — the job and the workflow are the unknowns; high-touch B2B or service ideas; you need struggle evidence, not click counts.
- **When NOT to use** — scale questions; or when hand-delivery hides a cost structure you actually need to learn (pair it with a cost model).
- **Sizing caution** — 5-10 walkthroughs per segment [ASSUMPTION]; pre-register what counts as pull: asked to keep it, offered to pay, referred a peer.
- **Worked example** — early Zappos was effectively a per-order walkthrough of buying shoes online, executed by hand (Ries); IBM's hidden typist walked users through "speech recognition" (Savoia).
- **Sources** — theleanstartup.com; pretotyping.org.

### Fake Door (In-Product, Same-Day)

- **Definition** — entry point to a non-existent feature behind a flag in a live product; honest waitlist screen on click. Full shape and Nubank worked example: [./experiment-menu.md](./experiment-menu.md) §1.
- **When to use** — existing product traffic and a same-day answer on interest/salience.
- **When NOT to use** — trust-sensitive flows; willingness-to-pay claims.
- **Sizing caution** — read clicks with a binomial CI (~300 exposures at 8% => +/-3.1pt); per segment if read per segment.
- **Sources** — pretotyping.org; amandaelyss.com/experimentation-at-nubank.

### Pinocchio / Video Pretotype

- **Definition** — a dummy artifact or demo video simulating the experience: Jeff Hawkins' wooden Palm Pilot block, Dropbox's demo video, Google Glass' "through the glasses" video (Savoia; Ries).
- **When to use** — form factor or vision is the risk; you need "would I carry/use/want this" evidence cheaply.
- **When NOT to use** — as behavioral evidence at scale; wonder is not retention.
- **Sizing caution** — 5 moderated reactions per segment [NN/g anchor]; count what they do after (sign up, pre-order), not applause.
- **Sources** — pretotyping.org; theleanstartup.com; nngroup.com.

## 4. Scoring & Decisions

- Pre-run: write "X% of Y do Z" + anchor + run date. Every number without a historical anchor is `[ASSUMPTION]` with a revisit trigger.
- Decision rule template: at or above threshold -> fund the next, bigger test (not a full build); between kill and fund -> refine and re-test once; below kill line -> kill and log the learning.
- One-day evidence feeds the experiment brief's hypothesis and baseline; it never replaces a sized test when traffic allows one.

## 5. Sources

- Torres — Continuous Discovery Habits: [producttalk.org](https://www.producttalk.org)
- Savoia — Pretotype It / The Right It: [pretotyping.org](https://www.pretotyping.org)
- Ries — The Lean Startup: [theleanstartup.com](https://theleanstartup.com)
- Nielsen Norman Group: [nngroup.com](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- Zapier painted-door roundup: [zapier.com/blog/painted-door-test](https://zapier.com/blog/painted-door-test/)
- Nubank case: [amandaelyss.com](https://www.amandaelyss.com/experimentation-at-nubank)
