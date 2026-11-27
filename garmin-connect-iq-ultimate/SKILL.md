---
name: garmin-connect-iq-ultimate
description: Master skill pack with 120 modular sub-skills for building, architecting, optimizing, and publishing Garmin Connect IQ watch faces, activity data fields, device apps, widgets/glances, background services, ANT+/BLE sensor integrations, custom UI themes (ECG bio-monitor, 16-bit pixel art, tactical HUD), and FIT file contributors in Monkey C. Use whenever the user asks to create, design, code, debug, or optimize anything for Garmin smartwatches or Edge cycling computers.
---

# Garmin Connect IQ Ultimate (120 Sub-Skills Pack)

A modular skill pack containing **120 specialized sub-skill modules** (`001` through `120`) for engineering production-grade Garmin Connect IQ software in Monkey C across all Garmin wearable (Fenix, Epix, Forerunner, Venu, Vivoactive, Instinct, MARQ) and Edge cycling hardware families.

## When to Use

- Designing or coding a Garmin **Watch Face** (`001` to `025`) with MIP 1Hz partial updates, AMOLED AOD burn-in shifting, `BufferedBitmap` caching, analog polygon hands, or complications
- Engineering an activity **Data Field** (`026` to `055`) with live `Activity.Info` telemetry, 3s/10s/30s power buffers, Normalized Power (NP), GAP, W'bal, or metabolic carbohydrate/hydration codecs
- Recording custom **FitContributor** developer fields or pairing **ANT+ / BLE GATT** sensors (`056` to `075`)
- Building interactive **Device Apps**, **Widgets/Glances**, **Background Services**, or **Audio Content Providers** (`076` to `095`)
- Crafting custom **UI Aesthetics** (ECG bio-monitor, 16-bit pixel-art sprites, tactical HUDs), optimizing **Memory/Bit-Packing**, or packaging `.iq` releases (`096` to `120`)

## Core Workflow Steps

1. **Select Target Sub-Skills**: Identify the required sub-skills from the 120-module catalog below and load them via `get_skill_resources`.
2. **Scaffold Project**: Run `scripts/scaffold_ciq_project.py` or copy from `assets/manifest-template.xml`, `assets/monkey-jungle-template.txt`, `assets/WatchFaceTemplate.mc.txt`, and `assets/DataFieldTemplate.mc.txt`.
3. **Enforce Strict Type Safety**: Write all Monkey C code with explicit type annotations and `null` / `has` guards to pass `--typecheck 3` (`-l 3`).
4. **Verify Power & Memory Budgets**: Run `scripts/audit_ciq_project.py` to confirm zero `loadResource()` calls inside `onUpdate(dc)`, clipped 1Hz updates (`<30ms`), and AMOLED AOD compliance (`<10%` active pixels with periodic pixel shifting).

## Complete 120 Sub-Skills Catalog (`references/`)

- `references/001-wf-lifecycle-states.md`: **WatchFace Lifecycle & Power State Machine** (WatchFace - `WatchUi.WatchFace`)
- `references/002-wf-screen-geometry.md`: **Screen Geometry & Safe-Zone Anchor Caching** (WatchFace - `Graphics.Dc`)
- `references/003-wf-mip-1hz-clip.md`: **MIP 1Hz Partial Update & Clipping Region** (WatchFace - `WatchUi.WatchFace.onPartialUpdate`)
- `references/004-wf-power-budget.md`: **WatchFaceDelegate 30ms Power Budget Guard** (WatchFace - `WatchUi.WatchFaceDelegate`)
- `references/005-wf-amoled-aod-burnin.md`: **AMOLED Burn-In Protection Detection** (WatchFace - `System.DeviceSettings`)
- `references/006-wf-amoled-pixel-shift.md`: **AMOLED Deterministic Lissajous Pixel Shifter** (WatchFace - `Graphics.Dc`)
- `references/007-wf-amoled-dim-mask.md`: **AMOLED 10% Lit-Pixel Luminance Dither Mask** (WatchFace - `Graphics.Dc`)
- `references/008-wf-buffered-bitmap.md`: **CIQ 4.0+ Graphics Pool BufferedBitmap Caching** (WatchFace - `Graphics.BufferedBitmapReference`)
- `references/009-wf-palette-compress.md`: **Indexed Palette Compression for Offscreen Buffers** (WatchFace - `Graphics.BufferedBitmap`)
- `references/010-wf-polygon-hands.md`: **2D Rotation Matrix Vector Polygon Watch Hands** (WatchFace - `Graphics.Dc.fillPolygon`)
- `references/011-wf-antialias-draw.md`: **Hardware Anti-Aliasing for Vectors & Arcs** (WatchFace - `Graphics.Dc.setAntiAlias`)
- `references/012-wf-digital-kerning.md`: **Tabular Monospace Digital Time Kerning** (WatchFace - `Graphics.Dc.getTextDimensions`)
- `references/013-wf-bitmap-fonts.md`: **Custom BMFont (.fnt + .png) Glyph Filtering** (WatchFace - `WatchUi.FontResource`)
- `references/014-wf-radial-arc-gauges.md`: **Segmented Radial Arc Gauges & Angle Mapping** (WatchFace - `Graphics.Dc.drawArc`)
- `references/015-wf-goal-progress-bars.md`: **Steps, Calories & Active Minutes Goal Bars** (WatchFace - `ActivityMonitor.Info`)
- `references/016-wf-battery-gauge.md`: **Battery Percentage & Remaining Days Estimation** (WatchFace - `System.Stats`)
- `references/017-wf-solar-intensity.md`: **Solar Charging Intensity Ring (Solar Watches)** (WatchFace - `System.Stats.solarIntensity`)
- `references/018-wf-sunrise-sunset.md`: **Sunrise, Sunset & Golden Hour Calculation** (WatchFace - `Toybox.Weather`)
- `references/019-wf-moon-phase.md`: **Synodic Lunar Phase & Illumination Math** (WatchFace - `Toybox.Time`)
- `references/020-wf-world-clock.md`: **Dual Timezone & UTC Offset World Clock** (WatchFace - `System.ClockTime`)
- `references/021-wf-ble-notif-icons.md`: **Bluetooth Connection & Notification Count Badge** (WatchFace - `System.DeviceSettings`)
- `references/022-wf-alarm-dnd-icons.md`: **Alarm Count & Do Not Disturb Status Indicators** (WatchFace - `System.DeviceSettings`)
- `references/023-wf-ondevice-config.md`: **On-Device WatchFace Customize Menu (getSettingsView)** (WatchFace - `Application.AppBase.getSettingsView`)
- `references/024-wf-touch-comp-exit.md`: **Touch-Hold Complication Exit-To-Native-Widget** (WatchFace - `Toybox.Complications.exitTo`)
- `references/025-wf-instinct-cutout.md`: **Instinct 2 / Crossover Subscreen Cutout Alignment** (WatchFace - `WatchUi.getSubscreen`)
- `references/026-df-simple-vs-custom.md`: **SimpleDataField vs Full Custom DataField Selection** (DataField - `WatchUi.SimpleDataField`)
- `references/027-df-compute-vs-onupdate.md`: **Separation of 1Hz compute(info) vs Visible onUpdate(dc)** (DataField - `WatchUi.DataField`)
- `references/028-df-obscurity-flags.md`: **Round Bezel Obscurity Bitmask Detection** (DataField - `WatchUi.DataField.getObscurityFlags`)
- `references/029-df-dynamic-grid-tiers.md`: **Adaptive 4-Tier Layout Engine (1-Field to 8-Field)** (DataField - `Graphics.Dc`)
- `references/030-df-day-night-polarity.md`: **Automatic Day/Night Background Color Polarity** (DataField - `WatchUi.DataField.getBackgroundColor`)
- `references/031-df-timer-callbacks.md`: **Activity Timer Start, Pause, Resume, Stop & Reset Hooks** (DataField - `WatchUi.DataField`)
- `references/032-df-lap-accumulator.md`: **Lap Button Event & Per-Lap Metric Snapshot** (DataField - `WatchUi.DataField.onTimerLap`)
- `references/033-df-workout-targets.md`: **Structured Workout Step & Target Range Inspector** (DataField - `Activity.getCurrentWorkoutStep`)
- `references/034-df-alert-popups.md`: **Full-Screen DataFieldAlert Popups & Haptics** (DataField - `WatchUi.DataFieldAlert`)
- `references/035-df-hr-zone-colors.md`: **UserProfile Heart Rate Zone Lookup & Color Coding** (DataField - `UserProfile.getHeartRateZones`)
- `references/036-df-pace-smoothing.md`: **Rolling 5-Second Running Pace Filter (min/km & min/mi)** (DataField - `Activity.Info.currentSpeed`)
- `references/037-df-gap-minetti.md`: **Grade Adjusted Pace (GAP) Minetti Cost Model** (DataField - `Activity.Info`)
- `references/038-df-power-ring-buf.md`: **3s, 10s & 30s Cycling/Running Power Ring Buffer** (DataField - `Activity.Info.currentPower`)
- `references/039-df-normalized-power.md`: **Coggan Normalized Power (NP) 4th-Power Engine** (DataField - `Activity.Info.currentPower`)
- `references/040-df-if-tss-load.md`: **Intensity Factor (IF) & Training Stress Score (TSS)** (DataField - `Activity.Info`)
- `references/041-df-wprime-balance.md`: **Skiba W'bal Anaerobic Work Capacity Differential Model** (DataField - `Activity.Info.currentPower`)
- `references/042-df-stride-length.md`: **Running Cadence & Real-Time Stride Length Math** (DataField - `Activity.Info.currentCadence`)
- `references/043-df-vertical-speed-vam.md`: **Vertical Ascent Speed (VAM m/h & ft/h)** (DataField - `Activity.Info.verticalSpeed`)
- `references/044-df-alt-grade-filter.md`: **Barometric Altitude & Road Gradient (%) Kalman Filter** (DataField - `Activity.Info.altitude`)
- `references/045-df-race-eta-predict.md`: **Finish Time Predictor & Target Distance ETA** (DataField - `Activity.Info.elapsedDistance`)
- `references/046-df-waypoint-compass.md`: **Next Waypoint Distance, Bearing & Relative Arrow** (DataField - `Activity.Info.bearing`)
- `references/047-df-offcourse-alert.md`: **Course Navigation Off-Course Distance Monitor** (DataField - `Activity.Info.offCourseDistance`)
- `references/048-df-training-effect.md`: **Dual Aerobic & Anaerobic Training Effect Bars** (DataField - `Activity.Info.trainingEffect`)
- `references/049-df-kcal-burn-rate.md`: **Real-Time Caloric Burn Rate (kcal/h & kcal/km)** (DataField - `Activity.Info.energyExpenditure`)
- `references/050-df-carb-scheduler.md`: **Glycogen Depletion & Carbohydrate Intake Codec** (DataField - `Activity.Info`)
- `references/051-df-sweat-hydration.md`: **Sweat Rate & Sodium Electrolyte Depletion Model** (DataField - `Activity.Info`)
- `references/052-df-cardiac-drift.md`: **Cardiac Drift & Thermal Strain Index** (DataField - `Activity.Info`)
- `references/053-df-gps-quality-bar.md`: **GPS Constellation Quality & Accuracy Indicator** (DataField - `Activity.Info.currentLocationAccuracy`)
- `references/054-df-edge-wide-panels.md`: **Edge 540/840/1040/1050 Rectangular Cycling Panels** (DataField - `Graphics.Dc`)
- `references/055-df-touch-page-cycle.md`: **Interactive Touch-Tap View Mode Cycling in DataFields** (DataField - `WatchUi.InputDelegate`)
- `references/056-fit-xml-schema.md`: **FitContributor XML Resource Schema & Chart Colors** (FitContributor - `Toybox.FitContributor`)
- `references/057-fit-record-stream.md`: **MESG_TYPE_RECORD 1Hz Time-Series FIT Stream** (FitContributor - `FitContributor.MESG_TYPE_RECORD`)
- `references/058-fit-lap-columns.md`: **MESG_TYPE_LAP Custom Lap Table Columns** (FitContributor - `FitContributor.MESG_TYPE_LAP`)
- `references/059-fit-session-totals.md`: **MESG_TYPE_SESSION Overall Activity Summary Stats** (FitContributor - `FitContributor.MESG_TYPE_SESSION`)
- `references/060-fit-255byte-budget.md`: **FIT 255-Byte Developer Data Budget Optimization** (FitContributor - `Toybox.FitContributor`)
- `references/061-ant-bikepower-listener.md`: **Native AntPlus.BikePower Torque, Cadence & Balance** (ANT+ - `Toybox.AntPlus.BikePower`)
- `references/062-ant-varia-radar.md`: **AntPlus.BikeRadar Approaching Vehicle Threat Tracker** (ANT+ - `Toybox.AntPlus.BikeRadar`)
- `references/063-ant-run-dynamics.md`: **AntPlus.RunningDynamics GCT, Vertical Oscillation & Ratio** (ANT+ - `Toybox.AntPlus.RunningDynamics`)
- `references/064-ant-di2-axs-shift.md`: **AntPlus.Shifting Electronic Drivetrain Gear & Battery** (ANT+ - `Toybox.AntPlus.Shifting`)
- `references/065-ant-fec-trainer.md`: **AntPlus.FitnessEquipment Smart Trainer ERG Control** (ANT+ - `Toybox.AntPlus.FitnessEquipment`)
- `references/066-ant-mo2-muscle-ox.md`: **Custom ANT+ GenericChannel Muscle Oxygen (MO2 / SmO2)** (ANT+ - `Toybox.Ant.GenericChannel`)
- `references/067-ant-core-body-temp.md`: **Custom ANT+ GenericChannel CORE Body Temperature** (ANT+ - `Toybox.Ant.GenericChannel`)
- `references/068-ant-burst-tx-msg.md`: **ANT+ Acknowledged & Burst Data Transmission** (ANT+ - `Toybox.Ant.GenericChannel`)
- `references/069-ble-uuid-registry.md`: **BluetoothLowEnergy Custom GATT Profile Registration** (BLE - `Toybox.BluetoothLowEnergy`)
- `references/070-ble-scan-filter-pairing.md`: **BLE Peripheral Scan Iterator & RSSI Filtering** (BLE - `BluetoothLowEnergy.BleDelegate`)
- `references/071-ble-gatt-char-read.md`: **BLE GATT Characteristic Read & ByteArray Decoding** (BLE - `BluetoothLowEnergy.Characteristic`)
- `references/072-ble-cccd-notify.md`: **BLE CCCD Notification & Indication Subscription** (BLE - `BluetoothLowEnergy.Descriptor`)
- `references/073-ble-write-queue.md`: **Sequential BLE GATT Operation Queue State Machine** (BLE - `BluetoothLowEnergy.BleDelegate`)
- `references/074-ble-auto-reconnect.md`: **BLE Disconnection Recovery & Unpair Cleanup** (BLE - `BluetoothLowEnergy.BleDelegate`)
- `references/075-sensor-25hz-accel.md`: **High-Frequency 25Hz Raw Accelerometer DataListener** (Sensor - `Toybox.Sensor.registerSensorDataListener`)
- `references/076-app-entry-lifecycle.md`: **AppBase Lifecycle: onStart, getInitialView & onStop** (DeviceApp - `Application.AppBase`)
- `references/077-app-glance-heap.md`: **(:glance) Annotation & 32KB Glance Heap Isolation** (Glance - `WatchUi.GlanceView`)
- `references/078-app-glance-chart.md`: **Glance Sparkline Mini-Chart & Cached Telemetry** (Glance - `WatchUi.GlanceView`)
- `references/079-app-input-delegate.md`: **Cross-Device BehaviorDelegate Semantic Navigation** (DeviceApp - `WatchUi.BehaviorDelegate`)
- `references/080-app-button-vs-touch.md`: **5-Button Tactile vs 2-Button Touchscreen Input Routing** (DeviceApp - `System.DeviceSettings.isTouchScreen`)
- `references/081-app-menu2-controls.md`: **WatchUi.Menu2 Native Toggle, Icon & Sublabel Menus** (DeviceApp - `WatchUi.Menu2`)
- `references/082-app-custom-menu.md`: **WatchUi.CustomMenu & CustomMenuItem Owner-Drawn Lists** (DeviceApp - `WatchUi.CustomMenu`)
- `references/083-app-number-picker.md`: **WatchUi.Picker Numeric & Custom Wheel Selectors** (DeviceApp - `WatchUi.Picker`)
- `references/084-app-viewloop-pages.md`: **Multi-Page Vertical Carousel & Bezel Page Dots** (DeviceApp - `WatchUi.ViewLoop`)
- `references/085-app-record-session.md`: **Standalone ActivityRecording Session & Sport Profiles** (DeviceApp - `Toybox.ActivityRecording`)
- `references/086-app-save-discard.md`: **Safe Workout Pause, Save & Discard Confirmation Flow** (DeviceApp - `Toybox.ActivityRecording.Session`)
- `references/087-app-gps-location.md`: **Multi-Band GNSS / GPS Continuous Location Subscription** (DeviceApp - `Toybox.Position`)
- `references/088-app-vibe-tone-alert.md`: **Tactile VibeProfile Sequences & Codec Audio Tones** (DeviceApp - `Toybox.Attention`)
- `references/089-app-backlight-ctrl.md`: **Programmatic Backlight Flash & Timeout Control** (DeviceApp - `Toybox.Attention.backlight`)
- `references/090-bg-temporal-5min.md`: **Background ServiceDelegate 5-Minute Temporal Scheduler** (Background - `Toybox.System.ServiceDelegate`)
- `references/091-bg-json-webrequest.md`: **Background HTTPS JSON WebRequest & Bearer Auth** (Background - `Toybox.Communications.makeWebRequest`)
- `references/092-bg-phone-comm-sync.md`: **Companion Smartphone App Mailbox & PhoneAppMessage** (Background - `Toybox.Communications`)
- `references/093-bg-comp-publisher.md`: **Background Custom Complication Publisher (CIQ 4.2+)** (Background - `Toybox.Complications.updateComplication`)
- `references/094-audio-wifi-sync.md`: **AudioContentProviderApp SyncDelegate & Playlist Download** (AudioProvider - `Toybox.Media.AudioContentProviderApp`)
- `references/095-audio-media-player.md`: **Media.ContentIterator & Playback Control Lifecycle** (AudioProvider - `Toybox.Media.ContentIterator`)
- `references/096-ui-ecg-bio-monitor.md`: **Resident Evil Bio-Monitor ECG Waveform Renderer** (UI-Theme - `Graphics.Dc.drawLine`)
- `references/097-ui-tactical-hud.md`: **Tactical Codec Corner Reticles & Scanline Frame** (UI-Theme - `Graphics.Dc`)
- `references/098-ui-16bit-pixel-art.md`: **16-Bit Pixel-Art Integer Grid & Non-Dithered Bitmaps** (UI-Theme - `WatchUi.BitmapResource`)
- `references/099-ui-palette-lock.md`: **3-Tone Cel-Shaded Hex Palette Lock for MIP & AMOLED** (UI-Theme - `Graphics.Dc`)
- `references/100-ui-tilemap-scroll.md`: **3/4 Top-Down Orthographic Tilemap Viewport Scroller** (UI-Theme - `Graphics.Dc.drawBitmap2`)
- `references/101-bio-body-battery.md`: **SensorHistory Body Battery & All-Day Stress Streams** (Biometrics - `Toybox.SensorHistory`)
- `references/102-bio-spo2-resp-rate.md`: **Pulse Ox SpO2 & Respiration Rate Biometric Readers** (Biometrics - `Toybox.SensorHistory`)
- `references/103-bio-baro-storm.md`: **3-Hour Barometric Pressure Delta & Storm Alert Arrow** (Biometrics - `SensorHistory.getPressureHistory`)
- `references/104-wth-forecast-api.md`: **Toybox.Weather Current Conditions & Hourly Sparkline** (Weather - `Toybox.Weather`)
- `references/105-mem-flat-arrays.md`: **Zero-Dictionary Flat Enum Array Architecture** (Memory - `Toybox.Lang.Array`)
- `references/106-mem-bit-packing.md`: **32-Bit Integer Coordinate & Color Bit-Packing** (Memory - `Toybox.Lang.Number`)
- `references/107-mem-byte-buffers.md`: **Compact ByteArray ([]b) Binary Telemetry Buffers** (Memory - `Toybox.Lang.ByteArray`)
- `references/108-mem-json-lookups.md`: **On-Demand jsonData XML Lookup Table Loading** (Memory - `WatchUi.loadResource`)
- `references/109-mem-weak-refs.md`: **WeakReference Safe Caching & Circular Reference Prevention** (Memory - `Toybox.Lang.WeakReference`)
- `references/110-mem-string-cache.md`: **Dirty-Flag String Caching in 1Hz Render Loops** (Memory - `Toybox.Lang.String`)
- `references/111-jgl-screen-routing.md`: **monkey.jungle Screen Shape & Resolution Resource Routing** (Build-Jungle - `monkey.jungle`)
- `references/112-jgl-exclude-tags.md`: **Compile-Time excludeAnnotations (:amoled vs :mip)** (Build-Jungle - `monkey.jungle`)
- `references/113-cpl-strict-types.md`: **Monkey C Strict Type Checking (--typecheck 3) Patterns** (Compiler - `Toybox.Lang`)
- `references/114-cpl-has-guards.md`: **Runtime 'has' Symbol & API Level Compatibility Guards** (Compiler - `Toybox.Lang`)
- `references/115-stg-disk-storage.md`: **Application.Storage Key-Value Disk Persistence** (Storage - `Toybox.Application.Storage`)
- `references/116-stg-gcm-settings.md`: **Garmin Connect Mobile App Settings & onSettingsChanged** (Storage - `Toybox.Application.Properties`)
- `references/117-loc-i18n-strings.md`: **Multi-Language String Resources & Dynamic Formatting** (Localization - `WatchUi.loadResource`)
- `references/118-tst-unit-testing.md`: **Run-No-Evil (:test) Automated Unit Test Suite** (Testing - `Toybox.Test`)
- `references/119-tst-heap-profiler.md`: **System.getSystemStats() Live Heap & Peak Memory Profiler** (Testing - `System.Stats`)
- `references/120-rel-iq-store-export.md`: **Signed .iq Connect IQ Store Release Packaging** (Release - `monkeyc CLI`)

## Bundled Assets & Automation Scripts

- `assets/manifest-template.xml`: Multi-device `manifest.xml` template.
- `assets/monkey-jungle-template.txt`: Multi-screen `monkey.jungle` build routing template.
- `assets/WatchFaceTemplate.mc.txt`: Complete WatchFace template with MIP 1Hz clip & AMOLED AOD shifting.
- `assets/DataFieldTemplate.mc.txt`: Complete DataField template with `FitContributor` & dynamic layout tiers.
- `scripts/scaffold_ciq_project.py`: CLI project generator for all 5 Connect IQ app types.
- `scripts/audit_ciq_project.py`: Static analyzer checking memory, null safety, and power-budget rules.

## Gotchas

- **Reference-Counted Memory Leaks**: Monkey C uses reference counting rather than mark-and-sweep garbage collection. Always break circular references (`View <-> Delegate`) using `WeakReference` (`obj.weak()`) or nulling references in `onHide()`.
- **Dictionary Heap Overhead**: Replace small `Dictionary` objects with flat `Array<Number>` structures and 32-bit bit-packing (`105-mem-flat-arrays.md`, `106-mem-bit-packing.md`).
