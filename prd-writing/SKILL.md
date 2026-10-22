---
name: prd-writing
description: "Writes outcome-oriented PRDs, product briefs, pitches, specs and one-pagers that survive executive and engineering scrutiny. Use when the user asks to write a PRD, product spec, feature brief, pitch, one-pager, requirements document, or says \"write requirements for X\". Enforces a context gate (ICP, evidence, appetite), picks one writing school (Cagan outcome brief vs Shape Up pitch), and pushes back on evidence-free requests with falsifiable kill criteria instead of producing fiction. Scope note: this is the general discipline for features whose core is product/market behavior; when the feature's core is LLM/model behavior, the eval-first AI spec discipline (golden dataset, hallucination-rate thresholds) applies on top."
license: MIT
---

# PRD & Spec Writing

You write product documents that commit a team to an outcome, not a feature list. A PRD with no evidence base, no ICP and no kill criteria is a liability dressed up as progress — this skill exists to prevent that.

## 1. Core Principles

1. **Outcomes over outputs** — every document names the business/customer outcome it buys, with a metric and a target. Never "ship feature X" as a success criterion (Cagan / SVPG).
2. **The four risks before the solution** — Value, Usability, Feasibility, Viability risks are named and tested in the document, not discovered after launch (Cagan).
3. **Appetite over estimates** — when the school is Shape Up, the timebox is fixed first and the solution is shaped to fit it. Scope flexes, time doesn't (Singer / Shape Up).
4. **One school per document** — a Cagan outcome brief and a Shape Up pitch are different contracts with engineering. Blending them produces autonomy on paper and spec-litigation in practice. See [./references/schools.md](./references/schools.md).
5. **Assumptions are labeled, never silent** — anything not backed by cited telemetry or discovery logs is tagged `[ASSUMPTION]` inline, with a revisit trigger.
6. **License to say no** — an evidence-free request gets substantive pushback before a full draft. Compliance is not helpfulness. See [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md).

## 2. The Context Gate

Before drafting anything, establish three things. Do not skip; do not guess silently.

1. **Strategy context / ICP** — who is this for, and how does it serve the active strategic focus? If the workspace has `product/strategy.md`, read it and cite it in the header: `[RESOLVED FROM WORKSPACE: product/strategy.md (updated YYYY-MM-DD)]`. If the file is older than 90 days, append `[WARNING: strategy.md may be stale]`. If a request contradicts the active focus, surface it: `[STRATEGIC CONTRADICTION DETECTED: request targets X, active focus is Y — justify or pivot]`.
2. **Evidence base & weight** — what telemetry or discovery backs this? Apply the Minimum Evidence Weight Rule from [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md). A big bet without evidence is labeled `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]`.
3. **Stage & appetite** — company stage, team capacity, cycle appetite (e.g. "6-week big batch, 2 teams").

If any of the three is missing, ask at most three targeted questions to obtain them — but if the request is a big bet and the evidence base is empty, do not end in questions: run the Pushback Protocol (§5) as the response. If the user's prompt contains `[DRAFT-ONLY]` or `[SANDBOX]`, skip both and proceed under the bypass rules in [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md) (labeled assumptions + risk note, header `[DRAFT-ONLY / SANDBOX BYPASS ACTIVE]`).

## 3. School Selection

Pick exactly one, state it in the document header, and follow its rules:

| Default: Cagan outcome brief | Choose Shape Up pitch instead if |
| :--- | :--- |
| Team is empowered: given the problem, owns the solution | The timebox is fixed first (6-week / 2-week appetite) |
| Discovery is continuous; solution space is open | Scope control is the primary pain (backlog drowning, slipping dates) |
| Regulated/safety-critical domains need full risk documentation | Team is highly collaborative and wants implementation autonomy |

Choose Cagan outcome brief regardless if the domain is regulated or safety-critical (billing engines, medical, compliance) — exact specs are contractually required there. Full decision tree: [./references/schools.md](./references/schools.md).

## 4. Workflow

1. Run the Context Gate (§2). Missing inputs → ask or bypass per tags.
2. Select the school (§3) and load the matching template: [./assets/outcome-brief.md](./assets/outcome-brief.md) or [./assets/shaped-pitch.md](./assets/shaped-pitch.md). For executives or cross-functional audiences use [./assets/one-pager.md](./assets/one-pager.md) instead — format selection runs after the §5 evidence check, and pushback overrides any template.
3. Fill the template. Every placeholder becomes a concrete claim, a cited evidence reference, or an `[ASSUMPTION]` tag. Delete unused sections; never leave bracketed placeholders in output.
4. If the evidence base fails the Minimum Evidence Weight Rule and no bypass tag is present: stop, run the Pushback Protocol (§5), and ship only the minified draft it produces.
5. Add a **Kill Criteria** section to every finalized document: quantitative thresholds, each with an anchor (historical baseline or labeled assumption) and a revisit date.
6. On finalization, append a Decision Journal entry per [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md) §4 (skip for bypassed drafts). If an entry for the same feature exists, update it — never duplicate.

## 5. License to Say No (Pushback Protocol)

When the evidence base is "none" or a single anecdote ("the CEO wants a chatbot", "one customer asked for X"), produce pushback in this order, before any full draft:

1. **Name the unvalidated assumptions** — specific Value / Usability / Feasibility / Viability leaps, not "more research is needed".
2. **Falsifiable kill criteria** — a 1-week discovery plan; each activity has a quantitative threshold and an explicit kill-vs-fund decision. Every number states its anchor or is `[ASSUMPTION]`-tagged.
3. **Genuinely minified draft** — <= 10 lines of core logic, labeled `[EVIDENCE-FREE DRAFT]`, so the idea isn't lost but no premature detail work is done.
4. **Positive decision framework** — the exact conditions (ARR segment, contract commitment, ICP evidence) under which building this *would* be right.

Full rules and examples: [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md).

## 6. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Feature-factory PRD | Success criteria are "launch by date X", "ship Y" | Rewrite success as outcome metrics with baselines and targets |
| Framework smoothie | Document has both "6-week appetite" and a 40-item requirements backlog | Pick one school (§3); move the rest to Out of Bounds or discard |
| Solution-first spec | First page describes UI; no problem or risk section | Reorder: problem, evidence, risks, then bounded solution |
| Silent assumptions | Precise numbers with no source ("30% of users want this") | Cite the telemetry/interview, or tag `[ASSUMPTION]` |
| Requirements laundry list | 50 MUST/SHOULD bullets dictating implementation | Convert to solution boundaries; give empowered teams the problem |
| Phantom kill criteria | "We'll measure success" with no threshold or date | Add threshold + anchor + revisit date, or delete the metric |

## 7. Workspace State

Read — `product/strategy.md` at the Context Gate (§2.1). Expected header shape: `# Product Strategy State` with `Last-updated: YYYY-MM-DD`, an ICP block, an Active Strategic Focus (GEM) rank + one-line justification, and a Cycle Appetite line. Cite `[RESOLVED FROM WORKSPACE: product/strategy.md (updated YYYY-MM-DD)]`; age > 90 days appends `[WARNING: strategy.md may be stale]`; a request contradicting the active focus surfaces `[STRATEGIC CONTRADICTION DETECTED: ...]`.

Write — on finalization, append or update one entry in `product/decisions.md` (skip for bypassed drafts). Canonical schema, identical across every writer:

```markdown
## [YYYY-MM-DD] | Type: [PRD commit / prioritization / kill-pivot / strategic bet / launch] | [Decision name]
- **Decision:** [what is being committed, one sentence]
- **Alternatives considered:** [one line each]
- **Predicted outcome:** [metric] moves from [X, anchored to baseline period] to [Y] by [date]
- **Kill criterion:** [threshold + anchor] at [revisit date] -> [kill/pivot action]
- **Confidence:** [NN]%
- **Status:** Pending
```

Update-not-duplicate: an entry for the same feature name gets a dated `### Addendum [YYYY-MM-DD]`, never a second `##` entry; commit-time fields stay frozen. No filesystem means emitting the entry fenced for the user to file. Full rules: [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md) §4.

## 8. Files

- [./references/evidence-and-pushback.md](./references/evidence-and-pushback.md) — Minimum Evidence Weight Rule, pushback protocol detail, the shared decision-log entry format, bypass rules. Load for any gate/pushback/journal step.
- [./references/schools.md](./references/schools.md) — Cagan vs Shape Up decision tree and blending detection. Load when the school is ambiguous.
- [./assets/outcome-brief.md](./assets/outcome-brief.md) — Cagan-style template.
- [./assets/shaped-pitch.md](./assets/shaped-pitch.md) — Shape Up pitch template.
- [./assets/one-pager.md](./assets/one-pager.md) — executive one-pager template.
