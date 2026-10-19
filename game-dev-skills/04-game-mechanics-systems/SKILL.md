---
name: game-mechanics-systems
description: Design game mechanics and systems: core loop, rules, progression, economy, combat, crafting, skill trees, difficulty, balancing, feedback/juice. Use for any "how does the game work / feel" question.
---

# Game Mechanics & Systems Design

## Building blocks
- **Verbs**: the 3-6 things the player does (move, jump, shoot, build, trade). Each verb needs: input, rule, feedback, consequence.
- **Resources & sinks/sources**: map every currency/resource (soft, hard, energy, XP, materials). Every source needs a sink; draw an economy flow diagram.
- **Progression**: power (stats/gear), knowledge (skill), content (unlocks), narrative. Choose curves: linear, exponential, logistic/S-curve, diminishing returns; define level cap and time-to-level targets.
- **Combat**: real-time/turn-based/ATB/tactical; hit detection, damage formula, status effects, cooldowns, resource costs, counters (rock-paper-scissors), TTK targets, telegraphs.
- **Crafting/building/survival**: recipes graph, gathering loops, hunger/stamina, base building rules.
- **Difficulty**: static tiers, dynamic difficulty adjustment (DDA), assist modes, fail states (checkpoints, roguelike permadeath, soft fail).
- **Meta systems**: gacha/loot tables (pity timers, disclosed odds), daily quests, achievements, collections, social, seasons.
- **Randomness**: input vs output randomness; seeded RNG; bad-luck protection.

## Balance workflow
1. Put all numbers in data files (see 03).
2. Define target metrics (TTK, session length, win rate band, currency per hour).
3. Simulate in a spreadsheet/script (Monte Carlo) before implementing.
4. Playtest, log telemetry, adjust in small steps; keep a changelog of balance.

## Juice / game feel checklist
Anticipation, hit-stop, screen shake (configurable), squash & stretch, particles, sound on every action, input buffering, coyote time, easing, camera lag/lookahead, haptics, UI feedback <100 ms.

## Output
Verb table, loop diagram, economy flow (Mermaid), formulas with example numbers, data schema, balance targets, and tuning knobs list.
