# Contributing to Web & App Dev Skills

Thank you for helping improve these skills. This guide explains what makes a good contribution and how to submit one.

## Ways to contribute

- **Report a problem:** a skill gives wrong, vague, or unsafe guidance; a skill does not trigger when it should; the output is inconsistent.
- **Improve an existing skill:** clearer wording, missing edge cases, better output structure, removed redundancy.
- **Propose a new skill:** a task in web or app development that no existing skill covers well.
- **Share evaluation results:** test prompts, example outputs, and notes on how a skill behaves in a particular AI tool.
- **Fix documentation:** typos, broken links, unclear instructions.

## Before you start

1. Search existing issues and pull requests to avoid duplicates.
2. For a **new skill** or a **large change**, open an issue first and describe the task, the audience, and how it differs from the existing skills. Overlap with an existing skill is usually a reason to improve that skill instead.
3. For small fixes, you can open a pull request directly.

## Skill requirements

Every skill must meet these rules.

### File and naming

- One folder per skill: `skills/<skill-name>/SKILL.md`.
- The folder name, lowercase with hyphens, must exactly match the `name` in the frontmatter.
- The skill is a single self-contained `SKILL.md`. Do not depend on other files.

### Frontmatter

```yaml
---
name: skill-name
description: "What the skill does, plus when to use it. Include the situations and phrases that should trigger it."
---
```

- `description` is required and must be under 1024 characters.
- Put both **what the skill does** and **when to use it** in the description. Mention realistic user phrasings so the skill is not under-triggered.
- Avoid double quotes inside the description unless escaped.

### Structure

Follow the shared structure (see [`templates/SKILL_TEMPLATE.md`](templates/SKILL_TEMPLATE.md)):

1. Role and responsibility.
2. **Platform-Agnostic Operation** section (copy it unchanged from an existing skill).
3. **Core Principles**.
4. Numbered **Workflow**.
5. **Required Output Structure**.
6. **Scope Boundaries**, **Communication Style**, and **Final Quality Standard**.

Aim for roughly 120 to 200 lines. If a skill grows past about 500 lines, split it or reorganize it.

### Content rules

- **Tool and vendor independent.** Do not require a specific AI product, model, framework, or service. Where examples are useful, present them as examples, not requirements. Tool-specific file names (for example agent instruction files) are acceptable when that is the actual convention.
- **Evidence honesty.** Skills must never instruct the AI to claim something was tested, executed, deployed, or verified without evidence. Keep facts, assumptions, recommendations, and open questions distinct.
- **No invention.** Skills must tell the AI not to fabricate requirements, endpoints, metrics, or results.
- **Defensive security only.** Security-related skills must not include exploit code or guidance for unauthorized access.
- **No sensitive data.** Do not include secrets, credentials, personal data, internal URLs, or content copied from proprietary or copyrighted sources.
- **Imperative and concrete.** Prefer direct instructions and checklists to long explanations. Explain the reason when a rule is not obvious.
- **Right-sized.** Every instruction should change the AI's behavior. Remove generic advice that a capable AI already follows.

## Validating your change

Before opening a pull request, check:

- [ ] Frontmatter parses as valid YAML and has `name` and `description`.
- [ ] `name` matches the folder name.
- [ ] `description` is under 1024 characters and states when to use the skill.
- [ ] The Platform-Agnostic Operation section is present.
- [ ] There are no vendor lock-in assumptions, secrets, personal data, or unverified claims.
- [ ] Links and cross-references to other skills use the correct names.
- [ ] You tested the skill on at least two realistic prompts (see below).

A quick local check for frontmatter, assuming Python with PyYAML installed:

```bash
python3 - <<'EOF'
import glob, yaml
for p in sorted(glob.glob("skills/*/SKILL.md")):
    text = open(p, encoding="utf-8").read()
    fm = yaml.safe_load(text.split("---\n")[1])
    folder = p.split("/")[-2]
    assert fm["name"] == folder, f"{p}: name does not match folder"
    assert len(fm["description"]) < 1024, f"{p}: description too long"
    assert "Platform-Agnostic Operation" in text, f"{p}: missing platform section"
print("All skills passed.")
EOF
```

## Testing a skill

Skill quality is about behavior, so please include evidence in your pull request:

1. Write **at least two realistic prompts** a user might send, including one that does not mention the skill by name.
2. Run them with the skill loaded in an AI tool and note which tool and model you used.
3. Record whether the skill **triggered** (if your tool loads skills automatically) and whether the output **followed the required structure**.
4. Describe any failure modes: invented facts, skipped steps, bloated output, or ignored boundaries.
5. For a modified skill, compare behavior before and after the change.

Short summaries in the pull request description are enough. Do not paste private project data into examples.

## Commit and pull request conventions

- Use clear, imperative commit messages, for example `Add rate-limit guidance to api-contract-designer`.
- Keep each pull request focused on one skill or one theme.
- In the description, explain **what** changed, **why**, and **how you tested it**.
- Update `CHANGELOG.md` under the `Unreleased` heading.
- If you add a skill, also add it to the table in `README.md`.

## Review process

Maintainers review for accuracy, clarity, consistency with the shared structure, tool independence, and overlap with existing skills. You may be asked to simplify, merge with an existing skill, or add test evidence. Reviews aim to be constructive; please respond to feedback in the pull request.

## Versioning

The project uses [Semantic Versioning](https://semver.org/):

- **Patch:** wording fixes and clarifications that do not change behavior.
- **Minor:** new skills or meaningful additions to existing skills.
- **Major:** renamed or removed skills, or changes that significantly alter a skill's behavior.

Renaming a skill is a breaking change because people reference skills by name. Avoid it unless necessary and document it in the changelog.

## Licensing of contributions

By submitting a contribution, you confirm that you have the right to submit it and that it may be distributed under the license in the [LICENSE](LICENSE) file. Do not submit content you do not have the right to share.

## Reporting security concerns

If a skill could lead an AI to produce unsafe output, such as offensive security content or guidance that exposes secrets, report it privately to the maintainers instead of opening a public issue, using the contact method listed on the repository page.
