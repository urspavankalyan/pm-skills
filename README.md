# pm-skills — the Product Management Playbook for AI Agents

17 focused agent skills that cover the full PM lifecycle — strategy, discovery, specs, stories, prioritization, roadmaps, experiments, AI features, metrics, pricing, GTM, growth, team design, and failure analysis — in the open [Agent Skills](https://agentskills.io) / skills.sh format. Works with any skills-compatible agent: Claude Code, Cursor, Hermes, and more.

[![CI](https://github.com/urspavankalyan/pm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/urspavankalyan/pm-skills/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![skills.sh](https://skills.sh/b/urspavankalyan/pm-skills)](https://skills.sh/urspavankalyan/pm-skills)

## Start Here

| You're trying to... | Prompt your agent with | Skill that loads |
| :--- | :--- | :--- |
| Define who you win with and why | "Define our product strategy for a B2B invoicing tool" | `product-strategy` |
| Learn why users churn | "Build a churn interview guide, we have session telemetry" | `customer-discovery` |
| Write a PRD that survives scrutiny | "Write a PRD for calendar sync, 6-week appetite" | `prd-writing` |
| Rank a contested backlog | "Prioritize these 8 requests; sales wants 3 of them" | `prioritization` |
| Communicate the plan | "Turn our bets into a Now/Next/Later roadmap" | `roadmap-planning` |
| Diagnose a metric drop | "Activation fell 20% WoW, investigate" | `metrics-analysis` |
| Decide what to charge | "Design our pricing tiers and value metric" | `pricing-packaging` |
| Ship without chaos | "Plan the launch for our beta feature" | `gtm-launch` |
| Grow without leaking | "Design a growth loop for our referral flow" | `growth-loops` |
| Learn from your calls | "Run a decision-journal retro on last quarter" | `decision-journal` |
| Keep execs aligned | "Write this month's stakeholder update; we missed target" | `stakeholder-updates` |
| Fix a feature factory | "Our team ships features but outcomes never move" | `empowered-teams` |
| Decode PM jargon | "What does GEM mean in this strategy doc?" | `glossary` |
| Write stories that aren't tickets | "Break this bet into user stories for the cycle" | `user-stories` |
| Test before building | "Design a 1-week experiment for this assumption" | `experiment-design` |
| Spec an AI feature honestly | "PRD for AI summarization — we have no eval data" | `ai-product-prds` |
| Find failure before or after it costs you | "Pre-mortem this roadmap" / "postmortem the launch — what went wrong" | `failure-analysis` |

## The Skills

| Skill | What it does |
| :--- | :--- |
| `product-strategy` | ICP-first strategy with DHM moats, GLEe horizon exit criteria, GEM sequencing, OKRs |
| `customer-discovery` | Continuous discovery, Opportunity Solution Trees, Mom-Test interviewing, churn triangulation |
| `prd-writing` | Outcome briefs vs shaped pitches, context gate, evidence-weight rules, pushback protocol |
| `prioritization` | Evidence-cited ranking, RICE-vs-debate decision criteria, GEM alignment checks |
| `roadmap-planning` | Now/Next/Later horizons, hill charts, exec-safe uncertainty communication |
| `metrics-analysis` | Step-0 instrumentation checks before diagnosis, North Star design, cohort & funnel discipline |
| `pricing-packaging` | Value metrics, willingness-to-pay research, packaging, price-rise playbooks |
| `gtm-launch` | Positioning (Dunford), GTM motion selection, staged rollout gates |
| `growth-loops` | Loop taxonomy & mechanics, activation discipline, "no growth before retention" rule |
| `decision-journal` | Prediction logging with calibration retros; small-sample vs large-sample rules |
| `stakeholder-updates` | Outcome-based updates, health ratings, bad-news-early protocol |
| `empowered-teams` | Empowered vs feature teams, outcome charters, team-topology transitions |
| `glossary` | 34 canonical terms with owner attribution, usage-fork notes; refuses invented etymology |
| `user-stories` | JTBD job stories, story mapping, INVEST/Gherkin craft, splitting patterns, volume-demand pushback |
| `experiment-design` | Experiment menu with power/peeking discipline, one-day pretotypes, pre-registered briefs |
| `ai-product-prds` | Eval-first AI specs: golden datasets, hallucination tiers, cost gates, HITL & escalation design |
| `failure-analysis` | Klein pre-mortems, blameless Allspaw-style postmortems, kill retros; refuses blame documents and unfalsifiable lessons |

Every skill ships with `references/` (deep frameworks, each with Definition / When to use / When NOT to use / Worked Example / Source URL); skills whose workflow produces artifacts also ship `assets/` fill-in templates. All 17 are covered by scenario evals in `evals/`.

## This suite understands

An agent searching for skills — through the skills.sh index, `npx skills find`, or a plain web search — matches on these terms as much as on skill names; each links to the skill that owns it: ICP, moats, DHM, GLEe, GEM, OKRs (`product-strategy`); customer interviews, Mom Test, churn interviews, OST, JTBD, recruitment screener (`customer-discovery`); PRD, product brief, pitch, one-pager, spec, kill criteria (`prd-writing`); user stories, INVEST, Gherkin, story mapping, story splitting (`user-stories`); prioritize, RICE, ICE, T-shirt sizing, backlog, roadmap ranking (`prioritization`); roadmap, Now-Next-Later, horizons, hill charts, "when does it ship" (`roadmap-planning`); experiments, A/B test, fake door, pretotype, power, peeking, readout (`experiment-design`); AI feature specs, golden datasets, hallucination rates, evals, LLM cost gates (`ai-product-prds`); activation, retention, cohorts, funnels, North Star, AARRR, vanity metrics, tracking plans (`metrics-analysis`); pricing, value metric, willingness to pay, Van Westendorp, tiers, packaging, price increase (`pricing-packaging`); launch, positioning, PLG, sales-led, rollout, GTM (`gtm-launch`); growth loops, k-factor, virality, referrals, aha moment (`growth-loops`); pre-mortem, postmortem, root cause, five whys, blameless, kill retro (`failure-analysis`); stakeholder update, exec readout, board update, status report (`stakeholder-updates`); decision journal, calibration, predictions, retros (`decision-journal`); empowered teams, feature teams, charters, build trap (`empowered-teams`); any PM term or jargon, translations and forks (`glossary`).

## Install

```bash
# install everything or pick one skill (forkers substitute their handle)
npx skills add urspavankalyan/pm-skills
npx skills add urspavankalyan/pm-skills --skill prd-writing
```

## Your first ten minutes

No account, no key, no PM training required — the skills are the expertise. After the one install command above, you just chat normally:

1. *"Write a PRD for calendar sync — 7 churn interviews cite failed exports and telemetry shows 18% of actives hit them; 6-week appetite."* `prd-writing` loads, checks the evidence bar, picks Shape Up because the appetite is fixed, and ships a filled pitch with boundaries, no-gos, and kill criteria — then appends a dated prediction to `product/decisions.md` in your folder.
2. Next week, same folder: *"Activation fell 20% WoW — why?"* `metrics-analysis` reads your `product/` files first, quotes them in its header, and opens with the instrumentation checklist instead of a cause story.
3. *"Pre-mortem this roadmap before we commit."* `failure-analysis` assumes it already failed, reconstructs why, and hands back the top failure modes wired to kill criteria.

No maintenance: the behavioral difference appears in every PM-shaped answer from then on.

## Out of scope (for now)

pm-skills covers the judgment loop: strategy, discovery, specs, stories, prioritization, roadmaps, experiments, AI features, metrics, pricing, GTM, growth, retros. Deliberately out today: legal and compliance drafting (`ai-product-prds` scopes PII and liability inside AI specs, but no skill writes contracts or privacy policies); analytics instrumentation *build* — tracking plans ship as an asset of `metrics-analysis`, which audits instrumentation rather than operating it; standalone OKR writing (covered inside `product-strategy` and `empowered-teams` charters); sales-enablement collateral and churn winback campaigns (`gtm-launch` gates on sales readiness; `customer-discovery` runs churn interviews); AI evals operations such as drift monitoring and eval CI (`ai-product-prds` specs evals, not pipelines); TAM sizing, competitive-intel deep dives, and release notes. Each is a welcome skill if authored per `STYLE_GUIDE.md` with evals; until then no skill here pretends to cover it.

## See it say no

Skills are only as good as their worst compliant answer. Asked *"The CEO wants a PRD for an AI chatbot in our B2B analytics app. Write it today."* with no evidence supplied, `prd-writing` refuses to ship a full PRD and instead returns: the four unvalidated risks named specifically, a 1-week discovery plan with quantitative kill/fund thresholds (each anchored or `[ASSUMPTION]`-tagged), an `[EVIDENCE-FREE DRAFT]` of <= 10 lines, and the exact conditions under which building today *would* be right. Asked *"make our compliance software viral like Dropbox"*, `growth-loops` refuses virality (no natural sharing trigger in regulated data, low branching factor, saturation-capped k), fires the GEM retention gate, and offers the loops that fit instead. Full rubrics live in `evals/`.

## Shared workspace state

Across sessions, six skills read and write the same three files (schema in `docs/workspace-contract.md`): `product/strategy.md` (ICP, GEM rank, appetite — written by `product-strategy`, read by `prioritization`, `prd-writing` and `failure-analysis` with a >90-day staleness warning), `product/bets.md` (written by `prioritization`, grounds `roadmap-planning`'s Now column), and `product/decisions.md` (one canonical prediction-entry schema, written by `prd-writing`, resolved by `decision-journal` and `failure-analysis`). Each skill restates the schema inline, so every skill still works installed alone.

## Chained workflows

Skills load automatically from context; chain them by working the lifecycle:

1. **New bet:** `product-strategy` (ICP + GEM focus) → `customer-discovery` (OST + interviews) → `prd-writing` (outcome brief with kill criteria) → `decision-journal` (log the prediction).
2. **Quarterly reset:** `metrics-analysis` (cohort read) → `prioritization` (rank bets) → `roadmap-planning` (Now/Next/Later) → `stakeholder-updates` (communicate).
3. **Scale phase:** `metrics-analysis` (retention validated?) → `pricing-packaging` → `gtm-launch` → `growth-loops`.
4. **AI & experiment bets:** `experiment-design` (1-week tests) → `ai-product-prds` (eval-first spec) → `decision-journal` (log predictions, retro calibration).

## Why this beats a monolith

The classic shape of a PM skill repo is one monolithic file that triggers on everything and declares half the discipline out of scope upfront. This suite inverts that:

- **Focused skills, sharp triggers** — each skill owns one job, so the right expertise loads and nothing irrelevant does.
- **Coverage the monolith skipped** — pricing, GTM and growth loops are first-class skills, not future promises. What stays out is declared in the Out of scope section, so gaps are design, not oversight.
- **Self-contained installs** — every skill works alone; no sibling assumed.
- **Guardrails, not vibes** — context gates, evidence-weight rules, falsifiable kill criteria, and a license to say no to evidence-free requests.
- **Conflicts resolved, not blended** — Cagan vs Shape Up, RICE vs debate, GEM vs monetization-first: explicit decision criteria, never framework smoothies.
- **Tested** — `evals/` holds 70 adversarial scenario rubrics across the 17 skills; live hostile-test runs are logged in `docs/eval-results.md` as they execute; `scripts/validate_skills.py` lints the whole repo against the Agent Skills spec (CI on every push).

## Framework & source attribution

| Framework | Author / source |
| :--- | :--- |
| Outcome briefs, empowered teams, four risks | Marty Cagan — [svpg.com](https://svpg.com/articles/) |
| DHM, GLEe, GEM | Gibson Biddle — [gibsonbiddle.com](https://www.gibsonbiddle.com/) |
| Continuous Discovery, OSTs | Teresa Torres — [producttalk.org](https://www.producttalk.org/) |
| Shape Up (appetites, hill charts) | Ryan Singer — [basecamp.com/shapeup](https://basecamp.com/shapeup) |
| Mom Test interviewing | Rob Fitzpatrick — [momtestbook.com](https://www.momtestbook.com/) |
| Now/Next/Later roadmaps | Janna Bastow — Mind the Product |
| Prioritization-theater critique | Lenny Rachitsky; Janna Bastow (ProdPad) — [lennysnewsletter.com](https://www.lennysnewsletter.com/), [prodpad.com](https://www.prodpad.com) |
| Positioning | April Dunford — *Obviously Awesome* |
| Value metric & packaging | Ramanujam & Weisser — *Monetizing Innovation* |
| Growth loops & network effects | Andrew Chen / Reforge — [andrewchen.com](https://andrewchen.com/) |
| Aggregation Theory, platform strategy | Ben Thompson — [stratechery.com](https://stratechery.com/) |
| Pre-mortem / prospective hindsight | Gary Klein — [HBR](https://hbr.org/2007/09/performing-a-project-premortem) |
| Blameless postmortems | John Allspaw; Google SRE — [sre.google](https://sre.google/workbook/postmortem-analysis/) |

Frameworks are credited to their authors; this repo adds the operating rules, guardrails, templates, and evals that turn them into agent behavior.

## Contributing

Add or improve a skill by following `STYLE_GUIDE.md`, then run `python3 scripts/validate_skills.py` and ensure the new skill's evals pass. MIT license — see `LICENSE`.
