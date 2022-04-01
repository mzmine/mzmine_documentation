# Spectral library search

The spectral library search can be performed on feature lists, feature rows, or single scans. Depending on the MS level (MS1 or MS2), all corresponding rows will be matched against selected spectral libraries that were previously imported (formats: .json, .mgf, .msp, or .jdx).

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
the amount of spectra to match.

#### Remove precursor

#### Spectral m/z tolerance

#### CCS tolerance

#### Minimum ion intensity

#### 13 C deisotoping

#### Crop spectra to m/z overlap
