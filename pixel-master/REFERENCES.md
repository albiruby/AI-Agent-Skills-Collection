# References and Tool Notes

This package is intentionally not tied to one pixel editor or game engine. The following official documentation is useful when an agent needs to verify current behavior. Always inspect the installed version and use matching documentation.

## Agent Skills format
- Microsoft Agent Skills specification and directory/frontmatter guidance: https://github.com/microsoft/skills/blob/main/.github/docs/skills.md

## Pixel-art editors
- Aseprite documentation: https://www.aseprite.org/docs/
- Aseprite CLI: https://aseprite.org/docs/cli/
- Aseprite scripting API: https://www.aseprite.org/api/
- LibreSprite: https://libresprite.github.io/
- Pixelorama: https://orama-interactive.itch.io/pixelorama (verify current repository/docs for the installed release)
- Piskel: https://www.piskelapp.com/

## Game engines / rendering
- Godot stable documentation: https://docs.godotengine.org/en/stable/
- Unity Manual: https://docs.unity3d.com/Manual/
- GameMaker manual: https://manual.gamemaker.io/
- RPG Maker product documentation: https://www.rpgmakerweb.com/
- Defold manual: https://defold.com/manuals/

## Implementation cautions
- Aseprite exposes CLI batch/export functions and a Lua scripting API; verify the version and command options before using them.
- Pixel-perfect rendering is engine- and renderer-specific. Check texture filtering, mipmaps, internal resolution, camera snapping, scaling, and UI rendering separately.
- Nearest-neighbor filtering is common for crisp pixel textures, but it is not a complete pixel-perfect solution by itself. Camera movement, fractional scaling, atlases, mipmaps, and UI layers can still cause artifacts.
- Do not copy commands or properties from a different major engine/editor version without verification.
