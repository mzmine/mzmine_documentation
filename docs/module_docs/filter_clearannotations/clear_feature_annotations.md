# Clear feature list annotations

:material-menu-open: **Feature list methods → Clear feature list annotations**

Removes selected annotation types from all rows of a feature list. The features themselves, their
intensities, and all other data types are untouched - only the chosen annotation columns are
cleared.

Typical uses are:

- re-running an annotation step with different parameters on a clean feature list,
- removing intermediate or low-quality annotations before export,

!!! danger

    Clearing annotations cannot be undone. The annotations have to be recreated by re-running the
    corresponding annotation module.

---

## Parameters

#### Feature lists

The feature lists to process.

#### Clear annotations

A checkbox is shown for each main annotation type, for example spectral library matches, compound
database matches, lipid annotations, formula lists, and manual annotations. Only the selected types
are removed, and only if the feature list actually contains them. By default nothing is selected.

---

{{ git_page_authors }}
