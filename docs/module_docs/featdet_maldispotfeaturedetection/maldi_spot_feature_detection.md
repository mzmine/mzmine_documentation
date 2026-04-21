# MALDI spot feature detection

## Description

:material-menu-open: **Feature list methods → Feature detection → MALDI spot feature detection**

This module detects features in MALDI dried-droplet spots directly from native **timsTOF fleX**
imaging data (`.d` folder). It only works with imaging raw data files acquired with this instrument.

For each MALDI spot found in the data, a separate feature list is produced. Every signal in the
spot's frame spectrum that exceeds the **Minimum intensity** threshold is recorded as an individual
feature row. This gives one feature per detected m/z per spot, allowing downstream modules (spectral
library matching, formula prediction, etc.) to be applied on a per-spot basis.

If the raw data were acquired with ion mobility (timsTOF fleX TIMS mode), the detected features are
automatically expanded into the mobility dimension by running
the [IMS Expander](../lc-ims-ms_featdet/featdet_ims_expander/ims-expander.md) internally for each
spot feature list using the same m/z tolerance.

!!! warning

    Mass detection must be run before this module. Features are detected from the processed mass list, not from the raw spectral data.

## Parameters

#### Raw data files

The raw data files to process.

#### m/z tolerance

m/z tolerance used to group data points during IMS expansion (for timsTOF fleX data with TIMS).
Default: ±0.005 Da or ±15 ppm (whichever is larger).

#### Minimum intensity

Minimum intensity a signal must reach in the frame spectrum to be detected as a feature. Data points
below this threshold are not processed. Default: 5,000.

#### Spot sample names _(Optional)_

Path to a semicolon-delimited CSV file (`.csv`) that maps MALDI spot identifiers to human-readable
sample names. The file must contain at least two columns with headers `spot` and `name` (
case-insensitive). Additional columns are ignored.

Each spot's feature list is named `<name> - <spotId>`. If no mapping file is provided, or if a spot
identifier is not found in the file, the raw data file name is used as the prefix instead.

**Example CSV content:**

```
spot;name;treatment
A1;Control_1;blank
B2;Sample_A;compound_X
```

## Output

One feature list is created per MALDI spot in the data. The feature list name follows the pattern
`<sampleName> - <spotId>`, where `<sampleName>` comes from the spot name mapping file (or the raw
data file name as fallback) and `<spotId>` is the spot identifier recorded in the raw data.

For IMS data, each feature list entry contains a mobilogram (intensity vs. mobility profile) in
addition to the MS1 signal.

---

{{ git_page_authors }}
