# Section

Groups related content; a top-level section renders as a card.

**Web component:** `<s-section heading="…">` · **Mock-up classes:** `pl-card` (`--flush` for tables and images), `pl-card__head`.

| Prop / slot | Values |
| --- | --- |
| `heading`, `subheading` | title; supporting line |
| `padding` | `base`, `none` (edge-to-edge tables, images) |
| `accessory` / `supplemental` slots | badge or button by the heading; section status |
| `primary-action`, `secondary-actions` slots | section actions |

- Nesting raises heading levels (h2 → h3 → h4); nested sections draw no card. Stop at 2–3 levels.
- Card: `p-color-bg-surface`, radius `p-border-radius-300`, `p-shadow-100` plus `p-shadow-bevel-100`, padding `p-space-400`, `p-space-400` between cards. Heading `headingMd`.
- No collapse/expand built in.
