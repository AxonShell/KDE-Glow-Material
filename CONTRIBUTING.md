# Contributing

Thank you for helping develop Glow Material for MuliOS.

## Before opening a change

1. Read `docs/DESIGN.md`.
2. Check component status in `docs/ARCHITECTURE.md` and `docs/ROADMAP.md`.
3. Keep changes focused on one component where practical.
4. Never describe a scaffold, mockup, or untested effect as production-ready.

## Design contributions

- Prefer contextual illumination over permanent neon decoration.
- Preserve contrast and clear keyboard focus.
- Consider rest, hover, focused, pressed, selected, disabled, and inactive states.
- Respect reduced-motion preferences.
- Update shared tokens and documentation when changing visual behavior.
- Include screenshots for visual changes where practical.

## Code contributions

- Follow conventions of the relevant KDE component and its upstream API.
- Keep Plasma, Aurorae, KWin, and Qt integrations modular.
- Document supported Plasma, Qt, and KDE Frameworks versions.
- Isolate unstable or version-specific APIs.
- Add validation or tests where practical.
- Run `./scripts/check-structure.sh`.

## Pull requests

Explain the motivation, affected component, test environment and versions, test results, limitations, and visual changes. By contributing, you agree that contributions are provided under the repository MIT license unless otherwise agreed.
