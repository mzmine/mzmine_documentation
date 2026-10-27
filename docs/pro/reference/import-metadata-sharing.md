# Import and metadata sharing: implementation reference

This reference covers the reviewed 4.10.111 development-series snapshot. See [agent-assisted mzmine](../agent-assisted-mzmine.md) for the user guide.

## Inputs and prerequisites

`native-import` scans a selected directory for supported raw files; native mode keeps the file selection local. An agent-driven import instead requires explicitly shared source paths. `native-login` and connector access depend on an eligible signed-in user. `reviewed-metadata-sharing` and `reviewed-metadata-editing` operate on the current `project_id`. A sharing request starts the review that can create a grant; row-level metadata editing requires that grant to be current.

The **Acquisition metadata** view is a read-only table of imported file-header information. Ordinary metadata edits through the connector apply to sample metadata, not these acquisition fields.

## Parameters and validation

Directory scanning has a `recursive` choice. Symbolic links and nonregular files are ignored; CSV and TSV candidates may be offered as native sample metadata. Metadata-sharing requests require a canonical UUID request ID, current project ID, and `approval_mode` of `native` or `chat`. At most 10,000 file rows may be reviewed, and at most 32 outstanding reviews are retained.

`include_acquisition` is an optional boolean, default **false**. Setting it requests review of an acquisition-header summary; it does not grant access. The native dialog shows **Share acquisition metadata (file-header text)** only for such a request, and starts with that checkbox unchecked. `include_rows` separately requests row-level sample-metadata access.

## Processing behavior

### Consent precedes data access

Nothing is shared before approval. The native preview starts with no sample columns or acquisition checkbox selected and lets the user choose the scope. A chat review prepares all current sample-metadata columns and, only when requested, acquisition metadata. It produces an approval token for the trusted mediator; ordinary status reads do not disclose that token or the prepared values. Chat choices allow the scope once, allow it for the session, or keep it private. Opening the native review replaces the pending chat approval and lets the user narrow the selection. Editing row-level metadata requires a current grant. Changes are proposed and reviewed rather than silently committed.

### Acquisition-header summary

Approved acquisition sharing returns `acquisition_summary` with provenance `file_header_text`. It groups instrument-model, mass-analyzer, ion-source, and detector values across the project files. These are stored file-metadata strings, not validated instrument facts or standardized vocabulary terms. The summary contains up to **128 distinct values per field**, sorted by text, with each displayed value limited to **256 characters**. It reports per-value file counts, missing-file counts, omitted-value counts, and text-truncation flags. Duplicate values within one file count once. Unknown metadata does not establish absence.

Project context exposes only acquisition-sharing status and, for a current approved grant, its review ID. The values themselves are returned through the approved metadata review. Header text can contain sensitive information; inspect the preview rather than treating the field names as a guarantee about the contents.

### Invalidating a review

The review is tied to the project, ordered file selection, and observed metadata version. If metadata changes while approval is pending, the decision is rejected as stale and a new review is required. When acquisition sharing was requested, the review also checks the complete included acquisition fields, including values outside the bounded preview. Changes to those fields invalidate acquisition-inclusive approval even when session reuse was allowed; a new review is required. A revoke prevents later reads or edits under that grant. Ending the local connection also clears pending metadata reviews and their grants.

## Outputs and side effects

Scanning reports counts for raw files, nested files, outside-directory discoveries, source folders, and metadata candidates. A completed native selection can import files and optional metadata into the project. An approved sharing decision makes only the selected current metadata scope available; a reviewed edit can apply, revert, reject, or keep the current project values local.

Sharing acquisition headers creates a bounded summary for the agent/provider; it does not edit the acquisition metadata or grant access to raw spectra. The approved scope reports whether acquisition metadata was actually included.

## Edge cases and errors

Unreadable folders, cancellation, or no supported files produce non-ready scan results. Agent import without shared paths fails. Reusing a request ID for different sharing inputs conflicts; more than 10,000 files returns `too_many_files`. Attempts to read/edit without a grant return `metadata_not_shared`.

Changing `include_acquisition` while reusing the same request ID causes `request_conflict`. A sample-metadata-only approval cannot be reused to add acquisition headers. Empty header fields contribute to `unknown_file_count`; large sets are explicitly marked as omitted or truncated rather than silently presented as complete.

## Worked examples

### Private import

Scan a directory non-recursively and choose native import. The resulting selection may include a discovered TSV metadata file, but paths are not made available to the agent merely because they were scanned.

### Edited metadata after approval

Request chat approval for selected sample columns, then alter project metadata in mzmine before deciding. The old approval is stale, so the connector must request a fresh preview rather than applying the decision to changed rows.

### Share headers only when needed

Request a native metadata review with `include_acquisition` enabled. Leave **Share acquisition metadata (file-header text)** unchecked to keep those values local, or select it, inspect the preview, and approve to share the bounded summary. Later changes to an included instrument-model value require fresh approval even if session reuse was selected.
