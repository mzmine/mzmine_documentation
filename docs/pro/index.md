# mzmine Pro reference

mzmine Pro provides additional workflows for MRM data and detectors such as UV/DAD.
This page helps you find those tools and their processing guides. For help from an AI assistant,
start with [mzassist](agent-assisted-mzmine.md).

!!! info "Choose your mzmine version"

    Use the website's version selector to read the guide for your installed release.
    Download installers and portable packages from [GitHub Releases](https://github.com/mzmine/mzmine/releases/latest).

## Workspaces and access {#workspaces-and-access}

The **PRO (complete)** workspace groups the standard processing menus with **Other detectors** and
**MRM**. To use those additional workflows, the corresponding features must be enabled for your
account. If a workflow is missing, check the selected account in [Users management](../services/users.md).
Changing the workspace does not change your account's access.

To use **mzassist**, sign in with an Academic, Pro, or Pro trial account, then open
**mzassist → Set up mzassist**. Follow the [setup guide](mzassist-setup.md) to connect your assistant.

## Choose a workflow {#choose-a-workflow}

| Your data or task | Start here |
| --- | --- |
| LC-MS with additional UV/DAD or other-detector traces | [DDA (UV/Other) and DIA (UV/Other)](workflows.md#dda-uv-other) |
| LC triple-quadrupole MRM/SRM transition data | [MRM workflow](../workflows/mrmworkflow/mrm-workflow.md) |
| Compare an experimental resolver with an established method | [Wavelet feature resolver](../module_docs/featdet_resolver_wavelet/wavelet_resolver.md) |
| Ask an agent to help configure, run, or inspect an analysis | [Agent-assisted mzmine](agent-assisted-mzmine.md) |
| Quantification, QC diagnostics, study comparisons, activity associations, or exposure calculations | [Scientific analysis](scientific-analysis.md) |

For ordinary LC-MS, ion-mobility, GC-MS, imaging, annotation, or spectral-library tasks, begin with
the relevant [processing wizard](../wizard.md) and module documentation. The pages below supplement
those workflows rather than changing the meaning of their parameters or outputs.

## Other-detector processing {#other-detector-processing}

These tools work with detector traces associated with the raw data. Review the
[detector terminology](../module_docs/uv/otherdetector_glossary.md) before choosing raw traces,
extracted chromatograms, or resolved features.

| Tool | Purpose and documentation |
| --- | --- |
| Chromatogram builder (Other spectral data) | [Extract chromatograms from spectral detector data, including selected wavelength ranges](../module_docs/uv/uv_spectra_chromatogram_builder/spectrachrombuilder.md). |
| Shift, trim, and bin traces (Other detectors) | [Correct time offsets and control the trace range and sampling](../module_docs/uv/uv_shift_trim_bin_traces/uv_shift_trim_bin_traces.md). This tool can also be available with the MRM service. |
| Baseline correction (Other detectors) | [Estimate and subtract a detector baseline](../module_docs/uv/uv_baseline_correction/uv_baseline_correction.md). The module is labelled beta. |
| Local minimum resolver (Other detectors) | [Split detector traces into individual features](../module_docs/uv/uv_resolve_traces/uv_local_min_resolver.md). |
| Correlate MS features with other detectors | [Assign detector features to MS features using retention time and peak-shape correlation](../module_docs/uv/uv_ms_other_aligner/uv_ms_other_aligner.md). |
| Clear correlated traces (Other detectors) | [Remove stored assignments before rebuilding them](../module_docs/uv/uv_clear_correlated_traces/uv_clear_correlated_traces.md). |
| Correlation dashboard (Other detectors) | [Inspect and manually adjust assignments](../module_docs/uv/uv_correlation_dashboard/uv_correlation_dashboard.md). |
| Multi detector visualizer | [Inspect detector traces and integrate them manually](../module_docs/uv/uv_multi_detector_visualizer/uv_multi_detector_visualizer.md). |

## MRM processing {#mrm-processing}

| Tool | Purpose and documentation |
| --- | --- |
| MRM to scans and chromatograms | [Convert transition chromatograms into the representation used for MRM processing](../module_docs/mrm_mrmtoscans/mrm-to-scans.md). |
| Set MRM quantifiers | [Choose quantifier transitions using a transition table](../module_docs/mrm_setquant/mrm-set-quant-mass.md). |
| MRM aligner | [Align MRM feature lists with mass, retention-time, and transition constraints](../module_docs/align_mrm/mrm-aligner.md). |
| Export MRMs to TSV | [Export MRM-specific quantitative results](../module_docs/io_mrmtotsv/mrm-to-tsv.md). |

Use the [MRM workflow guide](../workflows/mrmworkflow/mrm-workflow.md) for the processing order and
the [Pro workflow overview](workflows.md#mrm) for the wizard's acquisition restrictions.

## Agent assistance and analysis {#agent-assistance-and-analysis}

Use [mzassist](agent-assisted-mzmine.md) to ask about settings, build a processing method, or inspect
results. The guide explains the tasks you can request and which steps to review in mzmine.
[Scientific analyses](scientific-analysis.md) cover quantification, QC diagnostics, study comparisons,
activity associations, and exposure calculations. For normalization, see the native
[Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md).

If your workflow also uses mzconnect or another online service, follow that service's account and
data-sharing instructions before submitting data.

## Documentation and citations {#documentation-and-citations}

mzassist includes a local copy of the mzmine documentation. You can ask the assistant to cite the
page supporting an explanation. Check the cited version when its instructions differ from your
installation. Having documentation available locally does not make your AI assistant an offline
service; its connection and data-handling requirements still apply.

When reporting an analysis, record the mzmine version and the method actually used. Follow the
citation recommendations for the processing modules in your method.

---

{{ git_page_authors }}
