# Study comparison {#compare-study-conditions}

A study comparison summarizes feature measurements across conditions or time points and can calculate a specified statistical test when the design supports it. Begin with one shared feature table containing the samples to compare.

## What you need {#prepare-the-study-design}

The design identifies each sample's condition and independent experimental unit, plus time, pairing, or covariates when required by the question. An independent unit might be a biological specimen or a separately prepared experimental sample; it is not automatically each raw data file. A QC label or filename alone does not define the comparison.

This **illustrative mapping** shows two injections of the same control sample as one independent unit; it is not a recommended study size:

| Injection | Condition | Independent unit |
| --- | --- | --- |
| C01-injection-1 | Control | C01 |
| C01-injection-2 | Control | C01 |
| C02-injection-1 | Control | C02 |
| T01-injection-1 | Treatment | T01 |
| T02-injection-1 | Treatment | T02 |

## Choose the measurement and analysis

Measurements can be raw area, height, existing normalized values, or a compatible quantification result. Technical repeats are averaged within condition, time, and independent unit. Optional log2 transformation happens before averaging; nonpositive measurements then remain missing.

Descriptive output is a useful start if the design is unresolved. Supported tests include Welch/Student t tests, Mann–Whitney, paired t, one-way ANOVA, covariate-adjusted linear models, subject random-intercept mixed models, and moderated tests. Review the assumptions with mzassist to decide whether a test or model fits your study. Paired tests need complete pair mappings, independent tests need independent replicates, and ANOVA needs at least three conditions.

## Calculate with mzassist

1. Ask mzassist to compare the conditions. For example:

    > Compare treatment with control using raw area. First show the sample mapping, how technical repeats will be handled, and a descriptive summary. Explain the assumptions of a proposed test before running it.

2. mzassist checks the metadata you approved for sharing. Provide only the study-design facts it still needs. If needed, edit metadata under **Project → Sample metadata**; see [Sample metadata](../../module_docs/project_metadata/project_metadata.md).
3. Confirm the sample mapping, measurement, transformation, and analysis in chat. Ask mzassist to calculate and open the results.
4. Inspect group summaries, independent-unit counts, missing measurements, effect estimates, confidence intervals where available, and test status. Some features may have unavailable calculations while others have valid results. Examine important feature rows in mzmine.
5. Use **Save table (CSV)** and **Save calculation record (JSON)** in the result view, preserving the feature selection, design, transformation, test, and exclusions.

## Interpretation {#review-the-comparison}

Benjamini–Hochberg adjusted p values are calculated across the valid, testable features selected for that analysis. Selecting a shortlist first changes that family; separate analyses do not share one automatic correction.

There is no automatic imputation, model selection, random-slope fitting, serial residual-correlation model, small-sample mixed-model correction, or simultaneous confidence interval. Review the model and selected features before interpreting evidence of a difference.

{{ git_page_authors }}
