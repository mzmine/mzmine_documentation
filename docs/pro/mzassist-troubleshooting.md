# Troubleshooting {#troubleshoot-mzassist}

Start with **mzassist → Agent activity** to inspect the connection and recent activities.
If mzmine itself cannot open the data or run the method, resolve that problem in mzmine first.

## Connection and installation

| Symptom | What to check |
| --- | --- |
| No mzassist menu | Confirm the selected account in [Users management](../services/users.md). The connection requires an Academic, Pro, or Pro trial account and an mzmine installation that includes mzassist. |
| The assistant cannot find mzmine | Keep both applications on the same computer. Open **mzassist → Agent activity**, then click **Enable local connection**. Confirm that the mzassist plugin/connector is enabled in your chat app. If you previously disconnected, select **Enable local connection when mzmine starts** to restore the normal startup behavior. |
| Several mzmine instances appear | Choose the instance containing the project you intend to use. |
| The assistant still has old tools after an update | Update the included mzassist packages, restart the assistant, and start a new chat. |
| A documented task is unavailable | Check the installed mzmine version and account access. Ask the assistant which tasks that installation supports; a failed documentation search is not an availability check. |

### Missing setup files {#missing-setup-files}

Open **mzassist → Set up mzassist** and read its package status. The mzmine application and the
assistant packages have platform-specific builds; an mzmine installer for a platform does not by
itself establish that its mzassist packages are included. Use the appropriate current installer from
[GitHub Releases](https://github.com/mzmine/mzmine/releases/latest).
If the files are still unavailable, include the mzmine version, operating system/processor, assistant
version, and setup message when asking for support. Do not substitute packages for another platform.

## Reviews and data

| Symptom | What to do |
| --- | --- |
| A review is no longer current | The project, table, metadata, or method changed. Ask for a fresh review and inspect the new selection. |
| The assistant cannot read metadata or results | Ask mzassist to explain what access is missing and prepare a sharing request. Respond in chat, or ask it to open the pending review in mzmine. The manual review button appears only after a request exists and while inspection is available; see [Review a sharing request](mzassist-data-sharing.md#review-a-sharing-request). |
| A chromatogram or spectrum is unavailable in chat | Ask mzassist to review the signal-sharing choice or open the feature in mzmine so you can inspect it privately. |
| Normalized values are missing | Ask mzassist which values could not be normalized and why. Raw and normalized measurements answer different questions; check which the analysis uses. |
| A result contains fewer features than expected | Ask mzassist to explain the selection and exclusions and provide the complete result for your stated question. |
| A statistical calculation needs more information | Ask mzassist which missing experiment details affect the calculation. Confirm them from your records; a descriptive summary may still be useful while the design is unresolved. |

## Processing and exports

| Symptom | What to do |
| --- | --- |
| The job is still running | Ask mzassist for progress, or open **mzassist → Agent activity** and select the processing entry. |
| Nothing new starts after manual inspection | Tell mzassist you are ready to continue, or click **Resume agent changes** under **mzassist → Agent activity** if changes are paused. |
| Processing continued after disconnecting | Submitted mzmine tasks can continue locally. Open **mzassist → Agent activity**, click **Enable local connection**, then ask mzassist to cancel the specific job. |
| A canceled job left tables behind | Ask mzassist what completed and how to continue. Cancellation does not remove outputs from completed steps. |
| No file appears after choosing an export option | Confirm that export actually ran and finished. Check the destination and reported output files. |
| A reviewed export fails after editing the table | Ask mzassist to use the updated table and show a new sharing/export review. |

{{ git_page_authors }}
