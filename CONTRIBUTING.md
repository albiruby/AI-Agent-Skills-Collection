# Contributing

Thanks for helping improve this collection. The bar is deliberately high: every skill here is something an agent will load into context, so vague or duplicated skills cost everyone tokens.

## Ways to contribute

- **Report a problem** — a skill gives wrong or unsafe guidance, doesn't trigger when it should, or produces inconsistent output.
- **Improve an existing skill** — clearer wording, missing edge cases, better output structure, removed redundancy.
- **Propose a new pack or skill** — a task no existing skill covers well.
- **Share evaluation results** — test prompts and notes on how a skill behaves in a particular agent.

## Before you start

1. Search [existing issues](../../issues) and pull requests to avoid duplicates.
2. For a **new pack** or a **large change**, open an issue first. Overlap with an existing skill is usually a reason to improve that skill instead.
3. Small fixes can go straight to a pull request.

## Skill requirements

Every `SKILL.md` in this repository must satisfy all of the following. CI enforces items 1–4; the rest are review requirements.

1. **Frontmatter is exactly `name` + `description`.** No other keys (`version`, `license`, `metadata` … belong in the README or CHANGELOG).
2. **Folder name = `name`.** Same value, same spelling, at every nesting level.
3. **The file opens with a title H1** in plain title case — not `# Instructions`, not `# Skill: …`, not ALL CAPS. Body sections may use `#` or `##`; keep the style consistent within your pack.
4. **`description` is under 1024 characters** and contains an explicit **"Use when…"** (or "Use whenever…") trigger naming concrete situations and realistic user phrasings.
5. **Plain Markdown.** No vendor-specific syntax; skills must work when pasted into any chat.
6. **Honest claims.** Never state that something was tested, run, or verified unless it was. Separate facts, assumptions, and recommendations.

Use [`SKILL_TEMPLATE.md`](SKILL_TEMPLATE.md) as the starting point for a new skill.

## Repository conventions

- **Folder names are kebab-case** with no version suffixes (`-v1`, `-v1.1`, `-universal`) and no numeric prefixes (`01-`, `NN-`). Versions belong in the pack's README or CHANGELOG.
- **One pack = one top-level folder** with a `README.md` describing what it covers, how to install it, and when to use it.
- **Pack READMEs** include a skills table (name + one-line job) and a "when to use" section.
- **Reference paths stay current** — if you rename a folder, update every `README.md`, `SKILL.md`, and `manifest.json` that points at it.

## Pull request process

1. Keep PRs focused: one concern per PR.
2. Run the frontmatter check locally before pushing:

   ```powershell
   powershell -File .github/scripts/validate-frontmatter.ps1
   ```

3. In the PR description, state what changed and why, and how you evaluated the skill (example prompt + observed behavior helps).
4. CI must pass before review.

## Style guide for descriptions

```
<What the skill does and what it produces.> Use when <concrete situations>,
<realistic user phrasings>, or <artifacts that should trigger it>.
```

Good:

> Designates a locked Style Bible for consistent character art. Use when the user wants the same character across multiple images, complains that "the face keeps changing", or starts a batch of related illustrations.

Bad:

> Helps with image consistency tasks. Use when needed.

Be specific enough that the skill triggers on its own, and narrow enough that it doesn't hijack unrelated requests.
