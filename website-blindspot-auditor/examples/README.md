# Worked Examples

Two complete examples show the expected depth, evidence style, and honesty level. They are fictional and exist to calibrate output quality.

- [`worked-example-saas.md`](worked-example-saas.md) — multi-tenant SaaS with Next.js, Supabase, and Stripe. Focus: tenant isolation, caching, webhook idempotency, entitlements.
- [`worked-example-ecommerce.md`](worked-example-ecommerce.md) — storefront with checkout, inventory, Stripe, and email. Focus: price integrity, oversell, replay, refunds, analytics.

## How to use them

1. Read the scenario and coverage excerpt, not just the findings.
2. Notice how each finding separates expected vs observed behavior and states what the evidence does not prove.
3. Compare the "what a shallow audit would have missed" section with your own first-pass instincts.
4. Use the report structure (`templates/audit-report.md`) and schema (`templates/findings.schema.json`) in real audits.

Do not copy the findings into another project. The value is in the reasoning pattern: context → adapters/domains → trace → verify → classify → coverage.

## Calibration questions

- Did the audit follow the money/access/content path to the authoritative layer?
- Did it distinguish a code-level defect from a runtime impact?
- Did it label blocked areas instead of guessing?
- Did it avoid inflating severity or volume?
- Did the coverage statement match what was actually done?

If a real report cannot answer these, it is not ready.
