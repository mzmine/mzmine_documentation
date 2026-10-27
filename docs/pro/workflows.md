# mzmine Pro workflows

This page describes the user-facing workflows added by mzmine Pro. The standard mzmine modules and
their documentation remain relevant; Pro workflows add support for MRM data and traces acquired
with other detectors, such as UV/DAD data measured with LC-MS.

!!! info

    Availability depends on the services enabled for the signed-in mzmine user. The running
    application's menus and parameter dialogs are authoritative for the installed version.

## DDA (UV/Other) {#dda-uv-other}

Choose **DDA (UV/Other)** in the batch wizard for LC-MS/MS data-dependent acquisition that also
contains other-detector traces. It follows the ordinary LC DDA workflow and adds an other-detector
branch: optional chromatogram extraction for additional wavelengths, trace shifting and binning,
baseline correction, local-minimum resolving, and correlation of the resulting other-detector
features with the MS feature list.

Use this workflow only for LC-based acquisition. Direct infusion and flow injection are not
available selections for this workflow. Select the detector trace type and, when applicable, the
wavelengths to process. The wizard can estimate a retention-time shift automatically; inspect the
result in the correlation dashboard before relying on cross-detector assignments.

## DIA (UV/Other) {#dia-uv-other}

Choose **DIA (UV/Other)** for LC data-independent acquisition with other-detector traces. It uses
the usual DIA workflow choices and adds the same other-detector preparation and correlation stages
as DDA (UV/Other). It is also restricted to LC acquisition; direct infusion and flow injection are
not available selections.

For either UV/Other workflow, use only traces that answer the analytical question. Processing every
available trace can add noise and unnecessary computation. See the [Other detector terminology]
(../module_docs/uv/otherdetector_glossary.md), [trace-processing steps]
(../module_docs/uv/uv_shift_trim_bin_traces/uv_shift_trim_bin_traces.md), and
[correlation workflow](../module_docs/uv/uv_ms_other_aligner/uv_ms_other_aligner.md).
Use the [Multi detector visualizer](../module_docs/uv/uv_multi_detector_visualizer/uv_multi_detector_visualizer.md)
when manual trace integration or side-by-side trace inspection is needed.

## MRM {#mrm}

Choose **MRM** for LC triple-quadrupole multiple-reaction-monitoring data. The wizard is limited to
low-resolution MS and no ion mobility. It converts the transition chromatograms into mzmine's MRM
feature representation, creates chromatograms, can assign quantifier transitions from a table, and
then resolves and aligns the features.

The workflow is designed around the MRM transition information, so prefer the
[MRM aligner](../module_docs/align_mrm/mrm-aligner.md) after resolving. The MRM guide gives the full
sequence, input expectations, and manual alternatives: [MRM workflow]
(../workflows/mrmworkflow/mrm-workflow.md).

---

{{ git_page_authors }}
