# Project handling

:material-menu-open: **Project → Open project / Save project / Save project as**

mzmine stores a complete processing session - raw data files, feature lists, spectral libraries,
sample metadata, and the applied methods of every step - in a single `.mzmine` project file. This
page describes the four modules that manage the project life cycle:

- [Open project](#open-project)
- [Save project](#save-project)
- [Save project as](#save-project-as)
- [Clear project](#clear-project)

!!! tip

    All four modules are also available as batch steps. `Clear project` in particular is useful to
    free memory between independent sub-workflows in a long batch.

---

## Project formats {#project-formats}

Projects can be saved in two formats. The format is chosen with the **Project type** parameter of
[Save project as](#save-project-as) and is reused automatically when an already saved project is
saved again.

#### Referencing (small)

The project stores only *paths* to the raw data files, both as absolute paths and - since
mzmine 4.3 - as paths relative to the project file. The project file itself stays small.

The project can be shared if the raw files are available either under exactly the same absolute
path or under the same path relative to the project file. Saving the project into the same folder
as the raw data files therefore produces a portable project.

!!! warning

    Renaming, moving, or deleting a raw data file breaks a referencing project.

#### Standalone (large/flexible)

The raw data files are copied into the project file. The resulting project is considerably larger
but self-contained and can be shared without any additional requirements.

!!! warning

    If you re-save an existing project, use the same format it was saved with.

---

## Open project {#open-project}

:material-menu-open: **Project → Open project...**

Loads an existing `.mzmine` project. By default the currently loaded project is discarded and
replaced.

The **Project** menu additionally offers a quick *Open project* entry that only shows a file chooser
and skips the parameter dialog, as well as a list of recently used projects.

### Parameters

#### Project file

The `.mzmine` file to load.

#### Merge onto existing

If enabled, the contents of the loaded project are added to the currently open project instead of
replacing it. This allows combining raw data files and feature lists from several projects.

!!! warning

    After merging a standalone project onto the current one, the result can only be saved as a
    standalone project, not as a referencing project.

#### Keep current spectral libraries

If enabled, spectral libraries that are currently loaded are kept in addition to the libraries of
the opened project. If disabled, they are removed.

!!! tip

    The quick *Open project* menu entry always keeps the current spectral libraries, because most
    users work with the same library across projects.

---

## Save project {#save-project}

:material-menu-open: **Project → Save project**

Saves the current project. If the project has already been saved to a writable file before, the
module reuses that file and the previously used [project format](#project-formats) without showing
a dialog. Otherwise it behaves exactly like [Save project as](#save-project-as).

---

## Save project as {#save-project-as}

:material-menu-open: **Project → Save project as**

Saves the current project to a new file and lets you choose the project format.

### Parameters

#### Project file

Target file of the project. The `.mzmine` extension is appended automatically if it is missing. If
the file already exists, a confirmation dialog asks whether it should be overwritten.

#### Project type

Selects `Referencing (small)` or `Standalone (large/flexible)`, see
[project formats](#project-formats). Default is `Referencing (small)`.

---

## Clear project {#clear-project}

Removes all raw data files and feature lists from the current project, leaving an empty project
space. This module has no parameters.

!!! danger

    Clearing the project cannot be undone. Unsaved raw data and feature lists are lost.

Typical use is inside a batch that processes several independent datasets in sequence: clear the
project after exporting the results of one dataset before importing the next one, to keep memory
usage low.

---

{{ git_page_authors }}
