# Peak finder

Some chromatographic peaks may not be detected in every sample for several reasons (deficient peak detection, mistake in the alignment of different peak lists etc.), causing undesirable gaps (missing values) in the aligned feature table. To account for this problem, the user can use the Peak finder module which searches through the original raw data to find the missing spectra, and is found under **Feature list methods → Gap filling → Peak finder**.
This algorithm fills the gaps in the peak list when it is possible according with the parameters defined by the user, with the most crucial being **m/z tolerance** and **RT tolerance**. These two parameters define the window where the algorithm should find the new peak. 


## Parameters

### Name suffix
Suffix to be added to the peak list name. 

### Intensity tolerance
Maximum allowed deviation from the expected peak shape in chromatographic direction.

### m/z tolerance
m/z range which will be applied when searching for the possible peak in the raw data.

### Retention time tolerance
Retention time range when searching for the possible peak in the raw data.

### Minimum data points
Feature will be used for gap filling only if it satisfies the set minimum number of data points.

:bulb: Usually lower number of data points is used.

### Original fature lits
User can either keep, remove or process in place of the original feature list.

