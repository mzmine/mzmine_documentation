# Quantify selected features

Use quantification to convert feature responses into concentrations using a stated calibration.
Start with a processed feature table, identified calibration samples, and the feature rows you
intend to quantify. Review the chromatograms and assignments before fitting a calibration.

## Prepare the calibration

| Choice | What you need |
| --- | --- |
| External calibration | The analyte feature row, calibrator samples, and their concentrations with units |
| Internal-standard calibration | The analyte and internal-standard rows, calibrator concentrations, and the internal-standard concentration for each calibrator and unknown |
| Surrogate-reference-equivalent calibration | A reference-standard row and calibration, plus a positive relative response factor and its source for each analyte |

Choose raw area, raw height, or an existing normalized measurement. Supply at least two distinct
calibrator concentrations; a fitted line alone does not establish that the calibration is suitable.
State the regression weighting (unweighted, 1/x, or 1/x²) and whether to fit or fix the intercept at
zero. Zero-concentration points cannot be used with 1/x or 1/x² weighting.

Prepare independent QC samples with expected concentrations if you want to assess their recovery.
Keep calibrator and QC assignments separate from unknown samples. Explain exclusions and include any
dilution, extraction volume, sample mass, or device count needed to express the final quantity.
These are calculation inputs; a generic metadata column does not automatically configure calibration.

For example, you might prepare this **illustrative input table**, with your actual sample names and
concentrations in place of the examples:

| Sample | Use | Concentration (µg/L) |
| --- | --- | --- |
| Cal-1 | Calibrator | 1 |
| Cal-5 | Calibrator | 5 |
| Cal-10 | Calibrator | 10 |
| QC-check | Independent QC | 4 |
| Unknown-1 | Unknown | Not supplied |

## Ask mzassist

> Quantify the selected analyte using external calibration and raw peak area. I will provide the
> calibrator concentrations and QC assignment. Show me the sample mapping, regression choices,
> units, and preparation corrections before calculating.

Approve result sharing, confirm the row and sample mapping, and resolve missing inputs before
running. Internal-standard concentrations for unknowns must be supplied explicitly; mzmine does
not substitute the amount used in a calibrator.

## Review and save the result

Inspect the calibration curve, residuals and back-calculated concentrations, excluded calibrators,
QC results, and unknowns outside the calibrated range. Check dilution and unit conversions against
the sample preparation. Missing or invalid results remain unavailable.

Quantification retains individual sample estimates; it does not automatically average technical
replicates into independent samples. Surrogate-reference-equivalent values remain labelled as
estimates. This calculation does not establish LOD/LOQ, compound identity, or method acceptance.

Open the native result view and save both the CSV table and JSON calculation record. See
[Save and reproduce your work](../mzassist-saving.md). To compare quantified results between
conditions, continue with [Study comparisons](study-comparison.md) and state the independent samples.

{{ git_page_authors }}
