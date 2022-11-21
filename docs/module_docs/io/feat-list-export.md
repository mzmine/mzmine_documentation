# **Feature list export modules**

This section describes general format export modules. For the description of export modules for the specific software, please, refer to [Data export to other software](data-exchange-with-other-software.md).

## **CSV**

### **Description**

:material-menu-open: **Feature list methods → Export feature list → CSV**

This module allows to export obtained feature lists to csv (comma-separated values) file format.

### **Parameters**

#### **Field separator**

Character(s) used to separate fields in the exported file. "," by default.

#### **Identification separator**

Character(s) used to separate multi object columns in the exported file. ";" by default.

#### **Remove empty columns**
_Optional parameter_

Removes empty columns during data export.

#### **Filter rows**

Allows user to export only those rows that have associated MS/MS data or are annotated. 

## **CSV (legacy MZmine 2)**

### **Description**

:material-menu-open: **Feature list methods → Export feature list → CSV (legacy MZmine 2)**

This module is a legacy module from MZmine2 and, similarly to the previously described module, exports the contents of the feature list(s) into a csv file, which can later be processed by MS Excel or other tools. The produced CSV files cannot be imported back to MZmine. Missing values such as heights and areas of undetected features are exported as 0.

### **Parameters**

#### **Filename**

Name of file where the exported data is saved

#### **Field separator**

Columns in the new CSV file will be separated by this character (coma by default)

#### **Export common elements**

Which row elements (such as row ID, row retention time, or best ion annotation) from the feature list will be exported 

#### **Export data file elements**

Which feature elements (such as feature status, name, or tailing factor) will be exported.

#### **Export quantitation results and other information**
_Optional parameter_

If checked, all feature-associated data will be exported.

#### **Identification separator**

Character to separate multiple identification results (if they are available) for a feature. 

#### **Filter rows**

Allows user to export only those rows that have associated MS/MS data or are annotated. 

## **Venn diagram export**

## **Description**

:material-menu-open: **Feature list methods → Export feature list → Venn diagram export**

Exports a feature list to a csv that can be plotted as a venn diagram by other software such as [VennDis](https://pubmed.ncbi.nlm.nih.gov/25545689/) or [VENNY](https://bioinfogp.cnb.csic.es/tools/venny/).

## **Parameters**

#### **Directory**

Choose a directory to export the feature list to.

#### **Export gap filled as detected**
_Optional parameter_

If checked, gap filled features will be exported as detected, otherwise they will be marked as undetected.



