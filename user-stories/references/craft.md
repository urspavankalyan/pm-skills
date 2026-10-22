# Craft: INVEST, Gherkin, Splitting

Companion to SKILL.md §2 steps 4-5 and §4. Load when writing, checking, or splitting stories.

## 1. INVEST checklist

- **Definition:** A story is healthy when it is Independent (scheduleable on its own), Negotiable (a placeholder for conversation, not a contract), Valuable (delivers a slice of customer or outcome value alone), Estimable (small and understood enough to size), Small (fits the team's horizon), Testable (its acceptance criteria can falsify it). Mnemonic by Bill Wake (2003); disseminated and taught via Mike Cohn's *User Stories Applied*.
- **When to use:** on every story before it enters a sprint or cycle slice; as the split trigger — the first failing letter names the split goal.
- **When NOT to use:** as a scoring formula (no point totals; a single hard fail on Valuable or Testable vetoes the story); and not for discovery spikes, which are testable by a learning deliverable but not by customer-value Gherkin.
- **Worked Example (Hypothetical: marketplace merchant):** "As a merchant, I want bulk order management" fails Small and Testable. After splitting by workflow (pick → pack → ship), the child "When I have 50 orders to ship, I want to print all picking lists at once, so I can start the warehouse floor without an hour of clicking" passes all six.
- **Source URL:** [mountaingoatsoftware.com](https://www.mountaingoatsoftware.com/) (Mike Cohn); origin: Bill Wake, 2003.

## 2. Gherkin acceptance criteria

- **Definition:** Structured Given [context] / When [single triggering action] / Then [observable, measurable result] scenarios, from Behavior-Driven Development (Dan North) and its Cucumber tooling. The Then-clause is the contract: observable from the user's or system's outside, measurable without interpretation.
- **When to use:** on every story that produces user-visible or system-visible behavior; also the cleanest input to test automation and to the story's experiment note.
- **When NOT to use:** for pure discovery spikes (use a learning deliverable instead: "a dated note answering X"); and not as a UI spec — Gherkin describes behavior, not pixels.
- **Worked Example (Hypothetical: B2B analytics):** Given a workspace with 2M event rows, When the PM exports the last 30 days as CSV, Then the export completes in under 60 seconds and the file opens with all 14 columns intact. The 60-second bound cites its anchor: current exports time out at 10 minutes (telemetry report Q3).
- **Source URL:** [cucumber.io](https://cucumber.io/) (Gherkin / BDD)

## 3. Splitting patterns (Lawrence & Richardson)

Richard Lawrence and Pete Richardson's Humanizing Work pattern list; the three primary patterns for this skill:

- **By workflow steps:** split a story that strings a multi-step process into one child per step, keeping the end-to-end thin path alive in the first child. Use when the narrative contains "and then".
- **By business rule:** split when one story embeds several rules ("apply discount, tax, and shipping rules"); one child per rule, simplest rule first.
- **By data variation:** split when complexity lives in the kinds of data handled ("export orders" becomes CSV first, then scheduled exports, then filtered exports); each variation is its own child, ordered by customer frequency.

Secondary patterns: by interface variation (web first, API later), by effort spike (separate the unknown into a timeboxed spike child), and by simplifying the acceptance criteria (write the simple version, add each complexity as a child).

- **When to use:** whenever INVEST fails on Small, or a story will not fit the team's stated horizon; pick the pattern whose axis matches where the size lives (process length → workflow; rule count → rule; data kinds → data variation).
- **When NOT to use:** to split by technical layer or by team ownership — those children fail Valuable and Testable and are tasks, not stories; re-split on a value axis.
- **Worked Example (Hypothetical: marketplace merchant exports):** "When I need my order history for accounting, I want to export orders, so I can close the books without manual entry" is too big. By data variation: child 1 CSV of all orders (the walking-skeleton slice), child 2 date-filtered exports, child 3 scheduled monthly exports. By business rule, child 2 itself later splits (tax-inclusive vs tax-exclusive rows). Every child releasable and learned-from alone.
- **Source URL:** [humanizingwork.com](https://www.humanizingwork.com/) (story-splitting patterns poster, Lawrence & Richardson)

## 4. Stories as experiments, not tickets

Operational rules tying craft to outcomes:

1. The acceptance criteria define the build; the experiment note defines the learning. Both live on the same card ([../assets/user-story.md](../assets/user-story.md)).
2. The experiment note states: signal (metric delta or usage event, with anchor or `[ASSUMPTION]`), observation window, and decision (kill / pivot / iterate) if the signal is absent. No undated "we will monitor".
3. Release slices in the story map carry expected outcome deltas; at slice review, the delta is compared to the note and the next slice is re-planned from evidence. That loop — not ticket count — is the definition of progress.

## 5. Sources

- INVEST: Bill Wake (2003), via Mike Cohn — [mountaingoatsoftware.com](https://www.mountaingoatsoftware.com/)
- Gherkin / BDD: Dan North, Cucumber — [cucumber.io](https://cucumber.io/)
- Splitting patterns: Richard Lawrence & Pete Richardson — [humanizingwork.com](https://www.humanizingwork.com/)
- Stories as conversations: Mike Cohn, *User Stories Applied* — [mountaingoatsoftware.com](https://www.mountaingoatsoftware.com/)
