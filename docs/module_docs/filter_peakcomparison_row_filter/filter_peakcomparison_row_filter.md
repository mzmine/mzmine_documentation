# **Peak comparison rows filter**

## **Description**

:material-menu-open: **Feature list methods → Feature list filtering → Peak comparison rows filter**

This method removes certain rows from an aligned feature list based on peak comparisons in two columns.

# **Parameters**

#### **Name suffix**

Suffix to be added to feature list name.

#### **1st peak column to compare (zero indexed)**

Index of second column for comparison, e.g. "0".

#### **2nd peak column to compare (zero indexed)**

Index of second column for comparison,e.g. "1".

#### **Fold change range : log2(peak1/peak2)**

Return peaks with a fold change within this range.

#### **m/z difference range : peak1 to peak2 (ppm)**

Return peaks with a m/z difference within this range.

#### **RT difference range : peak1 to peak2 (min)**

Return peaks with an RT difference within this range.

#### **Remove source feature list after filtering**

If checked, the original feature list will be removed leaving only the filtered version.