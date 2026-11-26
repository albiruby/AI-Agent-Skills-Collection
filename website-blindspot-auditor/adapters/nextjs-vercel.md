# Adapter: Next.js on Vercel

## Purpose

Inspect Next.js applications (App Router or Pages Router) deployed on Vercel or a similar platform. Focus on server/client boundaries, authorization placement, caching and revalidation, build-time versus runtime configuration, rendering failures, and deployment behavior.

This adapter assumes the framework is confirmed. It does not replace the universal audit or the product-specific profiles.

## Detection signals

- `next` in `package.json`, `next.config.js|mjs|ts`.
- `app/` with `page.tsx`, `layout.tsx`, `route.ts`, or `pages/` with `_app`, `_document`, `api/`.
- `middleware.ts` at the project root or `src/`.
- `"use server"` directives, server actions, `use cache` directives if present.
- `vercel.json`, `.vercel/`, Vercel environment configuration, or deployment metadata.
- Framework-specific scripts such as `next build`, `next start`, `next dev`.

False positives: a static export can resemble Next.js but have no server runtime; a monorepo may include Next.js apps that are not the target. Confirm the deployable unit before loading this adapter.

## Applicability

Load when the target includes a Next.js app and at least one of:

- authenticated or personalized behavior,
- server-side data fetching or mutations,
- caching/ISR/revalidation,
- deployment on Vercel or a comparable edge/CDN platform.

Skip framework-specific deep checks when the target is only static marketing output with no server behavior, but still check content, SEO, accessibility, and build integrity.

## Boundaries and data flows

Map these boundaries where present:

1. Browser ↔ React Server Components / client components.
2. Browser ↔ server action or route handler.
3. Server component / action ↔ data source, API, CMS, or payment provider.
4. Application ↔ Next.js cache (fetch cache, route cache, full route cache, data cache).
5. Application ↔ CDN/edge cache and image optimizer.
6. Build time ↔ runtime environment variables.
7. Preview deployment ↔ production data and authentication.
8. Vercel cron/queue/webhook integrations ↔ application state.

Identify which state is authoritative: the database, the CMS, the payment provider, the cache, or the client. Do not assume the rendered page reflects the authoritative state.

## Audit procedures

### A. Route and rendering model

- Enumerate routes, layouts, route groups, dynamic segments, parallel/intercepting routes, and route handlers.
- Distinguish server components, client components, server actions, and API routes. Note where data crosses the boundary.
- Check whether sensitive data is serialized into props sent to client components.
- Inspect loading, error, not-found, and streaming behavior. Can a partial failure render a misleading success state?
- Verify dynamic route parameters are validated before use.

### B. Authorization and trust boundaries

- For every mutation (server action, route handler, API route), verify authorization is enforced inside the handler, not only by hiding UI.
- Check object-level and tenant-level checks on every lookup, update, and delete.
- Inspect `middleware.ts` matcher and logic. Middleware can redirect or rewrite, but confirm it actually protects the affected routes and cannot be bypassed by direct requests.
- For server actions, verify the caller, allowed origin assumptions, and input validation. Do not assume framework defaults cover business authorization.
- Check preview/draft mode: who can enable it, what data it can expose, and whether preview deployments are publicly reachable.
- Check admin routes, internal tools, and feature-flagged surfaces that may not appear in navigation.

### C. Caching, freshness, and personalization

- Identify cacheable versus personalized data. Look for `force-cache`, `no-store`, `revalidate`, `dynamic`, `fetchCache`, `unstable_cache`, `revalidatePath`, `revalidateTag`, and route segment config.
- Check whether user-specific data can enter a shared cache key. Verify cache keys include tenant/user scope where required.
- Trace content/pricing/entitlement updates through revalidation to the rendered page.
- Check stale-while-revalidate behavior and whether stale data can authorize an action, show a wrong price, or expose an unpublished document.
- Inspect image optimization and remote image allowlists for abuse or unexpected fetching.

### D. Secrets and client exposure

- Search for `NEXT_PUBLIC_` variables and confirm none contain secrets or privileged tokens.
- Check whether server-only modules are imported into client components; look for `server-only` usage where appropriate.
- Inspect error messages, stack traces, source maps, and build logs for leaked configuration.
- Verify environment separation: preview must not silently use production secrets or production data.
- Never print secret values; report the variable name and exposure path.

### E. Failure behavior and resilience

- Check error boundaries, fallback UI, retry behavior, and timeout handling for server actions and data fetching.
- Verify mutations are idempotent or guarded against duplicate submission.
- Check what happens when a downstream API, CMS, payment provider, or auth provider is slow or unavailable.
- Inspect race conditions between revalidation, client navigation, and background jobs.

### F. Deployment and operations

- Verify build-time variables versus runtime variables; a variable present at build may not be present at runtime.
- Check preview deployment protection, password protection, and whether preview URLs are indexed or shared.
- Inspect Vercel cron jobs, webhooks, and background functions for authentication, retries, and observability.
- Check deployment skew: old client bundles or server instances may call new APIs after a release.
- Verify redirects, rewrites, headers, and custom domains in `next.config.*` and platform configuration.

## Verification methods

- Static inspection of route trees, handlers, middleware, configuration, and data access.
- Read-only build output inspection (`.next`) for route and cache metadata.
- Browser inspection of local/preview environments: network requests, cache headers, console errors, navigation, back/forward, multiple tabs.
- Header checks with `curl -sI` on authorized environments.
- Targeted tests using existing test infrastructure; do not install tools without permission.
- Log inspection if provided, focusing on authorization failures, 5xx errors, revalidation, and deployment timestamps.

## Common failure modes

- Authorization only in middleware or UI, missing inside server actions/route handlers.
- `NEXT_PUBLIC_` secret exposure or privileged token in a client bundle.
- User-specific data cached in a shared route/fetch cache and served to another user.
- Stale ISR/page data used for pricing, entitlement, inventory, or publication state.
- Draft/preview mode reachable by unauthorized users or connected to production data.
- Build-time environment values differing from runtime expectations.
- Direct route-handler access bypassing page-level guards.
- Duplicate mutation on retry or double submit.
- Old and new deployments coexisting with incompatible API payloads or cache keys.
- Error boundaries hiding a failed mutation as a successful state.

## Evidence requirements

- For authorization claims: the handler/route, the missing or incorrect check, the actor who can reach it, and the resulting data/action.
- For cache claims: the cache directive/config, the data scope, and the path by which one user's data could be served to another or become stale.
- For secret exposure: variable name, file/bundle location, and exposure path — never the value.
- For deployment claims: configuration or observed behavior, environment, and version/time if available.

A framework pattern alone is not proof of runtime impact. State whether the finding is static, reproduced, or inferred.

## Safety constraints

- Do not trigger revalidation, cache purge, deployments, or cron jobs in production without explicit authorization.
- Do not access preview deployments or accounts beyond the authorized scope.
- Do not run load tests against Vercel or production.
- Do not modify environment variables or project settings.
- Do not print secrets, tokens, or private URLs in the report.

## Related modules

- `adapters/supabase-postgres.md` for common data/auth backends.
- `adapters/ecommerce-and-payments.md` for checkout, webhooks, and entitlements.
- `adapters/static-spa.md` for client-only or static-export behavior.
- `references/07-cross-layer-analysis.md` for cache/version-skew tracing.
- `references/08-edge-case-library.md` for scenario prompts.
