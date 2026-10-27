# Results, exports, and batch drift: implementation reference

This is the reviewed 4.10.111 development-series behavior reference. See [agent-assisted mzmine](../agent-assisted-mzmine.md) for the general results workflow.

## Inputs and prerequisites

`feature-table-management`, `result-features`, `result-compounds`, `result-selection-review`, `result-evaluation`, `result-grouping`, `result-batch-quality`, `feature-signal`, `batch-drift`, `result-chat-approval`, and `dashboard-navigation` use an approved feature-table scope. At most two feature tables can be actively shared (eight scopes are retained). Result export needs an existing output directory and an approved, current snapshot.

## Parameters and validation

Study grouping takes 2–32 distinct, trimmed labels of up to 128 characters; labels are case-insensitively unique. A metadata column is optional but, when supplied, must be a trimmed title up to 128 characters. Review/export requires each row only once and at least one inclusion or follow-up disposition. Result pages can fail with `result_too_large`; reduce rows or choose a smaller table.

## Processing behavior

### Immutable shared projection

Approval creates a bounded snapshot; native views/exports subsequently require that source results remain unchanged. Missing, nonfinite, and negative abundance stays unavailable—there is no raw-value fallback, imputation, or pseudocount. Opening a table is non-mutating; most other table actions alter workflow context. Disconnecting revokes active result-sharing scopes and cancels connector-owned result tasks.

### Batch drift is descriptive

Batch drift fits ordinary least squares to raw QC abundance versus run order. It needs shared run order, a defined batch, unique order, and at least three suitable QC injections. It fits only detected/manual finite nonnegative QC values, applies no correction, and reports `(fittedLast - fittedFirst) / mean` across the observed QC order range. It is not a run-acceptance decision or proof of instrumental drift.

## Outputs and side effects

Exports can produce CSV and report artifacts with scope/evaluation IDs, revision, grouping, comparability status, review dispositions, and a missing-data policy. The report explicitly says that omitted native columns and raw spectral bytes are outside its fingerprint. Dashboard navigation opens native views; it does not alter feature data.

## Edge cases and errors

The export stops if its approved scope or table snapshot becomes stale during generation. A reviewed row that disappeared, a non-modular table, unsupported export format, or a canceled export fails. Batch drift reports `needs_input` for absent sharing, batch assignment, valid run order, or fewer than three QC samples; tied timestamps require an unambiguous numeric injection order.

## Worked examples

### Two-group comparison export

Approve a feature-table scope, define `control` and `treated`, review at least one row, and export to an existing directory. If the table changes before writing, export fails rather than attaching the old approval to new data.

### QC trend request

Share run order and select one batch with three ordered QC injections. The response describes per-feature linear raw-abundance trends; it never modifies intensities or declares the batch accepted.
