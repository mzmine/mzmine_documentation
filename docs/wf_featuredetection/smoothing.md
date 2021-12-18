#Smoothing

## Retention time dimension

Smoothing chromatograms is optional.
The necessity of smoothing in RT dimension is determined by the noisiness of chromatographic peaks.
These can be influenced by the overall spray stability, instrument accumulation times, transfer
efficiency and many more.

The number of data points to be smoothed in rt dimension can be set at [1]. Note that the correct
preview dimension is selected at [2].

For large batch modes, the **Remove original feature list** parameter should be selected. While
parameters are being optimised, this is not recommended, because removing a feature list cannot be
undone.

![](../img/imsworkflow/smoothingdialog.png)

## Mobility dimension

After resolving a feature in RT dimension, the mobilograms will be recalculated from the from the
raw data (the resolved ion mobility trace). Therefore, a smoothing step is necessary if the data
requires it. The smoothing dialog is opened via **Feature detection → Smoothing**

Select to smooth the mobility dimension [1] and select it as preview dimension [2]. The filter with
depends on the number of spectra acquired in the observed mobility range. Usually, a value between 5
and 15 should be appropriate.

![](../img/imsworkflow/mobilitysmoothing.png)
