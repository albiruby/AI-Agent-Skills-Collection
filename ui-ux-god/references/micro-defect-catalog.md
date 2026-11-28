# Micro-UI Geometry Defect Catalog (Real-World Root Causes)

Use this catalog to diagnose subtle visual imperfections that separate amateur interfaces from flagship-grade products.

## 1. Centering & Alignment Micro-Defects

| Defect | Visual Symptom | Common Code Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Asymmetric 3-Slot Navbar Drift** | Brand logo in header looks shifted left or right of page center. | Parent uses `display: flex; justify-content: space-between` while left slot (e.g., menu icon, 40px) and right slot (e.g., login + CTA, 180px) have different widths. | Use CSS Grid `grid-template-columns: 1fr auto 1fr; align-items: center;` so the middle track is strictly centered regardless of side slot widths. |
| **Optical Centering Illusion** | Play button triangle, arrow icon, or asymmetric brand mark is mathematically centered in a circle/button but looks shifted left. | Geometric bounding box ignores visual center-of-mass of triangular/tapered shapes. | Apply a subtle `1px-2px` optical nudge (`translateX(1px)` or `padding-left: 2px` on play icons). |
| **SVG Transparent ViewBox Padding** | Logo looks off-center or misaligned with left grid edge even though `x = 0`. | Exported SVG has unequal empty whitespace inside its `viewBox`. | Trim SVG `viewBox` tightly to artwork paths or compensate with exact negative margin. |
| **Icon + Label Vertical Mismatch** | 16px icon beside 14px text sits slightly too high or low. | Relying on `vertical-align: baseline` or mismatched `line-height` on inline-flex children. | Wrap in `display: inline-flex; align-items: center; gap: 6px;` and set icon `flex-shrink: 0`. |
| **Mixed Sibling Column Alignment** | Column 1 is left-aligned, Column 2 is center-aligned inside the same feature row. | Inconsistent `text-align` utilities copied from different templates. | Unify alignment axis across all sibling columns in a horizontal band. |

## 2. Divider Line & Border Micro-Defects

| Defect | Visual Symptom | Common Code Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Incomplete Full-Bleed Divider** | Divider line inside a card or section stops 16-24px short of the container edges. | Parent container has `padding-inline: 24px`, constraining child `<hr>` width. | Either make the divider explicitly full-bleed using negative horizontal margin (`-mx-6 w-[calc(100%+3rem)]`) or intentionally align it to inner content padding on BOTH sides. |
| **Short Flex Divider** | Horizontal `<hr>` or `<div>` inside a `flex-col` container collapses to `0px` or narrower than expected. | Missing `align-self: stretch` / `w-full` inside a `flex-col items-center` parent. | Add `w-full self-stretch` to the divider element. |
| **Asymmetric Divider Inset** | Divider has 16px gap on the left and 28px gap on the right. | Unmatched margin/padding or scrollbar gutter eating right space. | Remove asymmetrical margin; enforce symmetric `mx-4` or `w-full` inside a balanced container. |
| **Double Border Thickness** | Two stacked cards or list rows create a 2px thick seam between them instead of 1px. | Both adjacent items apply `border-top` and `border-bottom`. | Use `divide-y` or apply `border-bottom` only and remove on `:last-child` (`border-b last:border-b-0`). |
| **Harsh Dark-Mode Divider** | Divider line looks blindingly bright white in dark theme. | Hardcoded `#e5e7eb` light-mode border color reused in dark mode. | Use low-opacity semantic hairline (`rgba(255, 255, 255, 0.08)` or CSS token `--border-subtle`). |

## 3. Card, Grid & Whitespace Micro-Defects

| Defect | Visual Symptom | Common Code Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Ragged Sibling Card Bottoms** | Cards in the same row end at different vertical heights and CTA buttons don't align. | Missing `h-full` / `align-items: stretch` on grid items and missing `mt-auto` on card footer/CTA. | Set grid `items-stretch`, card `flex flex-col h-full`, and footer/CTA `mt-auto`. |
| **Concentric Radius Clash** | Inner card/image inside a rounded outer card has the same `border-radius`, making corners look pinched. | Both outer (`16px`) and inner (`16px`) share the same radius token despite `12px` padding. | Apply concentric formula: `R_inner = max(4px, R_outer - padding)` (e.g., `16px - 12px = 4px` or `20px - 12px = 8px`). |
| **Macro vs Micro Whitespace Inversion** | Gap between two unrelated sections is equal to or smaller than internal card padding. | Arbitrary `my-6` between sections while cards use `p-8`. | Enforce Gestalt hierarchy: macro section gap (`48px-96px`) must be visibly >= `2x` micro element padding (`16px-24px`). |
| **Subtle Mobile Horizontal Scroll** | Page jiggles horizontally by 4-12px on 375px mobile screens. | Fixed-width element (`w-[400px]`), wide table without overflow wrapper, or decorative blur blob without `overflow-x: clip` on section. | Replace fixed widths with `max-w-full`, wrap tables in `overflow-x-auto`, and apply `overflow-x: clip` (not `hidden` which breaks `position: sticky`) on decorative section wrappers. |

## 4. Typography Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Orphan / Widow Headline** | One lonely word wraps onto a second line in a hero or card title. | Fixed width plus no balance/wrap control. | Add `text-wrap: balance` or adjust the container width; do not shrink the font arbitrarily. |
| **Inconsistent Optical Size** | A 24px icon font and a 24px SVG look different in weight. | Same nominal size, different optical box/stroke. | Match optical bounds, not just numeric size; adjust stroke or box. |
| **Line-Height Collision** | Descenders touch the next line or get clipped. | Line-height below 1.1 on multi-line text; fixed height. | Use role-appropriate line-height (body >=1.35) and remove fixed heights. |
| **Measure Too Wide** | Body copy runs 90–120 characters per line. | Full-width paragraph without `max-w-prose`. | Cap at 45–75ch; add `max-w-prose` or a grid column. |
| **Tabular Number Drift** | KPI values/prices do not align vertically. | Proportional numerals. | Apply `font-variant-numeric: tabular-nums`. |
| **Faux Bold / Faux Italic** | Text looks smeared or poorly spaced. | Synthesized weight/style because the family lacks the face. | Load the real weight or choose another family. |

## 5. Color & Contrast Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Gray-on-Gray Body** | Secondary text is technically visible but tiring. | `text-neutral-400` on white or `text-white/50` on dark. | Use a token that meets 4.5:1; verify against the effective background. |
| **Invisible Input Border** | Fields disappear into the surface. | Border contrast <3:1. | Use a 3:1 boundary or a filled surface with sufficient contrast. |
| **Dark-Mode Halation** | White text on pure black glows/vibrates. | `#000` + `#fff` without surface elevation. | Use charcoal surfaces and off-white text; add subtle edge highlights. |
| **Status by Color Only** | Users cannot distinguish success/error in grayscale. | Red/green alone. | Add icon, label, pattern, or text. |
| **Focus Ring Vanishes** | Keyboard focus is invisible on some surfaces. | Ring color matches background or is clipped. | 2px ring + offset, tested on every surface/theme. |
| **Gradient Contrast Trap** | Text passes at the top but fails over a lighter gradient stop. | Contrast measured at one point. | Test the lightest/busiest pixel; add a scrim or move the text. |

## 6. Icon & Asset Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Mixed Stroke Weights** | Nav icons look inconsistent/heavy. | 1.5px and 2px icons mixed. | Normalize stroke weight and corner style per context. |
| **Icon Sits High** | Icon appears above the text cap height. | Baseline alignment or mismatched line-height. | `inline-flex; align-items:center; gap`; check midpoint delta. |
| **Logo Looks Off-Center** | CSS center is mathematically correct but visually wrong. | Asymmetric SVG viewBox/transparent padding. | Trim viewBox or apply a measured optical offset. |
| **Blurry Raster Icon** | Icon is soft on Retina/HiDPI. | 1x PNG upscaled. | Use SVG or @2x/@3x; check 125/150/200% scaling. |
| **Stretched Illustration** | Art looks squashed. | `width:100%; height:100%` without `object-fit`. | `object-fit: cover/contain` + aspect-ratio. |
| **Decorative Icon Announced** | Screen reader says “image” for a decorative glyph. | Missing `aria-hidden="true"`. | Hide decorative icons; name meaningful ones. |

## 7. Form & State Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Placeholder-as-Label** | Label disappears after typing. | Placeholder used as the only label. | Add a persistent visible label. |
| **Error Not Associated** | Screen reader does not announce the error. | No `aria-invalid`/`aria-describedby`. | Associate the message; announce on submit. |
| **Error Jumps Layout** | Form shifts when an error appears. | Error inserted without reserved space. | Reserve space or use an inline message that does not move the field. |
| **Disabled Looks Clickable** | User clicks a dead control. | Opacity only, cursor unchanged, handler still active. | Muted style + `disabled`/`aria-disabled` + no handler. |
| **Double Submit** | Duplicate orders/messages. | Button not locked during pending. | Disable + spinner + idempotency key where relevant. |
| **Empty Void** | Blank panel with no guidance. | No empty state. | Explain value + primary action + example. |
| **Skeleton Jump** | Content jumps when data arrives. | Skeleton geometry differs from final. | Match final height/rows; reserve space. |

## 8. Motion & Interaction Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Hover Layout Shift** | Card moves when hovered. | Animating margin/width/height. | Animate transform/opacity only. |
| **Sticky Header Covers Anchor** | Section title hides under the header after jump. | No `scroll-margin-top`. | Add `scroll-margin-top` equal to header height + gap. |
| **Focus Lost Behind Overlay** | Tab goes to content under a modal. | No focus trap/inert. | Trap focus, `inert` the background, restore on close. |
| **Reduced Motion Ignored** | Motion persists despite OS preference. | No `prefers-reduced-motion` branch. | Remove/limit non-essential motion. |
| **Janky Blur/Filter** | Scroll stutters on low-end devices. | Large `backdrop-filter`/shadow areas. | Reduce area/intensity; test on mid-tier hardware. |

## 9. Platform Micro-Defects

| Defect | Visual Symptom | Common Root Cause | Exact Fix |
| :--- | :--- | :--- | :--- |
| **Safe-Area Collision** | Content under notch/home indicator. | No safe-area insets. | `SafeArea`/`WindowInsets`; test on device. |
| **Keyboard Covers Field** | Active input hidden by keyboard. | No keyboard avoidance. | Scroll/inset the active field into view. |
| **Titlebar Collision** | Custom header overlaps traffic lights/caption buttons. | Centering in remaining space. | Reserve platform insets; use a 3-column grid. |
| **Blurry HiDPI Hairline** | 1px border looks 2px/soft at 150%. | Raster border or transform scaling. | Use CSS borders/logical pixels; test 125/150/200%. |
| **CLI Right-Edge Jag** | Box borders misalign with emoji/CJK. | `.length` instead of display width. | Use `wcwidth`/`string-width`; test 80/120 columns. |

## 10. False-Positive Check

Before flagging, ask:

- Is the asymmetry intentional (editorial 60/40, brand mark, optical alignment)?
- Is the difference caused by subpixel/DPR rendering under 1px?
- Is the element intentionally hidden at this breakpoint?
- Is the “missing” state handled by a parent or a portal?
- Is the reference outdated or contradicted by the current design system?

Record the intent check. A false positive costs more trust than a missed P3.
