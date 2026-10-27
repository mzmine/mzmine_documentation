# Native analysis tools: implementation reference

This reference covers the reviewed 4.10.107 development-series connector behavior. For analysis choices, see [scientific analysis](../scientific-analysis.md).

## Inputs and prerequisites

`normalization` operates on a selected current feature table and native task controller. `library-search` uses a reviewed native configuration; `library-generation-preflight` and its settings provide data-free checks/settings review. `scientific-analysis` dispatches only from an approved result scope; individual analysis calculations are documented separately.

## Parameters and validation

Normalization accepts `run`, `status`, or `cancel`; only `run` accepts settings. Its schema exposes abundance, a suffix (maximum 256 characters), original-list handling, optional batch column, and inter-sample methods `no_normalization`, `feature_intensity_normalization`, `spectral_tic`, and `feature_qc`. Feature-intensity metric IDs are `median`, `sum_tic`, `average`, and `max`; its `sum_tic` is feature-table TIC, not spectral TIC. QC-RLSC requires at least five usable QC observations per feature/batch; fixed span must yield at least degree + 2 points.

## Processing behavior

Normalization builds and submits the ordinary native intensity-normalizer queue. A request ID is idempotent only for identical inputs. Its finished response lists native output-table references; an error reports the native task message when present. Library settings are proposal/review based: inspect is read-only, while changes are workflow mutations. Preflight checks readiness before library-generation batch preparation rather than generating a library.

## Outputs and side effects

Normalization produces native normalized feature-list outputs according to its native handling choice and marks changed outputs in the bridge. Library search/generation actions return review, job, or readiness state; they do not imply a validated identification. Scientific-analysis dispatch retains the approved scope and its sharing limits, so it does not automatically broaden metadata or signal access.

## Edge cases and errors

No selected table gives `table_unavailable`; incompatible active processing/project loading gives `processing_active`; unavailable native normalization gives `task_unavailable`. Invalid parameters return `invalid_parameters`, and reaching 64 retained normalization requests prevents another run; reconnect releases completed records, while active requests remain. The service blocks normalization while library search is active. Unsupported methods/metrics and unavailable or stale required context are request errors. Insufficient usable QC data is handled per feature and batch: affected normalized values are marked unavailable with diagnostics, while the overall normalization job can still finish and produce a table.

## Worked examples

### Feature-QC normalization

Select a table with pooled QC samples, request `feature_qc` with valid QC settings, and poll the returned request ID. A feature/batch with fewer than five usable QC observations cannot meet the native minimum. Normalization can still finish, but affected normalized values are unavailable with a reason rather than substituted with raw abundance.

### Library-generation preparation

Inspect library-generation settings, request preflight, then submit reviewed settings. Preflight can identify missing required preparation, but it neither writes a library nor bypasses the native review step.
