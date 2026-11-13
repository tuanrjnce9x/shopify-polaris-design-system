# Switch

A toggle for settings that apply immediately, without a save button.

**Web component:** `<s-switch label="Enable notifications" checked>` · **Mock-up classes:** `pl-switch` (`--on`) inside `pl-choice`.

- Props: `label`, `details`, `checked`, `disabled`, `error`.
- Never inside a form with a save bar: the merchant cannot tell when the change applies. Use Checkbox there.
- Rendition only: Polaris React has no switch, and the web component's exact metrics were not available. The track (32 × 20px, `p-border-radius-full`, off `p-color-bg-fill-tertiary`, on `p-color-bg-fill-brand`) and white knob are composed from tokens; check them against a live admin before you treat them as exact.
