# Quantification: implementation reference

This reference documents the `quantification` operation in the reviewed knowledge-pack snapshot of the mzmine 4.10.107 development series. See the [scientific-analysis overview](../scientific-analysis.md) for scope and workflow.

## Inputs and prerequisites

The operation reads only the approved, immutable feature-table snapshot. Required fields are `mode`, `signal`, `concentration_unit`, and a non-empty `analytes` list. `signal` is `area`, `height`, `normalized_area`, or `normalized_height`; unavailable chosen data makes the specification invalid. Each analyte has `row_id` and at least two calibration entries (`sample_id`, non-negative `concentration`). Calibrator IDs must be unique and present in the calibration row. QC IDs must likewise be unique and cannot overlap calibrators. A row outside the snapshot is returned as `invalid_row`; duplicate analyte row IDs reject the request.

Modes are `external`, `internal_standard`, and `surrogate_reference_equivalent`. Internal-standard mode needs a different, present `internal_standard_row_id`; surrogate mode needs a present `reference_row_id`, positive `relative_response_factor`, and nonblank `relative_response_factor_source` for every analyte. Concentration units are `ng/mL`, `ug/mL`, `mg/L`, `ug/L`, or `ng/L`.

## Parameters and validation

`weighting` defaults to `unweighted` (`one_over_x` and `one_over_x_squared` are alternatives); `intercept` defaults to `free` (`fixed_zero` is the alternative). A calibrator marked `excluded` must have `exclusion_reason`. Zero concentrations are accepted for unweighted fitting, but are rejected by 1/x and 1/x² weighting. In internal-standard mode every usable calibrator needs positive analyte and internal-standard responses and a positive IS concentration; unknowns need their own positive IS concentration, not a substituted calibrator amount.

Optional `sample_preparation.samples.<sample_id>` accepts positive `dilution_factor`, `extraction_volume_ml`, `sample_mass_g`, `device_count`, and `output_unit`. Sample mass and device count are mutually exclusive. Either denominator requires extraction volume, and extraction volume alone is invalid; those invalid combinations return an unavailable value with invalid preparation/basis rather than a converted result. QC entries carry `sample_id`, non-negative `expected_concentration`, and optional non-negative `accuracy_tolerance_fraction`.

## Processing behavior

### Calibration and estimates

The fitted response is `y = intercept + slope × x`. For external and surrogate modes, `x` is concentration and `y` is chosen signal. Internal-standard mode uses `x = analyte concentration / IS concentration` and `y = analyte response / IS response`. The least-squares fit uses weights 1, 1/x, or 1/x² and requires at least two usable, distinct x levels and a finite positive slope. A failed fit returns its availability status rather than inventing a value.

An external estimate is `(response − intercept) / slope`; an internal-standard estimate multiplies that regression x by the unknown IS concentration. A surrogate estimate divides the reference-calibration result by the supplied response factor (the convention is unknown response/reference response at equal concentration). An estimate is flagged `outside_calibrated_range` if its regression x or comparable concentration is outside the fitted calibration range.

### Missingness and corrections

Missing/invalid responses, IS inputs, response factors, or numerical results give `value: null` with an unavailable reason. Preparation can apply dilution and convert solution concentration to mass per original sample mass or per device only when the required positive preparation values are supplied. It does not calculate LOD, LOQ, identity confirmation, acceptance criteria, or toxicity.

## Outputs and side effects

The result preserves mode, signal, weighting, intercept, canonical `ng/mL` concentration provenance, fitted coefficients, R², used/rejected calibration counts, calibration back-calculations, and rows by analyte. Each sample reports role, value, value unit/basis, status, flags and range status; QC reporting includes expected value, error and optional tolerance flag. Surrogate outputs retain `surrogate_reference_equivalent_estimate`. This operation does not alter the source table.

## Edge cases and errors

A missing IS row yields `missing_internal_standard_row`; a missing surrogate reference row yields `missing_reference_calibration_row`. The IS row cannot equal the analyte row. Unsupported signal/unit, duplicate analytes, malformed regression choices, and missing surrogate factor/source are invalid specifications. Excluded or unusable calibration points can leave fewer than two distinct usable levels.

## Worked examples

### External curve with a zero standard

With `external`, `unweighted`, `free`, concentrations 0 and 10, and usable areas, both points can fit. Changing to `one_over_x` rejects the zero-concentration point; the curve is unavailable if that leaves fewer than two distinct x levels.

### Internal-standard unknown

For `internal_standard`, a calibrator at analyte/IS concentrations 10/10 uses x=1 and its response ratio as y. An unknown with response ratio 2 has regression x `(2−intercept)/slope`; multiplying by its explicitly supplied 8 ng/mL IS concentration yields the reported analyte concentration. Omit that 8 ng/mL input and the sample is unavailable rather than using 10 ng/mL.

{{ git_page_authors }}
