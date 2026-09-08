# MS2 quality export

:material-menu-open: **Tools → Libraries → MS2 quality export**

Exports a set of quality metrics for individual MS/MS spectra to a tabular file. The module is used
during spectral library generation and method development to judge how clean and how informative the
acquired fragmentation spectra are, for example when comparing acquisition settings or SIMSEF
schedules.

!!! warning

    This module currently only evaluates **PASEF MS/MS spectra of ion mobility features**. Features
    from non-IMS data, and merged spectra that are not single PASEF spectra, are skipped without
    producing a line in the output. Run
    [MS2 scan pairing](../featdet_ms2_scan_pairing/ms2_scan_pairing.md) or
    [MALDI MS2 scan pairing](../featdet_ms2_scan_pairing/ms2_maldi_scan_pairing.md) first, so the
    features carry their fragmentation spectra.

One line is written per MS/MS spectrum. Fields are separated by a semicolon (`;`).

## Exported columns

| Column | Description |
|---|---|
| `feature_list` | Name of the feature list the spectrum belongs to |
| `row_id` | ID of the feature list row |
| `compound`, `adduct` | Compound name and adduct of the best annotation |
| `purity_score` | Isolation purity: precursor intensity divided by the total intensity inside the isolation window in *m/z* and mobility, evaluated on the corresponding MS1 frame |
| `explained_intensity`, `explained_peaks` | Fraction of MS2 intensity and of MS2 signals that can be explained by a sub formula of the annotated molecular formula |
| `num_peaks` | Number of signals in the spectrum |
| `spectral_entropy`, `normalized_entropy`, `weighted_entropy`, `normalized_weighted_entropy` | Spectral entropy measures describing the information content of the spectrum |
| `tic_ms2`, `bpi_ms2` | Total ion current and base peak intensity of the MS2 spectrum |
| `precursor_intensity` | Summed precursor intensity of the contributing MS1 scans |
| `spots` | MALDI spot names contributing to the merged spectrum (imaging / SIMSEF data) |
| `mobility_range` | Mobility range that was isolated for fragmentation |
| `precursor_mz` | Isolation *m/z* |
| `collision_energy` | Collision energies of the merged spectrum |

!!! tip

    `explained_intensity` and `explained_peaks` are only meaningful if the annotation provides a
    molecular formula. Spectra without a formula are still exported, but the two columns are 0.

---

## Parameters

#### Feature lists

The feature lists to evaluate.

#### Export File

Target file. An existing file is overwritten.

#### Only compound matches

If enabled (default), only features with a compound annotation that carries a molecular formula are
exported. Disable to evaluate all fragmented features.

#### Sub formula m/z tolerance

Tolerance used to assign sub formulas of the annotated molecular formula to MS/MS signals when
calculating `explained_intensity` and `explained_peaks`. Default is 0.003 Da or 10 ppm.

#### Match compound name to feature list name

If enabled, only spectra whose annotated compound name is contained in the name of the feature list
are exported. This is useful for library generation workflows in which one feature list is created
per measured standard and named after that standard.

---

{{ git_page_authors }}
