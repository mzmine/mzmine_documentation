# Post-column reaction

:material-menu-open: **Feature list methods → Feature grouping → Post Column Reaction**

This module identifies and annotates **transformation products** produced by
post-column reactions in LC-MS experiments. In a post-column reaction setup, a parent compound
with a known database annotation undergoes a chemical transformation after chromatographic
separation. The resulting derivative features co-elute with the parent (correlated
chromatographic profiles) but are absent from unreacted control samples.

The module scans every annotated feature in a feature list and, for each one, looks at its
correlation group for candidate transformation products: features whose chromatographic profile correlates with the
parent above a configurable threshold **and** that are not detected in any of the designated
unreacted raw data files. Matching features receive a compound annotation derived from the
parent name, and their molecular formula can optionally be predicted automatically based on the 
parent compound's formula.

!!! warning "Prerequisites"

    1. **Correlation grouping** (metaCorrelate) must be run on the feature list before this module.
       The module will display a message and exit if no MS1 correlation map is found.
    2. At least one feature in the list must already carry a **compound annotation** (e.g. from a
       database search or manual annotation). Unannotated lists are skipped silently.
    3. All raw data files selected as *unreacted* must be part of the aligned feature list.

---

## Parameters

#### Aligned feature list

The aligned feature list to process. Exactly one feature list can be selected. The list must
include both reacted and unreacted raw data files and must already contain MS1 correlation data
from a previous correlation grouping step.

#### Unreacted raw data files

Raw data files from control (unreacted) analyses. These files are used to distinguish parent
compounds and chemical background — which remain detectable in unreacted samples — from 
transformation products, which are expected to appear **only** in reacted samples. All selected 
files must be present in the chosen feature list.

!!! tip

    Select all control files acquired without post-column reaction. Features detected in any of 
    these files are excluded from transformation product annotation.

#### Predict molecular formulae _(Optional)_

When enabled (default), the module predicts molecular formulae for each transformation product candidate based on
the molecular formula of the parent compound annotation. The search space is derived
automatically from the parent formula by allowing up to **8 additional H and O atoms** for each
candidate, which covers common redox products. Oxygen is always included in the search space (min. 
0–8 atoms) even if the parent formula contains no oxygen.

Formula prediction is run only if the parent annotation carries a valid molecular formula string.

##### Ionization type

Ionization mode used to calculate the neutral mass from the transformation product feature's m/z. Default: `[M+H]+`.

##### *m*/*z* tolerance

Mass accuracy tolerance for formula matching. Default: **0.002 Da or 5 ppm** (whichever is
larger). Adjust to match the mass accuracy of the instrument.

##### Element count heuristics _(Optional)_

Applies heuristic rules to elemental counts and elemental ratios (e.g. H/C, N/C) to filter
chemically implausible formula candidates. Disabled by default. See
[Chemical formula prediction](../id_spectra_chem_formula/chem-formula-pred.md#element-count-heuristics)
for a detailed description of the available rules.

##### RDBE restrictions _(Optional)_

Restricts formula candidates to a specified range of Ring and Double Bond Equivalents (RDBE).
Disabled by default. See
[Chemical formula prediction](../id_spectra_chem_formula/chem-formula-pred.md#rdbe-restrictions)
for details.

##### Isotope pattern filter _(Optional)_

Retains only formula candidates whose predicted isotope pattern matches the observed pattern
within the configured similarity threshold. Disabled by default. See
[Chemical formula prediction](../id_spectra_chem_formula/chem-formula-pred.md#isotope-pattern-score)
for details.

##### MS/MS filter _(Optional)_

Validates formula candidates against the observed MS/MS fragmentation spectrum by checking
whether neutral losses can be explained by the candidate formula. Disabled by default. See
[Chemical formula prediction](../id_spectra_chem_formula/chem-formula-pred.md#msms-filter)
for details.

#### Apply shape correlation threshold _(Optional)_

When enabled (default), only features whose Pearson correlation score with the parent feature
meets or exceeds this threshold are considered as transformation product candidates. This needs to be set in addition
to the threshold defined in the metaCorrelate processing step. Default: **40%**.

!!! tip

    A stricter threshold (e.g. 70–90%) reduces false positives but may miss transformation products with partially
    misaligned peaks. Use a lower threshold when chromatographic peak shapes are noisy or when
    retention times vary across samples.

---

## Algorithm {#algorithm}

1. **Validation** — The module checks that all selected unreacted raw data files are present in
   the feature list. Processing stops with an error message if any file is missing.

2. **Reacted file determination** — Files in the feature list that are *not* in the unreacted
   selection are treated as reacted samples.

3. **Row preparation** — All feature list rows are sorted by *m*/*z*. Rows that carry at least one
   compound annotation are collected as parent candidates.

4. **Correlation map lookup** — For each parent row, the MS1 correlation map (produced by the
   correlation grouping step) is queried for all correlated rows.

5. **Transformation product candidate filtering** — A correlated row is added to the transformation product candidate list if:
    - Its correlation score with the parent is ≥ the configured threshold (or the threshold
      check is disabled), **and**
    - The feature is absent from **all** unreacted raw data files (i.e. no feature is detected
      in any unreacted file for that row).

6. **Annotation** — Each unannotated transformation product candidate receives a `SimpleCompoundDBAnnotation` with:
    - **Precursor *m*/*z***: the average m/z of the transformation product feature.
    - **Compound name** following the pattern `{parentName}_{tpName}_{nominalMZ}` where `parentName` is the name of the parent compound, `tpName` is the name of transformation products chosen by the user and `nominalMZ`
      is the m/z of the transformation product rounded to the nearest integer. If multiple transformation products share the same parent name
      and nominal m/z, a letter suffix is appended: `_TP_195`, `_TP_195a`, `_TP_195b`, …
    - **Molecular formula** (if formula prediction is enabled and a formula was found).

    !!! note
    
        Features that already carry a compound annotation are skipped; existing annotations are
        not overwritten.

7. **Formula prediction (optional)** — If enabled, a formula prediction sub-task is executed
   for all transformation product candidates of each parent before annotation, using the search space derived from
   the parent formula. The best-scoring formula is stored on the transformation product annotation.

---

## Output

The module modifies the input feature list in-place. No new feature list is created.
Newly annotated transformation product features appear in the **Compound annotations** column of the feature list
table with names in the `{parentName}_{tpName}_{nominalMZ}` format. If formula prediction was
enabled, the annotation also carries a predicted molecular formula.

{{ git_page_authors }}
