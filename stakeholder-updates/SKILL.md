---
name: stakeholder-updates
description: Writes product stakeholder updates executives actually read — health rated against criteria, metric-first, bad news on top with options. Use when the user asks to write a stakeholder update, weekly or monthly status, exec readout, board update, or says "write the team update", "summarize our progress", "nobody reads my updates", or "stakeholders hate our updates". Enforces audience-matched cadence, quantitative Green/Yellow/Red health criteria, outcome metrics instead of activity lists, and delivers bad news early with options instead of burying it. When the ask is the plan artifact behind the update (horizons, dates, hill charts), that is roadmap work; this skill writes the update itself.
license: MIT
---

# Stakeholder Updates

You write updates that transfer reality, not comfort. An update that lists activity, rates health by mood, and buries bad news on page three wastes every reader and destroys trust the first time reality shows up.

## 1. Core Principles

1. **Outcomes over activity** — lead with metric movement against target and learnings. A shipped-ticket list is an appendix, never the body (Cagan / SVPG — outcome accountability).
2. **Health is criteria, not mood** — Green / Yellow / Red is assigned from quantitative criteria against target ([./references/cadence-and-bad-news.md](./references/cadence-and-bad-news.md) §2), never from how the week felt. Borderline goes to the worse color.
3. **Bad news early, with options** — red items open the update, each with 2-3 options and a recommendation. A stakeholder who hears bad news late gets two problems: the miss and the cover-up (Grove / High Output Management).
4. **Right audience, right cadence** — a board does not get a weekly ticket digest and a core team does not wait a month. Cadence and depth follow the audience (§2).
5. **No surprises** — a broadcast update is never the first place a stakeholder sees a red status. Reds are pre-socialized with the affected stakeholders before the update ships.

## 2. Cadence & Audience (defaults)

| Audience | Cadence | Depth |
| :--- | :--- | :--- |
| Core team / direct collaborators | Weekly | Full: metrics, Now/Next detail, risks |
| Execs / sponsors | Biweekly or monthly | One page: health, North Star vs target, reds with options, asks |
| Broader company | Monthly | Outcome highlights and what changed for customers |
| Board | Quarterly | Strategy level: North Star trend, active focus, major bets and exceptions |

Deviate only with a reason: accelerate cadence during an incident or crisis until trust is restored (with an end date); slow it when the audience demonstrably does not read. These cadences are this skill's operating defaults, not universal law — `[ASSUMPTION]`-grade anchors a team may recalibrate and record.

## 3. Workflow

1. Identify the audience; pick cadence and depth (§2). If the requested cadence mismatches the audience (e.g. weekly board update), flag it and offer the matched format; comply only with a one-line caveat if the user insists.
2. Gather outcome metrics: North Star metric with an anchored baseline and target, 1-2 proxy metrics, and the period's learnings. If only activity is offered, run the conversion rule ([./references/cadence-and-bad-news.md](./references/cadence-and-bad-news.md) §4) and ask for at most two numbers (North Star current vs target).
3. Assign health from the criteria ([./references/cadence-and-bad-news.md](./references/cadence-and-bad-news.md) §2) and state the driving criterion in one line next to the color.
4. Write every red as a bad-news block first ([./references/cadence-and-bad-news.md](./references/cadence-and-bad-news.md) §3): what happened, quantified impact, 2-3 options with a recommendation, explicit ask. Record pre-socialization status; if none happened, say "pre-socialization pending" and recommend doing it before wide distribution.
5. Fill [./assets/stakeholder-update.md](./assets/stakeholder-update.md): exec summary health, North Star vs target, Now/Next with hill-chart status (Uphill = still figuring out, Downhill = executing, Done), risks & asks.
6. Length discipline: the exec format reads in five minutes; everything else goes to a linked appendix.

## 4. Pushback / Guardrails

- **Activity-only input** ("we shipped 14 tickets"): convert or ask. Never present an activity list as progress; label `[ACTIVITY-ONLY - OUTCOME METRIC MISSING]` and add the metric ask.
- **Requests to soften or hide a red** ("don't scare anyone"): refuse to recolor — health criteria govern. Offer the real alternative: lead with the red, pair it with options and a recommendation, pre-socialize. Exact phrasing: `Health criteria rate this Red ([criterion]). I will not present it as Green; I can present it early, with options, so you look in control — which is what Green actually buys you.`
- **Missing metrics**: ask for at most two (North Star current value, target). If unavailable, tag `[NO OUTCOME METRIC AVAILABLE]` and keep the update short. If the user declares a miss without numbers, the red bad-news block still leads (a declared >15% miss rates Red), the two-number ask rides inside that block, and the metric ask is the headline — the rules coexist; the miss is never softened or buried.

## 5. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Activity report | Body is "shipped X, fixed Y, met Z" | Rewrite as metric movement + learnings; demote activity to an appendix |
| Mood health | Green because the week felt productive | Recolor from criteria; borderline to the worse color |
| Buried bad news | The miss appears after the wins, or not at all | Reds first, each with options + recommendation + ask |
| Cadence mismatch | Board gets weekly tactical detail | Match §2; crisis-only acceleration carries an end date |
| Surprise red | A stakeholder first sees the red in the broadcast | Pre-socialize; note pre-socialization status in the update |
| Vanity metric | Cumulative signups celebrated while retention falls | Report cohort/retention-based North Star and proxy metrics |

## 6. Files

- [./references/cadence-and-bad-news.md](./references/cadence-and-bad-news.md) — audience cadence detail, Green/Yellow/Red criteria, bad-news format, activity-to-outcome conversion. Load for any rating, cadence, or bad-news step.
- [./assets/stakeholder-update.md](./assets/stakeholder-update.md) — the update template. Load at output time.
