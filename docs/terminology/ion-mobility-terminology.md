# **Ion mobility spectrometry terminology**

## **Background**
Ion-mobility mass-spectrometry, here simply referred to as **ion-mobility (IM)**, is an analytical technique where ions are separated through a gas-filled mobility cell prior to the MS acquisition. 

In classic **drift tube ion mobility (DTIM)**, ions migrate through an inert buffer gas under the influence of a weak electric field.  Ions drift with different **velocity** based on their interaction with the buffer gas, which allows for the separation of different shaped molecules. Modern devices are able to perform IM separation on a millisecond timescale, typically within 10 to 100 ms. 

As larger ions have more collisions with the gas, they are more strongly retarded than their smaller counterparts. Thus, smaller ions, having a smaller cross section, arrive earlier at the detector than ions with a larger collisional cross section ([CCS](#collisional-cross-section)). 

The **ion mobility** $K$ is then defined as the ratio of the analyte's steady-state net drift velocity to the applied electric field, and it is convention to calculate the reduced ion mobility $K_0$ at standard pressure and standard temperature. This value is often reported as the inverse reduced ion mobility $1/K_0$.

From practical point of view, IM nicely fits in-between LC separation (~seconds timescale) and MS detection of TOF instruments (~microseconds timescale). This allows LC-IM-MS instruments to acquire several MS spectra during each [accumulation](#accumulations-mobility-scans-and-frames), without incurring sensitivity loss. 

For example, assuming a typical 100 µs MS-acquisition time of TOF analyzers, around 1000 spectra can be recorded within 100 ms of IM separation. Therefore, as opposed to LC-MS, multiple MS (or MS2) spectra are associated to each RT in LC-IM-MS data. 

A more detailed explanation of LC-MS and LC-IMS-MS raw data structure is provided [here](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md).

[Visual explanation of IMS by Waters](https://www.youtube.com/watch?v=RRxW18bFbHo)

### **Trapped ion mobility spectrometry (TIMS)**

**Trapped ion mobility spectrometry** (TIMS) reverses the concept of traditional drift tube IM. Rather than moving ions through a stationary gas, TIMS holds ions stationary against a **moving gas** and then releases them according to their mobility. 

TIMS has the advantage that the physical dimension of the analyzer can be smaller, whereas the analytical column of gas – the column that flows past during the course of an analysis – can be large and user defined. This can lead to increased method sensitivity.

[Bruker's TIMS TOF Video](https://www.youtube.com/watch?v=cWjz32wky2A)

### Time-dispersive ion mobility spectrometry (DTIMS and TWIMS)

**Time-dispersve IM** devices include "traditional" **drift tube (DTIMS)** and **travelling-wave (TWIMS)** devices. 

In TWIMS, ions are propelled through a gas-filled stacked ring ion guide with the help of travelling voltage waves. 

Higher mobility ions undergo less ‘roll over’ events on the waves than the lower mobility ions. As the waves pass along the device, ions can ‘surf’ on the wave front for a period of time before being overtaken by the wave. Usage of travelling waves makes possible to increase sensitivity, selectivity, and speed of the method.

For more information, see [Fundamentals of Traveling Wave Ion Mobility Spectrometry](https://doi.org/10.1021%2Fac8016295)

## Terminology

### Accumulations, Mobility Scans and Frames

Altough mainly used for TIMS, the term **"accumulation"** refers to the pack of ions gathered at the head of the IM device prior to the release and separation in the IM cell. 

As explained [above](#background), since the accumulation-separation cycle typically last ~100 ms, multiple MS spectra (referred to as **"mobility scans"** in MZmine) are acquired during each cycle. 

**Frame** is the set of **mobility scans** collected during each IM separation. A frame can be seen as the IM separation of a single accumulation, along which multiple MS spectra are collected. Several frames are contained within one LC peak. Thus, the **frame number** are a natural unit to measure chromatographic RT. 

See [here](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md) for more details.

![lcimsmsdata](../workflows/imsworkflow/lcimsmsdataformat.png)

### Mobilograms

A "_mobilogram_" represents the intensity of an m/z or m/z range along the mobility axis. A
_mobilogram_ may be build from multiple frames and summed or built from a single frame.

![mobilogram](mobilogram.png)

### Ion mobility trace

An "_ion mobility trace_" basically represents a mobility resolved extracted ion chromatogram (EIC).

![trace](trace.png)

### Collisional Cross Section
**Collision cross section (CCS)** can be defined as area of interaction between an individual ion and gas molecule. CCS depends on ion's size, shape, and charge. IM-derived CCS values can be used as an additional molecular descriptor to support the compound unknown identification process.

## References
- Meier, F., Brunner, A.D., Koch, S., Cox, J., Räther, O., Mann, M. Online Parallel Accumulation–Serial Fragmentation (PASEF) with a Novel Trapped Ion Mobility Mass Spectrometer. _Molecular & Cellular Proteomics_ (2018). DOI: <a>10.1074/mcp.TIR118.000900</a>
- Paglia, G. et al. Ion Mobility Derived Collision Cross Sections to Support Metabolomics Applications. _Anal. Chem._ (2014). DOI: <a>10.1021/ac500405x</a>


