# UI/UX Quality Assurance Checklist

## Visual structure

- [ ] Page hierarchy, container width, grid, gutters, alignment, and section rhythm are coherent.
- [ ] Header/logo alignment is checked against actual asset bounds and the intended center axis.
- [ ] Dividers and borders align with the intended text, card, container, or viewport boundary.
- [ ] Typography wraps without clipping, overlap, awkward truncation, or unstable font loading.
- [ ] Icon size, stroke, optical alignment, and accessible meaning are consistent.
- [ ] Images preserve intended crop, ratio, focal point, and responsive quality.
- [ ] Cards in the same row have consistent height/baseline/CTA alignment.
- [ ] Concentric radii follow `R_inner = max(0, R_outer - padding)`.
- [ ] Shadows/elevation share one light direction; dark mode uses surface steps.

## Responsive and platform

- [ ] 320, 375, 768, 1024, 1440, and 1920 widths checked (as applicable).
- [ ] Intermediate widths checked, not just preset breakpoints.
- [ ] No horizontal page scroll at 320/375 except intentional table scrollers.
- [ ] 200% text resize and 400% zoom/reflow are usable.
- [ ] Mobile safe areas, keyboard avoidance, and orientation are handled.
- [ ] Desktop minimum window size, titlebar clearance, and 125/150/200% DPI are handled.
- [ ] CLI/TUI aligns at 80 and 120 columns; wide Unicode is width-checked.
- [ ] Browser/engine differences (Safari/Firefox/Edge) are checked where relevant.

## Interaction and states

- [ ] Default, hover, focus-visible, active, disabled, loading, empty, error, and overflow states exist.
- [ ] Hover does not shift layout.
- [ ] Focus ring is visible on every surface and theme.
- [ ] Touch targets >= 44/48px (24px WCAG floor with spacing).
- [ ] Sticky headers do not cover anchor targets or focused elements.
- [ ] Modals/drawers trap focus, close on Escape, and restore focus.
- [ ] Buttons lock during pending actions; no double submit.
- [ ] Long/localized strings, 0 items, 999+ badges, and slow networks are tested.

## Accessibility

- [ ] Keyboard-only path completes every core task.
- [ ] Tab order is logical; no keyboard trap.
- [ ] Headings, landmarks, labels, and table semantics are correct.
- [ ] Images have appropriate alt; decorative icons are hidden.
- [ ] Form errors are associated and announced.
- [ ] Contrast: 4.5:1 body, 3:1 large text/UI.
- [ ] Reduced motion is respected.
- [ ] Language (`lang`) and page title are set.
- [ ] Automated scan results are manually verified; no conformance claim from a scan alone.

## Content and trust

- [ ] Terminology is consistent.
- [ ] Error copy explains what happened, why, and how to fix.
- [ ] Empty states explain value and provide an action.
- [ ] Destructive actions are confirmed or reversible.
- [ ] No placeholder/lorem/“Coming soon” in production surfaces.
- [ ] Dates, numbers, currency, and timezone are correct for the locale.

## Performance and media

- [ ] LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 (field, 75th percentile) where measurable.
- [ ] Images are responsive, compressed, dimensioned, and lazy-loaded below the fold.
- [ ] Fonts use `font-display: swap`; no invisible text.
- [ ] No obvious layout shift from ads/embeds/dynamic content.
- [ ] Long lists/tables are paginated or virtualized where needed.

## Release gate

- [ ] All P0/P1 findings fixed or explicitly accepted with owner.
- [ ] Every claimed fix has before/after evidence.
- [ ] Visual regression/E2E checks pass (where available).
- [ ] Coverage and limitations are documented.
- [ ] No secrets/personal data in screenshots or reports.
