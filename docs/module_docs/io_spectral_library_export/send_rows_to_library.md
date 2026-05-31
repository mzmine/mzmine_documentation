# **Send annotated rows to spectral library**

## **Description**

:material-menu-open: **Feature list context menu → Send annotated rows to spectral library**

This module adds annotated feature list rows to a spectral library within the current MZmine
project. It reuses the same entry-generation engine as
[Batch spectral library generation](spectral_library_generation.md) but writes entries to an
in-memory library instead of a file. The library can then be exported or edited with the
[Spectral library editor](../spectral_library_editor/spectral_library_editor.md).

Only **identified rows** (rows with at least one annotation) are processed. For each
annotated row, fragment scans are selected, quality-checked, and converted into library entries.
Sequential entry IDs are assigned automatically, starting after the highest existing integer ID in
the target library.

## Workflow

### Step 1 -- Select rows

Select one or more annotated feature list rows in the feature table, then choose
**Send annotated rows to spectral library** from the context menu.

### Step 2 -- Choose or create a target library

A dialog appears with two options:

- **Add to existing library** -- choose from a dropdown of libraries already imported in the
  project. This option is disabled when no libraries are available.
- **Create new library** -- enter a name for a new library. The feature list name is suggested as
  the default.

!!! tip

    Creating a new library keeps your manually curated entries separate from batch-generated
    libraries, making it easier to track provenance.

### Step 3 -- Configure entry generation parameters

After selecting the library, a parameter dialog appears with the same settings used for batch
library generation. See the parameter descriptions below.

### Step 4 -- Generated entries are added to the project

The task runs in the background. When finished, the entries are added to the target library and the
library is registered in (or updated within) the current project.

---

## Parameters

The parameter dialog is a subset of the
[Batch spectral library generation](spectral_library_generation.md) parameters. It shares the same
defaults and behavior for all included settings.

#### **Metadata**

Global metadata applied to every generated entry. Includes fields such as acquisition type,
instrument, ion source, principal investigator, description, and more. See
[Batch spectral library generation → Metadata](spectral_library_generation.md#metadata) for details
on each field.

#### **Intensity normalizer**

Controls how signal intensities are written into the generated entries.

- **Original intensities** (default since v4.4.3) -- preserves measured intensity values.
- **Normalize to 100%** -- scales the most intense signal to 100.

#### **Merge & select fragment scans**

Controls how fragment spectra are filtered, merged, and selected before entry creation (see
[detailed description](../filter_scan_merge_select/scan_merge_select.md)). The recommended preset
for library generation is **Representative scans or MSn tree**.

#### **Handle chimeric spectra** _(Optional)_

When enabled, MS1 scans are inspected for co-isolated precursors within the isolation window.
Chimeric spectra can be skipped entirely or flagged in the entry metadata.

See [Batch spectral library generation → Handle chimeric spectra](spectral_library_generation.md)
for sub-parameter details (target ion tolerance, isolation tolerance, minimum purity).

### Quality parameters

Quality thresholds that spectra must pass before an entry is created. Spectra that do not meet
these criteria are silently skipped.

#### **Minimum number of signals** _(Optional)_

Minimum number of peaks an MS/MS spectrum must contain. Default: **3**.

:material-lightbulb: The optimal value depends on the fragmentation richness of the compounds in
your library. At least 3 signals is a good starting point for diverse compound sets.

#### **Minimum explained signals (%)** _(Optional)_

Minimum percentage of signals that can be assigned to a molecular subformula. Default: **40%**.

#### **Minimum explained intensity (%)** _(Optional)_

Minimum percentage of total spectrum intensity that can be explained by subformula assignments.
Default: **40%**.

:material-lightbulb: This threshold emphasizes high-abundance signals. We recommend setting this
before the explained-signals threshold, as abundant signals that cannot be explained often indicate
quality issues.

#### **Formula m/z tolerance**

The _m/z_ tolerance used to match MS/MS signals to subformulas derived from the molecular formula.
Default: **0.003 _m/z_** or **10 ppm** (whichever is larger).

#### **Export explained signals only**

When enabled, only signals that match a subformula within the tolerance are included in the
generated entry. Default: **off**.

#### **Feature list name match only**

When enabled, an entry is only generated if the compound annotation name is contained in the feature
list name. This is useful when building libraries from standard mixtures where the feature list name
reflects the compound identity. Default: **off**.

### Advanced parameters

#### **Compact USI** _(Optional)_

When enabled, Universal Spectrum Identifiers are written in a compact scan-range format
(e.g., `1-5,9`) instead of one USI per scan. This reduces file size but has limited compatibility
with external tools. Default: **off**.

---

## Algorithm {#algorithm}

The module delegates entry creation to the same engine used by
[Batch spectral library generation](spectral_library_generation.md). For each selected row:

1. Fragment scans are extracted from the row.
2. Annotations are filtered by the quality checker and optional name matching.
3. Chimeric precursors are detected if enabled.
4. Scans are selected, merged, and filtered according to the spectrum-merging preset.
5. For each annotation/scan combination, signals are matched against the molecular formula and
   quality thresholds are applied.
6. Passing entries receive a sequential `ENTRY_ID` (starting after the maximum existing ID in the
   target library) and are added to the library.

After all rows are processed, the library is added to (or updated in) the current project.

---

{{ git_page_authors }}
