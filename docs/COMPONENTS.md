# Component specifications

This document describes intended behavior; it does not imply that every component is implemented.

## Buttons

Quiet surface at rest; soft accent illumination on hover; persistent visible keyboard focus; brief pressed feedback; no glow when disabled.

## Window decorations

Thin active outline using the selected accent; subdued or neutral inactive outline; recognizable titlebar controls and usable hit targets. Avoid thick neon frames and large exterior bloom.

## Panels and taskbars

Dark, mostly opaque surfaces; clear separation from windows; active application marker or restrained illumination; hover feedback for icons and controls.

## Menus, popups, and tooltips

Elevated dark surface with subtle boundary; short fade; selected items use a quiet accent surface and readable text.

## Inputs and switches

Visible focused-field outline; accent for selected switches; clear slider and checkbox states. Glow must not be the only focus indicator.

## Consistency

Use shared semantic tokens. If an API prevents a visual treatment, document the limitation rather than introducing an inconsistent workaround.
