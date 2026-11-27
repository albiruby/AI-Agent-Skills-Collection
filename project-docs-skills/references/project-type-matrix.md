# Project Type & Documentation Matrix

Use this matrix during Step 1 (Project Profiling) to pick the right documentation files, screenshot capture method, and preview asset pack for the repository.

| Project Archetype | Detection Signals | Core Tech Docs | Screenshot Capture & Slicing | Store / Preview Asset Pack |
| :--- | :--- | :--- | :--- | :--- |
| **Garmin Connect IQ (Monkey C)** | `manifest.xml`, `monkey.jungle`, `.mc` files | `README.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `docs/DEVICES.md` | CIQ Simulator capture -> strip title/menu/status bar + white flood-fill alpha slice -> transparent watch PNG | `COVER_500x500.jpg`, `HERO_1440x720.jpg`, `SCREEN_1..5` (`1440x900`), `master/` PNGs |
| **Web App / SaaS** | `package.json` (Next.js, Vite, React, Vue, Astro), `index.html` | `README.md`, `ARCHITECTURE.md`, `docs/DEPLOYMENT.md`, `CHANGELOG.md` | Headless Playwright/Chromium capture at `1440x900` & `390x844` -> hide scrollbars/banners -> optional browser frame | `OG_1200x630.png`, `GITHUB_SOCIAL_1280x640.png`, `HERO_1440x720.png`, `SCREEN_1..5` |
| **Mobile App (iOS / Android / Flutter / RN)** | `pubspec.yaml`, `Info.plist`, `AndroidManifest.xml`, `app.json` | `README.md`, `ARCHITECTURE.md`, `docs/RELEASE.md`, `CHANGELOG.md` | `xcrun simctl` / `adb screencap` with clean status bar -> optional device bezel + transparent alpha crop | App Store (`1290x2796`), Play Feature (`1024x500`), Play Screens (`1080x1920`), `COVER_1024x1024` |
| **Desktop App** | `tauri.conf.json`, `electron-builder`, `.csproj`, `CMakeLists.txt` | `README.md`, `ARCHITECTURE.md`, `docs/BUILD.md`, `CHANGELOG.md` | Window-only capture -> strip desktop clutter -> rounded shadow / transparent margin | `HERO_1440x720.png`, `SCREEN_1..4` (`1440x900`), `GITHUB_SOCIAL_1280x640.png` |
| **CLI Tool** | `bin` in `package.json`, `clap`/`cobra`/`argparse`/`typer` | `README.md`, `docs/CLI_REFERENCE.md`, `CHANGELOG.md` | Clean terminal render (dark theme, high contrast, zero personal paths/tokens) | `HERO_1280x640.png` (terminal showcase), `README` inline SVG/PNG |
| **API / SDK / Library** | OpenAPI/Swagger, `setup.py`/`pyproject.toml`, `exports` in `package.json` | `README.md`, `docs/API.md`, `ARCHITECTURE.md`, `CHANGELOG.md` | Architecture & sequence diagrams (Mermaid) + clean code/response cards | `GITHUB_SOCIAL_1280x640.png`, `ARCHITECTURE` diagram PNG/SVG |
| **Game (2D / 3D / Indie)** | Unity `ProjectSettings`, Godot `project.godot`, Phaser/Love2D | `README.md`, `docs/CONTROLS.md`, `docs/ARCHITECTURE.md`, `CHANGELOG.md` | In-engine clean HUD capture (no debug FPS/colliders) -> aspect-locked frames | Store Capsule/Cover, Hero Banner (`1440x720`), `SCREEN_1..5` gameplay showcases |
| **Data / ML Tool** | notebooks, pipeline configs, model cards, `requirements.txt`/`pyproject.toml` | `README.md`, `docs/DATA.md`, `docs/EVALUATION.md`, `CHANGELOG.md` | Clean notebooks, metric charts, pipeline diagrams, sample I/O cards | Social card, architecture diagram, results visual |
| **Monorepo / Multi-app** | workspaces, multiple manifests, shared packages | Root README with app map; per-app docs where needed | Per-app capture flows; shared brand system | Per-app or shared social/preview assets |

## Common blind spots by archetype

- **Garmin:** unsupported device claims, raw simulator windows, white canvas, round-display distortion, missing AOD/battery notes.
- **Web:** browser chrome in screenshots, cookie banners, desktop-only screenshots for responsive claims, stale OG images.
- **Mobile:** unclean status bars, wrong store dimensions, fake device frames, missing tablet variants.
- **Desktop:** full-desktop captures, OS-specific chrome, missing platform requirements.
- **CLI/API:** fabricated output, leaked tokens/paths, missing error examples, docs that disagree with runtime.
- **Game:** debug overlays, menu-only galleries, unsupported platform claims.
- **Data/ML:** unverified metrics, cherry-picked charts, missing data/limitations, notebook outputs with personal data.
