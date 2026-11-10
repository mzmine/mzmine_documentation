# Explore and evaluate results

Use mzassist with a completed mzmine feature table to investigate an analytical question.
Keep the project open and describe your question in chat. mzassist checks the available tables;
you do not need to select one in mzmine before asking.

## Choose the table and the question

For example:

> Use the final aligned table. Help me identify features that are reproducibly detected in my samples
> and weak in the blanks. Explain the criteria before selecting candidates.

mzassist identifies the relevant output and explains its choice. If several tables could fit, it
asks you to clarify in chat. Intermediate aligned, filtered, normalized, or correlation tables can
describe the same samples; their names and row counts do not make them separate experimental conditions.

Before reading measurements that you have not already approved for sharing, mzassist prepares a
[result-sharing request](mzassist-data-sharing.md#review-a-sharing-request). It names the table and
explains the information needed, such as sample names to confirm a mapping or chromatograms to
inspect peak shape. Approve or decline in chat, or ask it to open the pending review in mzmine
so you can inspect and adjust the selection there.

## Define samples and groups

Tell mzassist which conditions you want to compare. It can check the sample information already
in the project, after you approve metadata sharing, and help add missing assignments. For example:

> Compare treatment with control. Check the existing sample information and show me which
> injections belong to each condition and independent sample. Ask me about missing or ambiguous
> assignments, and help me save the confirmed information in mzmine.

Check the proposed mapping against your sample sheet. This matters because a QC or blank label
describes analytical use, not a treatment group. Two injections of the same specimen are technical
repeats; counting them as independent biological samples would exaggerate the amount of evidence.
Time points and pairing are needed only when your question uses them.

You can provide missing information in chat or ask mzassist to help import a sample sheet.
Manual editing is optional: **Project → Sample metadata** opens the table in mzmine. The
[Sample metadata guide](../module_docs/project_metadata/project_metadata.md) covers that editor.

## Inspect candidate features

1. Agree a selection criterion appropriate for the question, such as blank contribution, detection
   across replicates, a mass range, or annotation evidence.
2. Ask for a manageable set of candidate rows and the reasons they were selected.
3. Ask mzassist to open representative rows in mzmine. Inspect peak boundaries, coelution, mass accuracy,
   chromatograms, MS/MS, isotope/adduct relationships, and blank behavior as relevant.
4. Record which candidates to retain, exclude, or investigate further, with reasons.

A shortlist helps you choose candidates for closer inspection; it is not a count of everything
detected in the experiment. If your goal is an inventory, state that when describing the task.
An unavailable measurement means that no usable value is available for that sample and feature;
it does not establish zero concentration or chemical absence.

## Choose a calculation

The [scientific-analysis guide](scientific-analysis.md) helps choose quantification, batch diagnostics,
study comparison, activity association, or an exposure calculation. These run in mzmine and can be
opened in native result views.

For normalization, ask mzassist to explain a suitable correction and show the settings before
applying it. Confirm whether the comparison should use raw or normalized measurements. The
[Intensity normalizer guide](../module_docs/norm_intensity/norm_intensity.md) explains the available
methods and their manual setup. Some measurements may remain unavailable after correction; the
diagnostics explain which values could not be normalized.

## Export a reviewed selection

Ask mzassist to prepare the rows you want to export and inspect that selection. Choose the output
folder in mzmine to keep its path local, or deliberately supply a path in chat. The destination must
already exist and be writable.

Reviewed exports can include feature CSV, a selection or comparison record, and a PDF or HTML report.
Check the reported completed files and open them. Selecting an export option alone does not create
an output file. Scientific calculation views have their own CSV and calculation-record export
controls; see [Save and reproduce your work](mzassist-saving.md).

{{ git_page_authors }}
