# **Local compound database search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search precursor
mass → Local compound database (CSV) search**

This method assigns identity to features according to their m/z. Additionally, retention
time, mobility, and CCS values can be provided to restrict the annotation. Otherwise, only the m/z
is used for the matching, which can be used for the spectral library building. For compound annotation
in complex samples, an additional identifier should be available.

:material-lightbulb: If you want to filter your feature list for a list of target compounds
afterwards, you can use
the [Feature list rows filter](../feature_list_row_filter/feature_list_rows_filter.md)
with the only identified option.

The user has to provide a database of m/z values (or neutral masses, formulae,
smiles strings to calculate m/zs from) and retention times in ***.csv format** (
see below).

### **Database file**

Database file has to be provided in ***.csv** or ***.tsv format** (Comma-Separated or tab).
Such files can be exported from a spreadsheet software such as MS Excel, or
edited manually using a text editor.

The following examples shows the structure of the database file:

    ID,monoisotopic_mass,rt,compound_name,formula
    1,175.121,24.5,Arginine,C6H14N4O2
    2,133.063,11.9,Asparagine,C4H8N2O3
    3,134.047,11.7,Aspartate,C4H7NO4

:warning: If the m/z value or Retention time value in the CSV file is 0, then
the value is considered as a wild card. E.g, the following item will match all
peaks of 174.121 m/z without considering the retention time:

    1,175.121,0,Arginine,C6H14N4O2

The available fields in a library file include:

| Field name        | Field description               |
|-------------------|---------------------------------|
| monoisotopic_mass | Neutral mass                    |
| mz                | Precursor m/z                   |
| rt                | Retention time                  |
| formula           | Formula                         |
| smiles            | SMILES                          |
| inchi             | InChI                           |
| compound_name     | Compound name                   |
| CCS               | CCS/ Å<sup>2</sup>              |
| mobility          | Ion mobility                    |
| comment           | Text comment                    |
| adduct            | Information on adduct           |
| pubchem_cid       | Compound ID in PubChem database |

## **Parameters**

#### **Database file**

Path and Name of the file that contains information for peak identification.

#### **Field separator**

Character(s) used to separate fields in the database file.
- *.csv = ,
- *.tsv = \t

#### **Columns**

Columns that should be imported from the library file are selected. The choice of columns
depends on the availability of retention time, mobility data, information about adducts, and
the presence of the PubChemID in your database file. If the exact mass should be calculated, the
neutral mass (or structure information) needs to be provided and enabled together with the adduct
settings. When only a structure is provided, MZmine calculates the monoisotopic mass based on the
given information. If the table contains already the adduct m/z value, the precursor m/z can be selected. 
This might be useful, when the ionization differs within one dataset. The column names can be adapted
to your table by double click and pressing enter after changing.

#### **m/z tolerance**

Maximum allowed m/z difference to set an annotation to a peak (max. difference between exact and accurate mass).

#### **Retention time tolerance**

Maximum allowed retention time difference to set an identification to a peak.

#### **Mobility time tolerance**

Maximum allowed tolerance to set an identification to a peak.

#### **CCS tolerance (%)**

Maximum allowed difference (in percents) to set an identification to a peak.

#### **Use isotope matcher**

This option matches the predicted isotope pattern against the detected ones. It is only possible to
use if the isotope finder was run before.

#### **Use adducts**

This can be used, if the precursor should be calculated. If chosen, m/z values for all set adducts
will be calculated and matched against the feature list. For this option, you have to provide a neutral mass, a
formula or a SMILES code to calculate the m/z from. Be aware, if multiple adducts are set,
more sporious hits will be created. This is also important for the spectral library creation, when
one sample contains multiple compounds. Therefore the modifications can be limit to specific adduct
combinations. This can be done by adding and combining them. For example M-H2O+H, by adding M-H2O and combining
it with the M+H.

#### **Filter filename header**

This option is important for the library building workflow. This column contains a unique sample id
to link the compound to the corresponding acquisition file. The unique sample id can be either part
of the filename or the complete filename. If data are acquired multiple times with differnet method,
a part of the filename enables the option of one metadata file or one column for the identification.
The unique sampel id can be a combination of library_id, the plate or rack location together with the well or rack
position. It is important to notice, that the unique sample id should not end on a number, otherwise
libid_Plate1_A2 is also contained in libid_Plate1_A20 ect.

#### **Append comment fields**

Multiple fields, that are appended to the comment. They are separated by comma. For example: Pathway,
Synonyms,...

{{ git_page_authors }}