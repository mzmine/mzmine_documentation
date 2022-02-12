# Ion mobility spectrometry terminology

## Background
Ion-mobility mass-spectrometry, here simply referred to as ion-mobility (IM), [...].
Modern devieces are able to perform IM separation on a millisecond timescale, typically within 10 to 100 ms. Thus, IM nicely fits in-between LC separation (~seconds timescale) and MS detection of TOF instruments (~microseconds timescale). This allows LC-IM-MS insturments to acqurie several MS spectra during each [accumulation](#frames-and-mobility-scans), without incurring sensitivity loss. For example, assuming a typical 100 µs MS-acquisition time of TOF analyzers, around 1000 spectra can be recorded within 100 ms of IM separation. Therefore, as opposed to LC-MS, multiple MS (or MS2) spectra are associated to each RT in LC-IM-MS data. A more detailed explanation of LC-MS and LC-IMS-MS raw data structure is provided [here](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md).

### Trapped ion mobility spectrometry
Trapped ion mobility spectrometry (TIMS) reverses the concept of traditional drift tube IM by bringing ions to a rest at different positions in an ion tunnel device, balanced in an electrical field against a constant gas stream.
Video: https://www.youtube.com/watch?v=cWjz32wky2A

### Time-dispersve ion mobility spectrometry
Time-dispersve IM devices include "traditional" drift tube (DTIMS) and travelling-wave (TWIMS) devices. In classic DTIM, ions migrate through aninert buffer gas under the influence of a weak electricfield, whereas collisions with buffer gas molecules retard theprogress of the ions
Todo


## Terminology

### Mobility Scans and Frames
As explained [above](#background), multiple MS (and MS2) spectra are acquired during each IM accumulation. 
The mass spectra acquired during a 
All mass spectra acquired during a single mobility separation are referred to as "_mobility scans_" in MZmine. 

The agglomerate of all the _mobility scans_ for one IM accumulation are called "_frame_".

All the _mobility scans_ witin a single _frame_ can be summed, to represent a single mass spectrum as in classic LC-MS.

top level: one full cycle of scans is called
a frame. Therefore, several frames are contained cover one chromatographic peak.
Frame numbers are thus a natural unit to measure LC retention time.

### Mobilograms

A "_mobilogram_" represents the intensity of an m/z or m/z range along the mobility axis. A
_mobilogram_ may be build from multiple frames and summed or built from a single frame.

![mobilogram](mobilogram.png)

### Ion mobility trace

An "_ion mobility trace_" basically represents a mobility resolved extracted ion chromatogram (EIC).

![trace](trace.png)

### Cross Collisional Section
IM-derived CCS values can be used as an additional molecular descriptor to support the compound unknown identification process.(Paglia et al. 2014) However, the number of acquired spectra per run increases from several thousand to several million, requiring memory-efficient software and new processing algorithms. 


## References
https://doi.org/10.1074/mcp.TIR118.000900
