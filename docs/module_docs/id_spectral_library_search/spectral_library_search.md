# Spectral library search

The spectral library search can be performed on feature lists, feature rows, or single scans. Depending on the MS level
(MS1 or MS2), all corresponding rows will be matched against selected spectral libraries that were 
previously imported (formats: .json, .mgf, .msp, or .jdx).      

## Supported library formats
- .json: MassBank of North America (MoNA) ([download](https://mona.fiehnlab.ucdavis.edu/downloads))
- .json: The Global Natural Product Social Molecular Networking (GNPS) (format from the spectral DB submission module)
- .mgf: GNPS ([download](https://gnps-external.ucsd.edu/gnpslibrary))
- .msp: MoNA
- .msp: National Institute of Standards and Technology (NIST)
- .jdx: JCAMP-DX

### Parameters

#### Spectral libraries
The spectral libraries of interest need to be imported before the spectral library search can be applied. 
A single library or multiple libraries can be selected for the library matching workflow. 

#### MS level
Choose the MS level of the scans that should be compared with the library. Set the MS level to "1" to compare MS^1^ 
or GC-EI-MS spectra or set it to "2" or higher for fragmentation scans. Here, the stored MS level of your spectra 
of interest is important.

#### Check all scans (only for MS2)
This option enables the comparison of all MS2 scans otherwise only the most intense MS^2^ scan is used for the matching. 
It does not apply to MS1 scans.

#### Precursor m/z tolerance
This option is only used for MS level > 1. Here, the library entries are filtered by their precursor m/z reducing 
the number of spectra to match. The absolute (in m/z) and relative (in ppm) m/z tolerance can be set, whereas 
the maximum tolerance for each precursor is applied. Here, the isolation window of the precursor must be keep in mind
for the setting.

#### Remove precursor
Can be only selected for MS level > 1. Depending on the fragmentation method, e.g., collision induced dissociation (CID)
or higher-energy collisional dissociation (HCD), the precursor can be detected with different 
intensities resulting in varying cosine similarities during the library matching. Therefore, this option enables the
removal of the precursor signal within the precursor m/z tolerance (parameter above) prior to the matching.

#### Spectral m/z tolerance
During the library matching procedure, the query signals are compared with the library scan signals. 
Therefore, the spectral m/z tolerance is used for matching these signals within a defined mass difference. It 
can be set in absolute (in m/z) and relative (in ppm) m/z tolerance, whereas 
the maximum tolerance for each m/z value is applied. It must keep in mind, which mass resolutions are achieved 
with the own instrument and within the spectral library.

#### Retention time tolerance
Here, you can set the maximum allowed retention time difference when comparing the query and library scan.
This option might be more useful when using your own library with the same set up, e.g., column, instrument,
and method). It can be set in absolute (min or sec) or relative (%) values.

#### CCS tolerance
The collision cross-section (CCS) tolerance can be used in a similar way as the retention time tolerance.
Accordingly, the CCS value of a query will be compared with the library entries and the maximum tolerance
can be set in %. If the query or library entry was analyzed without ion mobility (no CCS values), no spectrum
will be matched.

#### Crop spectra to m/z overlap
If query and library scans were acquired with different methods, e.g., mass range, fragmentation
energy or mode, it can be helpful to crop the spectra to their overlapping m/z range (+ m/z tolerance).

#### Minimum ion intensity
Signals below the minimum ion intensity will be filtered from the mass lists and are not 
taken into account during the library matching.

#### ^13^C deisotoping

- **m/z tolerance**:
- **Monotonic shape**:
- **Maximum charge**:


#### Min matched isotope signals
This option is only useful if the query AND library entries contain isotope pattern (MS^1^ or wider isolation 
windows). You can set the minimum number of matched signals of ^13^C isotopes, distance
of H and 2H or Cl isotopes. It cannot be applied when ^13^C deisotoping is enabled.

#### Min matched signals
Here, the minimum number of matched signals can be set. Accordingly, the query mass list 
and spectral library entry must contain at least a predefined number of the same m/z values 
(+- m/z tolerance). This parameter must be set carefully to not exclude compounds that show less
fragmentation, when using a higher number of matched signals. Choosing a lower number of matched
signals can result in spurious library hits.

#### Similarity
Different algorithm can be applied to calculate the similarity of the query and library 
scans and to filter these library matches. The most common spectral similarity measure for library search
is the cosine similarity or an alternative version.
The **weighted dot-product cosine** similarity is used for comparing MS^2^ data, whereas the
**composite dot-product identity (similar to NIST search)** considers the relative intensity of
neighboring signals and is, therefore, applied to MS^1^ spectra.

- **Weights**: For calculating the cosine similarity, different weighting strategies for  m/z
value and signal intensity can be applied. 
- **Minimum cosine similarity**: This option defines the minimum accepted similarity
score that is taken into account for annotation. The similarity score depends on the data 
handling of unmatched signals.
- **Handle unmatched signals**: Signals that only occur within one scan (query OR library entry)
can be handled in different ways to affect the cosine similarity and controlling the quality
of matching results. 
  - **Keep all and match to zero** is usually used for GC and MS^2^ spectra. Especially GC is 
  a robust and reproducible method, resulting in similar fragmentation spectra for the same 
  compound. Missing signals are replaced by zero-intensity and unaligned signals are paired with
  this value, consequently reducing the similarity score.
  - **Remove all** is the opposite option and discard all unaligned signals, which increases the
  similarity score artificially. Therefore, the last two options are more conservative.
  - **Keep library signals** results in discarding all unaligned signals of the query scan,
  whereas all unaligned library signals are matched to zero. Here, the negative impact of 
  contaminating signals in the query scans are reduced. This might be helpful for mixed spectra
  of multiple compounds, especially during imaging techniques without any further separation.
  - **Keep experimental signals** results in discarding all unaligned signals of the library scan,
  whereas all unaligned query signals are matched to zero.