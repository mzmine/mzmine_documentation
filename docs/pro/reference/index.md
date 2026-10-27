# Implementation reference for mzmine Pro

These pages explain the processing rules behind Pro features: defaults, validation, calculations,
fallbacks, output changes, and failure cases. Use them alongside the [Pro user guides](../index.md)
when a general description does not explain a result or parameter choice. They also cover the
Community multi detector visualizer used in the Pro workflow.

!!! info "Reviewed snapshot"

    This reference describes the 4.10.107 development snapshot reviewed for this knowledge pack.
    Builds with the same version number can differ. The pack's source revisions identify the reviewed
    snapshot; check the connected application's capabilities and parameter schema for current inputs.
    Documented defaults do not establish the settings used in a particular analysis.

The reference is derived from implementation review, with worked examples of behavior that matters
to users. It does not reproduce the implementation or claim to document every internal branch.
Where a question needs detail beyond these pages, the helper should identify that gap rather than
infer a rule from a similar Community module.

## MRM and resolving

- [MRM conversion](mrm-to-scans.md)
- [MRM quantifiers](mrm-quantifiers.md)
- [MRM alignment](mrm-aligner.md)
- [MRM export](mrm-export.md)
- [Wavelet resolver](wavelet-resolver.md)

## Other detectors

- [Chromatogram extraction](detector-chromatograms.md)
- [Shift, trim, and bin](detector-shift.md)
- [Baseline correction](detector-baseline.md)
- [Trace resolving](detector-resolver.md)
- [Correlation](detector-correlations.md)
- [Clear correlations](detector-clear-correlations.md)
- [Correlation dashboard](detector-dashboard.md)
- [Multi detector visualizer](detector-visualizer.md)

## Scientific analysis

- [Quantification](quantification.md)
- [Batch diagnostics](batch-diagnostics.md)
- [Study comparison](study-comparison.md)
- [Activity association](activity-association.md)
- [Exposure assessment](exposure-assessment.md)

## Workflows and connection

- [Workflow availability](workflows-access.md)
- [Import and metadata sharing](import-metadata-sharing.md)
- [Workflow state and review](workflow-state.md)
- [Results and exports](results-exports.md)
- [Native analysis tools](native-analysis-tools.md)
- [Application setup and access](application-setup.md)

## Citations

The helper cites the public documentation revision and lines supporting its answer. An implementation
reference citation points to the reviewed explanation; it is not a link to private source code.
Private source-review evidence is maintained separately and is not included in the customer pack.

---

{{ git_page_authors }}
