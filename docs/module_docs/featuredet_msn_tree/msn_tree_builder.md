# MSn tree feature list builder

:material-menu-open: **Feature detection → MSn → MSn tree feature list builder** 

This module is an alternative to the [Chromatogram builder](../lc-ms_featdet/featdet_adap_chromatogram_builder/adap-chromatogram-builder.md) 
for creating chromatograms based on MS2 spectra or MSn trees. 

1. Groups all MS2 spectra are by an m/z tolerance.
2. Adds MSn, multi-stage fragmentation, spectra to the MS2 groups, if they are present.
3. Builds an extracted ion chromatogram (EIC) for each group around their first MS2 scans precursor m/z and the m/z tolerance.
4. The EICs may be empty if the precursor m/z reported in the MS2 scan metadata does not match the MS1 data or if the m/z tolerance is too narrow.
5. Even empty EICs will be reported in the resulting feature list with their respective precursor m/z and fragmentation scans.

## Parameters

#### Raw data files
The selected data files to process. 

#### EIC scans
A filter to select scans (usually MS1) for building extracted ion chromatograms. 

#### m/z tolerance (scan-to-scan)
Defines the fluctuation of an individual m/z peak in between scans. For TOF instruments, 0.005 m/z
or 20 ppm is a good starting point, while Orbitraps or FT-ICRs can achieve narrower signals
depending on the set mass resolution.

#### Suffix
This suffix is added to the produced feature list.


---

{{ git_page_authors }}
