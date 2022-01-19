# LC-IMS-MS Workflow Overview

## Supported formats

* Vendor formats:
    * .tdf (Native Bruker LC-IMS-MS and MALDI-IMS-MSI format)
    * .tsf (Native Bruker MALDI-IMS-MS (single shot) format)
* .mzML
    * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native Bruker
      data
    * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native
      Waters/Agilent data

***

## Feature detection workflows

Ion mobility data can be processed in MZmine 3 in two ways. The first few steps are different for
the two workflows (see below).

1. [LC-IMS-MS workflow via **ADAP Chromatogram builder and IMS expander** **(recommended)**](#lc-ms-workflow-recommended)
2. [LC-IMS-MS workflow via **Ion mobility trace builder / Recursive IMS builder**](#lc-ims-ms-workflow)

While these lists might seem fairly similar, there are some differences in the processing approach.
The LC-IMS-MS workflow builds ion mobility traces from the data in the mobility scans, whilst the
LC-MS workflow builds EICs from the summed frames. Imagine setting the noise level to 200 and occurs
in 15 mobility scans with an intensity of 180 and in 20 with > 200, but the ion mobility trace
builder required at least 25 data points. At the same time, the ADAP chromatogram builder was set to
a minimum highest intensity of 1000 in a frame, which might have been reached due to summed
intensities.  
Since intensities are summed to build frames, the LC-MS workflow can be more sensitive to less
abundant compounds whilst the LC-IMS-MS workflow will directly detect ion mobility traces and be
less susceptible to noise. For .mzML data, this might not make a significant impact, because the
frame is built from the thresholded mass list. This means that the main impact on sensitivity for
low intense compounds is made by the user's noise level selection. However, for native Bruker raw
data, the summed frame is automatically built via the functionality of the vendor library without
the user's influence. Therefore, the more low abundant compounds might be detected, if the LC-MS
workflow is chosen.

### LC-MS workflow (recommended)

LC-IMS-MS data can also be processed via the regular LC-MS modules. If necessary, detected features
can be expanded into the mobility dimension.

For this workflow, generation of summed frame spectra via
the [Mobility scan merging](../../module_docs/mobilityscanmerging/mobility-scan-merging.md) module is a mandatory step, if the data was
imported from an .mzML file (automatically generated via native Bruker import).
  - [Data import](../../module_docs/dataimport/data-import.md#lc-ims-ms-data)
  - [Mass detection](../../module_docs/massdetection/mass-detection.md#lc-ims-ms-data)
  - [Mobility scan merging](../../module_docs/mobilityscanmerging/mobility-scan-merging.md) (mzML data)
  - [ADAP Chromatogram builder](../../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md)
  - [Smoothing in retention time dimension (optional)](../../module_docs/smoothing/smoothing.md)
  - [Resolving in retention time dimension](../../module_docs/localminimumresolver/local-minimum-resolver.md)
  - [Expanding EICs in mobility dimension](../../module_docs/imsexpander/ims-expander.md)
  - [Smoothing  in mobility dimension (optional)](../../module_docs/smoothing/smoothing.md#mobility-dimension)
  - [Resolving in mobility dimension](../../module_docs/localminimumresolver/local-minimum-resolver.md#ion-mobility-data)
  - [Smoothing in rt and mobility dimension (optional)](../../module_docs/smoothing/smoothing.md)
    - Some recognised features might have rather noisy signals (in rt and mobility dimension) after the
mobility resolving step. If smoother shapes are required, the smoothing can be reapplied afterwards.
In that case, smoothing can be applied to both dimensions at once.

### LC-IMS-MS workflow

The LC-IMS-MS workflow will directly
build [ion mobility traces](ion-mobility-spectrometry-terminology.md#ion-mobility-trace) from the raw data in the
mobility scans. This workflow does not necessarily require summed frame spectra. However, if
extracted ion chromatograms shall be visualized via
the [Chromatogram visualizer](../../Raw-data-visualisation.md#chromatogram-plot), the frame intensities
are used. In case these are not present, the chromatograms will be blank. Note that feature
intensities from the LC-IMS-MS workflow might not exactly match the frame chromatograms due to
summing being executed prior to thresholding (for native Bruker data). Furthermore, multiple isomers
might hide behind a single chromatographic peak.
  - [Data import](../../module_docs/dataimport/data-import.md#lc-ims-ms-data)
  - [Mass detection](../../module_docs/massdetection/mass-detection.md#lc-ims-ms-data)
  - [Ion mobility trace builder](../../module_docs/ionmobilitytracebuilder/ion-mobility-trace-builder.md)
  - [Smoothing in retention time dimension (optional)](../../module_docs/smoothing/smoothing.md)
  - [Resolving in retention time dimension](../../module_docs/localminimumresolver/local-minimum-resolver.md)
  - [Smoothing  in mobility dimension (optional)](../../module_docs/smoothing/smoothing.md#mobility-dimension)
  - [Resolving in mobility dimension](../../module_docs/localminimumresolver/local-minimum-resolver.md#ion-mobility-data)
  - [Smoothing in rt and mobility dimension (optional)](../../module_docs/smoothing/smoothing.md)
    - Some recognised features might have rather noisy signals (in rt and mobility dimension) after the
mobility resolving step. If smoother shapes are required, the smoothing can be reapplied afterwards.
In that case, smoothing can be applied to both dimensions at once.


## Graphical comparison of LC-MS and LC-IMS-MS data

[Data comparison](lc-ms-and-lc-ims-ms-data-comparison.md)

## Page Contributors

{{ git_page_authors }}
