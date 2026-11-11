# Quantification {#quantify-selected-features}

Quantification converts feature responses into concentrations using a stated calibration. Start with a processed feature table and review chromatograms and assignments for the features you want to quantify.

## What you need {#prepare-the-calibration}

| Calibration | Information needed |
| --- | --- |
| External | Analyte feature row, calibrator samples, and concentrations with units |
| Internal standard | Analyte and internal-standard rows, calibrator concentrations, and internal-standard concentration for each calibrator, independent QC, and unknown |
| Surrogate-reference-equivalent | Reference-standard row and calibration, plus a positive relative response factor and its source for each analyte |

The response can be raw area, raw height, or an existing normalized measurement. The calibration needs at least two distinct concentrations. Regression can be unweighted, 1/x, or 1/x², with the intercept fitted or fixed at zero. mzassist helps you review these choices before calculating. Zero-concentration points cannot be used with 1/x or 1/x² weighting. A fitted line alone does not establish that a calibration is suitable.

Independent QC samples with expected concentrations can assess recovery. Calibrator and QC assignments must be distinct; every remaining sample is treated as an unknown. Exclusions and preparation details such as dilution, extraction volume, sample mass, or device count belong to this quantification setup when they are needed to express the final quantity. A generic metadata column does not automatically configure calibration. Internal-standard concentrations must be supplied for calibrators, independent QCs, and unknowns; mzmine does not substitute the calibrator amount.

For the calibration and reported sample concentration, mzmine uses only detected or manually integrated measurements that are unflagged, finite, and non-negative. Gap-filled (**ESTIMATED**) responses are unavailable for calibrators, independent QCs, and unknowns. Other measurements can still be shown for inspection, but they are not used to fit the calibration or calculate a concentration.

For example, this **illustrative input table** shows the information for an external calibration:

| Sample | Use | Concentration (µg/L) |
| --- | --- | --- |
| Cal-1 | Calibrator | 1 |
| Cal-5 | Calibrator | 5 |
| Cal-10 | Calibrator | 10 |
| QC-check | Independent QC | 4 |
| Unknown-1 | Unknown | Not supplied |

## Calculate with mzassist {#ask-mzassist}

1. Ask mzassist to quantify the selected features. For example:

    > Quantify the selected analyte using external calibration and raw peak area. Show me the sample mapping, regression choices, units, and preparation corrections before calculating.

2. mzassist checks the metadata you approved for sharing. Provide only the calibration, QC, and sample-preparation facts it still needs. If needed, sample metadata can also be edited under **Project → Sample metadata**; see [Sample metadata](../../module_docs/project_metadata/project_metadata.md).
3. Confirm the proposed feature and sample mapping and calculation choices in chat, then ask mzassist to calculate and open the results.
4. Inspect the calibration curve, residuals, back-calculated concentrations, excluded calibrators, QC results, and unknowns outside the calibrated range. Check dilution and unit conversions against the sample preparation. Missing or invalid results remain unavailable.
5. Use **Save table (CSV)** and **Save calculation record (JSON)** in the result view. See [Save and reproduce your work](../mzassist-saving.md).

## Interpretation {#review-and-save-the-result}

Quantification retains individual sample estimates; it does not automatically average technical replicates into independent samples. Surrogate-reference-equivalent values remain labelled as estimates. The calculation does not establish LOD/LOQ, compound identity, or method acceptance. To compare quantified results between conditions, see [Study comparison](study-comparison.md) and identify the independent samples.

{{ git_page_authors }}
