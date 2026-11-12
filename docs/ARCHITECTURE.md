# Architecture

Glow Material is split by KDE extension point to avoid coupling the design system to one monolithic theme or compositor plugin.

## Glow Core

Semantic colors, spacing, radii, outline roles, glow roles, motion targets, and accessibility rules. Documentation and token definitions are the source of truth.

## Plasma desktop theme

Path: `plasma/desktoptheme/glow-material/`. Owns Plasma theme metadata and assets for panels, widgets, dialogs, tooltips, and shell surfaces. It does not automatically style every Qt application.

## Aurorae window decoration

Path: `aurorae/`. Owns titlebars, window buttons, and decoration frame assets where Aurorae is suitable. Validate metadata, scaling, and active/inactive states on the target KWin release.

## KWin effects

Path: `kwin/`. Reserved for optional compositor effects that cannot be expressed by a theme or decoration. Prefer supported APIs; document minimum versions and keep effects disableable.

## Qt integration

Path: `qt/`. Qt Widgets and Qt Quick need different integration strategies. A Qt Widgets style does not automatically theme every Qt Quick application.

## MuliOS packaging

Path: `packaging/`. Install into standard KDE locations, provide clean upgrade/uninstall behavior, and avoid overwriting user configuration. MuliOS should consume versioned packages.

## Compatibility

Initial target: KDE Plasma 6 and Qt 6. Exact minimum versions must be documented per component after implementation and testing.

## Runtime boundaries

- The desktop theme must remain usable without a custom KWin effect.
- Optional effects must fail safely when unavailable.
- The base theme must remain legible with blur, transparency, and animation disabled.
- Components share semantic tokens but remain independently installable.
