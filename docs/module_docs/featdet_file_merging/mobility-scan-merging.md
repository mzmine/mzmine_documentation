# Mobility scan merging

## **Description**

**File merging → Mobility scan merging** 

This module merges mobility scans at the same retention time to a summed frame spectrum.

The merged frame spectrum is used if a *.mzML file is imported. The merged frame spectrum is required to gain access to MZmine's LC-MS
functionality. 

:material-exclamation-thick: This step uses the centroided and thresholded data produced by
the [mass detection](../featdet_mass_detection/mass-detection.md)
step.

:warning: **This step is not required when importing native Bruker .tdf or .tsf data from .d folders.**
When importing native Bruker data, a merged spectrum for the frame is created automatically by the
vendor library.

## **Parameters**

**Raw data files**

Raw data files the module will take as an input.

**Noise level**

Data points beyond the defined noise level threshold will be ignored.

**Merging type**

The way to calculate intensities. Intensities can be either averaged, summed, or the maximum value can be chosen.

**m/z weighing**

Chosen function is used to weigh m/z values by their intensities. The available options are:

+ None,
+ Linear,
+ log10,
+ log2,
+ square root,
+ or cube root.

**Scans**

Selects the scans that should be included.

**m/z tolerance**

Maximum allowed difference between two m/z values in order for them to be considered the same.

