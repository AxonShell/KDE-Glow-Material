# Color system

Components should consume semantic roles rather than independently hard-code accent colors.

## Initial palette

| Role | Value | Purpose |
| --- | --- | --- |
| Background | `#101312` | Desktop canvas |
| Surface | `#171C19` | Main application surfaces |
| Surface elevated | `#202723` | Menus and popups |
| Surface muted | `#141916` | Quiet controls |
| Text primary | `#E8F0EB` | Main text |
| Text secondary | `#A8B5AD` | Secondary text |
| Outline | `#35433A` | Subtle boundaries |
| Accent | `#48C780` | MuliOS emerald |
| Accent bright | `#78E5A5` | Highlight accent |
| Accent dim | `#205A3A` | Low-energy selected surfaces |
| Focus | `#78E5A5` | Keyboard focus |

## Glow roles

- `glow-rest`: absent or barely perceptible.
- `glow-hover`: soft, low-opacity halo.
- `glow-focus`: clear focus outline plus restrained glow.
- `glow-active`: restrained active-window or selected-state halo.
- `glow-pressed`: brief stronger feedback, never persistent bloom.

Glow derives from the selected accent. Support alternate user accents, including blue, violet, and neutral. Verify contrast and visibility for all derived colors. Color must never be the only state indicator.
