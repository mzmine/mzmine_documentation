# Shift traces (Other detectors)

Commonly, a shift in the observed retention time is observed between the MS detector and other
detectors due to different lengths in flow path. This module corrects the shift.

## Parameters

![shift_traces.png](shift_traces.png)

#### Raw data files

Select the MS data files to shift the selected traces of.

#### Trace selection

Select the specific traces you want to shift. Typically, it is not necessary to shift all existing
traces, but only the ones you want to correlate with the MS, e.g., the UV (=Absorption) traces

For a detailed description of all sub-parameters
see [trace selection parameter](../otherdetector_glossary.md#trace-selection-parameter).

#### RT shift

Specify the RT shift that shall be applied to the other detector. The numeric value will be added to
the retention time (minutes) of the other detector trace. Positive values will shift the trace
further back, negative values will shift the trace to the front.
