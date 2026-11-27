# Installation Guide

## 1. Requirements

- Python 3.9+ for QA/palette/validation scripts.
- Pillow:
  ```bash
  pip install pillow
  ```
- numpy is **not required**.
- Optional: Aseprite/LibreSprite, Blender, ImageMagick, or a game engine for production/integration.
- An image viewer or multimodal harness is recommended for pixel-level QA.

On Windows use `python`; `python3` may be a Store alias. On macOS/Linux use `python3` when available.

## 2. Install options

### OpenCode (global)

Copy the **whole pack** so shared references/templates remain available:

```text
~/.config/opencode/skills/pixel-master/
```

OpenCode discovers each `skills/<skill>/SKILL.md` below that folder.

Project-level:

```text
<project>/.opencode/skills/pixel-master/
```

### Claude Code

```text
~/.claude/skills/pixel-master/
```

### Codex / universal Agent Skills

```text
~/.agents/skills/pixel-master/
```

### Gemini CLI / Cursor / Windsurf / other harnesses

Use the product's documented skill directory. Keep the pack hierarchy if you want shared references/templates.

## 3. Installer scripts

The included installers copy the 26 skill folders directly into a destination:

```bash
bash ./install.sh ~/.config/opencode/skills
```

```powershell
.\install.ps1 -Destination "$env:USERPROFILE\.config\opencode\skills"
```

Skills remain self-contained through their built-in standards block, but the pack-level `shared/`, `references/`, `templates/`, and `scripts/` are not copied by the installer. For full resources, copy the entire pack folder instead.

## 4. Verify

```bash
python scripts/validate_package.py
python scripts/pixel_art_qa.py --help
python scripts/palette_ramp.py "#3a6ea5" --steps 5
```

Ask the agent:

> Use `pixel-master` to inspect this project and propose a pixel-art production plan.

## 5. Update / remove

- Update: replace the whole pack folder; keep project assets outside it.
- Remove: delete the pack folder from the skills directory.
- Do not delete project source assets, native files, or manifests during uninstall.

## 6. Troubleshooting

- **Skill not discovered:** confirm each folder contains `SKILL.md` and lives under a configured skill source.
- **`python3` opens Microsoft Store:** use `python`.
- **Pillow missing:** install with permission; image QA will otherwise fail.
- **No image viewer:** run the scripts and report visual checks as unverified.
- **Engine claims:** verify the installed engine version and test a minimal scene; do not rely on remembered settings.
