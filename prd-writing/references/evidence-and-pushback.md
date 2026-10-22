# Evidence, Pushback & Decision Journal Reference

## 1. Minimum Evidence Weight Rule

Match the bet size to the evidence weight. State the weight class explicitly in every PRD header.

| Bet size | Minimum evidence | Otherwise |
| :--- | :--- | :--- |
| **Big batch** (6-week cycle, >2 person-weeks) | Opportunity observed in >= 5 independent interviews within the ICP, OR session telemetry showing >= 15% of active users hit the friction | Label `[STRATEGY-DRIVEN ONLY - NO COMPELLING EVIDENCE]` and run pushback (§2) |
| **Small batch** (2-week cycle / discovery spike) | 1–4 customer interviews, or recurring support tickets / churn notes | Acceptable; still label the evidence source |
| **Hygiene / compliance** | Regulatory requirement, security fix, contractual obligation | Evidence base is the obligation itself; cite it |

The 5-interview and 15% thresholds are this skill's operating defaults, not universal law — they are `[ASSUMPTION]`-grade anchors a team may recalibrate and record in its strategy doc.

## 2. Pushback Protocol (License to Say No)

Trigger: evidence base is "none", a single customer, or executive vanity, and no `[DRAFT-ONLY]` / `[SANDBOX]` tag is present.

Output, in order:

1. **Unvalidated assumptions** — one bullet per product risk (Cagan): *Value: no evidence anyone outside this one account wants it. Usability: unknown where it fits the workflow. Feasibility: LLM cost per conversation unmodeled. Viability: support burden unscoped.*
2. **1-week discovery plan with kill criteria** — each item: activity, quantitative threshold, anchor, and the kill-vs-fund decision. Example: "Fake-door card in settings for 5 days; click-through >= 8% of eligible sessions (anchor: median entry-point CTR 6% in Q2 telemetry) funds a 2-week spike; < 4% kills."
3. **Minified draft** — <= 10 lines of core logic, labeled `[EVIDENCE-FREE DRAFT]`.
4. **Positive decision framework** — a short matrix: "Build now if: (a) >= 3 ICP accounts commit in writing, (b) churn interviews name this cause in >= 5 of 10 calls, (c) strategic exception approved by CEO with kill date."

Pushback is respectful and concrete. It never says "more research is needed" without saying exactly what research, what threshold, what decision.

## 3. Bypass Tags

If the prompt contains `[DRAFT-ONLY]` or `[SANDBOX]`:

- Header the output `[DRAFT-ONLY / SANDBOX BYPASS ACTIVE]`.
- Skip blocking questions and pushback, but keep the strategic spine: every assumed ICP, need, or evidence claim is tagged `[ASSUMPTION]` inline.
- If the build implies > 2 weeks of effort or a strategic feature, append a one-paragraph **Risk Note** naming the specific value/usability risks of building undiscovered.
- Never write bypassed drafts to the decision journal.

## 4. Decision Journal Entry

On finalization of a PRD, spec, or prioritization commit, append to `product/decisions.md` (create if absent; if filesystem is unavailable, emit the entry as a fenced block for the user to file):

```markdown
## [YYYY-MM-DD] | Type: [PRD commit / prioritization / kill-pivot / strategic bet / launch] | [Decision name]
- **Decision:** [what is being committed, one sentence]
- **Alternatives considered:** [one line each]
- **Predicted outcome:** [metric] moves from [X, anchored to baseline period] to [Y] by [date]
- **Kill criterion:** [threshold + anchor] at [revisit date] -> [kill/pivot action]
- **Confidence:** [NN]%
- **Status:** Pending
```

Resolution and context changes are appended below the entry by scoring sessions as `### Resolution [YYYY-MM-DD]` and `### Addendum [YYYY-MM-DD]`; commit-time fields stay verbatim forever. This is the one canonical schema: entries written here are complete for calibration scoring, and entries written by journal sessions are updated, never duplicated.

Regeneration semantics: updating an existing PRD updates the matching entry by feature name via addendum — never append a duplicate.

## 5. Sources

- Four product risks, empowered teams, outcome briefs: Marty Cagan — [svpg.com/articles](https://svpg.com/articles/)
- Appetite, shaping, reject-the-backlog: Ryan Singer — [basecamp.com/shapeup](https://basecamp.com/shapeup)
- Evidence-cited prioritization critique: Lenny Rachitsky — [lennysnewsletter.com](https://www.lennysnewsletter.com/)
