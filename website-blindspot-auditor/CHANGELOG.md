# Changelog

## 2.0.0

Major expansion from a methodology-only skill into an executable audit system.

### Added

- Six technology adapters: Next.js/Vercel, WordPress/WooCommerce, e-commerce/payments, Supabase/PostgreSQL, static/SPA, and AI-enabled products.
- Mode runbooks for Deep, Focused, Blind-Spot Hunt, and Re-audit, including minimum coverage and stop conditions.
- Intake question bank and scope/authorization contract.
- Read-only check cookbook by capability and stack.
- Coverage scoring model and definition of done.
- Output pack: intake/scope, executive summary, remediation plan, re-audit report, evidence log, and `findings.schema.json`.
- Two worked examples (SaaS and e-commerce).
- Evaluation harness with three cases, distractors, and a scorecard.
- Routing guidance for structured pre-launch audit packs.

### Expanded

- Audit domains from a short catalogue into 13 briefs with verification methods, evidence requirements, and false-positive traps.
- Project profiles with highest-yield blind spots.
- Edge-case library from ~70 to 200+ scenarios, adding email deliverability, caching/version skew, i18n/timezone/currency, mobile/deep links, AI, integrations, abuse, admin operations, and business claims.
- Blind-spot methods with promise-vs-implementation, invariant derivation, change/version-skew, shadow-process, and counterfactual analysis.
- Evidence guidance with machine-readable export, remediation-ready findings, and re-audit status.
- Safety guidance with scope contracts, test-data handling, and responsible disclosure.

### Changed

- `SKILL.md` now routes to adapters, runbooks, and the output pack; adds Re-audit mode and explicit "when not to use" guidance.
- Validation reference now describes a repeatable evaluation protocol rather than only general QA principles.

## 1.0.0

- Initial universal adaptive audit skill.
- Added technology-, project-, and capability-aware audit selection.
- Added universal, conditional, and integration-level audit guidance.
- Added blind-spot reasoning and cross-layer analysis.
- Added evidence, confidence, severity, coverage, and safety requirements.
- Added reusable audit report and coverage templates.
