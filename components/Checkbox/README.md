# Checkbox

An on/off choice that takes effect when the form is saved.

**Web component:** `<s-checkbox label="…" checked>` · **Mock-up classes:** `pl-choice`, `pl-choice__control`, `pl-checkbox` (`--checked`), `pl-choice--disabled`, `pl-choice__help`.

- Props: `label`, `details`, `checked`, `indeterminate`, `disabled`, `error`, `name`, `value`.
- Use with a save action; for settings that apply instantly use Switch.
- 18px control (20px on mobile), radius `p-border-radius-100`, 0.66px `p-color-input-border`; checked fill `p-color-bg-fill-brand-selected` with a white check (`p-color-text-brand-on-bg-fill`); label `bodyMd`, `p-space-200` gap.
