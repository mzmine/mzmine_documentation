# CCSBase export

:material-menu-open: **Feature list methods → Export feature list → CCSBase export**

Exports annotated features with a collision cross section (CCS) value into a CSV file in the format
expected by [CCSBase](https://ccsbase.net/), so that measured CCS values can be contributed to the
database.

Only rows that are identified and carry a
[preferred annotation](../../terminology/annotations.md) are exported. For each row, the compound
name, adduct, neutral mass, charge, *m/z*, CCS, SMILES, molecular class, mobility type, and
calibration method are written.

!!! warning

    Rows are silently skipped if any required field is missing (for example no SMILES, no adduct, or
    no CCS value). Make sure CCS values have been calculated (see
    [CCS calibration](../id_ccs_calibration/ccs_calibration.md)) and that your compound database
    provides structures.

If the same compound (identified by SMILES) is annotated with the same adduct on several rows, only
the entry of the most intense feature is exported.

---

## Parameters

#### Feature lists

The feature lists to export.

#### Export file

Target CSV file. A `.csv` extension is added if missing, and an existing file is overwritten.

#### Fallback molecule type

Molecular class used when the compound database does not provide one. Choices are
`small molecule` (default), `lipid`, `carbohydrate`, and `peptide`.

#### Calibration method

The calibration approach used for the ion mobility device of the instrument. This value is written
to every exported entry and cannot be derived from the data, so it must be set correctly. Choices
are `single field, calibrated with Agilent Tune Mix`, `single field, calibrated`,
`stepped field, calibrated with Agilent tune mix`, and `stepped-field`.

---

{{ git_page_authors }}
