# Import and metadata sharing: implementation reference

This reference covers the reviewed 4.10.107 development-series snapshot. See [agent-assisted mzmine](../agent-assisted-mzmine.md) for the user guide.

## Inputs and prerequisites

`native-import` scans a selected directory for supported raw files; native mode keeps the file selection local. An agent-driven import instead requires explicitly shared source paths. `native-login` and connector access depend on an eligible signed-in user. `reviewed-metadata-sharing` and `reviewed-metadata-editing` operate on the current `project_id`. A sharing request starts the review that can create a grant; row-level metadata editing requires that grant to be current.

## Parameters and validation

Directory scanning has a `recursive` choice. Symbolic links and nonregular files are ignored; CSV and TSV candidates may be offered as native sample metadata. Metadata-sharing requests require a canonical UUID request ID, current project ID, and `approval_mode` of `native` or `chat`. At most 10,000 file rows may be reviewed, and at most 32 outstanding reviews are retained.

## Processing behavior

### Consent precedes data access

Nothing is selected or shared by default. The native preview lets the user choose columns; a chat review produces a short-lived approval token for the trusted mediator, while ordinary status reads do not disclose it. Editing row-level metadata requires a current grant. Changes are proposed and reviewed rather than silently committed.

### Invalidating a review

The review is tied to the observed metadata version. If metadata changes while approval is pending, the decision is rejected as stale and a new review is required. A revoke prevents later reads or edits under that grant. Ending the local connection also clears pending metadata reviews and their grants.

## Outputs and side effects

Scanning reports counts for raw files, nested files, outside-directory discoveries, source folders, and metadata candidates. A completed native selection can import files and optional metadata into the project. An approved sharing decision makes only the selected current metadata scope available; a reviewed edit can apply, revert, reject, or keep the current project values local.

## Edge cases and errors

Unreadable folders, cancellation, or no supported files produce non-ready scan results. Agent import without shared paths fails. Reusing a request ID for different sharing inputs conflicts; more than 10,000 files returns `too_many_files`. Attempts to read/edit without a grant return `metadata_not_shared`.

## Worked examples

### Private import

Scan a directory non-recursively and choose native import. The resulting selection may include a discovered TSV metadata file, but paths are not made available to the agent merely because they were scanned.

### Edited metadata after approval

Request chat approval for selected sample columns, then alter project metadata in mzmine before deciding. The old approval is stale, so the connector must request a fresh preview rather than applying the decision to changed rows.
