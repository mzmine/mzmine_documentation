# **Standard compound normalizer**

## **Description**

:material-menu-open: **Feature list methods → Normalization → Standard compound normalizer**

The purpose of this module is to reduce the deviation between samples caused by different detection efficiency.

Internal standard peaks must be present in the detected samples. User can select one or multiple internal standard peaks, which must be present in all raw data files. Then peak height (or area) of each peak is normalized by either the **nearest standard** or a **weighted contribution** of all standards.

In case a weighted contribution is used, the contributions of all standards are weighted by distance. The distance of the standard peak to the peak being normalized is calculated as

$$distance = MZvsRT_{Balance} * MZ_{difference} + RT_{difference}$$

where $MZvsRT_{Balance}$ is a multiplier of m/z difference set by **m/z vs RT balance** parameter

:warning: Feature list must be aligned prior to normalization.

## **Parameters**

#### **Name suffix**

Suffix to be added to a processed feature list name

#### **Normalization type**

Normalize intensities using either only one (nearest) standard or using a weighted contribution of all selected standards, weighted by distance.

#### **Feature measurement type**

Selection of either feature height or feature area, which will be used to calculate the normalization factors

#### **m/z vs RT balance**

Used in distance measuring as a multiplier of m/z difference.

#### **Standard compounds**

List of features for choosing the normalization standards

#### **Original peak list**

If selected, the original peak list is automatically removed

{{ git_page_authors }}
