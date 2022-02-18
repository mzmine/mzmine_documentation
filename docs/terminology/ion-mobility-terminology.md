# Ion mobility spectrometry terminology

## Background
Ion-mobility mass-spectrometry, here simply referred to as ion-mobility (IM), is an analytical technique where ions are separated through a gas-filled mobility cell prior to the MS acquisition. Ions drift through the IM cell with different velocity based on their interaction with the buffer gas, which allows for the separation of different shaped molecules. Modern devieces are able to perform IM separation on a millisecond timescale, typically within 10 to 100 ms. Thus, IM nicely fits in-between LC separation (~seconds timescale) and MS detection of TOF instruments (~microseconds timescale). This allows LC-IM-MS insturments to acqurie several MS spectra during each [accumulation](#accumulations-mobility-scans-and-frames), without incurring sensitivity loss. For example, assuming a typical 100 µs MS-acquisition time of TOF analyzers, around 1000 spectra can be recorded within 100 ms of IM separation. Therefore, as opposed to LC-MS, multiple MS (or MS2) spectra are associated to each RT in LC-IM-MS data. A more detailed explanation of LC-MS and LC-IMS-MS raw data structure is provided [here](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md).

### Trapped ion mobility spectrometry (TIMS) - Todo
Trapped ion mobility spectrometry (TIMS) reverses the concept of traditional drift tube IM. Rather than moving ions through astationary gas, TIMS holds ions stationary against a moving gas and then releases them according to their mobility. 
Video: https://www.youtube.com/watch?v=cWjz32wky2A

### Time-dispersve ion mobility spectrometry (DTIMS and TWIMS) - Todo
Time-dispersve IM devices include "traditional" drift tube (DTIMS) and travelling-wave (TWIMS) devices. In classic DTIM, ions migrate through aninert buffer gas under the influence of a weak electricfield, whereas collisions with buffer gas molecules retard theprogress of the ions. As larger ions have more collisions withthe gas, they are more strongly retarded than their smaller counterparts. Thus, smaller ions, having a smaller cross section, arrive earlier at the detector than ions with a larger collisional cross section (CCS). The ion mobility K is then defined as the ratio of the analyte's steady-state net drift velocity to the applied electric field, and it is convention toc alculate the reduced ion mobility K0 at standard pressur eand standard temperature, often reported as the inverse reduced ion mobility 1/K0.


## Terminology

### Accumulations, Mobility Scans and Frames

Altough mainly used for TIMS, the term "_accumulation_" refers to the pack of ions gathered at the head of the IM device prior to the release and separation in the IM cell. As explained [above](#background), since the accumulation-separation cycle typically last ~100 ms, multiple MS spectra (referred to as "_mobility scans_" in MZmine) are acquired during each cycle. The set of _mobility scans_ collected during each IM separation constitutes a "_frame_". A _frame_ can be seen as the IM separation of a single _accumulation_, along which multiple MS spectra are collected. Several _frames_ are contained within one LC peak. Thus, the frame number are a natural unit to measure chromatographic RT. See [here](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md) for more details.

--FIGURE HERE--

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
