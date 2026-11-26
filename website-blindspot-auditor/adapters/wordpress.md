# Adapter: WordPress and WooCommerce

## Purpose

Inspect WordPress sites, themes, plugins, and WooCommerce stores. Focus on capability and nonce handling, REST/AJAX exposure, content rendering safety, uploads, caching of personalized content, plugin/theme risk, scheduled work, and operational hygiene.

## Detection signals

- `wp-config.php`, `wp-content/`, `wp-admin/`, `wp-includes/`.
- `wp-json` endpoints, `admin-ajax.php`, `xmlrpc.php`.
- Theme `functions.php`, custom plugins, mu-plugins.
- WooCommerce templates, `woocommerce` directories, order/product tables or APIs.
- Hosting panels or configuration referencing WordPress, WP-CLI, or a managed WordPress platform.

False positives: a static site may contain a `/blog` powered by a separate WordPress instance; confirm which host/domain and codebase are in scope.

## Applicability

Load when the target runs WordPress or WooCommerce and the audit includes authenticated behavior, plugins, content management, commerce, or server-side customization.

For a purely static exported site with no WordPress runtime, use `adapters/static-spa.md` and content/SEO checks instead.

## Boundaries and data flows

1. Anonymous visitor ↔ theme templates ↔ database/content.
2. Logged-in user ↔ roles/capabilities ↔ admin/REST/AJAX actions.
3. Editor/author ↔ content HTML ↔ frontend rendering.
4. Plugin ↔ third-party API/webhook/cron.
5. WordPress ↔ object cache/CDN/search index.
6. WooCommerce ↔ payment gateway ↔ order/inventory state.
7. Uploads ↔ filesystem/object storage ↔ public URLs.
8. WP-CLI/cron ↔ scheduled jobs ↔ notifications/cleanup.

Identify which plugins are active, their versions, and whether they are maintained. A plugin inventory is not proof of vulnerability; it is a lead for verification.

## Audit procedures

### A. Roles, capabilities, and authorization

- Enumerate roles and custom capabilities. Check for unintended privilege grants.
- Verify `current_user_can()` checks in custom code, not only nonces. A nonce proves intent/CSRF protection, not authorization.
- Inspect admin menus, custom post types, settings pages, bulk actions, and export/import features.
- Check REST routes for a real `permission_callback`; flag missing or always-true callbacks.
- Check AJAX handlers (`wp_ajax_*`, `wp_ajax_nopriv_*`) for capability and input validation.
- Check direct file access to plugin/theme files and any custom endpoints.

### B. Input, output, and content safety

- Look for unsafe SQL construction; `$wpdb->prepare` must be used correctly, including identifiers and `LIKE` patterns.
- Check escaping at output (`esc_html`, `esc_attr`, `esc_url`, `wp_kses` with a deliberate allowlist).
- Review shortcodes, blocks, widgets, and custom fields that render user or editor content.
- Check `unfiltered_html` exposure and whether lower-privileged roles can inject scripts.
- Review file uploads: type validation, filename handling, storage location, execution permissions, and public access.
- Inspect `unserialize`, object injection, SSRF-prone fetch functions, and unsafe redirects in plugins.

### C. REST, AJAX, and authentication

- Enumerate custom REST namespaces and routes; verify authentication and authorization per route.
- Check CORS configuration, application passwords, XML-RPC, and user enumeration surfaces.
- Verify login protection, rate limiting, MFA if present, and session behavior.
- Check password reset and email change flows for token handling and account takeover paths.
- Confirm whether the REST API exposes private data (users, drafts, order data) to unauthenticated callers.

### D. Caching and personalization

- Check page cache, object cache, CDN, and optimization plugins.
- Verify logged-in, cart, checkout, and personalized content is excluded from shared caches.
- Check cache invalidation after publish/update, product/stock changes, and plugin settings changes.
- Look for stale content served after a slug change, deletion, or role change.
- Inspect cookie-based cache bypass rules and whether they can be spoofed.

### E. Scheduled work, email, and operations

- Verify WP-Cron is actually triggered; a low-traffic site may miss schedules. Check server cron alternatives.
- Inspect custom scheduled events for idempotency, overlap, failure handling, and logging.
- Check transactional email deliverability, retries, and sensitive content in emails.
- Review backups, restore evidence, updates, staging, and rollback procedures.
- Check debug logging and whether logs, backups, or database exports are publicly accessible.
- Verify security headers and TLS at the edge/host.

### F. WooCommerce specifics

- Verify server-side price, tax, shipping, discount, and currency calculations.
- Check inventory races, cart persistence, checkout retries, and order state transitions.
- Inspect webhook signature verification, duplicate delivery, replay, and ordering.
- Check refunds, partial refunds, subscriptions, and entitlement revocation.
- Review guest checkout, account creation, address handling, and customer data exposure.
- Treat payment testing as high risk; use sandbox/test mode only with authorization.

## Verification methods

- WP-CLI read-only commands: `wp core version`, `wp plugin list`, `wp theme list`, `wp user list`, `wp cron event list`.
- Static review of theme/plugin code and `wp-config.php` (redact secrets).
- Browser inspection of authorized local/staging environments: roles, admin actions, checkout sandbox.
- `curl -sI` for headers; bounded checks of `robots.txt`, `sitemap.xml`, and public REST routes.
- Log inspection if provided, focusing on authentication, fatal errors, cron, and checkout failures.

## Common failure modes

- Nonce checks without capability checks.
- Custom REST routes with missing or permissive `permission_callback`.
- SQL injection in custom queries or plugin code.
- Stored XSS through post meta, shortcodes, widgets, or unfiltered HTML.
- Arbitrary file upload or executable uploads in a public directory.
- Cache serving logged-in/cart content to anonymous visitors.
- WP-Cron not running, duplicate scheduled events, or missed cleanup.
- Abandoned plugins with known vulnerabilities or incompatible PHP versions.
- Publicly exposed debug logs, backups, database dumps, or directory listings.
- WooCommerce overselling, duplicate orders, or webhook replay causing double fulfillment.
- User enumeration, weak login protection, or XML-RPC abuse.
- Staging site indexed or reachable with production data.

## Evidence requirements

- For capability issues: the action, the missing/incorrect check, the role that can reach it, and the resulting impact.
- For REST/AJAX exposure: route, authentication state, returned data or action, and whether it is reachable unauthenticated.
- For injection: the source-to-sink path and why input is not validated/parameterized; do not exploit production.
- For cache issues: cache configuration, personalization signal, and the path that could serve the wrong content.
- For plugin risk: plugin name/version/status and the specific behavior observed; a version number alone is not a finding.

## Safety constraints

- Do not install, update, deactivate, or delete plugins/themes.
- Do not modify options, users, roles, content, or database records.
- Do not run exploit payloads against production.
- Do not print database credentials, salts, API keys, or personal data.
- Do not test real payments; use sandbox mode with synthetic data.

## Related modules

- `adapters/ecommerce-and-payments.md` for deeper commerce analysis.
- `adapters/static-spa.md` for frontend/CDN behavior.
- `references/04-audit-domains.md` and `references/08-edge-case-library.md` for CMS/content scenarios.
- `references/09-evidence-and-prioritization.md` for severity and confidence.
