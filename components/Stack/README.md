# Stack

Box, Stack and Grid lay out content with Polaris spacing; Divider separates groups.

**Web components:** `<s-stack direction="inline|block" gap="base">`, `<s-box padding="base">`, `<s-grid>`, `<s-divider>` · **Mock-up classes:** `pl-row`, `pl-col`, `pl-col-tight`, `pl-spread`, `pl-divider`.

- Stack props: `direction` (`block` default, `inline`), `gap`, `padding`, `justifyContent`, `alignItems`; responsive values allowed.
- Spacing keywords: `small-500` … `small-100`, `small`, `base`, `large`, `large-100` … `large-500`, `none`. Their pixel mapping is not published in the tokens package; in mock-ups use `p-space-200` for tight groups and `p-space-400` between blocks.
- Divider: 1px (`p-border-width-025`) in `p-color-border-secondary`.
- Tight spacing means related; generous spacing separates groups.
