# ChoiceList

A labelled group of radio buttons, or checkboxes with `multiple`.

**Web component:** `<s-choice-list label="…">` with `<s-choice value="…">` · **Mock-up classes:** `pl-choice-list`, `pl-choice`, `pl-radio` (`--checked`) or `pl-checkbox`.

- Props: `label`, `name`, `multiple`, `details`, `error`, `disabled`, `values`; on `s-choice`: `value`, `selected`, `defaultSelected`, `disabled`.
- Labels describe the outcome ("Free shipping"), not the mechanism.
- More than ~20 options: use Select.
- Radio: 18px circle, 0.66px `p-color-input-border`; selected fills `p-color-bg-fill-brand-selected` with an 8px `p-color-text-brand-on-bg-fill` dot.
