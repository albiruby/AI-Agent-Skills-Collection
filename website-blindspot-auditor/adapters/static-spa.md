# Adapter: Static Sites and Single-Page Applications

## Purpose

Inspect static or CDN-hosted sites and client-rendered applications. Focus on routing and indexability, client-side exposure, API trust, caching, service workers, third-party forms, and deployment/version behavior.

This adapter covers marketing sites, documentation, static exports, and SPAs built with React, Vue, Svelte, Angular, or similar frameworks.

## Detection signals

- Build output (`dist/`, `build/`, `out/`, `public/`) and static hosting configuration.
- `index.html` with a client-side router; routes resolved in the browser.
- React Router, Vue Router, SvelteKit static adapter, Angular router, or similar.
- Service worker/manifest files.
- CDN/hosting configuration (Netlify, Vercel static, Cloudflare Pages, GitHub Pages, S3/CloudFront, Nginx).
- Client-side API calls with public keys or tokens.

False positives: a statically generated framework may still have server functions or edge middleware; inspect the deployment model before concluding there is no backend.

## Applicability

Load when the target is primarily static or client-rendered. Combine with `adapters/nextjs-vercel.md` if a Next.js app uses static export or hybrid rendering, and with `adapters/supabase-postgres.md` if the client talks directly to a database service.

## Boundaries and data flows

1. Browser ↔ CDN/host ↔ static assets.
2. Browser router ↔ deep links/refresh ↔ host rewrite rules.
3. Browser ↔ third-party API/service (auth, forms, database, analytics).
4. Build pipeline ↔ environment variables ↔ bundle.
5. Service worker ↔ cache ↔ network ↔ new deployment.
6. CDN cache ↔ HTML/assets ↔ deployment invalidation.
7. Client storage (localStorage/sessionStorage/IndexedDB/cookies) ↔ session/state.

Identify which data is public by design and which is protected only by client behavior. Client-side checks are not authorization.

## Audit procedures

### A. Routing, hosting, and indexability

- Test deep links, refresh, trailing slashes, case sensitivity, unknown routes, and 404 behavior.
- Verify the host's SPA fallback does not turn every missing page into a 200 index page.
- Check canonical URLs, redirects, trailing-slash policy, and mixed http/https or www/non-www behavior.
- Check `robots.txt`, `sitemap.xml`, meta robots, and whether primary content exists in the initial HTML.
- For content-heavy sites, verify whether search engines can see rendered content; test with JavaScript disabled.
- Check Open Graph/social previews for dynamic routes and share URLs.

### B. Client-side exposure and API trust

- Inspect bundles for secrets, privileged tokens, internal endpoints, and debug configuration.
- Distinguish public keys (expected) from service keys (must never ship).
- Identify APIs called directly from the browser. Verify authentication, authorization, rate limits, and input validation on the server.
- Check whether access control relies on hidden UI, route guards, or client-side role checks.
- Check CORS configuration and whether it allows unintended origins with credentials.
- Check third-party scripts for data leakage and consent behavior.

### C. Sessions and client storage

- Check where tokens/session data are stored and the XSS/CSRF implications.
- Verify logout, expiry, refresh, and multi-tab behavior.
- Check whether cached data survives logout or is visible to another user on the same device.
- Verify password reset, email verification, and account deletion flows.
- Check deep links that carry tokens or sensitive parameters (URL leakage, referrer).

### D. Caching, service workers, and deployment

- Check `Cache-Control` for HTML vs hashed assets; HTML should not be cached indefinitely.
- Verify service worker update behavior; stale caches can serve an old app against a new API.
- Check cache invalidation after deployment and whether old chunks 404 for open tabs.
- Verify build-time environment values and whether preview/staging builds point at the right backend.
- Check redirects/rewrites and custom headers at the host/CDN.

### E. Forms, integrations, and content

- Verify forms actually deliver: endpoint, validation, spam protection, success/error states, retries.
- Check third-party embeds (maps, chat, video, payment links) for privacy, consent, and failure behavior.
- Check content accuracy, broken links, stale pricing/claims, and placeholder text.
- Check accessibility: semantics, keyboard, focus, contrast, zoom, reduced motion, media alternatives.
- Check performance: image/font weight, render-blocking resources, layout shift, third-party scripts.

## Verification methods

- Static inspection of built assets, configuration, and source.
- Browser inspection with JavaScript disabled, network throttling, and cache disabled.
- `curl -sI` for headers and cache behavior; bounded link checks.
- Lighthouse/axe if already available and authorized; otherwise manual checks.
- Service worker inspection in DevTools (application/cache storage).
- Host/CDN configuration review.

## Common failure modes

- SPA fallback returning 200 for missing pages, harming SEO and error handling.
- Content invisible without JavaScript when indexability matters.
- Secrets or privileged keys in the bundle.
- APIs trusting the client for authorization or price.
- Tokens in localStorage combined with an XSS sink.
- Service worker serving stale app shells after deployment.
- HTML cached too aggressively, showing stale prices/content.
- CORS allowing arbitrary origins with credentials.
- Forms failing silently or delivering to the wrong destination.
- Third-party scripts loading before consent.
- Deep links broken on refresh or shared with the wrong base URL.
- Old chunks 404 after deploy for open tabs.

## Evidence requirements

- For exposure: the bundle/file, the secret or privileged value type, and why it is reachable — never the value.
- For API trust: the request, the client-supplied field, the server behavior, and the resulting unauthorized effect.
- For routing/SEO: URL, response status, rendered content, and crawler-visible output.
- For cache/service worker: cache header or worker logic, the stale content observed, and the deployment/version context.

Client-side code alone may be conclusive for exposure but not for server-side impact. State what was observed versus inferred.

## Safety constraints

- Do not crawl production aggressively or bypass rate limits.
- Do not test destructive actions or authenticate with real customer accounts.
- Do not modify CDN, DNS, or hosting configuration.
- Do not print secrets or personal data found in bundles.

## Related modules

- `adapters/nextjs-vercel.md` for hybrid/static Next.js deployments.
- `adapters/supabase-postgres.md` for direct browser-to-database access.
- `references/04-audit-domains.md` for SEO, accessibility, performance, and content.
- `references/08-edge-case-library.md` for browser/storage/cache scenarios.
