# Bin traces (Other detectors)

As other detectors typically have a higher acquisition rate than mass spectrometers, it may be
useful to bin the detected intensities/absorptions together to achieve a similar acquisition rate
for better [cross-correlation](../uv_ms_other_aligner/uv_ms_other_aligner.md) and processing
performance.


## Parameters
![parameters.png](parameters.png)

#### Raw data files

Select the MS data files to bin the selected traces of.

#### Trace selection

Select the specific traces you want to bin. Typically, it is not necessary to bin all existing
traces, but only the ones you want to correlate with the MS, e.g., the UV (=Absorption) traces.

For a detailed description of all sub-parameters
see [trace selection parameter](../otherdetector_glossary.md#trace-selection-parameter).

#### Bin width (manual/auto)

Set how many points shall be binned.
"Auto" will adjust the acquisition rate of the other detector to **four** times the MS acquisition rate.
"Manual" will bin the given number of points manually.
