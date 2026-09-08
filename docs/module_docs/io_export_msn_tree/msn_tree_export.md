# Export MSn trees

:material-menu-open: **Raw data methods → Raw data export → Export MSn trees**

Exports all MSn fragmentation trees of the selected raw data files into a single tabular file. An
MSn tree groups all fragmentation spectra that originate from the same MS1 precursor, following the
precursor chain over MS2, MS3, and higher levels.

This export works directly on the raw data and does not require feature detection. It is intended
for the inspection and downstream analysis of MSn acquisition experiments, for example to check how
deep and how broad the fragmentation trees of a method actually are. To build features from MSn
trees instead, use the [MSn tree builder](../featuredet_msn_tree/msn_tree_builder.md).

!!! warning

    [Mass detection](../featdet_mass_detection/mass-detection.md) must be run on all MS levels
    before this export. Without a mass list the task fails with a missing mass list error.

One line is written per fragmentation spectrum. Each line repeats the summary values of the tree it
belongs to, so single lines can be filtered without losing the tree context.

## Exported columns

| Column | Description |
|---|---|
| `FILENAME` | Raw data file the spectrum comes from |
| `SCAN_NUMBER` | Scan number of the spectrum |
| `TREE_ID` | Running number of the MSn tree, counted across all exported files |
| `MS_LEVEL` | MS level of the spectrum |
| `PRECURSOR_MZ` | Precursor *m/z* of this spectrum |
| `PRECURSOR_MS2` | Root precursor of the tree, i.e. the MS2 precursor |
| `PRECURSOR_LIST` | Full precursor chain leading to this spectrum, from the root down |
| `N_SIGNALS` | Number of signals in the mass list of this spectrum |
| `MAX_MSN` | Highest MS level reached in this tree |
| `N_PREC` | Total number of precursors in the tree |
| `N_PREC_MS3` … `N_PREC_MS6` | Number of precursors fragmented on the respective level |
| `N_SPEC` | Total number of spectra in the tree |
| `N_MS2` … `N_MS6` | Number of spectra per MS level in the tree |
| `MZS`, `INTENSITIES` | Comma-separated signal lists of the spectrum |

---

## Parameters

#### Raw data files

The raw data files to export.

#### Filename

Name of the output file, `.tsv` or `.csv`. Use the pattern `{}` in the file name to substitute the
raw data file name. An existing file is overwritten.

#### Separator

Character used to separate fields. Default is a tab, matching the default `.tsv` extension. Note
that the signal lists in `MZS` and `INTENSITIES` always use a comma internally.

#### m/z tolerance

Tolerance used to link fragmentation spectra to their precursor when building the MSn trees.
Default is 0.001 Da or 5 ppm.

!!! tip

    Use a tolerance that reflects the precursor isolation accuracy of your instrument. A tolerance
    that is too narrow splits one tree into several, a tolerance that is too wide merges unrelated
    precursors into one tree.

---

{{ git_page_authors }}
