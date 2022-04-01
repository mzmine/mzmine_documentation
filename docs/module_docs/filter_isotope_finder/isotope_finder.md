# Isotope pattern finder

The **Isotope pattern finder** is found under **Feature list methods → Isotopes → Isotope pattern finder.**

![](Isotope_pattern_finder.png)

### Parameters

#### Chemical elements
Here you can choose the elements for which you wish the isotope pattern to be considered.

#### m/z tolerance
Maximum allowed difference between two features' m/z values in order for them to be considered the same. The value is specified both as absolute tolerance (in m/z) and relative tolerance (in ppm). The tolerance range is calculated using maximum of the absolute and relative tolerances.

#### Maximum charge of isotope m/z
Maximum possible charge of isotope distribution m/z's. 
All present m/z values obtained by dividing isotope masses with 1,2 ...,maxCharge values will be considered.
The default value is 1, but insert an integer greater than 1 if you want to consider ions of higher charge states.

#### Search in scans
Currently, the supported option is "Single most intense", which means the search for isotopes will happen in the single most intense scan of each feature.