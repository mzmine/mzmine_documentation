# MRM workflow

!!! warning
    To process multiple reaction monitoring (MRM) data, the MRM service of mzmine is required. This is
    included for PRO customers. Academics can reach out to info[at]mzio.io to request a free license.

In contrast to HRMS data, MRM acquisitions are usually stored as chromatograms of specific transitions,
e.g., _m_/_z_ 413 -> 96 instead of full spectra. This is a raw data format, that mzmine is not used 
to handling, since workflows usuallys start with a set of centroided spectra along the retention time.

Therefore, a specific module is required to build scans and chromatograms, which is the [MRM to scans](../../module_docs/mrm_mrmtoscans/mrm-to-scans.md) module.

## Workflow

### Import raw data
Raw data is import in the usual fashion see [data import](../../module_docs/io/data-import.md).

### MRM to scans
The imported raw data is converted using the [MRM to scans](../../module_docs/mrm_mrmtoscans/mrm-to-scans.md)
module. This creates pseudo MS1 and MS2 spectra as well as a feature list, which groups the MRM transitions
by their retention time and precursor ion mass. 
