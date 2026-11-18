---
name: pra-cost-scalability
description: Audit cost, billing, resource usage, scalability and capacity of a Next.js/Vercel/Sanity website - plan limits and quotas (bandwidth, image optimization, functions, builds, Sanity API/asset limits), unexpected-spend risks, billing ownership, growth readiness (more brands/events/articles/images/traffic) and safe load/stress testing. Use when the user asks "biaya bulanan berapa?", will we hit limits, traffic spike readiness, Vercel/Sanity plan fit, image bandwidth, quota exhaustion, load testing, or whether the architecture can grow. Covers audit domains 70-73.
---

# Cost, Resources, Growth, Capacity (Domains 70–73)

Parent: `production-readiness-audit`. Pricing and limits change often — **verify current limits and prices from the vendors' official pricing/docs at audit time**; never quote them from memory as fact. Lists: `references/checklist.md`.

## Procedure
1. **Cost inventory (70)**: every paid service (hosting, CMS, domain, DNS, email, maps, monitoring, analytics, error tracking, AI/APIs, storage), plan, price, billing cycle/renewal date, billing owner and payment method (company vs personal card), alert thresholds/spend caps, seats, duplicates/unused subscriptions, per-month forecast and a worst-case spike scenario. Needs account access → otherwise ask the owner for the invoice list; mark Not Verifiable.
2. **Resource usage (71)**: current vs plan limits for bandwidth (esp. image/video), image-optimization transformations, function invocations/duration/memory, build minutes, Sanity API/CDN requests and asset storage, email quota, map loads, analytics events, log volume. Estimate **headroom** (months until limit at current growth) and what breaks first when exhausted (fail-open or hard stop?).
3. **Scalability (72)** — project growth axes (visitors, concurrent users, number of entities/events/articles/locations/gallery images, assets, API requests) and test architecture against each: static/ISR rendering vs per-request dynamic work, `generateStaticParams` and build-time growth (build duration with 500 pages?), listing pages without pagination, large GROQ results, heavy galleries, editorial workload, serverless limits, rate limits of third parties, cost growth curve, bottlenecks, scaling strategy. Use the multi-entity matrix in `pra-cms-sanity` for content growth.
4. **Capacity & stress testing (73)** — **no load tests on production without written approval and scope.** Prefer a preview/staging deployment with production-like config and test data; throttle, small ramps (k6/Artillery/autocannon); never hammer third-party APIs (Sanity, email, maps) from tests — mock or use sandbox. Measure p95 latency, error rate, rate-limit behavior, graceful degradation, recovery after spike, timeouts. Note that vendors may treat load tests as abuse; check their policy first.
5. **Cost-risk controls**: caching so traffic spikes hit CDN not functions; bot/scraper protection for image endpoints; remote image patterns restricted (prevents others from using your optimizer); budget alerts; hard caps where available.

## Calibration
- Commercial site on a plan whose terms or limits don't fit → Medium (confirm).
- No spend alert/cap on usage-billed services with public image endpoints → Medium.
- A page type whose build/query cost grows linearly with content without pagination → Medium (growth risk).
- Billing tied to a departed individual → High (see governance).

## Output
Cost table, quota headroom table, growth-scenario analysis, load-test plan/results (or "not run, why"), findings (`COST-NNN`).

## Pitfalls
Quoting stale prices · load-testing production · ignoring image bandwidth (usually the first limit) · assuming serverless scales infinitely and costs nothing.
