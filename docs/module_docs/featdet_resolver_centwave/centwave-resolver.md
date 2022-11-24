# **CentWave Resolver**

## **Description**

:material-menu-open: **Feature detection → Chromatogram resolving → CentWave resolver**

This method uses wavelets (from [xcms library](http://www.bioconductor.org/packages/release/bioc/html/xcms.html)) to detect features within a chromatogram. A series of wavelets of different scales is convolved within the chromatogram. **Local maxima** in the convolution results determine the locations of possible peaks. 

When these candidate feature locations co-occur at multiple scales then the scale with the strongest response indicates **peak width**. Given the candidate feature locations and scales, features can then be reconstructed from the original chromatogram. 

Full details of the algorithm are published in Tautenhahn et al. [[1]](#references).

### **Requirements**

The Wavelets detector employs **Bioconductor's XCMS package for R** [[2]](#references). Therefore, you must have R v2.15 or later installed. To install the XCMS package, run R and issue the following commands:

    source("http://bioconductor.org/biocLite.R")
    biocLite("xcms")

To run R from MZmine the Rserve package [[3]](#references) must be installed in R, so also run the following R command:

    install.packages("Rserve")

## **References**

!!! quote " "

    1. Ralf Tautenhahn, Christoph Böttcher, and Steffen Neumann "Highly sensitive feature detection for high resolution LC/MS" BMC Bioinformatics 2008, 9:504

    2. Bioconductor XCMS "LC/MS and GC/MS Data Analysis" http://www.bioconductor.org/packages/release/bioc/html/xcms.html.

    3. Rserve "A TCP/IP server which allows other programs to use facilities of R" https://rforge.net/Rserve/.

## **Parameters**

#### **Suffix**

This string is added to feature list name as suffix

**Original feature list**

Defines the processing.

Standard is to KEEP the original feature list and create a new processed list.

REMOVE saves memory.

PROCESS IN PLACE is an advanced option to process directly in the feature list and reduce memory consumption more - this might come with side effects, apply with caution.

#### **MS/MS scan pairing**

Set MS/MS scan pairing parameters. For more details see [MS2 scan pairing](..//featdet_ms2_scan_pairing/ms2_scan_pairing.md)

#### **S/N Threshold**

Features with a signal-to-noise ratio less than the threshold will be rejected.

The S:N ratio is defined as

$$(max - baseline) / sd$$

where max is the maximum feature intensity, baseline is the estimated baseline value, and sd is the standard deviation of local chromatographic noise.

[//]: # (Peak scales)

[//]: # (The range of peak scales to search for. Scales are expressed as RT values &#40;minutes&#41; and correspond to the range of wavelet scales that will be applied to the chromatogram. If the minimum scale is too small then noise may be detected as peaks. If the maximum scale is to low then broad peaks may be ignored.)

#### **Peak duration range**

The acceptable range of feature widths. Features with widths outside this range will be rejected.

#### **Peak integration method**

Type of data used during feature reconstruction.

When reconstructing a feature from the chromatogram, gradient descent is used. This can be performed on the raw peak data or a smoothed version of it. Smoothed data is obtained through mexican hat filtering.

Using the unfiltered data is more accurate but can be susceptible to noise. The smooth data provide less exact results but are more robust in the presence of noise.

#### **R engine**

The R engine to be used for communicating with R. RServe might provide you with better performance.

#### **Min # of data points**

Minimum number of data points on a feature.

{{ git_page_authors }}