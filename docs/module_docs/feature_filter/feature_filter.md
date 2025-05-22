# **Feature filter**

## **Description**

:material-menu-open: **Feature list methods → Feature list filtering → Feature filter**

This module deletes features in a selected feature list that do not meet the requirements defined by
the user. The filter is performed separately on each raw data file in the peak list.

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

#### Shape score

(since mzmine 4.7)

Tries to fit a chromatographic peak with a Gaussian, a bi-Gaussian, or two Gaussian functions.
The Gaussian function models an ideal case. The bi-Gaussian models each side with by a
different gaussian function, creating a fronting or tailing gaussian. The model with two Gaussian
functions describes a feature that has not been completely resolved during
the [feature resolving step](../featdet_resolver_local_minimum/local-minimum-resolver.md).

#### Top to edge ratio

(since mzmine 4.7)

Determines the top-to-edge ratio of the chromatographic peak by dividing the highest by the lowest
point of the feature.

#### **Keep only features with MS/MS scans**

Peaks without any MS/MS scans will be removed.

#### **Remove source feature list after filtering**

If the checkbox is selected, the source feature list will be removed, and the filtered version will
remain.

{{ git_page_authors }}
