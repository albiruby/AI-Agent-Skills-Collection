# Changelog

## 1.0.0

Initial merged and enhanced pack.

### Merged

- Combined the executable visual pipeline from `project-docs-visual-skills-suite` with the documentation architecture, evidence discipline, platform adapters, and release packaging from `project-documentation-visual-assets-skill-pack`.
- Replaced the two overlapping formats with one consistent `SKILL.md` pack.

### Added

- 10 skills:
  - `project-docs-skills`
  - `project-context-analyzer`
  - `project-docs-planner`
  - `project-tech-docs-author`
  - `visual-asset-capture`
  - `clean-screenshot-slicer`
  - `store-preview-asset-builder`
  - `product-store-copywriter`
  - `docs-visual-qa-auditor`
  - `docs-release-packager`
- Garmin Connect IQ playbook with screenshot types, round-display handling, store assets, and QA.
- Extended project type matrix (Garmin, web, mobile, desktop, CLI, API/SDK, game, data/ML, monorepo).
- New documentation templates: API, user guide, deployment, troubleshooting, contributing, ADR.
- Screenshot shot list, platform requirement record, and QA report templates.
- Evaluation harness with three cases and a scorecard.
- Cross-platform/tool capability contract with truthful completion states.

### Enhanced

- Unified clean/dirty screenshot standard, slicing QA, and store composition rules.
- Added authenticity/privacy rules for screenshots and store visuals.
- Added explicit "verify current official requirements or mark unverified" policy.
- Consolidated source-of-truth, audience, maturity, and over-documentation guidance.
- Made pack-level references/templates explicit and documented install implications.
- Reused and tested the three bundled Python scripts end-to-end.

### Fixed

- Removed duplicated/overlapping sub-skill descriptions between the two source packs.
- Removed stale `# Instructions`/flat-markdown packaging from the merged pack.
- Clarified Windows `python` vs `python3` usage.
- Corrected cross-skill reference paths.
