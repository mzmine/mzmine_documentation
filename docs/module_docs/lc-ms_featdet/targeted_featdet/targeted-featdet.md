# **Targeted feature detection**

## **Description**

:material-menu-open: **Feature detection → LC-MS → Targeted feature detection**

This algorithm opens a *.csv file with a list of peaks and searches for each peak in the selected raw data file. 
The most crucial parameters are **m/z tolerance** and **Retention time tolerance**, which define the window where the algorithm should find the new peak. It is centered in the m/z average and retention time average of the source peak list. Once the best candidate is found inside the window, its shape in RT direction is also checked.

The *.csv file should have three columns:

- The first column should contain the expected M/Z,
- the second column the expected RT,
- and the third the peak name. 

:warning: Each peak should be in a different row.

## **Parameters**

#### **Name suffix**

Suffix to be added to the peak list name.

#### **Peak list file**

Path of the csv file containing the list of peaks to be detected.

#### **Field separator**

Character(s) used to separate fields in the peak list file.

#### **Ignore first line**

Check to ignore the first line of peak list file.

#### **Intensity tolerance**

This value sets the maximum allowed deviation from expected shape of a peak in chromatographic direction.

#### **Noise level**

The minimum intensity level for a data point to be considered part of a chromatogram. All data points below this intensity level are ignored.

#### **m/z Tolerance**

Maximum allowed m/z difference to find the peak

#### **Retention time tolerance**
Maximum allowed retention time difference to find the peak

{{ git_page_authors }}