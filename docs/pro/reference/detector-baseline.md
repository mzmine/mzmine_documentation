# Other-detector baseline correction: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.107 development series. It baseline-corrects selected other-detector traces; see the [user guide](../../module_docs/uv/uv_baseline_correction/uv_baseline_correction.md).

## Inputs and prerequisites

Select raw data files and raw or preprocessed traces. The default selection is preprocessed UV traces. The selected algorithm's nested settings are part of the parameter state.

## Parameters and validation

**Suffix** defaults to `bl`; it is retained as a parameter but is not used to rename the stored traces by this task. **Baseline corrector** offers LOESS, Polynomial, Spline, and arPLS, defaulting to **arPLS**. Algorithm-specific validation and settings come from the selected corrector.

## Processing behavior

For each selected trace, the chosen corrector produces a corrected time series and a derived feature is made from it. The task uses a fresh corrector instance for each selected other-data collection. It then replaces that collection's preprocessed traces with the corrected results.

## Outputs and side effects

Corrected results intentionally replace the preprocessed traces, whether the selected input was raw or preprocessed. Raw traces remain unchanged. The output is not a new raw-data file or feature list: it is the current preprocessed trace set for each matched collection. Subsequent feature resolution therefore sees the corrected, replacement preprocessed data.

## Edge cases and errors

Selecting no matching collections performs no correction. The `Suffix` does not create a parallel named trace collection in this implementation, so it should not be treated as a preservation mechanism.

## Worked examples

### Default correction

Running with the untouched dialog uses arPLS on the default preprocessed UV traces and replaces those preprocessed traces with their corrected derivatives.

### Preserving a raw source

Selecting a raw trace does not overwrite the raw trace: the corrected derivative is stored as preprocessed data, allowing the raw signal to remain selectable later.
