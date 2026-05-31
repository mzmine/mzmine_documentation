# **Spectral library editor**

## **Description**

:material-menu-open: **Tools → Libraries → Spectral library editor**

The _Spectral library editor_ is a dedicated tool for viewing, editing, and managing spectral
library files. It can run as a **standalone desktop application** or as an **embedded tab** inside
MZmine Pro when opening imported spectral libraries from the project.

The editor loads spectral library files, displays each entry with its mass spectrum and metadata,
and lets users modify metadata fields, remove entries, and save the result back to disk. Changes are
tracked at the field level so that edited entries are clearly marked throughout the session.

## Supported file formats {#supported-formats}

| Format      | Extension | Read | Write |
|-------------|-----------|------|-------|
| MGF         | `.mgf`    | Yes  | Yes   |
| MSP (NIST)  | `.msp`    | Yes  | Yes   |
| MSP (RIKEN) | `.msp`    | Yes  | Yes   |
| JDX         | `.jdx`    | Yes  | No    |
| MZmine JSON | `.json`   | Yes  | Yes   |

!!! tip

    The **MZmine JSON** format preserves full numeric precision and is recommended when libraries
    are intended to be re-imported into mzmine.

---

## User interface

The editor is organized as a three-column layout:

- **Left panel** -- A filterable, checkable list of library entries. Each entry displays its index,
  name (or entry ID), and precursor _m/z_. Edited entries are marked with an asterisk (**\***).
- **Center panel** -- An interactive bar chart showing the mass spectrum (_m/z_ vs. intensity) of
  the currently selected entry.
- **Right panel** -- A scrollable form with text fields for all metadata fields (name, precursor
  _m/z_, formula, SMILES, InChI, adduct, retention time, and more). When SMILES or InChI data is
  available, a 2D molecular structure preview is shown above the form.

A **toolbar** at the top provides Open, Save As, and Remove buttons as well as a label showing the
currently loaded file and entry count. A **status bar** at the bottom displays messages about the
most recent operation.

---

## Workflows

### Opening a library (standalone)

1. Click **Open** in the toolbar.
2. Select a spectral library file (MGF, MSP, JDX, or JSON).
3. The format is auto-detected and all entries are loaded on a background thread.
4. The entry list, spectrum chart, and metadata pane are populated automatically.

### Opening a library (embedded in MZmine Pro)

1. Import one or more spectral libraries into the MZmine project.
2. Open the editor via **Spectral library processing → Spectral library editor**.
3. Select the libraries to edit. Each opens in a separate tab.

### Editing metadata

1. Select an entry in the left panel.
2. Modify any metadata field in the right panel.
3. Changes are committed when you press ++enter++ or move focus away from the field.
4. Invalid values are highlighted with a red border and a status-bar message.
5. Changed fields receive an accent-colored border; the entry is marked with **\*** in the list.
6. Editing **SMILES** or **InChI** automatically refreshes the 2D structure preview.

!!! tip

    List-type fields (tags, authors, etc.) accept comma-separated values on a single line or
    multiple lines.

### Removing entries

1. Check one or more entries using the checkboxes in the left panel, or simply select them.
2. Click **Remove** in the toolbar.
3. Removed entries are gone from the working set immediately. This counts as an unsaved change.

### Saving a library

1. Click **Save As** and choose a target file.
2. The output format is determined from the file extension (`.mgf`, `.msp`, or `.json`). If
   ambiguous, the format selected in the file chooser filter is used.
3. Entries are serialized on a background thread. Intensity normalization is applied during export.
4. After saving, the change-tracking baseline is rebuilt and the dirty-state marker is cleared.

---

## Change tracking {#change-tracking}

The editor tracks unsaved changes at two levels:

| Level      | What is tracked                              | Visual indicator            |
|------------|----------------------------------------------|-----------------------------|
| Field      | Individual metadata values compared to the loaded/saved baseline | Accent border on the field |
| Structural | Entry removals (cannot be inferred from field diffs)            | Window title `*` marker    |

When unsaved changes exist, the window title (or tab subtitle) shows an asterisk. Opening a new
file while changes are pending shows a confirmation dialog asking whether to discard edits.

---

## Parameters

The spectral library editor does not expose a traditional parameter dialog. When used as an embedded
module inside MZmine Pro, the only parameter is the library selection:

#### **Spectral libraries**

Select one or more spectral libraries that have been imported into the current project. Each library
is opened in its own editor tab.

---

{{ git_page_authors }}
