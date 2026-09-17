# Clear retention time correction on scans

:material-menu-open: **Feature list methods → Normalization → Clear Retention time correction on scans**

Removes any retention time correction previously applied to the scans of the selected raw data
files by the
[Retention time correction of scans](../norm_rt_calibration_scans/scan-based-rt-corr.md) module,
restoring their original, uncorrected scan retention times.

This module is mostly used internally: the
[ADAP chromatogram builder](../lc-ms_featdet/featdet_adap_chromatogram_builder/adap-chromatogram-builder.md)
and the
[Retention time correction of scans](../norm_rt_calibration_scans/scan-based-rt-corr.md) module
itself can clear a previous correction automatically through their own **Clear previous RT
corrections** parameter. Use this module directly when you want to reset the scan retention times
of a set of raw data files without immediately re-running one of those steps.

!!! warning

    Applying this module to data files after feature lists have already been generated from them
    will lead to mismatches between the (now uncorrected) scan retention times and the retention
    times stored in those feature lists. Existing feature lists are not updated. To avoid this,
    remove the affected feature lists after clearing the correction and reprocess the raw data
    files from scratch.

---

## Parameters

#### Raw data files

The raw data files whose scan retention times shall be reset to their original, uncorrected values.

---

{{ git_page_authors }}
