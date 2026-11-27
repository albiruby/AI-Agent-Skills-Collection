# Reference: Visual Asset Guidelines

## Asset categories

Do not conflate these outputs:

1. **Raw capture:** untouched screenshot from the actual application or simulator.
2. **Clean screenshot:** cropped to the actual application viewport/display, with unrelated environment UI removed.
3. **Device render:** device body and screen isolated from its original background.
4. **Mockup:** genuine screenshot placed inside a rendered device frame or presentation scene.
5. **Store composition:** promotional layout combining genuine screenshots, feature copy, and visual design.
6. **Diagram/illustration:** explanatory visual that is not a literal application screenshot.

Store the raw capture separately from processed assets.

## Screenshot authenticity

- The app UI shown as evidence must come from the real app or a user-supplied genuine capture.
- Do not fabricate UI or replace the actual screen with an AI-generated lookalike.
- A generated background or device mockup may be used around a genuine screenshot, but must not misrepresent the actual interface.
- Captions must describe verified features.
- Do not show fake ratings, reviews, metrics, notifications, or compatibility claims.

## Crop and geometry

- Identify the active content boundary, not merely the outer device boundary.
- For circular watch displays, the screen is inside the bezel; decide explicitly whether the output includes the bezel.
- For round/curved screens, preserve the geometry and do not stretch to a rectangle unless the requested composition intentionally uses a clipped or masked presentation.
- Keep all meaningful interface edges, indicators, and text visible.
- If automatic boundary detection is ambiguous, use a manual crop or request a reference.

## Composition

- Keep the product UI as the focal point.
- Use concise feature labels.
- Maintain readable type at final display size.
- Apply consistent margins, alignment, spacing, and visual hierarchy across a gallery.
- Avoid dense paragraphs, excessive decorations, clutter, and low-contrast text.
- Use the project's existing color, type, icon, and logo assets when available.
- If a new visual direction is requested, document the design choices and apply them consistently.

## Accessibility and practical quality

- Check contrast and text readability.
- Avoid relying only on color to convey meaning.
- Do not use tiny captions that will become illegible in store previews.
- Include alt text or a brief description where the publishing destination supports it.

## File and export hygiene

- Keep original source captures.
- Prefer lossless formats for UI screenshots where appropriate.
- Avoid repeated lossy conversions.
- Preserve aspect ratio; use padding/canvas expansion instead of stretching.
- Keep working/editable source when it is useful.
- Use descriptive filenames and record dimensions in the asset manifest.

## Clean versus dirty standard

**Dirty (reject):**

- Simulator/emulator window title bar, menu bar, toolbar, or memory/status bar.
- Solid white or light-gray canvas around a watch/phone.
- Browser chrome, scrollbars, cookie banners, desktop wallpaper.
- Clipped hardware, jagged white halos, or stretched device geometry.

**Clean (accept):**

- Only the intended device silhouette and active screen, or only the app viewport.
- Fully transparent exterior for device cutouts.
- Crisp anti-aliased edges with no white fringe.
- Consistent scale across sibling screens.
- Interior white text/icons remain opaque.

## Cleanup and slicing QA

- Use edge-connected flood fill, not global white replacement.
- Check all four exterior corners for alpha = 0 on device cutouts.
- Check that interior white UI remains opaque.
- Check for white halos around dark bezels.
- Check for clipped straps, lugs, buttons, or phone corners.
- Normalize sibling device heights.
- Preserve round display geometry; do not stretch to a square.
- Keep raw and clean assets separate.
- Save device cutouts as lossless PNG.
- If crop confidence is low, stop and request a reference crop.
