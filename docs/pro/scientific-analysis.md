# Scientific analysis through the mzmine MCP local connector

The local connector can perform five bounded analyses on a reviewed, immutable snapshot of a selected feature table. This avoids changing measurements while an analysis is running and records the application version, snapshot revision, requested specification, and any upstream native result used as input.

The running application returns the accepted input schema and result contract; use those for exact field names and options.

!!! info "MCP-only workflow entry point"

    In the reviewed build, these five workflows are initiated through the MCP local connector. Calculation
    runs locally in mzmine, and results can be opened in mzmine's native result view.

!!! warning

    These analyses organize and calculate evidence from the selected feature table. They do not confirm compound identity, validate an experimental design, establish causality, or replace method-specific acceptance criteria.

## Shared rules

You choose the feature rows and explicitly map opaque sample identifiers to their condition, independent unit, and, where relevant, time or pair. Technical repeats are aggregated within the declared independent unit. Missing, non-finite, negative, or invalid measurements remain missing; they are not changed to zero. Raw area is the normal default. Normalized values are used only when the chosen native normalized column is present.

Results are bounded and paged. Large requests may need fewer feature rows or samples. An analysis is tied to its approved scope: downstream analyses can use only compatible prior native results from the same scope.

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

For every selected sample, the quantification role must be explicitly unassigned. Calibration and QC
samples cannot be submitted as exposure samples; assign the role correctly in the quantification
result before creating the exposure scope.

The result reports eligible samples, the selected reference ratio, and whether the calculated value is above or at/below that selected reference. It excludes unavailable, flagged, unsupported-unit, or—in the absence of explicit acceptance—estimated values. A surrogate-reference-equivalent value stays labelled as an estimate. The comparison is not a safety assessment, regulatory determination, or toxicological conclusion.

## Next steps

Open the returned feature row in mzmine to inspect chromatograms, spectra, annotations, and the native table. Export or share a result only after reviewing the concrete selection and destination. When an assumption, group mapping, calibration source, or reference applicability is uncertain, keep the analysis descriptive and resolve it before making a decision.

{{ git_page_authors }}
