# Multi-detector visualizer: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.111 development series. It is the shared multi-detector plotting surface exposed in the Pro **Other detectors** menu; see the [user guide](../../module_docs/uv/uv_multi_detector_visualizer/uv_multi_detector_visualizer.md).

## Inputs and prerequisites

The command opens a visualizer tab rather than processing a selected file or feature list. Its usable content depends on other-detector data already attached to the open project. The Pro workspace inserts this command at the top of its **Other detectors** menu, ahead of the processing modules.

## Parameters and validation

Launching the command has no user-facing module parameters. Opening returns successfully after adding the tab; data selection and display interaction occur within the GUI surface.

## Processing behavior

The launch operation creates/adds the multi-detector visualizer tab and schedules no processing task. It therefore does not build chromatograms, apply a shift, baseline-correct, resolve peaks, or write correlation results.

Within the tab, visualization and manual integration use the selected collection's preprocessed traces when available. If the collection has no preprocessed traces, they fall back to its raw traces. Existing resolved features for the selected trace are loaded into the integration plot and can be edited.

## Outputs and side effects

Opening the tab alone leaves project data unchanged. Manual integration followed by **Save** replaces the selected trace's resolved features with the edited integration results, including any additions or removals. These features are associated with the original raw trace; the raw and preprocessed trace signals themselves remain unchanged.

## Edge cases and errors

Because the command has no parameter validation, it can open even when the project has no useful other-detector traces; in that state there is simply nothing meaningful to visualize. Opening the visualizer is not evidence that the other-detector service or any particular data-processing output is available.

Manual edits are not written back until **Save** is pressed.

## Worked examples

### Inspect without mutation

Opening **Multi detector visualizer** after importing data adds the viewing tab but leaves raw traces, preprocessed traces, and feature correlations unchanged.

### Save a manually integrated peak

Select a trace, set its peak boundaries, accept the integration with **Finish feature**, and press **Save**. The edited feature set replaces the resolved features for that trace. If the collection has no preprocessed traces, integration uses the raw signal.

### Prepare data first

If only spectral other-data are available, first run the chromatogram builder to create time series; opening the visualizer alone will not perform that extraction.
