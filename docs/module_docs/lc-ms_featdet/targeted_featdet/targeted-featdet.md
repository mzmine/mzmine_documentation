# **Targeted feature detection**

## **Description**

:material-menu-open: **Feature detection → LC-MS → Targeted feature detection**

This algorithm opens a *.csv or *.tsv file with a list of target compounds and searches for each
target in the selected raw data files. The most crucial parameters are **m/z tolerance** and
**Retention time tolerance**, which define the window where the algorithm should find the new
peak. It is centered on the m/z and retention time of the target. Once the best candidate is found
inside the window, its shape in RT direction is also checked.

The file needs a header line. Its column names must match the names configured in the **Columns**
parameter, one target per row. The file format and the available columns are the same as for the
[Local compound database search](../../id_prec_local_cmpd_db/local-cmpd-db-search.md#database-file).
Each target needs an m/z, which is either given directly (`mz`) or calculated from a neutral mass,
formula, or SMILES together with the **Calculate adduct masses** parameter.

:warning: Targets that overlap within the tolerances are merged into a single feature list row that
carries all their annotations.

## **Parameters**

#### **Scan filters**

See [Scan selection filters](../../scan_selection/scan_selection.md) for all available criteria and
combination rules.

#### **Name suffix**

Suffix to be added to the feature list name. Default is `detectedPeak`.

#### **Database file**

Path of the csv file containing the list of targets to be detected.

#### **Field separator**

Column separator of the database file. Options are **Auto detect** (default), **Comma  ,**,
**Semicolon  ;**, **Tab**, **Space**, and **Custom**, which accepts any other character (`\t` is
also accepted for a tab).

**Auto detect** uses the separator declared in a `sep=` first line (as written by Excel), if
present. Otherwise, it tests tab, comma, semicolon, and pipe (`|`) on the first 40 non-empty lines
of the file and picks the best-scoring separator. If no separator can be determined, tab is used for
`.tsv`, `.tab`, and `.txt` files and comma for all other files.

!!! tip

    Batch files and presets from older mzmine versions keep their separator: a previously entered
    `,`, `;`, or `\t` is mapped to the matching option, any other text to **Custom**.

#### **Columns**

Columns to import from the database file. Enabled by default are `neutral mass`, `mz`, `rt`,
`formula`, `smiles`, and `comment`; `adduct`, `inchi`, `inchi key`, `name`, `CCS`, and `mobility`
can be enabled in addition. Double-click a column name to rename it to match the header of your
file.

#### **Intensity tolerance**

This value sets the maximum allowed deviation from the expected /\ shape of a peak in
chromatographic direction.

#### **m/z tolerance**

Maximum allowed m/z difference to find the peak.

#### **Retention time tolerance** _(Optional)_

Maximum allowed retention time difference to find the peak.

#### **Mobility tolerance** _(Optional)_

Maximum allowed mobility difference to find the peak in ion mobility data.

#### **Calculate adduct masses** _(Optional)_

Ion types to calculate the m/z of each target from its neutral mass, formula, or SMILES. Only ion
types that match the polarity of the selected scans are used. Either the neutral mass, formula, or
SMILES must be imported for every compound.

{{ git_page_authors }}
