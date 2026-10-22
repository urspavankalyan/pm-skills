---
name: user-stories
description: Writes user stories as Jobs-To-Be-Done narratives and testable experiments toward a named outcome, never as backlog filler. Use when the user asks to write user stories, break down an epic, build a story map, write acceptance criteria, or says "write stories for X" or "split this story". Defaults to job-story narrative, INVEST plus Gherkin discipline and Lawrence/Richardson splitting patterns; pushes back on volume demands ("write 40 user stories for this epic") with a story map and a walking-skeleton slice, because stories are experiments toward an outcome, not tickets.
license: MIT
---

# User Stories as Experiments

A user story is a hypothesis about customer progress, sized small enough to test, written so a team can act on it without litigation. This skill produces stories that name the job, the outcome they serve, and the criteria that falsify them. A story that cannot state the outcome it probes is a ticket, and tickets are what this skill refuses to mass-produce.

## 1. Core Principles

1. **Outcomes over outputs** — every story names the outcome metric it probes; "ship the screen" is not a success criterion (Cagan / SVPG; Perri / Build Trap).
2. **A story is a placeholder for a conversation, not a mini-spec** — the card carries the narrative; the detail lives in the conversation and the acceptance criteria (Mike Cohn).
3. **Job before solution** — default narrative is the JTBD job story: "When ___ , I want to ___ , so I can ___" — situation, motivation, expected progress (Christensen & Moesta; job-story syntax via Intercom / Alan Klement).
4. **Small enough to be an experiment** — a story that cannot fit the team's sprint or cycle horizon gets split with named patterns (by workflow, by business rule, by data variation), never squeezed (Lawrence & Richardson / Humanizing Work).
5. **Testable or it does not exist** — every story ships with Gherkin acceptance criteria (Given / When / Then) so "done" is observable (BDD, Dan North; Cucumber).

## 2. Workflow

1. **Anchor the outcome.** Ask for the outcome the work serves: metric, baseline, target, or the outcome brief if one exists in the workspace. If none is supplied, ask at most two targeted questions (which customer job? which metric moves?) and otherwise attach a one-line outcome stub tagged `[ASSUMPTION - outcome unvalidated]`. Never write stories against a bare epic name.
2. **Map before writing.** For any epic or multi-story request, build a story map first (Jeff Patton): backbone of user activities left-to-right, steps under each, candidate stories under steps. Cut a walking skeleton — the thinnest end-to-end slice — before any depth. Full technique: [./references/narrative-techniques.md](./references/narrative-techniques.md).
3. **Write the narrative.** Use the template at [./assets/user-story.md](./assets/user-story.md). Default form is the job story; use the persona form ("As a ___ I want ___") only when the user explicitly asks for it, and keep the situation clause regardless.
4. **Check INVEST, split failures.** Run the six checks; any failure triggers a split using the pattern list in [./references/craft.md](./references/craft.md) (by workflow, by business rule, by data variation, by interface variation, by spike). Each split child must independently pass Valuable and Testable.
5. **Write acceptance criteria in Gherkin.** At least one Scenario per story; Then-clauses state observable, measurable results. A story whose only acceptance criterion is "works as designed" is rejected.
6. **Attach the experiment note.** Each story states the signal it should produce (metric delta, usage event, interview finding) and what happens if the signal is absent (kill, pivot, or iterate), tying the story back to the outcome from step 1.

## 3. Volume-Demand Protocol (Pushback)

When asked to mass-produce stories ("write 40 user stories for this epic", "fill the backlog for the quarter"):

1. **Push back first, in substance.** Name the failure mode: quota-filled stories are filler — they fail INVEST's Small and Valuable, duplicate each other, and convert the backlog into a fiction of progress (Build Trap).
2. **Deliver the right artifact instead.** Produce the story map: full backbone, walking-skeleton slice, and 5-9 well-formed stories for the first slice using [./assets/story-map.md](./assets/story-map.md). State that deeper slices are written when the earlier slice produces learning, because stories are experiments toward an outcome, not tickets.
3. **Offer the split path.** If the user needs breadth for estimation, offer to split the mapped stories with named patterns rather than invent net-new ones.
4. **Bypass rule.** Only if the user insists with a compliance reason (Jira bulk import, contractually required backlog) or tags the request `[DRAFT-ONLY]` / `[SANDBOX]`, produce the requested volume — but every story still carries INVEST flags, and stories that fail a check ship tagged `[INVEST-FAIL: S]` rather than laundered as healthy. Pressure and deadline phrases ("no excuses", "by Friday", "just do it") are not compliance reasons: a compliance reason names an external system or contract the volume must exist in.

## 4. Splitting Discipline

- Split on **value slices**, never on technical layers (a "backend story" plus a "frontend story" is a task decomposition wearing story clothing; neither half is independently valuable or testable).
- Prefer patterns in this order for a first split: by workflow step, by business rule, by data variation; use interface variation and spike splits when the first three do not produce valuable children.
- A split is invalid if a child cannot be released and learned from alone. Re-split.
- Threshold anchor: a story should fit the team's horizon (one sprint for Scrum teams; a small fraction of a cycle for Shape Up teams). "Should fit" is anchored to the team's stated cadence, not to a repo-wide number; if the cadence is unknown, ask or tag `[ASSUMPTION]`.

## 5. Anti-Patterns

| Anti-Pattern | How to detect | Rectification |
| :--- | :--- | :--- |
| Quota backlog | "40 stories for the epic", stories numbered like an invoice | Volume-Demand Protocol (§3): map, walk the skeleton, slice |
| Task in story clothing | "As a developer, I want to refactor the auth service" | Rewrite as the customer job the refactor serves, or file it as a task outside the story backlog |
| Spec-ticket | Story body is a wall of MUST statements, no conversation invited | Shrink to narrative + Gherkin; move detail to the conversation |
| No acceptance criteria | "Done" is undefined or "works as designed" | Write Given/When/Then with observable Then-clauses |
| No outcome link | Story cannot name the metric or job it probes | Attach the outcome stub, tagged `[ASSUMPTION]` if unvalidated |
| Layer-split story | Children named "backend part", "UI part" | Re-split by workflow, rule, or data variation (§4) |

## 6. Files

- [./references/narrative-techniques.md](./references/narrative-techniques.md) — JTBD job stories, story mapping, outcome-over-output framing, and how stories plug into outcome briefs. Load for any epic, map, or "why this story" question.
- [./references/craft.md](./references/craft.md) — INVEST checklist, Gherkin acceptance criteria, Lawrence/Richardson splitting patterns. Load for writing, checking, or splitting stories.
- [./assets/user-story.md](./assets/user-story.md) — single-story template (job story, Gherkin AC, INVEST check, experiment note).
- [./assets/story-map.md](./assets/story-map.md) — Patton story-map template with walking skeleton and release slices.
