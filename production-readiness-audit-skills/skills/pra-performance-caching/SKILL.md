---
name: pra-performance-caching
description: Audit web performance and caching of a Next.js site - Core Web Vitals (LCP, INP, CLS, TTFB), image/video/font loading, JavaScript bundle size and hydration cost, third-party scripts, Sanity/GROQ data-fetching, Next.js caching layers (Data Cache, Full Route Cache, ISR, revalidateTag), Vercel CDN and cache headers. Use when the user asks about speed, Lighthouse/PageSpeed, "website lambat", LCP/CLS/INP, bundle analyzer, image optimization, font loading, cache not updating after CMS publish, ISR/revalidation, or CDN configuration. Covers audit domains 40-45.
---

# Performance & Caching (Domains 40–45)

Parent: `production-readiness-audit`. Measure the **production build** (or deployed production/preview), never `next dev`. Label every number as **lab** (Lighthouse/WebPageTest) or **field** (CrUX/RUM, p75). Lists: `references/checklist.md`.

## Targets (p75 field data when available)
LCP ≤ 2.5 s · INP ≤ 200 ms · CLS ≤ 0.1. TBT and Speed Index are diagnostics, not pass/fail. Also set pragmatic budgets for JS, images, fonts, third-party scripts (e.g. initial JS ≤ ~170 KB gz for content sites as a starting point — justify any chosen budget).

## Procedure
1. **Baseline**: Lighthouse (mobile preset, slow-4G/4× CPU throttle, 3 runs, median) for each page type; PageSpeed Insights/CrUX for the production URL if public; record device/network profile. Note TTFB, FCP, LCP element, CLS sources, long tasks.
2. **Waterfall**: Chrome DevTools/Playwright trace or WebPageTest; request count, blocking resources, priority, third-party weight, duplicate requests, redirect hops.
3. **Images/media (41)**: use `next/image` (or equivalent) with correct `sizes`; LCP/hero image `priority`/`fetchpriority="high"`, never lazy; others lazy; dimensions reserved (no CLS); formats AVIF/WebP; Sanity image URLs with `auto=format`, width/quality params via `@sanity/image-url`; no multi-MB originals served; galleries/carousels load offscreen images lazily; video: compressed, `poster`, `preload="none"` or `metadata`, muted autoplay rules, no background video on mobile unless justified; `remotePatterns` correct; image-optimization quota (Vercel) impact.
4. **Fonts/CSS (42)**: `next/font` or self-hosted, subsets, only used weights, `font-display: swap|optional`, preload only critical, fallback metrics (`size-adjust`) to limit CLS, no render-blocking third-party CSS, unused CSS, Tailwind purge correctness.
5. **JS/bundles (43)**: `@next/bundle-analyzer` (`ANALYZE=true next build`) or `next build` route table; look for heavy libs (moment, lodash full, icon packs, animation/3D libs, map SDKs), duplicate versions, unnecessary `'use client'` pushing server components into the client bundle, missing `dynamic()` for below-the-fold/heavy widgets, third-party tags (analytics, chat, pixels) — measure each one's main-thread cost; hydration cost; long tasks; memory growth on carousels/marquees.
6. **Data fetching (44)**: server fetching in parallel (`Promise.all`), no waterfalls, no N+1 queries, GROQ projections only (no `...`), payload sizes, pagination, timeouts/retries, CMS query latency (time each query), unnecessary dynamic rendering (use of `cookies()/headers()/searchParams` forcing dynamic), `export const dynamic`/`revalidate` consistency.
7. **Caching & CDN (45)**: identify the model per route (static / ISR / dynamic). Check `Cache-Control`, `x-vercel-cache` (HIT/MISS/STALE), `age`; Sanity CDN (`useCdn`) vs API; `revalidate` values vs how often content changes; on-demand revalidation by tag/path wired to a **signed** webhook; verify the cycle: publish test change in staging → page updates; draft/preview data never cached publicly; authenticated/personalized responses not cached; static asset immutable caching; cache keys (query-string variants, `Vary`); bot/crawler behavior on cold cache; behavior after rollback (stale cache) .
8. **Regression guard**: is there a performance budget or Lighthouse CI? Is RUM present (see `pra-monitoring-observability`)?

## Calibration
- LCP > 4 s or CLS > 0.25 on home/primary landing (lab, mobile) → High; 2.5–4 s / 0.1–0.25 → Medium.
- Hero image lazy-loaded or 4 MB → Medium–High. A single 3rd-party script adding >300 ms TBT → Medium.
- Content published in CMS not appearing on site → High (functional).
- Over-fetching queries on low-traffic pages → Low.
Lab results on a developer laptop without throttling are not evidence of "fast".

## Output
Metrics table (page · LCP · INP* · CLS · TTFB · JS KB · requests · lab/field), top bottlenecks with evidence, cache map per route, findings (`PERF-NNN`) with expected gain and effort.

## Pitfalls
Optimizing from a single run · mixing lab and field data · measuring on localhost · recommending memoization where the cost is images/third parties · enabling aggressive caching on preview/draft data.
