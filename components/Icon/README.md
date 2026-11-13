# Icon

Polaris icons: 20 × 20 filled SVGs, drawn in the text or icon colour.

**Web component:** `<s-icon type="product">` (names are kebab-case: `alert-circle`, `check-circle`) · **Mock-up:** inline the SVG from `assets/Icons/` inside `<span class="pl-icon">`, which fills it with `p-color-icon`; `pl-icon--secondary|success|info|caution|warning|critical` switch the tone.

- Icons support a label; they never replace one, except icon-only buttons with `accessibilityLabel`.
- Use the admin's own icon for admin concepts (orders, products, apps).
- Only Polaris icons are available to the web component; do not draw custom marks.
