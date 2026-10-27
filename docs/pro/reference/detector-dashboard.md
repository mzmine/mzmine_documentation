# Other-detector correlation dashboard: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.107 development series. It is an interactive review and editing surface for MS–other-detector links; see the [user guide](../../module_docs/uv/uv_correlation_dashboard/uv_correlation_dashboard.md).

## Inputs and prerequisites

Select exactly one modular feature list. The dashboard initially selects the list's first raw data file and offers its preprocessed other-detector traces. It can be opened before automatic correlation has been run.

## Parameters and validation

The launch parameter is one feature list. The live **RT shift** control defaults to **0 min** and applies a display/editing offset between the other-detector and MS views. It is not a processing-module parameter set. The dashboard uses a fixed 0.005 m/z plus 10 ppm tolerance only to draw the auxiliary MS chromatogram.

## Processing behavior

The view links the MS and other-detector RT axes. Choosing a row, raw file, preprocessed trace, or a feature in either plot updates the related selection. If the list lacks the correlation-result column, opening the dashboard adds that column so manual associations can be stored.

**Filter MS features** filters the feature table to the selected other feature's RT range after the shift. **Define as correlated** adds a manual association for the selected MS/other features. **Clear selected correlation** removes the selected other feature from the selected MS feature. The correlation pane compares normalized signals, while the MS and other-detector plots retain their own intensity presentation.

## Outputs and side effects

Manual actions alter correlation-result data in the feature list. Existing calculated results remain distinguishable from manually defined associations. Selecting an entry in the existing-correlations selector chooses its corresponding preprocessed parent trace when possible; otherwise that selection path falls back to the raw trace.

## Edge cases and errors

Controls require the relevant selections. In this reviewed snapshot, a nonzero RT shift with no selected other feature can make the correlation display refresh fail: select the other feature before changing the shift, or keep the offset at zero. Choosing an entry in the existing-correlations selector whose preprocessed parent cannot be found falls back to raw data. The dashboard does not calculate Pearson scores; use the correlation module for automatic scoring.

## Worked examples

### Manual review before automatic correlation

Open a feature list with no correlation column, select an MS feature and a resolved other feature, then use **Define as correlated**. The dashboard first adds the result column and stores a manual association without running the automatic score threshold.

### Shifted filtering

If RT shift is 0.10 min, **Filter MS features** uses the selected other feature's RT extent adjusted by 0.10 min, not its unshifted extent.
