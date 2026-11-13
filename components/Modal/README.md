# Modal

An overlay for a focused task or a confirmation; opened only by a merchant action.

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
