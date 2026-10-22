# Contributing

One skill per PR. Quality bar:

1. **Read `STYLE_GUIDE.md` first.** It is the contract, and `scripts/validate_skills.py` enforces the structural half of it.
2. **Self-contained.** The skill must work when installed alone — no references to sibling skills.
3. **Grounded.** Every framework carries Definition / When to use / When NOT to use / Worked Example / Source URL, attributed to its author. Every quantitative threshold cites its anchor or is tagged `[ASSUMPTION]` with a revisit trigger.
4. **Tested.** Add `evals/<skill-name>.md` with at least 3 scenarios, including one adversarial prompt (evidence-free demand, vague ask, or conflicting evidence) and the exact expected behavior.
5. **Lint clean.** `python3 scripts/validate_skills.py` must exit 0 with no new warnings on your skill.

Good first contributions, in rough ROI order:

- Deep-dive references or assets inside existing skills (the recruitment screener, the tracking-plan taxonomy and the experiment readout protocol are examples of depth added inside existing skills rather than new directories).
- Pain-utterance clauses in skill descriptions, so triggers match how PMs actually phrase problems.
- Attribution upgrades: replace homepage URLs with stable deep links, verified live.
- New vertical skills when the `README` out-of-scope list still names them — e.g. sales-enablement briefings, release notes, TAM memos, competitive teardowns.

Two quality notes:

- **Evals are execution rubrics, not CI.** `scripts/validate_skills.py` lints structure only. When you change a skill's behavior, execute its `evals/` scenarios against a fresh agent and append the run to `docs/eval-results.md`. The PR template has a checkbox for this.
- **Guardrails travel with everything.** Any new pushback rule keeps the repo's shape: named assumptions, quantitative thresholds with anchors or `[ASSUMPTION]` tags, and a positive decision framework. MIT license — see `LICENSE`.

## Releasing

On every release: this repo ships from `urspavankalyan/pm-skills` (forkers point their README install block at their own handle); set or review GitHub topics (product-management, agent-skills, prd, roadmap, prioritization, product-discovery, ai-agents); add CI / license / skills.sh badges once the URLs exist; run `python3 scripts/validate_skills.py` until 0 warnings. Nothing ships with an unresolved relative link or an eval file that no longer matches its skill.
