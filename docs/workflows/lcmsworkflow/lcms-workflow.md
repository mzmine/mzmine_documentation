# LC-MS Workflow
The following workflow is intended to turn raw LC-MS data into a table of all the detected featuresand the corrisponding signal intensity recorded in each sample. A simplified version of the workflow is shown below:

![workflow-image](https://github.com/titodamiani/mzmine_documentation/blob/215a9bf2df1647c4588cfd978b7e834acbe548b5/docs/workflows/lcmsworkflow/workflow_image.png)


## Raw data processing
  
### Raw data import
Either open (e.g. mzML) and native vendor (e.g. Thermo, Bruker) data formats can be imported in MZmine 3. All the supported formats are listed here (LINK to Doc). For more details see [Data import module](../../module_docs/dataimport/data-import.md#lc-ms-data).

### Mass detection

[Mass detection](../../module_docs/massdetection/mass-detection.md)

## Feature processing

After raw data processing, the first step of feature detection is building extracted ion
chromatograms (EICs). This step can be executed by the **ADAP chromatogram builder** or **Grid
mass**.

### ADAP chromatogram builder

[ADAP Documentation](../../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md)

### Smoothing in retention time dimension (optional)

[Smoothing](../../module_docs/smoothing/smoothing.md)

### Feature resolving

[Local minimum resolver](../../module_docs/localminimumresolver/local-minimum-resolver.md)

## Page Contributors

{{ git_page_authors }}
