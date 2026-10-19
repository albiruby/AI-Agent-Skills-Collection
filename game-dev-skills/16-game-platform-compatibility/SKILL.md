---
name: game-platform-compatibility
description: Platform targeting, compatibility and porting for games: Web, Android, iOS, Windows, macOS, Linux, Steam Deck, consoles, VR/AR, smart TV, cloud gaming; hardware tiers, screen/aspect handling, store/platform requirements, export settings.
---

# Platform Compatibility & Porting

## Per-platform checklist
| Platform | Key concerns |
|---|---|
| **Web (HTML5)** | browser matrix (Chrome/Edge/Firefox/Safari, mobile Safari quirks), WebGL2/WebGPU fallback, audio unlock on gesture, fullscreen/pointer-lock, storage limits (IndexedDB), build size/loading, iframe embedding for portals (itch.io, CrazyGames, Poki, Newgrounds), PWA/offline, no threads without COOP/COEP headers |
| **Android** | API level targets, ABIs (arm64-v8a mandatory for Play), AAB format, fragmentation (RAM/GPU tiers), Vulkan/GLES, notch/cutouts, back button, permissions, Play Games Services, Play Billing, ads SDK, large-screen/foldable/Chromebook, size limits and Play Asset Delivery |
| **iOS/iPadOS** | Metal, Xcode/signing/provisioning, App Store review rules, privacy manifest/ATT, Sign in with Apple when other social logins, StoreKit IAP, Game Center, safe areas, ProMotion, thermal |
| **Windows** | DirectX 11/12/Vulkan, GPU vendors, resolutions/ultrawide, controller support, installer/Steam, antivirus false positives, signing |
| **macOS** | Apple Silicon/Intel universal, Metal, notarization, no OpenGL modern |
| **Linux / Steam Deck** | Proton vs native, Vulkan, 1280x800 UI scale, controller-first UI, Deck Verified criteria |
| **Consoles** (Switch, PlayStation, Xbox) | dev kit & publisher program approval (ID@Xbox, PlayStation Partners, Nintendo Developer Portal), certification (TRC/TCR/Lotcheck), memory/perf limits, achievements/trophies, save/suspend-resume, engine licensing/port partners |
| **VR/AR** | OpenXR, Quest standalone vs PC VR, 72-120 fps, comfort, hand tracking, passthrough, ARKit/ARCore |
| **Smart TV / Cloud** | remote/d-pad focus UI, overscan, low-end SoC, latency, streaming SDKs |

## Cross-cutting
- **Resolution/aspect**: design for scalable UI, safe areas, letterbox/pillarbox or expand-view policy, integer scaling for pixel art; test 4:3 to 21:9 and portrait/landscape.
- **Input parity**: map all actions to every supported device (13).
- **Graphics API/shader compatibility**: avoid platform-specific shader features without fallback; test on lowest-spec GPU.
- **Save portability**: cloud sync, endianness/path issues, sandbox paths.
- **Online services abstraction**: wrap platform SDKs (achievements, IAP, auth) behind an interface so ports swap implementations.
- **Min/recommended specs** table, supported OS versions, device test matrix (low/mid/high), analytics by device model.
- **Cross-play & cross-save** policies per platform holder.

## Output
Platform support matrix with priority, risks, SDK list, build/export settings, min-spec & device matrix, port plan with effort estimate, abstraction layer design.
