# Table

Rows of resources with columns; becomes a stacked list on small screens.

**Web components:** `<s-table>` › `<s-table-header-row>` › `<s-table-header>`, `<s-table-body>` › `<s-table-row>` › `<s-table-cell>` · **Mock-up classes:** `pl-table` inside `pl-card pl-card--flush`, `pl-num` for numbers, `pl-table__footer`, `pl-tabs` / `pl-tab` for index views.

- `s-table`: `variant` (`auto`, `list`), `paginate`, `loading`, `hasNextPage`, `hasPreviousPage`; `filters` slot for search and filter controls.
- `s-table-header`: `format` (`base`, `numeric`, `currency`) right-aligns numbers; `listSlot` (`primary`, `secondary`, `kicker`, `inline`, `labeled`) decides the mobile layout.
- Headers must still read as key–value pairs when stacked. Paginate beyond ~50 rows.
- Rendition from Polaris IndexTable: header `p-color-bg-surface-secondary`, 12px medium `p-color-text-secondary`; rows on `p-color-bg-surface` with a `p-color-border-secondary` top rule, hover `p-color-bg-surface-hover`. Tabs above the table are the admin index-filter pattern (no web component).
