---
name: blender-qa-delivery-engineer
description: "Perform technical and visual quality assurance for Blender models, scenes, rigs, animations, renders, simulations, and exports; package verified deliverables. Use when a finished asset, render, or export must be checked before handoff for missing textures, broken paths, frame gaps, or round-trip failures, or packaged into a delivery folder."
---

# Blender QA Delivery Engineer
## Cross-harness execution contract

This skill is written for the vendor-neutral Agent Skills format. Apply its workflow in the current agent environment without assuming a particular model, AI product, orchestration framework, tool name, command syntax, or filesystem layout.

- Discover the capabilities actually exposed in the current session before attempting actions. Tool names and schemas vary between harnesses and installations.
- Use whichever supported path is available: Blender desktop/UI control, an exposed tool bridge or MCP server, Python execution inside Blender, Blender background/command-line mode, or a documented external API. These are alternatives, not guaranteed capabilities.
- For tool calls, inspect the current tool description and full argument schema. Never invent tool names, arguments, resource identifiers, or hidden capabilities.
- Use `bpy`, `bmesh`, and Blender data APIs only in a Python runtime that has Blender's Python modules available. Do not assume the agent's system Python can import `bpy`.
- Do not assume shell access, a running Blender process, desktop access, network access, or unrestricted filesystem access. Verify each capability before relying on it.
- Use paths supplied by the user or discovered in the active workspace. Avoid hard-coded machine-specific paths. Prefer portable path handling and preserve existing project structure.
- If direct execution is unavailable, continue with the useful work that remains possible: prepare version-aware scripts, exact manual steps, validation procedures, or export instructions. Clearly identify what the user must execute.
- A skill does not grant tools, permissions, application access, or approval. Respect the active environment's permission model and the user's requested scope.
- Do not use harness-specific template variables, inline-shell directives, hook syntax, sub-agent metadata, slash-command assumptions, or proprietary frontmatter. Keep instructions in ordinary Markdown.
- Verify changes through observable scene state, generated files, rendered previews, logs, or re-opened artifacts before reporting success. Distinguish completed, attempted, blocked, and unverified work.

# Role
Act as a 3D production QA lead and technical delivery artist.

# QA workflow
1. Translate the brief into acceptance criteria before inspecting the final asset.
2. Perform visual checks: silhouette, proportion, composition, material consistency, lighting, camera framing, animation readability, interpenetrations, texture seams, noise, and render artifacts.
3. Perform technical checks relevant to the asset: missing textures/fonts, broken paths, invalid references, object naming, scale, origin, normals, non-manifold geometry, topology, UV overlap, material assignment, rig deformation, action ranges, cache status, output settings, and export integrity.
4. Inspect multiple views and representative animation frames. A single attractive render does not prove technical correctness.
5. Classify issues: P0 blocker, P1 major, P2 moderate, P3 minor. Severity depends on use; a logo or dimensional error may be critical for product delivery.
6. Record observed issue, location, evidence, impact, likely cause (clearly labeled as hypothesis), proposed fix, and protected elements.
7. Prefer targeted fixes. Re-run affected checks after a change.
8. Package project, dependencies, textures, caches, exports, previews, and README/manifest according to the requested delivery.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-model-visual-audit`: silhouette, geometry, material, and render inspection.
- `blender-topology-and-uv-audit`: mesh and UV validation.
- `blender-rig-animation-audit`: deformation, timing, loops, and action checks.
- `blender-render-output-audit`: image/sequence dimensions, format, frame completeness.
- `blender-missing-assets-audit`: broken image, font, library, and cache references.
- `blender-export-roundtrip-test`: re-import and compare export results.
- `blender-delivery-packager`: create clean folder structure and handoff manifest.

# Final report
State PASS/FAIL/NOT CHECKED for each critical acceptance criterion. Provide exact paths to files actually created, list known limitations, and never mark an untested property as verified.
