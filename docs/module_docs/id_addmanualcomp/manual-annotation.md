# Manual compound annotation

:material-menu-open: **Feature table → right-click → Identification → Annotate manually**

Lets you attach a compound identity to a single feature list row by filling in a form. Use this
when you know the identity of a feature from external data (e.g. an internal standard or a
reference compound) and want to record it without running an automated search module.

The annotation is stored as a `CompoundDBAnnotation` and labeled with the username of the person
who created it.

---

## Parameters

No standalone parameter dialog is shown to the user — the module is launched directly from the
feature table context menu and presents its own input form.

### Input form fields

| Field | Type | Description |
|---|---|---|
| CCS | Number | Collision cross-section (Å²) |
| Comment | String | Free-text note |
| Compound Name | String | Primary human-readable compound name |
| Formula | String | Molecular formula (e.g. `C6H12O6`) |
| InChI | String | IUPAC International Chemical Identifier |
| InChIKey | String | Hashed InChI key |
| Ion Type / Adduct | Ion type | Adduct, e.g. `[M+H]+` |
| Precursor m/z | Number | Exact precursor mass-to-charge ratio |
| RT | Number | Retention time |
| SMILES | String | SMILES structure string |

Entering a valid SMILES or InChI string displays a live 2D structure preview above the form.

### Validation

The **Save** button stays disabled until both conditions are satisfied:

1. **At least one compound name identifier** must be non-blank — any of: Compound Name, IUPAC
   Name, Internal ID, SMILES, InChI, InChIKey, Formula, or CAS.
2. **At least one m/z source** must be provided — any of:
    - Precursor m/z entered directly, **or**
    - Formula + Ion Type (m/z calculated from these), **or**
    - SMILES + Ion Type (formula is first derived from the structure, then m/z is calculated).

---

## Algorithm {#algorithm}

### On save

1. A compound annotation is built from all non-empty form fields.
2. Missing values that can be derived from what was entered are calculated automatically:

    | Derived field | Source |
    |---|---|
    | Formula | Derived from SMILES/InChI structure if not entered directly |
    | Precursor m/z | Calculated from Formula + Ion Type if not entered directly |
    | Neutral mass | Calculated from Precursor m/z and Ion Type |
    | Ion Type | Best-match adduct inferred from neutral mass vs. row m/z if not specified |
    | m/z PPM difference | Annotation m/z vs. row average m/z |
    | m/z absolute difference | Annotation m/z vs. row average m/z |
    | RT absolute difference | Annotation RT vs. row average RT (if RT was entered) |
    | CCS relative error (%) | Annotation CCS vs. row average CCS (if CCS was entered) |

3. The **Database Name** field is set to `"Annotated manually by <username>"` (falls back to
   `"unknown user"` when no user is logged in).
4. The annotation is added to the row and the feature table is refreshed.

!!! tip

    If you know the SMILES or InChI of a compound, entering it together with an adduct is the most
    complete way to annotate: formula, m/z, neutral mass, and mass error are all derived
    automatically.

!!! warning

    This module annotates exactly **one selected row** at a time. To annotate multiple rows, run
    the annotation for each row individually, or use an automated search module (e.g. local
    compound database search).

---

{{ git_page_authors }}
