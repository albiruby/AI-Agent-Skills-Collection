# Screenshot Slicing QA Rules

Check every sliced PNG in `docs/assets/clean/` against these pass/fail criteria before compositing store graphics or embedding in docs:

1. **Zero Window Chrome**: No OS title bar, minimize/maximize/close buttons, menu bar, scrollbars, or simulator memory/status bar visible anywhere in the frame.
2. **True Transparent Exterior**: All 4 corners must have `alpha == 0`. Never leave solid white (`#FFFFFF`) or light-gray rectangles around a circular watch or rounded phone.
3. **Interior White Preserved**: White text, white icons, and bright screen highlights inside the device screen must remain 100% opaque (confirm edge-connected flood fill was used, not global color keying).
4. **Zero White Halo / Fringe**: When placed over a dark navy or charcoal store banner background, the outer bezel and straps must blend cleanly without jagged white pixel halos.
5. **No Clipped Hardware**: Watch straps, lugs, buttons, or phone corners must not be accidentally cropped off.
6. **Uniform Scale Across Siblings**: All screenshots from the same device model used in a side-by-side layout must share the exact same pixel height (`--target-height`).
