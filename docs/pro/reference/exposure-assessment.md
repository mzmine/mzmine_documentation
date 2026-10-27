# Exposure assessment: implementation reference

This reference documents the `exposure` operation in the reviewed knowledge-pack snapshot of the mzmine 4.10.111 development series. See the [scientific-analysis overview](../scientific-analysis.md).

!!! info "MCP-only workflow entry point"

    In the reviewed build, this workflow is initiated through the MCP local connector. Calculation
    runs locally in mzmine, and results can be opened in mzmine's native result view.

## Inputs and prerequisites

Exposure requires a completed native `quantification` result from the same scope; supplied measurements are not accepted. Required fields are non-empty unique `sample_ids`, `scenario`, and `reference`. Selected IDs must exist in that quantification result and can select only samples whose quantification role is `unassigned`, never calibrators or QC samples.

## Parameters and validation

`scenario.interpretation` is required and retained verbatim. It may provide positive `devices_per_day`, `sample_mass_g_per_day`, `solution_volume_ml_per_day`, `body_mass_kg`, `accept_estimated_values`, and textual assumptions. Reference requires positive `value`, supported `unit`, nonblank `source_url`/`version`, and `applicability_acknowledged: true`. Reference units are `ng/day`, `ug/day`, `ng/kg/day`, and `ug/kg/day`; per-kg/day requires positive body mass.

## Processing behavior

The operation accepts compatible quantified values only: per-device (`ng/device`, `ug/device`) uses devices/day; original-sample-mass (`ng/g`, `ug/g`, `mg/kg`) uses sample mass/day; solution values (`ng/mL`, `ug/mL`, `mg/L`, `ug/L`, `ng/L`) use solution volume/day. It converts to ng/day, divides by body mass only for a per-body-mass reference, converts to the selected reference unit, and reports `reference_ratio = exposure / reference`.

Thus the denominator/rate is not inferred from a unit label: a per-device value needs `devices_per_day`, a mass-normalised value needs `sample_mass_g_per_day`, and a solution concentration needs `solution_volume_ml_per_day`. The reference conversion recognizes `ng/day` and `ug/day`, or `ng/kg/day` and `ug/kg/day`; only the latter pair needs `body_mass_kg`.

An explicitly surrogate-reference-equivalent value is rejected unless `accept_estimated_values` is true; other flags reject it. Missing or incompatible unit/basis/scenario rates return null with a reason rather than a calculation.

## Outputs and side effects

The result retains selected reference provenance, scenario assumptions, formula statement and descriptive warning. Each quantified row includes selected samples with `value`/`exposure`, reference unit, ratio, `above_selected_reference` or `at_or_below_selected_reference`, and flags. It does not change quantification or make a toxicological, safety, or regulatory verdict.

## Edge cases and errors

No quantification rows is an error. Unsupported/missing quantification unit yields `unsupported_or_missing_quantification_unit`; missing rate or incompatible basis yields `missing_or_incompatible_scenario_basis`; disallowed estimates yield `estimated_quantification_requires_accept_estimated_values`. Nonpositive quantities are unavailable.

## Worked examples

### Per-device result

A 2 ng/device quantification with `devices_per_day: 3` yields 6 ng/day before reference conversion. Against a 3 ng/day reference it reports ratio 2 and `above_selected_reference`; it remains a descriptive comparison.

### Per-body-mass reference

A compatible amount of 70 ng/day and `body_mass_kg: 70` is 1 ng/kg/day for comparison to an `ng/kg/day` reference. Omit body mass and the specification is invalid rather than comparing an unnormalised amount.

{{ git_page_authors }}
