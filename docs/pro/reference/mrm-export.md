# MRM export: implementation reference

This reference explains MRM transition export. See [Export MRMs to TSV](../../module_docs/io_mrmtotsv/mrm-to-tsv.md).

## Inputs and prerequisites

Select feature lists that contain the MRM transition data type and an export file. A `.csv` filename chooses comma separation; every other extension is written tab-separated. When several lists are selected, use `{}` in the name to substitute the current feature-list name.

## Parameters and validation

**Skip missing features** is presented with default **false**. In this snapshot, however, the task does not read that setting: its internal skip flag is fixed false. Missing features therefore retain a placeholder output row regardless of the UI choice; unknown non-null features with transitions still produce transition rows.

## Processing behavior

Rows are exported by ascending row ID and raw files by name. Each present transition produces one line. The fixed columns are row ID, `feature_list`, raw-file name, `q1_mz`, `q3_mz`, `is_quantifier`, `area`, `height`, and `rt`, followed by compound-database-match fields. Area, height and RT are calculated from the transition chromatogram clipped to that individual feature's raw-data-points RT range; RT is its most intense point within the clipped range.

## Outputs and side effects

The requested directory is created if possible and the target file is replaced. A `{}` name is resolved separately for each list. `is_quantifier` is `true` only when the exported transition is the selected transition object for that feature; it is `false` for missing, unknown, or transition-less features.

## Edge cases and errors

Lists lacking MRM transition data fail before a file is written. Failure to create the parent directory is reported. I/O exceptions during writing become task failures. A missing feature yields one row with identifying fields and empty transition-derived values, not one row per expected transition. An unknown but non-null feature that still has transitions instead yields one row per transition with Q1/Q3 present, while `is_quantifier` is `false` and range-derived metrics are empty.

## Worked examples

### One detected feature with two transitions

A row in `sampleA` containing Q1 500 transitions Q3 120 and 150 produces two lines. If Q3 150 is the selected quantifier, only its line has `is_quantifier=true`; both lines calculate area/height/RT from their own trace within that sample feature's raw-data-points RT boundaries.

### Missing feature despite enabled skipping

For an aligned row absent from `sampleB`, the export writes one `sampleB` placeholder row even if **Skip missing features** is checked in this snapshot. It carries row/list/file identity but empty Q1, Q3, area, height and RT values.
