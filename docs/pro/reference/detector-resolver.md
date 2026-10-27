# Other-detector local-minimum resolver: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.107 development series. It resolves preprocessed other-detector chromatograms into features; see the [user guide](../../module_docs/uv/uv_resolve_traces/uv_local_min_resolver.md).

## Inputs and prerequisites

Choose raw data files and other-detector traces. The default selection is preprocessed UV traces. A usable trace must contain RT/intensity points; the resolver operates in retention-time dimension.

## Parameters and validation

Defaults are: **Chromatographic threshold** 0.85 (bounded 0–1), **Search RT range** 0.05, **Minimum relative height** 0.0, **Minimum absolute height** 10, **Minimum ratio** 1.7, **Peak duration range** 0.0–10.0 min, and **Minimum number of data points** 10. These values are transferred into the local-minimum resolver, with resolving dimension fixed to retention time.

## Processing behavior

Each input trace is passed to the local-minimum resolver as its RT and intensity arrays. Each accepted RT interval becomes a subseries-derived feature. Results are grouped by their raw trace and replace processed features for that trace; this is replacement, not cumulative peak picking.

## Outputs and side effects

The resolved subfeatures retain their parent/raw-trace relationship and are stored as processed features for the associated raw trace. No separate feature list is created.

## Edge cases and errors

If the module is started with an incompatible parameter set, it records an error and stops. A trace with no accepted ranges contributes no replacement group, so existing processed features for that raw trace are not explicitly cleared by this task path. Parameter semantics beyond the listed values follow the shared local-minimum resolver.

## Worked examples

### Default thresholding

A trace peak below absolute height 10 cannot pass the default absolute-height gate even if its local shape otherwise satisfies the threshold settings.

### Two accepted intervals

If one selected trace resolves to two RT ranges, it produces two subfeatures and replaces that raw trace's previous processed features with those two results.
