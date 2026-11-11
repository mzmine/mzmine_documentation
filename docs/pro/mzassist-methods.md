# Build and improve a method {#build-and-improve-a-processing-method}

mzassist works with the [processing wizard](../wizard.md) and mzmine's processing modules.
Start by stating the analytical goal, acquisition type, polarity, ion mobility, and the output you
need. If a method is already configured, say whether to retain it or design a replacement.

## Choose how much to delegate

| Goal | Example request |
| --- | --- |
| Design a method for inspection | “Prepare an LC-MS workflow and explain the main settings. Stop before processing.” |
| Process a dataset | “Help me process these files into an aligned feature table. Include a method review.” |
| Make one change | “Change only the retention-time alignment tolerance. Keep all other settings.” |
| Resume after manual editing | “I edited the wizard in mzmine. Read the current settings before continuing.” |

Review the selected files, acquisition settings, feature-detection thresholds, alignment, annotation
strategy, and exports. Optional stages should answer your analytical question: library matching,
lipid annotation, networking, and library generation serve different purposes.

## Estimate settings from the data

Ask mzassist to estimate settings after selecting the appropriate wizard presets and files.
Estimation measures representative data and can update settings such as peak width, noise,
mass tolerance, and minimum feature height. Inspect the before/after values and the corresponding
chromatography before accepting them as suitable for your method.

Estimation updates the wizard when its starting settings are still current; it does not start the
full processing batch. It can replace MS1 mass lists and reset wizard customization. Preserve any
customized method you need before estimating. See
[Estimate wizard parameters](../module_docs/wizard_optimizer/wizard_estimate.md) for supported data,
representative-file selection, and side effects.

## Optimize when estimation is not sufficient

Optimization runs candidate workflows on representative files and scores their results. Ask for it
when you want to compare settings, and specify the available time and what good results mean for
your method. Review candidate settings and native evidence before applying one.

A higher score does not necessarily mean a better method for every analyte. Check weak peaks,
coelution, blanks, mass/retention-time tolerances, and memory requirements before processing all files.
See [Optimize wizard parameters](../module_docs/wizard_optimizer/wizard_optimize.md).

## Review and process

Review the method summary in chat, especially the selected files, annotation steps and export
destinations. If you requested a review before processing, tell mzassist to start when you are
satisfied. You do not need to open the batch editor to run the reviewed method.

Ask “How is processing progressing?” for a status update, or open **mzassist → Agent activity**
in mzmine to see the job. If processing is interrupted, ask mzassist to check what finished and
explain how to continue; completed outputs may still be present.

For an optional manual inspection, ask mzassist to open the method or batch review in mzmine.
The normal editors are **mzwizard → Processing wizard** and **Project → Batch mode**. These are
also described in the [processing wizard](../wizard.md) and
[batch-processing guide](../workflows/batch_processing/batch-processing.md). After editing manually,
tell mzassist what you changed so it can use the current settings.

## Spectral-library search and library generation

**Library search** matches your measured spectra to an existing library. Tell mzassist which library
to use, review the matching settings, and inspect the spectral evidence for important hits.
Use the [spectral-library search guide](../module_docs/id_spectral_library_search/spectral_library_search.md).

**Library generation** creates a library from known reference standards. Prepare the raw data and
compound CSV, map the compound identifiers and mass information, and choose an export destination.
mzassist can check whether those inputs are consistent before preparing the batch. This readiness
check does not generate the library or verify the chemical identity of your standards.
Follow the [library-generation workflow](../workflows/librarygeneration/library_generation.md).

Save the reviewed wizard settings and the actual processing batch as described in
[Save and reproduce your work](mzassist-saving.md).

{{ git_page_authors }}
