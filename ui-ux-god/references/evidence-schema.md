# Standardized UI/UX Audit Evidence Schema

Every finding in this pack uses one record shape so that reports are deterministic, verifiable, and directly consumable by the repair and verification skills.

## 1. Evidence hierarchy

Use the strongest available evidence and label the rest:

1. **Runtime observation** — live screenshot, recording, native frame, terminal capture.
2. **Measured structure** — DOM rect, computed style, accessibility tree, native view hierarchy, terminal cell grid.
3. **Reproducible test/log** — console/network output, test run, visual diff, performance trace.
4. **Authoritative reference** — current Figma/spec/design-system source.
5. **Inference** — clearly labeled; never presented as measured fact.

## 2. JSON finding schema

```json
{
  "id": "GEO-001",
  "title": "Header logo drifts 35.5px left of center",
  "subskill": "uiux-layout-geometry-auditor",
  "category": "layout",
  "severity": "P1",
  "confidence": "High",
  "surface": {
    "route": "/",
    "screen": "Home",
    "state": "default",
    "userRole": "guest"
  },
  "environment": {
    "viewport": "1440x900",
    "dpr": 1,
    "os": "Windows 11",
    "browser": "Chrome 126",
    "theme": "light",
    "locale": "en-US",
    "zoom": "100%"
  },
  "target": {
    "selector": "header nav .brand-logo",
    "componentFile": "src/components/Navbar.tsx:42",
    "description": "Primary brand mark in top navigation"
  },
  "evidence": {
    "measured": {
      "elementCenterX": 684.5,
      "containerCenterX": 720.0,
      "deltaX_px": -35.5,
      "tolerance_px": 1.5
    },
    "computedStyle": {
      "parentDisplay": "flex",
      "parentJustifyContent": "space-between",
      "leftSiblingWidth": 112,
      "rightSiblingWidth": 183
    },
    "screenshotBefore": "audit-out/home-1440-before.png"
  },
  "observed": "Logo center is 684.5px; header center is 720px; delta -35.5px.",
  "userImpact": "Brand mark reads as misaligned; the header feels unfinished.",
  "frequency": "Every load at >=1024px",
  "reproduction": [
    "Open / at 1440x900",
    "Inspect header nav .brand-logo",
    "Compare element center to header center"
  ],
  "rootCause": "Navbar uses flex justify-between with asymmetric side slots.",
  "rootCauseStatus": "confirmed",
  "recommendedFix": "Use CSS Grid `grid-template-columns: 1fr auto 1fr`.",
  "affected": ["src/components/Navbar.tsx"],
  "verification": {
    "status": "FIXED_AND_VERIFIED",
    "measuredAfter": { "deltaX_px": 0.0 },
    "screenshotAfter": "audit-out/home-1440-after.png",
    "tests": ["dom_geometry_audit.mjs", "visual check 375/768/1440"]
  }
}
```

### Field rules

- `id` is stable across report → repair → verification. Never renumber silently.
- `severity` uses P0–P3; `confidence` is High/Medium/Low.
- `surface` and `environment` are mandatory: a finding without conditions is not reproducible.
- `observed` is fact; `rootCause` is fact or hypothesis and must say which.
- `evidence` paths must be real and accessible. Never fabricate a path or a measurement.
- `verification.status` must be one of the states in section 5.

## 3. Markdown finding record

```markdown
### [GEO-001] Header logo drifts 35.5px left of center

- **Category:** layout
- **Severity:** P1 / High
- **Confidence:** High
- **Surface:** `/` Home, guest, default
- **Environment:** 1440x900, DPR 1, Chrome 126, light, en-US, 100%
- **Evidence:** `home-1440-before.png`; `header nav .brand-logo`; element center 684.5px vs header 720px; delta -35.5px; parent `justify-between`, slots 112px/183px
- **Observed:** Logo is 35.5px left of the header center.
- **Impact:** Brand mark reads as misaligned; header feels unfinished.
- **Frequency:** Every load >=1024px.
- **Reproduction:** 1) Open `/` at 1440x900. 2) Inspect `.brand-logo`. 3) Compare centers.
- **Cause:** Confirmed — asymmetric flex side slots with `justify-between`.
- **Fix:** Grid `1fr auto 1fr` on the header; keep logo in the middle track.
- **Verification:** FIXED_AND_VERIFIED — delta 0.0px; 375/768/1440 re-checked.
```

## 4. Severity classification

| Severity | Label | Examples | Action |
|---|---|---|---|
| **P0** | Critical / Broken | Core flow blocked, clipped/unreadable primary text, page-wide mobile overflow, overlapping controls, broken assets, contrast <3.0:1 on primary text | Fix before polish |
| **P1** | High / Structural | Off-center brand >2px, incomplete divider, broken grid, uneven sibling cards, body contrast <4.5:1, touch target <44px | Primary pass |
| **P2** | Medium / System | Off-grid spacing, radius mismatch, rogue font sizes/colors, missing focus ring, missing state | Quality pass |
| **P3** | Low / Craft | 1–2px optical nudge, missing tabular numerals, orphan wrap, subtle shadow drift | Polish pass |

Severity is impact, not scheduling. Use `../../references/severity-and-priority.md` for priority.

## 5. Verification states

- `OPEN` — detected with evidence, not patched.
- `FIXED_AND_VERIFIED` — patched, re-rendered, re-measured, within tolerance, no regression.
- `PARTIAL_NEEDS_DESIGN_DECISION` — technical fix needs a brand/product decision.
- `BLOCKED_EXTERNAL` — third-party iframe/embed/read-only asset.
- `NOT_FIXED` — attempted, still failing.
- `REGRESSION_INTRODUCED` — fix broke another surface.
- `UNABLE_TO_VERIFY` — required state/device/tool unavailable.

## 6. Coverage ledger

| Surface / route | States checked | Viewports / devices | Theme / locale / zoom | Tools / evidence | Result |
|---|---|---|---|---|---|
| `/` | default, hover, focus, 320/375 overflow | 375x812, 1440x900 | light/dark, en-US, 100% | Playwright + DOM | inspected |
| `/checkout` | default, error, loading | 375x812 | light, en-US | screenshots only | partial — no auth |
| `/admin` | — | — | — | — | blocked — no credentials |

## 7. Report assembly

1. Executive summary: scope, mode, overall risk, top 3 findings.
2. Coverage: inspected / partial / blocked / not in scope.
3. Findings sorted by priority; each with the standard record.
4. Repairs: files/components changed, rationale, blast radius.
5. Verification: status per finding + before/after evidence.
6. Limitations: what could not be tested or claimed.
7. Decisions needed: owner, options, deadline.
