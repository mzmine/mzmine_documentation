# Compare study conditions

Use a study comparison to summarize feature measurements across conditions or time points and,
when the design supports it, calculate a specified statistical test. Begin with one shared feature
table containing the samples to compare.

## Prepare the study design

For every selected sample, identify its condition and independent experimental unit. Add time,
pairing, or covariates when required by the question. An independent unit might be a biological
specimen or a separately prepared experimental sample; it is not automatically each raw data file.

For example, two injections of the same control sample have one independent-unit identifier:

| Injection | Condition | Independent unit |
| --- | --- | --- |
| C01-injection-1 | Control | C01 |
| C01-injection-2 | Control | C01 |
| C02-injection-1 | Control | C02 |
| T01-injection-1 | Treatment | T01 |
| T02-injection-1 | Treatment | T02 |

This is a mapping illustration, not a recommendation for study size. Prepare the actual design in
[Sample metadata](../../module_docs/project_metadata/project_metadata.md), then confirm the mapping
that mzassist will use. A QC label or filename alone does not define the comparison.

## Choose the measurement and analysis

Choose raw area, height, existing normalized values, or a compatible native quantification result.
Technical repeats are averaged within condition, time, and independent unit. Optional log2
transformation happens before that averaging; nonpositive measurements then remain missing.

Start with descriptive output if the design is unresolved. Supported tests include Welch/Student
t tests, Mann–Whitney, paired t, one-way ANOVA, covariate-adjusted linear models, subject
random-intercept mixed models, and moderated tests. mzassist does not automatically establish
which test or model is scientifically appropriate. Paired tests need complete pair mappings;
independent tests need independent replicates, and ANOVA needs at least three conditions.

> Compare treatment with control using raw area. First show the sample mapping, how technical
> repeats will be handled, and a descriptive summary. Explain the assumptions of a proposed test
> before running it.

## Review the comparison

Inspect group summaries, independent-unit counts, missing measurements, effect estimates and
confidence intervals where available, and the reported test status. A calculation may be unavailable
for some features even when other features have valid results.

Benjamini–Hochberg adjusted p values are calculated across the valid, testable features selected for
that analysis before the results are paged. Selecting a shortlist first changes that family;
separate analyses do not share one automatic correction.

There is no automatic imputation, model selection, random-slope fitting, serial residual-correlation
model, small-sample mixed-model correction, or simultaneous confidence interval. Review the
appropriateness of the model and the selected features before interpreting evidence of a difference.

Open important feature rows in mzmine and save the result table and calculation record. Record the
feature selection, design, transformation, test, and exclusions with the reported results.

{{ git_page_authors }}
