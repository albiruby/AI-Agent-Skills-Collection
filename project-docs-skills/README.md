# Project Documentation & Visual Assets

A plug-and-play Agent Skills pack for producing professional project documentation, authentic clean screenshots, and store-ready preview assets for any software project.

Merged and enhanced from two earlier packs:

- `project-docs-visual-skills-suite` — executable screenshot/store pipeline and specialist skills.
- `project-documentation-visual-assets-skill-pack` — documentation architecture, evidence discipline, platform adapters, release packaging.

The result is **10 cohesive skills**, shared references, executable scripts, templates, worked examples, and an evaluation harness.

## What it does

1. Inspects the real project and separates implemented, partial, planned, and unverified behavior.
2. Plans the smallest professional documentation set for the project's maturity and audience.
3. Writes grounded README, architecture, API/CLI, user, deployment, troubleshooting, and release docs.
4. Captures genuine screenshots from simulators, emulators, browsers, desktops, games, devices, or terminals.
5. Cleans raw captures into transparent device cutouts, display-only crops, or viewport cards.
6. Composes store covers, hero banners, feature showcases, mobile panels, GitHub/OG cards.
7. Writes store copy, captions, and release notes grounded in verified features.
8. Runs automated + visual QA and reports unverified requirements honestly.
9. Packages source, working, final, and editable assets with a manifest and handoff note.

## Skills

| # | Skill | Role |
|---|---|---|
| 1 | `project-docs-skills` | Main entry, project routing, pipeline, completion states |
| 2 | `project-context-analyzer` | Evidence model, feature maturity, asset/tool inventory |
| 3 | `project-docs-planner` | Audience map, document set, source-of-truth, visual plan |
| 4 | `project-tech-docs-author` | README, architecture, API/CLI, user, deployment, troubleshooting, changelog |
| 5 | `visual-asset-capture` | Genuine captures from simulator/browser/device/game/terminal |
| 6 | `clean-screenshot-slicer` | Chrome removal, transparency, tight crops, viewport cards |
| 7 | `store-preview-asset-builder` | Cover, hero, feature, mobile panel, OG/GitHub compositions |
| 8 | `product-store-copywriter` | Store listing, banner copy, release notes, permissions |
| 9 | `docs-visual-qa-auditor` | Traceability, automated validator, visual/compliance QA |
| 10 | `docs-release-packager` | Naming, manifest, package integrity, handoff |

## Supported project types

- Garmin Connect IQ / Monkey C and other wearables/embedded apps.
- Web apps, SaaS dashboards, static sites.
- iOS, Android, Flutter, React Native.
- Desktop apps, Electron, Tauri, CLI tools.
- APIs, SDKs, libraries, packages.
- Games and interactive applications.
- Data/ML tools (docs and evidence; visual policy still applies).

See `references/project-type-matrix.md`.

## Architecture

```text
project-docs-skills/
  README.md
  INSTALL.md
  CHANGELOG.md
  skill-pack.json
  skills/
    project-docs-skills/SKILL.md
    project-context-analyzer/SKILL.md
    project-docs-planner/SKILL.md
    project-tech-docs-author/SKILL.md
    visual-asset-capture/SKILL.md
    clean-screenshot-slicer/
      SKILL.md
      scripts/slice_clean_device.py
    store-preview-asset-builder/
      SKILL.md
      scripts/compose_store_assets.py
    product-store-copywriter/SKILL.md
    docs-visual-qa-auditor/
      SKILL.md
      scripts/validate_doc_pack.py
    docs-release-packager/SKILL.md
  references/
  templates/
  examples/
  evals/
```

## Pipeline

```text
context → plan → docs → capture → clean/slice → compose → copy → QA → package
```

Visuals come before embedding. Raw captures never go directly into final docs/store art.

## Quick start

1. Read `INSTALL.md` and install the pack.
2. Try:

> Use `project-docs-skills` to inspect this project and propose a documentation and visual asset plan.

3. Or run a focused task:

> Use `clean-screenshot-slicer` to turn these Garmin simulator captures into transparent watch PNGs.

> Use `store-preview-asset-builder` to build a 500x500 cover, 1440x720 hero, and three 1440x900 feature screens from `docs/assets/clean/`.

## Scripts

Bundled Python scripts require Python 3.9+ and Pillow; numpy is optional.

| Script | Purpose |
|---|---|
| `skills/clean-screenshot-slicer/scripts/slice_clean_device.py` | Strip chrome/background, transparent cutout, viewport card |
| `skills/store-preview-asset-builder/scripts/compose_store_assets.py` | Render cover/hero/feature/mobile/OG assets from a JSON manifest |
| `skills/docs-visual-qa-auditor/scripts/validate_doc_pack.py` | Check links, placeholders, transparency, dimensions, masters |

On Windows use `python`; on macOS/Linux use `python3` when available.

## References

- Documentation principles, architecture, standards, Mermaid.
- Project type matrix and Garmin playbook.
- Visual asset guidelines, capture recipes, slicing QA, composition.
- Store asset specs, store copy limits, platform requirements adapter.
- Tool capability contract, harness compatibility, QA checklist.

## Templates

README, architecture, API, user guide, deployment, troubleshooting, changelog, contributing, ADR, docs plan, screenshot shot list, platform requirement record, asset manifest, store listing, release notes, QA report, Garmin/Web manifests.

## Examples

- Garmin watch face end-to-end.
- Web/SaaS docs + social visuals.
- Mobile release pack.
- CLI/API/library docs + diagrams.

## Evaluation

Use `evals/` to test grounding, screenshot authenticity, clean/slice quality, store composition, compliance honesty, QA, and handoff. Cases are samples, not certification.

## Core rules

- Ground every project-specific claim in evidence.
- Do not fabricate UI, features, metrics, devices, ratings, or screenshots.
- Keep raw, working, editable, and final assets separate.
- Verify current store requirements or mark compliance **not verified**.
- Never expose secrets or personal data.
- Do not publish/submit/deploy without explicit authorization.
- State completion precisely: created, processed, reviewed, validated, submitted, published.

## Provenance and versioning

This merged pack is version **1.0.0**. The two source packs were consolidated into this folder; version history is in `CHANGELOG.md`.
