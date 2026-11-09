# Troubleshoot mzassist

Start with **mzassist → Agent activity** to inspect the connection and recent activities.
If mzmine itself cannot open the data or run the method, resolve that problem in mzmine first.

## Connection and installation

| Symptom | What to check |
| --- | --- |
| No mzassist menu | Confirm the selected account in [Users management](../services/users.md). The connection requires an Academic, Pro, or Pro trial account and an mzmine installation that includes mzassist. |
| The assistant cannot find mzmine | Keep both applications on the same computer. Enable the local connection in Agent activity and confirm that the mzassist plugin/connector is enabled in the assistant. |
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
| The assistant cannot read metadata or results | Check whether the appropriate sharing request was approved. Metadata and result sharing are separate decisions. |
| A chromatogram or spectrum is unavailable in chat | Check the optional signal-sharing choice, then open the row in mzmine to inspect the native data. |
| Normalized values are missing | Check that the normalized column exists and inspect the normalizer diagnostics. Do not substitute raw values without changing and reporting the analysis choice. |
| A result contains fewer rows than expected | Ask whether more result pages are available and check the selected table/row filters. |
| A statistical calculation needs more information | Supply the actual conditions, independent samples, pairing/time, or required units. Keep the output descriptive until those inputs are resolved. |

## Processing and exports

| Symptom | What to do |
| --- | --- |
| The job is still running | Check native progress before submitting another request. |
| Nothing new starts after manual inspection | Check **Pause agent changes** and resume when ready. |
| Processing continued after disconnecting | Submitted mzmine tasks can continue locally. Cancel the task in mzmine if it must stop. |
| A canceled job left tables behind | Inspect the partial outputs and decide what to keep before rerunning. Cancellation does not roll back completed steps. |
| No file appears after choosing an export option | Confirm that export actually ran and finished. Check the destination and reported output files. |
| A reviewed export fails after editing the table | Prepare a fresh result-sharing/review selection for the changed table. |

{{ git_page_authors }}
