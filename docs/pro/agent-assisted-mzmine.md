# AI-assisted mzmine with mzassist {#agent-assisted-mzmine}

**mzassist** connects your AI assistant to mzmine. You can describe an analytical question in chat,
ask for help choosing processing settings, and inspect the resulting data in mzmine. Calculations
run in mzmine on your computer. The assistant receives the information returned by mzassist,
including any measurements or metadata you choose to share.

Start with [Set up mzassist](mzassist-setup.md), read
[Data sharing and agent controls](mzassist-data-sharing.md), then follow
[Process your first dataset](mzassist-first-analysis.md). You can also use mzassist with an already
processed project; importing and processing again is not required to explore its results.

## What can I ask?

| Your task | Example request | Guide |
| --- | --- | --- |
| Understand a setting | “Explain how the minimum feature height affects detection, and show me the documentation.” | Ask a question in chat |
| Process raw data | “Help me turn these LC-MS files into an aligned feature table. Let me review the method before processing.” | [Process your first dataset](mzassist-first-analysis.md) |
| Improve a method | “Estimate suitable settings from these data and explain the changes.” | [Build and improve a method](mzassist-methods.md) |
| Review a completed table | “Help me inspect features that are strong in samples and weak in blanks.” | [Explore and evaluate results](mzassist-results.md) |
| Check analytical quality | “Review QC precision and possible carryover in this injection sequence.” | [Batch diagnostics](analysis/batch-diagnostics.md) |
| Compare study conditions | “Compare treatment and control, keeping repeat injections of the same sample together.” | [Study comparison](analysis/study-comparison.md) |
| Build a library from standards | “Help me generate a spectral library from these reference standards and their compound table.” | [Build and improve a method](mzassist-methods.md#spectral-library-search-and-library-generation) |

These are examples of how to describe your goal, not commands that must be copied exactly.
mzassist can inspect the data and information already in your project, with your sharing approval,
and ask about missing details. You do not need to transcribe the whole experiment before starting.

Available tasks depend on your installed mzmine and mzassist versions and account features.
The assistant checks what your running mzmine supports before preparing a task.

## Connect and choose what to share

Open **mzassist → Agent activity** to check the connection and pending activities. Connecting does
not start a processing job. The assistant can discover feature-table names and counts; sharing
sample metadata or measured results requires a separate decision. If the connection was turned off,
click **Enable local connection** on this page. The **Enable local connection when mzmine starts**
checkbox is selected by default.

Use the file chooser in mzmine to keep file and folder paths out of the conversation. If you paste
a path or sample information into chat, that text is visible to your assistant/provider.
Read [Data sharing and agent controls](mzassist-data-sharing.md) before working with confidential data.

### Optional acquisition metadata sharing {#optional-acquisition-header-sharing}

Acquisition metadata comes from imported file headers, such as instrument-model, mass-analyzer,
ion-source, and detector descriptions. It is read-only and separate from sample metadata such as
condition or replicate. You can share a summary when it helps choose the method.

When mzassist needs this information, it explains what it wants to read and asks for sharing
approval in chat. You can approve or decline there. To inspect the contents privately first, reply
“Open this sharing request in mzmine.” mzassist opens the pending review for you; you do not need
to find a setting before making your request.

In the native review, **Share acquisition metadata (file-header text)** starts unchecked. A chat
approval covers this summary when it is included in the request; it does not depend on that checkbox. Header
text is not standardized and may contain names, paths, or other sensitive information. Missing or
shortened fields do not establish that an instrument component is absent. See
[Review a sharing request](mzassist-data-sharing.md#review-a-sharing-request) for the optional
manual route and when its review button is available.

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

Describe your question in chat, for example: “Help me inspect the final table from the last
processing run.” mzassist checks the available tables and identifies the relevant output. If the
choice is unclear, it asks you to clarify in chat. Before reading measurements, it explains which
table and information it wants to share and asks for approval, unless you have already approved
that access. Respond in chat, or ask mzassist to open the pending sharing review in mzmine first.
You do not need to select a table in the mzmine interface to start this conversation.

Once sharing is approved, mzassist can help find rows, define comparison groups, inspect evidence,
and open the corresponding views in mzmine. Tell it which experimental conditions you want to
compare. For example, treatment and control are study groups; aligned and correlation tables can
be different processing stages for those same samples.

Ask mzassist to explain why it selected a candidate and to open its chromatograms or spectra in
mzmine. Compare peak shape, blanks, repeat measurements and annotation evidence before choosing
features for follow-up. See [Explore and evaluate results](mzassist-results.md), including
the guidance on [interpreting measurements and annotations](mzassist-results.md#interpreting-results).

mzassist can also rename or delete tables. Deletion removes the table from the current project;
save a project copy before deleting anything you may need again.

### Normalization

mzassist uses the native [Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md).
Choose the measurement and correction method deliberately, preserve the original values, and inspect
the resulting normalized columns. A QC-drift diagnostic describes a trend; it does not correct it.

### Spectral-library search and library generation

Searching a library compares features against existing reference spectra. Generating a library
uses your own reference-standard measurements and a compound table. mzassist supports both tasks.
See [Library workflows](mzassist-methods.md#spectral-library-search-and-library-generation) for the
readiness check and the steps to generate and save a library.

## Limits and troubleshooting

Use [Troubleshooting](mzassist-troubleshooting.md) for connection problems, missing setup files,
changed reviews, or interrupted jobs. To take over editing, ask mzassist to pause, or open
**mzassist → Agent activity** and click **Pause agent changes**. Submitted processing keeps
running; ask mzassist to cancel the job if it must stop.

Save the [project, method, and exported results](mzassist-saving.md) you need before ending the
session.

{{ git_page_authors }}
