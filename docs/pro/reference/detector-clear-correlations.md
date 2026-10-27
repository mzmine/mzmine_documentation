# Clear MS–other-detector correlations: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.111 development series. It removes stored correlation results; see the [user guide](../../module_docs/uv/uv_clear_correlated_traces/uv_clear_correlated_traces.md).

## Inputs and prerequisites

Select from **1 to 2,147,483,647** feature lists. This module changes stored annotation data in the selected lists; it does not need other-detector traces to still be present.

## Parameters and validation

The only parameter is **Feature lists**. At least one list is required. There are no score, RT, or trace-selection controls because the operation removes all stored MS–other correlation results it encounters.

## Processing behavior

For every row and every modular feature in each selected list, the module checks whether correlation-result data exists and removes that data field when present.

## Outputs and side effects

The selected feature lists are mutated in place. Only the correlation-result field is removed; the MS feature, other-detector features, raw/preprocessed traces, and unrelated feature annotations remain.

## Edge cases and errors

Rows or features without stored results are left unchanged. Clearing does not regenerate a feature table or delete an other-detector signal. It is therefore safe to run on a list that has never been correlated, but it is irreversible unless the project was saved beforehand or correlations are recomputed.

## Worked examples

### Clear mixed rows

In a list where only one feature has stored correlated traces, that field is removed from that feature while rows without it remain unchanged.

### Recalculate after clear

After clearing, running MS–other correlation again creates only the new qualifying result set; the clear operation itself cannot restore former scores.
