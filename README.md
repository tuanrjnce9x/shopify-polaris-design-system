Polaris is Shopify's design system for the Shopify admin. Apps embedded in the admin use it so they look and behave like the rest of the admin: same type, colours, controls and page structure. This system holds the Polaris light-theme tokens, Polaris icons, and static renditions of the components an embedded app uses, for mock-ups of app screens.

## Which Polaris to build with

- **New embedded apps: Polaris web components** (`<s-page>`, `<s-section>`, `<s-button>` …), loaded by the App Home runtime with App Bridge. They work in any framework or plain HTML and render the admin's current look.
- **Polaris React** (`@shopify/polaris`) is in maintenance. Use it only in an existing React app that already depends on it.
- **App Bridge** owns the admin-drawn UI: title bar, nav menu, contextual save bar (`ui-save-bar` or `<form data-save-bar>`), toasts (`shopify.toast.show`) and resource pickers. Mock them, never restyle them.
- The previews here are hand-built HTML/CSS (`components/bundle.css`, classes prefixed `pl-`) because the official component script cannot load in this page. Treat them as visual references; ship `<s-*>` markup.

## Content and voice

Shopify talks to merchants plainly, like a helpful colleague. Write for someone busy running a store.

- **Sentence case** for every title, label, button and badge: "Shipping and delivery", "Add product". Never Title Case or ALL CAPS.
- **Active verb + noun** for actions: "Save", "Add tags", "Create discount", "Turn on app embed". No articles, no punctuation, no "Click here".
- **"You" for the merchant, "we" for the app** only when needed: "We couldn't connect to your account. Try again in a few minutes."
- **Say what happened, then what to do.** Banners: one message, one next step. Errors: tell them how to fix it ("Enter a valid email address"), not that they failed.
- **Toasts:** noun + past-tense verb, no period: "Settings saved", "Reward deleted".
- **Badges:** 1–2 words, past tense or state: "Fulfilled", "Partially refunded", "Out of stock".
- No emoji, no exclamation marks, no jargon ("SKU" is fine because merchants use it; "webhook failed" is not).
- Numbers and money as merchants see them: "$12,480", "3 of 5", "24 in stock".

## Visual foundations

- **Type.** One family: Inter (`--font-sans`), loaded from Google Fonts as the variable font (weights 450/550/650/700 need it); system UI faces are the fallback. Default copy is `bodyMd` (13px/20px, 450). Page titles `headingLg` at bold; section and modal headings `headingMd` (14px semibold); banner headings `headingSm`. Big numbers on dashboards `heading2xl`. Code and Liquid snippets in `--font-mono`.
- **Colour is neutral first.** Page ground `p-color-bg` (#f1f1f1); cards `p-color-bg-surface` (white); text `p-color-text` (#303030); secondary text `p-color-text-secondary`. The primary action is near-black `p-color-bg-fill-brand` (#303030), not a brand hue: do not paint app chrome in your brand colour.
- **Colour means state.** Info blue, success green, caution yellow, warning orange, critical red, each in a `bg-surface-<tone>` (large areas), `bg-fill-<tone>-secondary` (badges) and `bg-fill-<tone>` (strong fill), with matching `text-<tone>` and `text-<tone>-on-bg-fill`. Always pair a status colour with a word or icon. `emphasis` (blue) is for editors like the theme editor; `magic` (purple) only for AI-suggested content.
- **Links and focus** are blue: `p-color-text-link` (#005bd3) and a 2px `p-color-border-focus` outline offset 1px on every focusable control.
- **Spacing** on a 4px scale: `p-space-400` (16px) card padding and gap between cards, `p-space-200` (8px) inside groups, `p-space-100` (4px) label to field, `p-space-600` (24px) page header.
- **Radius:** `p-border-radius-200` (8px) controls, badges and thumbnails; `p-border-radius-300` (12px) cards and banners; `p-border-radius-400` (16px) modals; `p-border-radius-full` radios, switches, avatars.
- **Depth:** cards are white on grey with `p-shadow-100` plus the inset `p-shadow-bevel-100`; buttons carry their own bevel shadows (`p-shadow-button`, `p-shadow-button-primary`); popovers and toasts `p-shadow-400`; modals `p-shadow-600` over `p-color-backdrop-bg`.
- **Borders** are hairlines: inputs 0.66px `p-color-input-border`; dividers and table rules 1px `p-color-border-secondary`.
- **Motion** is short and functional: controls transition in `motion-duration-100`–`150` (100–150ms) on `motion-ease-out` (cubic-bezier(0.19, 0.91, 0.38, 1)). The page has no motion family, so these stay out of tokens.json; keep mock-ups static.
- **Light theme only.** The tokens package ships a partial `dark-experimental` theme that the admin does not use for apps; it is not included.

## Layout for embedded admin pages

1. **Page** (`s-page`) with a title that names the screen, a breadcrumb back when it is a sub-page, and actions in the header: at most one primary and three secondary. No action buttons at the bottom of the page.
2. **Sections** (`s-section`) stacked in the main column; top-level sections render as cards. Group by task ("Points", "Rewards", "Appearance"), heading in sentence case.
3. **Aside** column (1/3 width, `inlineSize="base"`) for status and summary, never for the main form.
4. **Forms save through the contextual save bar** (`<form data-save-bar>`). Settings that apply instantly use Switch; everything else waits for Save.
5. **Feedback:** a page-level Banner for state that persists (setup incomplete, app embed off), a Toast for "done", an inline field error for validation.
6. **Empty first run:** an Empty state with one primary action, not a blank table.
7. Widths: content up to 62.375rem; `inlineSize="small"` (41.375rem) for single-column settings.

The admin draws the top bar and left navigation around your app. Your page starts at the title on `p-color-bg`. `components/AppHomeExample` shows a full dashboard.

## Iconography

Polaris icons only: 20 × 20 filled glyphs (no strokes), coloured by `p-color-icon` or a tone token. 22 are in `assets/Icons/` (see its README). In web components, name them in kebab-case (`<s-icon type="product">`). Icons go beside labels, not instead of them; icon-only buttons need `accessibilityLabel`. No emoji, no custom icon fonts, no Shopify logo.

## Storefront widgets are not Polaris

Polaris is for the admin only. A theme app extension (app block or app embed) on the merchant's storefront must look like part of their theme:

- `font: inherit; color: inherit;` on the widget root. No Inter, no `--p-*` tokens, no admin shadows or grey cards.
- Minimal styling: spacing and layout only; borders from `currentColor`; take accent colour and radius from block settings the merchant controls (often via a ColorField on the app's settings page).
- Scope class names (`loyalty-widget__title`) and avoid global selectors.
- Text follows the same plain voice, but the merchant can edit it, so expose it as block settings.

`components/StorefrontWidgetExample` shows the pattern.

## Using this system in mock-ups

- Colours, spacing, radii and shadows are CSS custom properties named exactly as in Polaris (`--p-color-bg-surface`, `--p-space-400`, `--p-shadow-100`), so mock-up CSS ports straight to code.
- Load `components/bundle.css` and compose with its `pl-` classes (each component README lists them), or write `<s-*>` markup for handoff.
- Contrast: text tokens state their ratio on `p-color-bg-surface` and `p-color-bg` in their usage note. `p-color-text-disabled` is below 4.5:1 by design; the `*-secondary` tone texts pass on cards but not on the bare page ground.

## Sources and licence

Tokens from `@shopify/polaris-tokens` 9.4.2 (light theme); component metrics from the `@shopify/polaris` 13.9.5 build CSS; icons from `@shopify/polaris-icons` 9.3.1; component APIs and guidance from shopify.dev's Polaris web components and App Bridge docs. © Shopify Inc. under an MIT-style licence that limits use to apps that integrate with Shopify. Embedded admin apps qualify.
