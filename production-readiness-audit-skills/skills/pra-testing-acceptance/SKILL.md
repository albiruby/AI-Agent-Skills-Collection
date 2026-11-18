---
name: pra-testing-acceptance
description: Audit the testing strategy and run release validation for a web project - unit, integration, end-to-end, visual regression, security and performance testing, production smoke test and user acceptance testing (UAT). Use when the user asks "sudah ada test belum?", wants a test plan, Playwright/Vitest/Jest review, smoke test after deploy, visual regression setup, UAT checklist, stakeholder sign-off, or a go/no-go acceptance gate before launch. Covers audit domains 81-89.
---

# Testing, Smoke Test, UAT (Domains 81–89)

Parent: `production-readiness-audit`. Two jobs: (a) **audit** the existing test strategy and coverage of critical logic; (b) **execute** acceptance activities (smoke, E2E, UAT prep) within safety limits. Lists: `references/checklist.md`.

## Procedure
1. **Strategy (81)**: documented scope, environments, test data, ownership, reporting, automation in CI, maintenance. Map existing tests (`inventory.sh` lists them) against risk: what are the 5 things that would hurt most if broken (home render, brand/detail pages, CMS data mapping, form delivery, navigation, revalidation)? Are those covered?
2. **Unit (82)**: utility/format/URL/date helpers, CMS→view-model mappers, validation functions, conditional rendering, null/undefined and boundary cases, error handling; test isolation and flakiness. Run the suite (`npm test`) and record pass/fail/skip; examine skipped tests and snapshots that assert nothing.
3. **Integration (83)**: Next.js ↔ Sanity (GROQ queries against fixture/staging dataset), data mapping, image handling, metadata generation, webhook + revalidation (signed request test), API routes/Server Actions, form → email (sandbox), maps/analytics stubs, error propagation, timeout/failure of external services.
4. **E2E (84)**: Playwright journeys — home, about, brand discovery→detail, events, journal→article, careers, contact submission (test mode), navigation incl. mobile, CTA→external destination, direct URL, refresh/history, invalid route, CMS update propagation, preview vs production behavior. Run against the production build; capture traces/screenshots on failure. Cross-browser: Chromium + WebKit + Firefox projects.
5. **Visual regression (85)**: baseline screenshots for key pages × desktop/mobile × states (menu open, modal, empty/long content, CMS variants); mask dynamic regions (dates, videos); same OS/font environment in CI to avoid false diffs.
6. **Security/performance testing (86/87)**: delegate to `pra-security` and `pra-performance-caching` for the actual checks; here verify they are *part of the strategy* (scheduled scans, Lighthouse CI, budgets) and note which were executed in this audit.
7. **Production smoke test (88)** — post-deploy, read-only: homepage & main nav (desktop/mobile), all critical routes and all entity pages return 200 with expected content, images/fonts load, links/CTAs work, form page loads (submit only with approved test), maps render, external integrations respond, metadata + canonical + robots + sitemap correct, HTTPS and redirects, **no critical console or network errors**, monitoring receives events, rollback target available. Produce a pass/fail table with timestamp and deployment ID.
8. **UAT (89)**: prepare checklist and sign-off record — stakeholder, content, design, brand, functional, mobile/desktop, accessibility, SEO, legal/privacy, CMS editor (can they publish and update without a developer?), production readiness; list known issues accepted; **launch decision recorded with name/date**. The agent prepares and tracks; humans approve.

## Test quality judgments
- Count of tests ≠ coverage. Check assertions are meaningful and that critical logic paths are covered; coverage numbers are a hint only.
- Flaky tests (retries, `waitForTimeout`) → Medium maintenance risk.
- No tests at all on a small brochure site → Low–Medium; on forms/revalidation/CMS mapping → Medium–High.

## Calibration
Failing smoke test on a critical route → launch blocker. UAT approval missing → READY WITH CONDITIONS at best (condition: obtain sign-off).

## Output
Test strategy assessment, test run log (executed/passed/failed/skipped), smoke-test table, UAT checklist with status, findings (`TEST-NNN`), recommended minimal test suite for the project's risk.

## Pitfalls
Running E2E against dev server · submitting real forms in smoke tests · reporting "tests pass" without saying what they cover · snapshot tests approved blindly.
