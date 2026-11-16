# Data sharing and agent controls

:material-menu-open: **mzassist → Agent activity**

mzmine performs processing and calculations locally. The information returned to your assistant
can be sent to its model provider. Decide what to share based on the analytical task and your
laboratory's policy.

## What information is shared?

| Information | What happens |
| --- | --- |
| Raw data files and project archive | mzassist does not upload the complete files or project through the normal processing workflow. Selected signals or results can be shared separately. |
| File and folder paths | Choose them in mzmine to keep the selection local. Text pasted into chat is visible to the assistant/provider. |
| Connection and project summaries | mzassist returns operational information such as available tasks, file counts, and counts of sample roles so the assistant can plan the next step. |
| Feature-table names and counts | The connected assistant can discover these to select a table. Avoid confidential information in table names. |
| Sample metadata | Sharing requires approval. Review the columns and values, including free text that may identify samples or contain paths. |
| Acquisition metadata | Optional, read-only file-header summaries. The native review starts with this option unchecked. A chat approval can include the summary when mzassist asks for it. Header text may contain sensitive information. |
| Measured results and annotations | Approve a selected feature table before the assistant reads its measurements, annotations, compound memberships, processing methods, sample roles, and selected grouping values. Group labels can identify a study even when sample names are not shared. |
| Sample names, metadata column titles, chromatograms, spectra, plot images, and run order | Additional choices in result sharing. They are selected initially in the mzmine review; clear any that are unnecessary before approval. |
| Anything you type, paste, or attach in chat | Already shared with that assistant under its own data-handling rules, independently of mzmine's sharing controls. |

## Review a sharing request

Start by describing your task in chat, for example: “Help me inspect the final feature table from
the last processing run.” mzassist checks which tables are available and asks you to clarify if
more than one could fit. When it needs metadata or measurements that you have not already approved
for sharing, it prepares a request explaining the table or files and the information to be shared.

Respond to that request in chat: approve it, decline it, or reply “Open the sharing review in mzmine
so I can inspect it first.” mzassist opens that review for you. You do not need to select a feature
table or find a sharing control in mzmine before asking for help.

**Optional manual route:** a sharing entry appears in **mzassist → Agent activity** only after
mzassist has prepared the request. While the request is still current, select its row in the
activity history. The details and available action for that row appear under **Selected activity**:

- For a **Metadata sharing** row, click **Inspect metadata in mzmine** or **Review metadata sharing**,
  according to the action shown. Select the columns you want to share and inspect their values.
  **Share selected metadata** confirms that selection.
- For a **Share results** row, click **Inspect in mzmine** or **Open review**. Check the feature
  table and additional sharing choices, then use **Share results** to approve them.

The action follows the selected row and its current state. If it is no longer available, ask
mzassist in chat to prepare a new request for the task. After approval, a metadata entry offers
**Revoke metadata sharing**; a result entry is renamed **Shared results** and offers **Revoke sharing**.
The revocation effects are explained under [Pause, cancel, revoke, or disconnect](#pause-cancel-revoke-or-disconnect).

A metadata approval in chat can cover all current columns and, when requested, acquisition-header
summaries. It is available for a preview of up to 32 columns and less than 200 kB. Larger requests
need to be narrowed or reviewed in mzmine. Use that review when you want to select fewer columns or inspect
their contents privately before deciding.

Sample metadata describes your study. **Acquisition metadata** describes information recorded in
file headers and is not edited by sample-metadata changes. Neither table establishes the study
design by itself: verify sample roles, conditions, and replicates.

Result sharing is separate from metadata sharing. Check the selected feature table and optional
information before approving it. If the table, project, or relevant metadata changes, a new
sharing review may be required so the assistant works from the correct data.

## Add or correct sample metadata

You can ask mzassist to add sample information or correct values in mzmine's Sample metadata table.
For example, supply a missing sample role or explain which injections belong to the same sample.
The assistant can edit shared columns and propose new columns for the selected files.

Sharing permission allows mzassist to read the approved information; it does not itself request a
metadata change. mzassist shows proposed before-and-after values and asks before applying them,
unless you have delegated metadata completion. You can instead inspect the proposal in chat or in
mzmine. Check inferred labels and replicate assignments against your sample records; a filename does
not establish biological meaning. These changes affect Sample metadata, not the acquisition
information recorded in the raw file.

## Pause, cancel, revoke, or disconnect

You can request a pause, cancellation or sharing revocation in chat. The manual controls below are in
**mzassist → Agent activity** in mzmine.

| What you want | In chat | Manual control and effect |
| --- | --- | --- |
| Take over editing | “Pause agent changes while I inspect the method.” | Click **Pause agent changes**. New changes and jobs, including metadata edits and new result-sharing requests or approvals, are blocked. Submitted mzmine tasks continue and previously shared results remain readable. You can still inspect status, request metadata sharing, keep a request private, or revoke sharing. Click **Resume agent changes** when ready. |
| Stop processing | “Cancel the current processing job.” | Ask mzassist to cancel the specific job. Pausing or disconnecting is not a substitute for cancellation; completed outputs remain. |
| End metadata sharing | “Revoke metadata sharing.” | Select a **Metadata sharing** history row, then click **Revoke metadata sharing** under **Selected activity**. This ends **all metadata sharing for the connection**, including other metadata reviews, and marks still-pending metadata requests as kept local. |
| End result sharing | “Stop sharing this feature table.” | Select its **Shared results** history row, then click **Revoke sharing** under **Selected activity**. |
| Disable local access | Use the manual control in mzmine. | Click **Disconnect**. This clears sharing approvals and pending reviews, and cancels jobs still waiting for file selection or approval. Submitted mzmine processing may continue; result-analysis tasks managed by the connection are canceled. |

**Disconnect** is temporary. The connection is enabled automatically on startup by default, and
can also be enabled again after a login or license refresh. To keep it off, clear **Enable local
connection when mzmine starts** in **mzassist → Agent activity**, then click **Disconnect**.

After manual editing, resume agent changes when ready and ask the assistant to inspect the current
method. Do not assume it can reuse a proposal made before your edits.

Revoking access or disconnecting cannot remove information already returned to a chat service.
Follow that provider's controls for conversation history and retention. A local mzmine installation
does not determine the provider's data-use policy.

Continue with [Process your first dataset](mzassist-first-analysis.md), or ask mzassist to help
[explore an existing result](mzassist-results.md).

{{ git_page_authors }}
