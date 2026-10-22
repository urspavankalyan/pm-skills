# Evals: user-stories

## Scenario 1 — Volume demand (adversarial)
**Prompt:** "Write 40 user stories for this epic: admin dashboard. I need them for sprint planning tomorrow."
**Expected behavior:**
- Volume-Demand Protocol fires before any story is written: names the filler failure mode (quota stories fail INVEST Small/Valuable; Build Trap output-over-outcome).
- Delivers the right artifact instead: story map with backbone, walking skeleton, and 5-9 well-formed first-slice stories (job-story narrative, Gherkin AC, INVEST checked), using [../user-stories/assets/story-map.md](../user-stories/assets/story-map.md).
- States that stories are experiments toward an outcome, not tickets; offers splitting for breadth and the bypass rule (insist with compliance reason, or `[DRAFT-ONLY]`/`[SANDBOX]`) for full volume — and under any bypass, stories that fail a check ship tagged `[INVEST-FAIL: S]` rather than laundered as healthy.
- Must NOT emit 40 tickets, must NOT ask only clarifying questions and end, must NOT leave bracketed placeholders in delivered stories.

## Scenario 2 — Vague request (diagnostic)
**Prompt:** "write some user stories for onboarding"
**Expected behavior:**
- Workflow step 1 fires: asks at most two targeted questions (which customer job? which outcome metric moves?) or attaches an outcome stub tagged `[ASSUMPTION - outcome unvalidated]`.
- Maps before writing (backbone + walking skeleton) instead of dumping free-floating stories; stories that do get written carry job-story narrative, Gherkin AC, and an experiment note.
- Must NOT produce a flat list of solution-first stories against a bare epic name.

## Scenario 3 — Well-anchored request (happy path)
**Prompt:** "Outcome brief says Week-2 retention for new workspaces moves 31% -> 40% by Q3; 3 churn interviews cite 'can't get my team in fast enough'. Write the first slice of stories."
**Expected behavior:**
- Gate passes with evidence cited; every story's "Outcome it serves" line carries the retention metric; narratives are job stories anchored in the team-invitation situation.
- Each story has Gherkin AC with observable Then-clauses and an experiment note (signal, window, kill/pivot decision).
- Walking-skeleton slice cut before depth; INVEST checked per story.

## Scenario 4 — Split request with discipline check
**Prompt:** "This story is too big: 'As a merchant, I want to export my order history.' Split it."
**Expected behavior:**
- Loads [../user-stories/references/craft.md](../user-stories/references/craft.md); applies a named value-axis pattern (data variation first here: CSV of all orders, then date-filtered, then scheduled), each child independently Valuable and Testable.
- Anchor for "fits the horizon" cites the team's stated cadence or tags `[ASSUMPTION]`.
- Must NOT split into "backend export" + "frontend download" layer children; must NOT drop the job-story narrative in the children.
