# Save and reproduce your work

Save the mzmine project, the method actually used, and the results needed for your report.
A chat history is useful context, but it does not replace these files.

## What to save

| Artifact | Purpose | How to preserve it |
| --- | --- | --- |
| mzmine project (`.mzmine`) | Feature tables, sample metadata, applied methods, and project data | Use **Project → Save project / Save project as** in mzmine. |
| Wizard preset (`.mzmwizard`) | Reuse selected wizard settings | Ask mzassist to save the current wizard preset, or use the wizard's save controls. Recheck file selections and local paths when loading. |
| Processing batch (`.mzbatch`) | Reuse the ordered modules and their settings | Save the actual batch from mzmine's batch editor; also inspect the applied methods of the resulting feature table. |
| Scientific calculation table and record | Preserve results, supplied assumptions, and calculation details | In the native calculation result view, use **Save table (CSV)** and **Save calculation record (JSON)**. |
| Reviewed shortlist/report | Preserve selected features and the review or comparison used for export | Complete the export, then check the files in the chosen folder. |

See [Project handling](../module_docs/project_io/project_io.md) and
[Batch processing](../workflows/batch_processing/batch-processing.md).
A referencing project needs its raw files to remain accessible; a standalone project includes the
raw data. Choose the appropriate project type before sharing or moving the analysis.

A portable wizard preset can omit file paths. Loading a preset restores settings; it does not
import or process data automatically. A preset exported from a chat-only draft contains that reviewed
draft, not later edits made in mzmine. For a connected session, save the current native wizard after
you finish editing.

## Before ending the session

1. Confirm that the required jobs have finished and inspect the actual outputs.
2. Save the project and method. Keep an unchanged source table when later comparisons depend on it.
3. Export scientific calculation records and reviewed selections you need to retain.
4. Record the mzmine version, relevant mzassist version, libraries/reference data, sample mappings,
   units, exclusions, and the choices that affect interpretation.

Scientific analysis records and sharing approvals are held by the connection; saving a project does
not replace exporting those calculation records. After disconnecting, expect to select the table
and approve sharing again. Do not rely on an old chat's job identifier to reopen an analysis.

## Continue after interruption

Reopen the saved project if needed, connect mzassist, and ask it to inspect the current state.
Explain the last completed step and the intended next action. Check any partially created feature
tables before restarting processing: cancellation does not undo earlier outputs.

To reproduce a result, use the recorded data, method, and software version, then compare the new
output. A fresh assistant conversation can suggest different settings, so describe whether you
want to repeat the recorded method or develop a new one.

{{ git_page_authors }}
