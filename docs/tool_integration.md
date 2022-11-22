# Integration to other tools

## Overview

| **Tool** | **Doc** | **MZmine module** | **Format** | **Description** |
|---|---|---|---|---|
| [SIRIUS](https://bio.informatik.uni-jena.de/software/sirius/) |  | Export to SIRIUS | .mgf | Contains MS2 spectra and MS1 or correlated MS1 spectra for each feature list row |
| [GNPS-FBMN](https://www.nature.com/articles/s41592-020-0933-6)<br>[GNPS-IIMN](https://www.nature.com/articles/s41467-021-23953-9) | [FBMN](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking-with-mzmine2/)<br>[IIMN](https://ccms-ucsd.github.io/GNPSDocumentation/fbmn-iin/) | Export/submit GNPS-FBMN | .mgf<br>_quant.csv<br>_edges.csv | - Contains one representative MS2 spectrum per feature<br>- The feature list as an intensity (area/height) matrix<br>- The additional IIN edges between features |
| [GNPS-GC-MS](https://ccms-ucsd.github.io/GNPSDocumentation/gcanalysis/) | [Doc](https://ccms-ucsd.github.io/GNPSDocumentation/gc-ms-deconvolution/#gc-ms-data-processing-with-adap-mzmine) | Export to GNPS-GC-MS | .mgf<br>_quant.csv | - Contains one representative correlated GC-MS1 spectrum per feature<br>- The feature list as an intensity (area/height) matrix |
| [MetaboAnalyst](https://www.metaboanalyst.ca/) |  | Export to MetaboAnalyst | .csv | Metadata grouped feature intensity matrix (area/height) |
| R, Python<br>general purpose export  |  | Export to CSV (legacy)<br>Export to CSV (modular) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format.<br>Export all columns from the feature table to a tabular format. |
| [tidyMass](https://github.com/tidymass/tidymass) | [Doc](https://www.tidymass.org/start/create_mass_dataset/#mzmine-feature-table-to-mass_dataset-class) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |
| [MetDNA](http://metdna.zhulab.cn/) | [Doc](https://github.com/ZhuMetLab/MetDNA2_Web/blob/main/Tutorials/Tutorial_data_preprocessing_MZmine.pdf) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |
| [NeatMS](https://github.com/bihealth/NeatMS) | [Doc](https://neatms.readthedocs.io/en/latest/first-steps/data-format/) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |
| [mzRAPP](https://github.com/YasinEl/mzRAPP#exporting-npp-outputs-from-different-tools) | [Doc](https://github.com/YasinEl/mzRAPP#exporting-npp-outputs-from-different-tools) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |




## Page Contributors

{{ git_page_authors }}
