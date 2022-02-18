# LC-MS Workflow
The workflow proposed herein is intended as a general pipeline for untargeted LC-MS (or LC−MS/MS) data preprocessing. The main goal is essentially to turn the highly-complex LC-MS raw data into a list of features, and corresponding signal intensity, detected across the analysed samples. Such feature lists can then be exported for furhter downstream analysis (e.g., identification, search against spectral libraries, statistical analysis, etc.). A schematic representation of the workflow is shown below:

![workflow-image](workflow-image.png)

References:
- 10.1039/9781788019880-00232
- 10.1007/978-1-0716-0239-3_3
- 10.1016/bs.coac.2018.08.003

## Raw data processing
The raw data processing consists of essentially two steps: [Data import](../../module_docs/dataimport/data-import.md#lc-ms-data) and [Mass detection](../../module_docs/massdetection/mass-detection.md)
  
### Raw data import
Either open (e.g. mzML) and native vendor (e.g. Thermo, Bruker) data formats can be imported in MZmine 3. All the supported formats are listed here (LINK to Doc). For more details see the [Data import](../../module_docs/dataimport/data-import.md#lc-ms-data) module.

### Mass detection
This step produces a list (referred to as "mass list") of the m/z values found in each MS scan across the LC run that exceed a user-defined threeshold (i.e. noise level). For more details see the [Mass detection](../../module_docs/massdetection/mass-detection.md) module.

## Feature processing
The goal of the "Feature processing" is to obtain a list of all the detected features (characterized by a RT and m/z value) from the raw LC-MS data.


### Chromatogram building
The first step in the "Feature processing" is to build the so-called extracted ion chromatograms (EICs) for each detected mass (see "Mass detection").
There are two modules in MZmine 3 that can fulfil this task: [ADAP chromatogram builder](../../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md) (widely used) and **Grid mass** (create docs).

The "detected" features in each ﬁle are listed in the so-called "feature lists", which are then further processed.

(e.g.  to  ) and aligned to connect correspond-ing features across all samples.


### Smoothing in retention time dimension (optional)
- Optional, depends on the LC peak shape
- For more details see the [Mass detection](../../module_docs/massdetection/mass-detection.md) module.

[Smoothing](../../module_docs/smoothing/smoothing.md)

### Feature resolving

[Local minimum resolver](../../module_docs/localminimumresolver/local-minimum-resolver.md)

### De-isotoping
- Remove features produced by natural isotopes
- For more details see the De-isotoping module (add link).

### Gap-filling
Gap-filling can be performed on the aligned feature lists to cope with missing features that might be artifacts of the feature-detection process.
- For more details see the [Gap-filling](../../module_docs/gapfilling/gap-filling.md) module.

## Page Contributors

{{ git_page_authors }}
