# AI-assisted mzmine with mzassist {#agent-assisted-mzmine}

**mzassist** connects your AI assistant to mzmine. You can describe an analytical question in chat,
ask for help choosing processing settings, and inspect the resulting data in mzmine. Calculations
run in mzmine on your computer. The assistant receives the information returned by mzassist,
including any measurements or metadata you choose to share.

Start with [Set up mzassist](mzassist-setup.md), then follow
[Process your first dataset](mzassist-first-analysis.md). You can also use mzassist with an already
processed project; importing and processing again is not required to explore its results.

## What can I ask?

| Your task | Example request | Guide |
| --- | --- | --- |
| Understand a setting | “Explain how the minimum feature height affects detection, and show me the documentation.” | Ask a question in chat |
| Process raw data | “Help me turn these LC-MS files into an aligned feature table. Let me review the method before processing.” | [First analysis](mzassist-first-analysis.md) |
| Improve a method | “Estimate suitable settings from these data and explain the changes.” | [Processing methods](mzassist-methods.md) |
| Review a completed table | “Help me inspect features that are strong in samples and weak in blanks.” | [Explore results](mzassist-results.md) |
| Check analytical quality | “Review QC precision and possible carryover in this injection sequence.” | [Batch diagnostics](analysis/batch-diagnostics.md) |
| Compare study conditions | “Compare treatment and control, keeping repeat injections of the same sample together.” | [Study comparisons](analysis/study-comparison.md) |
| Build a library from standards | “Help me generate a spectral library from these reference standards and their compound table.” | [Library generation](mzassist-methods.md#spectral-library-search-and-library-generation) |

These are examples of how to describe your goal, not commands that must be copied exactly. Include
information that changes the method: acquisition type, polarity, ion mobility, sample roles, and
whether your goal is feature discovery, annotation, quantification, or a comparison.

## Connect and choose what to share

Open **mzassist → Agent activity** to check the connection and pending activities. Connecting does
not start a processing job. The assistant can discover feature-table names and counts; sharing
sample metadata or measured results requires a separate decision.

Use the file chooser in mzmine to keep file and folder paths out of the conversation. If you paste
a path or sample information into chat, that text is visible to your assistant/provider.
Read [Data sharing and agent controls](mzassist-data-sharing.md) before working with confidential data.

### Optional acquisition metadata sharing {#optional-acquisition-header-sharing}

Acquisition metadata comes from imported file headers, such as instrument-model, mass-analyzer,
ion-source, and detector descriptions. It is read-only and separate from sample metadata such as
condition or replicate. You can share a summary when it helps choose the method.

In the sharing review, **Share acquisition metadata (file-header text)** starts unchecked.
Inspect the preview before approving it: header text is not standardized and may contain names,
paths, or other sensitive information. Missing or shortened fields do not establish that an
instrument component is absent. Changing the included fields requires a new review.

## Build, review, and run a workflow

Tell the assistant whether you want a complete analysis, a proposed method to inspect, or one
specific edit. For example: “Change the alignment tolerance only; keep the other settings.”

1. Describe the goal and choose the files in mzmine.
2. Check the proposed workflow, including annotation and export choices.
3. Estimate settings or optionally optimize them, then inspect the changes.
4. Review the processing summary and authorize the run when ready.
5. Inspect the feature table and representative chromatograms before interpreting the results.

Applying settings does not start the processing batch. Estimation can update the wizard; optimization
returns candidate settings to inspect. You can take over editing in mzmine and then continue in chat.
If the project or method changes, mzassist may need a fresh review.
See [Build and improve a method](mzassist-methods.md).

## Feature tables, evidence, and results

Choose the table that answers your question and approve the information to share.
The assistant can help find rows, define comparison groups, inspect evidence, and open the
corresponding views in mzmine. State experimental groups explicitly: an aligned table and a
correlation table are processing outputs, not two study conditions.

Results are returned in limited pages. Ask for additional rows or open the table in mzmine before
treating a shortlist as a complete inventory. Inspect chromatography, spectra, blanks, replicate
behavior, and annotation evidence. A library match is evidence for an annotation, not confirmed identity.
See [Explore and evaluate results](mzassist-results.md).

mzassist can also rename or delete tables. Deletion removes the table from the current project;
save a project copy before deleting anything you may need again.

### Normalization

mzassist uses the native [Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md).
Choose the measurement and correction method deliberately, preserve the original values, and inspect
the resulting normalized columns. A QC-drift diagnostic describes a trend; it does not correct it.

### Spectral-library search and library generation

Searching a library compares features against existing reference spectra. Generating a library
uses your own reference-standard measurements and a compound table. mzassist supports both tasks.
A library-generation readiness check verifies the supplied setup; it does not create a library or
confirm the identity of the standards. See [Library workflows](mzassist-methods.md#spectral-library-search-and-library-generation).

## Limits and troubleshooting

Use [Troubleshooting](mzassist-troubleshooting.md) for connection problems, missing setup files,
changed reviews, or interrupted jobs. **Pause agent changes** blocks new changes while submitted
mzmine tasks keep running. Cancel a job separately if it must stop.

Save the [project, method, and exported results](mzassist-saving.md) you need before ending the
session. A chat response alone is not a saved mzmine analysis.

{{ git_page_authors }}
