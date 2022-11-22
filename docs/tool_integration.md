# Integration to other tools

## Overview

| **Tool** | **Doc** | **MZmine module** | **Format** | **Description** |
|---|---|---|---|---|
| SIRIUS |  | Export to SIRIUS | .mgf | Contains MS2 spectra and MS1 or correlated MS1 spectra for each feature list row |
| GNPS-FBMN<br>GNPS-IIMN |  | Export/submit GNPS-FBMN | .mgf<br>_quant.csv<br>_edges.csv | - Contains one representative MS2 spectrum per feature<br>- The feature list as an intensity (area/height) matrix<br>- The additional IIN edges between features |
| MetaboAnalyst |  | Export to MetaboAnalyst | .csv | Metadata grouped feature intensity matrix (area/height) |
| R, Python<br>general purpose export  |  | Export to CSV (legacy)<br>Export to CSV (modular) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format.<br>Export all columns from the feature table to a tabular format. |
| tidyMass | [Doc](https://www.tidymass.org/start/create_mass_dataset/#mzmine-feature-table-to-mass_dataset-class) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |
| MetDNA | [Doc](https://github.com/ZhuMetLab/MetDNA2_Web/blob/main/Tutorials/Tutorial_data_preprocessing_MZmine.pdf) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |
| [NeatMS](https://github.com/bihealth/NeatMS) | [Doc](https://neatms.readthedocs.io/en/latest/first-steps/data-format/) | Export to CSV (legacy) | .csv | Export any row (averaged) and feature (per sample) types to a tabular format |




## Page Contributors

{{ git_page_authors }}
