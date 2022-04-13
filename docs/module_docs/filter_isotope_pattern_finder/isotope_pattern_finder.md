# Isotope pattern finder

The **Isotope pattern finder** is found under **Feature list methods → Isotopes → Isotope pattern finder.**

![](isotope_pattern_finder.png)

The isotope pattern finder will search for all possible isotope signals in the mass lists for each feature. The resulting pattern may contain signals from different charge states as this module tries to capture all available information, unlike the isotope filter, which acts as a feature filter.


### Parameters

#### Chemical elements
Chemical elements for which the isotopes will be considered. 

#### m//z tolerance
Maximum allowed difference between two features' m/z values in order for them to be considered the same. The value is specified both as absolute tolerance (in m/z) and relative tolerance (in ppm). The tolerance range is calculated using maximum of the absolute and relative tolerances.

#### Maximum charge of isotope m/z
Maximum charge to consider for detecting the isotope patterns.

#### Search in scans
Options to search isotopes in the single most intense scan or within all scans in full-widh at half maximum range. Currently, only the single most intense scan is supported.