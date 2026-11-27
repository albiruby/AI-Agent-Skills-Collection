# Example: Complete Character Pipeline

## Brief

A 32x32 side-view player character for a 2D action platformer, 4-direction set, idle/walk/run/attack/hit/death, Godot 4, 16-color dusk palette.

## 1. Lock the spec

- Paradigm: authentic pixel art.
- Native viewport: 480x270; integer scale to 1080p (4x).
- Character cell: 32x32; pivot bottom-center; feet 2 px above cell bottom.
- Projection: side view (plus mirrored left, redraw asymmetric weapon).
- Palette: 16 colors, locked hex order.
- Light: top-left; selective outline.
- Animation: 8 FPS for walk/run; attack 6 frames with hit event at frame 3.

Use `../templates/style-bible.md` and `../templates/palette-spec.md`.

## 2. Art direction

- Role silhouette: hooded runner with a short cape and a satchel.
- Silhouette hooks: hood peak, cape tail, satchel strap.
- 60-30-10 color distribution: 60% cloak, 30% tunic/boots, 10% scarf accent.
- Value hierarchy: character highest contrast; background compressed.

## 3. Character production

1. Block the idle silhouette in one flat color at 32x32.
2. Lock eye line, shoulder width, waist, foot baseline.
3. Add outfit clusters; avoid 1-pixel belts that vanish in motion.
4. Shade with the locked ramp and top-left light; use sel-out on lit edges.
5. Build down/side/up directions; mirror only if the design is symmetric.
6. Review at 1x and 4x on a representative background.

## 4. Animation

Use `../templates/sprite-animation-plan.md`:

| Clip | Frames | Timing | Loop | Event |
|---|---:|---|---|---|
| idle | 4 | 160/160/160/160 ms | yes | — |
| walk | 6 | 120/100/100/120/100/100 ms | yes | footstep frames 1,4 |
| attack | 6 | 80/60/50/120/100/80 ms | no | hitbox on frame 3 |
| hit | 2 | 80/120 ms | no | — |
| death | 8 | 120 ms each | no | — |

- Keep pivot/foot baseline fixed.
- Anticipation 1-2 frames; impact hold 2 frames; follow-through on cape 1 frame later.
- No duplicate first/last frame in loops.

## 5. Atlas and metadata

- Sheet: 6 columns x rows per clip, 32x32 cells, 1-2 px padding.
- JSON: frame tags, durations, pivot, events.
- Use `../templates/sprite-atlas-spec.md`.

## 6. Engine integration

- Godot 4: nearest filter, no mipmaps/compression, integer scaling, pixel snap.
- SpriteFrames: import durations; test idle/walk/attack transitions.
- CharacterBody2D collision: align to feet; test doorways/slopes.

## 7. QA

```bash
python scripts/pixel_art_qa.py export/hero_idle_side_00_32x32.png \
  --max-colors 16 --palette "<hex list>" --cell 32x32
```

Check:

- [ ] Silhouette reads at 1x
- [ ] Palette exact; no semi-alpha fringe
- [ ] Pivot stable; loops seamless
- [ ] Attack hitbox event aligns
- [ ] Engine import tested
- [ ] Source + exports + manifest delivered

## 8. Handoff

State files, dimensions, palette, pivot, frame durations, engine settings, QA results, and anything untested.
