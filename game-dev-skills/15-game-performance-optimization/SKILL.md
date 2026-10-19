---
name: game-performance-optimization
description: Performance budgets and optimization for games: CPU/GPU/memory/battery/load time/build size, profiling workflow, draw calls, batching, pooling, LOD, GC, shaders, mobile/web/console targets.
---

# Performance Optimization

## Set budgets first
Target FPS (30/60/90/120), frame budget (60 fps = 16.6 ms), memory ceiling per platform (low-end Android often 2-3 GB with <1 GB usable), load time (<5-10 s to menu), build size (web <= ~10-30 MB initial; mobile APK/AAB limits), battery/thermal (sustained, not peak), min-spec device list.

## Workflow: Measure -> Identify -> Fix -> Re-measure
Profilers: engine profilers (Unity Profiler/Frame Debugger, Unreal Insights/stat commands, Godot Profiler/Monitors), RenderDoc, Xcode Instruments/Metal, Android GPU Inspector/Perfetto, Chrome DevTools/Spector.js. Always profile on **target hardware in release builds**.

## Checklist
**CPU**: object pooling, avoid per-frame allocations/GC spikes, cache component lookups, spatial partitioning (grid/quadtree), stagger AI/physics, jobs/threads/ECS, simplify physics layers, avoid heavy scripts in Update.
**GPU/Render**: batching/instancing/SRP batcher, atlases, reduce overdraw (transparent particles), LOD + culling (frustum/occlusion), shadow budget, baked lighting, lower-res post FX, texture compression + mipmaps, shader variants stripping, dynamic resolution/FSR/DLSS options.
**Memory**: streaming, addressables/asset bundles, unload unused, audio streaming, compress textures/meshes, avoid duplicate assets.
**Loading**: async/additive, loading screens with progress, preload hot assets, chunked worlds.
**Web**: WebGL2/WebGPU, texture KTX2, wasm size, gzip/brotli, lazy loading, avoid main-thread blocking, audio unlock, canvas resolution scaling for DPR.
**Mobile**: thermal throttling, 30 fps option, low-power mode, background pause, ASTC.
**Quality settings**: presets + auto-detect, expose toggles (shadows, effects, resolution, FPS cap, VSync).

## Output
Budget table per platform, profiling plan, prioritized optimization list with expected gain, quality-preset definition, perf regression test plan (automated benchmark scene in CI).
