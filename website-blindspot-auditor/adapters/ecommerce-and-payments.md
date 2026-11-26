# Adapter: E-commerce and Payments

## Purpose

Inspect storefronts, carts, checkout, payment flows, orders, inventory, and post-purchase operations. Focus on money integrity, state consistency, idempotency, webhook handling, entitlement, and customer-data exposure.

The adapter applies to custom storefronts and to platforms such as Shopify, WooCommerce, and payment providers such as Stripe, Midtrans, Xendit, or PayPal. It does not assume a specific provider.

## Detection signals

- Product, variant, cart, checkout, order, payment, refund, or subscription models/routes.
- Provider SDKs or API calls (Stripe, Shopify, WooCommerce, PayPal, Midtrans, Xendit, Adyen, etc.).
- Webhook endpoints for payment/order/fulfillment events.
- Inventory, stock, reservation, coupon, discount, tax, shipping, or currency logic.
- Admin order management, refunds, payouts, or fulfillment screens.
- Analytics purchase/refund events and marketing pixels.

False positives: a catalog or lead-generation site may have no checkout; do not force payment checks. A marketplace may have separate seller payouts and buyer payments.

## Applicability

Load when the target includes any of:

- cart/checkout or order creation,
- payment authorization/capture,
- inventory or scarce-resource reservation,
- subscriptions, entitlements, or billing,
- refunds, disputes, fulfillment, or payouts.

For content-only commerce sites, keep the adapter limited to analytics, SEO, privacy, and trust signals.

## Boundaries and data flows

Trace the actual flow, for example:

1. Product/variant data → catalog/cache → price display.
2. Cart → checkout session → provider → return URL/webhook.
3. Payment event → order state → inventory → fulfillment → email.
4. Refund/dispute → order state → entitlement → customer notification.
5. Subscription renewal → invoice → payment → access renewal or grace period.
6. Order data → analytics/warehouse/support tooling.

Identify the authoritative source for price, stock, order status, and entitlement. Document what is recomputed server-side and what is trusted from the client or provider.

## Audit procedures

### A. Price, tax, shipping, discounts, and currency

- Verify price and line-item totals are recomputed server-side from authoritative data. Client-supplied price, discount, or currency must not be trusted.
- Check currency handling: minor units, rounding, display vs charge, multi-currency conversion, and currency mismatch between cart and charge.
- Check tax calculation, jurisdiction, inclusive/exclusive pricing, exemptions, and rounding at the order level.
- Check shipping rules, thresholds, address validation, and rate changes after quote.
- Check discount/coupon rules: stacking, reuse, expiry, minimum spend, product/category scope, and race conditions.
- Check whether stale cart prices or deleted products can still be checked out.

### B. Inventory and scarce resources

- Verify reservation, decrement, and release logic under concurrency.
- Check overselling risk: two buyers, last item, retries, abandoned checkout, delayed webhook.
- Check whether stock is decremented on order creation, payment, or fulfillment, and whether failures compensate.
- Check digital goods, licenses, seats, or capacity with the same rigor as physical stock.

### C. Checkout, idempotency, and state

- Map the order/payment state machine: created, pending, authorized, captured, paid, fulfilled, cancelled, refunded, partially refunded, disputed, failed.
- Verify duplicate submit, retry, browser refresh, back button, and multiple tabs cannot create duplicate orders or charges.
- Check idempotency keys/unique constraints for order creation and provider calls.
- Verify the return/cancel URL cannot mark an unpaid order as paid.
- Check timeout and ambiguous-success handling: payment succeeded but order update failed, or vice versa.
- Verify reconciliation exists for mismatched provider/order states.

### D. Webhooks

- Verify signature verification and replay protection.
- Check duplicate delivery, out-of-order events, late events, and events for unknown orders.
- Check whether webhook handlers are idempotent and whether they acknowledge quickly while processing safely.
- Verify failure/retry behavior and dead-letter/reconciliation visibility.
- Check that webhook endpoints do not trust unsigned payload fields for amount, currency, or customer identity.

### E. Refunds, disputes, subscriptions, and entitlement

- Check refund and partial-refund calculations, fees, taxes, and inventory restocking.
- Verify entitlement revocation on refund, cancellation, failed renewal, or chargeback, including cached sessions and offline access.
- Check subscription renewal, grace periods, dunning, plan changes, proration, and cancellation timing.
- Check invoice/receipt accuracy and legal/tax disclosures.
- Check dispute/chargeback handling and account restrictions.

### F. Customer data, notifications, and operations

- Check guest checkout, account creation, account merge, address book, and order history isolation.
- Verify order confirmation, shipping, refund, and failure emails are accurate and not duplicated.
- Check analytics purchase events for duplication, wrong amounts, consent, and refund handling.
- Check fraud/abuse controls: card testing, coupon abuse, resale, velocity, and account takeover.
- Check admin/support tooling: who can view or change orders, refund, or impersonate; is there an audit trail?
- Check exports, warehouses, and third-party integrations for data minimization.

## Verification methods

- Static review of pricing, cart, checkout, webhook, refund, and entitlement code.
- Sandbox/provider test mode with synthetic cards and test clocks if authorized.
- Browser inspection of cart/checkout behavior: refresh, back, duplicate submit, multiple tabs, expired session.
- Webhook replay in a local/sandbox environment only, with test signatures.
- Database read-only queries for orphaned/duplicate orders and state mismatches, if authorized.
- Log inspection for payment failures, webhook retries, and reconciliation jobs.

## Common failure modes

- Trusting client-supplied price, discount, currency, or entitlement.
- Duplicate charge/order on retry or double submit.
- Webhook processed twice or out of order, causing double fulfillment or state rollback.
- Payment succeeds but order remains unpaid, or order is marked paid without capture.
- Inventory oversell under concurrency or delayed release.
- Coupon stacking/reuse or discount applied to ineligible items.
- Currency/rounding mismatch between display, charge, refund, and accounting.
- Refund does not revoke access or restore inventory correctly.
- Subscription cancellation leaves access active beyond policy; failed renewal does not downgrade.
- Test-mode keys in production or live keys in test environments (report exposure, never print values).
- Guest checkout exposes another customer's order via guessable identifiers.
- Analytics double-counts purchases or records revenue before payment settles.

## Evidence requirements

- For price/inventory claims: the client input, the server path, the missing recomputation/constraint, and the resulting economic impact.
- For webhook claims: endpoint, signature/replay handling, event sequence, and observed or deterministic state effect.
- For entitlement claims: the access check, the event that should revoke it, and the path that still grants access.
- For duplicate-charge claims: the retry/duplicate path, idempotency mechanism (or absence), and provider/order behavior.

Do not claim real financial loss without evidence. A plausible race is a Potential Risk unless reproduced or conclusively established.

## Safety constraints

- Use sandbox/test mode and synthetic data only.
- Do not create real charges, refunds, payouts, or customer emails.
- Do not replay production webhooks or mutate production orders/inventory.
- Do not print keys, card data, customer personal data, or provider secrets.
- Do not run load tests against checkout or payment endpoints without explicit authorization.

## Related modules

- `adapters/wordpress.md` for WooCommerce implementation details.
- `adapters/nextjs-vercel.md` for storefront/server-action/caching behavior.
- `adapters/supabase-postgres.md` for order/inventory data integrity.
- `references/07-cross-layer-analysis.md` for payment/order/webhook tracing.
- `references/08-edge-case-library.md` for commerce scenarios.
