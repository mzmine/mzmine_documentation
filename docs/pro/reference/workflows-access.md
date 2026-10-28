# Registered Pro workflows: implementation reference

Actual workflow availability and schemas are determined by the running application. For the task-oriented overview, see [workflows](../workflows.md).

## Inputs and prerequisites

### Workflow choices

The registered choices are **DDA (UV/Other)** (`DDA_UV`), **DIA (UV/Other)** (`DIA_UV`), and **MRM** (`mrm`). DDA and DIA accept the UV/other-detector workflow configuration; MRM restricts the MS step to its MRM configuration and disables ion mobility. The first two require the other-detectors service; MRM requires the MRM-workflow service.

### Connector workflow requests

`native-wizard-inputs`, `agent-workflow`, `reviewed-processing`, `parameter-estimation`, and `reviewed-optimization` act on the current native project and wizard. A workflow-session start supplies the current `project_id`, a canonical UUID `request_id`, a goal of at most 500 characters, and one mode: `process`, `design`, `review_before_processing`, or `focused`.

## Parameters and validation

The DDA factory starts with feature filtering and library search enabled; DIA starts with correlation at 0.8 and minimum signals at 5, together with filtering and library search. MRM enables its MRM-specific sequence with filtering. These are factory defaults, not a claim about an already edited wizard.

Processing review requires the exact current `wizard_revision`; a changed wizard returns `stale_context`. Estimation accepts `recommended` or `all`. Optimization validates `max_evaluations` against the native optimizer range. One active workflow is allowed, and repeated request IDs only identify the same request.

## Processing behavior

### Native batch versus agent proposal

The agent may construct a proposal, but native review remains the handoff before a batch starts. Starting a workflow captures the project identity and wizard revision. While manual editing is active, agent continuation is refused; a manual take-over exposes a read-only comparison of the original and current wizard and, where applicable, batch state.

### State progression

Stages can wait for user input, continue, be taken over, resumed, or finished. `finish` succeeds only once all required stages are complete. Cancelling or completing a native job releases the corresponding activity state, but does not silently reapply a previously stale proposal.

## Outputs and side effects

The batch builder produces the native processing queue for the selected workflow. Connector operations produce job or workflow identifiers and status, not a portable replacement for the native wizard. A successful proposal or applied processing change updates the captured revision; future mutations must use current context.

## Edge cases and errors

An unknown mode, noncanonical UUID, overlong goal, unknown session, or another active workflow is rejected. A project reload or wizard edit invalidates revision-bound requests. A native job in progress blocks manual editing of its workflow; closing the native batch editor is required before the agent can resume.

## Worked examples

### DDA UV proposal

Choose DDA (UV/Other), read the wizard, and start a `design` session using its returned `project_id`. If a user changes a wizard setting before processing review, submitting the old revision fails rather than launching a queue built from stale settings.

### MRM optimization

Select MRM, request estimation with `recommended`, then submit a reviewed optimization using a native-valid `max_evaluations`. Passing `all` is supported for estimation; passing any other selection is rejected before native work starts.
