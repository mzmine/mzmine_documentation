# Refine IMS-MS2 spectra

:material-menu-open: **Feature list methods → Processing → Refine IMS-MS2 spectra**

Cleans up merged PASEF MS/MS spectra of ion mobility features. Merged MS2 spectra are built by
summing many individual mobility scans, which also accumulates noise: a signal that appears in a
single mobility scan only, or at an intensity close to the detection limit, ends up in the merged
spectrum next to the real fragments.

This module offers two independent refinements that can be combined.

!!! tip

    Run this module after [MS2 scan pairing](../featdet_ms2_scan_pairing/ms2_scan_pairing.md) and
    before spectral library search or spectral library generation, so all downstream steps use the
    refined spectra.

!!! info

    This module was added when the **Minimum number of mobility peaks parameter** did not exist in 
    the MS2 scan pairing module. Setting the minimum number of mobility peaks in the MS2 scan pairing
    module is equivalent to setting the same parameter here.

---

## Parameters

#### Feature lists

The feature lists to process.

#### Intensity-to-noise factor _(Optional)_

Applies a *factor of lowest signal* mass detection to each merged MS/MS spectrum: all signals below
`factor × lowest signal intensity` are removed.

Default is 2.5. Higher values remove more signals.

#### Minimum number of mobility peaks _(Optional)_

Requires a signal to be detected in at least this many individual mobility scans before it is
retained. The merged spectrum is rebuilt from its source mobility scans with this constraint
applied, which removes single-scan spikes.

Disabled by default.

!!! warning

    Unlike the intensity-to-noise factor, this option replaces the merged MS/MS spectra of the
    feature. Merged spectra that end up without any signal are dropped from the feature.

---

{{ git_page_authors }}
