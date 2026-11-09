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

The assistant explains the information it needs. You can approve the request in chat where that
option is offered, open the review in mzmine to inspect it, or keep the data private.
For metadata, the native preview lets you select columns and inspect the values before sharing;
a chat request can cover all current columns. Open the native review if you want a narrower selection.

Sample metadata describes your study. **Acquisition metadata** describes information recorded in
file headers and is not edited by sample-metadata changes. Neither table establishes the study
design by itself: verify sample roles, conditions, and replicates.

Result sharing is separate from metadata sharing. Check the selected feature table and optional
information before approving it. If the table, project, or relevant metadata changes, a new
sharing review may be required so the assistant works from the correct data.

## Pause, cancel, revoke, or disconnect

| Action | Effect | When to use it |
| --- | --- | --- |
| **Pause agent changes** | Blocks new agent changes and jobs. Previously shared results can still be read; submitted mzmine tasks keep running. | Inspect or edit the method yourself before continuing. |
| Cancel a job | Requests that the selected task stop. Outputs already created are not rolled back. | Stop unwanted or incorrectly configured processing. |
| Revoke sharing | Stops later access under that sharing decision. | Keep further metadata or result access private. |
| Disable the local connection | Disconnects mzassist and clears sharing approvals and pending reviews. Submitted native processing may continue; connector-owned result-analysis tasks are canceled. | End the assistant's access to mzmine. |

After manual editing, resume agent changes when ready and ask the assistant to inspect the current
method. Do not assume it can reuse a proposal made before your edits.

Revoking access or disconnecting cannot remove information already returned to a chat service.
Follow that provider's controls for conversation history and retention. A local mzmine installation
does not determine the provider's data-use policy.

{{ git_page_authors }}
