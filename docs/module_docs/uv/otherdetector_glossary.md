# Other Detector Workflow Glossary

## Trace

A **trace** or **chromatogram** refers to paired 2D (x-y) data acquired from another detector, e.g.
the intensity/absorption vs. retention time from an UV or DAD detector.

## Trace type

There are three types of traces in mzmine's **Other detector**
workflow. [Raw traces](#raw-trace), [Preprocessed traces](#preprocessed-trace),
and [Features](#features).

### Raw trace

The raw trace as acquired from the detector, without any alterations such as binning, smoothing,
baseline correction, or shifting.

### Preprocessed trace

A preprocessed state of the data from a non-MS detector. In this state, a varying number of
preprocessing steps has been applied (binning, smoothing,
baseline correction, or shifting...). There is only a single preprocessed trace per raw trace at a
time. Most _other detector processing modules_ work on the preprocessed trace by default. In case
there is no preprocessed trace, mzmine will fall back to the raw trace.

### Features

A feature is a specific peak in a trace/chromatogram.

## Trace selection parameter

This parameter is used throughout the workflow for processing data from other detectors to select
the traces that are being processed.

![trace_selection_param.png](trace_selection_param.png)

!!! Info 
    Typically, it is not necessary to select all existing traces here, but only the ones you want to 
    correlate with the MS, e.g., the UV (=Absorption) traces.

**Chromatogram type** Specify the type of chromatogram you want to process. Usually, specifying this
is enough.

**Range unit filter** (Uncommon) filter the traces of the selected chromatogram type to only have a
specific unit on the range axis to be affected by this filter. Use `*` as a wildcard (match any
character)

**Range label filter** (Uncommon) filter the traces of the selected chromatogram type to only have a
specific label on the range axis to be affected by this filter. Use `*` as a wildcard (match any
character)

**Description filter** (Uncommon) filter the traces of the selected chromatogram type to only have a
specific description (=name) to be affected by this filter. Use `*` as a wildcard (match any
character)

**Trace type** Specify the [trace type](#trace-type) to be used as input
for this module.
