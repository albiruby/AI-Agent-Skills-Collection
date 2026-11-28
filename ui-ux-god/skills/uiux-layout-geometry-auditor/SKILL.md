---
name: uiux-layout-geometry-auditor
description: "Measure rendered layout geometry, grid alignment, centering, dividers, spacing, overflow, clipping, and sibling symmetry. Use when auditing page structure, catching off-center logos or headers, incomplete divider lines, uneven cards, broken grids, horizontal scroll, or verifying layout fixes with DOM and pixel measurements."
---

# Layout, Grid & Geometry Audit

## Use when

- A page looks subtly wrong but the cause is not obvious from source code.
- You need exact centering deltas, divider spans, card symmetry, overflow, or clipping evidence.
- You are verifying a layout repair before and after the change.

## Do not use when

- The defect is purely typographic, color, or content-related with no geometry component.
- The layout intentionally uses editorial asymmetry; verify intent before flagging.

## Mission

Find and correct structural visual inconsistencies with measured evidence, down to 1px where it matters. A layout is not "a bit off"; it either follows a declared alignment rule or it does not.

## Procedure

1. Map the page into regions: app shell, header, primary navigation, main content, sidebars, cards, toolbars, footer, overlays, and nested sections. Determine the intended alignment axes and reading order.
2. Measure element bounds using DOM rectangles or native layout bounds whenever possible. Compare left/right edges, centers, baselines, gaps, padding, column widths, container widths, and vertical rhythm across peer elements.
3. Inspect parent-child layout logic before changing a child: flex/grid constraints, intrinsic sizing, min/max widths, overflow, sticky/fixed positioning, margins, gaps, box sizing, safe areas, and content-driven height.
4. Audit grid behavior: column count, gutter consistency, alignment across rows, card heights, responsive collapse, sidebar proportions, and whether content spans match the information hierarchy.
5. Check separators and rules: start/end alignment, visual length, thickness, color, inset, relationship to neighboring content, and whether the line belongs to the container or the viewport.
6. Diagnose common defects: header logo not centered within the viewport or available content region, nav items with inconsistent gaps, uneven card edges, clipped content, misaligned form labels, accidental horizontal scroll, inconsistent section widths, and baseline drift.
7. Choose the smallest structural correction that restores the layout rule. Prefer fixing the parent grid/flex constraint or shared token over one-off offsets. Use absolute positioning only when the design genuinely requires overlay positioning.
8. Re-measure at all affected breakpoints and verify that the correction did not create wrapping, overlap, clipping, or an unexpected scroll bar.

### Automated evidence

Run the geometry script against the live URL:

```bash
node ../../scripts/dom_geometry_audit.mjs --url http://localhost:3000 --out ./audit-out --routes /,/pricing
```

Run the pixel inspector on captured screenshots when optical centering or divider completeness is in question:

```bash
python ../../scripts/pixel_precision_audit.py --image ./audit-out/desktop-1440.png --out ./audit-out/annotated.png --json ./audit-out/pixel-report.json
```

## Precision defaults

- **Centering:** flag horizontal drift > **1.5px**; differences < **1.0px** are usually subpixel/DPR noise unless the design uses a hard grid.
- **Divider asymmetry:** flag > **2px**; decide full-bleed vs content-aligned before changing length.
- **Sibling cards:** compare height variance, top baselines, and internal padding; one outlier is a defect, a deliberate masonry layout is not.
- **Overflow:** flag `document.documentElement.scrollWidth > viewport + 1px` at **320px** and **375px**.
- **Overlap:** flag interactive boxes overlapping by more than **3px** in both axes.
- **Optical centering:** separate geometric center from ink center-of-mass; check SVG viewBox and transparent padding before applying a nudge.
- **Subpixel:** do not chase 0.5px differences caused by fractional flex tracks or non-integer zoom.

## Quality gates

- [ ] Alignment is judged against a declared axis or peer group, not vague visual intuition.
- [ ] A logo's geometric center and optical center are distinguished; transparent whitespace in the asset is checked before CSS offsets.
- [ ] Divider length is compared with its intended content/container boundary.
- [ ] One-off pixel nudges are not used to hide a broken parent layout.
- [ ] The fix is re-measured at the failing viewport and at least one neighboring breakpoint.

## Evidence to capture

- Selector and `file:line` for the offending element.
- Bounding boxes: element, container, and relevant siblings.
- Computed styles that explain the geometry: display, grid/flex properties, padding, margin, gap, width, position, overflow.
- Before/after screenshots with the same viewport, theme, and state.
- The exact delta in px and the tolerance used.

## Output

Return the standard finding record for each defect, plus the measured evidence and the structural fix. If no defect is found, state the regions, viewports, and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/micro-defect-catalog.md`
- `../../references/design-laws-formulas.md`
- `../../references/platform-capture-matrix.md`
- `../../templates/viewport-device-matrix.md`
