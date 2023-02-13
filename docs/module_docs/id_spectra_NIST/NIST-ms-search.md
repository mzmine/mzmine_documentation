# **NIST MS search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search spectra → NIST MS Search**

or, for an individual row in a feature table

:material-menu-open: highlight the row, right-click on the selection and choose ** Search → NIST MS Search** from the pop-up menu.

This module allows searching spectra against spectral libraries using the **NIST MS Search program**, which accepts spectra as input to its searches. 

The MS level may be specified to limit a search to MS/MS fragment spectra, clustered spectra produced from any Spectral Deconvolution module, or MS1 precursors ions. The spectra will be searched using the default library search parameters in the NIST MS Search program. 

To adjust these parameters: open the NIST MS Search software and adjust the library search parameters: **Options or Icon → Library Search Options → Search: enable automation → Libraries: choose the preferred libraries**.
More information about the libraries and their abbreviations: https://www.nist.gov/srd/nist-standard-reference-database-1a

Save the configuration to a ***.ini** file. 


:material-lightbulb: Automation must be enabled in the library search options to enable automatic searching. Be sure all appropriate libraries are included before starting a search.


Repeated MS/MS spectra may be merged between multiple data files using the Merge MS/MS (experimental) module. The input Mass list filters the fragment ions by intensity, and repeatable signals are assessed via cosine dot product.

### **Requirements**

This module relies on the installed NIST MS Search software, which is currently **only available for Microsoft Windows**.

## **Parameters**

#### **NIST MS Search directory**

Full path to the directory containing the NIST MS Search executable (**nistms$.exe**).

#### **MS level**

MS spectra level for searching. 

Use MS level = 1 to search for MS1 spectra or ADAP-GC clustered spectra produced from Spectral Deconvolution modules.

#### **Min cosine similarity**

The minimum cosine similarity score (dot product) for identification.

#### **Merge MS/MS (experimental)**

_Optional parameter._ 

Merge multiple high-quality MS/MS spectra into consensus feature instead of using the most intense one. 

More details are available [here](../io/merge_ms2_kai.md).

#### **Integer m/z**

_Optional parameter_. 

Merging mode for fractional m/z to unit mass. Converts accurate mass m/z measurements to low-resolution integer values.

Available options are Sum or Maximum.

#### **Spectrum Import**

Options for import, can be by either **Overwrite** (overwriting previous spectra) or **Append** (appending new ones).

{{ git_page_authors }}