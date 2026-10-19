---
name: game-audio-design
description: Plan game music, SFX, ambience, voice-over and audio implementation: style, adaptive/interactive music, mixing, formats, middleware (FMOD/Wwise), loudness, platform constraints.
---

# Game Audio Design

## Audio plan
1. **Audio pillars** matched to theme/mood (06).
2. **Music**: loops vs stingers, layered/vertical (add stems with intensity), horizontal re-sequencing, transitions on beat/bar, tempo map, menu/exploration/combat/boss/victory/defeat themes; chiptune, orchestral, lo-fi, synthwave, ambient, folk/traditional instruments (e.g. gamelan) per theme.
3. **SFX list**: UI, player actions, impacts, footsteps by surface, weapons, enemies, environment, notifications; 3-5 variations + pitch/volume randomization to avoid repetition fatigue.
4. **Ambience & spatial audio**: 3D attenuation curves, reverb zones, occlusion, HRTF for VR/headphones.
5. **Voice-over**: script, barks, localization plan, lip-sync approach, loudness consistency.
6. **Mixing**: buses (Master > Music/SFX/UI/Voice/Ambience), ducking (voice over music), compression, user volume sliders per bus, mute-on-focus-loss, mono/subtitle options.

## Technical
- Formats: WAV master; ship OGG Vorbis/Opus (or MP3/AAC where required); streaming for long music, in-memory for short SFX; loop points metadata.
- Loudness targets: music ~-18 to -14 LUFS, SFX peaks <-1 dBTP; mobile speakers need midrange emphasis.
- Latency: low-latency audio path for rhythm games (native audio, calibration screen). Web: user-gesture to unlock AudioContext, Howler.js/WebAudio.
- Middleware: FMOD, Wwise, Unity/Unreal/Godot built-in audio; Reaper/Audacity/BFXR/ChipTone/sfxr, LMMS/FL/Ableton, Tone.js for procedural.
- Licensing: royalty-free/CC0 sources vs commissioned; keep license log; AI music/voice terms and disclosure.

## Output
Audio bible, cue sheet (ID, trigger, loop?, length, priority, bus), implementation notes per engine, mix targets, asset specs for 07.
