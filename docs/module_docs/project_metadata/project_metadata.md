# Sample metadata

:material-menu-open: **Project → Sample metadata**

Sample metadata lets you attach study design information to each raw data file loaded in your
project, for example, sample group, treatment condition, replicate number, or batch. mzmine uses
this metadata throughout the software: For color-coding samples in visualizations, grouping them in
the statistics dashboard, and driving downstream analyses such as blank subtraction or
normalization.

---

## Accessing sample metadata

Open the sample metadata table from the main menu:

:material-menu-open: **Project → Sample metadata** (shortcut ++ctrl+m++ / ++cmd+m++)

This opens the **Sample metadata** tab as a panel in the main window. Each row corresponds to one
raw data file loaded in the project, and each column is a metadata parameter. You can add, edit, or
remove metadata columns directly in this table, or import them from a file.

---

## Automatically populated fields

When you import raw data files, mzmine automatically creates three reserved metadata columns and
fills them for every sample. These values may be overwritten manually or by metadata import.

| Column header        | Type      | Source                                              |
|----------------------|-----------|-----------------------------------------------------|
| `filename`           | Text      | The name of the raw data file (read-only reference) |
| `run_date`           | Date/Time | Acquisition time stamp embedded in the raw file (e.g., 2026-12-31T20:10:05)  |
| `mzmine_sample_type` | Text      | Inferred from the filename using pattern matching   |

### Sample type detection

The `mzmine_sample_type` column is filled automatically by scanning the file name for common naming
conventions used in untargeted metabolomics runs. The matching is case-insensitive and looks for
specific keywords that are not part of a longer word:

| Detected value | Filename keywords matched |
|----------------|---------------------------|
| `qc`           | `qc`                      |
| `blank`        | `blank`, `media`, `blk`   |
| `calibration`  | `cal`, `quant`            |
| `sample`       | anything else (default)   |

**Examples:**

- `QC_01.mzML` → `qc`
- `Blank_run3.mzML` → `blank`
- `Study_S001_liver.mzML` → `sample` (default)

!!! tip

    Consistent file naming pays off: if your QC injections all contain "QC" in the filename, 
    mzmine will classify them automatically. You can always correct individual entries in the 
    metadata table by typing directly into a cell or importing a metadata table.

---

## Importing metadata from a file

For larger studies it is more practical to prepare your metadata in a spreadsheet and import it.
mzmine accepts **CSV** and **TSV** files. The separator (comma or tab) is detected automatically
from the file extension, but the file extension itself is not important: You can use any extension
or even omit it entirely.

!!! tip "Start from a template"

    The easiest way to prepare a metadata file is to first load your raw data files into mzmine, 
    then **export** the current metadata table. This gives you a file that already contains all 
    the sample file names in the correct format. Open it in your spreadsheet software, add your 
    custom columns, and re-import.

    Export via: **Project → Sample metadata → Export** (choose **Default** or **mzmine internal** format).

### Required file structure

The file must be a plain table in a wide format (one row per sample). The **first column** must be
named `filename` or `filenames` (case-insensitive). Each subsequent column is one
metadata parameter.

**Minimal example** (TSV, no type hints means that mzmine will automatically try to use the date and
time or number format for a column if all values match - otherwise the column is recognized as
text):

```
filename	Group	Batch	Condition
study_S001.mzML	Control	1	Vehicle
study_S002.mzML	Treatment	1	Drug_A
QC_01.mzML	QC	1	QC
Blank_01.mzML	Blank	1	Blank
```

If no type information is provided, mzmine will auto-detect the most appropriate data type for each
column:

- All values parseable as numbers → **NUMBER** (stored as decimal)
- All values parseable as date/time → **DATETIME** (e.g., 2026-12-31T20:10:05)
- Otherwise → **TEXT**

### Optional header rows for explicit type definitions

You can add up to two optional rows **before** the `filename` title row to declare column
descriptions and data types explicitly. mzmine reads them in this order:

1. **Description row**: human-readable descriptions for each column (optional)
2. **Type row**: data type for each column: `TEXT`, `NUMBER`, or `DATETIME` (optional)
3. **Title row**: column headers; the first cell must be `filename` (required)
4. **Data rows**: one row per sample

**Example with full header (TSV):**

```
Sample grouping	Number of replicates	Acquisition date	Biological condition
TEXT	NUMBER	DATETIME	TEXT
filename	Replicate	run_date	Group
study_S001.mzML	3	2024-03-15T09:00:00	Control
study_S002.mzML	3	2024-03-15T09:45:00	Treatment
QC_01.mzML	1	2024-03-15T10:30:00	QC
```

!!! note "Filename matching"

    File names in your metadata file are matched against the raw data files loaded in the project. 
    The match is done by file name (without file extension or folder path). Files listed in the 
    metadata that are not present in the project are silently skipped; files in the project that 
    are absent from the metadata simply retain their current values.

    Raw data files must be loaded into the project **before** importing metadata.

### Date and time format

Date/time columns (`DATETIME`) accept a wide range of formats. ISO 8601 format is recommended for
unambiguous parsing, e.g., `2024-03-15T09:00:00`.

### GNPS compatibility

Metadata exported from GNPS uses an `ATTRIBUTE_` prefix for column names (e.g., `ATTRIBUTE_Group`).
mzmine can strip this prefix automatically during import. Enable the **Remove ATTRIBUTE\_ prefix**
option in the import dialog to clean up the column names.

---

## Data types

User-defined metadata columns can hold three types of values:

| Type         | Description           | Example values                    |
|--------------|-----------------------|-----------------------------------|
| **TEXT**     | Free-form text labels | `Control`, `Treatment`, `Batch_1` |
| **NUMBER**   | Decimal numbers       | `1`, `0.5`, `42.7`                |
| **DATETIME** | Date and time         | `2024-03-15T09:00:00`             |

The data type determines how mzmine handles the column in downstream analyses (e.g., the statistics
dashboard treats `NUMBER` columns as continuous variables).

---

## Adding custom metadata columns manually

To add a new column directly in the metadata table without importing a file:

1. Open **Project → Sample metadata**
2. Click **Add parameter** in the table toolbar
3. Choose a column name, data type, and optional description
4. Fill in values for each sample in the table

---

## Export formats

When exporting metadata you can choose between three formats:

| Format              | Description                                                                               |
|---------------------|-------------------------------------------------------------------------------------------|
| **Default**         | Plain TSV with filename column and data: easy to open in Excel or other tools             |
| **mzmine internal** | Includes description and type rows in the header: preserves type information on re-import |
| **GNPS**            | Adds `ATTRIBUTE_` prefix to all columns as required for GNPS metadata uploads             |

---

{{ git_page_authors }}
