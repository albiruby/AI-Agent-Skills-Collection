# Performance & Perceived Speed Budgets

Use these budgets when auditing loading performance, responsiveness, and perceived speed. Always record the measurement conditions: device, network, cache state, build, and percentile.

## 1. Core Web Vitals (field, 75th percentile)

| Metric | Good | Needs improvement | Poor | What it measures |
|---|---:|---:|---:|---|
| **LCP** — Largest Contentful Paint | <= 2.5s | 2.5–4.0s | > 4.0s | Main content visibility |
| **INP** — Interaction to Next Paint | <= 200ms | 200–500ms | > 500ms | Responsiveness to input |
| **CLS** — Cumulative Layout Shift | <= 0.1 | 0.1–0.25 | > 0.25 | Visual stability |

Supporting targets:

| Metric | Target | Notes |
|---|---:|---|
| **TTFB** | <= 800ms | Server/network baseline |
| **FCP** | <= 1.8s | First paint |
| **TBT** | <= 200ms | Lab proxy for long tasks |
| **Speed Index** | <= 3.4s | Visual completion |
| **Long task** | <= 50ms | Main-thread block during interaction |
| **Feedback latency** | <= 100ms | Direct manipulation feels instant |

## 2. Asset budgets (initial view)

| Asset | Budget | Rules |
|---|---:|---|
| HTML | <= 100KB compressed | Avoid huge inline data |
| CSS | <= 100KB compressed | Critical CSS inline where useful |
| JS (initial) | <= 200KB compressed | Split routes; defer non-critical |
| Fonts | <= 2 families, <= 4 weights | `font-display: swap`; subset; preload only critical |
| Hero image | <= 250KB | AVIF/WebP; responsive `srcset`; dimensions reserved |
| Above-the-fold images | <= 500KB total | Lazy-load below the fold |
| Third-party scripts | <= 3 critical | Audit each; async/defer; consent-gated |
| DOM nodes | <= 1,500 | Flag >3,000 |
| Requests (initial) | <= 50 | Flag >100 |

Budgets are starting points. Record the product’s actual policy if stricter.

## 3. Perceived speed

- Show a **pending state within 100ms** for any action that takes longer.
- Skeletons must match final geometry to avoid CLS; do not use a spinner that replaces a full layout.
- Prefer optimistic UI for reversible actions; reconcile on failure.
- Keep navigation feedback instant: active state, progress, or skeleton.
- Avoid blocking the main thread with large synchronous work; chunk or defer.
- Images: reserve `width`/`height` or `aspect-ratio`; use `loading="lazy"` below the fold; use `fetchpriority="high"` for LCP only.
- Fonts: `font-display: swap`, preload the critical face, avoid invisible text.
- Animations: transform/opacity only; avoid layout-triggering properties; honor reduced motion.

## 4. Measurement protocol

1. Record build/commit, device/CPU throttling, network profile, cache state, and viewport.
2. Measure **cold** and **warm** loads separately.
3. Use field data (CrUX/RUM) for the verdict; lab data for diagnosis.
4. Capture a filmstrip and a performance trace for any claimed bottleneck.
5. Measure before/after with the same conditions; report the delta, not just the new number.
6. Do not claim a Core Web Vitals improvement from a single lab run.

Useful commands (when the project has Lighthouse/Playwright):

```bash
npx lighthouse http://localhost:3000 --preset=desktop --output=json --output-path=./audit-out/lh-desktop.json
npx lighthouse http://localhost:3000 --preset=mobile --output=json --output-path=./audit-out/lh-mobile.json
```

## 5. Common UI performance defects

| Symptom | Likely cause | Check |
|---|---|---|
| Huge CLS on load | Images/ads/embeds without dimensions | Reserve space; inspect layout shifts |
| Slow LCP | Large hero, render-blocking CSS/JS, slow TTFB | Network waterfall; preload; compress |
| Bad INP | Long event handlers, heavy re-render, third-party tags | Performance trace; long tasks |
| Janky scroll | Layout thrash, heavy shadows/filters, large lists | Composite/layout counts; virtualize |
| Font flash | No `font-display`, late font load | Preload/subset; swap |
| Slow route change | No code splitting, blocking data | Bundle analysis; streaming |
| Input lag on mobile | 16px+ zoom, heavy JS, passive listeners | Device trace |

## 6. Report format

```markdown
| Metric | Before | After | Target | Conditions |
|---|---:|---:|---:|---|
| LCP | 4.1s | 2.3s | <=2.5s | Moto G4, Slow 4G, cold |
| INP | 340ms | 180ms | <=200ms | Same |
| CLS | 0.24 | 0.05 | <=0.1 | Same |
```

State what was **not** measured. A lab trace cannot prove field INP.
