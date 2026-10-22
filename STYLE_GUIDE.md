# pm-skills — Authoring Style Guide

Quality contract for every skill in this repo. The validator (`scripts/validate_skills.py`) enforces the structural rules; the rules below are the craft rules a linter can't catch.

## Repo layout

```
pm-skills/
├── README.md                  # marketplace-style overview, install, skill table
├── LICENSE                    # MIT
├── STYLE_GUIDE.md             # this file
├── scripts/validate_skills.py # structural lint (run before every release)
├── evals/<skill-name>.md      # 3+ scenario prompts + expected-behavior rubrics per skill
├── docs/                      # workspace-state contract + live eval-results log
├── .github/                   # CI lint on every push + PR template
└── <skill-name>/              # one directory per skill; name == frontmatter name
    ├── SKILL.md               # required; <= 400 lines
    ├── references/*.md        # deep-dive knowledge, each <= 300 lines
    └── assets/*.md            # fill-in templates (fenced markdown inside)
```

Skills are installed INDIVIDUALLY (`npx skills add owner/repo --skill <name>`). Therefore every skill must be fully self-contained: never reference a sibling skill directory, never assume another skill is installed. Shared ideas get duplicated in condensed form, not linked.

## Frontmatter

```yaml
---
name: <skill-name>            # must equal directory name; kebab-case
description: <what it does, concretely>. Use when <trigger phrases mirroring how users actually ask>. <one clause on the differentiating guardrail>.
license: MIT
---
```

- Description formula: capability sentence (verbs + artifacts: "writes PRDs, one-pagers, pitches") + "Use when" list of real user utterances + differentiator. <= 1024 chars, no emoji.

## SKILL.md body

Structure (adapt per skill, keep the order):

1. `# Title` — one line, no emoji.
2. `## Core Principles` — 3–6 numbered principles, each with attribution `(Author / Source)` and a source URL in the matching reference file. Principles are rules an agent can violate, not platitudes. "Be helpful" is banned; "Ask about past behavior, never hypotheticals (Fitzpatrick / Mom Test)" is good.
3. `## Workflow` — numbered steps with ONE recommended default path. If alternatives exist, state the default first and give explicit deviation criteria ("Choose X instead if ...").
4. `## Pushback / Guardrails` (where relevant) — what the agent must refuse or flag, and the exact output format for doing so.
5. `## Anti-Patterns` — table: Anti-Pattern | How to detect | Rectification.
6. `## Files` — bullet list of relative markdown links (`[references/x.md](./references/x.md)`) with one-line "when to load" hints. Markdown links (not backticks) are mandatory for every relative reference inside skill directories — the validator resolves and verifies them, so a renamed file fails the build instead of shipping a dead path. Top-level docs are prose and may mention paths in backticks.

Hard rules:
- <= 400 lines. Depth goes to references; SKILL.md is the router + operating rules.
- No emoji in SKILL.md or references (README may use a few, sparingly).
- Every framework entry needs: Definition, When to use, When NOT to use, Worked Example (real company), Source URL. This five-part shape is the repo's credibility signature; keep it.
- Every quantitative threshold must state its anchor ("historical median CTR", "industry benchmark: X") or be labeled `[ASSUMPTION]` with a revisit trigger. Unanchored numbers are fabrication.
- Second person, imperative voice. No filler ("Great question", "It's important to note"). No restating the user's request.
- Templates live in `assets/` as fenced ```markdown blocks with `[Bracketed placeholders]` and `<!-- guidance comments -->`.
- Worked examples use real companies (Netflix, Shopify, Spotify...) or clearly-labeled hypotheticals ("Hypothetical: B2B invoicing startup").

## Evals

`evals/<skill-name>.md` per skill: at least 3 scenarios, each with:
- **Prompt** (a realistic user message, including at least one adversarial one: evidence-free demand, vague ask, conflicting evidence)
- **Expected behavior** (bullets: which gate fires, which file loads, what pushback looks like, what must NOT appear)

## Attribution

Frameworks belong to their authors. The README carries a Framework & Source Attribution Matrix; each reference file repeats source URLs per framework. Never present a borrowed framework as this repo's invention.
