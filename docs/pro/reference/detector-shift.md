# Other-detector shift, trim, and bin: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.107 development series. It prepares other-detector traces for comparison; see the [user guide](../../module_docs/uv/uv_shift_trim_bin_traces/uv_shift_trim_bin_traces.md).

## Inputs and prerequisites

Choose raw data files and raw and/or preprocessed traces. The default trace selection is raw UV traces, but either state can be selected. Processing is per selected other-data collection and overwrites its preprocessed-trace list.

## Parameters and validation

**RT shift (min) (manual/auto)** defaults to manual **0 min**. Manual applies the entered offset. Auto calculates one global offset across the selected files. **Trim RT range** is optional (disabled by default; stored default 0–100 min) and is applied after the shift. **Bin width (manual/auto)** is optional and disabled by default. Manual bins the entered number of points; widths of 1 or less leave a trace unchanged.

Auto binning estimates other-detector points/minute divided by MS1 scans/minute, divides the integer result by **4**, and never returns less than 1. If either RT span or the MS rate is non-positive, it returns 1.

## Processing behavior

Binning occurs before shift and trimming. Auto shift is resolved once from the binned selected traces, then the identical shift is used for all of them. A zero shift preserves the original trace object unless trimming creates a subseries. Selected results replace—not append to—the collection's preprocessed traces.

### Automatic RT-shift estimation

1. For each file, a wavelet peak picker detects peaks in the selected, already binned other-detector traces and in the MS base peak chromatogram (BPC). Peaks whose boundaries touch a neighbouring peak are excluded from matching.
2. Differences between detector and BPC peak-apex times generate candidate shifts. Nearby candidates are clustered, and the strongest supported clusters are tested.
3. Each tested shift must produce apex matches with correlated peak shapes. Matches require at least 5 correlated data points and Pearson correlation of at least 0.8. Within each detector trace, a detector peak and a BPC peak can each be used only once for that candidate.
4. The best candidate for a file has the most validated matches; ties favour higher median correlation, then lower median residual apex error. A file needs at least 3 validated matches to contribute a shift estimate.
5. The median of the valid file-level shift estimates becomes the global offset. That same offset is intentionally applied to every selected trace in every selected file, including files that could not contribute an estimate. This is consistent with manual mode, where every selected file also receives one shared offset.

## Outputs and side effects

The processed list is stored as preprocessed traces; raw traces are not altered. The selected raw data files receive an applied-method record. When auto shift is used, that record includes the resolved formatted shift.

## Edge cases and errors

Disabling binning means no binning operation at all. A trim interval can yield an empty or very short subseries; there is no module-level fallback to the untrimmed signal. Older saved `RT shift (min)` settings are loaded as manual shifts.

Files without enough validated peak matches are excluded from estimating the global offset. If no file supplies a valid estimate, automatic shifting fails and a manual shift is required.

## Worked examples

### Manual alignment and trim

With manual shift `-0.20` min and enabled trim 1.0–8.0 min, a trace is shifted first, then only its shifted points in the closed trim interval are retained.

### Sparse data and auto binning

If a trace has a zero RT span, auto binning resolves to width 1, so it is retained unbinned even when the optional binning control is enabled.
