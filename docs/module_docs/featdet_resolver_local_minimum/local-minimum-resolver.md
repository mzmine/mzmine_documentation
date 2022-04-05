# **Local Minimum Resolver**

During the EICs building, overalpping and partially co-eluting peaks are retained as single features in the faeture list (see, for example, [ADAP chromatogram builder](../featdet_adap_chromatogram_builder/adap-chromatogram-builder.md)). The _local minimum resolver_ module aims at splitting such "shoulder" LC peaks into individual features (_i.e._ [chromatographic deconvolution](../../terminology/general-terminology.md#chromatographic-deconvolution)) based on local minima. In fact, a local minimum in the EIC trace might correspond to the valley between two adjacent, partially-resolved peaks.

The algorithm examines all the data points in the EIC trace starting from the earliest RT. A scan window is set (see _Minimum search range RT/Mobility_ parameter) and centred around the examined data point. A data point is considered a local minimum if it is the lowest intense point within the scan window. Moreover, it has to be X times lower than the highest point in the window (see _Min ratio of peak top/edge_ parameter). When a local minumum is found, a set of user-defined intensity and peak duration requirements is checked. If they are fulfilled, the original overlapping peaks are split into new, distinct features.

With the implementation of IM support in MZmine 3, this module was expanded and can now be applied to both the RT and IM dimension (see [Resolving the ion mobility dimension](#resolving-the-ion-mobility-dimension)).

:octicons-light-bulb-16: **Tip**. The LMR is particularly suitable for LC-MS data with little 
noise and nice peak shapes.

---
## **Parameters settings**
:material-menu-open: Feature detection → Chromatogram resolving → Local minimum resolver

![](local-minimum-resolver.png)


#### **Suffix**
String added as suffix when creating the corresponding feature list.

#### **Original feature list**
Keep or remove the processed feature list(s).

#### **MS/MS scan pairing**
Pair MS/MS fragmentation spectra collected in [DDA](../../terminology/general-terminology.md#data-dependent-acqusition-mode) mode to the resolved features. This is optional at this stage as the same can be done with a separate [module](../featdet_ms2_scan_pairing/ms2_scan_pairing.md). See [MS2 scan pairing](../featdet_ms2_scan_pairing/ms2_scan_pairing.md) documentation for more details.


#### **Dimension**
Dimension to be resolved. Select _Retention time_ or _Mobility_ to run the module over the RT or ion mobility dimension, respectively.

#### **Chromatographic threshold**
Percentage of data points in the EIC removed before local minima search. The algorithm finds the intensity value (threshold) such that the specified percentage of EIC's data points are below the threshold. All such data points are removed. For example, a _Chromatographic threshold_ = 50% will discard the lowest-intense 50% data points. This represents an important filter for noisy chromatogram and significantly reduces the precessing time.

:octicons-alert-16: Since the algorithms examines the EICs throughout the entire RT range (_i.e._ also the zero data points are considered), we recommend to set this value rather high (_e.g._ 95%) and lower it only if necessary. 
:octicons-alert-16: ION MOBILITY 80%

**Minimum search range RT/Mobility (absolute)**: size of the moving window examined for local minima search. Overly low values can cause peak edges to be cut off. On the other hand, too high might lead to incomplete separation of narrowly eluting compounds.


**Minimum relative height**: minimum relative intensity (respect to the highest data point in the EIC) a peak need to reach to be retained as a feature. Overly high thresholds may lead tolow-intensity features being discarded.

:octicons-light-bulb-16: **Tip**. Modern HRMS instruments can show linear dynamic ranges op to five orders of magnitude. If we take an Orbitrap device with a detector saturation level around 1.0E10 intensity, a _Minimum relative height_ = 0.001 would correspond to 1.0E5.


**Minimum absolute height**: minimum absolute intensity a peak needs to reach to be retained as a feature.

This parameter depends on what you want to detect, the instrument and detector type. Usually, Orbitrap
instruments report higher intensities than TOF instruments. However, the noise level is also higher
for Orbitrap than for TOF instruments. For TOF instruments 1E3 or even 5E2 can be appropriate,
whilst Orbitraps can require 1E5 or 5E4.

**Min ratio of peak top/edge**: Describes the minimum ratio of the highest point of a peak to the lowest point of a peak. This mostly affects detection of low intensity and not-baseline-resolved signals and should be optimised using such a signal as an example.

:octicons-light-bulb-16: **Tip**. We recommend values between 1.7 (not baseline separated) and 2 to start the optimisation.

**Peak durantion range (min/mobility)**: Describes valid peak lengths. Can be used to filter out very short or long noise signals.

**Min # of data points**: Can be used in addition to **Peak duration range** to filter out noise. Should be set no lower than
5 in most cases.

**Show preview**: To-do


## Example
Optimal algorithm settings [1] can lead to recognition of all good features in a "good"
EICs [2] and to few noise recognised as feature in EIC that also contains chromatographic noise
[3].
On the other hand, poorly set parameters [4] will likely recognize all features in
a good EIC [5], but also retain a lot of noise as feature in a noisy EIC [6]. 

Therefore, we recommend optimising the parameters on good EICs and checking the results of these
parameters with a noisy EIC. Most of the time, a noisy EIC can be found by sorting the feature table
by decreasing area.

![test](chromatogramresolving.png)



## Resolving the ion mobility dimension
To-finish

In general, the same principles apply as in the retention time resolving step. However, a few
differences shall be noted. In the screenshot you can also see, that the resolved mobilograms are
recalculated from the raw data and previously apply smoothing steps are therefore lost and must be
reapplied if necessary.

![](mobilityresolving.png)

##### Dimension

Mobility has to be selected as a dimension to resolve mobilograms [1].

##### Chromatographic threshold

Since there are less scans in mobility dimension (e.g., 400 - >1000 per frame, depending on the
instrument type and setting) than in rt dimension (e.g. 5000 for LC-MS depending on acquisition
rate), the threshold should be lowered to 80 or less.

##### Search minimum range

This value determines the search range in mobility dimension. Therefore, this value has to be set
lower when resolving a TIMS (Bruker data) mobilogram, because the absolute numerical values are
smaller (e.g., 0.01). When resolving mobilograms from Waters or Agilent data (mobility as drift time
in ms), the values are higher and must therefore be increased.

Other parameters such as minimum intensities or minimum number of data points should be adjusted
depending on what you want to detect.
