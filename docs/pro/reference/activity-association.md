# Activity association: implementation reference

This reference documents `activity_association` in the reviewed knowledge-pack snapshot of the mzmine 4.10.107 development series. See the [scientific-analysis overview](../scientific-analysis.md).

## Inputs and prerequisites

Provide non-empty `samples` mapping `sample_id`, `condition`, and `independent_unit`, plus non-empty `assay_rows`. Each assay row supplies a mapped sample, one shared `endpoint`, `dose`, `context`, `direction`, and finite `activity`. `direction` is `higher_is_more_active` or `lower_is_more_active`. `row_ids` defaults to every snapshot row. A compatible quantification source result may supply measurements.

## Parameters and validation

`association` is optional and defaults to `pearson`; `spearman` is the alternative. The optional measurement chooses a field and `include_estimated` policy; its default field is raw area. Unlike study comparison, activity association does not accept `measurement.transform`, so a requested log2 transformation is invalid rather than applied. Duplicate/out-of-scope sample IDs fail. A single independent unit may not occur across different condition/time groups, avoiding an association that treats cross-group repeats as independent. Mixed endpoint, dose, context, or direction fails; split those assays first.

## Processing behavior

Repeated assay rows are averaged per independent unit. Feature values are likewise averaged from valid mapped measurements per unit. Only units with both values enter the association. Pearson or Spearman correlation is calculated on these paired unit means; the output also orientates `priority_score` so positive priority means association in the declared more-active direction (the sign is reversed for `lower_is_more_active`).

At least three matched independent units are required. Constant or otherwise undefined vectors produce `constant_or_undefined_values`, not a coefficient. There is no p value. A 95% interval is reported only for Pearson correlation with more than three pairs and an absolute correlation below one, using the Fisher transformation. Result rows sort by descending numeric priority score; unavailable scores come last, with `row_id` breaking ties.

## Outputs and side effects

Each feature row reports paired observations, matched-unit count, association coefficient, confidence interval when available, `priority_score`, and `association_status`. It does not calculate or report a p value. Rows are ranked for review by the association result; the result records endpoint, dose, context and direction. It never edits the snapshot.

## Edge cases and errors

Missing, invalid, non-finite, negative or excluded measurements are not imputed; their units simply do not pair. Estimated values remain excluded unless explicitly included. A correlation ranks covariation only: it does not identify a compound, establish causality, dose response, or biological mechanism.

## Worked examples

### Direction-aware ranking

With `lower_is_more_active`, a feature correlation of -0.8 becomes a positive 0.8-oriented priority score, because increasing feature abundance tracks lower activity values, declared to mean more activity.

### Technical repeats

Two assay measurements 40 and 60 for one independent unit become activity 50. Two valid feature measurements in the same unit are also averaged before pairing; a missing feature replicate does not become zero.

{{ git_page_authors }}
