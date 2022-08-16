# Same m/z and RT range gap filler

This module is found in **Feature list methods → Gap filling → Same m/z and RT range gap filler**.
This method fills in gaps in each peak list row by using the same m/z and retention time range as other peaks in the row. The m/z and retention time ranges where the new peaks will be sought are obtained using the ranges of the rest of the peaks in the same row. The minimum value of these ranges is the minimum value in the range of all the peaks in the row and the same happens with the maximum value. User-specified tolerance is added to the m/z range. The new peak is constructed using the highest data point of each scan within the determined m/z and retention time ranges.

### Parameters

#### Name suffix
Suffix to be added to the peak list name.

#### m/z tolerance
Tolerance, which is added to the m/z range of other peaks in the peak list row.

#### Original feature list
The user can either select to keep or remove the original feature list.
