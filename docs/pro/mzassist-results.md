# Explore and evaluate results

Use mzassist with a completed mzmine feature table to investigate an analytical question.
Keep the project open; the assistant can list tables and help you choose the intended output.

## Choose the table and the question

For example:

> Use the final aligned table. Help me identify features that are reproducibly detected in my samples
> and weak in the blanks. Explain the criteria before selecting candidates.

Confirm which table contains the appropriate processing and annotations. Intermediate aligned,
filtered, normalized, or correlation tables can describe the same samples. Their names and row counts
do not make them separate experimental conditions.

Approve the [result-sharing request](mzassist-data-sharing.md). Share only the additional information
needed for the task, such as sample names to confirm a mapping or chromatograms to inspect peak shape.

## Define samples and groups

Check **Project → Sample metadata** before comparing conditions. Prepare condition, batch,
independent-sample identifier, and any time or pairing information required by the analysis.
[Sample metadata](../module_docs/project_metadata/project_metadata.md) explains how to import and edit it.

QC, blank, and sample roles describe analytical use; they do not identify treatment or biological
condition. Two injections of one sample are technical repeats, not two independent biological
replicates. Ask the assistant to show the proposed mapping and correct it before calculating.

## Inspect candidate features

1. Agree a selection criterion appropriate for the question, such as blank contribution, detection
   across replicates, a mass range, or annotation evidence.
2. Ask for a manageable set of candidate rows and the reasons they were selected.
3. Open representative rows in mzmine. Inspect peak boundaries, coelution, mass accuracy,
   chromatograms, MS/MS, isotope/adduct relationships, and blank behavior as relevant.
4. Record which candidates to retain, exclude, or investigate further, with reasons.

Requests return limited pages of rows and evidence. An initial shortlist is not the complete table;
request the remaining rows when completeness matters. A missing signal or unavailable measurement
must not silently become zero.

## Choose a calculation

The [scientific-analysis guide](scientific-analysis.md) helps choose quantification, batch diagnostics,
study comparison, activity association, or an exposure calculation. These run in mzmine and can be
opened in native result views.

For normalization, review the [Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md)
settings separately. Confirm whether the subsequent analysis uses raw area/height or an existing
normalized column. A normalization job can finish while some values remain unavailable; inspect its
diagnostics instead of assuming that every feature was corrected.

## Export a reviewed selection

Ask mzassist to prepare the rows you want to export and inspect that selection. Choose the output
folder in mzmine to keep its path local, or deliberately supply a path in chat. The destination must
already exist and be writable.

Reviewed exports can include feature CSV, a selection or comparison record, and a PDF or HTML report.
Check the reported completed files and open them. Selecting an export option alone does not create
an output file. Scientific calculation views have their own CSV and calculation-record export
controls; see [Save and reproduce your work](mzassist-saving.md).

{{ git_page_authors }}
