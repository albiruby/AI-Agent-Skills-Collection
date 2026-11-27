# Installation Guide

This pack is designed to be installed as a whole: skills, shared references, templates, scripts, examples, and evals.

## 1. Requirements

- Python 3.9+ for the bundled image/QA scripts.
- Pillow:
  ```bash
  pip install pillow
  ```
- Optional: numpy for faster background slicing (scripts fall back to Pillow).
- Image viewer/multimodal capability is recommended for visual QA.

On Windows use `python` (the `python3` alias may open the Microsoft Store). On macOS/Linux use `python3` when available.

## 2. Install the whole pack

### OpenCode

Global:

```text
~/.config/opencode/skills/project-docs-skills/
```

Project:

```text
<project>/.opencode/skills/project-docs-skills/
```

Copy the whole pack folder, not only `skills/`. OpenCode will discover each folder containing `SKILL.md` below the pack root (depth allows the `skills/` grouping).

### Claude Code

```text
~/.claude/skills/project-docs-skills/
```

### Codex / universal Agent Skills

```text
~/.agents/skills/project-docs-skills/
```

### Gemini CLI / Cursor / Windsurf

Use the skill directory documented by the product; keep the same pack hierarchy.

### Windows PowerShell

```powershell
$dest = "$env:USERPROFILE\.config\opencode\skills\project-docs-skills"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item -Recurse -Force ".\*" $dest
```

### macOS / Linux

```bash
mkdir -p ~/.config/opencode/skills/project-docs-skills
cp -R . ~/.config/opencode/skills/project-docs-skills/
```

## 3. Why install the whole pack

Skills reference shared files with `../../references/` and `../../templates/`. Scripts live inside their skill folders. Installing only `skills/<one-skill>/` may break those links.

If you must install a single skill, copy the referenced `references/` and `templates/` files alongside it and adjust paths.

## 4. Verify

Ask the agent:

> Use `project-docs-skills` to inspect this project and propose a documentation and visual asset plan.

Then test one script:

```bash
python skills/clean-screenshot-slicer/scripts/slice_clean_device.py --help
```

## 5. Update / remove

- Update: replace the whole pack folder; keep project outputs outside it.
- Remove: delete the pack folder from the skill directory.
- Do not delete `docs/assets/raw/` or store masters from a project as part of uninstalling the pack.

## 6. Troubleshooting

- **Skill not discovered:** confirm the folder contains `SKILL.md` and the pack is under a configured skill source.
- **`python3` opens Store on Windows:** use `python`.
- **Pillow missing:** install with permission; the scripts will otherwise fail.
- **Text-only harness:** use the scripts for validation and report visual checks as unverified.
- **Store requirements:** verify current official docs; never rely on remembered dimensions.
