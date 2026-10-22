# PM Glossary — Canonical Terms

Format: **Term** — one-line definition — *Source/author*. Forked terms carry a `[USAGE FORK]` clause. Source URLs in §Sources.

## Strategy & market

- **ICP (Ideal Customer Profile)** — the precise description of the customer who gets the most value from the product and from whom the business captures the most value; the filter every discovery, roadmap and GTM decision passes through. — *B2B GTM standard; Cagan's "target customer" (SVPG)*
- **PMF (Product/Market Fit)** — the condition where the market pulls the product: customers buy as fast as you can ship, usage grows without paid push, and retention stops decaying. — *Marc Andreessen (2007)*
- **DHM** — product strategy test: the product must increase Delight, be Hard-to-copy, and be Margin-enhancing; Netflix's three-lens check on any strategic bet. — *Gibson Biddle*
- **GLEe** — long-term vision test: Get big, Lead, Expand; Netflix got big on DVDs, led on downloading, then expanded internationally. — *Gibson Biddle*
- **GEM** — force-rank Growth, Engagement, Monetization, each with a proxy metric; the ranking is the company's active focus and flips with stage (Netflix ranked Monetization #1 in 2005, Growth #1 by 2008). — *Gibson Biddle*
- **JTBD (Jobs to Be Done)** — customers do not buy products, they hire them to make progress in a situation; the job, not the demographic segment, is the unit of demand. — *Clayton Christensen & Bob Moesta*
- **Atomic network** — the smallest network unit inside which the product already delivers value (Dropbox: one user and their synced files; Slack: one small team); the building block you seed before network effects compound. — *Andrew Chen, The Cold Start Problem*

## Metrics & growth

- **North Star metric** — the single metric that best captures the core value the product delivers to customers; every team's work should be able to move it. — *Sean Ellis / GrowthHackers*
- **Input metric (controllable input)** — a metric a team can directly move this quarter (e.g. share of orders shown a one-click promise), as opposed to output metrics like revenue; plans are written in inputs. — *Amazon "Working Backwards" (Bryar & Carr)*
- **Proxy metric** — a measurable near-term stand-in for a long-term or unmeasurable goal (DHM's delight proxied by retention); legitimate only while the proxy-goal correlation is deliberately checked. — *Analytics standard; Biddle pairs proxies with DHM*
- **Vanity metric** — a number that flatters but cannot guide action: unsegmented, cumulative, always rising; the antidote is cohort-split, actionable metrics. — *Eric Ries (Lean Startup); Croll & Yoskovitz (Lean Analytics)*
- **Retention curve** — the share of a cohort still active per period; a curve that flattens to a nonzero asymptote is the strongest graphical PMF signal, a curve that decays to zero means no amount of growth fixes the product. — *Reforge growth curriculum; standard growth practice*
- **Cohort** — a group of users sharing an event inside a window (e.g. signup week); cohorting holds acquisition quality constant so behavior change becomes visible. — *Analytics standard (Mode's SQL examples)*
- **AARRR** — Pirate Metrics skeleton for startup measurement: Acquisition, Activation, Retention, Revenue, Referral; a funnel to find the bottleneck, not a scoring formula. — *Dave McClure (500 Startups, 2007)*
- **k-factor (viral coefficient)** — average new users each existing user brings in; k > 1 means self-sustaining viral growth; borrowed from epidemiology's reproduction number. — *Epidemiology origin; growth standard (Reforge / GrowthHackers)*
- **Value metric** — the axis on which price scales (seats, events tracked, data volume); a good value metric rises with the value the customer receives, so price and value stay aligned. — *Price Intelligently / ProfitWell (Patrick Campbell)*

## Discovery & evidence

- **OST (Opportunity Solution Tree)** — desired outcome at the root, then customer opportunities (needs, pains, desires), then candidate solutions, then experiments; keeps the team moving outcome-to-evidence instead of idea-to-build. — *Teresa Torres, Continuous Discovery Habits (producttalk.org)*
- **Mom Test** — question discipline: ask about the other person's life and past behavior, not your idea, phrased so that even your mom cannot flatter you; compliments are noise. — *Rob Fitzpatrick, The Mom Test*
- **Commitment signal** — evidence a prospect is serious: they spend one of three currencies — time, reputation, or money (follow-up meeting, introduction, deposit); a meeting that ends with none of them failed, however warm it felt. — *Rob Fitzpatrick, The Mom Test (commitment & advancement)*
- **Fake door (painted-door test)** — presenting a feature that does not exist yet (button, landing page) and measuring click-through against an anchor before building; tests demand, not usability. — *Lean Startup standard; canonical early use: Buffer's landing-page MVP (Joel Gascoigne)*
- **Build Trap** — the organizational state of measuring success by output shipped instead of outcomes achieved; the escape is outcomes over outputs plus cadenced discovery. — *Melissa Perri, Escaping the Build Trap*
- **Golden dataset** — a curated set of real inputs paired with human-reviewed correct outputs or grading rubrics, held out from tuning and used as the fixed reference that gates AI-feature releases. — *ML/LLM eval standard (gold set / ground truth)*

## Shape Up — bets & shaping

- **Appetite** — the fixed time a bet is given (6-week big batch, 2-week small batch), chosen as a budget before shaping, not estimated after; scope flexes, time does not. — *Ryan Singer, Shape Up*
- **Breadboard** — a solution shaped as places, affordances, and the actions that wire them together, with no UI design; abstract enough to debate logic, concrete enough to build from. — *Ryan Singer, Shape Up*
- **Fat-marker sketch** — a marker-stroke-level drawing of the solution that shows boundaries and approach without specifying the pixels engineers should own. — *Ryan Singer, Shape Up*
- **Hill chart** — progress plotted on a hill: left of the peak is figuring-out (uncertainty), right is making-it-happen (execution); communicates uncertainty that percent-complete hides. — *Ryan Singer / Basecamp*
- **Circuit breaker** — the rule that a bet not finished by the end of its cycle stops; the cycle never silently extends, and the unfinished bet returns to the betting table. — *Ryan Singer, Shape Up*

## Teams & roadmaps

- **Empowered team** — a cross-functional team given a problem and outcome to own; it decides the solution and is accountable to the result, not to task completion. — *Marty Cagan, SVPG*
- **Feature team** — [USAGE FORK] Scrum: the healthy cross-functional team organized to deliver end-to-end features (opposite of component team). Cagan / SVPG: pejorative for a team handed feature lists with no outcome accountability. Disambiguate before use. — *Scrum standard vs Marty Cagan / SVPG*
- **Now/Next/Later** — a roadmap in three confidence horizons instead of dates: Now = actively building, Next = being validated, Later = strategic bets; communicates certainty, not deadlines. — *Janna Bastow & Simon Cast, ProdPad (2012)*
- **RICE** — prioritization score = (Reach x Impact x Confidence) / Effort on Intercom's fixed scales: Impact 0.25-3, Confidence 100/80/50%, Effort in person-months. — *Sean McBride, Intercom (2018)*

## Craft

- **INVEST** — good-story checklist: Independent, Negotiable, Valuable, Estimable, Small, Testable. — *Bill Wake (2003); disseminated via Mike Cohn, User Stories Applied*
- **User story** — [USAGE FORK] Cohn: a placeholder for a conversation about value, written on a card and finished in person. Common Jira practice: a fixed mini-spec ticket that ends the conversation. The fork is the whole game. — *Mike Cohn vs common Jira practice*
- **Kill criterion** — a threshold plus anchor plus revisit date agreed before a bet funds; missing it kills or explicitly re-bets the work, never silently extends it. — *Falsifiability standard; operationalized as Shape Up's circuit breaker (Singer)*

## Sources

- SVPG / Cagan (empowered teams, feature teams, ICP-as-target-customer): [svpg.com/articles](https://svpg.com/articles/)
- PMF: Marc Andreessen, "The PMA Guide to Startups, Part 8" — [pmarchive.com/guide_to_startups_part8.html](https://pmarchive.com/guide_to_startups_part8.html)
- DHM, GLEe, GEM, proxy metrics: Gibson Biddle — [gibsonbiddle.medium.com](https://gibsonbiddle.medium.com/) (GEM: [gibsonbiddle.medium.com/9-the-gem-model-65c89face5de](https://gibsonbiddle.medium.com/9-the-gem-model-65c89face5de))
- JTBD: Clayton Christensen Institute — [christenseninstitute.org/key-concepts/jobs-to-be-done](https://www.christenseninstitute.org/key-concepts/jobs-to-be-done/)
- Atomic network: Andrew Chen — [coldstartproblem.com](https://www.coldstartproblem.com/)
- North Star metric: Sean Ellis / GrowthHackers — [growthhackers.com](https://growthhackers.com/)
- Input metrics: Bryar & Carr, *Working Backwards* — [workingbackwards.com](https://www.workingbackwards.com/)
- Vanity metrics: Eric Ries — [theleanstartup.com](https://theleanstartup.com/); Croll & Yoskovitz, *Lean Analytics*
- Retention curves, k-factor: Reforge — [reforge.com](https://www.reforge.com/)
- Cohort analysis: Mode — [mode.com](https://mode.com/)
- AARRR: Dave McClure, "Startup Metrics for Pirates" — [500hats.typepad.com](https://500hats.typepad.com/)
- Value metric: ProfitWell / Price Intelligently — [profitwell.com](https://www.profitwell.com/)
- OST: Teresa Torres — [producttalk.org](https://www.producttalk.org/)
- Mom Test, commitment signal: Rob Fitzpatrick — [momtest.com](https://momtest.com/)
- Build Trap: Melissa Perri (O'Reilly) — [oreilly.com](https://www.oreilly.com/)
- Golden dataset: ML/LLM eval standard — [braintrust.dev/encyclopedia/golden-dataset](https://www.braintrust.dev/encyclopedia/golden-dataset), [langfuse.com/resources/engineering/golden-dataset-evaluation](https://langfuse.com/resources/engineering/golden-dataset-evaluation)
- Appetite, breadboard, fat-marker, hill chart, circuit breaker: Ryan Singer — [basecamp.com/shapeup](https://basecamp.com/shapeup)
- Now/Next/Later: Janna Bastow / ProdPad — [prodpad.com/blog/invented-now-next-later-roadmap](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)
- RICE: Sean McBride / Intercom — [intercom.com](https://www.intercom.com/)
- INVEST via Mike Cohn — [mountaingoatsoftware.com](https://www.mountaingoatsoftware.com/)
