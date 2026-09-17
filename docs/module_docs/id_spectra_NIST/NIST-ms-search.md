# **NIST MS search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search spectra → NIST MS Search**

or, for an individual row in a feature table

:material-menu-open: highlight the row, right-click on the selection and choose **Search → NIST MS Search** from the pop-up menu.

!!! danger

    As of mzmine ≥4.10, this module no longer drives the interactive NIST MS Search GUI. It now runs
    NIST's command line program **MSPepSearch** directly, so the workflow described below replaced
    the previous **.ini**-file / GUI-automation based one. Batch steps saved with an older mzmine
    version are migrated automatically: the search type is set to Automatic and the module message
    on first opening the dialog explains what changed.

This module searches feature spectra against the libraries of a licensed NIST installation, using
NIST's command line program **MSPepSearch**. It supports two kinds of workflows:

- **GC-EI**: unit mass electron ionization spectra (or pseudo spectra produced by a
  [Spectral deconvolution](../featdet_spectraldeconvolutiongc/spectraldeconvolutiongc.md) module)
  searched against the NIST EI libraries (`mainlib`, `replib`).
- **MS/MS**: accurate mass tandem spectra searched against the NIST tandem libraries
  (`hr_msms_nist`, `lr_msms_nist`, `apci_msms_nist`).

Every library of the required content found in the installation is searched, so libraries do not
have to be picked by hand. The search type actually used is written to the log and shown in the
task description.

!!! warning

    Requires a licensed NIST installation of NIST 17 or newer. NIST returns no library spectra or
    structures to mzmine, so the mirror plot only shows the input (query) spectrum. Contact
    [mzio.io/nist](https://mzio.io/nist/) to obtain the latest NIST library.

### **Requirements**

This module relies on an installed NIST MS Search / MSPepSearch installation, which is currently
**only available for Microsoft Windows**.

## **Parameters**

The setup dialog groups parameters into **General** (always shown), **MS/MS-specific**, and
**GC-EI-MS-specific**, since only one of the two tolerance/merging groups applies depending on the
selected search type. A **Presets** button offers the two recommended workflow configurations
("GC-EI (low resolution)" and "MS/MS (high resolution)") as a starting point; applying a preset
keeps the installation directory but resets the feature list selection.

#### **Feature lists**

The feature lists to search.

#### **NIST installation directory**

The NIST installation directory, for example `C:\NIST26`. It must contain the `MSPepSearch`
subdirectory with `MSPepSearch64.exe` and the library subdirectories, such as `mainlib` or
`hr_msms_nist`. Use the search button next to the field to detect an installation automatically
(drive roots and common program folders are scanned).

#### **Search type**

The NIST search preset to use. It also picks the libraries and decides which of the parameters
below apply:

- **Automatic** _(default)_ — GC-EI identity if the feature list was built by a spectral
  deconvolution module, MS/MS otherwise.
- **GC-EI identity** — unit mass EI spectra against the EI libraries, to find the compound itself.
- **GC-EI similarity** — the same, but also finds related compounds that are not in the library
  themselves.
- **MS/MS** — accurate mass spectra against the tandem libraries.

#### **Merge & select fragment scans**

Controls how fragment spectra are filtered, merged, and selected before searching (see
[detailed description](../filter_scan_merge_select/scan_merge_select.md)). Repeated MS/MS
spectra may be merged across multiple data files this way instead of using only the most intense
one.

#### **Min cosine similarity**

The minimum similarity score of a reported hit, on mzmine's 0 to 1 scale (this is the NIST match
factor divided by 1000). 0.7 and above is usually considered a good match, 0.9 and above an
excellent one. Default: 0.7 (GC-EI preset: 0.75).

#### **Precursor m/z tolerance** _(MS/MS-specific)_

MS/MS searches only, ignored by the GC-EI searches. How far the precursor m/z of a library entry
may differ from the searched spectrum. It only decides which library entries are compared and does
not enter the match factor itself. MSPepSearch takes a single value, so this is either an absolute
or a relative (ppm) tolerance, never the maximum of both. Default: 20 ppm.

#### **Fragment m/z tolerance** _(MS/MS-specific)_

MS/MS searches only. The product ion m/z uncertainty; unlike the precursor tolerance this one
decides which signals count as matched and therefore the match factor itself. NIST recommends 20
ppm or less. Single value for the same reason as the precursor tolerance. Default: 20 ppm.

#### **Integer m/z** _(GC-EI-MS-specific)_

GC-EI searches only, ignored by the MS/MS search. How signals of the same nominal mass are combined
before searching, because the NIST EI libraries are unit mass:

- **Sum** _(default)_ — adds their intensities, matching how a unit mass library spectrum reports a
  nominal mass; needed for accurate mass GC data (GC-QTOF, GC-Orbitrap).
- **Maximum** — keeps only the most intense signal of the nominal mass.

Unit mass quadrupole data has one signal per nominal mass, so both options are equivalent there.

{{ git_page_authors }}