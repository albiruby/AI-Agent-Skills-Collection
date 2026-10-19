---
name: game-qa-playtesting
description: QA and playtesting for games: test plans, automated tests, bug triage, balance/telemetry analysis, compatibility and soak tests, playtest protocols, release gates and certification readiness.
---

# QA & Playtesting

## Test layers
1. **Unit/logic tests** for simulation code (damage formulas, economy, save migration, quest state) - engine-independent when possible.
2. **Integration/automation**: headless runs, scripted bot playthroughs, smoke test per build (boot -> menu -> level -> quit), screenshot/golden-image tests, perf benchmarks in CI.
3. **Manual QA**: functionality, content, regression, edge cases (pause/resume, alt-tab, low battery, interrupts/calls, offline, time change, storage full, controller hot-plug, language switch).
4. **Compatibility**: device/OS/browser matrix (16), resolutions/aspects, input devices.
5. **Soak/stress**: 2-8 hour idle/loop for leaks; max entities; save/load hundreds of times.
6. **Network** (14): latency/loss/jitter, disconnect/reconnect, host migration, desync detection.
7. **Localization/accessibility QA** (20): text overflow, fonts, RTL, subtitles, colorblind modes.
8. **Security**: tamper tests on saves/IAP/leaderboards, API abuse.

## Playtesting protocol
- Test early with greybox; 5 players reveal most usability issues; observe silently, think-aloud, don't explain.
- Collect: time to first fun, drop-off points, deaths heatmap, confusion points, post-session survey (fun, clarity, difficulty, "would you play again").
- Telemetry events: level_start/complete/fail, death_position, tutorial_step, purchase, session_length, FPS/device.

## Bug management
Severity (S1 crash/data loss, S2 blocker, S3 major, S4 minor, S5 polish), priority, repro steps template (build, platform, steps, expected, actual, attachments/logs), triage cadence, regression suite, known-issues list.

## Release gates
No S1/S2 open, crash-free sessions target (e.g. >99%), perf targets met, store/platform checklist done (19), legal/privacy done (20), save compatibility between versions verified.

## Output
Test plan, test case sheet, automation plan, playtest script + survey, telemetry spec, bug template, release checklist.
