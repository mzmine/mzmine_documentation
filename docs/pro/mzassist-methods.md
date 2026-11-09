# Build and improve a processing method

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

Applying a proposed method changes settings; running the processing batch is a separate action.
Check the final processing summary, especially the selected files and export destinations.
If you asked mzassist to stop before processing, authorize the run only when the summary is correct.

While the job runs, follow its status in chat or **Agent activity**. Avoid submitting the same job
again just because a reply is delayed. If the method changes, request a new summary before running.
For an interrupted batch, inspect the outputs already produced before choosing what to rerun.

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
