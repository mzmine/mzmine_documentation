# **Peak finder** 

## **Description**

:material-lightbulb: It is a recommended gap-filling algorithm.

:material-menu-open: **Feature list methods → Gap filling → Peak finder**.

Some chromatographic features in an aligned feature list may not be detected in every sample for several reasons, such as:

- feature shape constraints in the resolver or later feature filters
- co-eluting features that are not baseline separated might be resolved in one sample but kept unsplit in another 
- misalignment due to shifts in m/z, retention time, or ion mobility within feature lists from different samples (or batches). Might originate from inaccurate mass calibration, etc.

All of these reasons can result in undesirable gaps (missing values) in the aligned feature table. Those gaps are not limited to smaller signals but can also affect abundant features. To account for this problem, the user can use the Peak finder module as a secondary, informed feature finding step. The algorithm searches for signals within the original centroided mass spectra. This algorithm fills the gaps in the feature list according to the user parameters, with the most crucial being **m/z tolerance** and **RT tolerance**. These two tolerances define the window where the algorithm should find the new feature. In the feature table, gap-filled features are marked with a grey color as the feature state. 


## **Parameters**

#### **Name suffix**
Suffix to be added to the peak list name. 

#### **Intensity tolerance**
Maximum allowed deviation from the expected peak shape in chromatographic direction.

#### **m/z tolerance**
m/z range which will be applied when searching for the possible feature in the raw data.

#### **Retention time tolerance**
Retention time range when searching for the possible feature in the raw data.

#### **Minimum data points**
Feature will be used for gap filling only if it satisfies the set minimum number of data points.

:material-lightbulb: Usually a lower number of data points is used compared to the primary feature finding workflow with the resolvers.

#### **Original feature list**
User can either keep, remove, or process in place of the original feature list. The latter two increase memory efficiency and throughput while users might want to keep the original feature list as a reference. 

