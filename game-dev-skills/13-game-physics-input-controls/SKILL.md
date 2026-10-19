---
name: game-physics-input-controls
description: Specify physics, collision, character controllers, camera, and input systems across keyboard/mouse, gamepad, touch, VR and accessibility rebinding; covers game feel tuning parameters.
---

# Physics, Controls & Input

## Physics
- Choose: kinematic custom controller (platformers; precise, deterministic) vs rigid-body engine (Box2D/Rapier/PhysX/Havok/Jolt/Chipmunk). Fixed timestep (e.g. 50-60 Hz), continuous collision for fast objects, layers/masks matrix, triggers vs colliders, one-way platforms, slopes/stairs handling.
- Determinism needs (replays, rollback netcode): fixed-point or deterministic engine, seeded RNG, no frame-time dependence.
- Common tuned parameters: gravity, jump velocity/height, variable jump cut, coyote time (~80-120 ms), input buffer (~100-150 ms), acceleration/deceleration, air control, max fall speed, dash/dodge i-frames.

## Camera
2D: follow with deadzone, lookahead, room-lock, pixel-snap, screen shake. 3D: orbit/third-person (collision, auto-recenter), first-person (FOV, head-bob toggles, motion-sickness options), cinematic dolly; avoid camera cutting through geometry.

## Input architecture
- **Action mapping layer** (jump, fire, move) separated from devices; Unity Input System, Godot InputMap, Unreal Enhanced Input, web: Gamepad API + pointer/keyboard events.
- Rebinding UI + save bindings; per-device glyphs; hold/toggle options; deadzones, sensitivity curves; aim assist; dual-stick shooting; hot-plugging; simultaneous devices.
- **Touch**: virtual joystick (fixed/floating), tap/swipe/pinch/drag, multi-touch, large hit areas, avoid thumb occlusion, optional auto-fire/auto-aim, haptics; orientation lock choice.
- **VR**: locomotion (teleport/smooth/snap-turn), hand presence, grab physics, comfort vignette.
- Accessibility: one-handed schemes, remappable everything, adjustable timing, no QTE-only mechanics (see 20).

## Output
Controls scheme table per device, action map list, physics config values with rationale, camera spec, tuning knobs list, test checklist (tunneling, stuck, jitter, input latency).
