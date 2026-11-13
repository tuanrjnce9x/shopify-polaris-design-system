# SaveBar

The contextual save bar the admin shows while a form has unsaved changes.

**App Bridge:** `<form data-save-bar>` (automatic) or `<ui-save-bar id="…">` with `<button variant="primary">Save</button><button>Discard</button>` and `shopify.saveBar.show(id)` / `hide(id)` · **Mock-up classes:** `pl-savebar`.

- Every settings form with a save action uses it; do not add your own Save button at the bottom of the page.
- Use one mechanism per form: `data-save-bar` or `ui-save-bar`, never both.
- The admin draws it over its top bar; your app does not style it. This rendition follows Polaris React's ContextualSaveBar: 56px, `p-color-bg-inverse`, `headingMd` "Unsaved changes" in `p-color-text-inverse`, a tertiary Discard and a success-tone primary Save. The current admin may differ in detail.
