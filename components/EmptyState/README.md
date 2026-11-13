# EmptyState

Explains why a page, list or table is empty and what to do next.

**Web component:** `<s-empty-state heading="…">` with slots `graphic`, `subheading`, `primary-action`, `secondary-actions` · **Mock-up classes:** `pl-empty`, `pl-empty__graphic`, `pl-empty__text`.

```html
<s-empty-state heading="Add your first product">
  <s-icon slot="graphic" type="product"></s-icon>
  <s-text slot="subheading">Products you add here are ready to sell across your sales channels.</s-text>
  <s-button slot="primary-action" variant="primary">Add product</s-button>
</s-empty-state>
```

- Say why it is empty, then what to do. One primary action.
- Inside a table it shows and hides itself with the rows.
- Rendition: heading `headingMd`, text `bodyMd` in `p-color-text-secondary`, paddings from Polaris React EmptyState. The round icon graphic is a stand-in composition, not a measured web component value.
