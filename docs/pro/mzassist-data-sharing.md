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
| Acquisition metadata | Optional, read-only file-header summaries. The native review starts with this option unchecked. Header text may contain sensitive information. |
| Measured results and annotations | Approve a selected feature table before the assistant reads its measurements, annotations, compound memberships, processing methods, sample roles, and selected grouping values. Group labels can identify a study even when sample names are not shared. |
| Sample names, metadata column titles, chromatograms, spectra, plot images, and run order | Additional choices in result sharing. Allow them when needed for the question. |
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
mzassist has prepared the request. While it is pending, select its row in the activity history.
The details and available action for that row appear under **Selected activity**:

- For a **Metadata sharing** row, click **Inspect metadata in mzmine** or **Review metadata sharing**,
  according to the action shown. Select the columns you want to share and inspect their values.
  **Share selected metadata** confirms that selection.
- For a **Share results** row, click **Inspect in mzmine** or **Open review**. Check the feature
  table and additional sharing choices, then use **Share results** to approve them.

The selected row does not have to be the newest activity. The button follows the row you select
and the request's state. After approval, the sharing entry offers a **Revoke** action instead of
the pending review action. If a request is no longer available, ask mzassist in chat to prepare a
new sharing request for the task. These are controls for individual requests, not permanent sharing
preferences.

A metadata approval in chat can cover all current columns. Use the mzmine preview when you want
to select fewer columns or inspect their contents privately before deciding.

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

Sharing permission alone does not authorize edits. If you delegate metadata completion, the assistant
can apply the proposed changes after inspecting the before-and-after values. You can instead ask to
review a proposal in chat or privately in mzmine before it is applied. Check inferred labels and
replicate assignments against your sample records; a filename does not establish biological meaning.
These changes affect Sample metadata, not the acquisition information recorded in the raw file.

## Pause, cancel, revoke, or disconnect

You can request a pause, cancellation or sharing revocation in chat. The manual controls below are in
**mzassist → Agent activity** in mzmine.

| What you want | In chat | Manual control and effect |
| --- | --- | --- |
| Take over editing | “Pause agent changes while I inspect the method.” | Click **Pause agent changes**. New changes and jobs stop; already submitted mzmine tasks continue and previously shared results remain readable. Click **Resume agent changes** when ready. |
| Stop processing | “Cancel the current processing job.” | Ask mzassist to cancel the specific job. Pausing or disconnecting is not a substitute for cancellation; completed outputs remain. |
| End metadata sharing | “Revoke metadata sharing.” | Select the active **Metadata sharing** history row, then **Revoke metadata sharing** under **Selected activity**. |
| End result sharing | “Stop sharing this feature table.” | Select its **Shared results** history row, then **Revoke sharing** under **Selected activity**. |
| Disable local access | Use the mzmine control to turn off the bridge. | Click **Disconnect** to disable the local connection and clear sharing approvals and pending reviews. Submitted mzmine processing may continue; connection-owned result-analysis tasks are canceled. |

After manual editing, resume agent changes when ready and ask the assistant to inspect the current
method. Do not assume it can reuse a proposal made before your edits.

Revoking access or disconnecting cannot remove information already returned to a chat service.
Follow that provider's controls for conversation history and retention. A local mzmine installation
does not determine the provider's data-use policy.

Continue with [Process your first dataset](mzassist-first-analysis.md), or ask mzassist to help
[explore an existing result](mzassist-results.md).

{{ git_page_authors }}
