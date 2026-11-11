# Cross-Harness Portability Guide

## What is portable

This suite uses the open Agent Skills shape:

```text
skill-name/
└── SKILL.md
```

Each `SKILL.md` starts with standard YAML frontmatter containing only the two broadly interoperable required fields, `name` and `description`, followed by ordinary Markdown instructions. No vendor-specific hooks, tool allowlists, inline shell injection, context-fork directives, template variables, slash-command syntax, or proprietary frontmatter are required.

This keeps the **skill content** portable. It does not make every AI product automatically discover a local folder: each harness has its own discovery path, permissions, tools, and invocation behavior. Use the documented path for the exact product and version installed.

## Common installation locations

The paths below are common documented locations for file-based agent skills. Use project scope for repository-specific workflows and user scope for personal skills shared across projects. Confirm the current product documentation because locations and support can change.

| Harness | Project-level skill root | User-level skill root | Notes |
|---|---|---|---|
| Codex CLI | `.agents/skills/` | `~/.agents/skills/` | Uses the standard Agent Skills folder format. |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` | Agent Skills discovery; use its skills command to verify. |
| OpenCode | `.agents/skills/`, `.opencode/skills/`, or `.claude/skills/` | `~/.agents/skills/`, `~/.config/opencode/skills/`, or `~/.claude/skills/` | Supports several compatible discovery paths. |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Skills are directory-based with `SKILL.md`. |
| Cursor | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` | Also recognizes some Claude/Codex-compatible locations. |
| GitHub Copilot | `.agents/skills/`, `.github/skills/`, or `.claude/skills/` | `~/.agents/skills/` or `~/.copilot/skills/` | Exact support depends on Copilot surface and version. |
| Hermes Agent | Configured skills directory (often under the user's Hermes directory) | Configured skills directory | Supports `SKILL.md`; use the active Hermes configuration/docs to confirm the actual path. |
| Other harnesses | Use the path documented by that harness | Use the path documented by that harness | If native Agent Skills discovery is absent, provide the instructions as project context or an imported prompt/rule. |

## Recommended strategy

1. **For a multi-agent repository:** install once into `.agents/skills/` when every target agent in your setup recognizes it.
2. **For Claude Code-only projects:** use `.claude/skills/`.
3. **For OpenCode-only projects:** `.opencode/skills/` is native; the compatible `.agents/skills/` path is also supported.
4. **For Cursor-only projects:** `.cursor/skills/` is native; `.agents/skills/` is also supported.
5. **For Hermes:** use its configured skill root. Do not assume a path if the installation has customized it.
6. Avoid copying the same skill into multiple directories that one harness scans simultaneously unless you intentionally want override behavior. Duplicate skill IDs can create ambiguity or precedence issues.

## Installation with the included scripts

The scripts accept a **destination skill root** instead of guessing which harness is running.

macOS/Linux/WSL:

```bash
bash ./install.sh .agents/skills
```

Claude Code project:

```bash
bash ./install.sh .claude/skills
```

OpenCode project:

```bash
bash ./install.sh .opencode/skills
```

Cursor project:

```bash
bash ./install.sh .cursor/skills
```

GitHub Copilot project:

```bash
bash ./install.sh .github/skills
```

Windows PowerShell:

```powershell
.\install.ps1 -Destination ".agents\skills"
```

To install globally, pass the actual user-level skill path for the chosen harness. On Windows, use the path specified by that product rather than assuming a Unix-style home directory.

## Harness differences that remain

Even with standard `SKILL.md` content, the following are harness-specific and must not be assumed:

- Skill discovery directories and search precedence.
- Automatic activation versus explicit loading.
- Skill invocation syntax or UI.
- Whether subagents, parallel agents, or delegated tasks exist.
- Tool names, parameters, permissions, and result formats.
- Shell access, desktop control, filesystem scope, and Python execution.
- Whether a skill's supporting files are exposed automatically or must be read explicitly.
- Whether skills are enabled in cloud, remote, or sandbox sessions.

The skills therefore instruct the agent to discover its active capabilities before acting. If a harness supports only imported instructions or project rules, use the relevant `SKILL.md` body through that supported mechanism; native discovery is not guaranteed on products that do not implement Agent Skills.

## Blender execution compatibility

The production skills support multiple execution routes but do not require all of them:

- **Blender UI:** suitable when desktop/application control is exposed.
- **Blender Python:** suitable when the Python process runs within Blender or has a compatible Blender module installation.
- **Background/CLI:** suitable when a local Blender executable and command execution are available and authorized.
- **MCP/tool bridge:** suitable when a documented Blender integration is exposed.
- **Manual handoff:** generate a script, exact UI steps, or validation checklist when none of the direct execution routes is available.

Do not run `bpy` scripts in a plain Python interpreter unless Blender's Python modules are confirmed available. Do not assume that a tool bridge is MCP, and do not assume every bridge supports rendering, saving, exporting, or file inspection.

## References

- Agent Skills specification: https://agentskills.io/
- OpenAI Skills guide: https://developers.openai.com/api/docs/guides/tools-skills
- Gemini CLI skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Hermes skill creation: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
- OpenCode skills: https://opencode.ai/docs/skills
- Claude Code skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Cursor skills: https://cursor.com/docs/skills
- GitHub Copilot skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
