# Cross-Harness Portability Guide

This pack uses the file-based Agent Skills convention: each skill is a directory containing `SKILL.md` with YAML frontmatter (`name`, `description`) and Markdown instructions.

## Common skill directories

| Harness | Common location |
|---|---|
| OpenCode | `~/.config/opencode/skills/` or `.opencode/skills/` |
| Claude Code | `~/.claude/skills/` or `.claude/skills/` |
| Codex / universal | `~/.agents/skills/` or `.agents/skills/` |
| Gemini CLI | documented skills directory (verify version) |
| Cursor | `.agents/skills/` or `.cursor/skills/` |
| GitHub Copilot | documented skills directory |
| Other agents | Use the configured skill source |

Paths and discovery rules change; verify the current official documentation.

## Install

```bash
bash ./install.sh <destination>
```

```powershell
.\install.ps1 -Destination "<destination>"
```

The installers copy the 26 skill folders. For the complete pack with shared references/templates, copy the whole `pixel-master/` folder into a skill source that scans nested `SKILL.md` files (OpenCode supports this).

## Shared resources

- `shared/PIXEL_ART_STANDARDS.md` is the canonical studio standard.
- `references/` contains deeper guides.
- `templates/` contains production briefs/specs.
- `scripts/` contains QA/palette/validation tools.

Every skill includes a compact non-negotiable standards block, so it remains usable when installed alone. The full shared files add depth but are optional for standalone installs.

## Tool portability

The skills are tool-agnostic, but execution depends on the harness. Pixel editors, image generation, Blender, game engines, file access, shell, and MCP tools must be provided separately. Installing a skill does not grant software access or permissions.

If a tool is unavailable, the agent should produce an actionable specification, script, prompt, or manual procedure and clearly state that the operation was not executed.
