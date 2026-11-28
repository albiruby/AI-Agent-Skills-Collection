---
name: uiux-cross-browser-device-auditor
description: "Audit rendering and interaction consistency across browsers, engines, devices, DPRs, operating systems, and input modes. Use when a UI works in one browser but breaks in another, or when Safari/Firefox/Edge/mobile rendering, fonts, scrolling, or input need verification."
---

# Cross-Browser & Device Compatibility

## Use when

- A layout or interaction works in Chrome but breaks in Safari, Firefox, or Edge.
- Fonts, scrollbars, sticky elements, backdrop filters, or input zoom differ by browser.
- You need a device/DPR compatibility matrix.

## Do not use when

- The issue reproduces identically everywhere and is a single layout bug.
- You only need native app testing.

## Mission

Separate true product defects from environment-specific rendering variation.

## Procedure

1. Build a support matrix from product policy, audience, analytics, and the current browser/device support statement. Do not invent a supported-browser policy.
2. Test representative engines and versions, including Chromium, WebKit, and Firefox where applicable, plus target mobile browsers and embedded webviews.
3. Compare layout geometry, font metrics, form controls, sticky/fixed behavior, viewport units, scrollbars, overflow, SVG, canvas, filters, gradients, focus rings, and media behavior.
4. Record OS, browser version, viewport, DPR, zoom, font environment, color scheme, reduced motion, locale, and network conditions for each reproduction.
5. Check pointer, touch, keyboard, and hybrid input. Test browser back/forward, refresh, direct deep link, private/session context, and offline fallback where relevant.
6. Use same-environment baselines for visual comparison. Rendering can vary by OS, fonts, hardware, browser build, and headless mode; do not classify all screenshot differences as regressions.
7. Fix standards-based compatibility issues with progressive enhancement and targeted fallbacks. Avoid broad user-agent sniffing unless unavoidable and documented.
8. Retest the exact failing environment plus a representative unaffected environment.

## Precision defaults

- Test Chromium, Firefox, WebKit/Safari, and Edge where available.
- Test DPR 1 and 2; check 1px hairlines and raster assets.
- iOS input font-size >= 16px to avoid auto-zoom.
- Check scrollbar-gutter, `100dvh`, sticky, backdrop-filter, and font fallback.

## Quality gates

- [ ] Support matrix is explicit.
- [ ] Screenshot comparison uses consistent environment settings.
- [ ] Browser-specific workarounds are narrow and justified.
- [ ] Every compatibility finding records its reproduction environment.

## Evidence to capture

- Browser/engine/version, OS, device, DPR, and input mode.
- Side-by-side screenshots and console/network diffs.
- Known-engine-specific CSS/JS behavior.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../references/platform-ui-standards.md`
