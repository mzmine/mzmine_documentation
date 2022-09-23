# **Feature list rows filter**

## **Description**

:material-menu-open: **Feature list methods → Feature list filtering → Feature list rows filter** 

This filter deletes all rows in a selected peak list that do not meet requirements defined by the user.

A range of different requirements can be set, such as the minimum number of features in the row, the minimum number of features in an isotope pattern, peak duration etc. 

When an aligned peak list, i.e. multiple peaks per row, is filtered then the average of each row's peak duration, m/z and retention time values are used to filter the row.


## **Parameters**

#### **Name suffix**
Suffix to be added to feature list name.

#### **Minimum features in a row (abs or %)**
Minimum number of features detected in a row required to not remove it. Values < 1 will be interpreted as %.

#### **Minimum features in an isotope pattern**

Minimum number of features in a row's isotope pattern required to not remove it.

#### **Validate 13C isotope pattern**
If ticked, searches for a +1 13C signal (considering possible charge states) within estimated range of carbon atoms. Uses [13C isotope filter](../filter_isotope_filter/isotope_filter.md).

#### **m/z**
Range of acceptable (average) m/z values in a row required to not remove it.

#### **Retention time**
Range of acceptable (average) retention times in minutes.

#### **Features duration range**
Range of acceptable (average) feature durations in a row required not to remove it.

#### **Chromatographic FWHM**
Range of permissible FWHM in a row required not to remove it.

#### **Charge**
Range of Charge in a row required not to remove it.

:warning: Please, run isotopic peaks grouper prior to using this.

#### **Kendrick mass defect**
Filter features in a Kendrick mass defect (KMD) range. For more details see [Kendrick mass defect](../../visualization_modules/processed_additional/processed_additional.md#background).

If KMD is used, following parameters can be changed in the setup.

- **Kendrick mass defect**
  Permissible range of a Kendrick mass defect per row
- **Kendrick mass base**
  Enter a sum formula for a Kendrick mass base, e.g. "CH2"
- **Shift**
  Enter a shift for shift dependent KMD filtering
- **Charge**
  Enter a charge for charge dependent KMD filtering
- **Divisor**
  Enter a divisor for fractional base unit dependent KMD filtering
- **Use Remainder of Kendrick mass**
  Use Remainder of Kendrick mass (RKM) instead of Kendrick mass defect (KMD)

#### **Parameter**
Paremeter defining the group of each sample.

#### **Only identified?**
If the checkbox is selected, only identified compounds will be retained.

#### **Text in identity**
Only rows that contain this text in their peak identity field will be retained.

#### **Text in comment**
Only rows that contain this text in their comment field will be retained.

#### **Keep or remove rows**
User can select to either keep or remove the rows that match the defined criteria.

#### **Feature with MS2 scan**
If checked, only features that have MS2 scan will be kept.

#### **Never remove feature with MS2**
If checked, all rows with MS2 are retained without applying any further filters on them.

#### **Reset the feature number ID**
If checked, row IDs will be reset.

#### **Mass defect**
Mass defect as a feature filter can be used for selective detection of compounds of interest, and the values accepted are 0.314-0.5 or 0.90-0.15.

#### **Original feature list**
It can be either processed in place, kept or removed.
