# Application setup and access: implementation reference

This page describes the reviewed 4.10.111 development-series application surfaces. See [Pro access and workspaces](../index.md) and [agent-assisted mzmine](../agent-assisted-mzmine.md).

## Inputs and prerequisites

The complete workspace surface is named **PRO (complete)** and has ID `pro_full`. The local bridge menu appears only for an allowed account. Eligible user types are Academic, Pro, and Trial Pro; Core, Plus, Unvalidated, and no current user are not eligible. The connection may be enabled manually or configured to connect automatically; automatic connection defaults to enabled.

## Parameters and validation

The setup/activity menu has separate connection and activity views. `native-login` requests the native account flow, not credentials through connector fields. Feature-table and dashboard navigation require the current project and a live known table. Reading results or metadata requires its own approved sharing scope; opening a native view does not grant that scope.

## Processing behavior

The local-connection license gate is shared by the menu and connection. When access is missing, protected bridge use fails with `license_required`; it does not expose an alternate unauthenticated endpoint. The menu opens setup or activity tabs and reuses existing tabs. Workspace visibility and connector eligibility are separate checks.

## Outputs and side effects

Enabling the bridge starts local connection state and discovery. Disabling it disconnects local services, clears pending approvals and revokes active result-sharing scopes; submitted native jobs continue in mzmine. Toggling automatic connection persists that preference. Opening activity/setup/dashboard surfaces changes native UI visibility but does not create a workflow, approve sharing, import files, or mutate a feature table.

## Edge cases and errors

The menu can be absent for an ineligible account. A license refresh may change whether subsequent connection attempts are admitted. Workspace visibility does not establish permission for every Pro tool: bridge operations check license and current context, with sharing approval required for the relevant data reads.

## Worked examples

### Trial Pro account

A Trial Pro user can open the local bridge menu and request native login. They still must approve metadata or results before the connector may read that scope.

### Workspace versus connector gate

Open PRO (complete) and request local connection with an account that does not meet the connection license requirement. The request is rejected as `license_required`; workspace visibility has not granted connector access.
