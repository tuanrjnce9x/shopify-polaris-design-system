B='/private/tmp/claude-501/-Users-will-second-brain/56790265-d246-44e6-a02d-a0051c52481d/scratchpad/polaris-ds/project/components/'
R={}
R['Button']='''Triggers an action or navigation; one primary button per page or section.

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
'''
R['Link']='''Inline navigation inside text; use Button for actions.

**Web component:** `<s-link href="…">` · **Mock-up classes:** `pl-link`, `pl-link--monochrome`.

- Colour `p-color-text-link` (#005bd3), underlined, hover `p-color-text-link-hover`.
- Use the monochrome variant inside banners and help text so the link takes the surrounding colour.
- Link text says where it goes ("order status page"), never "click here".
'''
R['Badge']='''A one- or two-word, system-generated status beside the thing it describes.

**Web component:** `<s-badge tone="success">Active</s-badge>` · **Mock-up classes:** `pl-badge` + `pl-badge--info|success|caution|warning|critical`, `pl-badge--strong`, `pl-badge--large`.

| Prop | Values |
| --- | --- |
| `tone` | `auto`, `neutral`, `info`, `success`, `caution`, `warning`, `critical` |
| `color` | `base` (tinted), `strong` (solid fill) |
| `size` | `base`, `large`, `large-100` |
| `icon` | Polaris icon name |

- Past tense or state nouns: "Fulfilled", "Refunded", "Out of stock".
- `base` size in tables and lists; `large` for a lone status.
- Never use badges for merchant-created tags or removable items (use a chip).
- Tinted tones pair `p-color-bg-fill-<tone>-secondary` with `p-color-text-<tone>`; strong pairs `p-color-bg-fill-<tone>` with `p-color-text-<tone>-on-bg-fill`. Text `bodySm`, padding `p-space-050` × `p-space-200`, radius `p-border-radius-200`.
'''
R['Banner']='''A prominent message about the page or a section: info, success, warning or critical.

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
'''
R['Progress']='''A horizontal bar showing how far a task has advanced.

**Web component:** `<s-progress value="3" max="5" accessibilityLabel="Importing products">` · **Mock-up classes:** `pl-progress` (+ `--small`, `--primary`, `--success`, `--critical`) with a `pl-progress__bar` set by width.

- Props: `value`, `max` (default 1), `tone` (`auto`, `neutral`, `info`, `success`, `caution`, `warning`, `critical`), `accessibilityLabel`.
- The bar shows no numbers: put "3 of 5" in text beside it. Unknown duration: use a spinner instead.
- Rendition from Polaris React ProgressBar: track `p-color-bg-fill-tertiary`, default fill `p-color-bg-fill-info`, 16px tall (8px small), radius `p-border-radius-100`. The web component's exact height and default tone colour were not verified.
'''
R['EmptyState']='''Explains why a page, list or table is empty and what to do next.

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
'''
R['Page']='''The frame of every app screen: title, breadcrumb, actions, then sections.

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
'''
R['Section']='''Groups related content; a top-level section renders as a card.

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
'''
R['Stack']='''Box, Stack and Grid lay out content with Polaris spacing; Divider separates groups.

**Web components:** `<s-stack direction="inline|block" gap="base">`, `<s-box padding="base">`, `<s-grid>`, `<s-divider>` · **Mock-up classes:** `pl-row`, `pl-col`, `pl-col-tight`, `pl-spread`, `pl-divider`.

- Stack props: `direction` (`block` default, `inline`), `gap`, `padding`, `justifyContent`, `alignItems`; responsive values allowed.
- Spacing keywords: `small-500` … `small-100`, `small`, `base`, `large`, `large-100` … `large-500`, `none`. Their pixel mapping is not published in the tokens package; in mock-ups use `p-space-200` for tight groups and `p-space-400` between blocks.
- Divider: 1px (`p-border-width-025`) in `p-color-border-secondary`.
- Tight spacing means related; generous spacing separates groups.
'''
R['Table']='''Rows of resources with columns; becomes a stacked list on small screens.

**Web components:** `<s-table>` › `<s-table-header-row>` › `<s-table-header>`, `<s-table-body>` › `<s-table-row>` › `<s-table-cell>` · **Mock-up classes:** `pl-table` inside `pl-card pl-card--flush`, `pl-num` for numbers, `pl-table__footer`, `pl-tabs` / `pl-tab` for index views.

- `s-table`: `variant` (`auto`, `list`), `paginate`, `loading`, `hasNextPage`, `hasPreviousPage`; `filters` slot for search and filter controls.
- `s-table-header`: `format` (`base`, `numeric`, `currency`) right-aligns numbers; `listSlot` (`primary`, `secondary`, `kicker`, `inline`, `labeled`) decides the mobile layout.
- Headers must still read as key–value pairs when stacked. Paginate beyond ~50 rows.
- Rendition from Polaris IndexTable: header `p-color-bg-surface-secondary`, 12px medium `p-color-text-secondary`; rows on `p-color-bg-surface` with a `p-color-border-secondary` top rule, hover `p-color-bg-surface-hover`. Tabs above the table are the admin index-filter pattern (no web component).
'''
R['TextField']='''Single-line text input with a label, help text and inline error.

**Web component:** `<s-text-field label="…">` (siblings: `s-email-field`, `s-number-field`, `s-money-field`, `s-password-field`, `s-search-field`, `s-url-field`, `s-text-area`) · **Mock-up classes:** `pl-field`, `pl-label` (`--required`), `pl-input` (`--focus`, `--error`, `--disabled`), `pl-input__prefix|suffix`, `pl-help`, `pl-error`.

- Props: `label`, `value`, `placeholder`, `details` (help text), `error`, `prefix`, `suffix`, `icon`, `required`, `disabled`, `readOnly`, `maxLength`, `minLength`, `autocomplete`, `labelAccessibilityVisibility` (`visible`, `exclusive`); `accessory` slot.
- Always a visible label; put formats in `details`, units in `suffix`.
- Errors say how to fix it ("Enter a valid email address").
- Input: `p-color-input-bg-surface`, 0.66px `p-color-input-border` (top edge #898f94, a literal in the Polaris source), radius `p-border-radius-200`, 32px tall, `bodyMd`. Focus: `p-color-input-border-active` plus a 2px `p-color-border-focus` outline offset 1px. Error: `p-color-bg-surface-critical` and `p-color-border-critical-secondary`.
'''
R['Select']='''Choose one option from four or more in a dropdown.

**Web component:** `<s-select label="…">` with `<s-option value="…">` and `<s-option-group label="…">` · **Mock-up classes:** `pl-field pl-select`, `pl-input`, `pl-input__value`.

- Props: `label`, `value`, `placeholder`, `details`, `error`, `disabled`, `required`, `icon`.
- Fewer than four options: use ChoiceList. Multiple selection: ChoiceList with `multiple`.
- Pre-select the sensible default. Options are plain text, no search.
- Same field frame as TextField; the Select icon is `p-color-icon-secondary`.
'''
R['Checkbox']='''An on/off choice that takes effect when the form is saved.

**Web component:** `<s-checkbox label="…" checked>` · **Mock-up classes:** `pl-choice`, `pl-choice__control`, `pl-checkbox` (`--checked`), `pl-choice--disabled`, `pl-choice__help`.

- Props: `label`, `details`, `checked`, `indeterminate`, `disabled`, `error`, `name`, `value`.
- Use with a save action; for settings that apply instantly use Switch.
- 18px control (20px on mobile), radius `p-border-radius-100`, 0.66px `p-color-input-border`; checked fill `p-color-bg-fill-brand-selected` with a white check (`p-color-text-brand-on-bg-fill`); label `bodyMd`, `p-space-200` gap.
'''
R['Switch']='''A toggle for settings that apply immediately, without a save button.

**Web component:** `<s-switch label="Enable notifications" checked>` · **Mock-up classes:** `pl-switch` (`--on`) inside `pl-choice`.

- Props: `label`, `details`, `checked`, `disabled`, `error`.
- Never inside a form with a save bar: the merchant cannot tell when the change applies. Use Checkbox there.
- Rendition only: Polaris React has no switch, and the web component's exact metrics were not available. The track (32 × 20px, `p-border-radius-full`, off `p-color-bg-fill-tertiary`, on `p-color-bg-fill-brand`) and white knob are composed from tokens; check them against a live admin before you treat them as exact.
'''
R['ChoiceList']='''A labelled group of radio buttons, or checkboxes with `multiple`.

**Web component:** `<s-choice-list label="…">` with `<s-choice value="…">` · **Mock-up classes:** `pl-choice-list`, `pl-choice`, `pl-radio` (`--checked`) or `pl-checkbox`.

- Props: `label`, `name`, `multiple`, `details`, `error`, `disabled`, `values`; on `s-choice`: `value`, `selected`, `defaultSelected`, `disabled`.
- Labels describe the outcome ("Free shipping"), not the mechanism.
- More than ~20 options: use Select.
- Radio: 18px circle, 0.66px `p-color-input-border`; selected fills `p-color-bg-fill-brand-selected` with an 8px `p-color-text-brand-on-bg-fill` dot.
'''
R['ColorField']='''A colour input that takes hex text or opens a picker.

**Web component:** `<s-color-field label="Button background color" value="#005BD3">` (palette-only: `<s-color-picker>`) · **Mock-up classes:** `pl-field`, `pl-input`, `pl-swatch`.

- Props: `label`, `value` (hex, rgb or rgba; output is always hex), `alpha`, `placeholder`, `details`, `error`, `required`.
- Name what the colour is for ("Button background color"), not just "Color".
- Typical use: styling your storefront widget from the app's settings page.
'''
R['Modal']='''An overlay for a focused task or a confirmation; opened only by a merchant action.

**Web component:** `<s-modal id="…" heading="…">`, opened with `<s-button commandFor="id" command="--show">` · **Mock-up classes:** `pl-backdrop`, `pl-modal` (`--small`), `pl-modal__head|body|foot`.

| Prop / slot | Values |
| --- | --- |
| `heading` | the question or task |
| `size` | `small-100`, `small`, `base`, `large`, `large-100` |
| `padding` | `base`, `none` |
| `primary-action` slot | one primary button |
| `secondary-actions` slot | Cancel and others |

- Cannot open on page load. Confirmations name the consequence; the confirm button repeats the verb ("Delete reward").
- Header `p-color-bg-surface-tertiary` with `headingMd` and a `p-color-border` rule; padding `p-space-400`; radius `p-border-radius-400`; `p-shadow-600`; backdrop `p-color-backdrop-bg`. 620px wide (base).
'''
R['SaveBar']='''The contextual save bar the admin shows while a form has unsaved changes.

**App Bridge:** `<form data-save-bar>` (automatic) or `<ui-save-bar id="…">` with `<button variant="primary">Save</button><button>Discard</button>` and `shopify.saveBar.show(id)` / `hide(id)` · **Mock-up classes:** `pl-savebar`.

- Every settings form with a save action uses it; do not add your own Save button at the bottom of the page.
- Use one mechanism per form: `data-save-bar` or `ui-save-bar`, never both.
- The admin draws it over its top bar; your app does not style it. This rendition follows Polaris React's ContextualSaveBar: 56px, `p-color-bg-inverse`, `headingMd` "Unsaved changes" in `p-color-text-inverse`, a tertiary Discard and a success-tone primary Save. The current admin may differ in detail.
'''
R['Toast']='''A short, non-blocking confirmation after an action.

**App Bridge:** `shopify.toast.show('Settings saved', { duration, isError, action, onAction })` · **Mock-up classes:** `pl-toast` (`--error`), `pl-toast__action`.

- Message: noun + past-tense verb, sentence case, no period ("Product saved", "Discount deleted").
- Errors that need action belong in a banner or inline error, not a toast.
- One action at most ("Undo", "Retry").
- The admin renders it at the bottom of the screen: `p-color-bg-inverse`, `p-color-text-inverse`, radius `p-border-radius-200`, `p-shadow-400`, padding `p-space-300`; error uses `p-color-bg-fill-critical`.
'''
R['Icon']='''Polaris icons: 20 × 20 single-path SVGs, drawn in the text or icon colour.

**Web component:** `<s-icon type="product">` (names are kebab-case: `alert-circle`, `check-circle`) · **Mock-up:** inline the SVG from `assets/Icons/` inside `<span class="pl-icon">`, which fills it with `p-color-icon`; `pl-icon--secondary|success|info|caution|warning|critical` switch the tone.

- Icons support a label; they never replace one, except icon-only buttons with `accessibilityLabel`.
- Use the admin's own icon for admin concepts (orders, products, apps).
- Only Polaris icons are available to the web component; do not draw custom marks.
'''
R['Thumbnail']='''A small square preview of a product, image or file.

**Web component:** `<s-thumbnail src="…" alt="…" size="small">` · **Mock-up classes:** `pl-thumb` (`--xs` 24px, default 40px, `--md` 60px, `--lg` 80px).

- Always set `alt` to what the image shows; use the Image icon as a placeholder when there is no image.
- `p-color-bg-surface`, radius `p-border-radius-200` (`p-border-radius-150` at 24px), 1px inner border `p-shadow-border-inset`.
'''
R['Text']='''Headings and body copy set in the Polaris text variants.

**Web components:** `<s-heading>`, `<s-text>`, `<s-paragraph>` (`tone`, `type="strong"` etc.) · **Mock-up classes:** `pl-heading-3xl … pl-heading-xs`, `pl-body-lg … pl-body-xs`, `pl-subdued`, `pl-bold`, `pl-mono`.

- Default copy is `bodyMd` (13px/20px, weight 450) in `p-color-text`; secondary copy `p-color-text-secondary`.
- Page title `headingLg` bold; section and modal headings `headingMd`; banner headings `headingSm`.
- Weights are Inter variable values: 450 regular, 550 medium, 650 semibold, 700 bold.
- Sentence case everywhere; no all-caps labels.
'''
R['AppHomeExample']='''A full embedded-app dashboard composed from this system, for mock-ups.

The left nav is the admin's (shown for context: your app only controls the area right of it). The page uses an info Banner for a setup step, two Sections in the main column, and an aside Section. One primary action ("Create reward") sits in the page header.
'''
R['StorefrontWidgetExample']='''A storefront theme app extension widget that inherits the merchant's theme instead of using Polaris.

- `font: inherit; color: inherit;` on the root; borders from `currentColor`; buttons take the theme's accent and radius when available.
- No `--p-*` tokens, no Inter, no admin shadows. Scope every class name (`loyalty-widget__…`) so it cannot clash with theme CSS.
- The serif "theme" around it is a stand-in to show inheritance, not a value to copy.
'''
import os
for n,t in R.items():
    os.makedirs(B+n,exist_ok=True); open(B+n+'/README.md','w').write('# %s\n\n'%n+t)
missing=[d for d in os.listdir(B) if os.path.isdir(B+d) and d not in R]
print(len(R),'readmes; dirs without:',missing)
