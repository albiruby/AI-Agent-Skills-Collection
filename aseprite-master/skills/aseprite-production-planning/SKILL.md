---
name: aseprite-production-planning
description: Converts a pixel-art or Aseprite request into a scoped, dependency-aware production plan with assumptions, checkpoints, and acceptance criteria. Use when a brief covers multi-step asset creation, animation, or batch generation and needs stages, dependencies, checkpoints, and acceptance criteria before work starts.
---

# Production Planning

## When to use
Use before multi-step asset creation, animation work, batch generation, or any task with multiple deliverables.

## Procedure
1. Rewrite the brief into concrete deliverables, not vague intentions.
2. Separate required outcomes from optional polish.
3. Identify constraints: canvas/frame dimensions, frame count, style, palette, timing, directions, engine, export, deadlines.
4. Identify dependencies: character design before animation; key poses before in-betweens; source file before export; QA before final handoff.
5. Divide work into small reversible stages.
6. Define an acceptance test for every deliverable.
7. Estimate uncertainty qualitatively (low/medium/high); do not invent precise duration estimates.
8. Decide when to request approval: major style change, destructive overwrite, scope expansion, or costly batch operation.

## Plan format
- Goal
- Deliverables
- Assumptions
- Tool capabilities confirmed
- Stages and checkpoints
- Risks / blockers
- Acceptance criteria
- Handoff contents

## Quality bar
A plan must be actionable by an agent, with each step tied to a real tool capability or a clearly labeled manual step. Avoid planning features the connected MCP server does not expose.
