# Component specifications

This document describes intended behavior; it does not imply that every component is implemented.

## Buttons

Circular hit-area artwork with a quiet emerald outline at rest. Hover and keyboard focus use layered accent rings; pressed state brightens the inner disc and outer halo. The close control uses a red danger accent. Disabled controls remain legible without glow. Focus must remain visible without relying on color alone.

## Window decorations

Rounded corners on all four sides, including the lower corners. Active windows use a layered emerald edge with a visible but controlled halo; inactive windows retain the same rounded silhouette with a subdued neutral outline. Titlebar controls are circular and share the button glow language. Maximized-window geometry must avoid gaps at screen edges.

The Aurorae SVG glow is composed of translucent vector strokes instead of SVG filter blur, improving compatibility with Qt SVG renderers. This creates a luminous edge treatment inside the decoration artwork; it is not a compositor-level bloom or a guarantee that application content is clipped to rounded corners. True content clipping requires KWin compositor support and must be tested separately.

## Panels and taskbars

Dark, mostly opaque surfaces; clear separation from windows; active application marker or restrained illumination; hover feedback for icons and controls.

## Menus, popups, and tooltips

Elevated dark surface with subtle boundary; short fade; selected items use a quiet accent surface and readable text.

## Inputs and switches

Visible focused-field outline; accent for selected switches; clear slider and checkbox states. Glow must not be the only focus indicator.

## Consistency

Use shared semantic tokens. If an API prevents a visual treatment, document the limitation rather than introducing an inconsistent workaround.
