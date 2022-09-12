# **Noise amplitude resolver**

## **Description**

:material-menu-open: **Feature detection → Chromatogram resolving → Noise amplitude resolver**

This method is suitable for chromatograms with significant background noise of varying intensities. It works in a similar way to the Baseline cut-off method, but sets the baseline level individually for each chromatogram, depending on the amplitude of signal noise.

The baseline level is calculated as follows:

- The intensity range of the chromatogram is divided into bins of the user-specified size (the Noise amplitude parameter)
- The bin with the highest number of data points is found. This bin represents the intensity level of the noise signal. 
- The baseline level is set to the intensity of the bin with the most data points

## **Parameters**

**Suffix**

This string is added to feature list name as suffix

**Original feature list**

Defines the processing. Standard is to keep the original feature list and create a new processed list. REMOVE saves memory. PROCESS IN PLACE is an advanced option to process directly in the feature list and reduce memory consumption more - this might come with side effects, apply with caution.

**MS/MS scan pairing**

Set MS/MS scan pairing parameters. For more details see [MS2 scan pairing](..//featdet_ms2_scan_pairing/ms2_scan_pairing.md)

**Min peak height**

Minimum acceptable height (intensity) for a chromatographic peak

**Peak duration range**

Range of acceptable peak durations

**Amplitude of noise**

This value is the intensity amplitude of the signal in the noise region

**Min # of data points**

Minimum number of data points on a feature.