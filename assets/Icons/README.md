# Icons

22 icons copied unchanged from `@shopify/polaris-icons` 9.3.1 (`dist/svg/`). Each is a 20 × 20 viewBox, single-ink SVG with no `fill`, so it renders **black (#000000)** in an `<img>`. To tint one, inline its markup and set `fill` (the `pl-icon` class uses `p-color-icon`, #4a4a4a).

- Navigation: `HomeIcon`, `OrderIcon`, `ProductIcon`, `CartIcon`, `AppsIcon`, `SettingsIcon`, `MenuIcon`.
- Actions: `PlusIcon`, `EditIcon`, `DeleteIcon`, `ViewIcon`, `SearchIcon`, `XIcon` (close or dismiss).
- Status: `CheckIcon`, `CheckCircleIcon` (success), `InfoIcon` (info banner), `AlertTriangleIcon` (warning), `AlertCircleIcon` (inline error), `QuestionCircleIcon` (help).
- Controls: `ChevronDownIcon` (disclosure), `SelectIcon` (select field), `ImageIcon` (missing image placeholder).

In web components, refer to them by kebab-case name without the suffix: `<s-icon type="alert-circle">`, `<s-button icon="plus">`.
