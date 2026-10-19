# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Nothing yet.

## [0.1.0] - 2026-10-14

First public release. Experimental: skills are written to be tool-independent but have not been systematically evaluated across AI tools.

### Added

**Planning**
- `prd-generator`
- `app-feature-scope-planner`
- `app-ux-flow-specifier`

**Architecture and design**
- `app-architecture-designer`
- `web-design-system-architect`
- `database-schema-designer`
- `api-contract-designer`

**Implementation**
- `frontend-implementation-planner`
- `backend-implementation-planner`
- `mobile-app-implementation-planner`
- `design-system-implementer`
- `ai-coding-agent-task-planner`

**Quality**
- `test-strategy-planner`
- `code-review-auditor`
- `security-privacy-auditor`
- `accessibility-performance-auditor`
- `debugging-root-cause-analyst`

**Release and maintenance**
- `devops-release-planner`
- `legacy-refactor-migration-planner`
- `repo-onboarding-agents-md-generator`
- `technical-docs-writer`

**AI features**
- `ai-feature-eval-designer`

**Repository**
- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE` (MIT), and `templates/SKILL_TEMPLATE.md`.
- A shared **Platform-Agnostic Operation** section in every skill, covering tool availability, vendor independence, response language, and delivering the artifact.

### Changed
- `prd-generator` was previously named `gemini-prd-generator`. It was renamed and its frontmatter `description`, which had been truncated, was rewritten.
- References to a specific coding agent product in `ai-coding-agent-task-planner` and `prd-generator` were replaced with tool-neutral wording.

[Unreleased]: https://github.com/albiruby/web-app-dev-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/albiruby/web-app-dev-skills/releases/tag/v0.1.0
