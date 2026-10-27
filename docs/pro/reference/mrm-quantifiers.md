# MRM quantifiers: implementation reference

This is the reviewed 4.10.107 development-series snapshot. See [Set MRM quantifiers](../../module_docs/mrm_setquant/mrm-set-quant-mass.md) for the user guide.

## Inputs and prerequisites

Choose MRM-containing feature lists and a CSV/TSV quantifier table. The table must map a precursor Q1 m/z, quantifier Q3 m/z, and retention time; additional columns are allowed. The operation edits the selected lists in place rather than creating a replacement list.

## Parameters and validation

### Column headers

All three mapped columns—Q1 m/z, quantifier m/z, and RT—must be selected. Validation rejects an incomplete mapping with “All types must be selected and set.” Header resolution is performed against the first input row.

### Tolerances

**RT tolerance** defaults to 0.1 minutes. **m/z tolerance** defaults to 0.2 m/z and 0 ppm. Q1 identifies candidate table entries; Q3 must match an existing transition within the same m/z tolerance; RT chooses the closest eligible entry and must then pass the RT tolerance.

## Processing behavior

Table rows are parsed and sorted by Q1. For each feature-list row, mzmine selects the tallest feature carrying MRM transitions, finds table entries within Q1 tolerance, removes entries whose Q3 does not exist in that feature, then selects the RT-closest remaining entry. This uses the row's average RT—not an individual file's RT—so an already aligned row gets the same intended transition across files.

If the selected table RT is outside tolerance, the row is left unchanged. Otherwise the selected Q3 is applied to every feature in the row; each file must contain both the table Q1 and Q3 within m/z tolerance.

## Outputs and side effects

Quantifier state is changed in place. No new list or transition trace is created. A row with no Q1 match, no eligible Q3, or no RT candidate is simply retained with its prior quantifier.

## Edge cases and errors

Unreadable files/CSV, missing headers, or non-numeric transition fields cause task errors. If the best table entry cannot be set in every feature, the task records an error naming the affected raw files; rows processed previously have already been changed. The implementation assumes each processed row has at least one MRM-bearing feature.

## Worked examples

### An aligned row receives one common quantifier

For a row at average RT 5.00 with Q1 500, table candidates 500/120/4.95 and 500/150/5.02, and a 0.1-minute RT tolerance, the 5.02 entry is closest. If every feature matches table Q1 500 and contains Q3 150 within the m/z tolerance, Q3 150 becomes the quantifier in each file. A per-file Q1 mismatch can still cause a partial-update error.

### Close Q1, unavailable Q3

A 500.00 row may match a 500.15 table Q1 under the default 0.2-m/z tolerance. If that table row asks for Q3 155 but the tallest feature contains only Q3 120 and 150, it is removed before RT selection; with no remaining entry, the existing quantifier is unchanged.
