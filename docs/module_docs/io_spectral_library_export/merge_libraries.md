# Merge & Export Spectral Libraries

## Description

:material-menu-open: **Spectral library methods → Merge & export spectral libraries**

This module combines two or more spectral libraries loaded in the current project into a single
library file. All entries from the selected libraries are written to the new file in sequence.
Optionally, the merged library can be re-imported into the project and the source libraries
removed, effectively replacing them with the combined result.

This is useful for:

- Consolidating a collection of in-house libraries into one file for distribution or search.
- Combining libraries from different instruments or projects before spectral library search.
- Re-numbering or standardising entry IDs across libraries from different sources.

## Parameters

#### Spectral libraries

The libraries to merge. By default the libraries selected in the main window are used.

#### Merged library file

Output file path for the merged library. The file extension is set automatically based on the
chosen export format. Default filename suffix: `merged_library`.

#### Export format

File format for the output library:

| Option                    | Extension | Notes                                               |
|---------------------------|-----------|-----------------------------------------------------|
| mzmine json (recommended) | `.json`   | Full metadata support; default                      |
| NIST msp                  | `.msp`    | Compatible with NIST MS Search and many other tools |
| mgf                       | `.mgf`    | Compatible with GNPS and other tools                |

#### Entry IDs

Controls how entry identifiers are assigned in the merged library. Since different source
libraries may use overlapping ID schemes, this option allows deduplication or full renumbering:

| Option                                   | Behaviour                                                                                           | ID pattern                               |
|------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------|
| **New IDs with dataset IDs** _(default)_ | Assigns new IDs using the entry's `DATASET_ID` field (e.g. MassBank accession prefix)               | `<DATASET_ID>_<n>_id`                    |
| **New IDs with filename**                | Assigns new IDs based on the merged output filename                                                 | `<new_filename>_<n>_id`                  |
| **New IDs with old library name**        | Assigns new IDs prefixed with the source library's filename                                         | `<source_lib_name>_<n>_id`               |
| **Avoid duplicates**                     | Keeps original IDs at their first appearance; resolves clashes with the source library name pattern | `<source_lib_name>_<n>_id` for conflicts |
| **Keep existing IDs**                    | Passes all original IDs through unchanged; duplicates are possible                                  | —                                        |

!!! warning

    **Keep existing IDs** can produce duplicate IDs when libraries from different sources are
    merged. This may cause unexpected behavior in spectral library search. Use one of the
    renumbering options unless you are certain all source IDs are unique across all input libraries.

#### Remove libraries, import merged library _(Optional)_

If enabled, after the export finishes:

1. All selected source libraries are removed from the project (their files on disk are **not**
   deleted).
2. The newly written merged library file is imported back into the project.

This replaces the individual libraries with the merged one in a single step. Disabled by default.

#### Intensity normalization

Optionally normalises fragment intensities before writing each entry:

| Option                           | Behaviour                                 |
|----------------------------------|-------------------------------------------|
| **No normalization** _(default)_ | Original absolute intensities are written |
| **Highest signal as 100%**       | Scales so the base peak = 100             |
| **Highest signal as 1**          | Scales so the base peak = 1               |
| **Sum as 100%**                  | Scales so all intensities sum to 100      |
| **Sum as 1**                     | Scales so all intensities sum to 1        |

Normalisation is applied independently per entry. The output format does not use scientific
notation for intensity values.

---

{{ git_page_authors }}
