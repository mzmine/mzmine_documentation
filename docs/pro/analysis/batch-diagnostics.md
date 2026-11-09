# Check an analytical batch

Use batch diagnostics to inspect QC precision, reference mass and retention-time deviations,
internal-standard responses, and possible carryover in one analytical batch. It describes the
measurements to investigate; it does not correct data or accept/reject a batch for your laboratory.

## Prepare the sequence

Provide the injection order and confirm which injections belong to this batch. Distinguish samples,
QCs, blanks, and standards. Check the order against the acquisition sequence; the order of rows in a
feature table is not an injection sequence. Approve run-order sharing when requested.

For reference checks, identify the appropriate feature rows and supply expected m/z or retention
time. For internal-standard response checks, confirm that the added amounts are comparable.
Choose raw area/height or an existing normalized measurement deliberately.

Carryover assessment needs the complete sequence and a blank immediately following the relevant
injection. A sequence with omitted injections cannot establish that adjacency.

For example, this **illustrative sequence** supports inspection of the blank after Sample-1:

| Injection order | Sample | Role |
| --- | --- | --- |
| 1 | QC-1 | QC |
| 2 | Sample-1 | Sample |
| 3 | Blank-1 | Blank |
| 4 | QC-2 | QC |
| 5 | Sample-2 | Sample |
| 6 | QC-3 | QC |

Use your actual sequence and method-specific alert criteria. The example is not a recommended QC
schedule or an acceptance rule.

## Ask mzassist

> Inspect this single batch using the complete injection order. Report QC precision and possible
> carryover, and show which observations support each flag. Ask me for expected reference values or
> alert thresholds if they are needed.

## Interpret the output

Check which QC observations contribute to each statistic. Missing, estimated, or aggregated signals
do not automatically count as detected QC observations. Inspect flagged chromatograms and reference
assignments before attributing a deviation to the instrument.

A separate QC-drift request can describe abundance versus run order. It needs at least three usable
QC injections and does not correct measurements. For a correction, configure the
[Intensity normalizer](../../module_docs/norm_intensity/norm_intensity.md) separately and inspect the
normalized output.

Save the diagnostic table and calculation record, including the sequence and thresholds used.
See [Save and reproduce your work](../mzassist-saving.md).

{{ git_page_authors }}
