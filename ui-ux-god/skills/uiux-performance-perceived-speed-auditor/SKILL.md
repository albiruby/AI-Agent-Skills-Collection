---
name: uiux-performance-perceived-speed-auditor
description: "Audit loading performance and perceived responsiveness: LCP, INP, CLS, feedback latency, rendering, assets, and interaction delays. Use when a UI feels slow, when Core Web Vitals regress, or when loading and feedback states need measurement."
---

# Performance & Perceived Speed Audit

## Use when

- The UI feels slow even when the network looks fine.
- LCP, INP, CLS, or TTFB regressed or must be verified.
- Loading, skeleton, and feedback states need measurement.

## Do not use when

- The issue is purely visual with no timing component.
- You need backend profiling only; this is the perceived UI layer.

## Mission

Make the interface feel responsive while preserving correctness.

## Procedure

1. Establish performance scope and environment: device class, network profile, cache state, route, user state, and measurement tool. Capture baseline before optimizing.
2. For web, inspect Core Web Vitals and supporting diagnostics where available: LCP, INP, CLS, and relevant resource/rendering causes. Do not treat a single Lighthouse score as the whole user experience.
3. Inspect perceived loading: first meaningful content, skeletons, spinners, optimistic updates, progress indicators, disabled controls, and time-to-feedback after an action.
4. Find layout shifts from image dimensions, font swaps, late banners, injected content, and dynamic height changes. Check that loading placeholders preserve expected geometry.
5. Inspect blocking scripts, oversized images/fonts, repeated requests, hydration/render churn, long tasks, expensive animations, large DOM trees, and slow API dependencies when tools permit.
6. Prioritize by user impact and bottleneck evidence. Avoid micro-optimizing code that does not affect measured experience.
7. After changes, compare the same route, state, device, and network conditions. Record tradeoffs such as lower visual fidelity, delayed content, or reduced animation.
8. Coordinate with backend/network teams when the UI is waiting on remote work; do not claim a frontend fix resolves a server bottleneck.

## Precision defaults

- Core Web Vitals: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 (75th percentile).
- TTFB <= 800ms; feedback within 100ms for direct manipulation.
- Avoid long main-thread tasks > 50ms during interaction.
- Reserve media dimensions; lazy-load below the fold; compress/format images.

## Quality gates

- [ ] Measurements include reproducible conditions.
- [ ] Perceived feedback latency is considered alongside load metrics.
- [ ] CLS/layout shift causes are identified, not merely scored.
- [ ] Optimization does not hide errors or remove necessary content.

## Evidence to capture

- Metric values and collection conditions (device, network, cache).
- Trace/screenshot filmstrip and long tasks.
- Before/after measurements for each change.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/performance-budgets.md`
- `../../references/evidence-schema.md`
