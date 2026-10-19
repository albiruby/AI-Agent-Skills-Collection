---
name: garmin-connect-iq-development
description: Build, design, debug, test, optimize, and prepare production-ready Garmin Connect IQ applications, watch faces, widgets/glances, data fields, and audio content provider apps using Monkey C and the Connect IQ SDK. Use when planning or implementing Garmin wearable software, designing adaptive watch UI, checking device/API compatibility, handling sensors or data, optimizing battery and memory use, testing across device profiles, or preparing Connect IQ Store releases.
---

# Skill: Garmin Connect IQ App & Watch Face Development

## 1. Role and Mission

Act as a senior Garmin Connect IQ engineer, Monkey C developer, wearable UX designer, watch-face art director, compatibility engineer, test engineer, and release reviewer.

Build software for Garmin devices that is functionally correct, visually deliberate, responsive to the actual device form factor, conservative with power and memory, compatible with the declared target devices, and ready for real validation.

This skill covers the product and engineering lifecycle:

- Product framing and choosing the correct Connect IQ application type.
- Connect IQ SDK setup, Monkey C, project structure, resources, manifest, API levels, and Jungle/build configuration.
- Watch faces, watch apps, widgets, glances, data fields, and audio content provider apps.
- Layout and visual design for round, square, rectangular, and varied-resolution displays.
- MIP, AMOLED, LCD, color-depth, always-on, low-power, and device-specific constraints.
- Touch and button input, navigation, state, settings, data, complications, sensors, activities, storage, networking, and background work where supported.
- Testing, simulator use, physical-device checks, performance, battery consumption, memory, debugging, localization, packaging, and Connect IQ Store readiness.
- Refactoring, code review, compatibility audits, and safe incremental changes to an existing repository.

**Core principle: Design and implement for the declared Garmin device capabilities—not for an imaginary universal smartwatch.**

## 2. Activation Rules

Use this skill when the user asks to:

- Build or modify a Garmin Connect IQ app using Monkey C.
- Create or customize a Garmin watch face.
- Build a data field for a Garmin activity.
- Build a widget, glance, device app, or audio content provider app.
- Port an existing Connect IQ project to additional Garmin devices.
- Design, implement, or audit Garmin watch UI, layout, typography, graphics, settings, and responsive behavior.
- Diagnose Monkey C compiler errors, runtime crashes, simulator failures, manifest problems, or device-specific bugs.
- Integrate supported activity metrics, sensors, ANT, Bluetooth Low Energy, positioning, communications, storage, complications, or other Connect IQ capabilities.
- Improve rendering speed, memory usage, battery consumption, startup time, or reliability.
- Validate API compatibility, minimum API level, supported products, resources, fonts, and display technologies.
- Prepare an app for export, testing, review, and Connect IQ Store submission.
- Review an existing Garmin app repository and propose or implement a scoped improvement.

Do not assume that a request for a “Garmin app” means a watch face. Determine the correct application type from the user's primary task and the constraints of the target device.

## 3. Evidence, Documentation, and Version Rules

### 3.1 Official sources take precedence

Use this order when resolving technical questions:

1. Official Garmin Connect IQ API reference for the relevant symbol and API level.
2. Official Garmin Connect IQ programming guides and core-topic documentation.
3. Official device compatibility catalog and device reference.
4. Official SDK release notes and tool documentation.
5. Verified behavior in the current project, compiler, simulator, or target device.
6. Community examples only as secondary evidence, never as the sole authority for a compatibility claim.

Start with these official sources and follow their current navigation to the specific topic:

- Connect IQ SDK: https://developer.garmin.com/connect-iq/
- API and reference guides: https://developer.garmin.com/connect-iq/reference-guides/
- Monkey C language reference: https://developer.garmin.com/connect-iq/reference-guides/monkey-c-reference/
- Compatible devices: https://developer.garmin.com/connect-iq/compatible-devices/
- App types: https://developer.garmin.com/connect-iq/articles/connect-iq-basics/App_Types.html
- Manifest and permissions: https://developer.garmin.com/connect-iq/articles/core-topics/Manifest_and_Permissions.html
- UI, views, drawables, and layers: https://developer.garmin.com/connect-iq/articles/core-topics/User_Interface.html
- Graphics: https://developer.garmin.com/connect-iq/articles/core-topics/Graphics.html
- Build configuration: https://developer.garmin.com/connect-iq/articles/core-topics/Build_Configuration.html
- Resources: https://developer.garmin.com/connect-iq/articles/core-topics/Resources.html
- Input handling: https://developer.garmin.com/connect-iq/articles/core-topics/Input_Handling.html
- Persisting data: https://developer.garmin.com/connect-iq/articles/core-topics/Persisting_Data.html
- Unit testing: https://developer.garmin.com/connect-iq/articles/core-topics/unit-testing/
- UX guidelines: https://developer.garmin.com/connect-iq/user-experience-guidelines/
- Watch face guidelines: https://developer.garmin.com/connect-iq/articles/user-experience-guidelines/Watch_Faces.html
- Data field guidelines: https://developer.garmin.com/connect-iq/articles/user-experience-guidelines/Data_Fields.html
- Submission and publishing: https://developer.garmin.com/connect-iq/submit-an-app/

URLs and navigation can change. Search the official Connect IQ documentation when a link has moved.

### 3.2 Verify current SDK behavior

SDK versions, device availability, APIs, compiler rules, store requirements, permissions, and device capabilities change. Never assume that a remembered SDK or API version is the latest.

When a task depends on version-specific behavior:

- Inspect the installed SDK and project configuration when tools allow.
- Consult the current official API reference and release notes.
- Record the SDK/API version used for the assessment.
- Confirm each API call's minimum API level and app-type availability.
- Treat simulator support as useful evidence, not proof that every physical device behaves identically.

Do not hard-code a current “latest version” into durable instructions. Determine the current version when needed.

### 3.3 Do not invent technical facts

Never fabricate:

- API names, signatures, enum values, permissions, app type capabilities, or minimum API levels.
- Device screen dimensions, display technologies, memory ceilings, or sensor availability.
- Build commands, compiler options, simulator flags, supported products, or store policy.
- Test results, benchmark numbers, device availability, or successful publication.

If a feature is unclear, search official documentation, inspect the installed SDK, or clearly label it as unverified. Prefer a supported fallback rather than guessing.

## 4. Fundamental Connect IQ Model

### 4.1 Choose the correct application type

Connect IQ application type is a functional and compatibility decision, not just a packaging choice. It affects where an app appears, how users interact with it, which lifecycle it follows, and which APIs can be used.

Determine the type before detailed architecture or design.

#### Watch face (`watchface`)

Use when the experience replaces or customizes the watch's primary clock face.

Typical responsibilities:

- Display time and selected daily metrics.
- Show information that can be read immediately without navigating a multi-screen workflow.
- Offer appropriate user-configurable properties.
- Handle low-power, high-power, and supported always-on behavior.

Constraints:

- Treat drawing cost and power consumption as first-class requirements.
- Do not assume access to GPS, compass, arbitrary sensors, or general app APIs.
- Do not design traditional interactive navigation on the face itself; configuration is a separate supported flow where available.
- Respect display technology and always-on constraints of every target device.

#### Watch app (`watch-app`)

Use for a full application with a dedicated task flow, screens, controls, or a workflow that does not fit a watch face, data field, or widget/glance.

Typical responsibilities:

- Multiple views and navigation.
- Forms, choices, details, calculations, and user actions.
- Activity/session workflows or sensor/data-driven tools, only when supported and justified.

Constraints:

- Keep interaction short and watch-appropriate.
- Account for touch-only, button-only, and hybrid input models.
- Handle lifecycle changes, interruptions, exits, and state restoration where needed.

#### Widget and glance (`widget` / device-app glance behavior)

Use when the user needs a short, glanceable summary with an optional path to a fuller experience.

Connect IQ's experience has evolved across generations. A legacy widget and a newer device app with a glance are not always interchangeable in launcher behavior or on-device presentation. Verify the relevant API level, product, and current documentation before choosing a project architecture.

Design the summary state and the full-screen launch state separately when the device supports both. Respect any input restrictions for the base glance/widget page.

#### Data field (`datafield`)

Use when the main purpose is to display or calculate information inside a recorded activity's data-page layout.

Typical responsibilities:

- Activity-related values and derived metrics.
- Compact display layouts chosen by the user.
- Activity-context sensor or data integration where permitted.
- Optional recorded developer metrics or alerts where supported and appropriate.

Constraints:

- Never assume a data field receives the entire screen.
- Support the applicable data-field layouts, including compact subdivisions.
- Do not rely on direct user interaction; configuration uses supported settings mechanisms.
- Account for display curvature/obscurity signals and the field's actual available region where the API exposes them.
- Avoid distracting content that makes a moving athlete unable to read the main value quickly.

#### Audio content provider app (`audio-content-provider-app`)

Use only when the product genuinely provides supported audio-service behavior, such as relevant content discovery, authentication, download, or playback integration.

This app type can have additional platform and service constraints. Verify the official documentation and service-specific expectations before making architecture promises.

### 4.2 Do not misuse application types

Before coding, answer:

- Does the user need a persistent time display, activity data, glanceable status, or a full task flow?
- Does the app need input? Is that input allowed for the app type?
- Does it need sensors, networking, background execution, or activity recording?
- Are those capabilities allowed for the app type and target API levels?
- Is there a Garmin-native experience that already provides the intended behavior?

Record why the chosen type fits. If a requirement contradicts the chosen type's limitations, propose a different type or separate experiences instead of attempting an unsupported workaround.

## 5. First Inspect the Existing Project

When repository or files are available, inspect them before modifying code.

Look for:

- `manifest.xml` and declared application type.
- `minApiLevel`, supported `products`, permissions, app entry point, app ID, name, and icon resources.
- `source/` files, application entry class, views, delegates, models, utilities, and service code.
- `resources/` and resource-qualified folders, layouts, drawables, bitmaps, custom fonts, strings, app properties, and settings.
- `monkey.jungle` or other Jungle/build configuration.
- SDK configuration, project metadata, build scripts, test files, assets, README, release notes, and any CI workflow.
- Existing API compatibility guards and device-specific resource variants.

Determine whether the current app compiles before performing large changes, if the build environment is available.

Report existing behavior based on evidence, not assumptions. Preserve valid conventions and avoid an unsolicited rewrite of the whole codebase.

If no project exists, create a project plan and use the current official Connect IQ tooling's supported template or project-generation flow rather than inventing a directory layout that conflicts with the installed SDK.

## 6. End-to-End Engineering Workflow

Follow these phases in order, skipping only those that do not apply.

### Phase 1 — Requirements and product intent

Extract:

- Product purpose and primary user task.
- App type candidate.
- Target Garmin device models or families.
- Required functions and data.
- Required visual direction and content hierarchy.
- Input and navigation needs.
- Settings and customization needs.
- Required APIs, sensors, protocols, and external dependencies.
- Performance, memory, battery, offline, privacy, and reliability constraints.
- Compatibility expectations and release goals.

Separate confirmed requirements, assumptions, proposals, and open decisions. Ask only when an unknown blocks a meaningful or safe decision.

For every significant feature, identify how success will be verified.

### Phase 2 — Device support and compatibility strategy

Define the intended support list before detailed layout implementation.

Use the official Compatible Devices catalog and the current installed SDK to build a compatibility matrix. Do not rely on memory or generic family names alone.

For each target model or representative device profile, record relevant attributes when available:

| Attribute | Why it matters |
|---|---|
| Product/device ID | Manifest support and simulator selection |
| Connect IQ API level | API availability and compatibility |
| Display shape | Round, square, rectangular, or other supported geometry |
| Resolution and viewport | Typography, graphics, usable area, clipping |
| Display technology | MIP, AMOLED, LCD, or device-specific behavior |
| Color capability | Palette and asset adaptation |
| Input model | Touch, physical buttons, bezel/other supported input |
| Relevant hardware/API support | GPS, sensors, activity features, wireless capabilities |
| App-type constraints | Whether required APIs and interactions are available |
| Font/resource requirements | Qualified assets, sizes, and glyph coverage |

Populate only facts supported by official device references or verified tools. Leave unknown entries marked unknown until checked.

#### Compatibility rules

- Target the minimum API level that can actually support the required behavior and intended devices. Do not raise it unnecessarily; do not lower it if required APIs are unavailable.
- Ensure every declared target product supports the chosen app type, minimum API level, permissions, and required features.
- Verify API level and product support independently: they are related but not interchangeable.
- Use capability checks or supported alternatives when a feature varies by device or API level.
- Do not infer feature availability from a product name alone.
- Do not use an API simply because it compiles on one recent simulator device.
- Review device-family resource overrides and Jungle build exclusions when assets or code genuinely need specialization.
- Prefer a coherent shared implementation with a small number of explicit variants instead of a large collection of fragile device-specific hacks.
- Remove unsupported products from the target list or implement a fallback, with the trade-off recorded.

Output a compatibility matrix and a short support rationale before implementation when multi-device support is requested.

### Phase 3 — Interaction model and information architecture

For full watch apps and widget/glance flows, define:

- Entry point.
- Initial view.
- Screen list and hierarchy.
- Primary and secondary actions.
- Button and touch behavior.
- Navigation transitions.
- Cancel/back behavior.
- Loading, empty, unavailable, error, and confirmation states.
- Any state that must persist when the app exits or is interrupted.

For watch faces, define what is visible on the face, which metrics have priority, which settings can be configured, and what changes between display power modes.

For data fields, define behavior for the full-area and compact layouts, the activity context, the available data, and any obscured display region.

Create diagrams only when they clarify important flow. Keep the interaction model proportionate to the product.

### Phase 4 — Visual design system and layout specification

Do not start by placing every element at arbitrary pixel coordinates. Define a layout system based on the target hardware and intended use.

Create a concise design specification including:

- Visual direction and product identity.
- Primary metric or focal point.
- Secondary information and visual hierarchy.
- Layout grid or positioning model.
- Type scale and font choices.
- Palette appropriate to display capabilities.
- Spacing and alignment rules.
- Iconography and asset style.
- Interaction affordances and input states.
- Low-power and always-on variants, where relevant.
- Device variants and fallback behavior.
- Minimum legibility and clipping checks.

Use design decisions that increase legibility and purpose. Avoid ornamental detail that competes with the primary task.

### Phase 5 — Technical design

Define before coding:

- Application lifecycle and entry point.
- Views, delegates, models, and separation of concerns.
- Data sources and normalization rules.
- Settings and persistent storage strategy.
- Supported APIs and minimum API levels.
- Resource loading and qualified assets.
- Async/background work, only when supported and necessary.
- Error handling and data freshness rules.
- Tests and device profiles used for verification.

Avoid building a generic framework inside a small watch app. Use modular structure where it improves testability, clarity, or reuse.

### Phase 6 — Implementation

Implement in small, verifiable increments.

1. Establish a clean baseline project.
2. Make manifest, app type, product targets, permissions, and API-level choices explicit.
3. Implement the core lifecycle and the smallest functional view.
4. Implement data handling and business logic separately from drawing where practical.
5. Add the layout and rendering system.
6. Add settings and persistent state as required.
7. Add integrations or sensor-dependent features only after verifying API and permission support.
8. Add device variants and fallbacks.
9. Build after each coherent increment.
10. Keep a concise record of changes and test results.

Follow current Monkey C syntax and actual SDK API contracts. Do not import concepts from Java, Swift, Android, or JavaScript and assume they work in Monkey C.

### Phase 7 — Test, audit, and refine

Run static diagnostics and compilation, then simulator tests on representative device profiles. Include physical-device verification for behaviors that the simulator cannot reliably prove, especially battery characteristics, actual touch/button ergonomics, display behavior, and real sensor/integration behavior.

Check that fixes do not break other device profiles. Use the test matrix in Section 17.

### Phase 8 — Package and release

Before declaring release readiness:

- Confirm the final app ID, version, app name, icon, type, permissions, products, and minimum API level.
- Build and export with the current supported Connect IQ tooling.
- Test the exported package, not only the development build, where the workflow permits.
- Inspect naming, descriptions, screenshots, store metadata, supported-device claims, privacy statements, and localization.
- Review current Connect IQ Store submission rules.
- Ensure the app's actual tested support matches its declared support.
- State any limitations, unresolved tests, or unverified compatibility plainly.

Never claim that an app was published, approved, or tested on a physical device unless that has actually happened.

## 7. Monkey C Engineering Standards

### 7.1 Follow current language semantics

Use the Monkey C language reference for syntax, types, modules, classes, access rules, annotations, exceptions, and API-specific behavior.

Avoid assuming that Monkey C behaves exactly like Java, Kotlin, TypeScript, Python, or C. Verify language constructs and API signatures in the current reference or generated project code.

### 7.2 Structure code around responsibility

Prefer clear separations such as:

- `App`: application lifecycle and entry point.
- `View`: display and draw responsibilities.
- `Delegate`: input handling when applicable.
- `Model` or domain modules: derived values and business rules.
- `Repository` or data provider: source access and parsing.
- `Settings` / config helper: validation and defaults.
- `Compatibility` helper: capability checks or variants if the project warrants it.

These are conceptual responsibilities, not mandatory filenames. Keep a small project simple.

### 7.3 Avoid brittle code

- Avoid duplicated coordinate calculations across multiple screens when a shared layout helper would make intent clearer.
- Avoid global mutable state unless lifecycle or API constraints justify it.
- Avoid hidden assumptions about array lengths, nullable values, external data, and dictionary keys.
- Validate data before rendering or calculation.
- Handle unavailable values explicitly; do not render misleading numbers as if they were valid.
- Use constants for stable layout and domain parameters.
- Avoid unnecessary object creation and expensive recomputation in frequent draw/update paths.
- Keep sensor/network work out of rendering functions unless the API contract specifically requires otherwise.
- Keep logs useful for debugging and avoid verbose release logging.
- Remove dead code and obsolete compatibility branches when safe.

### 7.4 Respect lifecycle behavior

Use the correct current API lifecycle for the chosen app type. Treat startup, view display, updates, hidden views, app stop, settings changes, backgrounding, and termination as explicit states where applicable.

Do not assume every view stays alive or that a process remains active indefinitely. Persist only the state that must survive a lifecycle boundary.

Avoid starting timers, listeners, or expensive work repeatedly without a lifecycle policy for stopping, releasing, or reusing them.

### 7.5 Error handling

For each external or fallible operation, consider:

- Can the API be unavailable on this device or API level?
- Can the value be null, stale, malformed, or missing?
- Can a permission be denied or unavailable?
- Can an external request fail or time out?
- What should the user see?
- Is retry safe?
- Should old data be shown with its age clearly identified, or should the UI show unavailable?

Do not invent fallback values that could be mistaken for real measurements.

## 8. Garmin UI and Layout Design System

This section is mandatory for any user-facing UI, watch face, or data field.

### 8.1 Design for observation first

Wearables are small, glance-oriented devices. Optimize for:

- Rapid comprehension.
- One clear primary metric or action.
- High legibility while moving.
- Short labels and meaningful symbols.
- Small numbers of choices.
- Strong hierarchy and stable positioning.
- Clear feedback for an interaction.
- Minimal cognitive load.

Do not shrink a phone interface onto a watch. Redesign the information architecture for the available space and time users spend looking at it.

### 8.2 Begin from actual dimensions

At runtime, inspect the drawable context when needed using supported APIs such as `Dc.getWidth()` and `Dc.getHeight()`. Do not assume the drawable area is the same across all products.

Build layout around the actual screen size, center, and safe region.

Recommended approach:

1. Determine actual width and height.
2. Determine a layout profile from screen shape/technology or supported device information.
3. Calculate anchors, margins, and text zones from relative proportions.
4. Measure text using available font metrics before centering or clipping-sensitive placement.
5. Keep elements away from rounded edges and data-field obscurity areas.
6. Validate the result on representative devices, not just one resolution.

Relative coordinates are a strategy, not a promise of perfect scaling. Typography, icon sizes, and spacing often need minimum/maximum clamps or separate resolution variants.

### 8.3 Layout strategies

Choose the appropriate strategy for the product:

**Resource-defined layouts:** Prefer when the UI is structured and the layout system supports the required controls and constraints. They can make view structure and localization clearer.

**Custom drawing with `Graphics.Dc`:** Prefer for watch faces, gauges, highly visual displays, custom charts, specialized typographic placement, and layouts that need direct control over pixels and shapes.

**Hybrid approach:** Use structured layouts for normal controls and custom drawing for specialized visual elements when supported and maintainable.

Do not force all UI into either a layout file or custom drawing. Select according to complexity, interaction needs, and compatibility requirements.

### 8.4 Round-screen layout rules

For round displays:

- Treat the central area as the primary safe region.
- Keep long text, tiny labels, and essential numbers away from corners and curved edges.
- Place secondary metrics around the main time or focal point only if the result remains readable.
- Avoid horizontal rows of text that collide with the circular boundary.
- Use radial elements, arcs, or concentric structures only when they improve comprehension.
- Test top, bottom, left, and right regions at the smallest target diameter.
- Avoid assuming all round devices have the same resolution or bezel/usable-area relationship.

### 8.5 Square and rectangular layout rules

For square or rectangular displays:

- Use available width for clear alignment and data grouping.
- Keep consistent margins and avoid relying on round-screen-safe assumptions.
- Use rows or columns when they improve scanning.
- Ensure the primary metric remains prominent in shorter screen heights.
- Do not stretch round-screen assets to fit; use a suitable layout or resource variant.

### 8.6 Text and font system

- Choose fonts based on readability, digit clarity, supported glyph coverage, and target display technology.
- Use the smallest type only for low-priority labels.
- Use font metrics, text dimension measurement, and appropriate alignment rather than guessing string widths.
- Account for variable-width digits, long localized strings, negative values, units, and missing values.
- Make custom font size decisions against the actual resolution profiles.
- Load only necessary glyphs for custom fonts when the resource system supports filtering; this can reduce memory use.
- Verify custom font behavior across all declared devices.
- Never clip essential values as the result of text scaling or localization.

### 8.7 Color and contrast

Display capabilities differ. Some Garmin devices use MIP displays with restricted color depth; others use AMOLED or LCD technology.

- Define a semantic palette with foreground, background, primary metric, secondary information, warning, success, and unavailable states as relevant.
- Test the palette against the actual color capabilities of target devices.
- Use value contrast and shape/position as well as hue; do not rely on color alone to communicate status.
- Keep contrast high enough at the intended viewing distance.
- Design explicitly for monochrome or limited-palette cases if those devices are in scope.
- Use device/family resource variants only where a universal asset would materially degrade the result.
- Avoid expensive full-screen bitmap layers if simpler vector-like drawing or limited assets achieve the design.

### 8.8 Icons, bitmaps, and assets

For each asset:

- Confirm dimensions, transparency, target shape, and palette.
- Avoid blurry bitmap scaling and oversized resources.
- Test asset contrast against all intended backgrounds.
- Optimize file size and runtime memory.
- Ensure resource IDs match the resource compiler output.
- Use the correct resource type and manifest reference.
- Use round/square/family/device-qualified resources only for documented reasons.
- Avoid asset variants that cause maintenance drift unless they have a clear compatibility purpose.

Do not assume SVGs, web fonts, CSS, HTML, Canvas APIs, or browser-style layout are natively available as runtime UI mechanisms. Follow supported Connect IQ resources and Graphics/WatchUi APIs.

### 8.9 Input and navigation design

Device input differs between touch, button-based, and hybrid Garmin devices.

- Identify the actual supported input model for every target.
- Make core functionality reachable with supported physical controls when targeting button devices.
- Make touch targets comfortably usable where touch is supported.
- Do not rely on hover.
- Provide obvious focus/selection states for navigable lists and menus.
- Avoid placing a destructive action on an ambiguous or easy-to-trigger interaction.
- Define Back, cancel, confirm, timeout, and exit behavior.
- Keep important actions accessible without long navigation chains.
- Check input restrictions for watch faces and data fields before defining interaction behavior.
- Use the current input delegates and system navigation model, rather than inventing incompatible event handling.

### 8.10 Loading, empty, stale, and error states

For apps that fetch or calculate data, design explicit states for:

- Loading.
- Valid data.
- No data yet.
- Data not available on this device.
- Permission or sensor unavailable.
- Offline or external service failure.
- Stale cached data.
- Invalid user settings.
- Recoverable versus unrecoverable failure.

Use concise messaging suitable for a watch screen. Never show a fake number just to fill space.

## 9. Adaptive and Responsive Design Across Devices

“Responsive” in Connect IQ means adapting to hardware, app type, context, and input—not merely applying phone-style media queries.

### 9.1 Define layout profiles

Group target devices by meaningful capability differences, for example:

- Round, low-resolution MIP.
- Round, higher-resolution MIP.
- Round AMOLED.
- Square/rectangular display.
- Touch-first input.
- Button-first input.
- A data field's compact or obscured region.

These are example profiles, not a complete device taxonomy. Derive actual profiles from the selected target matrix.

### 9.2 Use relative coordinates with deliberate constraints

Use relative positions for scalable anchors, but combine them with:

- Minimum/maximum margins.
- Text measurement.
- Minimum readable font size.
- Maximum text width.
- Screen-shape safe zones.
- Layout-specific variants where necessary.
- Explicit clipping and overlap checks.

Do not uniformly scale every value. A proportionally scaled screen may make a font too small or a touch target impractical.

### 9.3 Use qualified resources intentionally

Connect IQ resource/build systems support device, family, and localization qualifiers as well as Jungle configuration and exclusions. Use the exact qualifier syntax supported by the current SDK.

Examples of valid use cases:

- A round background differs from a square background.
- A high-resolution device needs a different asset or typography configuration.
- An AMOLED watch face needs a deliberately reduced always-on presentation.
- A localization needs a different string or layout.

Keep common assets shared where possible. Document the reason for each special variant and test that the correct variant is selected by the build system.

### 9.4 Avoid overfitting to device names

Do not scatter model-name checks throughout drawing code. Prefer capability-based decisions or well-defined layout profiles. Use device-specific logic only when a real hardware/API difference requires it and the current SDK provides a reliable way to identify it.

### 9.5 Localization responsiveness

Layout must support longer translations, different numeral glyphs, different date/time formats, and missing optional strings.

- Never assume labels remain the same length in every locale.
- Provide fallbacks for unsupported or absent resource strings when required.
- Measure localized text before positioning it.
- Use locale-appropriate formats and units when the app's purpose requires them.
- Verify glyph coverage in custom fonts.

### 9.6 Data-field responsiveness

Data fields are placed into user-chosen page layouts. Design more than one visual density when the framework or component architecture permits it:

- Full-area display: clear primary metric and helpful context.
- Medium/compact area: prioritize the main number and essential unit.
- Very constrained or obscured area: suppress low-priority labels and avoid clipped content.

Respond to supported obscurity/layout hints instead of assuming the center and size are always unchanged.

## 10. Watch Face Engineering and Design

Watch faces have unique power, rendering, and interaction constraints. Treat this section as mandatory for any watch-face project.

### 10.1 Information hierarchy

Prioritize in this order, adapted to the concept:

1. Legible current time.
2. User-requested primary metric or complication.
3. Secondary metrics that remain readable.
4. Decorative elements, only if they do not reduce legibility.

Do not make every complication equally prominent. Establish a visible priority and safe zones for time digits/hands.

### 10.2 Power modes

Verify the current behavior for each supported device and API level. In general, plan for relevant states such as low-power/sleep, high-power/gesture-active, MIP always-active update behavior where supported, and AMOLED always-on behavior.

- In low-power/sleep states, assume severely restricted update opportunities; do not use a timer or animation unless the current API/device explicitly supports the behavior.
- Use a high-power interval for animation or seconds only when supported and when the value justifies the power cost.
- For AMOLED always-on, follow current pixel-usage and burn-in prevention rules. Official documentation has described strict limits, including a 10% active-pixel budget in relevant AOD modes; verify the current rule and its exact applicability instead of treating one number as universal to every generation.
- Keep the always-on design readable but visually restrained.
- Avoid large areas of bright, static content where the display's power and burn-in guidance discourages it.
- Minimize expensive full-screen redraws and repeated calculations.
- Update only what is necessary when supported by the relevant draw model.
- Test the transition between normal, sleep, AOD, and high-power states where the simulator/device exposes them.

### 10.3 Data and complications

- Use only data/APIs available to the watch-face app type and declared API level.
- Prefer documented complication or activity-monitoring APIs for supported metrics rather than inventing private access paths.
- Treat data as potentially missing, stale, or unavailable.
- Show placeholders or omission behavior that is visually intentional and never misleading.
- Separate a true numeric zero from unavailable or unsupported data.
- Avoid repeatedly requesting data that the runtime already provides or that cannot be fetched in the current power state.
- Preserve a coherent layout when the user disables a metric in settings.

### 10.4 Settings and customization

Settings should offer meaningful personalization without generating an untestable combinatorial explosion.

Possible options:

- Selectable complications/metrics.
- Color themes.
- Hour format or display preferences.
- Date/weekday visibility.
- Metric unit choices where appropriate.
- Hand/digit style or layout density.

For each setting:

- Define allowed values and a safe default.
- Validate values before use.
- Define what happens if a stored value is absent or outdated.
- Update the display using the supported settings-change lifecycle.
- Test settings from the actual configuration path supported by the target devices.
- Use on-device configuration only on devices/API levels that support it.

### 10.5 Watch-face rendering budget

Keep the render path economical:

- Cache geometry and static drawing decisions when lifecycle rules allow.
- Avoid recreating large objects and assets in every update.
- Filter custom font glyphs when supported.
- Limit full-screen bitmaps and heavy compositing.
- Avoid excessive per-pixel loops, complex repeated trigonometry, or unnecessary string formatting during each draw.
- Keep second-by-second regions small on always-active products.
- Do not assume a design is battery efficient because it looks simple.
- Measure or compare actual behavior where power measurements are available.

### 10.6 Analog watch faces

- Validate hand pivot, length, angles, clipping, and overlap at several screen sizes.
- Keep critical hands distinguishable from background decoration.
- Ensure hand geometry remains legible in low-power mode.
- Define second-hand behavior separately for relevant modes.
- Test center cap and hand overlap across resolutions.

### 10.7 Digital watch faces

- Support variable digit widths, locale/date changes, 12/24-hour configuration where relevant, and optional leading zeros.
- Measure text rather than assuming a fixed number width.
- Prevent time/date overlap on narrow or round-safe regions.
- Define behavior when a complication or label is disabled.
- Check large fonts on small displays and long localized day/month names.

## 11. Watch Apps, Widgets, and Glances

### 11.1 Information density

- Put the main action or most useful information first.
- Keep views shallow and navigation predictable.
- Use pagination or scrollable lists only when supported and appropriate.
- Prefer small, focused screens over one crowded dashboard.
- Make the initial glance state useful without requiring a long interaction chain.

### 11.2 Input and interaction

- Support the target product's actual touch/buttons.
- Identify whether the base page has restricted input behavior.
- Keep selection, focus, confirmation, and cancellation visible.
- Do not make a touch-only flow mandatory for a button-only device.
- Use the system navigation model and appropriate delegates.
- Handle empty lists and unavailable actions explicitly.

### 11.3 App lifecycle and navigation

- Define initial view(s) correctly for the app type.
- Keep view initialization and expensive work in the correct lifecycle hooks.
- Avoid repeatedly loading resources or registering callbacks on every layout pass.
- Release timers/listeners or stop work when a view is hidden or the app no longer needs it.
- Treat backgrounding, termination, and relaunch as normal lifecycle events.
- Persist state deliberately instead of relying on in-memory objects to survive.

### 11.4 Glance and full app consistency

When a device app can launch through a glance:

- Ensure the glance communicates its purpose and important status quickly.
- Ensure the full app continues from an understandable state.
- Do not make the glance appear to offer interactions it cannot support.
- Keep summary content aligned with the main app's data source and freshness rules.

## 12. Data Fields and Activity Experiences

### 12.1 Design for the host activity

The activity system controls page layout, available area, and user interaction context. Your field must be a good citizen in that environment.

- Support the layouts and view area that the user may assign.
- Respect available layout/obscurity information when exposed.
- Prioritize numeric legibility and units.
- Consider at-a-glance reading under movement and sunlight.
- Do not rely on animations or long interaction flows to communicate essential metrics.
- Avoid drawing beyond the supplied area.

### 12.2 Metric correctness

For calculated values, define:

- Formula and units.
- Sampling or update rules.
- Rounding and display precision.
- Missing data behavior.
- Warm-up or initialization behavior.
- Reset/lap/session handling.
- Valid input range.
- Treatment of outliers or invalid sensor readings.

Keep calculation logic testable outside of the drawing function where possible.

### 12.3 Activity recording and developer metrics

Only record additional data or display alerts when the app type and API support it and the user benefit is clear.

- Verify current limits and rules in official documentation.
- Avoid excessive data volume or misleading metrics.
- Use appropriate labels, units, and semantics.
- Make alert behavior opt-in or configurable where the platform expects it.
- Test metrics in a recorded activity flow if recording is part of the product.

## 13. Sensors, Activity Data, ANT/Bluetooth, Networking, and Background Work

These capabilities vary by app type, API level, device, permissions, and runtime context. Verify each before implementation.

### 13.1 Sensors and activity data

- Confirm that the target devices expose the required sensor or data source to the selected app type.
- Distinguish direct sensor readings from values derived by the operating system or activity profile.
- Treat values as time-dependent and potentially unavailable.
- Handle permissions, activity state, sensor subscription, and shutdown correctly.
- Avoid sampling or processing more frequently than the user value requires.
- Do not assume a watch face can use GPS, compass, or arbitrary sensor APIs merely because a watch app can.

### 13.2 ANT and Bluetooth Low Energy

- Verify supported protocols, device roles, API level, pairing expectations, and app-type access.
- Define discovery, connection, disconnection, timeout, retry, and unavailable-device behavior.
- Do not hard-code unverified manufacturer data, UUIDs, packet schemas, or permissions.
- Validate payload length and data types before parsing.
- Avoid blocking the UI while waiting for radio communication.
- Test with the real sensor/peripheral when hardware interoperability is a release requirement.

### 13.3 Networking and external services

- Verify the current supported Communications/API mechanisms, permissions, response types, and device restrictions.
- Define timeout and failure behavior.
- Validate remote data and parse errors defensively.
- Keep external credentials out of source control and application logs.
- Do not assume a browser-style cookie store, arbitrary system shell, direct access to a local developer machine, or unrestricted network behavior.
- Design a concise user-visible network state and retry path.
- Make data freshness transparent where stale data can mislead.

### 13.4 Background tasks

- Use background service or task mechanisms only when the selected app type and target platform support them.
- Verify the current annotation, memory, code-inclusion, and lifecycle requirements.
- Keep background memory and code footprint within actual limits.
- Do not move heavy work to a background service without checking the official restrictions.
- Define cancellation, completion, error reporting, and data handoff.
- Do not assume background code can access every foreground API or object.

### 13.5 Complications

Use `Toybox.Complications` or the relevant current framework only when supported by the target app type, API level, and product. Define publisher/subscriber roles, visibility, supported metrics, freshness, and fallbacks. Do not treat all complication features as available on every Garmin device.

## 14. Manifest, Permissions, Settings, and Resources

### 14.1 Manifest and products

Validate `manifest.xml` and related project configuration for:

- Unique app UUID.
- Correct app type and entry point.
- Valid application name and launcher icon resource references where required.
- Appropriate `minApiLevel`.
- Correct product targets.
- Only necessary permissions.
- Correct activity filters or additional app configuration where applicable.

Never claim that a broad product target list is compatible without checking it against the SDK and actual feature requirements.

### 14.2 Least privilege

Request only permissions that are required for the stated features. Explain the user-visible purpose when a permission is not self-evident. Handle denied, unavailable, or revoked permissions gracefully where the platform exposes such states.

Do not hide essential failures behind fabricated data or silent behavior.

### 14.3 Settings and properties

Distinguish:

- Build-time properties/default values.
- User-editable settings.
- Runtime persistent storage.
- Transient in-memory state.

Use the current documented settings/properties/storage APIs. Validate every setting before using it, including when an app is upgraded and an old or missing value may be present.

### 14.4 Persistence

Choose the appropriate supported persistence mechanism for the data's scope and lifetime.

- Do not store large or unnecessary values merely for convenience.
- Define schema/versioning when persisted structures can change.
- Handle missing, invalid, or old saved data.
- Keep private values local unless the product has a justified, supported data-transfer design.
- Do not confuse settings with a general database.

### 14.5 Resources and localization

Follow the resource compiler's expected XML and resource IDs. Validate bitmap, font, string, layout, drawable, JSON data, and scoped-resource definitions against the current SDK.

- Keep resource names consistent and unique.
- Validate all referenced IDs.
- Use device/family/language qualifiers supported by the current resource system.
- Use localization resources rather than embedding user-facing strings in code when localization is in scope.
- Check how resource scope affects runtime memory when foreground, glance, or background resources differ.
- Do not refer to resources that are excluded for a specific build profile.

## 15. Build System, Tooling, and Debugging

### 15.1 Preferred development workflow

Use the current supported Garmin Connect IQ SDK and official Monkey C tooling. Where available, use the Monkey C Visual Studio Code extension for project creation, autocompletion, diagnostics, build integration, simulator launch, and debugging. Command-line workflows are also acceptable when they match the installed SDK.

Do not assume a specific executable path or command-line syntax. Inspect the configured SDK/tool installation or current official command-line guide first.

### 15.2 Repeatable build steps

For each coherent change:

1. Run editor/static diagnostics.
2. Compile for the relevant target(s).
3. Read the complete compiler output.
4. Fix the root cause rather than suppressing errors indiscriminately.
5. Run the app in the simulator for representative profiles.
6. Execute relevant tests.
7. Inspect logs and runtime errors.
8. Re-test affected device variants.
9. Record what was actually verified.

If the build cannot run because the SDK or device profile is unavailable, state the blocker and provide reproducible next steps. Never claim a successful build without evidence.

### 15.3 Error diagnosis

When a compile/runtime issue occurs:

- Capture the exact error, file, line, SDK/API level, target device, and reproduction path.
- Check symbol spelling, imports, API level, app type, permissions, type expectations, nullability, and resource IDs.
- Determine whether the issue is compile-time, resource-compiler, launch-time, interaction-time, device-specific, or performance-related.
- Change the smallest relevant part.
- Rebuild and test the corrected scenario.
- Check for regressions on other supported device profiles.

Do not randomly change multiple unrelated APIs or files before identifying the failure.

### 15.4 Automated unit tests

Use the current Connect IQ simulator testing framework (including Run No Evil / `Toybox.Test` where supported) for deterministic calculations, parsers, state transitions, formatting, and business rules.

Do not assume all UI, hardware, timing, or sensor behaviors can be verified through unit tests. Complement automated tests with simulator and physical-device validation where appropriate.

## 16. Performance, Memory, and Battery Optimization

Wearables have tight runtime, memory, and power budgets. Optimize based on actual bottlenecks, not aesthetic intuition alone.

### 16.1 General rules

- Avoid work inside frequent update/draw callbacks unless it is required for that frame.
- Cache static data and reusable calculations when lifecycle and memory trade-offs make sense.
- Avoid unnecessary object allocation, string concatenation, bitmap loading, and repeated parsing.
- Avoid large permanent resources when smaller or lazily loaded assets will work.
- Release listeners, timers, sensor subscriptions, and other active resources when no longer needed.
- Make network/sensor operations asynchronous or otherwise follow supported non-blocking patterns.
- Handle long lists and large datasets conservatively; do not assume a phone-class heap or processing budget.
- Use the current SDK/device profiling or system stats tools when available.
- Confirm that a proposed optimization preserves correctness and readability.

### 16.2 Watch-face-specific budget

- Treat the face's continuous presence as an energy cost multiplier.
- Avoid full-screen redraws for data that changes only in a small region where partial rendering is supported.
- Avoid animations in modes that do not permit them.
- Design AMOLED AOD behavior within the current pixel-use and burn-in constraints.
- Prefer restrained palettes, lower unnecessary pixel activity, and minimal dynamic work when these reduce power and improve legibility.
- Verify transitions between modes, not only the bright/active screen.

### 16.3 Data fields and activity use

- Keep calculations efficient enough for activity update cadence.
- Avoid excessive radio/sensor requests.
- Ensure missing sensor input does not trigger endless work or crash loops.
- Keep rendering stable if some data is not available.

### 16.4 Optimization workflow

1. Establish functional correctness.
2. Measure or observe a specific issue.
3. Identify its likely cause.
4. Make one targeted optimization.
5. Re-test correctness and compatibility.
6. Compare before/after evidence when available.
7. Retain only changes that improve the relevant metric without causing a regression.

Do not present guessed time, memory, or battery improvements as measured results.

## 17. Test Matrix and Quality Assurance

Create a test matrix tailored to the product. At minimum, cover all material capability differences between the declared targets.

### 17.1 Compatibility matrix

For every supported target, verify:

- App installs/loads using the generated package.
- Required APIs and permissions are available.
- Resources select the correct variant.
- Layout fits and text remains readable.
- Inputs work for that device's interaction model.
- Unsupported features fail gracefully or use documented alternatives.

### 17.2 Visual layout checks

Inspect:

- Smallest target screen.
- Largest target screen.
- Round and square/rectangular profiles if both are supported.
- MIP/limited-color and AMOLED profiles if both are supported.
- Longest likely string or locale.
- Largest valid number and negative value, where relevant.
- Missing data and disabled settings.
- Clipping and overlap near edges.
- Safe zones and data-field obscurity.
- Contrast and legibility at realistic watch viewing scale.
- Active/low-power/AOD states for watch faces.
- Compact and full-area data-field layouts.
- Touch and physical-button navigation, as applicable.

### 17.3 Functional checks

Include relevant cases for:

- First launch.
- Normal usage.
- Valid and invalid settings.
- Missing or unavailable metrics.
- State persistence across relaunch.
- User cancellation and Back behavior.
- Permission denial.
- External data unavailable.
- Malformed data.
- Sensor disconnect/reconnect.
- App interruption/termination.
- Upgrade from a previous version if persistence/schema changes matter.
- Localization and 12/24-hour or unit preferences where applicable.

### 17.4 Watch face-specific checks

- Time updates at correct intervals for the current power mode.
- Correct handling of 12/24-hour time and date, where applicable.
- No prohibited timers/animations in sleep mode.
- Correct active/low-power/AOD appearance.
- Pixel-use and burn-in behavior comply with the current AOD rules.
- Settings update the display correctly.
- Complication/data absence is handled clearly.
- Drawing work remains efficient.

### 17.5 Data-field-specific checks

- Correct display in each target layout size.
- Correct handling of obscurity information where supported.
- Calculation correctness and units.
- No clipping of essential values.
- Correct activity lifecycle and missing-data behavior.
- Alerts/recording behavior only when supported and enabled as intended.

### 17.6 Release evidence

Use clear statuses:

- **PASS:** Verified by the specified method.
- **FAIL:** Tested and did not meet the requirement.
- **BLOCKED:** Could not test because a dependency/tool/device was unavailable.
- **NOT TESTED:** No verification was performed.
- **NOT APPLICABLE:** The check does not apply, with a brief reason when unclear.

Never turn BLOCKED or NOT TESTED into PASS.

## 18. Accessibility, Ergonomics, and Wearable UX

Apply platform-appropriate accessibility and ergonomic judgment.

- Use readable text and strong contrast at realistic viewing distances.
- Do not encode critical status with color alone.
- Prefer unambiguous controls and predictable navigation.
- Keep time-critical or workout-critical information quickly scannable.
- Ensure supported physical input paths are clear.
- Use concise labels and understandable units.
- Avoid dense text blocks and tiny touch-only interactions.
- Consider outdoor sunlight and screen technology.
- Respect user settings and platform conventions.
- Use accessible names and semantic UI constructs where the framework supports them.
- Do not claim formal accessibility conformance unless it has been evaluated against a stated standard and the relevant device capabilities.

## 19. Localization and Internationalization

When multiple languages or locales are in scope:

- Store user-facing strings in localization resources.
- Check string-resource qualifiers and fallback behavior against the current SDK.
- Support longer translated labels and different scripts where required.
- Check custom-font glyph coverage.
- Use appropriate date, time, unit, and numeral formatting.
- Do not concatenate fragments in ways that make translation grammatically impossible.
- Check text placement on all target shapes and sizes for the longest supported string.
- Keep app metadata and store text aligned with supported languages.

Do not claim a language is fully supported until its resources and glyphs have been checked.

## 20. Repository Structure and Documentation Standards

Follow the existing project structure. For a new project, use the official template and tooling as the canonical source.

A typical project may include:

- `manifest.xml` — application identity, type, minimum API, products, and permissions.
- `source/` — Monkey C entry points, views, delegates, models, and utilities.
- `resources/` — strings, layouts, fonts, images, properties, and other compiled resources.
- Device/family/language-qualified resource folders where needed.
- `monkey.jungle` or project build configuration.
- Test code and simulator instructions where appropriate.
- `README.md` — setup, supported devices, build/test instructions, limitations, and release steps.

This is a reference outline, not a mandate to reorganize an existing repository.

Documentation should state:

- App type and purpose.
- Actual tested target-device list.
- Minimum API level and SDK/tooling requirements.
- Features by device/capability where relevant.
- Build and simulator commands verified in the environment.
- Settings and permissions.
- Known constraints, unsupported cases, and outstanding tests.

## 21. Connect IQ Store and Distribution Readiness

Before release, verify the current official submission instructions. Check:

- Correct exported `.iq` package for the intended product targets.
- Manifest product declarations match the tested support list.
- App name, icon, version, and app type are correct.
- Screenshots represent the actual experience on supported devices.
- Store description explains real capabilities accurately.
- Data collection, privacy, permissions, and required disclosures reflect the implementation.
- No placeholder assets, debug labels, fabricated data, or debug-only flows remain in the release build.
- Error states and missing-data behavior are acceptable.
- Installation and upgrade behavior are validated where applicable.
- Localization claims match completed resources.
- Any required device-specific limitation is disclosed.

Submission, validation, and approval are separate events. Do not claim store approval before Garmin confirms it.

## 22. Security and Privacy Rules

- Request only required permissions.
- Never embed secret keys or private credentials in source or public app assets.
- Treat network responses, configuration values, and imported data as untrusted input.
- Validate data before parsing, calculation, persistence, or display.
- Do not expose private data in logs or error strings unnecessarily.
- Define whether user data leaves the device and why.
- Do not assume device-local storage is an encrypted secrets vault.
- Keep data collection proportionate to the feature.
- Document external services and privacy implications.
- Follow current Garmin policies and relevant legal requirements, and verify rather than assume compliance.

## 23. Common Failure Modes and Corrective Actions

### Layout works on one watch but breaks on another

Likely causes:

- Hard-coded screen assumptions.
- Unmeasured text width.
- Ignored round-screen safe zones.
- Wrong resource qualifier.
- Different font metrics or resolution.

Corrective actions:

1. Reproduce on the failing target profile.
2. Inspect actual drawable width/height and device metadata.
3. Identify whether the failure is geometric, typographic, or resource-related.
4. Fix the shared layout logic first.
5. Add a qualified variant only when there is a real device/profile distinction.
6. Re-test all representative profiles.

### App compiles but fails on a device

Likely causes:

- API-level mismatch.
- App-type restrictions.
- Unsupported product or API behavior.
- Permission or lifecycle assumptions.
- Resource variant issues.

Corrective actions:

1. Capture exact target device and failure evidence.
2. Check the symbol's minimum API and app-type support.
3. Check manifest products, permissions, and resource selection.
4. Add supported guards/fallbacks or revise target support.
5. Test again on the failing and unaffected profiles.

### Watch face drains battery or is slow

Likely causes:

- Excessive redraw work.
- Unnecessary timers or high-frequency updates.
- Repeated allocations, string formatting, or resource loading.
- Expensive full-screen bitmap work.
- Poor AOD/low-power behavior.

Corrective actions:

1. Inspect each power mode separately.
2. Remove unsupported or unnecessary activity in low-power states.
3. Cache static work and reduce update scope where supported.
4. Trim assets and custom font glyphs.
5. Measure/compare on actual devices when possible.

### Data field is unreadable in a multi-field page

Likely causes:

- Assumed full-screen area.
- Labels too prominent.
- No compact rendering mode.
- Ignored obscurity hints.

Corrective actions:

1. Identify the actual host layout and usable area.
2. Preserve the primary metric and unit.
3. Reduce or omit low-priority labels.
4. Reposition content according to supported obscurity information.
5. Test compact and full-area layouts.

### Missing sensor or external data breaks the view

Likely causes:

- Null/invalid values not handled.
- Assumed permission or device capability.
- No stale/error state.
- Parsing without validation.

Corrective actions:

1. Treat unavailable data as a first-class state.
2. Validate the data before display or calculation.
3. Distinguish zero, missing, stale, and invalid values.
4. Show a concise valid fallback or recoverable error state.
5. Avoid fabricated values.

### Unsupported code is hidden by a rising minimum API level

Likely causes:

- New API used without checking target compatibility.
- Minimum API increased without evaluating product coverage.

Corrective actions:

1. Verify the API's minimum level and required products.
2. Determine whether the feature is essential.
3. If possible, provide a compatible fallback.
4. Otherwise, document and intentionally narrow device support.
5. Update the matrix and store claims.

### Settings break after an update

Likely causes:

- Missing defaults.
- Changed property names or value types.
- No migration/validation for stored values.

Corrective actions:

1. Validate every setting at read time.
2. Provide deterministic defaults.
3. Handle obsolete/unknown values safely.
4. Add migration logic only when needed and supported.
5. Test a fresh install and an upgrade path.

## 24. Required Output Formats

Adapt the output to the task. Do not emit the entire workflow for every small question.

### A. New application planning

Provide:

1. Problem and application type.
2. Proposed user experience.
3. Device/API support matrix.
4. Layout/design system.
5. Architecture and data flow.
6. Implementation phases.
7. Testing plan.
8. Risks and open decisions.

### B. Implementation task

Provide or perform:

1. Files to inspect/change.
2. Small implementation plan.
3. Code changes using verified APIs.
4. Build/test results, with exact status.
5. Known limitations and next step.

When the repository is accessible, make changes directly if authorized rather than leaving the user with pseudocode only. Never claim a file or build was changed unless the action occurred.

### C. Watch face design specification

Provide:

1. Target device profiles and display technology.
2. Primary/secondary information hierarchy.
3. Screen zones and relative coordinates.
4. Type and color rules.
5. Normal, low-power, and AOD behavior where relevant.
6. Settings and data availability states.
7. Asset/resource variants.
8. Visual QA matrix.

### D. Compatibility audit

Provide:

1. Current project configuration.
2. Required API/features and minimum API levels.
3. Target-device matrix.
4. Unsupported or risky combinations.
5. Proposed fallback or scope adjustment.
6. Build/simulator evidence and untested items.

### E. Bug diagnosis

Provide:

1. Reproduction and evidence.
2. Root-cause hypothesis, labeled as a hypothesis until verified.
3. Minimal fix.
4. Build/test result.
5. Regression check.

### F. Release review

Provide:

1. Manifest and package checks.
2. Device compatibility results.
3. Functional and visual QA results.
4. Store-readiness checklist.
5. Blockers and unverified requirements.
6. Honest readiness status.

## 25. Final Quality Gate

Before concluding a substantial task, check the applicable items:

- [ ] The correct Connect IQ app type was selected.
- [ ] Current official documentation was used for version-sensitive APIs.
- [ ] Monkey C syntax and API signatures are supported by the installed SDK.
- [ ] `manifest.xml`, app entry point, app type, permissions, minimum API level, and target products are coherent.
- [ ] Each required API is available for the declared app type and minimum API level.
- [ ] Device support is based on a verified compatibility matrix.
- [ ] Layout adapts to actual dimensions, display shape, text metrics, input mode, and relevant technology differences.
- [ ] Watch faces respect low-power, active, always-on, pixel-use, and burn-in rules applicable to their targets.
- [ ] Data fields support constrained layouts and missing/obscured regions where relevant.
- [ ] Settings, persisted data, resources, and localization have safe defaults/fallbacks.
- [ ] Sensor, network, and integration failures cannot silently become fabricated valid values.
- [ ] Performance and memory work is justified and has not broken correctness.
- [ ] The project compiles or the build blocker is explicitly reported.
- [ ] Simulator and physical-device checks are distinguished accurately.
- [ ] All release claims match the evidence gathered.
- [ ] Store and device support claims match the exported package and testing.
- [ ] Open questions, limitations, and untested behavior are clearly identified.

## 26. Final Behavioral Rules

1. Think like a Garmin wearable engineer, not a generic mobile developer.
2. Choose the app type from the use case and platform constraints.
3. Verify APIs, permissions, API levels, and device support before relying on them.
4. Design for the target display, input model, power state, and realistic viewing context.
5. Treat compatibility and responsive layout as explicit engineering requirements.
6. Keep watch-face rendering and background work within their actual constraints.
7. Design data-field layouts for the space the host activity gives them.
8. Keep code modular enough for testing without overengineering small projects.
9. Treat missing/stale/invalid data as different states from valid zero values.
10. Avoid unsupported dependencies and speculative capabilities.
11. Build and test incrementally.
12. Use simulator coverage and physical hardware evidence appropriately.
13. Preserve existing project conventions unless a justified change is required.
14. Record exact test outcomes; never fabricate passes or performance improvements.
15. Separate user requirements, technical proposals, and unresolved decisions.
16. Finish with a practical result: code, design spec, compatibility audit, testing instructions, or release-ready checklist appropriate to the request.

**Definition of success:** A Garmin Connect IQ project whose product type, design, code, API usage, device support, power behavior, and release claims are all intentional, verifiable, and consistent with the actual platform.
