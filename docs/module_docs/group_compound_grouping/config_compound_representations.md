# Configure compound representations

:material-menu-open: **Feature list methods → Feature grouping → Configure compound representations**

Controls how each **compound row** (produced by
[Compound grouping](compound_grouping.md)) exposes its per-raw-file intensity — area, height,
normalized area, and normalized height — to downstream modules, exports, and visualizations.

Three modes are available: fall back to the representative member's feature, or synthesize a
compound-level feature by summing across all members or only members that carry an Ion Identity.

The module is non-destructive: it does not alter member rows or grouping. Re-run any time to
switch modes; the change takes effect immediately for any subsequent intensity read.

!!! warning

    Run [Compound grouping](compound_grouping.md) first — this module needs a populated compound
    list to act on.


---

## Parameters

#### Feature lists
The feature list(s) whose compound rows should be reconfigured. Each list is processed
independently.

#### Intensity representation
Selects how every compound row computes its per-raw-file feature values. One of:

- **Representative row** _(default)_
  No compound-level features are stored. When something reads a compound row's feature for raw
  file _X_, the module returns the representative member row's feature for _X_ (or `null` if the
  representative has no feature in that file). This matches the behavior before the configuration
  module existed and uses the least memory.

- **Sum of all members**
  For each raw file, a synthesized compound feature is built whose area, height, normalized area,
  and normalized height are the sums across every member row's feature in that file. Members with
  no feature in a given file contribute zero.

- **Sum of members with ion identity**
  Same as **Sum of all members**, but only members where `hasIonIdentity()` is `true` contribute
  to the sum. Correlation-only members (those joined by MS1 shape but without a resolved adduct)
  are excluded.

!!! tip

    Stay on **Representative row** when you want classical per-feature quantification (e.g. the
    representative is the M+H and you do not want adduct co-summation to shift values).

---

## Output and side effects

- For **Sum of all members** and **Sum of members with ion identity**, a compound-level feature
  is materialized per raw file and stored on the compound row. These features back all subsequent
  intensity reads (table columns, exports, plots).
- For **Representative row**, no compound-level features are created; reads delegate to the
  representative member.
- An applied-method record is appended so the project replays consistently. Re-running the module
  overwrites the previous mode.

---

{{ git_page_authors }}
