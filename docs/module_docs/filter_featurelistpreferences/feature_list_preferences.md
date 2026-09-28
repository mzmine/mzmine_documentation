# **Feature list preferences**

## **Description**

:material-menu-open: **Feature lists list → right-click a feature list → Set feature list
preferences**

or, from an open feature list:

:material-menu-open: **Feature list summary → Set feature list preferences**

Feature list preferences are settings that are stored on the feature list itself (and persisted
with the project) rather than being parameters of a single processing step. They influence how
other parts of mzmine interpret an already-processed feature list. Running this module only
updates the stored preferences of the selected feature list (s); it does not create a new feature
list or change any feature data.

Two preferences are currently available:

- **Samples for RSD columns** — which sample types are used to calculate the relative standard
  deviation (RSD) columns shown in the feature table (e.g. the area RSD).
- **Ion type ranking** — the frequency ranking used to judge how likely an ion type (adduct,
  in-source fragment, cluster, neutral loss/gain) is the correct explanation for a feature.

Every preference offers three options:

- **Keep as is** — the preference of the feature list is not changed.
- **Default** — the preference follows the current mzmine default. This lets a preference
  automatically pick up future mzmine default changes instead of freezing the value that was in
  effect when the project was created.
- **Custom** — the preference is pinned to the entered value, which is stored with the feature
  list.

If all preferences are on **Keep as is**, or the resulting preferences equal the ones already in
effect, running the module leaves the feature list untouched.

!!! tip

    Selecting multiple feature lists before opening the dialog applies the same preferences to all
    of them. The dialog always starts with every preference on **Keep as is**, so running it only
    changes the preferences you actively switch to **Default** or **Custom**. The **Custom** inputs
    are pre-filled with the preferences currently in effect for the first selected feature list.

!!! info

    In a batch, the step keeps the options you selected. When the dialog is opened while adding the
    step to a batch, it also starts on **Keep as is**.

---

## Parameters

#### Feature lists

The feature list (s) whose preferences shall be redefined.

#### Samples for RSD columns

Select the sample type (s) (from the metadata sample type column, ++ctrl+m++ / ++cmd+m++) that are
used to calculate the RSD columns of the feature table, e.g. the area RSD. Default: QC samples.

#### Ion type ranking

Defines how strongly each possible ion building block (an adduct such as `+H`, `+Na`; an
in-source fragment or neutral loss/gain such as `-H2O`; or a cluster such as `+Cl`) is expected to
occur, for both polarities. The ranking is used to:

- **score candidate ion identities** during ion identity networking, so that a more common
  explanation (e.g. `[M+H]+`) is preferred over a rarer one when several ion types would explain
  the same neutral mass, and to order the ion identities of a row from most to least likely,
- **pick the representative row of a compound** when the
  [Compound grouping](../group_compound_grouping/compound_grouping.md) module's **Representative
  row** parameter is set to **Ion type ranking**.

Click **Edit ranking** to open the ranking editor, which lists every configured ion building block
together with a frequency value. A higher frequency means the building block is assumed to occur
more often; unlisted building blocks always rank last. The score of a whole ion type (e.g.
`[M+H-H2O]+`) is the mean frequency of its building blocks, reduced by a fixed penalty for every
additional molecule in a cluster (so `[2M+H]+` scores lower than `[M+H]+` even with the same
building blocks).

Default ranking (highest frequency first, abbreviated): `+H` / `-H` (tied) > `+Na` > `+NH4` >
`+FA-H` (formate) > `+Cl` / `[M]+` / `[M]-` (tied) > `+CH3COO-H` (acetate) > `+K` > ... For the
full list of building blocks and their default frequencies, open the ranking editor.

---

{{ git_page_authors }}
