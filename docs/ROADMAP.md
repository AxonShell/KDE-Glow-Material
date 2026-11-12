# Roadmap

Items are complete only when implemented, installed, and tested on a documented target environment.

## 0.1 — Project foundation

- [x] Establish repository structure and project metadata.
- [x] Define design principles, colors, and motion roles.
- [x] Add contribution, security, and licensing documents.
- [x] Create initial Aurorae SVG package scaffold.
- [ ] Validate Aurorae metadata and SVG rendering in a live Plasma 6 session.
- [ ] Capture first visual prototype screenshots.

## 0.2 — Rounded luminous window prototype

- [x] Add rounded SVG corner geometry for active and inactive frames.
- [x] Add layered active-edge illumination without SVG filter dependencies.
- [x] Redraw minimize, maximize, restore, and close controls as circular glowing buttons.
- [x] Add distinct hover, pressed, inactive, and disabled artwork states.
- [ ] Validate actual corner radii and glow rendering in a live Plasma 6 session.
- [ ] Verify scaling, maximized, tiled, and borderless windows.
- [ ] Confirm whether KWin clips application content to rounded corners.

## 0.3 — Compositor and interaction polish

- [ ] Prototype true compositor-level window bloom and rounded content clipping in a KWin effect.
- [ ] Add configurable accent and glow intensity.
- [ ] Validate keyboard navigation and reduced motion.
- [ ] Test with compositor effects disabled.

## 0.4 — Application consistency

- [ ] Implement Plasma desktop theme assets.
- [ ] Test panels, popups, tooltips, and widgets.
- [ ] Evaluate Qt Widgets and Qt Quick integration separately.
- [ ] Document unsupported application surfaces.

## 0.5 — MuliOS integration

- [ ] Produce versioned packages.
- [ ] Add MuliOS build/package integration.
- [ ] Add default configuration for new installations.
- [ ] Test upgrade, rollback, and uninstall.

## 1.0 — Stable

- [ ] Publish compatibility matrix.
- [ ] Complete accessibility and performance reviews.
