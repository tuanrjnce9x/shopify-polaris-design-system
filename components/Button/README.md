# Button

Triggers an action or navigation; one primary button per page or section.

**Web component:** `<s-button>` · **Mock-up classes:** `pl-btn` + `pl-btn--primary` | `pl-btn--tertiary` | `pl-btn--critical` | `pl-btn--large` | `pl-btn--icon-only` | `pl-btn--icon-text` | `pl-btn--loading`, `disabled`.

| Prop | Values |
| --- | --- |
| `variant` | `auto` (default, renders secondary), `primary`, `secondary`, `tertiary` |
| `tone` | `auto`, `neutral`, `critical` |
| `icon` | Polaris icon name, e.g. `plus` |
| `loading`, `disabled` | boolean |
| `href`, `target`, `download` | navigation |
| `commandFor` + `command` | open a modal or popover (`--show`, `--hide`, `--toggle`) |
| `accessibilityLabel` | required for icon-only buttons |

```html
<s-button variant="primary">Save</s-button>
<s-button icon="plus">Add product</s-button>
<s-button tone="critical">Delete</s-button>
<s-button variant="tertiary" icon="edit" accessibilityLabel="Edit product"></s-button>
```

- Labels: a strong verb plus noun, sentence case, no articles, no punctuation ("Add tags", not "Add the tags!").
- Primary is `p-color-bg-fill-brand` (#303030) with the white gradient sheen and `p-shadow-button-primary`; secondary is white `p-color-bg-fill` with `p-shadow-button`. Never recolour the primary button with a brand hue.
- Use `tone="critical"` only for destructive actions that are hard to undo.
- Metrics: 28px tall on desktop (`p-height-700`; `p-height-800` large), padding `p-space-150` × `p-space-300`, radius `p-border-radius-200`, label `bodySm` medium (large: `bodyMd`).
