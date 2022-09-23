# **Align scans (MS1)** 

## **Description**

:material-menu-open: **Raw data methods → Raw data filtering → Align scans (MS1)**

This module aligns scans for small fluctuations correlating consecutive scans. 

## **Parameters**

#### **Suffix**

This string is added to filename as suffix.

#### **Horizontal scans**

Number of scans to be considered in the correlation (to the left and to the right of the scan being aligned).

#### **Max Vertical Alignment**

Maximum number of shifts to be compared. This depends on equipment, normally this should be 1.

#### **Minimum height**

Minimum intensity to be considered for align correlation.

If chromatogram height is below this level, it is not used in the correlation calculation.

#### **Correlation in log**

Transform intensities to _log_ scale before comparing correlation.

#### **Remove previous files**

Remove processed files to save memory.

