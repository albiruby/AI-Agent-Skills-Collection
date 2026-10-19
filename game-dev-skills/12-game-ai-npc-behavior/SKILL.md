---
name: game-ai-npc-behavior
description: Design and implement game AI: enemies, NPCs, companions, pathfinding, perception, state machines, behavior trees, GOAP, utility AI, steering, crowd, difficulty tuning; also LLM-driven NPCs safely.
---

# Game AI & NPC Behavior

## Choose the technique
| Need | Use |
|---|---|
| Simple enemies, UI/animation states | Finite State Machine / hierarchical FSM |
| Modular, designer-readable behaviors | Behavior Tree |
| Emergent goal planning | GOAP / HTN |
| Many weighted options (sims, RTS, shooters) | Utility AI |
| Board/card/turn-based | Minimax/alpha-beta, MCTS, heuristics |
| Crowds/flocks | Boids, steering, RVO/ORCA |
| Learning-based opponents | RL / imitation (offline, ship as small model or tuned params) |

## Components
- **Perception**: vision cone + line-of-sight, hearing radius, memory with decay, alert levels (idle -> suspicious -> search -> chase).
- **Navigation**: A* on grid/navmesh/waypoint graph, jump-point search, flow fields for many units, dynamic obstacles, path smoothing, stuck recovery.
- **Decision cadence**: tick AI at 5-10 Hz, stagger across frames, LOD for distant agents.
- **Combat AI**: attack tokens (limit simultaneous attackers), telegraphs, flanking roles, cover use, retreat/heal, boss phase scripts.
- **Companions/NPC life**: schedules, needs, idle barks, relationships.
- **Fairness**: avoid superhuman aim/reaction (add reaction delay, error), rubber-banding only if transparent, difficulty via parameters not cheating where possible.
- **LLM NPCs** (optional): sandbox with persona + knowledge constraints, content filtering, latency fallback to scripted lines, cost caps, no gameplay-critical logic delegated to the model, offline fallback.

## Debug tooling
Draw gizmos for vision/paths/states, AI log panel, replay of decisions, deterministic seeds.

## Output
Behavior spec per enemy/NPC type (states, transitions, params), nav plan, perception parameters table, performance budget (agents x ms), debug tools list, implementation outline per engine.
