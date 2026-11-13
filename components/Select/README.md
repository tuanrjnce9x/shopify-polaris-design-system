# Select

Choose one option from four or more in a dropdown.

**Web component:** `<s-select label="…">` with `<s-option value="…">` and `<s-option-group label="…">` · **Mock-up classes:** `pl-field pl-select`, `pl-input`, `pl-input__value`.

- Props: `label`, `value`, `placeholder`, `details`, `error`, `disabled`, `required`, `icon`.
- Fewer than four options: use ChoiceList. Multiple selection: ChoiceList with `multiple`.
- Pre-select the sensible default. Options are plain text, no search.
- Same field frame as TextField; the Select icon is `p-color-icon-secondary`.
