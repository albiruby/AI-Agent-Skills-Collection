# Blender 3D Production Suite

A harness-neutral, modular skill library for professional Blender 3D production. The package contains **1 master orchestrator + 18 specialist skills**. Each skill uses the open Agent Skills file shape: a `SKILL.md` file with YAML frontmatter (`name`, `description`) followed by plain Markdown instructions.

The skills do not bind to Hermes, Claude Code, Codex, Gemini CLI, OpenCode, Cursor, GitHub Copilot, or another specific agent. They discover the tools available in the active environment and adapt to Blender UI control, Python execution inside Blender, background/CLI execution, MCP or another documented tool bridge, or a manual handoff when no direct execution tool is available.

## Package contents

- `skills/` — all independent skill folders.
- `SKILL-INDEX.md` — skill catalog and routing guidance.
- `PORTABILITY-GUIDE.md` — compatibility model and install locations for common harnesses.
- `install.sh` — portable shell installer that copies the complete skill set into a destination skill root.
- `install.ps1` — PowerShell installer for Windows.

## Skill inventory

| # | Skill | Responsibility |
|---:|---|---|
| 00 | `blender-3d-studio-director` | Master orchestration and end-to-end pipeline routing |
| 01 | `blender-concept-art-director` | Concept, references, visual development, shot plan |
| 02 | `blender-scene-project-pipeline` | Project setup, organization, file/dependency management |
| 03 | `blender-modeling-specialist` | Hard-surface, product, props, architecture, mesh modeling |
| 04 | `blender-sculpting-specialist` | Organic sculpting, anatomy, high-poly workflow |
| 05 | `blender-topology-retopology` | Topology, retopology, normals, mesh quality |
| 06 | `blender-uv-baking-specialist` | UVs, texel density, seams, texture baking |
| 07 | `blender-material-texturing-specialist` | PBR, shader nodes, texture painting, materials |
| 08 | `blender-geometry-nodes-specialist` | Procedural modeling, scattering, instancing, node systems |
| 09 | `blender-rigging-skinning-specialist` | Character, creature, prop, and mechanical rigs |
| 10 | `blender-animation-director` | Character, object, camera, motion graphics animation |
| 11 | `blender-simulation-fx-specialist` | Rigid body, cloth, fluids, particles, smoke, fire |
| 12 | `blender-environment-worldbuilder` | World building, terrain, architecture, foliage, sets |
| 13 | `blender-lighting-lookdev` | Camera, studio/cinematic lighting, look development |
| 14 | `blender-render-compositing` | Cycles/EEVEE, rendering, passes, compositor, color |
| 15 | `blender-python-automation-engineer` | `bpy`, `bmesh`, `mathutils`, scripts, add-ons, batch workflows |
| 16 | `blender-tool-interface-operator` | Harness-neutral Blender operation through discovered interfaces |
| 17 | `blender-asset-optimization-export` | Optimization, LODs, export, interchange, 3D print preparation |
| 18 | `blender-qa-delivery-engineer` | Technical/visual QA, artifact inspection, final handoff |

## Quick install

Choose the skill root that your agent actually scans, then install the package into that directory.

### macOS / Linux / WSL

```bash
bash ./install.sh /path/to/your/agent-skills-root
```

### Windows PowerShell

```powershell
.\install.ps1 -Destination "C:\path\to\your\agent-skills-root"
```

The installer copies every skill folder (the folder containing its `SKILL.md`) into the destination. It does not modify agent settings, configure tools, install Blender, install add-ons, or grant application permissions. It will not overwrite an existing skill unless the overwrite option is explicitly provided.

For example, the shared `.agents/skills/` directory is recognized by several Agent Skills-compatible environments. See `PORTABILITY-GUIDE.md` for the platform-specific locations and caveats.

## Use

- Use `blender-3d-studio-director` for a complete project.
- Load specialist skills for focused tasks when the active harness supports on-demand skill discovery.
- If the harness does not support a skill loader, open the relevant `SKILL.md` and provide its instruction body to the agent, or configure it as a project-level instruction using that harness's documented mechanism.
- A specialist skill can be used on its own; it does not require Hermes or the master skill.

## Tool and environment portability

The skills intentionally do not assume that the agent has any particular tool. The agent must discover what is actually available in its current environment and adapt:

1. Blender desktop/UI controls, if exposed.
2. Python execution inside Blender or a confirmed Blender Python runtime.
3. Blender background/CLI execution, if Blender's executable and shell access are available and authorized.
4. MCP or another supported tool bridge, if exposed.
5. Manual instructions or a ready-to-run script if direct execution is unavailable.

`bpy` is available only in Blender's Python environment or another environment that has Blender's Python modules correctly installed. The agent must not assume its system Python can import `bpy`.

## Critical production rules

- Discover Blender version and available capabilities before work.
- Verify version-sensitive APIs against documentation matching the installed Blender version.
- Discover actual tool schemas before using a tool bridge; never invent tool names or arguments.
- Preserve a recoverable source before destructive edits.
- Work in inspect → modify → validate → save → preview/export stages.
- Use previews before expensive final renders.
- Verify actual `.blend`, image, animation, cache, and export artifacts before reporting success.
- Never claim an operation or test was performed when it was not.

## Documentation

- Blender Manual: https://docs.blender.org/manual/en/latest/
- Blender Python API: https://docs.blender.org/api/current/
- Agent Skills format: https://agentskills.io/

The installed Blender version and its matching API documentation take precedence over assumptions in these skills.
