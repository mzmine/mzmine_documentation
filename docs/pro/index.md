# mzmine Pro reference

Use this reference for the additional workflows and features included in the mzio distribution of
mzmine. It covers interactive use, batch processing, and assistance through the local MCP connector.
The [general mzmine documentation](../index.md) also applies to the Community modules included in
this distribution.

!!! info "Version and availability"

    Use the website's version selector to read documentation for your mzmine release. Availability
    depends on the installed application's menus, account services, and available connector
    capabilities. When using a bundled knowledge pack, use the documentation snapshot supplied with
    your build. A missing search result does not establish that a feature is unavailable.

## Workspaces and access {#workspaces-and-access}

The **PRO (complete)** workspace brings the standard processing menus together with the additional
**Other detectors** and **MRM** menus. Individual tools and workflow choices depend on the services
available to the active user. Seeing the workspace name alone does not confirm access to every tool.
Sign in and select the intended account in [Users management](../services/users.md) when a tool is
missing or an operation reports that a service is required.

The MRM workflow and the other-detector workflow have separate service requirements. The local MCP
connection requires an active Academic, Pro, or Pro trial account in the mzio build. Availability of a
GUI module does not by itself mean that a chat agent can configure or execute that module.

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

The general mzmine helper can explain any documented mzmine feature, including a GUI-only feature.
Execution through the connector depends on what the running application actually exposes.

The [agent guide](agent-assisted-mzmine.md) covers connection setup, private import, metadata,
workflow configuration, estimation and optimization, review and execution, jobs, presets,
navigation, feature-table management, result sharing, library searches, and exports.
The [scientific-analysis reference](scientific-analysis.md) explains supported calculations and their
assumptions. Normalization uses the native
[Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md).

Online services reached through mzconnect have their own account and data-sharing requirements.
Public documentation or inclusion of a tool in a menu does not establish entitlement to an online
service or transfer experimental data to it.

## Documentation and citations {#documentation-and-citations}

The helper searches the documentation snapshot bundled with its knowledge pack. Answers should
identify the page and relevant section, with a link to that revision of the public documentation.
The same material is available to the helper offline. An offline citation can still identify the
document even when its web link cannot be opened.

For questions about your installed build, the helper should distinguish documented behavior from
the capabilities reported by that application. A recommendation or interpretation should explain
its assumptions. Documentation does not replace checking experimental suitability or reviewing the
actual processing outputs.

---

{{ git_page_authors }}
