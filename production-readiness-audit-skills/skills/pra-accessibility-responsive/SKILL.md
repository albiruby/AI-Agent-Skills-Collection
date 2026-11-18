---
name: pra-accessibility-responsive
description: Audit accessibility (WCAG 2.2 AA - semantics, keyboard, focus, screen reader, contrast, motion, touch targets, carousels/modals/menus) and responsive/cross-browser behavior (320-2560 px viewports, iOS Safari, Android Chrome, Firefox, Edge, zoom/reflow). Use when the user asks for an a11y audit, WCAG check, screen-reader/keyboard test, color contrast, reduced motion, "cek responsif", "tampilan rusak di HP", horizontal scroll, Safari bug, or mobile/tablet/desktop QA. Covers audit domains 38-39.
---

# Accessibility & Responsive/Cross-Browser (Domains 38–39)

Parent: `production-readiness-audit`. Target: **WCAG 2.2 Level AA** assessment. Automated tools find ~30–40% of issues; manual checks are required and must be reported separately. Lists: `references/checklist.md`.

## Procedure
### Accessibility (38)
1. **Automated pass** on each page type and each state (menu open, modal open, form error): axe-core / `@axe-core/playwright`, Lighthouse a11y, `eslint-plugin-jsx-a11y` (static). Record rule IDs and counts; de-duplicate by root cause.
2. **Manual keyboard pass**: Tab/Shift+Tab through every page — visible focus (2.4.7, 2.4.11 not obscured), logical order, no traps except intentional modal traps with Esc to exit and focus return, skip link, all interactions reachable (hover-only menus, carousels, custom dropdowns), no keyboard-inaccessible click handlers on `div`s.
3. **Semantics**: one `h1`, logical heading hierarchy, landmarks (`header/nav/main/footer`), lists/tables semantics, `lang` attribute, buttons vs links used correctly, accessible names (icon-only buttons, social links, carousel arrows), form labels/instructions/error association (`aria-describedby`, `aria-invalid`), live-region announcements for async status, valid ARIA (no ARIA better than bad ARIA).
4. **Media**: meaningful vs decorative images (`alt=""`), CMS alt-text coverage, video captions/transcripts where speech exists, autoplay/pause controls (2.2.2), no content conveyed by color alone.
5. **Visual**: contrast (text 4.5:1, large 3:1, UI components/focus 3:1) — check text over hero images/videos and transparent headers at multiple scroll positions; 200% text resize and browser zoom; 400% reflow at 320 CSS px without two-dimensional scroll; text spacing override; target size (2.5.8 ≥ 24×24 CSS px).
6. **Motion**: `prefers-reduced-motion` respected for parallax/marquee/autoplay/transitions; no flashing; pause/stop for moving content > 5 s.
7. **Screen reader smoke test** (VoiceOver/NVDA, or accessibility-tree inspection in browser devtools when unavailable — label as such): nav, a form, a modal, a carousel.
8. **WCAG 2.2 additions**: dragging alternatives (2.5.7), consistent help (3.2.6), accessible authentication (3.3.8) if login exists, redundant entry (3.3.7).

### Responsive & cross-browser (39)
1. Viewports: **320, 360, 375, 390, 412, 430, 768, 820, 834, 1024, 1280, 1366, 1440, 1600, 1920, 2560** px, portrait + landscape for mobile/tablet; also 200% zoom and 400% reflow.
2. Per viewport/page type: no horizontal scroll, text wraps, images scale/crop sensibly, hero height (use `dvh/svh` not `100vh` on mobile Safari), header/nav positioning and safe-area insets, grids/columns collapse, carousels/marquees, modals fit the screen, dropdown positioning, sticky/fixed elements not covering content, hover fallbacks on touch, font/spacing scaling, long names/strings.
3. Browsers: Chrome, Edge, Firefox, Safari (macOS), iOS Safari, Android Chrome; real device or BrowserStack/Playwright WebKit/Firefox/Chromium. Look for browser-specific CSS (`:has`, container queries, `backdrop-filter`, `100vh`, `aspect-ratio`, `scrollbar-gutter`), video autoplay policies, form control rendering, `position: sticky` in overflow containers.
4. Evidence: screenshots per viewport/browser with file names; matrix of covered vs not covered.

## Calibration
- Keyboard trap or unreachable primary nav/form → High. Missing form labels on contact form → High–Medium. Contrast failure on body text → Medium; on decorative text → Low.
- Horizontal scroll on mobile home page → Medium–High. Layout broken in Safari for core page → High.
- Report each WCAG failure with the Success Criterion (e.g. 1.4.3), element, and fix.

## Output
Accessibility findings (`A11Y-NNN`) with SC mapping, manual vs automated split, responsive/browser matrix (covered/not covered), screenshots list. State plainly that conformance cannot be certified from an agent audit alone.

## Pitfalls
Passing axe and claiming WCAG AA · testing only a default viewport · ignoring states (open menu, error messages) · using hover as the only affordance · forgetting reduced motion.
