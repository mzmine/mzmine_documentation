# **Local compound database search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search precursor mass → Local compound
database (CSV) search**

This method assigns identity to features according to their m/z. Additionally, retention time,
mobility, CCS, and retention index (RI) values can be provided to restrict the annotation and
improve the annotation score. Otherwise, only the m/z is used for the matching, which can be used
for spectral library building. For compound annotation in complex samples, an additional identifier
should be available.

:material-lightbulb: If you want to filter your feature list for a list of target compounds
afterwards, you can use the
[Feature list rows filter](../feature_list_row_filter/feature_list_rows_filter.md)
with the only identified option.

The user has to provide a database of m/z values (or neutral masses, formulae, SMILES strings to
calculate m/z from) and optionally retention times in ***.csv format** (see below).

### **Database file**

Database file has to be provided in ***.csv** or ***.tsv format** (Comma-Separated or tab).
Such files can be exported from a spreadsheet software such as MS Excel, or
edited manually using a text editor.

The following example shows the structure of the database file using the default column names:

    neutral_mass,rt,name,formula
    175.119,24.5,Arginine,C6H14N4O2
    132.054,11.9,Asparagine,C4H8N2O3
    133.038,11.7,Aspartate,C4H7NO4

!!! tip

    The column names used in your CSV file must match the names configured in the **Columns**
    parameter. Column names are configurable in the parameter dialog by double-clicking the
    column name and pressing Enter after changing. Use the **Example** button in the dialog to
    export a CSV file with the currently configured column headers.

!!! warning

    Wildcards for RT, mobility, and CCS: values ≤ 0 for `rt`, `mobility`, and `CCS` are treated
    as wildcards — the row matches all features regardless of tolerance. Negative values are
    converted to `null` (absent) on import; zero is retained as a value but skipped during
    matching. **m/z has no wildcard behaviour** — a valid positive m/z is always required.

The available fields in a library file include:

| Field name (default)          | Field description                                 |
|-------------------------------|---------------------------------------------------|
| `neutral_mass`                | Neutral monoisotopic mass                         |
| `mz`                          | Precursor m/z                                     |
| `rt`                          | Retention time (values ≤ 0 are wildcards)         |
| `ri_record`                   | Retention index record (see RI tolerance)         |
| `formula`                     | Molecular formula                                 |
| `smiles`                      | SMILES                                            |
| `inchi`                       | InChI                                             |
| `inchi_key`                   | InChIKey                                          |
| `name`                        | Compound name                                     |
| `CCS`                         | CCS / Å² (values ≤ 0 are wildcards)               |
| `mobility`                    | Ion mobility (values ≤ 0 are wildcards)           |
| `comment`                     | Text comment                                      |
| `adduct`                      | Adduct type                                       |
| `PubChemCID`                  | Compound ID in PubChem database                   |
| `molecular_class`             | Molecular class                                   |
| `classyfire_superclass`       | ClassyFire superclass                             |
| `classyfire_class`            | ClassyFire class                                  |
| `classyfire_subclass`         | ClassyFire subclass                               |
| `classyfire_direct_parent`    | ClassyFire direct parent                          |
| `npclassifier_superclass`     | NPClassifier superclass                           |
| `npclassifier_class`          | NPClassifier class                                |
| `npclassifier_pathway`        | NPClassifier pathway                              |
| `iupac_name`                  | IUPAC name                                        |
| `cas`                         | CAS number                                        |
| `internal_id`                 | Internal compound identifier                      |

---

## **Parameters**

#### **Database file**

Path and name of the file that contains information for peak identification.

#### **Field separator**

Character(s) used to separate fields in the database file.

- `.csv` = `,`
- `.tsv` = `\t`

#### **Columns**

Columns to import from the library file. Enable a column by checking it; disable by unchecking.
The column name used in the CSV must match the name shown here. Double-click a column name to
rename it to match your file's header.

The choice of columns depends on the availability of retention time, mobility data, information
about adducts, and the presence of identifiers in your database file. If the exact mass should be
calculated, the neutral mass (or structure information) needs to be provided and enabled together
with the adduct settings.

Use the **Example** button in the parameter dialog to export a CSV template with the configured
headers.

#### **m/z tolerance**

Maximum allowed m/z difference to set an annotation to a feature (max. difference between
database and observed m/z).

#### **Retention time tolerance** _(Optional)_

Maximum allowed retention time difference to set an identification to a feature. Disabled means
RT is not used for filtering or scoring.

#### **Mobility time tolerance** _(Optional)_

Maximum allowed mobility difference to set an identification to a feature.

#### **CCS tolerance (%)** _(Optional)_

Maximum allowed relative CCS difference (in percent) to set an identification to a feature.

#### **Retention index tolerance** _(Optional)_

Maximum allowed retention index (RI) difference to set an identification to a feature. Requires
the `ri_record` column to be present in the database file and the feature list to contain RI
values (e.g. from a GC workflow with RI calibration).

!!! tip

    The RI tolerance has a `Match on null` option: when enabled, features without an RI value
    still match library entries that have an RI record. When disabled, features without an RI
    value do not match entries that have an RI record.

#### **Charge filter**

Filter annotations by charge state. Requires either the **Use adducts** parameter or the `adduct`
column to be enabled to determine the expected charge. If no isotope pattern is detected for the
feature, charge filtering is skipped.

- **No filter** (default): charge is not considered.
- **Filter**: annotations whose charge does not match the feature's detected charge are excluded.

#### **Use isotope matcher** _(Optional)_

Matches the predicted isotope pattern of the candidate compound against the detected isotope
pattern of the feature. The [Isotope finder](../filter_isotope_finder/isotope_finder.md) must be
run before using this option. Matches with low isotope pattern similarity are removed. The
sub-parameters are:

- **Isotope m/z tolerance**: maximum m/z difference between a predicted and a measured isotope
  peak to be considered a match. Default: 0.005 Da / 10 ppm.
- **Minimum isotope intensity (%)**: predicted isotope peaks below this relative intensity are
  excluded from the predicted pattern. Default: 5 %.
- **Minimum isotope score**: annotations whose isotope pattern score falls below this threshold are
  removed after scoring. Default: 0.0 (all passing matches are kept).

#### **Use adducts** _(Optional)_

If enabled, m/z values for multiple adducts are calculated from the neutral mass (or formula or
SMILES) and matched against the feature list. Requires `neutral_mass`, `formula`, or `smiles` to
be selected in the **Columns** parameter.

!!! warning

    Using many adducts increases spurious hits. This is especially important for spectral library
    creation where one sample contains multiple compounds. Restrict adducts using the combination
    feature (e.g. combine `M-H2O` with `M+H` to create `M-H2O+H`).

#### **Calculate main isotopic signal** _(Optional)_

For compounds with abundant heavy isotopes (e.g. molecules > C75, containing Cl, Br, S), the most
intense peak in the isotope pattern may not be the monoisotopic peak. When enabled, additional
annotations are generated for the most intense isotope signal.

#### **Filter filename header** _(Optional)_

Column header used to filter matches to the corresponding acquisition file. The value in this
column must be contained in the raw data filename. Used in library generation workflows to link
each compound to its specific sample.

!!! tip

    The unique sample identifier should not end with a number (e.g. `libid_Plate1_A2` also matches
    `libid_Plate1_A20`).

#### **Additional columns**

Controls how columns in the database that are not listed in the **Columns** parameter are handled:

- **Ignore**: unlisted columns are discarded.
- **Import specific**: a comma-separated list of additional column names to import as-is (e.g.
  `Pathway,Synonyms`). These are stored in the annotation and exported in spectral library JSON.
- **Import all**: every column from the CSV is imported, regardless of the **Columns** selection.

---

## **Algorithm** {#algorithm}

### Matching

For each database entry and each feature list row, a match is attempted:

1. **m/z** must fall within the configured m/z tolerance window around the database entry's
   precursor m/z — this check is always applied.
2. **RT**, **mobility**, and **CCS** are checked only when the corresponding tolerance is enabled
   *and* the database entry has a valid (> 0) value for that dimension.
3. **RI** is checked when the RI tolerance is enabled and the database entry contains an RI record.
   The "match on null" option controls behaviour when the feature has no RI value.

Values ≤ 0 for RT, mobility, and CCS act as wildcards: they bypass the tolerance check and the
feature is annotated regardless of its measured value in that dimension.

### Score calculation

Every successful match receives a compound annotation score between **0** (at the tolerance
boundary) and **1** (exact match at the reference value). The score is stored in the
**Compound annotation score** column of the feature table.

**Per-dimension center score:**

For each active dimension *i* (m/z, RT, mobility, CCS, RI), the score contribution is:

$$
\text{score}_i = \max\!\left(0,\ 1 - \frac{|\text{feature value}_i - \text{ref value}_i|}{\text{tolerance}_i}\right)
$$

- **1.0** when the feature value exactly matches the reference value (centre of the tolerance
  window).
- **0.0** at or beyond the tolerance boundary.
- Linear interpolation between 0 and 1 within the window.

**Final score (weighted average):**

$$
\text{score} = \frac{\sum_{i} \text{score}_i \cdot w_i}{\sum_{i} w_i}
$$

All active dimensions receive equal weight (*w* = 1). A dimension is included in the average only
when:

- the library entry has a non-null value for that dimension,
- the corresponding tolerance parameter is enabled, and
- the feature has a measured value for that dimension.

Dimensions without a reference value or without an enabled tolerance do not contribute to the
score. When only m/z is enabled, the score equals the m/z center score alone.

!!! tip

    Enabling more dimensions (RT, mobility, CCS, RI) increases score resolution and allows better
    ranking of candidates. A perfect m/z match with no additional constraints gives a score of 1.0
    regardless of how far the RT is from the reference — so enabling RT tolerance is strongly
    recommended for complex samples.

!!! warning

    Wildcard entries (RT/mobility/CCS ≤ 0) that match due to the wildcard still contribute a
    centre score of 0 for that dimension if the tolerance is enabled and a range around 0 is
    computed. In practice this lowers the overall score for wildcard entries. Prefer omitting
    optional tolerances (disabling them) rather than using wildcard values when a dimension is
    truly unknown.

### Isotope pattern score {#isotope-score}

The isotope matcher runs as a post-processing step **after** the main compound annotation score is
assigned. It removes and re-ranks annotations based on how well the theoretical isotope pattern of
the candidate matches the measured one.

**Prerequisites:**

- The annotation must contain both a molecular **formula** and an **adduct type**. Annotations
  without these are scored 0 and removed if a minimum score > 0 is set.
- A **detected isotope pattern** (from the Isotope finder module) must be available for the
  feature. If no isotope pattern was stored but an MS1 scan exists, the full MS1 mass list is used
  as a fallback.

**Prediction:**

The theoretical isotope pattern is predicted for the ionized formula (formula + adduct) at
multiple instrument resolution levels (from coarse to high resolution). Predicted isotope peaks
with a relative intensity below the **Minimum isotope intensity (%)** parameter are excluded.
The prediction is cached per formula to avoid redundant computation across annotations.

**Scoring per resolution level:**

Two composite cosine similarity scores are calculated between the predicted (library) pattern and
the measured (query) pattern for each resolution:

| Score | Unmatched signal treatment | Purpose |
|---|---|---|
| `similarity` | Both unmatched predicted and unmatched measured peaks penalised | Penalises both directions |
| `similarityLibrary` | Only unmatched predicted peaks penalised | Focus on predicted peaks being present |

The combined score for a given resolution level is:

$$
\text{score}_\text{res} = \frac{\text{similarity} + 2 \times \text{similarityLibrary}}{3}
$$

The factor of 2 gives more weight to `similarityLibrary`, so missing predicted isotope peaks are
penalised more strongly than having extra peaks in the measured spectrum. The final isotope score
is the **maximum** across all resolution levels:

$$
\text{isotope score} = \max_{\text{res}}\left(\text{score}_\text{res}\right)
$$

**Composite cosine algorithm:**

Each of the two similarity scores is computed using the composite cosine (similar to NIST search):

$$
\text{composite} = \frac{N_\text{query} \times \cos_\text{weighted} + N_\text{overlap} \times r}{N_\text{query} + N_\text{overlap}}
$$

where:

- $N_\text{query}$ = total number of signals in the measured spectrum
- $N_\text{overlap}$ = number of matched signal pairs (within isotope m/z tolerance)
- $\cos_\text{weighted}$ = cosine similarity of the matched pairs with **square-root intensity
  weighting** (each intensity is raised to the power 0.5; m/z weighting = 0)
- $r$ = relative neighbour factor: average of min/max intensity-ratio agreements between
  adjacent matched peaks, ranges 0–1. A value of 1 means all adjacent peaks have perfectly
  matching intensity ratios in both spectra.

The composite score ranges from **0** (no match) to **1** (perfect identity).

**Filtering and re-ranking:**

After scoring, annotations with an isotope score below the **Minimum isotope score** threshold are
removed from the feature. The remaining annotations are re-sorted in descending isotope score
order. The score is stored in the **Isotope pattern score** column of the feature table.

!!! tip

    Set **Minimum isotope score** > 0 (e.g. 0.6–0.8) to discard poor isotope matches. Leave it
    at 0 to keep all annotations and just use the score for ranking.

!!! warning

    The isotope matcher requires both a **formula** and an **adduct** in the library entry.
    Annotations without this information score 0. Make sure the `formula` column is selected and
    the **Use adducts** parameter is enabled (or the `adduct` column is imported).

### Output columns added per match

| Column                      | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| Compound annotation score   | Overall score (0–1)                                       |
| m/z ppm difference          | Mass error in parts-per-million                           |
| m/z absolute difference     | Absolute mass error in Da                                 |
| RT absolute difference      | Absolute RT difference (if RT was available and > 0)      |
| RT relative error (%)       | Relative RT error in percent                              |
| Mobility absolute difference| Absolute mobility difference (if mobility > 0)            |
| CCS relative error (%)      | Relative CCS error in percent (if CCS was available > 0)  |
| RI difference               | RI difference (if RI tolerance is enabled and RI present) |
| Isotope pattern score       | Composite cosine score 0–1 (if isotope matcher is enabled) |

---

{{ git_page_authors }}
