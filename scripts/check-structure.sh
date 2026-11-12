#!/usr/bin/env sh
set -eu

fail() {
    printf 'FAIL: %s\n' "$1" >&2
    exit 1
}

for file in README.md LICENSE CONTRIBUTING.md SECURITY.md docs/DESIGN.md docs/COLORS.md docs/ROADMAP.md docs/ARCHITECTURE.md plasma/README.md aurorae/README.md aurorae/glow-material/metadata.desktop aurorae/glow-material/glow-materialrc aurorae/glow-material/decoration.svg kwin/README.md qt/README.md; do
    [ -f "$file" ] || fail "Missing required file: $file"
done

for dir in assets packaging scripts; do
    [ -d "$dir" ] || fail "Missing required directory: $dir"
done

printf 'Glow Material repository structure: OK\n'
printf 'Note: this check does not validate KWin runtime behavior.\n'
