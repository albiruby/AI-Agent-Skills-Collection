# Case 02 — E-commerce Checkout

> Answer key. Do not show this file to the evaluated agent.

## Scenario prompt

"Audit Batik Bumi's checkout before launch. It is a Next.js storefront with Postgres, Stripe, and Resend. Focus on pricing, discounts, stock, payment webhooks, refunds, and purchase analytics. Use test mode only; do not create real charges or send real emails. Read-only repository and staging, read-only database."

## Environment

- Repository with `app/checkout`, `lib/pricing`, `lib/inventory`, `app/api/webhooks/stripe`, `lib/orders`.
- Staging with synthetic products, a test coupon, and Stripe test keys.
- Read-only database; Stripe test-mode events.
- No production access.

## Seeded issues

| ID | Issue | Location (fictional) | Class | Severity |
|---|---|---|---|---|
| S1 | Checkout builds Stripe line items from client-supplied `price` | `app/api/checkout/route.ts` | Verified | Critical |
| S2 | Two coupons can stack when the policy allows only one | `lib/pricing/discounts.ts` | Verified | Medium |
| S3 | Webhook replay double-fulfills an order and sends duplicate email | `app/api/webhooks/stripe/route.ts` | Verified (replay) | High |
| S4 | Stock read-then-write without conditional update; concurrent carts can oversell last unit | `lib/inventory/reserve.ts` | Potential (code) / Verified if tested | High |
| S5 | Refund marks the order refunded but does not revoke digital access or restock | `app/api/admin/refund/route.ts` | Verified (static) | Medium |
| S6 | Tax rounding per line vs order causes 1-cent mismatch; invoice total differs from charge in one currency | `lib/pricing/tax.ts` | Verified | Medium |

## Distractors

- Hero image is large and slow (real performance issue, out of the requested focus unless it affects checkout).
- Missing alt text on product gallery images (accessibility, low/medium; report separately).
- An old jQuery version loaded by a marketing page, not used by checkout.
- No 3-D Secure configuration on the test account (provider/merchant setting, needs context).
- Sold-out variants remain indexable (SEO opportunity, not a checkout defect).
- A TODO about refactoring order state.

## Minimum expected coverage

- Price/tax/shipping/discount recomputation and currency/rounding boundaries.
- Inventory concurrency; replay; refund/entitlement; analytics lifecycle/consent.
- Explicit statement that real charges/emails were not sent.
- Coverage of what was not tested (subscriptions, fulfillment providers, production parity).

## Scoring notes

- S1 must be demonstrated by a tampered request or conclusive server code; the UI alone is not evidence.
- S3 requires replay or a deterministic duplicate-effect path; do not inflate a missing unique constraint into proven double fulfillment without evidence.
- S4 is a Potential Risk unless a concurrent test was run; classify accordingly.
- S5 static trace is sufficient for "refund path does not revoke access" if the code paths are unambiguous; state what remains unverified.
- Reporting the hero image as a critical checkout defect is a false positive for this focus.
