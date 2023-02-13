# **Feature filter**

## **Description**

:material-menu-open: **Feature list methods → Feature list filtering → Feature filter**

This module deletes features in a selected feature list that do not meet the requirements defined by the user. The filter is performed separately on each raw data file in the peak list.

## **Parameters**

#### **Name suffix**

Suffix to be added to feature list name.

#### **Duration**

Peaks with a duration outside the entered range will be removed.

#### **Area**

Peaks with an area outside the entered range will be removed.

#### **Height**

Peaks with a height outside the entered range will be removed.

#### **\# data points**

Peaks with fewer data points than the entered range will be removed.

#### **FWHM**

Peaks with a FWHM outside the entered range will be removed.

#### **Tailing factor**

Peaks with a tailing factor outside the entered range will be removed.

[//]: # (TODO Explain tailing factor)

#### **Asymmetry factor**

Peaks with an asymmetry factor outside the entered range will be removed.

[//]: # (TODO EXplain asymmetry factor)

#### **Keep only features with MS/MS scans**

Peaks without any MS/MS scans will be removed.

#### **Remove source feature list after filtering**

If the checkbox is selected, the source feature list will be removed, and the filtered version will remain.

{{ git_page_authors }}