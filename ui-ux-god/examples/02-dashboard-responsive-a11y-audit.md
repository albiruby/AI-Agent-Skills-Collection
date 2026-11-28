# Example 2 — Dashboard Responsive & Accessibility Audit

A worked example for a data-heavy analytics dashboard. The product is fictional; the method and evidence shape are reusable.

## 1. Scope

- **Mode:** Audit + Repair
- **Surfaces:** `/dashboard`, `/reports`, `/settings`
- **Viewports:** 320x568, 375x812, 768x1024, 1280x800, 1440x900
- **Themes:** light, dark
- **States:** default, loading, empty, error, long content, filter applied
- **Tools:** Playwright, DOM geometry, token audit, interactive a11y, keyboard run

## 2. Coverage ledger

| Surface | States checked | Viewports | Result |
|---|---|---|---|
| `/dashboard` | default, loading, empty, filter | 320/375/768/1440 | inspected |
| `/reports` | default, long table, error | 375/1440 | inspected |
| `/settings` | default, form error, modal | 375/1440 | inspected |
| `/admin` | — | — | blocked — no credentials |

## 3. Findings

### [RESP-001] Dashboard grid overflows at 375px

- **Category:** layout / responsive
- **Severity:** P0
- **Confidence:** High
- **Surface:** `/dashboard`, default
- **Environment:** 375x812, DPR 2, light
- **Evidence:** `document.documentElement.scrollWidth = 412px` vs viewport 375px; offender `.kpi-grid` with `grid-template-columns: repeat(3, 320px)`; overflow **37px**
- **Observed:** The KPI row forces horizontal page scroll on mobile.
- **Impact:** Users must pan sideways; sticky header and charts break.
- **Cause:** Fixed 320px columns; no `minmax(0, 1fr)` or mobile breakpoint.
- **Fix:** `grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr))`; test 320/375/768.
- **Verification:** `FIXED_AND_VERIFIED` — scrollWidth 375px at 375; 320 re-checked.

### [RESP-002] Data table scrolls the whole page

- **Category:** layout / responsive
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/reports`, default
- **Environment:** 375x812, DPR 2
- **Evidence:** `<table>` width 980px inside `main`; no overflow wrapper; page scrollWidth 980px
- **Observed:** The table stretches the page instead of scrolling inside its region.
- **Impact:** Navigation and surrounding content are pushed off-screen.
- **Cause:** Missing `overflow-x-auto` wrapper and `min-width` control.
- **Fix:** Wrap the table in `div.overflow-x-auto[role=region][aria-label][tabindex=0]`; keep the table `min-w-full`.
- **Verification:** `FIXED_AND_VERIFIED` — page scrollWidth 375; table scrolls within its region; keyboard focusable.

### [A11Y-002] Modal does not trap focus

- **Category:** accessibility / interaction
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/settings`, “Invite member” modal
- **Environment:** 1440x900, Chromium, keyboard
- **Evidence:** Tab moves from the last modal control to the page footer behind the overlay; `aria-modal="true"` present but no focus trap
- **Observed:** Keyboard focus escapes the modal.
- **Impact:** Keyboard/screen-reader users interact with hidden content and lose context.
- **Cause:** Visual overlay only; background not `inert`; no focus loop/restore.
- **Fix:** Use a dialog primitive or implement focus trap + `inert` background + restore focus on close; close on Escape.
- **Verification:** `FIXED_AND_VERIFIED` — Tab cycles inside; Escape closes; focus returns to “Invite”.

### [COL-002] Chart series distinguished by color only

- **Category:** color / accessibility
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/dashboard`, revenue chart
- **Environment:** 1440x900, light/dark
- **Evidence:** Three series use green/teal/blue lines with no dash pattern, markers, or labels; grayscale screenshot indistinguishable
- **Observed:** Users who cannot distinguish the hues cannot read the chart.
- **Impact:** Data is inaccessible; decisions may be wrong.
- **Cause:** Color-only encoding.
- **Fix:** Add distinct dash patterns/markers + a legend with labels; provide a table alternative.
- **Verification:** `FIXED_AND_VERIFIED` — series distinguishable in grayscale; legend and table present.

### [FORM-001] Error message not associated with the field

- **Category:** forms / accessibility
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/settings`, profile form
- **Environment:** 1440x900, light
- **Evidence:** Invalid email shows red border + text below, but input lacks `aria-invalid` and `aria-describedby`; screen reader announces only “Email, edit text”
- **Observed:** The error is visual only.
- **Impact:** Screen-reader users do not know why submission failed.
- **Cause:** Error rendered as a sibling `<p>` without association.
- **Fix:** `aria-invalid="true"`, `aria-describedby="email-error"`, `role="alert"` on the message; move focus to the first invalid field on submit.
- **Verification:** `FIXED_AND_VERIFIED` — error announced; focus moves to the field.

### [PERF-001] KPI cards cause CLS on load

- **Category:** performance
- **Severity:** P2
- **Confidence:** Medium
- **Surface:** `/dashboard`, cold load
- **Environment:** 375x812, Slow 4G, cold cache
- **Evidence:** CLS **0.18**; skeleton height 72px vs final card 116px; layout shift when data arrives
- **Observed:** Content jumps after the skeleton resolves.
- **Impact:** Mis-taps and a feeling of instability.
- **Cause:** Skeleton geometry does not match final content.
- **Fix:** Match skeleton rows/height to final; reserve space for the delta badge.
- **Verification:** `FIXED_AND_VERIFIED` — CLS 0.03 in the same lab run; field verification pending.

## 4. Repair plan

| Order | Finding | Layer | Risk | Verification |
|---:|---|---|---|---|
| 1 | RESP-001 | CSS grid | Low | 320/375/768 + screenshot |
| 2 | RESP-002 | Table wrapper | Low | page scrollWidth + keyboard |
| 3 | A11Y-002 | Dialog behavior | Medium | keyboard + screen reader |
| 4 | COL-002 | Chart encoding | Low | grayscale + legend |
| 5 | FORM-001 | Markup/ARIA | Low | screen reader + focus |
| 6 | PERF-001 | Skeleton geometry | Low | lab CLS; field later |

## 5. Verification summary

| Finding | Before | After | Status |
|---|---|---|---|
| RESP-001 | scrollWidth 412 @375 | 375 | FIXED_AND_VERIFIED |
| RESP-002 | page scrollWidth 980 | 375; table scroller | FIXED_AND_VERIFIED |
| A11Y-002 | focus escapes | trapped + restored | FIXED_AND_VERIFIED |
| COL-002 | color-only | patterns + labels + table | FIXED_AND_VERIFIED |
| FORM-001 | visual-only error | associated + announced | FIXED_AND_VERIFIED |
| PERF-001 | CLS 0.18 | 0.03 lab | FIXED_AND_VERIFIED (lab); field pending |

## 6. What this example demonstrates

- A responsive defect can be P0 when it breaks the page, even if it looks like “just mobile”.
- A table needs its own scroll region, not a page-wide overflow.
- Visual overlays are not dialogs; focus behavior is part of the component.
- Data visualization needs a non-color encoding.
- An error message without semantics is not an accessible error.
- Lab CLS improvement is not proof of field improvement; say what is pending.
