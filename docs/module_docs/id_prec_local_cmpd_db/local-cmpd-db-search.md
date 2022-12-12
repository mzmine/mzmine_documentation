# **Local compound database search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search precursor
mass → Local compound database (CSV) search**

This method assigns identity to features according to their m/z and retention
time values.

:material-lightbulb: If you want to filter your feature list for a list of target compounds
afterwards, you can use
the [Feature list rows filter](../feature_list_row_filter/feature_list_rows_filter.md)
with the only identified option.

The user has to provide a database of m/z values (or neutral masses, formulae,
smiles strings to calculate m/zs from) and retention times in ***.csv format** (
see below).

### **Database file**

Database file has to be provided in ***.csv format** (Comma-Separated Values).
Such files can be exported from a spreadsheet software such as MS Excel, or
edited manually using a text editor.

The following examples shows the structure of the database file:

    ID,m/z,Retention time (min),Identity,Formula
    1,175.121,24.5,Arginine,C6H14N4O2
    2,133.063,11.9,Asparagine,C4H8N2O3
    3,134.047,11.7,Aspartate,C4H7NO4

:warning: If the m/z value or Retention time value in the CSV file is 0, then
the value is considered as a wild card. E.g, the following item will match all
peaks of 174.121 m/z without considering the retention time:

    1,175.121,0,Arginine,C6H14N4O2

The available fields in a library file include:

| Field name   | Field description               |
|--------------|---------------------------------|
| neutral mass | Neutral mass                    |
| mz           | Precursor m/z                   |
| rt           | Retention time                  |
| formula      | Formula                         |
| smiles       | SMILES                          |
| name         | Compound name                   |
| CCS          | CCS, Å<sup>2</sup>              |
| mobility     | Ion mobility                    |
| comment      | Text comment                    |
| adduct       | Information on adduct           |
| PubChemID    | Compound ID in PubChem database |

## **Parameters**

#### **Database file**

Name of file that contains information for peak identification.

#### **Field separator**

Character(s) used to separate fields in the database file.

#### **Columns**

Columns that will be imported from the library file. The choice of columns
depends on the availability of mobility data, information about adducts, and
presence of PubChemID in your database file.

#### **m/z tolerance**

Maximum allowed m/z difference to set an identification to a peak.

#### **Retention time tolerance**

Maximum allowed retention time difference to set an identification to a peak.

#### **Mobility time tolerance**

Maximum allowed tolerance between two mobility values.

#### **CCS tolerance (%)**

Maximum allowed difference (in percents) between two CCS values.

#### **Use adducts**

If chosen, m/z values for multiple adducts will be calculated and matched
against feature list. For this option, you have to provide a neutral mass, a
formula or a smiles code to calculate the m/z from.

{{ git_page_authors }}
