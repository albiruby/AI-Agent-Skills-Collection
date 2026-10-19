---
name: game-tech-stack-architect
description: Design the full technical stack and software architecture of a game: engine, languages, ECS/OOP pattern, state management, save system, data-driven design, backend, tools, CI/CD, repo structure. Use after engine selection.
---

# Game Tech Stack & Architecture

## Layers to decide
1. **Runtime**: engine/framework, language, render pipeline (2D sprite, URP/HDRP, Forward+/Mobile/Compatibility, WebGL2/WebGPU).
2. **Architecture pattern**: scene/component (Unity/Godot), ECS (Bevy, DOTS, bitECS), state machines, event bus/signals, service locator/DI (use sparingly), command pattern (undo/replay/input buffering).
3. **Game loop**: fixed timestep for physics/sim, variable for render, interpolation; deterministic sim if replay/netcode needed.
4. **Data-driven design**: balance, items, enemies, levels in JSON/CSV/ScriptableObjects/Resources/YAML; hot-reload; schema validation; never hardcode numbers.
5. **Save/Load**: versioned schema, migrations, atomic writes, cloud save (Steam Cloud, Play Games, iCloud, custom), corruption recovery, encryption only if needed.
6. **Scene/State flow**: Boot -> Splash -> Main Menu -> Loading -> Gameplay -> Pause -> Results; async loading; additive scenes.
7. **Asset management**: addressables/resource packs, streaming, pooling, atlases.
8. **Backend (if needed)**: auth, leaderboards, cloud save, matchmaking, IAP validation, remote config, analytics, push. Options: PlayFab, Nakama, Firebase/Supabase, Unity Gaming Services, Steamworks, GameAnalytics, custom (Node/Go + Postgres/Redis).
9. **Tooling**: Git + Git LFS (or Perforce/Plastic for big binary projects), `.gitignore` per engine, linting, formatters, unit tests, CI (GitHub Actions/GitLab) building per platform, automated store upload (fastlane, Steamcmd, butler for itch.io).
10. **Observability**: logging, crash reporting (Sentry, Crashlytics), analytics events.

## Reference repo layout (adapt)
```
/game
  /src (or /Assets/Scripts)   code by feature: core, gameplay, ui, audio, net, tools
  /data                        balance + content (JSON/CSV)
  /assets                      raw -> /assets_export (engine-ready)
  /docs                        GDD, architecture decisions (ADR)
  /tests, /ci, /build
```

## Principles
- Separate **simulation** from **presentation** (testable logic, easy porting).
- Composition over inheritance; avoid global singletons for state; pool anything spawned frequently.
- One source of truth for config; feature flags for risky features.
- Record each major choice as an ADR (context, options, decision, consequences).

## Output
Stack table (layer -> choice -> alternative -> why), architecture diagram (Mermaid), repo layout, risks, and the minimum "walking skeleton" (boot -> menu -> game -> save) to build first.
