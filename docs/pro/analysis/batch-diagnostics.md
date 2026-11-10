# Batch diagnostics {#check-an-analytical-batch}

Batch diagnostics help you examine QC precision, reference mass and retention-time deviations, internal-standard responses, and possible carryover within one analytical batch. It highlights measurements to investigate; it does not correct data or accept or reject a batch for your laboratory.

## What you need {#prepare-the-sequence}

The injection order and batch membership are needed to interpret trends and carryover. Distinguish samples, QCs, blanks, and standards, and check the sequence against acquisition records: the display order of files does not establish their acquisition sequence. Carryover assessment requires the complete sequence and a blank immediately following the relevant injection; omitted injections cannot establish adjacency.

Reference checks need the relevant feature rows and expected m/z or retention time. Internal-standard response checks require comparable added amounts. Choose raw area, height, or an existing normalized measurement and provide method-specific alert criteria.

This **illustrative sequence** supports inspection of the blank after Sample-1; it is not a recommended QC schedule or acceptance rule:

| Injection order | Sample | Role |
| --- | --- | --- |
| 1 | QC-1 | QC |
| 2 | Sample-1 | Sample |
| 3 | Blank-1 | Blank |
| 4 | QC-2 | QC |
| 5 | Sample-2 | Sample |
| 6 | QC-3 | QC |

## Calculate with mzassist {#ask-mzassist}

1. Ask mzassist to inspect the batch. For example:

    > Inspect this single batch using the complete injection order. Report QC precision and possible carryover, and show which observations support each flag. Ask me for expected reference values or alert thresholds if needed.

2. Let mzassist read approved existing metadata, including run order when requested. Supply missing sequence, reference, and threshold information. If needed, edit metadata under **Project → Sample metadata**; see [Sample metadata](../../module_docs/project_metadata/project_metadata.md).
3. Confirm the proposed sequence, sample roles, measurement, and diagnostic choices in chat. Ask mzassist to calculate and open the results.
4. Check which QC observations contribute to each statistic and inspect flagged chromatograms and reference assignments. Missing, estimated, or aggregated signals do not automatically count as detected QC observations.
5. Use **Save table (CSV)** and **Save calculation record (JSON)** in the result view. See [Save and reproduce your work](../mzassist-saving.md).

## Interpretation {#interpret-the-output}

A separate QC-drift request can describe abundance versus run order. It needs at least three usable QC injections and does not correct measurements. For correction, ask mzassist to help prepare a separate normalization step and inspect its output. The manual workflow is described in [Intensity normalizer](../../module_docs/norm_intensity/norm_intensity.md).

{{ git_page_authors }}
