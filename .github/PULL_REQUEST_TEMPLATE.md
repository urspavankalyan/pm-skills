## What does this PR change?

- [ ] New skill (dir matches `name` in frontmatter; SKILL.md <= 400 lines, per STYLE_GUIDE)
- [ ] Behavior change to an existing skill
- [ ] Reference / asset / template improvement
- [ ] Docs, evals, or tooling only

## Quality gates

- [ ] `python3 scripts/validate_skills.py` exits 0 with no new warnings
- [ ] Every relative markdown link resolves
- [ ] New frameworks carry Definition / When to use / When NOT to use / Worked Example / Source URL
- [ ] Every quantitative threshold states its anchor or is tagged `[ASSUMPTION]`
- [ ] Frontmatter description includes "Use when" trigger phrases in real user language
- [ ] The skill stays self-contained (no sibling-skill directory references; schemas restated inline)

## Eval execution (required for behavior changes)

- [ ] I executed `evals/<skill-name>.md` scenarios against a fresh agent reading only the skill files
- [ ] Adversarial scenario included; expected behavior observed
- [ ] Result appended to `docs/eval-results.md` (date, prompt, verdict, issues fixed)
