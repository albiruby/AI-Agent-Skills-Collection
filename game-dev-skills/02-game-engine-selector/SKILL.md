---
name: game-engine-selector
description: Choose the right game engine or framework (Unity, Unreal, Godot, GameMaker, Defold, Phaser, PixiJS, Three.js, Babylon.js, PlayCanvas, Bevy, LOVE2D, MonoGame, Cocos, Construct, RPG Maker, Roblox, Flame, Raylib, etc.) based on genre, platform, team and budget. Produces a scored decision matrix.
---

# Game Engine Selector

## Method
1. Read PROJECT_BRIEF (genre, dimension, platforms, team skill, budget, timeline).
2. Apply **hard filters** (platform support, language the team knows, license/cost model, 2D vs 3D).
3. Score remaining candidates 1-5 on: Fit-to-genre, Platform reach, Learning curve, Tooling/editor, Asset-store/community, Performance, Licensing/cost, Agent-friendliness (text-based project files, scriptable, CLI build).
4. Recommend 1 primary + 1 fallback with rationale. State migration risk.
5. Remind user to verify current license terms/versions.

## Landscape (knowledge base)
**Full editors**
- **Unity** (C#): 2D/3D/mobile/VR/AR; biggest asset store & mobile ecosystem; URP/HDRP, DOTS/ECS, Addressables; check current runtime/licensing terms.
- **Unreal Engine** (C++/Blueprints): AAA 3D, Nanite/Lumen, MetaHuman, strong for FPS/third-person/cinematic; heavy; weaker for small mobile/2D; check royalty terms.
- **Godot** (GDScript/C#/C++ via GDExtension): MIT, light, excellent 2D, good 3D, text-based scenes (`.tscn`) = very agent-friendly; export to desktop/mobile/web; console via third-party.
- **GameMaker** (GML): 2D, fast prototyping, strong for pixel-art/arcade/RPG, console exports commercial tiers.
- **Defold** (Lua): tiny builds, great web/mobile 2D, free/source-available.
- **Cocos Creator** (TypeScript): 2D/light 3D, strong in Asia mobile/mini-games/WeChat.
- **Construct** (visual, browser): no-code 2D web/mobile.
- **RPG Maker**: JRPG-style 2D RPGs, plugin ecosystem.
- **Stride, Flax, O3DE, Wicked**: niche/advanced 3D (C#/C++).
- **Roblox Studio** (Luau), **Fortnite UEFN** (Verse), **Core**, **Minecraft add-ons/mods**: platform-hosted UGC games.

**Code-first frameworks**
- **Web (JS/TS)**: Phaser (2D), PixiJS (2D renderer), Three.js / Babylon.js / PlayCanvas (3D), Excalibur, Kaboom/Kaplay, melonJS, Matter.js/Rapier (physics), Howler/Tone (audio).
- **Rust**: Bevy (ECS), Macroquad, Fyrox, ggez.
- **C/C++/others**: Raylib, SDL3, SFML, sokol, Cinder; **C#**: MonoGame, FNA, Stride; **Python**: Pygame, Arcade, Ursina; **Lua**: LOVE2D, Solar2D; **Dart**: Flame (Flutter); **Kotlin**: libGDX, KorGE; **Java**: libGDX; **Swift**: SpriteKit/SceneKit/RealityKit/Metal; **Haxe**: Heaps, HaxeFlixel, Kha; **Zig/Odin**: Raylib bindings.

## Default recommendations (adjust to brief)
| Situation | Pick |
|---|---|
| Solo/small 2D, any platform | Godot (or GameMaker if team knows GML) |
| 2D/3D mobile with monetization SDK needs | Unity |
| AAA-looking 3D, realistic, team with C++/BP | Unreal |
| Instant-play browser game, no install | Phaser / PixiJS / Three.js / Babylon / PlayCanvas |
| Tiny build size, HTML5 portals | Defold, Phaser, Construct |
| Learning / jam / code purists | LOVE2D, Pygame, Raylib, Kaplay |
| Large simulation/ECS, performance nerds | Bevy, Unity DOTS |
| Kids/social UGC | Roblox, UEFN |
| Flutter app with light game | Flame |
| Console-first indie | Unity / Unreal / Godot via porting partner / GameMaker |
| Multiplayer-heavy | Unity (Netcode/Mirror/Fish-Net/Photon), Unreal (built-in replication), Godot (high-level multiplayer), Colyseus/Nakama for web |

## Output
Decision matrix table, recommendation + fallback, project folder convention for the chosen engine, and a "first 10 steps" setup list.
