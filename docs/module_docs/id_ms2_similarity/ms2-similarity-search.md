# **MS2 Similarity Search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search spectra → MS2 similarity search**

Ions arising from compounds with similar chemical structures often give similar fragmentation patterns (MS2 spectra). Therefore, calculating the similarity between MS2 spectra is a useful approach for the discovery of structurally similar compounds. 

This module calculates the similarity between **centroided MS2 spectra** associated with two feature lists. These two feature lists can be the same feature list, or different feature lists. 

The module outputs the result of the search, the MS2 similarity comparisons of feature list (1) with feature list (2), into the "Identity" column of feature list (1).

:material-lightbulb: In practice, you can consider the features in feature lists (1) as "bait", which is used to "fish" for MS2 similarity from feature list (2). Feature list (1) or feature list (2) can be a single peak + MS2 spectra, or an entire experiment.

[//]: # (Example output of the MS2 similarity module: )

[//]: # (TODO ADd example)
[//]: # (In this example, the presumed precursor ion of m/z 360.9615 at RT 10.53 has a high degree of MS2 spectral similarity to the MS2 of the precursor ion with m/z 281.0047 & RT 12.55. In actuality, precursor ion 360.9615 is the [M+H] of the sulfonated version &#40;sulfoluciferin&#41; of the 281.0047 compound &#40;firefly luciferin&#41;. Sulfoluciferin was discovered by a MS2 similarity approach. See here for more information: &#40;Fallon et al., 2016&#41;)

### **MS2 similarity score**

The similarity metric used is as follows: 

- For all MS2 spectra in feature list (1) **"MS2 spectra A"**, and feature list (2) **"MS2 spectra B"**, iterate over all ions in MS2 spectra A (**ion "i"**), and over all ions in MS2 spectra B (**ion "j"**). 
- For a given ion, only include this ion in following calculations if its intensity is greater than the **minimum ion intensity parameter**. 
- Compare the m/z values of ions "i" and "j". If these m/z values are within the range specified by the **m/z tolerance** parameter, consider these ions identical, and therefore "matched". 
- If two ions match, roughly score the match by multiplying the intensity of ions "i" and "j". Save that as the **"ion match subscore"**. 
- Repeat this for every ion i and j in MS2 spectra A and MS2 spectra B, and report the sum of the ion match subscores as the total **"spectral match score"**. 
- If this spectral match score is greater than the **minimum spectral match score** parameter, annotate the "Identity" column of feature list (1) with the matched ions, and the total spectral match score of the MS2 similarity calculation.

### **Interpreting the results**

The score from of a MS2 similarity match should not be taken as an absolute measure, as it depends on the instrument reported intensity value (which is an uncalibrated and relative measure). 

That being said, as the reported score increases when the intensity of the matched ion is higher, it is useful as a quick metric to find the matches between the most intense MS2 spectra, and potentially the most reliable compounds.

:warning: It is worth mentioning that the link between the MS2 spectra, and the presumed precursor ion in the feature list is somewhat tentative. As the isolation window of the quadrapoles typically used for selection of the precursor ion in MS2 fragmentation analysis is typically around ~1 m/z unit, ions from the MS2 fragmentation spectra from an abundant compound with a long chromatographic tail will often show up in the MS2 values of unrelated compounds, but whose precursor isolation window picks up ions from the original compound. 

[//]: # (Is this information up-to-date?)
An experimental Python script which converts the MS2 similarity relationships exported from MZmine2 in CSV format into GraphML format suitable for viewing in the freely available **graph manipulation software Cytoscape** is available on Github (<a>https://github.com/photocyte/ms2_graph</a>).

## **Parameters**

#### **Feature list (1)**

A single feature list with features that have associated centroided MS2 spectra. Results from the module are output into the identifications column of Feature list (1)

#### **Feature list (2)**

A single feature list, which has centroided MS2 spectra (in the masslist). This can be the same as Feature list (1), or a different peaklist / experiment. 

For best results Feature list (2) should have MS data with the same polarity as Feature list (1), and close range of m/z values close (e.g. LC/MS data obtained on the same day, or m/z calibrated between the two feature lists).

#### **m/z tolerance**

Maximum allowed m/z difference between two ions to be considered identical, and therefore "matched". 

[//]: # (TODO Either transfer this info to terminology or remove altogether)
[//]: # (Depends on the mass accuracy, precision, and resolution of the MS data. For data obtained on HRAM instruments, and when comparing within the same peaklist &#40;aka the same experiment or LC/MS run&#41;, this parameter can be set to the mass precision of the instrument during that experiment &#40;4e-4 m/z or ~1 PPM for Q-Exactive&#41;. It is recommended that you set this value to the smallest range which reliably matches your ions of interest.)

#### **Minimum MS2 ion intensity** 

Minimum ion intensity to consider in MS2 comparison.
Ions of the MS2 spectra below this threshold will be ignored. 

:material-lightbulb: This parameter depends on your instrument, but 1e5 is a reasonable value. 

:material-lightbulb: Set to 0 to use all ions.

#### **Minimum ion(s) matched per MS2 comparison**

Minimum number of matched ions needed in a given MS2 similarity comparison. Otherwise, that spectral match will not be reported. 

:material-lightbulb: This depends on the compounds being compared, but roughly speaking 2-5 is a reasonable number. For complex spectra values of 10-20+ may be reasonable. 

:material-lightbulb: Set to 0 to report all matches.

#### **Minimum spectral match score to report**

Minimum spectral match score threshold, below which spectral matches will not be reported. 

[//]: # (TODO 1e10??)

[//]: # (A value of 1e10 is a decent cutoff on a Q-Exactive instrument with typical data. Set to 0 to report all matches.)