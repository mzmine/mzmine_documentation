# Scientific analyses with mzassist {#scientific-analysis-through-the-mzmine-mcp-local-connector}

Use these analyses with a processed feature table to answer a specific analytical question.
Ask mzassist to select the table, show the required inputs, and open the completed calculation in
mzmine. Calculations use the approved data as they were when shared; changing the table requires
a fresh sharing review.

| Your question | Guide | Prepare first |
| --- | --- | --- |
| What concentration does this response represent? | [Quantification](analysis/quantification.md) | Calibrators, concentrations/units, analyte rows, optional internal standards and independent QCs |
| Which injections or features need a QC review? | [Batch diagnostics](analysis/batch-diagnostics.md) | One batch, injection order, roles, reference values and method-specific alerts |
| How do conditions or time points differ? | [Study comparison](analysis/study-comparison.md) | Conditions, independent samples, repeats and any pairing/time/covariates |
| Which features track the measured assay activity? | [Activity association](analysis/activity-association.md) | Matched assay values, independent samples, endpoint, dose and direction |
| What does a quantified amount imply under this use scenario? | [Exposure calculation](analysis/exposure-calculation.md) | Native quantification, quantity basis, use rate, and a justified reference |

These five analyses are started through mzassist. Their calculations run locally in mzmine, where
you can inspect and export the results. They supplement the existing mzmine processing modules.

!!! warning

    These analyses organize and calculate evidence from the selected feature table. They do not confirm compound identity, validate an experimental design, establish causality, or replace method-specific acceptance criteria.

## Shared rules

Choose the feature rows and samples for the question. For study comparisons and activity associations, identify the experimental conditions and independent samples, and distinguish repeat injections of the same sample from independent replicates. Study comparison can also use time and pairing information. Technical repeats are averaged for these two analyses; quantification and exposure calculations retain individual sample results. Missing, non-finite, negative, or invalid measurements remain missing; they are not changed to zero. Raw area is the normal default. Normalized values are used only when the chosen native normalized column is present.

Large result tables are shown in pages; ask for the remaining rows before treating the visible page as complete. Calculations that use a previous native result must use compatible data from the same sharing selection.

## Quantification

Quantification fits calibration data from selected feature-table rows. Choose area, height, normalized area, or normalized height; a concentration unit; and an external, internal-standard, or surrogate-reference-equivalent calibration.

- **External calibration** uses the analyte's calibration points.
- **Internal-standard calibration** uses a separate internal-standard feature row and its stated concentration for each calibrator or unknown.
- **Surrogate-reference-equivalent** uses a reference-standard calibration row and requires a positive relative response factor and its stated source for every analyte.

Unweighted, 1/x, and 1/x² regression weighting and a free or zero-fixed intercept are available. At least two distinct calibrator points are required; excluded calibrators need a reason. Independent QC samples can be included with expected concentrations and an optional accuracy tolerance. Optional sample-preparation values support dilution correction and conversions using extraction volume, sample mass, or device count.

The result retains calibration and preparation provenance and labels unavailable or estimated values. It does **not** calculate LOD, LOQ, acceptance thresholds, identity confirmation, or a toxicity conclusion. Surrogate-reference-equivalent values are estimates and do not establish the identity of the analyte.

## Batch diagnostics

Batch diagnostics inspect one explicitly confirmed analytical batch. Supply its injection order and, as applicable, QC IDs, sample roles, reference rows, expected retention time or m/z, and alert thresholds. The analysis reports QC precision, reference retention-time and mass deviations, optional internal-standard behavior, and possible carryover only where a blank is explicitly adjacent to a preceding shared injection.

Thresholds are method-specific alerts, not built-in release rules. Incomplete injection order leaves carryover unconfirmed. Reference m/z and retention time are compared only against supplied values. Flags identify evidence for inspection; they do not prove instrument failure or release a batch.

## Study comparison

Study comparison supports descriptive output, Welch or Student t tests, Mann–Whitney, paired t, one-way ANOVA, covariate-adjusted linear models, subject random-intercept mixed models, and moderated tests. Specify the conditions and, when relevant, time, baseline condition, pair IDs, and selected feature rows. A log2 transformation is optional; nonpositive values then remain missing.

For each selected feature, the result supplies trajectories, sample and independent-unit counts, the requested test status, and where applicable an effect estimate, standard error, and pointwise confidence interval. Benjamini–Hochberg adjusted p values (`p_value_bh`) are calculated across valid, testable selected features before pagination. The correction applies to that selected family, not to separate analyses.

Paired tests require complete explicit pair mappings. Independent tests need enough independent units; ANOVA needs at least three conditions. Estimated and surrogate-reference values are excluded unless you explicitly include them. There is no automatic imputation, model selection, random slopes, serial residual correlation, small-sample mixed-model correction, or simultaneous confidence interval.

## Activity association

Activity association maps assay values to the same approved sample identifiers and correlates their independent-unit means with each selected feature. Choose Pearson or Spearman association and state a single assay endpoint, dose, context, and direction. The direction tells the result whether a higher or lower assay value means more activity, so the priority score is oriented consistently.

The result includes paired observations, correlation, confidence interval where available, matched independent-unit count, and a direction-adjusted priority score. Technical repeats are averaged and missing values are not replaced. The analysis ranks associations for review; it does not establish causality, chemical identity, or a biological mechanism.

## Exposure assessment

Exposure assessment converts a completed native quantification result into a transparent comparison with a stated reference value. It cannot use manually supplied measurements. Provide the scenario and its interpretation, any dilution/body-mass assumptions, a reference value with unit, source URL and version, and an explicit acknowledgement that the reference applies to the question.

Select study samples that were not designated as calibrators or QC samples in the quantification
setup. mzmine derives these roles from the calibration and QC sample lists; there is no separate
role-editing step in the result. If that setup was incorrect, correct it and rerun quantification.
Actual calibrators and QC samples must not be used as exposure samples.

The result reports eligible samples, the selected reference ratio, and whether the calculated value is above or at/below that selected reference. It excludes unavailable, flagged, unsupported-unit, or—in the absence of explicit acceptance—estimated values. A surrogate-reference-equivalent value stays labelled as an estimate. The comparison is not a safety assessment, regulatory determination, or toxicological conclusion.

## Next steps

Open important feature rows in mzmine to inspect chromatograms, spectra, annotations, and the native table. In the calculation result view, save the table (CSV) and calculation record (JSON) before ending the session. See [Save and reproduce your work](mzassist-saving.md). Resolve uncertain groups, calibration inputs, or reference applicability before interpreting a calculation.

{{ git_page_authors }}
