# **Recursive IMS builder**

## **Description**

:material-menu-open: **Feature detection → LC-IMS-MS → Recursive IMS builder**.

Builds m/z traces for ion mobility spectrometry data.

## **Parameters**

#### **m/z tolerance**

The m/z tolerance to build ion traces. The tolerance is specified as a +- tolerance. 

m/z 500.000 with a tolerance of 0.01 will allow m/z change from 499.99 to 501.01.

#### **Minimum consecutive retention time data points**

The minimum number of consecutive detections in frames (retention time dimension).

#### **Minimum number of data points**

The minimum number of consecutive detections in frames (retention time dimension).

#### **Advanced parameters**

Allows adjustment of internal binning parameters for mobilograms. The default values are set to 1.

**Override default TIMS binning width (Vs/cm²)**

The binning width in mobility units of the selected raw data file.

**Travelling wave binning width (ms)**

The binning width in mobility units of the selected raw data file.

**Drift tube binning width (ms)**

The binning width in mobility units of the selected raw data file.

