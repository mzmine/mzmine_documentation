
# Export scans (feature list)

:material-menu-open: **Feature list methods → Export feature lists → Export scans (feature list)** 

A module to export spectra in different formats like mgf, msp, json (mzmine) with many options to customize the scan selection and output.
One application of this module is to export fragment scans merged on various levels. 
Furthermore, this module allows to generate "blank" or "sample" libraries of unknown spectra with added identifiers from sample wide metadata.

## Parameters

#### **Export file**

The path and name of the exported spectra.

#### **Export format**

Here, you can set the export format. It mostly depends on your next steps and where to import the
library. Every format works, but we recommend the .json format.

#### **Metadata**

Various information about the acquired data can be stored her. For example, who acquired the data,
which instrument was used, ect. On the description information about the compounds or library can be
given. The Ion mode is only need, when the polarity is not safed in the data files.

#### **Sample wide metadata**

This is metadata that is imported as project metadata for each sample, usually from a tsv or csv table.
This parameter allows to map the values from specific columns to all scans of these samples. So if a spectrum was merged from two samples, 
the compound name or entry description will contain the values from all source samples. 

This option was added to allow for **blank libraries** or **sample libraries**. Measure various blanks like 
"well plate, manufacturer XY" and load this information as sample metadata. Then define the column to be used as compound name or description 
to export all scans from this sample labelled as potentially originating from this blank.

#### **Skip annotated features**

If true, annotated features will be skipped and only "unknown" features will be exported. 
This is useful when all annotated features were already exported by the 
[**Spectral library batch generation**](../io_spectral_library_export/spectral_library_generation.md). 

#### **Export MS1**

Option to export MS1 scans, either the most intense MS1 across all samples or a correlated MS1 of isotopologue and adduct signals.
The MS1 data may be exported together with fragment scans or into a separate file. 

#### **Intensity normalization**

Options to apply intensity normalization to all signals. Scientific format is preferred as it best accounts for many orders of magnitude.

### **Export fragment scans**

#### **Handle chimeric spectra**

Score the isolation purity and handle chimeric precursor ion isolation. See full description of all parameters in
[**Spectral library batch generation**](../io_spectral_library_export/spectral_library_generation.md#Chimeric-spectra).

#### **Merge & select fragment scans**

This parameter controls how fragment spectra are filtered, merged, and selected for downstream analysis
(see [detailed description](../filter_scan_merge_select/scan_merge_select.md)). Briefly, either choose
preset based spectral merging, input scans without merging, or an advanced setup for more options.

#### **Minimum signals**

Threshold to exclude low informative spectra from export.

### **Advanced**

#### **Compact USI**

Universal spectrum identifiers:

- Compact USI are non canonical USI for merged spectra and export a list of USI for each sample one, where all source scan number are reduced to number ranges as in 1-5,9 for the scans from 1 to 5 and scan 9. This greatly reduces the redundancy compared to regular USI.
- Regular USI export a list of USI, one for each source scan of a merged spectrum. 

---

{{ git_page_authors }}
