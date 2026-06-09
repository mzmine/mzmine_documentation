# Compound grouping (beta)

:material-menu-open: **Feature list methods → Feature grouping → Compound grouping (beta)**

Groups feature list rows that represent the same chemical compound — adducts, isotopologues,
in-source fragments, and correlation members — into **compound rows**. A compound row links its
member rows under a single representative row and is the unit consumed by the Compound dashboard
and by downstream per-compound exports.

The module consumes the output of upstream feature grouping and requires at least one of:

- **Ion Identity Networks** (from the [Ion Identity Networking](../id_ion_networking/iin/iin.md)
  module)
- **MS1 correlation map** (from
  the [Correlation grouping](../id_ion_networking/metacorr/metacorr.md)
  module).

!!! warning

    Run [Correlation grouping](../id_ion_networking/metacorr/metacorr.md) and/or
    [Ion Identity Networking](../id_ion_networking/iin/iin.md) first — without one of those, the
    module aborts with a validation message.

!!! danger "Beta"

    The module is marked beta in the menu. It is safe to use but might be subject to change to improve and strengthen the algorithm in the future.

## Recommended citations

!!! info

    When using mzmine for your work, please consider citing:<br>
    Schmid R., Heuckeroth S., Korf A., et al. Integrative analysis of multimodal mass spectrometry
    data in MZmine 3, Nature Biotechnology (2023), doi:10.1038/s41587-023-01690-2.

    When using this module on data that relies on Ion Identity Networking, please also cite:<br>
    Schmid, R., Petras, D., Nothias, LF. et al. Ion identity molecular networking for mass
    spectrometry-based metabolomics in the GNPS environment. Nat Commun 12, 3832 (2021).
    https://doi.org/10.1038/s41467-021-23953-9

---

## Parameters

#### Feature lists

The feature list(s) to group. Each list is processed independently and gets its own compound list
attached.

#### Strategy

Selects the algorithm that decides which feature rows belong to the same compound. Each strategy
exposes its own sub-parameters via the combo box. Two strategies are available:

- **Simple correlation & IIN** _(default)_

[//]: # (- **Weighted multi-evidence graph** _&#40;in development — see warning above&#41;_)

See the [Strategies](#strategies) section below for details.

#### Representative row

Selects how the representative row of each compound is picked from its members. The representative
is the row exposed by `Feature list → row.getBestFeatureListRow()` semantics: it is what other
modules read when they need a single per-compound feature row (intensity export, annotation
display, etc.). Two options are available:

- **Prefer annotated highest row (default)** — tiered preference:
    1. Highest-intensity row that is identified (compound DB / spectral library / lipid / manual /
       formula annotation).
    2. Otherwise, highest-intensity row carrying any Ion Identity.
    3. Otherwise, highest-intensity row overall.

- **Ion type ranking** — primary score is the row's ion type position in the tier list:
  `M+H → M-H → M+ → M- → Na+ → Cl- → K+ → NH4+ → Formate-H`. Ties broken by intensity.
  Rows must carry a *clean* single-adduct ion (one molecule, no neutral losses, no clusters) to
  qualify; otherwise the ultimate fallback is the highest-intensity row.

Neither selector exposes user-tunable parameters.

---

## Strategies {#strategies}

### Simple correlation & IIN _(default)_

Seeds compounds from clean Ion Identity Networks, attaches loose correlated rows to the best seed,
then peels dense communities out of the residual correlation graph. Conservative — keeps compound
sizes small unless evidence is strong.

#### _m/z_ tolerance

Intra-sample _m/z_ tolerance used when matching isotopologue spacings during role assignment.
Default: **5 ppm or 1 mDa** (whichever is broader).

#### Retention time tolerance

Maximum allowed RT difference between a member and the representative when checking isotopologue
and coherence relations. Default: **0.03 min**.

#### Minimum density

Minimum edge density `[0..1]` required to accept a residual correlation cluster (rows without an
Ion Identity Network) as a compound. `1.0` requires a clique; lower values accept looser
communities. Default: **0.4**.

!!! tip

    Lower the density threshold if your data has weak but consistent co-elution patterns (e.g.
    high-resolution LC-IMS-MS); raise it if you see too many unrelated rows being clumped
    together.

[//]: # ()
[//]: # (### Weighted multi-evidence graph _&#40;experimental&#41;_)

[//]: # ()
[//]: # (Builds a weighted multi-evidence graph &#40;RT, MS1 shape correlation, IIN, isotope spacing,)

[//]: # (annotation agreement&#41;, detects dense cores, and assigns the remaining rows via weighted neighbor)

[//]: # (voting plus bounded message-passing smoothing. Designed to handle ambiguous cases where multiple)

[//]: # (evidence sources partially agree.)

[//]: # ()
[//]: # (!!! danger)

[//]: # ()
[//]: # (    This strategy is not yet enabled by default and is under active development. Output may)

[//]: # (    change between releases.)

[//]: # ()
[//]: # (Exposes ~16 parameters covering edge weights &#40;`RT`, `shape`, `IIN`, `isotope`, `annotation`&#41;,)

[//]: # (core-detection thresholds, assignment confidence cutoffs, message-passing smoothing controls, and)

[//]: # (an annotation-conflict splitter. See the in-app dialog for the full list; defaults are tuned for)

[//]: # (typical LC-MS data.)

---

## Outputs and side effects {#outputs}

When the task completes, the selected feature lists each carry a populated **compound list**:

- One **compound row** per group, with a designated **representative member**.
- Other members are tagged with a **role** based on their relation to the representative:
    - **ADDUCT** — same Ion Identity Network, different adduct ion type (confidence 0.90).
    - **ISOTOPOLOGUE** — _m/z_ delta matches a known isotope spacing (default tolerance 0.005 Da,
      up to 4× multiples) and RT within tolerance (confidence 0.85).
    - **IN_SOURCE_FRAGMENT** — ion type carries a neutral loss or cluster part (confidence 0.70).
    - **CORRELATED** — joined only via the correlation edge, no IIN evidence (confidence 0.50).
    - **REPRESENTATIVE** — the selected representative row (confidence 1.0).
- Each compound row carries a confidence score combining size, IIN fraction, and RT coherence.

An applied-method record is appended to the feature list so the operation is reproducible from
the project XML.

!!! warning

    If the feature list is structurally mutated (rows added/removed) while the task is running,
    the result is discarded — re-run the module after any such change.

---

## Manual editing

After the automated grouping, three context-menu actions on the Compound dashboard let you adjust
compound rows manually. Each is recorded as an applied method so the project can be replayed.

#### Set representative row

Promotes a member row of a compound to be the new representative; the previous representative is
demoted to **CORRELATED**.

**Parameters:** target compound ID, new representative row ID.

#### Merge compound rows

Merges one or more compound rows (and/or extra individual feature rows) into a target compound.
The target's representative is preserved; representatives from merged compounds are demoted to
**CORRELATED**. Fully consumed source compounds are removed from the compound list.

**Parameters:** target compound ID, other compound IDs (comma-separated, may be empty), extra
feature row IDs to pull in (comma-separated, may be empty).

#### Split compound row

Moves selected member rows out of a compound into a new compound row. The new compound inherits
the source's confidence and neutral mass. The source compound is dropped if it ends up empty.

**Parameters:** source compound ID, member row IDs to move (comma-separated).

---

## Configuring compound-row intensity {#config-intensity}

A separate module —
[**Configure compound representations**](config_compound_representations.md) —
controls how each compound row exposes its per-raw-file intensity (area, height, normalized
variants). Run it after Compound grouping to switch between using the representative member's
feature, summing across all members, or summing only members that carry an Ion Identity.

---

## Algorithm {#algorithm}

### Simple correlation & IIN

1. **Build correlation adjacency lists** from the MS1 correlation map.
2. **Seed from clean IINs only** — networks where every member's best Ion Identity points to that
   same network. Members of these networks form initial compound groups via Union-Find.
3. **Attach loose rows to a single best seed** — for each non-IIN row, count edges to each seeded
   group; assign to the group with the highest edge count, tie-broken by summed correlation
   score. Multi-membership only on a genuine tie.
4. **Peel dense residual communities** — in the subgraph of rows that are neither seeded nor
   attached, greedily pick the highest-degree node, take its closed neighborhood, peel
   low-degree members until edge density meets the **Minimum density** threshold, commit the
   remaining set as a compound. Leftover isolated rows become singleton compounds.
5. **Assign roles** via `RoleAssigner` (see [Outputs](#outputs)) and compute a per-compound
   confidence as `0.3 × size + 0.5 × IIN-fraction + 0.2 × RT-coherence`.

[//]: # (### Weighted multi-evidence graph)

[//]: # ()
[//]: # (1. **Build cores** — each clean IIN becomes a core; dense communities in the residual correlation)

[//]: # (   subgraph become additional cores; heavily inter-connected residual cores are merged on Jaccard)

[//]: # (   overlap.)

[//]: # (2. **Assign loose rows** by weighted neighbor voting over the multi-evidence graph, followed by)

[//]: # (   `MP_ITERATIONS` rounds of message-passing smoothing &#40;`MP_DAMPING` controls how much weight is)

[//]: # (   given to neighbors&#41;. Rows with a preferred annotation or a defined best Ion Identity are)

[//]: # (   forced into a single core; a runner-up core receives dual membership only on a near-tie.)

[//]: # (3. **Assemble compounds**, optionally splitting on MS2 annotation conflict, and record)

[//]: # (   annotation/RT contradictions on the resulting members and compound rows.)

---

{{ git_page_authors }}
