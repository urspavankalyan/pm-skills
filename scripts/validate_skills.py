#!/usr/bin/env python3
"""Structural linter for the pm-skills repo (agentskills.io spec).

Usage: python3 scripts/validate_skills.py [repo_root]
Exits 1 on errors, 0 when clean. Warnings never fail the build.
"""
import os
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)(#[^)]*)?\)")
LOCAL_ABS_RE = re.compile(r"/(Users|home)/[^\s)]+")
BANNED_RE = re.compile(r"TODO|lorem ipsum|SKILL_PRUNED", re.I)


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, "missing frontmatter opener"
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, "frontmatter not closed"
    fm, body = m.group(1), m.group(2)
    fields = {}
    for line in fm.splitlines():
        km = re.match(r"^([A-Za-z0-9-]+):\s*(.*)$", line)
        if km:
            fields[km.group(1)] = km.group(2).strip()
    return fields, body


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser("~"), "pm-skills"))
    errors, warnings = [], []
    skill_dirs = sorted(
        d for d in os.listdir(root)
        if os.path.isdir(os.path.join(root, d)) and os.path.isfile(os.path.join(root, d, "SKILL.md"))
    )
    if not skill_dirs:
        print(f"ERROR: no skill directories found under {root}")
        sys.exit(1)

    for d in skill_dirs:
        sdir = os.path.join(root, d)
        skill_md = os.path.join(sdir, "SKILL.md")
        text = open(skill_md, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{d}: {body}")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")

        if name != d:
            errors.append(f"{d}: frontmatter name '{name}' != directory name")
        if not NAME_RE.match(name or ""):
            errors.append(f"{d}: name '{name}' violates kebab-case spec")
        if len(name) > 64:
            errors.append(f"{d}: name > 64 chars")
        if not desc:
            errors.append(f"{d}: missing description")
        elif len(desc) > 1024:
            errors.append(f"{d}: description {len(desc)} chars > 1024")
        elif "use when" not in desc.lower():
            warnings.append(f"{d}: description lacks a 'Use when' trigger clause")

        lines = text.count("\n")
        if lines > 400:
            errors.append(f"{d}: SKILL.md {lines} lines > 400 (move depth to references/)")
        elif lines > 320:
            warnings.append(f"{d}: SKILL.md {lines} lines (target <= 320)")

        if not re.search(r"\]\(\./references/|\]\(\./assets/", text):
            warnings.append(f"{d}: no references/ or assets/ links (fine if truly minimal)")

        # relative markdown links must resolve; no absolute local paths, no banned tokens
        for dirpath, _, files in os.walk(sdir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dirpath, f)
                content = open(p, encoding="utf-8").read()
                rel = os.path.relpath(p, root)
                for target, _anchor in LINK_RE.findall(content):
                    if target.startswith(("http", "mailto")):
                        continue
                    resolved = os.path.normpath(os.path.join(dirpath, target))
                    if not os.path.isfile(resolved):
                        errors.append(f"{rel}: broken relative link -> {target}")
                if LOCAL_ABS_RE.search(content):
                    errors.append(f"{rel}: absolute local path found")
                if BANNED_RE.search(content):
                    errors.append(f"{rel}: TODO/placeholder marker found")

        if not os.path.isfile(os.path.join(root, "evals", f"{d}.md")):
            warnings.append(f"{d}: missing evals/{d}.md")

    print(f"Skills found: {len(skill_dirs)}")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). FAIL")
        sys.exit(1)
    print(f"\nClean. {len(warnings)} warning(s). PASS")


if __name__ == "__main__":
    main()
