# WCAG 2.2 Quick Reference for UI Audits

A practical subset of WCAG 2.2 A/AA criteria used most often in interface audits. This is **not** a complete conformance checklist. For a formal claim, test every applicable success criterion against the official specification and document the method.

- Official specification: https://www.w3.org/TR/WCAG22/
- Understanding documents: https://www.w3.org/WAI/WCAG22/Understanding/
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/

## 1. Default target

Unless the product or policy specifies otherwise:

- **WCAG 2.2 Level A + AA** for web content.
- Native apps: map comparable requirements to platform accessibility APIs and guidelines; do not force web techniques onto native controls.
- Automated scans are evidence inputs, never proof of conformance.

## 2. Perceivable

| SC | Level | Requirement | How to test | Common failure |
|---|---|---|---|---|
| **1.1.1** Non-text Content | A | Informative images have equivalent alt; decorative images are ignored by AT; complex images have a longer description | Accessibility tree + alt audit | Missing alt, filename as alt, icon-only button without name |
| **1.2.2** Captions (Prerecorded) | A | Prerecorded video with audio has captions | Check captions track and accuracy | Auto-captions with no review |
| **1.2.4** Captions (Live) | AA | Live audio has real-time captions | Check live workflow | No caption path |
| **1.2.5** Audio Description (Prerecorded) | AA | Visual information not conveyed by audio is described | Check description track | Description missing |
| **1.3.1** Info and Relationships | A | Structure and relationships are programmatic or textual | Accessibility tree, headings, lists, tables, labels | Visual headings are `<div>`; layout tables; labels not associated |
| **1.3.2** Meaningful Sequence | A | Reading order matches meaningful sequence | DOM/AT order vs visual order | CSS order differs from DOM order |
| **1.3.4** Orientation | AA | Content is not restricted to one orientation unless essential | Rotate device | Portrait-only lock |
| **1.3.5** Identify Input Purpose | AA | Common input purposes expose autocomplete tokens | Inspect `autocomplete` | Missing `autocomplete="email"` etc. |
| **1.4.1** Use of Color | A | Color is not the only way to convey information | Grayscale/contrast check | Red-only error state; color-only chart legend |
| **1.4.3** Contrast (Minimum) | AA | Normal text **>=4.5:1**; large text **>=3:1** (>=24px regular or >=18.66px bold) | Contrast tool against effective background | Gray-on-gray body copy; text over photo |
| **1.4.4** Resize Text | AA | Text resizes to **200%** without loss of content/function | Browser zoom 200% | Fixed-height text containers clip |
| **1.4.5** Images of Text | AA | Use real text, not images of text, except logos | Inspect text rendering | Headline baked into PNG |
| **1.4.10** Reflow | AA | Content reflows at **320 CSS px** without 2D scrolling, except data tables | 320px viewport / 400% zoom | Fixed 400px card; horizontal page scroll |
| **1.4.11** Non-text Contrast | AA | UI components and meaningful graphics **>=3:1** against adjacent colors | Contrast tool | Invisible input borders; low-contrast focus ring |
| **1.4.12** Text Spacing | AA | No loss when line-height **1.5x**, paragraph **2x**, letter **0.12x**, word **0.16x** | Text-spacing bookmarklet | Fixed-height cards clip |
| **1.4.13** Content on Hover or Focus | AA | Extra content is dismissible, hoverable, persistent | Hover/focus test | Tooltip disappears when moving pointer |

## 3. Operable

| SC | Level | Requirement | How to test | Common failure |
|---|---|---|---|---|
| **2.1.1** Keyboard | A | All functionality is operable via keyboard | Keyboard-only run | Custom div buttons; drag-only |
| **2.1.2** No Keyboard Trap | A | Focus can always leave a component | Tab/Escape through dialogs | Modal traps focus with no exit |
| **2.1.4** Character Key Shortcuts | A | Single-character shortcuts can be turned off/remapped | Shortcut audit | `s` saves with no opt-out |
| **2.2.1** Timing Adjustable | A | Time limits can be extended/disabled | Timed flow test | Session timeout with no warning |
| **2.2.2** Pause, Stop, Hide | A | Moving/blinking content >5s can be paused | Carousel/auto-play test | Auto-rotating hero |
| **2.3.1** Three Flashes | A | No more than 3 flashes per second | Recording/frame check | Strobe effect |
| **2.4.1** Bypass Blocks | A | Skip link or landmark structure | Keyboard first Tab | No skip link on long nav |
| **2.4.2** Page Titled | A | Every page has a descriptive title | Tab title / DOM | “Untitled” or route name only |
| **2.4.3** Focus Order | A | Focus order preserves meaning/operability | Tab sequence | Focus jumps to footer |
| **2.4.4** Link Purpose (In Context) | A | Link purpose is clear from text/context | Link audit | “Click here” x20 |
| **2.4.5** Multiple Ways | AA | More than one way to find a page (nav, search, sitemap) | IA check | Single hidden path |
| **2.4.6** Headings and Labels | AA | Headings/labels describe topic/purpose | Heading outline | “Section 1”, “Field” |
| **2.4.7** Focus Visible | AA | Keyboard focus is visible | Tab through | `outline: none` with no replacement |
| **2.4.11** Focus Not Obscured (Minimum) | AA (2.2) | Focused element is not entirely hidden by sticky/overlay content | Tab with sticky header | Focus ring under fixed bar |
| **2.4.13** Focus Appearance | AAA (2.2) | Focus indicator meets area/contrast thresholds | Measure ring | Thin low-contrast ring |
| **2.5.1** Pointer Gestures | A | Multipoint/path gestures have a single-pointer alternative | Touch test | Pinch-only zoom |
| **2.5.2** Pointer Cancellation | A | Down-event does not trigger irreversible action | Tap/click test | Action on `mousedown` |
| **2.5.3** Label in Name | A | Visible label is contained in the accessible name | AT audit | Visible “Search”, name “Go” |
| **2.5.4** Motion Actuation | A | Device-motion actions have a UI alternative | Device test | Shake-only undo |
| **2.5.7** Dragging Movements | AA (2.2) | Dragging has a single-pointer alternative | Slider/drag test | Drag-only reorder |
| **2.5.8** Target Size (Minimum) | AA (2.2) | Target **>=24x24 CSS px**, with documented exceptions (spacing, inline, essential, UA) | Measure targets | 16px icon button with no spacing |
| **2.5.5** Target Size (Enhanced) | AAA | **>=44x44 CSS px** | Measure targets | Small tap targets |

## 4. Understandable

| SC | Level | Requirement | How to test | Common failure |
|---|---|---|---|---|
| **3.1.1** Language of Page | A | `lang` matches page language | DOM audit | Missing/wrong `lang` |
| **3.1.2** Language of Parts | AA | Language changes are marked | Mixed-language audit | Indonesian quote in English page unmarked |
| **3.2.1** On Focus | A | Focus does not trigger unexpected context change | Tab test | Focus opens modal |
| **3.2.2** On Input | A | Input does not unexpectedly change context | Form test | Selecting a radio submits |
| **3.2.3** Consistent Navigation | AA | Repeated navigation is in the same relative order | Multi-page check | Nav reshuffles per page |
| **3.2.4** Consistent Identification | AA | Same function has same label/icon | Component audit | “Save” vs “Submit” for same action |
| **3.2.6** Consistent Help | A (2.2) | Help mechanisms appear in a consistent relative order | Multi-page check | Help link moves |
| **3.3.1** Error Identification | A | Errors are identified in text | Invalid submit | Red border only |
| **3.3.2** Labels or Instructions | A | Labels/instructions for required input | Form audit | Placeholder-only labels |
| **3.3.3** Error Suggestion | AA | Suggest a correction when known | Invalid submit | “Invalid input” with no guidance |
| **3.3.4** Error Prevention (Legal, Financial, Data) | AA | Reversible, checked, or confirmed before finalizing | Checkout/delete test | One-click irreversible delete |
| **3.3.7** Redundant Entry | A (2.2) | Do not ask for the same information twice in one process unless necessary | Multi-step form | Re-enter address at payment |
| **3.3.8** Accessible Authentication (Minimum) | AA (2.2) | No cognitive function test unless an alternative/assistance exists | Login test | Unpasteable password; memory-only puzzle |

## 5. Robust

| SC | Level | Requirement | How to test | Common failure |
|---|---|---|---|---|
| **4.1.2** Name, Role, Value | A | Custom UI exposes name, role, state, value | Accessibility tree | Div button with no role/name |
| **4.1.3** Status Messages | AA | Status messages are announced without focus change | Live region test | Silent “Saved” toast |

> Note: 4.1.1 Parsing is obsolete in WCAG 2.2. Do not report it as a failure.

## 6. Contrast math

```text
relative luminance L = 0.2126 R + 0.7152 G + 0.0722 B
(linearized sRGB channels)

contrast = (L1 + 0.05) / (L2 + 0.05)
```

- Normal text: **>=4.5:1**
- Large text: **>=3:1**
- UI components/graphics: **>=3:1**
- Test the **effective** background: gradients, images, overlays, and dark-mode surfaces.

## 7. Target size exceptions (2.5.8)

A 24x24px target is not required when:

- **Spacing:** a 24px-diameter circle centered on the target does not intersect another target.
- **Inline:** the target is in a sentence or block of text.
- **User agent control:** the size is determined by the browser/platform and not modified.
- **Essential:** a specific presentation is essential to the information.

44/48px remains the ergonomic recommendation even when 24px is technically allowed.

## 8. Audit method

1. Define the target level and scope.
2. Test keyboard-only and with at least one screen reader where available.
3. Test 320px / 400% zoom, 200% text resize, and text spacing.
4. Measure contrast and target sizes with a tool; record values.
5. Map each failure to a criterion ID; distinguish definite failure, potential issue, and not applicable.
6. Record the AT/browser/OS versions actually tested.
7. State limitations. A single screen-reader pass is not universal compatibility.
8. Never claim “WCAG AA compliant” from an automated scan alone.
