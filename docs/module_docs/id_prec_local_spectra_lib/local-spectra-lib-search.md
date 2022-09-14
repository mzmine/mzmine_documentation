# **Precursor search in local spectral MS/MS library**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search precursor mass → Precursor search in spectral libraries**

This module uses a **local spectral MS/MS library** to search for putative precursor ions in a feature list.  

**Supported formats:** 

- MoNA *.json, 
- NIST *.msp, 
- GNPS *.json (internal library submission format), 
- and JCAMP-DX *.jdx.

## **Parameters**

**Spectral libraries file (MS/MS)**

Name of the library file of the supported format.

**Precursor m/z tolerance**

Matches the average row m/z against the precursor m/z of the spectral library entry

**Retention time tolerance**

_Optional parameter_, should only be used if the DB entry has a retention time