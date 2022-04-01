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
Choose the MS level of the scans that should be compared with the library. Set the MS level to "1" to compare MS1 
or GC-EI-MS spectra or set it to "2" or higher for fragmentation scans. Here, the stored MS level of your spectra 
of interest is important.

#### Check all scans (only for MS2)
This option enables the comparison of all MS2 scans otherwise only the most intense MS2 scan is used for the matching. 
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
the maximum tolerance for each m/z value is applied. It must keep in mind, which mass resolutions are achieved with the
own instrument and within the spectral library.

#### Retention time tolerance

Maximum allowed difference between two retention time values

#### CCS tolerance

CCS tolerance for spectral library entries to be matched against a feature. If the row or the library entry does not
have a CCS value, no spectrum will be matched.

#### Crop spectra to m/z overlap

crop query and library spectra to overlapping m/z range (in m/z tolerance). This is helpful if spectra were acquired
with different fragmentation energies/modes

#### Minimum ion intensity

signals below this level will be filteres away from mass lists

#### ^13^C deisotoping

- **m/z tolerance**:
- **Monotonic shape**:
- **Maximum charge**:


#### Min matched isotope signals

#### Min matched signals

#### Similarity


