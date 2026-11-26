# Cross-Harness Portability Guide

## Standard format
Each skill is a directory containing `SKILL.md` with this portable metadata shape:

```yaml
---
name: example-skill
description: "What it does and when to use it."
---

# Example Skill
...
```

The package does not use vendor-specific frontmatter keys, runtime code, tool names, or environment assumptions. It is designed for Agent Skills-compatible harnesses and systems that can load Markdown instruction folders.

## Common installation targets
Use the exact location documented by your product/version and your local configuration. Common supported conventions include:

| Agent / harness | Common skill directory |
|---|---|
| OpenAI Codex | `.agents/skills/` or `~/.agents/skills/` |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` (verify version/config) |
| OpenCode | `.agents/skills/`, `.opencode/skills/`, or configured global skill directory |
| Claude Code | `.claude/skills/` or `~/.claude/skills/` |
| Cursor | `.agents/skills/` or `.cursor/skills/` |
| GitHub Copilot | `.agents/skills/`, `.github/skills/`, or supported configured path |
| Hermes | configured skills directory for the installed version |

These paths and discovery behavior can change. Check the target product's current documentation before deployment; do not copy to multiple directories that the same harness scans unless you intentionally want duplicates.

## Install

```bash
bash ./install.sh .agents/skills
```

```powershell
.\install.ps1 -Destination ".agents\skills"
```

## What portability means—and does not mean
- **Portable instructions:** skill IDs, descriptions, and operating procedures do not depend on one AI vendor.
- **Not portable tool access:** Outlook, Graph, Power Automate, native Office UI, local filesystem, VBA runtime, and desktop control must be made available separately by the environment.
- **Not guaranteed identical behavior:** skill activation, discovery, context limits, and tool permission models differ across products.
- **No universal invocation command:** invoke by skill name or task description according to the harness's own interface.

## Recommended tool capability matrix

| Task | Useful capability |
|---|---|
| Create/edit DOCX/XLSX/PPTX offline | Filesystem plus appropriate Open XML-aware libraries |
| Preserve advanced Word/PowerPoint layout | Native Office app or high-fidelity renderer |
| Recalculate Excel formulas/pivots | Excel calculation engine or compatible verified engine |
| Run VBA | Desktop Office with macros permitted by policy |
| Run Office Scripts | Eligible Microsoft 365 Excel environment with Office Scripts enabled |
| Send/read Outlook mail or calendar | Authorized Outlook connector or Microsoft Graph permissions |
| Read/write OneNote | Authorized OneNote connector or Graph delegated permissions |
| Build/run Access database | Access/ACE runtime and suitable database access |
| Orchestrate cloud business processes | Power Automate or an approved workflow platform |

Never ask the agent to bypass enterprise policies, MFA, consent, DLP, or macro security to obtain access.
