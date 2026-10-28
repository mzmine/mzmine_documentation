# Batch diagnostics: implementation reference

This reference documents `batch_diagnostics`. See the [scientific-analysis overview](../scientific-analysis.md).

!!! info "MCP-only workflow entry point"

    In the reviewed build, this workflow is initiated through the MCP local connector. Calculation
    runs locally in mzmine, and results can be opened in mzmine's native result view.

## Inputs and prerequisites

Diagnostics use an approved snapshot whose result scope permits run-order sharing. `injection_order` is required, non-empty, unique `sN` IDs from that snapshot; `single_batch_confirmed` must be `true`. The default `abundance` is `area`; height and normalized fields are alternatives when available. Optional role mapping uses `qc`, `blank`, `sample`, or `standard`.

## Parameters and validation

`qc_sample_ids` defaults to all ordered samples explicitly mapped as `qc`; it must uniquely select ordered samples. Each `reference_rows` entry identifies an approved row and may provide expected RT, m/z, response, and `internal_standard`. Duplicate or unknown reference rows fail. Thresholds are optional non-negative `max_qc_cv`, `max_rt_shift_minutes`, `max_mass_error_ppm`, `carryover_fraction`, and `max_internal_standard_deviation_fraction`; omission is not a pass criterion.

`complete_sequence_confirmed` enables carryover assessment. `internal_standard_amounts_comparable` enables internal-standard deviation assessment. Both default false.

## Processing behavior

QC CV is calculated per feature from explicitly selected QC measurements; only detected/manual finite values contribute, so imputed or aggregated values cannot improve precision. RT shift is observed RT minus supplied expected RT; mass error is `(observed m/z − expected m/z) / expected m/z × 1,000,000` ppm. For an internal-standard reference, the target is supplied `expected_response` or the median positive usable response across selected injections; relative deviation is `(response−target)/target`.

Carryover is checked only for a blank immediately after a `sample`, `standard`, or `qc` in the supplied order. If both usable signals exist and preceding signal is positive, its fraction is `blank / preceding`; it is reported only when strictly greater than `carryover_fraction`.

## Outputs and side effects

The result records the explicit injection order, roles, value unit, no automatic correction and no automatic acceptance decision. Every sample has missing-feature count and, for referenced IS rows, response, target, relative deviation and flags. Every feature has QC CV/counts, reference measurements and flags, plus carryover status/events. No data are corrected or changed.

## Edge cases and errors

Fewer than two QCs produce a warning and unavailable/descriptive QC CV. Without complete-sequence confirmation carryover is `sequence_completeness_unconfirmed`; without a carryover threshold it is `not_requested`. Missing reference RT/m/z produces measurement-unavailable flags only when that expected value was supplied. Flags mean inspection evidence, not a release decision or proof of instrument failure.

## Worked examples

### Adjacent blank

For order `s1,s2`, roles `sample,blank`, areas 100 and 2, and `carryover_fraction: 0.01`, the event fraction is 0.02 and is flagged. Reversing the order or not confirming a complete sequence prevents that assessment.

### QC precision

Two detected QC values allow a feature QC CV. A third estimated or aggregated value does not increase the detected count used for that precision summary; a configured maximum flags an unavailable or over-threshold CV.

{{ git_page_authors }}
