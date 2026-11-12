#!/usr/bin/env python3
"""Static validation for the Glow Material Aurorae package."""
from pathlib import Path
import configparser
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "aurorae" / "glow-material"
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

for name in ("metadata.desktop", "glow-materialrc", "decoration.svg",
             "close.svg", "minimize.svg", "maximize.svg", "restore.svg"):
    require((THEME / name).is_file(), f"Missing Aurorae file: {name}")

if (THEME / "metadata.desktop").exists():
    metadata = configparser.ConfigParser(interpolation=None, strict=False)
    metadata.read(THEME / "metadata.desktop", encoding="utf-8")
    require(metadata.has_section("Desktop Entry"), "metadata.desktop needs [Desktop Entry]")
    if metadata.has_section("Desktop Entry"):
        require(metadata.get("Desktop Entry", "X-KDE-PluginInfo-Name", fallback="") == "glow-material",
                "Aurorae plugin ID must match folder name (glow-material)")
        require(metadata.get("Desktop Entry", "X-KDE-PluginInfo-Version", fallback="") == "0.1.0",
                "Unexpected Aurorae version")

for svg_path in THEME.glob("*.svg"):
    try:
        root = ET.parse(svg_path).getroot()
        ids = {node.attrib.get("id") for node in root.iter() if node.attrib.get("id")}
        if svg_path.name == "decoration.svg":
            for state in ("decoration", "decoration-inactive"):
                for part in ("top", "left", "right", "bottom", "topleft",
                             "topright", "bottomleft", "bottomright", "center"):
                    require(f"{state}-{part}" in ids,
                            f"{svg_path.name}: missing SVG element ID {state}-{part}")
            source = svg_path.read_text(encoding="utf-8")
            require("A14 14" in source, "Window corners must use rounded 14px arcs")
            require('stroke-width="9"' in source and 'opacity=".10"' in source,
                    "Active frame should include a layered outer glow stroke")
        else:
            require("active-center" in ids,
                    f"{svg_path.name}: missing active-center button element")
            for state in ("inactive", "hover", "hover-inactive", "pressed",
                          "pressed-inactive", "deactivated", "deactivated-inactive"):
                require(f"{state}-center" in ids,
                        f"{svg_path.name}: missing {state}-center button element")
            source = svg_path.read_text(encoding="utf-8")
            require('r="10"' in source, f"{svg_path.name}: expected circular button body")
            require('r="16"' in source, f"{svg_path.name}: expected outer hover glow ring")
    except ET.ParseError as exc:
        errors.append(f"Invalid XML in {svg_path.name}: {exc}")

rc_path = THEME / "glow-materialrc"
if rc_path.exists():
    rc = configparser.ConfigParser(interpolation=None, strict=False)
    rc.read(rc_path, encoding="utf-8")
    require(rc.has_section("General"), "glow-materialrc needs [General]")
    require(rc.has_section("Layout"), "glow-materialrc needs [Layout]")
    if rc.has_section("General"):
        require(rc.get("General", "RightButtons", fallback="") == "IAX",
                "Expected minimize/maximize/close button order IAX")
        require(rc.getboolean("General", "HaloActive", fallback=False),
                "Active halo should be enabled")
    if rc.has_section("Layout"):
        require(rc.getint("Layout", "TitleHeight", fallback=0) > 0,
                "TitleHeight must be positive")
        require(rc.getint("Layout", "BorderLeft", fallback=0) >= 8,
                "Rounded glow frame needs room for its left edge treatment")
        require(rc.getint("Layout", "ButtonWidth", fallback=0) >= 28,
                "Circular titlebar buttons need a usable width")

if errors:
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    sys.exit(1)

print("Glow Material rounded/glow Aurorae package: static checks passed.")
print("This does not replace testing in a live KDE Plasma session.")
