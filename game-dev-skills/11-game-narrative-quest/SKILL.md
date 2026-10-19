---
name: game-narrative-quest
description: Create game story, lore, characters, dialogue, branching narrative and quest systems, including data formats and tools (Ink, Yarn Spinner, Twine, Dialogic). Use for story-driven or quest-driven games.
---

# Narrative & Quest Design

## Layers
1. **Premise & theme** (one-line moral/question), **setting bible** (history, factions, geography, rules of magic/tech, cultural sources - research respectfully).
2. **Characters**: protagonist (want vs need, flaw, arc), antagonist, companions, NPC roles; voice sheet (speech patterns), design hooks for visuals.
3. **Structure**: 3-act, hero's journey, kishotenketsu, episodic, environmental storytelling, emergent narrative.
4. **Delivery**: cutscenes, dialogue, barks, codex/lore items, environment, audio logs, UI text. Match delivery to genre (don't stop action games for long cutscenes; make cutscenes skippable).
5. **Branching**: state variables/flags, choice consequences (show them!), bottleneck/diamond structure to control scope, reactivity tracking sheet.
6. **Quests**: main/side/repeatable/daily; quest types (fetch, kill, escort, investigate, puzzle, delivery) disguised with story; objective states (inactive/active/complete/failed), prerequisites, rewards, journal text, map markers.
7. **Dialogue systems**: node graph, conditions, variables, localization keys, voice cue IDs, portraits/emotion tags.

## Tech
Ink (inkle), Yarn Spinner, Twine/Twee, Dialogic/Dialogue Manager (Godot), Articy:draft, custom JSON. Keep text in string tables (no hardcoding) for localization (20).

## Output
Story bible, character sheets, quest table (ID, giver, objectives, conditions, rewards, text keys), dialogue script sample in chosen format, flag/variable list, localization-ready string table.
