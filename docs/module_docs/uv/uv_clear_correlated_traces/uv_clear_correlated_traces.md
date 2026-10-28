# Clear correlated traces (Other detectors)

!!! info

    Processing data from other detectors requires the Other detector service of mzmine. This feature
    is included in the mzmine Pro subscription. Academic program and other users can inquire about
    [access options](https://mzio.io/#contact).

:material-menu-open: **Feature list methods → Other detectors → Clear correlated traces (Other detectors)**

**Clear correlated traces** removes the stored links between MS features and other-detector
features from the selected feature lists. Use it when a correlation was run with unsuitable trace
selection, retention-time shift, tolerance, or score threshold and you want to recreate the links.

The module preserves the MS feature list, raw traces, preprocessed traces, and resolved
other-detector features. It only clears the **Correlated traces** results attached to each feature.

## Parameters

#### Feature lists

Select the feature lists whose stored correlations should be removed. The selected lists are
modified in place.

## Next steps

After clearing correlations, correct any retention-time offset with
[Shift, trim, and bin traces](../uv_shift_trim_bin_traces/uv_shift_trim_bin_traces.md) if needed,
then run [Correlate MS features with other detectors](../uv_ms_other_aligner/uv_ms_other_aligner.md)
again. Use the [Correlation dashboard](../uv_correlation_dashboard/uv_correlation_dashboard.md) to
inspect or manually adjust the new assignments.

---

{{ git_page_authors }}
