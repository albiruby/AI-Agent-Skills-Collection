# Surgical UI/UX Fix Patterns (Production Recipes)

Canonical, root-cause fixes for the most common real-world UI/UX defects.

## 1. True Mathematical Centering in 3-Slot Navbars / Headers

**Broken Pattern (Logo shifts left/right when action widths differ):**

```html
<!-- BAD: justify-between centers based on free space, not viewport center -->
<header class="flex items-center justify-between px-6 h-16">
  <button>Menu</button>
  <a class="logo">BRAND</a>
  <div class="flex gap-3"><button>Login</button><button>Get Started</button></div>
</header>
```

**Surgical Fix (Exact 0.0px center drift regardless of side widths):**

```html
<!-- GOOD: 1fr auto 1fr locks middle track to exact container center -->
<header class="grid grid-cols-[1fr_auto_1fr] items-center px-6 h-16">
  <div class="justify-self-start"><button>Menu</button></div>
  <a class="justify-self-center logo">BRAND</a>
  <div class="justify-self-end flex items-center gap-3">
    <button>Login</button>
    <button>Get Started</button>
  </div>
</header>
```

## 2. Full-Bleed vs Content-Aligned Divider Lines

**Broken Pattern (Divider stops short inside a padded card or collapses in flex-col):**

```html
<div class="flex flex-col items-center p-6 rounded-2xl border">
  <h3>Card Title</h3>
  <hr class="border-neutral-200 my-4" /> <!-- collapses or stops 24px short -->
  <p>Details...</p>
</div>
```

**Surgical Fix A (Full-bleed edge-to-edge inside padded card):**

```html
<div class="flex flex-col p-6 rounded-2xl border">
  <h3>Card Title</h3>
  <hr class="-mx-6 w-[calc(100%+3rem)] border-t border-neutral-200 dark:border-white/10 my-4" />
  <p>Details...</p>
</div>
```

**Surgical Fix B (Cleanly aligned to symmetric content column):**

```html
<div class="flex flex-col items-center p-6 rounded-2xl border">
  <h3>Card Title</h3>
  <hr class="w-full self-stretch border-t border-neutral-200 dark:border-white/10 my-4" />
  <p>Details...</p>
</div>
```

## 3. Symmetric Sibling Cards with Aligned CTAs

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
  <article class="flex flex-col h-full p-6 rounded-2xl border">
    <h3 class="text-lg font-semibold text-balance">Plan Name</h3>
    <p class="mt-2 text-sm text-neutral-600">Variable length copy...</p>
    <div class="mt-auto pt-6">
      <button class="w-full h-11 rounded-lg">Choose Plan</button>
    </div>
  </article>
</div>
```

## 4. Concentric Border-Radius Nesting

```html
<!-- Outer radius 16px (rounded-2xl), padding 8px (p-2) -> Inner radius 8px (rounded-lg) -->
<div class="rounded-2xl p-2 bg-neutral-100 border">
  <img src="hero.jpg" alt="..." class="w-full aspect-video object-cover rounded-lg" />
</div>
```

## 5. Optical Centering & Icon + Text Alignment

```html
<!-- Inline icon + label locked on vertical midline -->
<button class="inline-flex items-center justify-center gap-2 min-h-[44px] px-4 rounded-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-600 focus-visible:ring-offset-2">
  <svg class="w-4 h-4 shrink-0" aria-hidden="true">...</svg>
  <span>Continue</span>
</button>

<!-- Play triangle optical nudge (+1.5px right inside circular button) -->
<button aria-label="Play video" class="inline-flex items-center justify-center w-12 h-12 rounded-full">
  <svg class="w-5 h-5 translate-x-[1.5px]" aria-hidden="true">...</svg>
</button>
```

## 6. Zero-Overflow Responsive Wrapper (Without Breaking `position: sticky`)

```css
/* Avoid overflow-x: hidden on html/body; use clip on decorative sections */
.hero-section {
  overflow-x: clip;
}
```

## 7. Flex Child Refuses to Shrink

**Symptom:** long text or a table pushes the layout wider than its container.

```css
/* BAD: min-width defaults to auto, so the flex item refuses to shrink */
.row { display: flex; }
.row > .content { flex: 1; }

/* GOOD: allow the item to shrink, then handle text deliberately */
.row { display: flex; min-width: 0; }
.row > .content { flex: 1 1 0%; min-width: 0; }
.row > .content .truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
```

Do not add `overflow: hidden` to the whole row unless clipping is intended.

## 8. Grid Track Blows Out the Page

**Symptom:** `grid-template-columns: 1fr 1fr` overflows when one child has a long unbreakable string.

```css
/* BAD: 1fr has an auto minimum */
.grid { display: grid; grid-template-columns: 1fr 1fr; }

/* GOOD: allow tracks to shrink below content size */
.grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
```

## 9. `100vw` Scrollbar Overflow

**Symptom:** a full-bleed section causes a horizontal scrollbar on desktop.

```css
/* BAD: 100vw includes the vertical scrollbar width */
.full-bleed { width: 100vw; margin-left: calc(50% - 50vw); }

/* GOOD: use the container or 100% inside a full-bleed wrapper */
.full-bleed { width: 100%; }
.container { max-width: 72rem; margin-inline: auto; padding-inline: 1.5rem; }
```

If a viewport unit is required, prefer `100dvw`/`100svw` carefully and test with a visible scrollbar.

## 10. Sticky Header Covers Anchor Targets

```css
:root { --header-height: 4rem; }

[id] { scroll-margin-top: calc(var(--header-height) + 1rem); }

html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
}
```

## 11. Z-Index Trapped by a Stacking Context

**Symptom:** a dropdown/modal sits under a sibling no matter how high its `z-index`.

Check for ancestors with `transform`, `filter`, `opacity < 1`, `will-change`, `contain`, or `position` that create a stacking context. Fix the context, not the number:

```css
/* BAD: escalating z-index inside a trapped context */
.dropdown { z-index: 99999; }

/* GOOD: portal the overlay to the document body, or remove the trapping transform */
```

Prefer a documented z-index scale (`--z-dropdown: 40; --z-modal: 50; --z-toast: 60`).

## 12. Focus Ring That Survives Every Surface

```css
:focus-visible {
  outline: 2px solid var(--focus-ring, #2563eb);
  outline-offset: 2px;
}

/* On dark/brand surfaces, switch the token, not the behavior */
.on-dark { --focus-ring: #93c5fd; }
```

Do not use `outline: none` without a visible replacement. Test on light, dark, image, and gradient backgrounds.

## 13. Data Table Overflow Without Page Scroll

```html
<div class="overflow-x-auto" role="region" aria-label="Orders table" tabindex="0">
  <table class="min-w-full">...</table>
</div>
```

- Keep the table’s semantic markup.
- Give the scroll region an accessible name and keyboard focus.
- Do not shrink text to 10px to avoid scrolling.

## 14. Image Aspect Ratio & CLS

```html
<img
  src="hero.avif"
  alt="..."
  width="1600"
  height="900"
  class="w-full h-auto aspect-video object-cover"
  loading="eager"
  fetchpriority="high"
/>
```

- Reserve dimensions or `aspect-ratio`.
- Use `object-fit` for art-directed crops.
- Lazy-load below the fold; never lazy-load the LCP image.

## 15. Dark-Mode Semantic Tokens

```css
:root {
  --surface: #ffffff;
  --surface-raised: #f8fafc;
  --text: #0f172a;
  --text-muted: #475569;
  --border: #e2e8f0;
  --focus-ring: #2563eb;
}

[data-theme="dark"] {
  --surface: #0b0d12;
  --surface-raised: #12151e;
  --text: #e5e7eb;
  --text-muted: #a1a1aa;
  --border: rgba(255, 255, 255, 0.10);
  --focus-ring: #93c5fd;
}
```

Use semantic tokens for text/border/surface; never reuse a light-mode hex in dark mode.

## 16. Form Error Association

```html
<label for="email">Email</label>
<input
  id="email"
  name="email"
  type="email"
  autocomplete="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" role="alert">Enter an email in the format name@example.com.</p>
```

- Error text is specific and near the field.
- `aria-invalid` + `aria-describedby` connect the message.
- Do not rely on a red border alone.
- For long forms, add an error summary with links to fields.

## 17. Icon-Only Button Hit Area

```html
<button
  type="button"
  aria-label="Close dialog"
  class="inline-flex items-center justify-center w-11 h-11 rounded-lg"
>
  <svg class="w-5 h-5" aria-hidden="true">...</svg>
</button>
```

The visible icon can be 20px; the interactive box must be at least 44x44px (or 24x24px with adequate spacing as the WCAG 2.2 floor).

## 18. Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Use this as a safety net, not a substitute for designing a reduced-motion variant. Keep essential state changes understandable.

## 19. RTL & Logical Properties

```css
/* Prefer logical properties */
.card { margin-inline: auto; padding-inline: 1rem; border-inline-start: 1px solid var(--border); }
.icon { margin-inline-end: 0.5rem; }
```

Avoid hardcoded `left/right` for directional spacing when the product supports RTL. Test mirrored layouts; do not mirror logos or media that should stay directional.
