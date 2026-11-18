---
name: pra-functionality-ux
description: Audit routes and navigation, functional behavior, forms and submissions, external integrations (email, maps, analytics, booking, CAPTCHA) and user experience of a website. Use when the user asks to test all pages and flows, check links/404/redirects/deep links, verify the contact or career form really delivers, review mobile navigation, CTA clarity, loading/empty/error states, "cek semua halaman", "form tidak terkirim", "navigasi bermasalah", or UX friction before launch. Covers audit domains 33-37.
---

# Routes, Functionality, Forms, Integrations, UX (Domains 33–37)

Parent: `production-readiness-audit`. Prefer the **production build** (`next build && next start`) or the deployed preview; dev mode hides real problems. Lists: `references/checklist.md`.

## Procedure
1. **Route inventory (33)** from `pra-discovery`; compare with the sitemap/nav: every nav/footer/CTA link resolves (script a crawl with `curl -s -o /dev/null -w "%{http_code}"` or Playwright `request`), dynamic routes with valid/invalid/odd slugs (empty, very long, URL-encoded, uppercase, trailing slash), unknown route → custom 404 with correct 404 status, redirects (permanent vs temporary, no chains/loops), canonical host (www/apex), query params, deep links, refresh/back/forward behavior, anchor links, external links (`rel="noopener noreferrer"`, correct targets, not dead).
2. **Navigation components**: desktop/mobile/hamburger, dropdowns, sticky/transparent header over hero (contrast and stacking), z-index/pointer-event conflicts, focus handling, scroll locking, body scroll after closing menu, active-state accuracy, footer links.
3. **Functional pass (34)**: per page type (home, about, listing, detail, events, journal, careers, locations, collaboration, contact): content renders, CTAs work, carousel/gallery/marquee/modal/accordion/tabs behave (keyboard + touch), maps interactive, social share links, loading/empty/error/success states, content updates after CMS change (revalidation), preview vs production parity. Use Playwright when available; otherwise manual browser steps recorded as evidence.
4. **Forms (35)** — **never submit to production recipients without approval; use a test inbox/staging**: field inventory, required/optional rules, server-side validation (bypass client validation with `curl`), length/file limits, error and success messages, disabled state/double-submit protection, spam control (honeypot/CAPTCHA/rate limit), CSRF where applicable, where data goes (email/API/CMS), recipient config per environment, failure/retry behavior, privacy notice at the form, retention, monitoring of delivery failures. Delivery must be proven end-to-end in a test environment, not inferred from a 200 response.
5. **Integrations (36)**: for each third-party (Sanity API, email provider, Maps/Mapbox, analytics/Tag Manager, social, booking/reservation, payments, CAPTCHA, CRM): key restrictions (HTTP referrer / IP), quotas and billing, timeouts/retries, error handling and **fallback when the vendor is down**, privacy impact, status monitoring, cost. Maps: key restricted to production domains; fallback static link to Google Maps.
6. **UX (37)**: user journeys per audience (visitor wanting hours/menu, applicant, press, partner), information architecture, CTA clarity and ambiguity (links that leave the site without warning), dead ends, unnecessary steps, label clarity, feedback on interactions, excessive/unnecessary motion, scroll behavior, mobile reachability, cognitive load. Judge against the site's goal, not taste; cite the specific page/element.

## Calibration
- Primary nav link 404 or form that silently loses submissions → High.
- Wrong status code for 404 pages, redirect chains → Medium (SEO).
- Broken external link in a footer → Low; broken CTA on the home page → High.
- UX opinions → Low/Informational unless they block a flow.

## Output
Route table (URL · status · notes), flow test log (steps · result · evidence), form test matrix, integration register, UX observations (`FUNC-NNN`).

## Pitfalls
Testing only desktop · testing only in `next dev` · clicking "submit" on a real form · ignoring empty/error states · treating a 200 from a form API as delivery.
