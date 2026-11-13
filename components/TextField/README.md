# TextField

Single-line text input with a label, help text and inline error.

**Web component:** `<s-text-field label="…">` (siblings: `s-email-field`, `s-number-field`, `s-money-field`, `s-password-field`, `s-search-field`, `s-url-field`, `s-text-area`) · **Mock-up classes:** `pl-field`, `pl-label` (`--required`), `pl-input` (`--focus`, `--error`, `--disabled`), `pl-input__prefix|suffix`, `pl-help`, `pl-error`.

- Props: `label`, `value`, `placeholder`, `details` (help text), `error`, `prefix`, `suffix`, `icon`, `required`, `disabled`, `readOnly`, `maxLength`, `minLength`, `autocomplete`, `labelAccessibilityVisibility` (`visible`, `exclusive`); `accessory` slot.
- Always a visible label; put formats in `details`, units in `suffix`.
- Errors say how to fix it ("Enter a valid email address").
- Input: `p-color-input-bg-surface`, 0.66px `p-color-input-border` (top edge #898f94, a literal in the Polaris source), radius `p-border-radius-200`, 32px tall, `bodyMd`. Focus: `p-color-input-border-active` plus a 2px `p-color-border-focus` outline offset 1px. Error: `p-color-bg-surface-critical` and `p-color-border-critical-secondary`.
