# MS–other-detector correlation: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.111 development series. It associates MS features with resolved other-detector features; see the [user guide](../../module_docs/uv/uv_ms_other_aligner/uv_ms_other_aligner.md).

## Inputs and prerequisites

Select feature lists and other-detector features. The trace selector only permits the **features** state and defaults to UV features. The feature list's raw data files must have selected other-detector features for correlation to be possible.

## Parameters and validation

**RT tolerance** defaults to **4 seconds** around the MS feature apex. **Minimum correlation score** defaults to **0.8**, is Pearson r, and is constrained to 0–1.

## Processing behavior

For each non-unknown MS feature, only other-detector features whose apex is inside the RT tolerance are considered. The two RT spans must also overlap. Shapes are correlated using the shared DIA shape routine with a minimum of five points and its fixed interpolation settings; results below the minimum score (or no computable correlation) are discarded.

## Outputs and side effects

Each passing pair is stored on the MS feature as a calculated correlation result containing the other feature and Pearson r. Existing correlation results are only replaced when this run finds at least one passing pair for that MS feature; a run that finds none does not clear a prior value.

## Edge cases and errors

Raw files without matching other-detector features are skipped. Unknown MS features are skipped. A candidate with an apex in tolerance but non-overlapping RT ranges is rejected before shape correlation.

## Worked examples

### Apex close, shapes insufficient

An other feature 3 seconds from an MS apex is a candidate with default tolerance, but it is not stored if its Pearson r is 0.79 under the default 0.8 threshold.

### No overlap

Two features can meet the apex tolerance yet produce no correlation if their measured RT ranges do not connect; no result is attached.
