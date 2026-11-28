# 9-State UI Matrix & Measurable UX Heuristics

## 1. The 9 Mandatory UI States

Audit every interactive widget, form, list, and data view against all 9 states:

| State | What Must Be Verified |
| :--- | :--- |
| **1. Default** | Clean hierarchy, balanced density, clear primary CTA. |
| **2. Hover** | Immediate visual feedback on pointer devices (`>= 100ms` smooth transition); no layout shift on hover. |
| **3. Focus-Visible** | Clear `2px` high-contrast ring (`>= 3:1`) with `2px` offset; never suppressed by `outline: none`. |
| **4. Active / Pressed** | Tactile feedback (subtle scale `0.98` or shade shift) on click/tap. |
| **5. Disabled** | Visually distinct (`opacity: 0.45-0.55` + `cursor: not-allowed`) and ignored by click handlers. |
| **6. Loading** | Skeleton or spinner matching final container geometry (zero CLS jump when data arrives); submit button locked against double-click. |
| **7. Empty** | Clear explanation + single actionable CTA to create/add first item (never a blank void). |
| **8. Error** | Inline error message next to offending field (`aria-invalid="true"` + `aria-describedby`), clear recovery step, never raw stack trace. |
| **9. Stress / Overflow** | Tested with 60-character names, 0 items, 9999+ badges, and slow/offline responses without breaking layout. |

## 2. Operational UX Laws

- **Fitts's Law**: Primary CTAs and frequent controls must be large (`>= 44px` height on mobile) and placed in easy thumb/cursor reach. Destructive actions (Delete) must have extra friction or spatial separation from primary Confirm buttons.
- **Hick's Law**: Limit top-level navigation items to `5-7` and form steps to logical chunks to minimize decision paralysis.
- **Jakob's Law**: Preserve familiar conventions (logo top-left or centered linking to home, search top-right/center, close `X` top-right of modal, primary button right-aligned in modal footer on web/macOS).
- **WCAG 2.2 Quick Floor**: Keyboard-operable (`Tab`, `Shift+Tab`, `Enter`, `Space`, `Escape`), visible focus, `4.5:1` body contrast, `>= 24x24px` minimum target size (aim `44x44px` mobile), `prefers-reduced-motion` respected.

## 3. State Coverage Matrix

Use this per component/screen. Mark `Y`, `N`, or `N/A` with a reason.

| Component | Default | Hover | Focus | Active | Disabled | Loading | Empty | Error | Stress |
|---|---|---|---|---|---|---|---|---|---|
| Button | | | | | | | | | |
| Input | | | | | | | | | |
| Select/Combobox | | | | | | | | | |
| Card/List | | | | | | | | | |
| Table | | | | | | | | | |
| Modal/Drawer | | | | | | | | | |
| Navigation | | | | | | | | | |

A missing state is a finding, not a polish note, when it affects task completion or trust.

## 4. Validation Timing

- Validate **on blur** for format/constraints; **on submit** for cross-field rules.
- Do not show an error before the user has had a chance to type.
- Clear an error as soon as the input becomes valid.
- Keep the submit button enabled unless the form is truly incomplete; explain what is missing.
- Preserve entered data on error; never wipe the form.
- For long forms, show an error summary with links to each field.

## 5. Error Copy Formula

```text
[What happened] + [Why] + [How to fix]
```

Examples:

- Bad: “Invalid input.”
- Better: “Enter a phone number in +62 812 3456 7890 format.”
- Bad: “Error 422.”
- Better: “That email is already registered. Sign in or use another email.”

Rules: no blame, no jargon, no raw stack traces, no dead end. Put the message near the field and announce it.

## 6. Empty & Loading Patterns

| State | Good pattern | Avoid |
|---|---|---|
| **Empty (first use)** | Explain the value + primary action + example | Blank panel, “No data” only |
| **Empty (filtered)** | “No results for X” + clear filter action | Same as first-use empty |
| **Loading (initial)** | Skeleton matching final geometry | Full-page spinner for a card |
| **Loading (refresh)** | Inline progress, keep old data visible | Blanking the whole list |
| **Loading (action)** | Disable + spinner/pending label | Double-submit possible |
| **Partial failure** | Show what loaded; retry the failed part | One error kills the page |
| **Offline** | Clear offline state + retry | Silent stale data |

## 7. Destructive Actions

- Require confirmation for irreversible/high-impact actions; name the object and consequence.
- Prefer undo for reversible actions over a confirmation dialog.
- Separate destructive actions spatially from primary confirm.
- Do not use a generic “Are you sure?”; say what will be deleted.
- Provide a recovery path where possible.

## 8. Nielsen’s 10 Heuristics (audit lens)

1. Visibility of system status.
2. Match between system and real world.
3. User control and freedom (undo, cancel, back).
4. Consistency and standards.
5. Error prevention.
6. Recognition rather than recall.
7. Flexibility and efficiency of use.
8. Aesthetic and minimalist design.
9. Help users recognize, diagnose, and recover from errors.
10. Help and documentation.

Use these to explain **why** a finding matters, not as a substitute for measured evidence.

## 9. Cognitive Load Checks

- One primary decision per screen/section.
- Group related fields; chunk long forms.
- Do not make users remember information from a previous step.
- Prefer sensible defaults and autofill.
- Keep primary actions visible; avoid hiding critical actions in overflow menus.
- Use progressive disclosure for advanced options.
