# Toast

A short, non-blocking confirmation after an action.

**App Bridge:** `shopify.toast.show('Settings saved', { duration, isError, action, onAction })` · **Mock-up classes:** `pl-toast` (`--error`), `pl-toast__action`.

- Message: noun + past-tense verb, sentence case, no period ("Product saved", "Discount deleted").
- Errors that need action belong in a banner or inline error, not a toast.
- One action at most ("Undo", "Retry").
- The admin renders it at the bottom of the screen: `p-color-bg-inverse`, `p-color-text-inverse`, radius `p-border-radius-200`, `p-shadow-400`, padding `p-space-300`; error uses `p-color-bg-fill-critical`.
