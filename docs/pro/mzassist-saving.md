# Save and reproduce your work

Save the mzmine project, the method actually used, and the results needed for your report.
A chat history is useful context, but it does not replace these files.

## What to save

| Artifact | Purpose | How to preserve it |
| --- | --- | --- |
| mzmine project (`.mzmine`) | Feature tables, sample metadata, applied methods, and project data | Use **Project → Save project / Save project as** in mzmine. |
| Wizard preset (`.mzmwizard`) | Reuse selected wizard settings | Ask mzassist to save the current wizard preset. For manual access, ask mzassist to open the applied method, then use **Presets → Save presets...** in that wizard tab. **mzwizard → Processing wizard** may open a new tab with different settings. Recheck file selections and local paths when loading. |
| Processing batch (`.mzbatch`) | Reuse the ordered modules and their settings | Recover the batch from the completed feature table's applied methods using the path below, then save it as a `.mzbatch` file. |
| Scientific calculation table and record | Preserve results, supplied assumptions, and calculation details | Ask mzassist to open the completed calculation in mzmine. In that result view, use **Save table (CSV)** and **Save calculation record (JSON)**. |
| Reviewed shortlist/report | Preserve selected features and the review or comparison used for export | Ask mzassist to export the reviewed selection, then open the files it reports as completed. |

Recovering a table's method replaces the current batch queue. If you need to keep the existing queue,
open **Project → Batch mode** and click **Save** first. Then open the **Feature lists** tab in mzmine,
right-click the completed table, choose **Show feature list summary**, and click **Open in batch queue**.
Review any warning about recorded methods that cannot be used as batch steps, then confirm
**Overwriting batch?**. Check the restored steps and click **Save** to write the `.mzbatch` file.
Close the editor with **Cancel** to avoid starting another run. **Project → Batch mode** now shows
the restored queue. See
[Project handling](../module_docs/project_io/project_io.md) and
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
4. Ask mzassist for a methods summary including the software versions, libraries/reference data,
   sample mappings, units, exclusions, and choices that affect interpretation. Check it against
   the saved method and calculation records.

Scientific analysis records and sharing approvals are held by the connection; saving a project does
not replace exporting those calculation records. After reconnecting, describe which analysis you
want to continue. mzassist identifies the table and asks for sharing approval again before reading
its results. Previously exported tables and calculation records remain your record
of those completed analyses.

## Continue after interruption

Reopen the saved project if needed, connect mzassist, and ask it to inspect the current state.
Explain the last completed step and the intended next action. Check any partially created feature
tables before restarting processing: cancellation does not undo earlier outputs.

To reproduce a result, use the recorded data, method, and software version, then compare the new
output. A fresh assistant conversation can suggest different settings, so describe whether you
want to repeat the recorded method or develop a new one.

{{ git_page_authors }}
