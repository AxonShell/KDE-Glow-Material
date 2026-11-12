# Glow Material

**Glow Material** is an original KDE visual design system developed for **MuliOS**.

Its defining idea is ambient illumination: controls blend into their surfaces at rest, then illuminate during hover, focus, selection, and activation. Windows use rounded silhouettes and luminous edges to communicate focus and depth. Glow Material is not a glassmorphism theme and does not imitate Liquid Glass or Android Material.

> **Design principle:** Light should communicate interaction, not decorate everything.

## Project status

The repository contains the design foundation and an updated rounded-and-glowing Aurorae window-decoration prototype. Static structure checks are being expanded alongside the artwork. It has not yet been validated in a live Plasma session; do not treat it as a finished desktop theme.

## Components

| Component | Responsibility | Status |
| --- | --- | --- |
| Glow Core | Shared design tokens, color roles, glow and motion specifications | Foundation |
| Glow Windows | Aurorae window decoration | Rounded/glow prototype; runtime testing needed |
| Glow Plasma | Plasma panels, widgets, popups, and tooltips | Scaffold |
| Glow Effects | Optional KWin effects and interaction feedback | Planned |
| Glow Controls | Native Qt application styling | Planned |
| MuliOS integration | Defaults, packaging, and installer integration | Planned |

## Rounded Glow Windows prototype

The Aurorae package in aurorae/glow-material provides rounded frame-corner artwork, layered emerald active-edge illumination, neutral inactive edges, and circular titlebar controls with distinct hover and pressed glow states.

See the installation and test instructions in aurorae/glow-material/README.md. Test in a separate Plasma session or use a reversible user-level installation before making it a system default.

The artwork glow is built from translucent vector strokes rather than SVG blur filters. It is not yet a compositor-level bloom, and Aurorae does not guarantee clipping application content to rounded corners. Those require separate KWin compositor work.

## Design direction

Initial MuliOS defaults: deep dark surfaces, MuliOS emerald accent, contextual glow, rounded geometry, minimal transparency, and short transitions. These defaults should remain configurable.

Read docs/DESIGN.md, docs/COLORS.md, docs/MOTION.md, docs/COMPONENTS.md, docs/ARCHITECTURE.md, and docs/ROADMAP.md.

## Repository layout

    assets/       Original artwork and previews
    aurorae/      KWin Aurorae decoration
    docs/         Design and development documentation
    packaging/    MuliOS packaging and integration
    plasma/       Plasma desktop theme
    qt/           Qt style integration
    scripts/      Developer utilities and validation
    kwin/         Optional KWin effects

## Development target

Initial target: KDE Plasma 6 and Qt 6. Minimum supported versions must be documented per component after implementation and testing. Do not assume APIs are available across every Plasma 6 minor release.

Useful references:
- https://develop.kde.org/docs/plasma/
- https://develop.kde.org/docs/plasma/aurorae/
- https://develop.kde.org/

## Validation

Run:

    sh scripts/check-structure.sh
    python3 scripts/check-aurorae.py

These checks validate repository structure, Aurorae metadata, and SVG structure. They do not replace testing in a live Plasma session.

## MuliOS relationship

Glow Material is an independent MuliOS project intended to become the default KDE visual experience for MuliOS. MuliOS should consume versioned Glow Material packages rather than copy files from a development checkout.

## Contributing

See CONTRIBUTING.md. Visual changes should include screenshots and updates to the relevant design documentation.

## License

Glow Material is licensed under the MIT License, unless a file or third-party asset states otherwise. Third-party assets retain their original license and attribution.
