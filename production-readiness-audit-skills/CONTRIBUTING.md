# Contributing

## Adding or changing a skill
1. Folder `skills/<name>/` with `SKILL.md` (YAML frontmatter `name` = folder name, `description` ≤ 1024 chars, "pushy": what it does **and** when to trigger, include Indonesian + English phrasing).
2. Keep `SKILL.md` under 500 lines; move long lists to `references/`.
3. Each domain checklist lives in `references/checklist.md` with headings `## <N>. <Title>`; update `references/domain-index.md` and `SKILLS.md`.
4. Every skill must define: procedure, severity calibration, output, pitfalls, and what is **Not Verifiable** without access.
5. Safety rules are non-negotiable: read-only by default, no secrets/PII in output, approval before production-affecting actions.
6. Run `python3 tools/validate_pack.py` — it must pass.
7. Add a line to `CHANGELOG.md`.

## Style
Imperative, specific, evidence-oriented. Explain *why* for rules. Prefer commands that are read-only. Do not hardcode vendor prices/limits — instruct the agent to verify current docs.
