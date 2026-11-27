# Garmin Connect IQ Playbook

Platform-specific guidance for documenting Garmin Connect IQ apps and producing clean simulator captures and store previews. Verify current Garmin SDK/store requirements before submission; this is a workflow aid, not an official specification.

## 1. Identify the project type

| App type | Typical signals | Documentation focus |
|---|---|---|
| Watch face | `WatchFace` / watch-face manifest entry | Time rendering, AOD/burn-in behavior, complications, battery |
| Data field | Data field manifest entry, activity info | Metric calculation, FIT contribution, device compatibility |
| Widget / glance | Widget/glance entry | Glanceable states, interaction limits |
| Device app | App entry, views, delegates | Navigation, state, storage, sensors |
| Background service | Background/service entry | Scheduling, resource limits, battery |
| Audio/content provider | Provider entry | Content format, offline behavior |

Ground claims in `manifest.xml`, `monkey.jungle`, source, and tests. Do not infer supported devices from screenshots.

## 2. Documentation set

Minimum for a store-bound app:

- `README.md`: what it is, supported devices, install/build, features, clean preview, limitations.
- `docs/ARCHITECTURE.md`: app lifecycle, views, data flow, storage, sensors, battery considerations.
- `docs/DEVICES.md` or compatibility table: verified device families, display types, constraints.
- `docs/USER_GUIDE.md`: controls, settings, modes, permissions.
- `CHANGELOG.md` and release notes.
- Privacy/permissions explanation if the app uses sensors, location, or network.

For a small watch face, a concise README + screenshots + device list may be enough.

## 3. Screenshot types

Distinguish:

1. **Simulator evidence:** full simulator window, useful for development notes.
2. **Isolated watch render:** watch body/bezel/strap with screen, transparent background.
3. **Display-only capture:** active display only; for round screens preserve the circle, do not stretch to a square.
4. **Store composition:** genuine watch screenshot inside a designed banner with copy.

Do not deliver a raw simulator window as a store asset. Do not crop a full watch when the user asked for the display only.

## 4. Simulator capture

- Select the intended device family and resolution; store art benefits from a high-resolution model.
- Load realistic demo data; avoid empty `0`, debug overlays, and placeholder text.
- Remove tooltips, mouse cursor, notifications, and overlapping windows.
- Capture at native resolution; preserve the raw file.
- Record device, build, screen/state, and date.
- If simulator control is unavailable, provide exact manual capture steps and process user-supplied captures.

## 5. Cleaning and slicing

- Simulator chrome: title bar, menu bar, toolbar, memory/status bar.
- Canvas: often solid white or light gray; remove only the exterior connected background.
- Use edge-connected flood fill; never global white replacement (it destroys white UI/icons).
- Keep transparent padding consistent.
- Normalize sibling captures to the same height.
- Check corners alpha = 0; no white halo; no clipped bezel/strap.
- For display-only, crop inside the bezel and preserve round geometry.

Use `clean-screenshot-slicer` and its `garmin-sim` preset.

## 6. Store/preview assets

Typical Garmin Connect IQ placements (verify current store requirements):

- Cover/icon: square, device silhouette + title.
- Hero banner: wide, multi-device or single hero, value proposition.
- Feature screens: several slides showing modes/benefits.
- Lossless masters retained for edits.

Keep one palette and device framing across the set. Do not show unsupported devices or features. Do not imply Garmin endorsement.

## 7. Copy

- State the app type and core benefit in the first line.
- Use verified device families, modes, metrics, and permissions.
- Explain sensor/data usage plainly.
- Avoid unverifiable battery/accuracy claims.
- Release notes: user-visible changes, compatibility, migration.

## 8. Common failure modes

- Raw simulator window in README/store.
- White rectangular background behind a round watch.
- White halo around a dark bezel.
- Stretched circular display.
- Mixed device scales in one banner.
- Store dimensions from an old blog post.
- Claiming devices not declared in the manifest.
- Exposing personal notifications or health data in screenshots.
- Treating a planned feature as shipped.
- Submitting without checking current store requirements.

## 9. QA gate

- [ ] Manifest/device claims verified.
- [ ] Raw and clean assets separated.
- [ ] Correct crop type and round geometry.
- [ ] Transparent exterior; interior UI intact.
- [ ] Store dimensions/formats checked or marked unverified.
- [ ] Copy matches shipped features.
- [ ] No personal/health data or secrets visible.
- [ ] QA report and asset manifest delivered.
