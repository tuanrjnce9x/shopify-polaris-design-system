# Progress

A horizontal bar showing how far a task has advanced.

**Web component:** `<s-progress value="3" max="5" accessibilityLabel="Importing products">` · **Mock-up classes:** `pl-progress` (+ `--small`, `--primary`, `--success`, `--critical`) with a `pl-progress__bar` set by width.

- Props: `value`, `max` (default 1), `tone` (`auto`, `neutral`, `info`, `success`, `caution`, `warning`, `critical`), `accessibilityLabel`.
- The bar shows no numbers: put "3 of 5" in text beside it. Unknown duration: use a spinner instead.
- Rendition from Polaris React ProgressBar: track `p-color-bg-fill-tertiary`, default fill `p-color-bg-fill-info`, 16px tall (8px small), radius `p-border-radius-100`. The web component's exact height and default tone colour were not verified.
