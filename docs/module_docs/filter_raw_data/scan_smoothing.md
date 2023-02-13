# **Scan smoothing (MS1)**

## **Description**

:material-menu-open: **Raw data methods → Raw data filtering → Scan smoothing (MS1)**

This module averages intensity values within a time-scan frame.

## **Parameters**

#### **Suffix**

This string is added to filename as suffix.

#### **Time (min)**

Time span over which intensities will be averaged in the same m/z over scans.

:warning: The max between this and Scan Span will be used.

#### **Scan span**

Number of scan in which intensities will be averaged in the same m/z.

:warning: The max between this and Time Span will be used.

#### **m/z tolerance**

m/z range in which intensities will be averaged.

:warning: The max between this and m/z points will be used. If both equal 0 no m/z smoothing will be performed.

#### **m/z min points**

Number of m/z points used to smooth.

:warning: The max between this and m/z tol will be used. If both equal 0 no m/z smoothing will be performed.

#### **Min height**

Minimum intensity of the highest data point in the chromatogram.

If chromatogram height is below this level, it is not used in the average calculation.

#### **Remove previous files**

Remove processed files to save memory.

{{ git_page_authors }}
