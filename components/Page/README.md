# Page

The frame of every app screen: title, breadcrumb, actions, then sections.

**Web component:** `<s-page heading="…" inlineSize="base">` · **Mock-up classes:** `pl-page` (`--small`, `--large`), `pl-page__header`, `pl-page__title`, `pl-page__layout` (2:1 main and aside).

| Prop / slot | Values |
| --- | --- |
| `heading` | page title |
| `inlineSize` | `small`, `base` (default), `large` |
| `primary-action` slot | one `variant="primary"` button |
| `secondary-actions` slot | up to 3 buttons |
| `breadcrumb-actions` slot | `s-link` back to the parent page |
| `aside` slot | side column (only with `base`) |
| `supplemental-start` slot | banners above the content |

```html
<s-page heading="Loyalty settings">
  <s-link slot="breadcrumb-actions" href="/app">Dashboard</s-link>
  <s-button slot="primary-action" variant="primary">Save</s-button>
  <s-button slot="secondary-actions">Preview</s-button>
  <s-section heading="Points">…</s-section>
</s-page>
```

- Always a title that names the screen. No more than one primary and three secondary actions; never put actions at the bottom of the page.
- In an embedded app the admin draws the outer chrome (top bar, left nav, app title bar). Your page starts at the title on `p-color-bg`.
- Title `headingLg` bold; header padding `p-space-600` on desktop; content max width 62.375rem (41.375rem primary + 20rem aside + 1rem gap); `small` is 41.375rem.
