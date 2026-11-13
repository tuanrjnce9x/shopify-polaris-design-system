# StorefrontWidgetExample

A storefront theme app extension widget that inherits the merchant's theme instead of using Polaris.

- `font: inherit; color: inherit;` on the root; borders from `currentColor`; buttons take the theme's accent and radius when available.
- No `--p-*` tokens, no Inter, no admin shadows. Scope every class name (`loyalty-widget__…`) so it cannot clash with theme CSS.
- The serif "theme" around it is a stand-in to show inheritance, not a value to copy.
