# LC-IMS-MS Workflow Overview
## Supported formats

* Vendor formats:
  * .tdf (Native Bruker LC-IMS-MS and MALDI-IMS-MSI format)
  * .tsf (Native Bruker MALDI-IMS-MS (single shot) format)
* .mzML
  * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native Bruker
        data
  * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native Waters
      data

**Note**: mzML via MSConvert from Agilent raw data can be imported, but certain restrictions might
hinder processsing workflows due to the nature of the raw data format.


***

## Background information and terminology

***

## Raw data processing

### Raw data import

[Data import](data-import.md#LC-IMS-MS-data)

### Mass detection

[Mass detection](mass-detection.md#LC-IMS-MS-data)

### Mobility scan merging

**This step is not required when importing native Bruker .tdf or .tsf data from .d folders.**
[Mobility scan mering](mobility-scan-merging.md)

## Feature detection workflows

Ion mobility data can be processed in MZmine 3 in two ways. The first few steps are different for
the two workflows.

1. Regular LC-MS workflow via **ADAP Chromatogram builder and IMS expander** (recommended)
    - build extracted ion chromatograms (rt dimension) from frame spectra
        - requires merged frame spectra (see [mobility scan merging](#Mobility-scan-merging))
    - smoothing (optional)
    - resolve retention time dimension
    - expand features into mobility dimension
    - smoothing (optional)
    - resolve mobility dimension
    - smoothing (optional)
2. LC-IMS-MS workflow via **Ion mobility trace builder / Recursive IMS builder**
    - directly build ion mobility traces (rt and mobility dimension)
    - smoothing (optional)
    - resolve retention time dimension
    - smoothing (optional)
    - resolve mobility dimension
    - smoothing (optional)

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
the [Mobility scan merging](#mobility-scan-merging) module is a mandatory step, if the data was
imported from an .mzML file (automatically generated via native Bruker import).

### ADAP chromatogram builder

[ADAP Chromatogram builder](adap-chromatogram-builder.md)

#### Smoothing in retention time dimension (optional)

[Smoothing](smoothing.md)

#### Resolving in retention time dimension

[Local minimum resolver](local-minimum-resolver.md)

#### Expanding EICs in mobility dimension

[IMS expander](ims-expander.md)

#### Smoothing  in mobility dimension (optional)

[Smoothing](smoothing.md#Mobility-dimension)

#### Resolving in mobility dimension

[Local minimum resolver (Mobility dimension)](local-minimum-resolver.md#ion-mobility-data)

#### Smoothing in rt and mobility dimension (optional)

Some recognised features might have rather noisy signals (in rt and mobility dimension) after the
mobility resolving step. If smoother shapes are required, the smoothing can be reapplied afterwards.
In that case, smoothing can be applied to both dimensions at once.

[Smoothing](smoothing.md)


### LC-IMS-MS workflow

The LC-IMS-MS workflow will directly build [ion mobility traces](#Ion-mobility-traces) from the raw
data in the mobility scans. This workflow does not necessarily require summed frame spectra.
However, if extracted ion chromatograms shall be visualized via
the [Chromatogram visualizer](../Raw-data-visualisation.md#Chromatogram-plot), the frame intensities
are used. In case these are not present, the chromatograms will be blank. Note that feature
intensities from the LC-IMS-MS workflow might not exactly match the frame chromatograms due to
summing being executed prior to thresholding (for native Bruker data). Furthermore, multiple isomers
might hide behind a single chromatographic peak.

#### Ion mobility trace builder

[Ion mobility trace builder](ion-mobility-trace-builder.md)

#### Smoothing in retention time dimension (optional)

[Smoothing](smoothing.md)

#### Resolving in retention time dimension

[Local minimum resolver](local-minimum-resolver.md)

#### Smoothing  in mobility dimension (optional)

[Smoothing](smoothing.md#Mobility-dimension)

#### Resolving in mobility dimension

[Local minimum resolver (Mobility dimension)](local-minimum-resolver.md#ion-mobility-data)

#### Smoothing in rt and mobility dimension (optional)

Some recognised features might have rather noisy signals (in rt and mobility dimension) after the
mobility resolving step. If smoother shapes are required, the smoothing can be reapplied afterwards.
In that case, smoothing can be applied to both dimensions at once.

[Smoothing](smoothing.md)

## Graphical comparison of LC-MS and LC-IMS-MS data

[Data comparison](lc-ms-and-lc-ims-ms-data-comparison.md)

## Page Contributors

{{ git_page_authors }}
