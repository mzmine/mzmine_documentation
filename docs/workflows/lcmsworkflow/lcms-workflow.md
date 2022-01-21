# LC-MS Workflow
The following workflow is intended to turn raw LC-MS data into a table of all the detected features and corrisponding signal intensity detected in each sample. A schematic representation of the workflow is shown below:

![workflow-image](https://github.com/titodamiani/mzmine_documentation/blob/e90deb3ccb11b18c94f7f27ed76f71c818640091/docs/workflows/lcmsworkflow/workflow-image.png)


## Raw data processing
The raw data processing consists of essentially two steps: [Data import](../../module_docs/dataimport/data-import.md#lc-ms-data) and [Mass detection](../../module_docs/massdetection/mass-detection.md)
  
### Raw data import
Either open (e.g. mzML) and native vendor (e.g. Thermo, Bruker) data formats can be imported in MZmine 3. All the supported formats are listed here (LINK to Doc). For more details see the [Data import](../../module_docs/dataimport/data-import.md#lc-ms-data) module.

### Mass detection
- Obtain a list of all the mass that were detected
- For more details see the [Mass detection](../../module_docs/massdetection/mass-detection.md) module.


## Feature processing
The goal of the "Feature processing" is to turn into features (i.e. RT and m/z).

### Chromatogram building
The first step in the "Feature processing" is to build the so-called extracted ion chromatograms (EICs) for each detected mass (see "Mass detection").
There are two modules in MZmine 3 that can fulfil this task: [ADAP chromatogram builder](../../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md) (widely used) and **Grid mass** (create docs).

### Smoothing in retention time dimension (optional)

[Smoothing](../../module_docs/smoothing/smoothing.md)

### Feature resolving

[Local minimum resolver](../../module_docs/localminimumresolver/local-minimum-resolver.md)

## Page Contributors

{{ git_page_authors }}
