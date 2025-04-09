# **Retention index calculation**

## **Description**

:material-menu-open: **Feature list methods → Normalization → Retention index calculation**

Retention index calculation assigns a retention index to each feature in the feature list. These are calculated by linear interpolation through the retention times of the straight-chain alkanes, which are listed in CSV files. 

Each raw data file has its features' retention indices calculated separately. In other words, the alkane list is selected independently for each raw data file.

To select the appropriate alkane list, a date is extracted from the name of each CSV file, and each raw data file is assigned the file with the most recent date, up to the raw data file's run date.


## **Parameters**


#### **Feature lists**
Selects the feature lists for which retention indices will be calculated

#### **Alkane scale files**

A list of CSV files, each with a list of straight-chain alkanes and their respective retention times. For example:

| Carbon # | RT     |
|----------|--------|
| 5        | 4.374  |
| 6        | 5.423  |
| 7        | 7.934  |
| 8        | 11.99  |
| 9        | 16.793 |
| 10       | 21.615 |
| 11       | 26.181 |

Each file's name should contain the date that the measurements were taken.


#### **Extrapolation**
This will enable calculation of retention indices for features with retention times not between those of the first and last straight-chain alkanes, performing linear extrapolation past the endpoints of the scale. Not recommended.

#### **Add row summaries**

Enabling this will cause each feature to show the CSV that was used to calculate its retention index. 

Additionally, each feature list row will display the lowest and highest retention index among its features, alongside the difference between those values.

#### **Original feature list**
If REMOVE option is selected, the original feature list is removed, allowing to save memory.

#### **Name suffix**
Suffix to be added to each processed feature list's name


{{ git_page_authors }}