---
name: uiux-iconography-asset-auditor
description: "Audit icons, logos, illustrations, SVGs, and interface assets for alignment, legibility, consistency, sizing, and semantic clarity. Use when icons look mismatched, logos sit off-center, SVG padding distorts alignment, or asset fidelity is suspect."
---

# Iconography & Asset Fidelity

## Use when

- Icons mix stroke weights, corner styles, or optical sizes.
- A logo looks off-center despite correct CSS centering.
- SVG, PNG, or illustration assets look blurry, clipped, or inconsistent across DPRs.

## Do not use when

- The issue is a layout container constraint rather than the asset itself.
- You need a full brand identity review; this is interface asset fidelity.

## Mission

Treat icons and brand assets as designed components, not decoration to nudge blindly.

## Procedure

1. Inventory icon sources: icon font, SVG set, inline vectors, image assets, emoji, CSS-drawn shapes, and platform-native symbols. Identify duplicate or inconsistent icon families.
2. Compare icon visual size, stroke/fill weight, optical center, baseline, viewBox, internal whitespace, aspect ratio, and alignment with neighboring text and controls.
3. Inspect logos separately from ordinary icons. Check correct brand variant, clear space, aspect ratio, source asset whitespace, intrinsic dimensions, scaling method, and container alignment.
4. Check whether an icon is decorative or carries meaning. Ensure meaningful icons have accessible names through the correct semantic mechanism; decorative icons should not create redundant announcements.
5. Inspect raster assets for blur, wrong density, compression, crop, transparency halos, background mismatch, and stretched proportions. Inspect vector assets for clipping and oversized viewBoxes.
6. Check consistency across states and sizes: active/inactive, light/dark, small/large, filled/outline, platform-specific variants, and icon-button hit areas.
7. Fix at source asset or shared component level where possible. Do not replace a bespoke brand symbol with a generic icon merely for visual uniformity.

## Precision defaults

- Standard icon sizes: 16/20/24px; one stroke weight per context (1.5px or 2px).
- Check SVG viewBox/transparent padding before CSS offsets.
- Decorative icons: `aria-hidden`; meaningful icons: accessible name.
- Check 1x/2x/3x rendering; avoid raster icons for UI glyphs.

## Quality gates

- [ ] Logo alignment accounts for internal whitespace and optical mass.
- [ ] Meaningful and decorative icons have correct accessibility treatment.
- [ ] No distorted aspect ratios or low-resolution assets at target density.
- [ ] Icon family and stroke weight are consistent within semantic groups.

## Evidence to capture

- Asset inventory with intrinsic dimensions, viewBox, and rendered size.
- Optical vs geometric bounds for logos and asymmetric glyphs.
- Screenshots at DPR 1 and 2.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/micro-defect-catalog.md`
- `../../references/design-laws-formulas.md`
