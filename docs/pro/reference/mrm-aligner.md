# MRM alignment: implementation reference

This reference covers the reviewed 4.10.107 development-series snapshot. See the [MRM aligner guide](../../module_docs/align_mrm/mrm-aligner.md).

## Inputs and prerequisites

Select feature lists that contain MRM transitions. Alignment clones features into a new list. With transition checking enabled, every feature in a candidate aligned row must carry MRM transition data.

## Parameters and validation

**m/z tolerance (sample-to-sample)** defaults to 0.01 m/z and 0 ppm. **Retention time tolerance** defines the candidate RT interval. **Only allow matches to same MRM** defaults to enabled. **Feature list name** defaults to `Aligned feature list`. The original-list handling control defaults to retaining originals.

## Processing behavior

Candidates must be inside both the m/z and RT tolerance ranges. The alignment scorer is RT-only after those candidate filters: all accepted candidate pairs receive the same scoring weights. With **Only allow matches to same MRM**, Q1 must be exactly equal, transition counts equal, and sorted Q3 arrays exactly equal; quantifier identity is not part of that gate.

After common alignment, mzmine takes the MRM-bearing feature with greatest height in each aligned row as the quantifier reference. Other features are switched to their transition with the same isolation pair. It then applies the requested original-list handling.

## Outputs and side effects

The output is a newly aligned feature list populated with cloned features and calculated alignment scores. Depending on original-list handling, source lists are retained or acted on after successful construction. Features in each aligned row are assigned the same quantifier transition, using the tallest feature as the reference. This does not apply intensity normalization. Reported feature height and area can change because they are recalculated from the selected quantifier transition.

## Edge cases and errors

With same-MRM filtering active, a candidate already in the aligned/base rows causes an error if one of its features lacks transitions; an incoming row whose best feature lacks transitions simply does not match. Disabling the filter permits different transition sets to align, but post-alignment quantifier assimilation fails if the tallest feature's quantifier isolation is absent from another feature. Cancellation or a null alignment result stops before assimilation/project update.

## Worked examples

### Strict compatible transitions

Two rows both at Q1 500.000, with RTs within the selected RT tolerance and identical sorted Q3 values 120 and 150, pass the strict transition check. If the tallest feature uses 150 as quantifier, each compatible feature is switched to its 150 transition. A row at Q1 500.006 is rejected by **Only allow matches to same MRM**, even though the difference is within the default 0.01 m/z candidate tolerance: strict matching requires exactly equal Q1 values.

### Loose matching can fail later

With **Only allow matches to same MRM** disabled, a 500/120,150 row can align to a 500/120 row when m/z and RT pass. If the taller feature's quantifier is 150, the second feature has no matching isolation and the task fails during quantifier assimilation rather than exporting a mixed quantifier row.
