# Glow Material — Aurorae window decoration

## Appearance

The rounded-glow prototype introduces:

- Dark charcoal titlebar and frame (#171C19).
- Rounded corner artwork on all four corners, including the lower corners.
- Layered emerald edge illumination for active windows.
- A subdued neutral outline for inactive windows.
- Circular minimize, maximize, restore, and close controls.
- Layered glow rings for hover and pressed states; close uses a red danger glow.
- Translucent vector strokes instead of SVG blur filters for wider renderer compatibility.

## Package contents

- metadata.desktop: Aurorae theme metadata.
- glow-materialrc: titlebar, border, halo, shadow, and button layout.
- decoration.svg: active and inactive rounded frame assets.
- close.svg, minimize.svg, maximize.svg, restore.svg: circular button artwork and interaction states.

## Install for the current user

From the repository root:

    mkdir -p ~/.local/share/aurorae/themes
    cp -a aurorae/glow-material ~/.local/share/aurorae/themes/

Then open System Settings → Colors & Themes → Window Decorations, select Glow Material, and apply it. The exact category label can vary slightly by Plasma release.

To remove it:

    rm -rf ~/.local/share/aurorae/themes/glow-material

Do not use sudo for a per-user installation.

## Test checklist

- [ ] Theme appears in the Window Decorations selector.
- [ ] All four corners are visibly rounded on normal windows.
- [ ] Active frame has a visible emerald edge glow.
- [ ] Inactive frame keeps the same rounded silhouette with a neutral outline.
- [ ] All three titlebar controls are circular.
- [ ] Hover and pressed button glows render; close uses the danger accent.
- [ ] Buttons remain readable and usable at 100%, 125%, 150%, and 200%.
- [ ] Long titles do not overlap the controls.
- [ ] Maximized and tiled windows do not show unwanted gaps.
- [ ] Wayland and X11 behavior checked where supported.
- [ ] No SVG parsing or KWin decoration errors in the journal.

## Current limitations

This is an Aurorae artwork prototype, not a complete desktop theme. Its glow is made from layered translucent strokes within the decoration artwork; it is not a compositor-level bloom extending arbitrarily beyond the decoration. Aurorae artwork also cannot guarantee clipping of application content to rounded corners. True content clipping and external window bloom require KWin compositor support and are tracked separately. The SVG slicing, corner geometry, shadow, and maximized-window behavior must be verified on the target Plasma/KWin version.

## License

MIT. See the repository root LICENSE.
