# Motion and glow behavior

## State model

| State | Intended appearance |
| --- | --- |
| Rest | No visible glow or a trace of ambient light |
| Hover | Glow fades in around the control or icon |
| Keyboard focus | Clear accent outline and restrained glow |
| Selected | Persistent low-intensity accent treatment |
| Pressed | Brief increase in intensity or surface brightness |
| Disabled | Reduced contrast and no interactive glow |
| Active window | Thin luminous frame or edge treatment |
| Inactive window | Neutral, low-contrast boundary |

## Starting timing targets

These are design targets, not implementation requirements:

- Hover in: 120–180 ms.
- Hover out: 140–200 ms.
- Press feedback: 80–120 ms.
- Window focus transition: 160–220 ms.

Prefer opacity, color, and restrained shadow changes over large movement. Avoid stacking large shadows that create excessive bloom.

## Reduced motion

When reduced motion is enabled, remove non-essential transitions or make them immediate. Never rely on animation to communicate state.
