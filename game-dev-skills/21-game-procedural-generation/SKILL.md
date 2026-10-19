---
name: game-procedural-generation
description: Procedural content generation (PCG): dungeons, terrain, levels, loot, quests, names, textures, music; algorithms (noise, WFC, BSP, cellular automata, L-systems, graph grammars), seeds, validation and design control.
---

# Procedural Generation

## When to use
Replayability, huge content needs with small team, roguelikes, survival worlds, endless modes. Avoid when authored experience/pacing matters most; hybridize (hand-made rooms/set-pieces + procedural assembly).

## Algorithms by need
| Output | Techniques |
|---|---|
| Terrain/heightmaps | Perlin/Simplex/Worley noise, fBm/ridged, domain warping, hydraulic erosion, biome via temperature/moisture maps, Voronoi regions |
| Caves/organic maps | Cellular automata, drunkard's walk |
| Dungeons/rooms | BSP, room-and-corridor, graph-based (lock-and-key), grammar-driven, Spelunky-style template chunks |
| Tile/level coherence | Wave Function Collapse, Markov chains, constraint solving |
| Plants/cities | L-systems, road networks (tensor fields), lot subdivision |
| Items/loot/enemies | Weighted tables, affix systems, budget-based generation, rarity tiers |
| Quests/stories | Template + grammar, graph rewriting, state-based |
| Names/text | Markov, syllable grammars |
| Audio | Generative sequencing, Tone.js/Pure Data |
| Textures/materials | Noise-based shaders, substance-like graphs |

## Must-haves
- **Seeded RNG** (deterministic per seed; share seeds; separate RNG streams for level/loot/events).
- **Validators**: reachability (flood fill), critical path exists, no softlocks, difficulty/economy bounds, retry on invalid.
- **Designer control**: parameters, constraints, curated chunk libraries, "fun budget" (enemies per area, rest rooms), preview tool.
- **Performance**: chunk/stream generation, background threads/jobs, caching, pooling.
- **Testing**: generate 10,000 seeds in CI and assert invariants; collect statistics.

## Output
PCG design doc (inputs, algorithm, validator rules), pseudocode, parameter table, seed strategy, test harness plan.
