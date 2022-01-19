# Ion mobility trace builder

The **Ion mobility trace builder** will
build [ion mobility traces](../../wf_featuredetection/imsworkflow/ims-background-terminology.md)
from the raw data. Alternatively, the **Recursive IMS builder** can be used, which requires less ram
but takes longer.

The **Ion mobility trace builder** is found under **Feature detection → LC-IMS-MS → Ion mobility
trace builder**.

![imstracebuilder-dialog](imstracebuilderdialog.png)

##### Scan selection

The scan selection parameter specifies the scans that shall be processed for feature detection.
Usually, setting the ms level to 1 is sufficient. If a calibration segment is present, it can be cut
out via the retention time filter in the scan selection.

##### m/z tolerance

The **m/z tolerance** specifies the scan-to-scan tolerance for ion mobility traces. This tolerance
window may need to be set higher that for classic LC-MS feature detection (e.g. to 0.005 m/z and
15-20 ppm instead of 10 ppm) due to lower intensities therefore less accuracy in individual mobility
scans compared to LC-MS scans. Note that the overall accuracy is achieved via LC-IMS-MS is the same
due to the higher number of scans.

##### Minimum consecutive retention time data points

This parameter specifies the number of consecutive detections of the same m/z value in a
chromatographic peak (rt dimension only). This means that a single m/z has to be detected in, e.g, 5
frames with an intensity higher than zero. This parameter helps to filter noise. Consecutive
detections in the mobility dimension do not affect this parameter. Usually no less than 5 should be
set here if the MS1 acquisition rate is sufficient.

##### Minimum total signals

Specifies the total number of peaks in the mobility dimension in all mobility scans. Every "dot" in
an ion mobility trace represents a single datapoint.
(
see [ion mobility traces](../../wf_featuredetection/imsworkflow/ims-background-terminology.md)
)

##### Advanced parameters

For most applications, these parameters do not need to set/altered. For high mobility resolved data
the mobilograms might become noisy due to less ions reaching the detector at the same time. By
default, the number of binned scans is set to cover about 0.0008 Vs/cm^2 per bin. The effect of
binning can be seen [here](../imsexpander/ims-expander.md#binned-mobilogram-example)
. If you are unsure about the nature of your data, you can perform trace building with the standard
parameters and apply/preview the binning afterwards via the **Feature detection → Mobilogram
binning** module.

##### Processing result

After performing ion mobiltiy trace detection, a feature list is created in the feature list tab
(see [feature lists tab](../../Main-window-overview.md#ms-data-files-and-feature-lists-tab)). In the
feature table, multiple columns are created. The displayed columns can be set via the button on the
right of the feature table ([1]).

![featuretable](featuretable.png)

The **shapes** displays an EIC of the ion mobility trace (intensities summed in rt dimension). The
**mobilograms** column shows a mobilogram for the ion mobility trace (intensities summed in mobility
dimension). The shapes and projections can be smoothed and resolved. However, the ion mobility trace
is always represented by the raw data and remains unaltered. After resolving, the shapes and
mobilograms have to be recalculated from the raw data, which is why the smoothing is lost after
resolving.
