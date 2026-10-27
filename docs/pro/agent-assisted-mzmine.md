# Agent-assisted mzmine

The mzmine MCP local connector lets a compatible chat agent request actions from a running mzmine
application. mzmine keeps the project, raw files, and the native user interface on the local
computer. The connector returns only the bounded information needed for the approved operation and
scope. Depending on that request, this can include selected measurements, sample metadata,
annotations, chromatographic or spectral signals, images, or injection order; it is not a general
copy of the local project.

This guide describes the connector included with the mzmine 4.10.107 development build. Availability
depends on the installed mzmine version, its enabled local connection, and the capabilities reported
by that running application. Use the application's current capabilities and parameter schemas as the
authority for what can be run.

!!! warning

    An agent's explanation or suggested setting is not scientific validation. Review the native method,
    assumptions, data selection, and outputs before starting a processing job or interpreting a result.

## Connect and choose what to share

Open **Agent activity** in mzmine to check the local connection or restore it if it has been disabled.
An agent first discovers available mzmine instances; connecting one does not start processing or share
a project automatically.

For a private folder, use mzmine's native directory chooser. mzmine scans and imports supported files
locally, and the agent receives a bounded summary such as counts by recognized file type rather than
folder paths or filenames. mzmine opens its own import dialog so you can correct the selection and
choose a matching sample-metadata file. A metadata file is never silently selected when several
plausible files are present.

Sample metadata and acquisition metadata have different roles:

- **Sample metadata** describes samples and can be reviewed and edited through the connector after
  you approve the requested fields.
- **Acquisition metadata** is a separate editable matrix saved with the project. It is not a fallback
  for sample metadata and is not changed by ordinary sample-metadata edits.

Keep project information local when the agent does not need it. A sharing review names the requested
fields and can be declined or revoked. Raw-file paths, raw spectra, and unreviewed metadata are not
required for the normal import and workflow route.

## Build, review, and run a workflow

The connector can inspect the selected project's available inputs, propose a workflow, estimate
settings, and optionally optimize a reviewed method. It uses the mzmine wizard vocabulary and the
connected application's current parameter schema; it does not make a static documentation snapshot
an input contract.

1. Confirm the analytical aim and import data through the native dialog.
2. Let the agent read approved project context and propose a method and batch.
3. Review the complete change set in chat or open the native mzmine editor for advanced editing.
4. Apply a reviewed method, estimate parameters when appropriate, and inspect the returned batch
   preview.
5. Start a processing job only after an explicit approval of that preview. You can instead adjust the
   settings, inspect the method in mzmine, cancel a queued/running job, or resume from the next
   unfinished stage.

Each reviewed change is tied to the project and method revision that produced it. A changed project,
method, batch, or disconnected connection can require the scope to be reviewed again. Applying a
proposal does not run a batch. When its starting wizard settings are still current, estimation applies
its result to that wizard as it completes and returns a reviewable before/after record. Optimization
returns separate candidate settings for review. Neither operation starts a batch.

The connector can save or load named workflow presets, including the selected workflow settings, and
can navigate to the requested wizard, feature table, dashboard, or feature row. Navigation only
changes the mzmine view. You can pause or resume new agent changes (already submitted mzmine tasks
continue), take over workflow editing in mzmine, or stop a job. After a stop, restart from the
suitable unfinished stage rather than assuming a
partially completed batch is scientifically interchangeable with a fresh run. Disconnecting ends the
local connection, not the project on disk.

## Feature tables, evidence, and results

After processing, an agent can list, rename, or delete feature tables in the project, request an
explicitly approved result context, and help organize a comparison. Treat deletion as irreversible in
the current project: preserve an export or project copy first if the table may be needed later. It can
create or revise sample groups, calculate a supported comparison, page the resulting rows, inspect a
known row's native evidence, and open the associated feature or dashboard in mzmine. Chromatograms,
feature signals, and result rows are returned in bounded pages; request the next page or open the row
in mzmine rather than assuming the first page is exhaustive.

Feature tables are processing outputs. An aligned table and a correlation table are not, by their
names or matching row counts alone, separate experimental conditions. State the scientific question
and assign the intended groups explicitly. QC, blank, and sample roles do not identify biological
conditions by themselves.

The agent can prepare a shortlist and export only after the relevant result context and destination
have been reviewed. An export setting is configuration, not evidence that a file was created. A
shortlist or an association score is a prioritization aid: inspect chromatography, spectra, annotation
evidence, replicate behavior, blanks, and study design before drawing an identification or causal
conclusion.

### Normalization

The connector exposes the parameters of the native **Intensity normalizer**. It can normalize area or
height, choose a suffix and how to retain the original feature list, and configure metadata scaling,
internal-standard correction, QC/inter-sample correction, and an optional batch metadata column.
The native normalizer writes separate normalized area and height columns. See
[Intensity normalizer](../module_docs/norm_intensity/norm_intensity.md) for the correction sequence,
preconditions, and interpretation.

Batch diagnostics can flag a pattern consistent with drift; it does not correct measurements. Apply
batch or QC correction only through a reviewed normalizer configuration, then retain the original
values and examine the correction assumptions.

### Spectral-library search and library generation

The connector can list local libraries, read the native parameter catalog, configure a reviewed
library search, and run it in mzmine. It does not turn a library hit into a confirmed identity.

For the library-generation workflow, a preflight checks that the selected raw files, configured CSV
database, required compound and mass mappings, optional filename filter, and export destination are
consistent. It reads only bounded local CSV content and reports aggregate counts; it does not expose
the file path, filenames, or CSV cells. A successful preflight means the supplied setup is ready for
the next native workflow step. It does not generate a library or validate the scientific identity of
the compounds. Review the CSV column mapping for the compound identifiers and mass information before
preflight; a preset can restore mappings and settings, but does not validate the source data. See the
[library generation workflow](../workflows/librarygeneration/library_generation.md).

## Limits and troubleshooting

- The connector does not bypass mzmine's native dialogs, operating-system permissions, or user
  reviews.
- Install the local connector from the mzmine release that matches the running application, then use
  **Agent activity** to confirm its connection. After updating mzmine, update the matching connector
  and reconnect before relying on an earlier capability list or workflow review.
- If a capability is not advertised by the connected build, the connector cannot use it. That does
  not establish that the feature is absent from every mzmine edition or installation; a documentation
  search likewise does not establish availability on the installed build.
- A failed search or an empty result does not prove that a feature or file is absent.
- Agent-hosted online services are separate from the local connector. They may have their own
  accounts, sharing choices, and availability requirements.
- If a job is still running, wait for its native status rather than submitting the same request again.

{{ git_page_authors }}
