# Workflow and job state: implementation reference

This page documents the reviewed 4.10.111 development-series connector state contract. See [agent-assisted mzmine](../agent-assisted-mzmine.md) for operational guidance.

## Inputs and prerequisites

`session-status`, `job-status`, `job-cancellation`, and `job-results` refer to work started in the current connection. Job-producing actions require current project context; processing review also needs a matching wizard revision. The bridge keeps up to 64 jobs and 32 retained result records.

## Parameters and validation

Workflow start validates `project_id`, UUID `request_id`, goal, and mode. Continuing requires the live `workflow_id`. Job cancellation targets an existing job; result actions distinguish non-mutating `keep_results` from state-changing actions. A repeated request may return its original job only when its semantic inputs match.

## Processing behavior

Statuses reflect native task lifecycle rather than estimated completion: queued, running, finished, error, or canceled. Native job submission is refused while incompatible processing or project loading is active. The workflow record tracks stage state and whether agent changes are paused for manual editing; it is cleared when the native context becomes invalid.

## Outputs and side effects

Status responses include the job/workflow identity, native progress where available, and completed output references. Cancellation asks the native task to stop; it does not roll back previously created outputs. A user can keep result outputs, while other result actions count as workflow mutations and refresh context.

## Edge cases and errors

More than 64 jobs, an old project ID, an old wizard revision, or a request ID reused with different inputs fail rather than selecting an arbitrary job. A missing workflow returns `workflow_unavailable`; an active workflow blocks a second one. Completion data may remain unavailable after reconnect because the in-memory request registry is connection-scoped.

## Worked examples

### Cancel a running review

Start reviewed processing and poll its job. A cancellation request changes task state if native cancellation succeeds, but any outputs created before cancellation remain native project content.

### Resume after manual inspection

Take over a waiting workflow to inspect the wizard. If no change is made, resume can continue; if the wizard changed, submit a request based on the returned current revision rather than the earlier snapshot.
