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

### Set quantifier masses
mzmine automatically selects the quantifier mass based on the intensity of the MRM transitions and sets the most intense ion as a quantifier. If other ions shall be used as quantifiers, this module allows the selection.
[mrm-set-quant-mass.md](../../module_docs/mrm_setquant/mrm-set-quant-mass.md)

### Smoothing in retention time dimension (optional)
Depending on the LC peak shape (i.e. data noisiness), the user can perform smoothing in retention time dimension. 

### Feature resolving
Feature resolving step enables separation of co-eluting and overlapping chromatography peaks and as such is one of the pivotal steps in data preprocessing. For more detalis on the algorithm used and parameters settings, see the [Local minimum resolver](../../module_docs/featdet_resolver_local_minimum/local-minimum-resolver.md) module.

### Feature alignment

mzmine offers a specific alignment module for MRM data. The [MRM aligner](../../module_docs/align_mrm/mrm-aligner.md) takes the transitions of a feature into account and only allows alignment of features with the same transitions (in default settings). In principle, MRM feature lists can be aligned to HRMS feature lists using the [Join aligner](../../module_docs/align_join_aligner/join_aligner.md). For downsides of this procedure, see the [the MRM aligner documentation](../../module_docs/align_mrm/mrm-aligner.md#mrm-aligner)

---

{{ git_page_authors }}
