# **Spectral library search**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search spectra → Spectral library
search** 
or
:material-menu-open: with a right click on one or multiple selected feature rows **Search → Spectral library search**

The spectral library search module can be performed on feature lists, individual features (contained in feature list rows), or single scans. 

Depending on the **MS level** (MS1 or MS2), all corresponding query scans (e.g., extracted from the rows) will be matched against selected spectral libraries that were previously imported.

:material-lightbulb: Preferred ways to import libraries are in this order:

- together with spectral data files in the advanced data import:

    **Raw data methods → Raw data import → MS data (advanced)**

- drag and drop into the main window

- with a dedicated import module: 

    **Raw data methods → Raw data import → Spectral library import** or from **Feature list methods → Annotation → Search spectra → Import spectral libraries.**

### **Supported library formats**

- *.json: MassBank of North America (MoNA) ([download](https://mona.fiehnlab.ucdavis.edu/downloads))
- *.json: The Global Natural Product Social Molecular Networking (GNPS) (format from the spectral DB submission module)
- *.mgf: GNPS ([download](https://gnps-external.ucsd.edu/gnpslibrary))
- *.msp: MoNA
- *.msp: National Institute of Standards and Technology (NIST)
- *.jdx: JCAMP-DX

## **Parameters**

![library_search](spectral_library_search.png)

#### **Spectral libraries**

The spectral libraries of interest need to be imported before applying spectral library search. 
Either uses all imported spectral libraries or only the selected libraries.

#### **MS level**

Choose the MS level of the scans that should be compared with the library. 

Set the MS level to "1" to compare MS^1^ spectra, e.g., from GC-EI-MS or MALDI-imaging MS^1^ data. 

Use "2" or higher for fragmentation scans. 

:warning: In case of issues with the scan selection, check how the actual scan numbers are reported in the data files and in MZmine's raw data overview and scan list.

#### **Check all scans (only for MS2)**

This option enables the comparison of all MS2 scans.

:warning: Otherwise, only the most intense MS^2^ scan (the highest TIC) is used for the matching.

:warning: It does not apply to MS1 scans.

#### **Precursor m/z tolerance**

This option is only used for MS level > 1. Here, the library entries are filtered by their precursor m/z reducing the number of spectral-pairs to match. 

The absolute (in m/z) and relative (in ppm) m/z tolerance can be set. The **maximum tolerance** for each precursor is applied. 

Considering that the precursor isolation window is often far greater than the resolution or accuracy of the MS scan, this parameter is often set to higher m/z tolerances. 

Another aspect is the used library, which might contain uncalibrated reference spectra from lower resolution instruments.

#### **Remove precursor**

:warning: Can be selected only for MS level > 1. 

Depending on the fragmentation method, e.g., collision induced dissociation (CID) or higher-energy collisional dissociation (HCD), the precursor can be detected with different intensities resulting in varying cosine similarities during the library matching. 

Therefore, this option enables the removal of the precursor signal within the precursor m/z tolerance (parameter above) prior to the matching. 

[//]: # (TODO Add separate entry on similarity measures)

#### **Spectral m/z tolerance**

This m/z tolerance is used to pair signals in the query and library scans. It 
can be set in absolute (in m/z) and relative (in ppm) m/z tolerance, whereas 
the maximum tolerance for each m/z value is applied. It must be kept in mind, which mass resolutions are achieved 
within the experimental spectra and within the spectral library.

#### **CCS tolerance**

The [collision cross-section (CCS)](../../terminology/ion-mobility-terminology.md#collisional-cross-section) tolerance can be used in a similar way as the retention time tolerance.

Accordingly, the CCS value of a query will be compared with the library entries and the maximum tolerance
can be set in %.

:warning: If the query or library entry was analyzed without ion mobility (no CCS values), no spectrum will be matched.

#### **Retention time tolerance**

The maximum allowed retention time difference when comparing the query and library scan. It can be set in absolute (min or sec) or relative (%) values.

:material-lightbulb: This option is useful for in-house libraries or standardized libraries that follow the same acquisition protocol with the same set-up, e.g., column, instrument, and method). 

#### **Crop spectra to m/z overlap**

If query and library scans were acquired with different methods, e.g., mass range, fragmentation energy or mode, it can be helpful to crop the spectra to their overlapping m/z range (+ m/z tolerance). 
This is done by using the maximum m/z range where both spectra contain signals.

:warning: However, this method will boost false matches and needs strict manual interpretation.

#### **Minimum ion intensity**

Signals in the query scan below the minimum ion intensity will be filtered from the mass lists and are not taken into account during the library matching. Absolute values.

#### **^13^C deisotoping**

Removes ^13^C isotope signals from the mass list using the following parameters:

- **m/z tolerance**: Maximum allowed difference between the measured and predicted isotope m/z values. The absolute (in m/z) and relative (in ppm) m/z tolerance can be set, whereas the maximum tolerance for each m/z value is applied.

- **Monotonic shape**: If enabled, the monotonically decreasing height of isotope pattern is required.

- **Maximum charge**: The maximum charge that will be considered for detecting the isotope pattern. For singly charged ions, the ^13^C isotope will be expected +1 whereas for doubly charged ions it will be +0.5 (+1 m/z divided by the charge 2). 

#### **Min matched isotope signals**

This option is only useful if the query AND library entries contain isotope patterns (e.g., in MS^1^ or with wider precursor isolation 
windows). 

The minimum number of matched signals of ^13^C isotopes. 

:warning: It cannot be applied when ^13^C deisotoping is enabled.

#### **Min matched signals**

The query mass list and spectral library entry must contain at least this number of matched (paired) m/z values (+- m/z tolerance). 

Common parameters include 4 signals for smaller molecules and 6 for more confident matches.

:warning: This parameter must be set carefully to not exclude compounds that show less
fragmentation, when using a higher number of matched signals. 

:warning: Choosing a lower number of matched
signals can result in spurious library hits.

#### **Similarity**

Several algorithms can be applied to calculate the similarity of the query and library scans and to filter the resulting library matches. The available algorithms are:

- Weighted dot-product cosine,
- Composite dot-product identity (similar to NIST search).

More details are available [here](spectral-similarity-measures.md).

:material-lightbulb: The **weighted dot-product cosine** similarity is used for comparing MS^2^ data, whereas the
**composite dot-product identity (similar to NIST search)** considers the relative intensity of
neighboring signals and is, therefore, applied to MS^1^ spectra from GC-EI-MS.
