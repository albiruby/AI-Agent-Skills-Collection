---
name: game-ui-ux-hud
description: Design game UI/UX: menus, HUD, onboarding/tutorial, inventory, shops, settings, screen flow, responsive layouts for touch/gamepad/keyboard, and UI implementation guidance per engine.
---

# Game UI/UX & HUD

## Screen inventory
Splash, Main Menu, Mode/Level select, Character/Loadout, Gameplay HUD, Pause, Inventory/Equipment, Map, Quest log, Shop/Store, Crafting, Social/Friends, Leaderboard, Settings (video/audio/controls/accessibility/language), Results/Game Over, Credits, Legal/Privacy/Consent, Error/Offline dialogs, Loading.
Output a **screen flow diagram (Mermaid)** with transitions and entry conditions.

## HUD principles
- Show only what the decision needs; diegetic > spatial > meta > non-diegetic when it fits the theme.
- Safe zones (notch/cutouts, TV overscan), anchor to corners, scale with DPI.
- Information hierarchy: health/ammo/objective primary; secondary on demand; fade when idle.
- Readability: min text size (mobile >= 14-16 sp equivalent; TV >= 28 px at 1080p), contrast, icons + text, color not sole signal.

## Input-aware UI
- **Touch**: thumb zones, >=44-48 dp targets, virtual stick/dynamic stick, gesture alternatives, no tiny close buttons.
- **Gamepad**: focus navigation, button glyphs switching by device, no mouse-only UI.
- **KB/M**: hotkeys, tooltips, rebind. **VR**: world-space UI, comfortable distance (~1-2 m), laser pointer/hand-ray.

## Onboarding
Teach by doing; one concept at a time; skippable; re-readable help; contextual hints; first 3 minutes = fun before text. FTUE metrics: completion rate, time to first win.

## Juice & feedback
Button states (hover/press/disabled), transitions 150-300 ms, SFX per interaction, haptics, number popups, screen-reader labels where supported.

## Implementation
Unity UI Toolkit/uGUI, Unreal UMG/Slate, Godot Control nodes/themes, web DOM+CSS overlay or canvas UI (use DOM for text/accessibility). Use a theme/style file, layout containers, and an event bus; never hardcode positions in pixels for multi-aspect support (test 16:9, 19.5:9, 4:3, ultrawide).

## Output
Screen list, wireframes (ASCII/Mermaid), HUD spec, UI style guide tied to 06, tutorial script, accessibility notes, implementation notes.
