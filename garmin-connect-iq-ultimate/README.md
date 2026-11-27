# Garmin Connect IQ Ultimate (120 Sub-Skills)

A deep, modular Garmin Connect IQ skill pack for Monkey C development across watch faces, data fields, widgets/glances, device apps, sensors, background services, memory, localization, testing, and store release.

This pack complements the broader `garmin-connect-iq-development` skill:

- Use the broad skill for end-to-end project workflow, architecture, UI system, and general engineering standards.
- Use this pack for advanced, topic-specific implementation guidance when a task needs exact lifecycle, rendering, sensor, memory, or release details.

## Module map

| Prefix | Modules | Coverage |
|---|---:|---|
| `wf` | 001-025 | Watch faces: lifecycle, MIP/AMOLED, AOD/burn-in, buffered bitmaps, hands, gauges, complications, on-device settings |
| `df` | 026-040+ | Data fields: simple/custom, compute vs onUpdate, layout tiers, timers, laps, zones, pace/power/NP/TSS |
| `app` | 14 | App structure, views, delegates, navigation, input, phone/cloud integration |
| `sensor` / `ant` / `ble` / `bio` | 15 | Sensor APIs, ANT+/BLE profiles, heart rate, biometrics |
| `fit` | 5 | FIT contributors, recording, session/activity data |
| `mem` | 6 | Memory, heap, object pools, leaks, profiling |
| `ui` | 5 | Adaptive UI, geometry, typography, contrast, accessibility |
| `bg` | 4 | Background services, scheduling, resource limits |
| `audio` / `wth` | 3 | Audio content and weather integrations |
| `stg` / `loc` / `jgl` / `cpl` | 7 | Storage, localization, jungle routing, strict types/API guards |
| `tst` / `rel` | 3 | Unit tests, heap profiler, store export |

The exact catalog is in `SKILL.md` and `references/001-...` through `references/120-...`.

## Usage

```text
@garmin-connect-iq-ultimate
```

Or directly ask for a topic, for example:

- "Implement a MIP 1Hz partial-update watch face with clipping regions."
- "Build an adaptive data field that supports 1 to 8 fields."
- "Add AMOLED burn-in protection and pixel shifting."
- "Audit memory use and propose a BufferedBitmap cache strategy."
- "Prepare a signed .iq store release and verify manifest compatibility."

## Structure

```text
garmin-connect-iq-ultimate/
  SKILL.md
  README.md
  references/001-... through 120-...
  scripts/
  assets/
```

## Grounding rules

- Verify device support, API levels, permissions, and SDK behavior against the project manifest and current Garmin documentation.
- Do not claim a feature, device, or store requirement without evidence.
- Keep raw simulator captures separate from clean store assets.
- Store requirements change; check current official guidance or mark compliance unverified.

## Related

- Broad Garmin skill: `garmin-connect-iq-development`
- Project documentation and store visuals: `project-docs-orchestrator`, `clean-screenshot-slicer`, `store-preview-asset-builder`
