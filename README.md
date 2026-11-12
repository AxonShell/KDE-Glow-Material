# Glow Material

**Glow Material** is an original KDE visual design system developed for **MuliOS**.

Its defining idea is ambient illumination: controls blend into their surfaces at rest, then softly illuminate during hover, focus, selection, and activation. Windows use restrained luminous edges to communicate focus and depth. Glow Material is not a glassmorphism theme and does not imitate Liquid Glass or Android Material.

> **Design principle:** Light should communicate interaction, not decorate everything.

## Project status

This commit establishes the project structure, design foundations, documentation, and packaging direction. It is an early development scaffold, not a finished or fully installable theme. Individual components will be marked as experimental or implemented as they become usable.

## Planned components

| Component | Responsibility | Status |
| --- | --- | --- |
| Glow Core | Shared design tokens, color roles, glow and motion specifications | Foundation |
| Glow Plasma | Plasma panels, widgets, popups, and tooltips | Scaffold |
| Glow Windows | Aurorae window decoration | Scaffold |
| Glow Effects | Optional KWin effects and interaction feedback | Planned |
| Glow Controls | Native Qt application styling | Planned |
| MuliOS integration | Defaults, packaging, and installer integration | Planned |

## Design direction

Initial MuliOS defaults: deep dark surfaces, MuliOS emerald accent, restrained contextual glow, minimal transparency, and short transitions. These defaults should remain configurable.

Read [Design](docs/DESIGN.md), [Colors](docs/COLORS.md), [Motion](docs/MOTION.md), [Components](docs/COMPONENTS.md), [Architecture](docs/ARCHITECTURE.md), and the [Roadmap](docs/ROADMAP.md).

## Repository layout

```text
assets/       Original artwork and previews
aurorae/      KWin Aurorae decoration
docs/         Design and development documentation
packaging/    MuliOS packaging and integration
plasma/       Plasma desktop theme
qt/           Qt style integration
scripts/      Developer utilities
kwin/         Optional KWin effects
```

## Development target

Initial target: KDE Plasma 6 and Qt 6. Minimum supported versions must be documented per component after implementation and testing. Do not assume APIs are available across every Plasma 6 minor release.

Useful references:
- https://develop.kde.org/docs/plasma/
- https://develop.kde.org/docs/plasma/theme/
- https://develop.kde.org/

## Validation

Run `./scripts/check-structure.sh`. This checks repository metadata and structure only; it does not validate a theme in a live Plasma session.

## MuliOS relationship

Glow Material is an independent MuliOS project intended to become the default KDE visual experience for MuliOS. MuliOS should consume versioned Glow Material packages rather than copy files from a development checkout.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Visual changes should include screenshots and updates to the relevant design documentation.

## License

Glow Material is licensed under the [MIT License](LICENSE), unless a file or third-party asset states otherwise. Third-party assets retain their original license and attribution.
