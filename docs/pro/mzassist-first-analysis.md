# Process your first dataset with mzassist

This walkthrough uses two small, public LC-MS/MS workshop files to practice importing data,
reviewing a method, processing, inspecting features, and saving your work. Complete
[Set up mzassist](mzassist-setup.md) first.

## Download the example files

Download these two QC extracts from the mzmine project's public workshop test dataset and place
them together in a new folder:

- [QC 04 — 171103_PMA_TK_QC_04-4to5min.mzML](https://raw.githubusercontent.com/mzmine/mzmine/b440bccf29c1cead1fb46d6003f859ac1416edc0/mzmine-community/src/test/resources/rawdatafiles/integration_tests/workshop_dataset/171103_PMA_TK_QC_04-4to5min.mzML)
- [QC 05 — 171103_PMA_TK_QC_05-4to5min.mzML](https://raw.githubusercontent.com/mzmine/mzmine/b440bccf29c1cead1fb46d6003f859ac1416edc0/mzmine-community/src/test/resources/rawdatafiles/integration_tests/workshop_dataset/171103_PMA_TK_QC_05-4to5min.mzML)

Each file is about 4 MB and contains only the 4–5 minute portion of a positive-mode Q Exactive
LC-MS/MS acquisition. These are two QC injections, not treatment and control groups. Use them to
learn the workflow; they cannot establish batch-wide drift, a biological difference, or the quality
of the complete chromatographic run.

## Import in mzmine

Save any existing project before starting a separate practice project. In your assistant chat, ask:

> Help me process the two public workshop QC extracts into an aligned feature table. Let me select
> the folder in mzmine, and stop for my review before running the processing batch.

Choose the example folder in the mzmine file chooser. Check that only the two mzML files are
selected, then complete the import. Do not import the repository's test metadata or batch files;
those serve separate automated tests.

**Check in mzmine:** two raw data files should be loaded. Open a raw-data view and check that the
chromatographic data cover approximately 4–5 minutes. Using the native chooser keeps your local
folder path out of chat.

## Prepare a simple method

Tell the assistant:

> These are positive-mode LC-MS/MS QC extracts from a Q Exactive, without ion mobility. Use a DDA
> feature-detection and alignment workflow. Keep the result in mzmine. For this practice run, omit
> library matching, specialized annotation, networking, normalization, and external exports.

This keeps the first run focused on finding and aligning chromatographic features. Review the
proposal in chat or open the processing wizard for a closer look. Check:

- The two selected files, positive polarity, and no ion mobility.
- A mass-spectrometer preset appropriate for Q Exactive data and the DDA workflow.
- A retention-time selection that includes the supplied 4–5 minute segment.
- Peak-width, noise, minimum-height, and alignment settings suitable for the visible signals.
- No comparison groups or filters requiring study samples that are absent from this QC-only example.

You can ask for parameter estimates and inspect their changes, but the cropped segment does not
represent a complete run. Do not use it to infer a full-run gradient or copy its estimated settings
unchanged to another dataset. Optimization needs at least three files and is outside this two-file
example. See [Build and improve a method](mzassist-methods.md) for those steps on a suitable dataset.

## Review and run

Ask the assistant to summarize the final method and files. Confirm that the output is a feature
table kept in mzmine, then authorize processing when the summary is correct.

Follow progress in **mzassist → Agent activity** or chat. Wait for the processing job to finish
before submitting another request. If it fails, inspect the reported step and existing outputs
before rerunning; [Troubleshooting](mzassist-troubleshooting.md) explains common cases.

## Inspect the result

**Expected output:** an aligned feature table containing measurements from the two QC extracts.
The number of rows depends on the reviewed method and software version; a large feature count
alone is not a quality criterion.

Ask:

> Open the final aligned table in mzmine. Help me inspect a strong feature detected in both files
> and a weaker feature. Explain what to check in their chromatograms.

You can inspect the table entirely in mzmine. If the assistant needs measurements or plots to
answer, inspect and approve the [result-sharing request](mzassist-data-sharing.md) first.
Check peak boundaries, shape, alignment between the two injections, and available MS/MS evidence.
No library matching was requested, so an unannotated feature is not a processing failure.

Do not turn the two QC injections into independent biological groups or use this example for a
carryover analysis: it contains no complete injection sequence or blanks.

## Save and continue

1. Save the practice project in mzmine.
2. Save the reviewed wizard preset and the batch actually used for the resulting table.
3. If you export a selection, check that export finished and open the output files.

Follow [Save and reproduce your work](mzassist-saving.md). With your own study data, add the real
sample metadata, review the annotation strategy, and choose an appropriate
[results analysis](scientific-analysis.md).

{{ git_page_authors }}
