# Worked Example: E-commerce Audit (Fictional)

This example shows how to audit money, inventory, and post-purchase state. The store, code, and findings are fictional.

## Scenario

**Request:** "We launch Kopi Kita next month. Audit checkout and orders — especially discounts, stock, and refunds. We use Next.js on Vercel, Postgres, Stripe, and Resend. Test mode only."

**Mode:** Focused Audit on checkout/order lifecycle, with adjacent reliability and analytics checks.

**Authorization:** Read repository, run tests, use Stripe test mode, inspect a staging storefront with synthetic carts, read-only database. No live charges, no real emails, no production mutation.

## 1. Context reconstructed

- Product: single-vendor coffee store; physical bags and a monthly subscription.
- Actors: guest, customer, subscriber, support agent, admin.
- Stack: Next.js App Router, Postgres (custom orders/inventory), Stripe Payment Intents + webhooks, Resend email, Vercel cron for abandoned carts.
- Critical journeys: browse → cart → discount → checkout → payment → fulfillment → delivery; subscription renewal; refund/cancel.
- Invariants:
  - Charged amount equals the server-computed total for the selected items, currency, shipping, tax, and discounts.
  - Confirmed orders never exceed available stock.
  - One payment event produces one order/fulfillment.
  - Refund/cancellation reverses entitlement, stock, and revenue reporting as policy requires.

## 2. Domains and adapters selected

| Domain | Why | Depth |
|---|---|---|
| Requirements/business logic | Discounts, tax, shipping, refund policy | Deep |
| Data integrity | Inventory, orders, idempotency | Deep |
| Security/privacy | Payment data, customer data, admin | Medium |
| Functional journeys | Checkout/retry/subscription | Deep |
| Reliability/operations | Webhooks, cron, email | Medium |
| Analytics | Purchase events/consent | Medium |
| Content/SEO/a11y | Product pages | Light |

Adapters: `nextjs-vercel`, `ecommerce-and-payments`, `supabase-postgres` (Postgres-only parts).

## 3. Findings

### KK-001 — Checkout accepts client-supplied unit price

- **Class:** Verified Finding
- **Severity:** Critical · **Confidence:** High
- **Location:** `app/api/checkout/route.ts:22`, `lib/cart.ts:48`
- **Evidence:** The route builds Stripe line items from `items[].price` sent by the browser. It validates the product ID exists but does not reload the current price from the database. A staging request with a modified price created a Payment Intent for the altered amount.
- **Expected:** Price is loaded server-side from the product/variant and never trusted from the client.
- **Observed:** Modified `price: 1` produced a $0.01 line item in test mode.
- **Impact:** Direct revenue loss; discount/price logic can be bypassed.
- **Verification:** Staging request with modified payload; Stripe test-mode Payment Intent amount compared.
- **Recommendation:** Recompute all line items, discounts, shipping, and tax server-side from product IDs, quantities, and the customer's currency/region. Pass only opaque IDs/quantities from the client.
- **Acceptance criteria:** Tampered price has no effect; checkout total matches server quote; test covers stale price, currency, and deleted product.
- **Regression risk:** Recalculation may change totals for existing carts; show a price-change notice before payment.
- **Remaining uncertainty:** Whether any other endpoint accepts client totals; search all checkout paths.

### KK-002 — Duplicate webhook delivery double-fulfills orders

- **Class:** Verified Finding
- **Severity:** High · **Confidence:** High
- **Location:** `app/api/webhooks/stripe/route.ts:57`, `lib/orders/fulfill.ts:19`
- **Evidence:** `payment_intent.succeeded` marks the order paid and enqueues a fulfillment job. The handler does not store the event ID and the fulfillment job has no idempotency key. Replaying the same test event created two fulfillment records and two "order shipped" emails in staging.
- **Expected:** One payment event → one fulfillment and one notification.
- **Observed:** Duplicate delivery produced duplicate fulfillment/email.
- **Impact:** Double shipping cost, customer confusion, inventory drift.
- **Verification:** Stripe test-mode replay with a synthetic order; database and email-outbox inspection.
- **Recommendation:** Persist provider event IDs with a unique constraint, make fulfillment idempotent per order, and suppress duplicate notifications. Use a transaction/outbox for state + job creation.
- **Acceptance criteria:** Replaying an event produces no second fulfillment/email; unique constraint present; failure returns non-2xx for retry.
- **Regression risk:** Retries may expose previously swallowed errors; monitor.
- **Remaining uncertainty:** Other providers/events may share the handler.

### KK-003 — Inventory can oversell the last unit under concurrent checkout

- **Class:** Potential Risk
- **Severity:** High · **Confidence:** Medium
- **Location:** `lib/inventory/reserve.ts:14`
- **Evidence:** Reservation reads `stock` then writes `stock - qty` without a conditional update or row lock. Two concurrent requests can both read the same value. No unique reservation constraint exists.
- **Expected:** Confirmed commitments never exceed stock.
- **Observed:** Not reproduced in the time box; the code path is unambiguous but staging concurrency requires controlled parallel requests, which was not authorized.
- **Impact:** Overselling, refunds, support load, fulfillment delays.
- **Verification:** Static trace; propose a staging test with two parallel carts on the last unit.
- **Recommendation:** Use `UPDATE ... SET stock = stock - $qty WHERE id = $id AND stock >= $qty` (or a transaction with `SELECT ... FOR UPDATE`), plus a reservation record and reconciliation for abandoned holds.
- **Acceptance criteria:** Concurrent last-unit test yields one success and one sold-out; stock never negative; reservation expiry releases stock.
- **Regression risk:** Lock contention on hot products; measure.
- **Remaining uncertainty:** Database isolation level in production; whether the provider checkout reserves stock elsewhere.

### KK-004 — Refund does not revoke subscription access or restore stock

- **Class:** Verified Finding
- **Severity:** Medium · **Confidence:** High
- **Location:** `app/api/admin/refund/route.ts:31`
- **Evidence:** The handler creates the Stripe refund and marks the order refunded, but does not update `subscriptions.status`, `entitlements`, or inventory. A second code path for cancellations does revoke access, so behavior differs by channel.
- **Expected:** Refund/cancellation applies the documented policy consistently across access, stock, and revenue.
- **Observed:** Static trace shows a refunded subscriber would retain access until the next renewal job; stock is not restocked.
- **Impact:** Continued access after refund; inventory undercount; revenue/stock mismatch.
- **Recommendation:** Centralize post-refund effects in one service, including entitlement, stock, analytics, and notifications; decide policy for partial refunds.
- **Acceptance criteria:** Refund path tests cover full/partial refund, subscription access, stock, and analytics; both admin and provider-initiated refunds behave the same.
- **Regression risk:** Restocking returned/undelivered goods varies by policy; encode explicitly.
- **Remaining uncertainty:** Whether the renewal job eventually corrects access, and how partial refunds are intended to behave.

### KK-005 — Free-shipping threshold can be bypassed by currency/rounding

- **Class:** Verified Finding
- **Severity:** Medium · **Confidence:** High
- **Location:** `lib/pricing/shipping.ts:22`
- **Evidence:** The threshold is compared before currency conversion, and totals are rounded per line rather than at the order level. A cart near the threshold in a non-default currency qualified for free shipping while the charged subtotal was below the policy amount in the store's base currency.
- **Expected:** Shipping policy is evaluated on a defined, consistent monetary basis.
- **Observed:** Boundary case in staging showed free shipping applied below the intended threshold.
- **Impact:** Margin loss; inconsistent customer experience across currencies.
- **Recommendation:** Define the policy currency and rounding rule, compute order-level totals in minor units, and test boundary cases for each supported currency.
- **Acceptance criteria:** Threshold tests pass at ±1 minor unit in every currency; invoice/email/report totals reconcile.
- **Regression risk:** Some existing carts may cross the threshold after the fix; communicate if needed.
- **Remaining uncertainty:** Tax-inclusive pricing policy by market.

### KK-006 — Purchase analytics fires before consent and on failed payments

- **Class:** Potential Risk
- **Severity:** Medium · **Confidence:** Medium
- **Location:** `components/checkout/analytics.ts:17`
- **Evidence:** The `purchase` event is sent from the client when the Payment Intent is created, before confirmation, and without checking consent state. Server-side order events are not reconciled.
- **Expected:** Purchase events fire after confirmed payment and only under the applicable consent policy.
- **Observed:** Static trace; no production analytics access. A test-mode checkout showed the event before payment confirmation.
- **Impact:** Inflated revenue/conversion, consent violations, unreliable reporting.
- **Recommendation:** Emit purchase server-side after payment success, include order ID for deduplication, and gate marketing analytics on consent.
- **Acceptance criteria:** Failed/cancelled payments do not produce purchase events; one event per order; consent-denied sessions send no non-essential events.
- **Remaining uncertainty:** Which analytics are classified essential vs marketing.

### KK-007 — Opportunity: out-of-stock variants remain indexable with stale schema

- **Class:** Improvement Opportunity
- **Severity:** Low · **Confidence:** Medium
- **Evidence:** Product pages for sold-out variants remain indexable with `availability: InStock` in structured data; canonical points to the variant URL. No policy was documented.
- **Expected benefit:** Better search quality and fewer disappointed customers.
- **Recommendation:** Choose a policy: keep indexable with `OutOfStock`, or redirect to the parent product. Make structured data match the visible state.

## 4. Coverage excerpt

| Area | Status | Note |
|---|---|---|
| Price/tax/shipping/discounts | Verified gap | KK-001, KK-005 |
| Webhooks/idempotency | Verified gap | KK-002 reproduced |
| Inventory concurrency | Potential | KK-003 static only; parallel test not authorized |
| Refunds/entitlement | Verified gap | Admin path traced; provider-initiated path not exercised |
| Subscription renewal | Not inspected | Outside focused scope; adjacent risk |
| Analytics/consent | Partial | Client trace only; no analytics access |
| SEO/structured data | Light | KK-007 |
| Accessibility | Light | Not the focus; basic keyboard pass only |

Coverage score: context 2, domain selection 2, journeys 2, cross-layer 2, security 1, money/identity 2, failure/recovery 1, execution 1, evidence 2, transparency 2. Main limitation: concurrency and provider-initiated refunds were not executed.

## 5. What a shallow audit would have missed

- The UI shows a price; nothing suggests the server trusts it until you tamper with the request.
- The webhook passes a happy-path test; only replay reveals duplicate fulfillment.
- A stock read/write "works" in single-user testing; concurrency is the failure mode.
- Refund code looks complete until you compare it with the cancellation path.
- Free shipping looks correct in the default currency; the boundary appears only after conversion/rounding.
- Analytics "has a purchase event"; the lifecycle and consent are the actual risk.

## 6. Lessons for the skill

- Money integrity requires tracing every number from client input to provider charge to order/report.
- Replay and concurrency are default hypotheses for commerce, even when the happy path passes.
- Post-purchase state (refund, cancel, fulfill, notify) is where many stores diverge.
- A focused audit can be strong without auditing the whole site, provided the boundaries and limitations are explicit.
