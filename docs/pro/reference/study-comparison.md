# Study comparison: implementation reference

This reference documents `study_comparison` in the reviewed knowledge-pack snapshot of the mzmine 4.10.111 development series. See the [scientific-analysis overview](../scientific-analysis.md).

!!! info "MCP-only workflow entry point"

    In the reviewed build, this workflow is initiated through the MCP local connector. Calculation
    runs locally in mzmine, and results can be opened in mzmine's native result view.

## Inputs and prerequisites

Map each selected `sN` sample exactly once with `condition` and `independent_unit`; optional `time` and `pair_id` describe the design. `row_ids` defaults to all approved rows. `measurement.field` defaults to `area`; `height`, normalized fields, or `source_result` are available. A source result is required for `source_result`, and a normalized field cannot be combined with one.

## Parameters and validation

`measurement.transform` defaults to `none`; `log2` happens before technical-repeat averaging and makes non-positive values missing. Estimated/surrogate values are excluded unless `include_estimated: true`; invalid, missing, non-finite and negative values remain excluded. `comparison.test` is required: `none`, Welch/Student t, Mann–Whitney, paired t, ANOVA, `linear_model`, `mixed_model`, or `moderated_t`. Confidence level defaults to 0.95 and must be strictly between zero and one.

Two-condition tests require `left_condition` and `right_condition`; ANOVA needs at least three listed mapped conditions. `baseline_condition` must be mapped. `pair_id` belongs to `paired_t` and ordinary sample `time` is accepted for descriptive trajectories. With a non-model test, model covariates, subject fields, and `comparison.at_time` fail rather than being ignored.

## Processing behavior

Technical repeats are averaged within condition, time and independent unit before inference. Descriptive trajectories retain means, SDs, independent-unit counts and missing counts. Paired t requires explicit complete pair mapping and at least two complete pairs; independent tests require two units per group; ANOVA requires three conditions and at least two measured independent units in every listed condition. Model variants use the explicitly supplied design; they do not select models automatically.

### Model variants and covariates

`linear_model` fits an explicitly encoded fixed-effect design. `mixed_model` adds a subject random intercept, fitted by REML with asymptotic Wald inference; it requires at least three subjects and repeated observations for at least two subjects. It does not fit random slopes, serial correlation, or a small-sample degrees-of-freedom correction. `moderated_t` moderates feature variances across the selected family, using a non-robust, non-trended scaled-inverse-chi-square prior, and needs at least three eligible finite OLS residual variances; ineligible features retain unavailable contrasts. All model comparisons use explicit, different `left_condition` and `right_condition`; `pair_id` is rejected here because it belongs to `paired_t`.

The optional `model.covariates` accepts at most 16 named numeric or categorical covariates. Numeric values must be finite and have no reference category. Categorical covariates need a present reference category and at least two observed levels; non-reference levels are dummy encoded. `include_time` requires time for every sample. A condition-time interaction additionally requires `comparison.at_time`; its contrast is the left-minus-right condition contrast at that supplied time. The design has at most 32 unambiguous columns. Missing responses are excluded feature-by-feature; missing design values and rank-deficient designs are not imputed.

For each selected row, `p_value_bh` is Benjamini–Hochberg corrected across all finite, testable p values in that selected feature family before pagination. Untestable rows keep null p values and do not enter that family. It is not correction across separate requests. `effect_mean_difference` is left minus right (or model contrast) on the selected scale. On log2, a baseline fold change is `2^(mean difference)`, a geometric-mean ratio.

## Outputs and side effects

Every row returns trajectories, warnings, test status, unit counts, raw and BH p values, effect, confidence fields where supported, and optional baseline changes. ANOVA, descriptive-only and unavailable rows have null effect/interval as appropriate. Result summary gives selected family size, tested feature count and sample-mapping count. The operation is read-only.

## Edge cases and errors

Normalized missing values are never replaced by raw values. Incompatible `value_unit`/`value_basis` among selected source-result samples rejects analysis. Confidence intervals are pointwise, not simultaneous across features; Mann–Whitney and omnibus ANOVA do not receive a mean-difference interval. No imputation, random slopes, serial correlation, small-sample mixed-model correction, robust/trended empirical Bayes, or automatic scaling occurs.

## Worked examples

### Log2 baseline

If baseline mean on the log2 scale is 3 and treatment mean is 4, baseline change is +1 and fold change 2. A zero raw measurement becomes missing before repeats are averaged, rather than `log2(0)` or zero.

### Selected-family correction

If three selected rows produce two finite p values and one untestable row, BH uses the two finite values only; the third row's `p_value_bh` remains null. Selecting a different `row_ids` family is a different correction family.

{{ git_page_authors }}
