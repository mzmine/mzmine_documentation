# **GNPS-FBMN/IIMN export**

## **Description**

:material-menu-open:  **Feature list methods → Export feature lists → GNPS - feature based molecular networking**.

This module connects MZmine feature finding results to the [GNPS](https://gnps.ucsd.edu/) workflows for [Feature-based Molecular Networking (FBMN)](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking/) and [Ion Identity Molecular Networking (IIMN)](https://ccms-ucsd.github.io/GNPSDocumentation/fbmn-iin).

![](gnps_export.png)

Using this module, the user can export the feature list needed for the manual submission to GNPS' feature based molecular networking (GNPS FBMN) or directly submit the job to the GNPS platform from MZmine. In both cases, two files are created: 

1. Quantification table (CSV file) which contains the features and their associated information (e.g., average m/z, retention time, and each feature's area or height).
2. MS/MS spectral summary (.MGF file) which contains one representative MS/MS spectrum for each row in the feature list. 
3. A [supplementary edges file](https://ccms-ucsd.github.io/GNPSDocumentation/fbmn-iin/#supplementary-pairs) with related ion identities (if ion identity networking was performed).

## **References**

!!! quote " "

    **IIMN:** Schmid R., Petras D., Nothias LF, et al. [Ion Identity Molecular Networking for mass spectrometry-based metabolomics in the GNPS Environment](https://www.nature.com/articles/s41467-021-23953-9). Nat. Comm. 12, 3832 (2021).

    **FBMN:** Nothias, L.-F., Petras, D., Schmid, R. et al. [Feature-based molecular networking in the GNPS analysis environment](https://www.nature.com/articles/s41592-020-0933-6). Nat. Methods 17, 905–908 (2020).

    **GNPS:** Wang, M. et al. [Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking](https://doi.org/10.1038/nbt.3597). Nat. Biotechnol. 34, 828–837 (2016).


### **Parameters**

#### **Filename**
Name to be given to the output files (.MGF and .CSV). In this field, the user can either write the path where they want to save the file, or click "select", navigate into the desired output folder, write the output name in the "file name" field and click save. Once that is done, the path should be visible in the Filename field in the GNPS export module.

#### **Merge MS/MS (experimental)**
If checked, high quality MS/MS spectra that correspond to one feature are merged, instead of exporting only the most intense MS/MS spectrum. See [MS/MS merger](merge_ms2_kai.md) for additional information.

#### **Filter rows**
In the final output files, the user can select to export all the rows without any filters applied, rows only with MS/MS spectra, rows with MS/MS and Ion Identity (it gives MS/MS and the adduct information) and rows with MS/MS or Ion Identity. Normally, for FBMN you want to retain features with MS/MS spectra.

#### **Feature intensity**
The user can either select peak area or peak height which will then be displayed in the quantification table.

#### **CSV export**
The user can choose between **simple**, **comprehensive**, or **all**. Difference is in the amount of information that is present in the quantification table. Simple resembles the legacy format from the MZmine 2 export. Both options can be used for FBMN in GNPS other tools might rely on the simple MZmine 2 style output. 

#### **Submit to GNPS**
This option allows any user to directly submit FBMN/IIMN jobs to GNPS. The password and user name are optional and are sent without encryption (until the server has moved to its final location with https).
The input files uploaded to GNPS with the "Submit to GNPS" option are not saved on your GNPS user account. These files are deleted on monthly basis, which prevent future cloning of the job and retrieval of the files. Use the "standard" interface of FBMN for persistant jobs and more options. Or log into your GNPS account and click on **Clone to latest version** for a job submitted via direct interface. 

#### **Open folder**
Opens the export folder.


