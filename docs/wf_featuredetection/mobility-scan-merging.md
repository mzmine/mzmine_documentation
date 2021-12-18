# Mobility scan merging

If a .mzML file is imported, the merged frame spectrum must be created via the **File merging →
Mobility scan merging** module. This is required to gain access to MZmine's regular LC-MS
functionality. This step uses the centroided and thresholded data produced by
the [mass detection](mass-detection.md#LC-IMS-MS-data)
step.

**This step is not required when importing native Bruker .tdf or .tsf data from .d folders.**
When importing native Bruker data, a merged spectrum for the frame is created automatically by the
vendor library.
