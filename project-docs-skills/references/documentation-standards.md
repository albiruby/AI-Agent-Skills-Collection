# Technical Documentation Standards

## Groundedness Rules

1. **Codebase Is Single Source of Truth**: Every feature bullet, CLI flag, API route, supported device, and prerequisite version must be verified from actual repository files.
2. **Exact Commands Only**: Copy exact npm/pnpm/cargo/monkeyc/flutter commands from config files. If a command requires an SDK or local tool, state the prerequisite explicitly.
3. **No Marketing Fluff**: Replace vague superlatives ("blazingly fast", "revolutionary", "seamless") with concrete facts ("renders at 1Hz in low-power mode", "supports 71 Garmin devices", "zero runtime dependencies").
4. **Zero Unresolved Placeholders**: Never leave `[TBD]`, `[Your Name]`, or `TODO` in finished docs unless the user explicitly requested a blank template.

## Structure & Scannability

- **Title + One-Line Summary**: State what the project does and who it is for in one crisp sentence.
- **Visual First**: Place the clean hero banner (`docs/store-assets/HERO_*.jpg`) or clean sliced screenshots directly below the intro so readers grasp the product in 3 seconds.
- **Tables for Comparisons & Options**: Use Markdown tables for environment variables, CLI flags, API endpoints, and supported device families.
- **Progressive Disclosure**: Keep `README.md` concise (typically 80-200 lines) and link out to `docs/ARCHITECTURE.md`, `docs/API.md`, or `docs/DEPLOYMENT.md` for deep technical detail.
