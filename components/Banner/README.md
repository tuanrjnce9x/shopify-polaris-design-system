# Banner

A prominent message about the page or a section: info, success, warning or critical.

**Web component:** `<s-banner tone="warning" heading="…">` · **Mock-up classes:** page level `pl-banner pl-banner--<tone>` with `pl-banner__head` / `pl-banner__body`; inside a section `pl-inline-banner pl-inline-banner--<tone>`.

| Prop / slot | Values |
| --- | --- |
| `tone` | `auto`, `info`, `success`, `warning`, `critical` |
| `heading` | short title |
| `dismissible`, `hidden` | boolean |
| `secondary-actions` slot | up to two buttons |

```html
<s-banner heading="127 products missing shipping weights" tone="warning">
  Products without weights may show inaccurate shipping rates.
  <s-button slot="secondary-actions" variant="secondary">Review products</s-button>
</s-banner>
```

- One message, one next step. Make it dismissible unless the merchant must act.
- Page-wide banners go outside sections (top of the page); contextual ones inside the section they refer to.
- Page level: header strip in `p-color-bg-fill-<tone>` with `p-color-text-<tone>-on-bg-fill`, heading `headingSm`, padding `p-space-300`; body on `p-color-bg-surface`; `p-shadow-200`, radius `p-border-radius-300`. Within a section: `p-color-bg-surface-<tone>`, radius `p-border-radius-200`.
