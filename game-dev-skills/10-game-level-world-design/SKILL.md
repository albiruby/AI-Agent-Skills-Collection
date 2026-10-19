---
name: game-level-world-design
description: Design levels, maps and worlds: structure, pacing, difficulty curve, tutorial levels, open world vs linear vs hub, level metrics, blockout workflow, tilemap/level tooling.
---

# Level & World Design

## Structure choices
Linear, hub-and-spoke, branching, open world, metroidvania graph, roguelike room-based, arena, endless/procedural (see 21), sandbox/chunked world, instanced missions.

## Workflow
1. **Level goals**: what skill/idea does this level teach or test? One new idea per level; introduce -> develop -> twist -> conclude (4-beat).
2. **Metrics**: jump height/distance, run speed, camera FOV, corridor width, enemy sight ranges. Build a metrics sheet and keep all levels within it.
3. **Blockout/greybox** first; playtest before art. Use tiles/modular kits.
4. **Pacing**: tension/release graph, rest points, checkpoints, save rooms, resource placement.
5. **Teach through level design**: safe-space practice, readable affordances, leading lines, light/colour guidance, no text-wall.
6. **Difficulty curve**: sawtooth (rise, ease, rise higher); optional hard content; secrets and collectibles for explorers.
7. **Navigation**: landmarks, minimap/compass, fast travel, signposting; avoid dead-ends without reward.
8. **Encounters**: enemy composition tables, spawn waves, arena rules, boss phases (3 phases, clear tells, vulnerability windows).
9. **Streaming/optimization**: chunking, occlusion, LOD, sublevels/addressables, loading zones hidden in corridors/elevators.

## Tools
Tiled, LDtk, Godot TileMap/GridMap, Unity Tilemap/ProBuilder, Unreal level streaming/World Partition, Blender/Trenchbroom/Hammer for brush levels. Store levels as data (JSON/TMX) for diffing and agent-editing.

## Output
Level list with goals, metrics sheet, difficulty graph, per-level beat sheet, encounter tables, tooling choice, validation checklist (reachability, softlocks, sequence breaks).
