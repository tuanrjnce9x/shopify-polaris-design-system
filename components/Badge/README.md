# Badge

A one- or two-word, system-generated status beside the thing it describes.

**Web component:** `<s-badge tone="success">Active</s-badge>` · **Mock-up classes:** `pl-badge` + `pl-badge--info|success|caution|warning|critical`, `pl-badge--strong`, `pl-badge--large`.

| Prop | Values |
| --- | --- |
| `tone` | `auto`, `neutral`, `info`, `success`, `caution`, `warning`, `critical` |
| `color` | `base` (tinted), `strong` (solid fill) |
| `size` | `base`, `large`, `large-100` |
| `icon` | Polaris icon name |

- Past tense or state nouns: "Fulfilled", "Refunded", "Out of stock".
- `base` size in tables and lists; `large` for a lone status.
- Never use badges for merchant-created tags or removable items (use a chip).
- Tinted tones pair `p-color-bg-fill-<tone>-secondary` with `p-color-text-<tone>`; strong pairs `p-color-bg-fill-<tone>` with `p-color-text-<tone>-on-bg-fill`. Text `bodySm`, padding `p-space-050` × `p-space-200`, radius `p-border-radius-200`.
