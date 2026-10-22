---
name: glossary
description: Decodes product-management jargon with author attribution and picks the canonical term when drafting. Use when the user asks what a PM term means, asks to decode jargon in a doc, transcript or meeting notes, asks to build or check a glossary, or is drafting a doc and must pick the canonical term instead of an ambiguous synonym. Every definition carries its author or school; when two schools use the same word differently the fork is surfaced, never picked silently; unknown terms get best-source attribution or a labeled stipulation, never invented etymology.
license: MIT
---

# PM Glossary

A vocabulary router: define single terms, decode jargon-dense documents, and pick canonical terms while drafting. Its contract is attribution — a term without an author is opinion, not terminology.

## 1. Core Principles

1. **Attribution over opinion** — every definition names its author or school; source URLs live in [./references/terms.md](./references/terms.md). Never present a borrowed framework or term as this repo's invention.
2. **Surface forks, never resolve silently** — when two schools use the same word differently (feature team, user story, commitment), present both meanings plus the disambiguation test. Silently picking one side is how two teams read one doc differently.
3. **One canonical term per concept when drafting** — pick the term, list synonyms once in a parenthetical, then never rotate. Synonym rotation reads as concept drift.
4. **Unknown terms are labeled, never invented** — if no sourced definition exists, say so. Best external source gets tagged `[NOT IN CANONICAL GLOSSARY]`; a pure guess gets tagged `[STIPULATED - NOT SOURCED]`. Invented attribution is fabrication.
5. **Terms are contracts** — calling a metric a North Star commits every team to it; calling a vanity metric a KPI commits the team to theater. When a term carries consequences, say what adopting it commits the team to.

## 2. Routing

Three modes by request shape. Run the matching workflow.

1. **Define** — "what does X mean?"
2. **Decode** — user pastes a doc, transcript, or meeting notes for a jargon sweep.
3. **Draft** — user is writing and needs the canonical term for a concept.

### Workflow

1. Normalize the term: lowercase, strip plurals, expand abbreviations against the aliases in [./references/terms.md](./references/terms.md).
2. Match found: return the entry's one-line definition plus its *Source/author* tail. If the entry carries a fork note, include both schools' meanings under `[USAGE FORK]`.
3. Ambiguous between two entries (e.g. "commitment"), or a compound of a canonical term plus an unrecognized modifier (e.g. "DHM moat"): present the canonical entry with its attribution and route the unrecognized half through the Unknown-Term Protocol (§3); ask at most one disambiguating question only if the surrounding context cannot resolve it.
4. No match: run the Unknown-Term Protocol (§3).
5. Decode mode: traverse the pasted text in order and emit `**term** — one-line decode` per hit. End with a Misuse Flags block for terms used against their school's meaning, or vanity metrics dressed as North Stars. Do not rewrite their document unless asked.
6. Draft mode: for each concept emit `canonical: X (avoid: y, z)`. Choose the vocabulary of the doc's declared operating model — empowered-team / outcome contract uses Cagan vocabulary; fixed-appetite shaped bets use Singer vocabulary. If the model is undeclared, state your choice in one line before the list.

## 3. Unknown-Term Protocol

1. State that the term is not in the canonical glossary.
2. If a real external source exists, give the best one-line definition with named author or field and source URL, tagged `[NOT IN CANONICAL GLOSSARY]`, and name the nearest canonical term.
3. If no source exists, offer a stipulative definition tagged `[STIPULATED - NOT SOURCED]` and ask where the user encountered the term.
4. Never invent an author, a year, or an etymology. Never present a guess as sourced.

## 4. Fork Table

When a term below appears, always show both sides and the disambiguation test.

| Term | School A | School B | Disambiguation test |
| :--- | :--- | :--- | :--- |
| Feature team | Scrum: the healthy cross-functional team that delivers end-to-end features (vs component teams) | Cagan / SVPG: pejorative — a team handed feature lists with no outcome accountability | Is the team accountable for an outcome, or for a list? |
| User story | Cohn: a placeholder for a conversation about value | Common Jira practice: a fixed mini-spec ticket | Does the card invite a conversation, or end one? |
| Commitment | Mom Test: the customer spends time, reputation, or money — evidence of demand | SAFe / Scrum: the team's pledge to a sprint or PI plan | Who commits — the customer (demand evidence) or the team (delivery promise)? |
| Proxy metric | Biddle: a deliberately chosen near-term stand-in for a long-term goal, correlation checked | Casual use: any conveniently available number, often vanity | Was the proxy chosen deliberately and is its correlation to the goal checked? |

## 5. Pushback / Guardrails

- Refuse to return an authoritative-sounding definition with no attribution; attach a source or the `[STIPULATED - NOT SOURCED]` tag.
- Refuse to silently pick one side of a §4 fork.
- If a decode surfaces a vanity metric proposed as a North Star or a target, flag it: the North Star must capture core value delivered to customers (Ellis), not an unsegmented cumulative count.
- Flag format: `[MISUSE: term — issue — canonical alternative]`.

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Unattributed authority | A definition delivered as fact with no author or school | Attach the source, or tag `[STIPULATED - NOT SOURCED]` |
| Silent fork resolution | One meaning of feature team / user story / commitment used without acknowledging the other | Print both meanings plus the disambiguation test (§4) |
| Synonym rotation | The same concept called "metric", "KPI", "North Star" across one doc | Pick one canonical term; list synonyms once |
| Vanity dressed as North Star | Cumulative signups or page views proposed as the North Star | Apply Ellis's test: does it express core value delivered? Else `[MISUSE]` flag |
| Invented etymology | Confident author or year for a term the agent cannot source | Delete or tag `[NOT IN CANONICAL GLOSSARY]` with a real source |

## 7. Files

- [./references/terms.md](./references/terms.md) — the canonical glossary (34 entries) with per-term attribution and a source-URL appendix. Load for any define, decode, or draft request.
