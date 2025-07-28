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
