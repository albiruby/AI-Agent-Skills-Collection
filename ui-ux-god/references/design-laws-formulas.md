# Measurable Design System Laws & Formulas

Reference equations for auditing visual craft with objective precision.

## 1. Concentric Border-Radius Formula

When a rounded element sits inside a rounded parent container with padding:

```
R_inner = max(2px, R_outer - P_padding)
```

- Example: Outer card `rounded-2xl` (`16px`) with `p-2` (`8px`) -> Inner image/card MUST be `rounded-lg` (`8px`), NOT `rounded-2xl` (`16px`).
- Why: Matching inner and outer radii creates uneven diagonal corner thickness that looks pinched and amateurish.

## 2. Typographic Vertical Rhythm & Scale

- **Modular Type Ratios**: Minor Third (`1.200`) for dense SaaS dashboards; Major Third (`1.250`) for general web apps; Perfect Fourth (`1.333`) for marketing/editorial landing pages.
- **Line-Height by Role**:
  - Display / H1 (`>= 36px`): `1.05 - 1.15` (tight tracking `-0.02em` to `-0.03em`)
  - Section Headings H2/H3 (`20px - 32px`): `1.20 - 1.30` (tracking `-0.01em`)
  - Body Prose (`14px - 18px`): `1.50 - 1.65` (tracking `0`)
  - Micro Labels / Uppercase Eyebrows (`11px - 12px`): `1.30 - 1.40` (wide tracking `+0.06em` to `+0.10em`)
- **Optimal Measure (Line Length)**: `45ch - 75ch` (`max-w-prose` / `65ch` ideal). Lines over `80ch` cause eye-tracking fatigue.
- **Data & KPI Numerals**: Always apply `font-variant-numeric: tabular-nums` (`tabular-nums` in Tailwind) on prices, tables, timers, and dashboards.

## 3. Spatial Rhythm & Gestalt Proximity

- **Base Grid**: Snap all spacing to `4px` increments (`4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96`).
- **Proximity Inequality**:
  - `gap(section_A, section_B) >= 2 * gap(card_internal_padding)`
  - `margin_top(heading) >= 1.5 * margin_bottom(heading)` so headings visually belong to the content below them, not above them.

## 4. Contrast & Color Balance

- **WCAG 2.2 AA Floors**:
  - Normal text (`< 24px` regular or `< 18.67px` bold): `>= 4.5:1`
  - Large text (`>= 24px` regular or `>= 18.67px` bold): `>= 3.0:1`
  - Non-text UI boundaries (inputs, toggles, active icons, focus rings): `>= 3.0:1`
- **60-30-10 Visual Weight Rule**: ~60% neutral canvas/surfaces, ~30% secondary structural containers/text hierarchy, ~10% high-emphasis brand accent & primary CTAs.
- **Dark Mode Surface Elevation**: Avoid pure `#000000` with pure `#FFFFFF` body text (causes halation). Use elevated charcoal steps (`#0B0D12` -> `#12151E` -> `#1A1F2E`) with `#E5E7EB` primary text and `rgba(255,255,255,0.08)` borders.

## 5. Optical Centering

Geometric center is not optical center. For asymmetric shapes:

```text
optical_offset = ink_center - bounding_box_center
```

- Measure ink bounds (non-transparent pixels), not the asset box.
- Play triangles usually need **+1 to +2px** toward the flat side.
- Chevrons/arrows need a nudge toward the direction of motion, not the flat side.
- Wordmarks with a protruding tail need a nudge away from the tail.
- Never apply an optical nudge until you have checked the SVG `viewBox` and transparent padding.
- An optical nudge is a deliberate design correction; record the value and reason.

## 6. Elevation & Shadow Physics

- Use one light source, typically top-down: `box-shadow: 0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.08)`.
- Elevation is a hierarchy signal: base surface, raised card, sticky bar, modal, toast.
- Dark mode: shadows are weak; use surface luminance steps plus a 1px top/edge highlight.
- Avoid huge blurred black shadows on every card; they flatten hierarchy and cost paint time.
- Shadow direction must be consistent across sibling components.

## 7. Grid & Container Math

- Content container: `max-width` between **64rem and 80rem** for marketing, **72rem** is a common default.
- Gutter: **16px** compact, **24px** standard, **32px** spacious.
- Column gap should be equal to or a multiple of the base spacing unit.
- Full-bleed section inside a padded container:

```css
.full-bleed {
  width: 100%;
  margin-inline: calc(50% - 50vw);
}
```

Beware `100vw` scrollbar overflow; prefer a wrapper or `100%` where possible.

- Sidebar layouts: `grid-template-columns: minmax(0, 1fr) 280px` rather than fixed widths that break at 1024px.
- Use `minmax(0, 1fr)` to prevent long content from blowing out a grid track.

## 8. Type Scale Examples

| Role | Size | Line-height | Tracking |
|---|---|---|---|
| Display | 48–72px | 1.05–1.15 | -0.02em to -0.03em |
| H1 | 36–48px | 1.10–1.20 | -0.02em |
| H2 | 28–36px | 1.20–1.30 | -0.01em |
| H3 | 20–24px | 1.25–1.35 | 0 |
| Body | 16–18px | 1.50–1.65 | 0 |
| Small | 13–14px | 1.40–1.50 | 0 |
| Eyebrow | 11–12px | 1.30–1.40 | +0.06em to +0.10em |

Scale ratios: 1.200 (dense SaaS), 1.250 (general app), 1.333 (marketing/editorial). Do not mix ratios without a reason.

## 9. Visual Hierarchy Checklist

- One primary focal point per viewport; one primary CTA per decision area.
- Primary > secondary > tertiary in size, weight, contrast, or isolation — not all three at once.
- Headings belong to the content below them: `margin-top(heading) >= 1.5 × margin-bottom(heading)`.
- Macro spacing between sections >= **2×** micro spacing inside a card.
- Use whitespace before adding borders, boxes, or dividers.
- 60-30-10 color weight: neutral canvas, secondary structure, small high-emphasis accent.

## 10. Motion Math

- Micro-interaction: **150–300ms**; larger transition: **200–500ms**.
- Enter: ease-out; exit: ease-in; spatial motion: avoid linear.
- Stagger lists by **20–40ms** per item, max ~6 items.
- Animate `transform`/`opacity`; avoid width/height/top/left.
- Respect `prefers-reduced-motion`; remove non-essential movement.
- Perceived instant feedback: **<=100ms**.
