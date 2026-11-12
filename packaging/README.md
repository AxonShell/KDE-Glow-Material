# Packaging

MuliOS is the first packaging target.

Requirements:
- Install components into standard KDE package locations.
- Keep Plasma, Aurorae, KWin, and Qt components independently packageable.
- Provide clean upgrade and uninstall behavior.
- Avoid overwriting user configuration.
- Record build and runtime dependencies.
- Declare supported Plasma, Qt, and KDE Frameworks versions.
- Package only implemented components; do not ship scaffolds as working plugins.

Choose package naming and versioning when the first installable component is ready.
