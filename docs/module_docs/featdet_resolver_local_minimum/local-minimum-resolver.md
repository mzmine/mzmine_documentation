# **Local Minimum Resolver**

During the EICs building, overalpping and partially co-eluting peaks are retained as single features in the faeture list (see, for example, [ADAP chromatogram builder](../featdet_adap_chromatogram_builder/adap-chromatogram-builder.md)). The _local minimum resolver_ module aims at splitting such "shoulder" LC peaks into individual features (_i.e._ [chromatographic deconvolution](../../terminology/general-terminology.md#chromatographic-resolving)) based on local minima. In fact, a local minimum in the EIC trace might correspond to the valley between two adjacent, partially-resolved peaks.

The algorithm examines all the data points in the EIC trace starting from the earliest RT. A scan window is set (see [Minimum search range RT/Mobility](#minimum-search-range-rtmobility-absolute) parameter) and centred around the examined data point. A data point is considered a local minimum if it is the lowest intense point within the scan window. Moreover, it has to be X times lower than the highest point in the window (see [Min ratio of peak top/edge](#min-ratio-of-peak-topedge) parameter). When a local minumum is found, a set of user-defined intensity and peak duration requirements is checked. If they are fulfilled, the original overlapping peaks are split into new, distinct features.
:octicons-light-bulb-16: **Tip**. The LMR is particularly suitable for LC-MS data with little 
noise and nice peak shapes.

With the implementation of ion mobility (IM) support in MZmine 3, this module was expanded and can now be applied to both the RT and IM dimension (see [Resolving the ion mobility dimension](#resolving-the-ion-mobility-dimension)).

---
## **Parameters settings**
:material-menu-open: Feature detection → Chromatogram resolving → Local minimum resolver

![](local-minimum-resolver.png)

#### **Suffix**
String added as suffix to when creating the new feature list(s).

#### **Original feature list**
Keep or remove the processed feature list(s).

#### **MS/MS scan pairing**
Pair MS/MS fragmentation spectra collected in [DDA](../../terminology/general-terminology.md#data-dependent-acqusition-mode) mode to the resolved features. This is optional at this stage as the same can be done later in the pipeline using a separate [module](../featdet_ms2_scan_pairing/ms2_scan_pairing.md). See [MS2 scan pairing](../featdet_ms2_scan_pairing/ms2_scan_pairing.md) documentation for more details.

#### **Dimension**
Dimension to be resolved. Select _Retention time_ or _Mobility_ to run the module over the RT or IM dimension, respectively.

#### **Chromatographic threshold**
Percentage of data points in the EIC removed before local minima search. This represents an important filter for noisy chromatogram and significantly reduces the precessing time. 
The algorithm finds the intensity value (threshold) that leaves the specified percentage of data points in the EIC trace below XXX. All such data points are removed. For example, a _Chromatographic threshold_ = 50% will discard the lowest-intense 50% data points in the EIC trace.

:octicons-alert-16: It must be noted that the algorithm examines the EICs throughout the entire RT range (_i.e._ also the zero data points are considered). Therefore, we recommend to set this value rather high (_e.g._ 90-95%) and lower it only if needed.

:octicons-alert-16: Since [mobilograms](../../terminology/ion-mobility-terminology.md#mobilograms) contains less data points than regular LC traces, we recommend to lower this settings to no more than 80% when [resolving the ion mobility dimension](#resolving-the-ion-mobility-dimension).

#### **Minimum search range RT/Mobility (absolute)**
Size of the RT or mobility window examined for local minima search. An overly narrow search range can cause peak edges to be cut off, whereas a too wide search ranges might lead to an incomplete resolution of narrowly eluting peaks (see example below).
![](min-search-range-example.png)

:octicons-alert-16: RECOMMENDATION FOR IM 

#### **Minimum relative height**
Minimum relative intensity (respect to the highest data point in the EIC) a peak need to reach to be retained as a feature. This parameter can be used in combination with the [Minimum absolute height](#minimum-absolute-height)) setting as to filter the resolved features to be retained. Many users prefer to rely only on the _Minimum absolute height_ as it is more straightforward to set. To do so, set the _Minimum relative height = 0_ and the parameter will be ignored. 

:octicons-light-bulb-16: **Tip**. Modern mass spectrometers provides linear dynamic ranges up to 5 orders of magnitude. If we take an Orbitrap device with a detector saturation around 1.0E10 intensity, a _Minimum relative height_ = 0.001 would correspond to a 1.0E5 minimum intensity.

#### **Minimum absolute height**
Minimum absolute intensity a peak needs to reach to be retained as a feature. This paramter is very similar to the [Min highest intensity](../featdet_adap_chromatogram_builder/adap-chromatogram-builder.md#min-highest-intensity) settings in the ADAP chromatogram builder module and the same concepts apply.

:octicons-light-bulb-16: **Tip**. The same value used as [Min highest intensity](../featdet_adap_chromatogram_builder/adap-chromatogram-builder.md#min-highest-intensity) in the EICs building can normally be used here.

:octicons-alert-16: RECOMMENDATION FOR IM 

#### **Min ratio of peak top/edge**
Minimum ratio between the highest and lowest point of a peak. This mostly affects detection of low intensity and not-baseline-resolved signals and should be optimised using such a signal as an example.
:octicons-light-bulb-16: **Tip**. We recommend values between 1.7 (not baseline separated) and 2 to start the optimisation.

:octicons-alert-16: RECOMMENDATION FOR IM . Should beaised to XXX as the traces tend to be more jagged.

#### **Peak durantion range (min/mobility)**
Range of acceptable peak length expressed in minutes (RT dimension) or absolute units (mobility dimension). This parameter can be used to filter out noisy features based on their overly short (or long) duration.

#### **Min # of data points**
Minimum number of data points a resolved peak needs to have to be considered valid and retained as a feature. This parameter can be used alogn with the [Peak duration range](#peak-durantion-range-minmobility) setting as  peak duration constraint to filter out noisy features.

:octicons-light-bulb-16: **Tip**. This paramter is very similar to the [Min group size in # of scans](../featdet_adap_chromatogram_builder/adap-chromatogram-builder.md#min-group-size-in--of-scans) settings in the ADAP chromatogram builder module and the same value can normally be used here (usually, no less than 4-5).

:octicons-alert-16: RECOMMENDATION FOR IM 

#### **Show preview**
By checking this box, an interactive visualization panel will open to help the user to adjust the algorithm parameters. In two EIC traces can be dispalyed simoultaneously in two sub-panels.
- Explain difference between the two sub-panels

This will help the user to appreciate how the chosen settings will impact the resolution of noisy and "good" EIC traces, respecively.
The feature list and EIC traces to display can be selected from the corresponding drop-down menus.

## Resolving the ion mobility dimension
This same module can be used to resolve features co-eluting in the RT dimension, based on their ion mobility. The same concept applies as in resolution of the RT dimension; however, [mobilograms](../../terminology/ion-mobility-terminology.md#mobilograms) are examined instead of EIC traces. Therefore, few differences should be kept in mind:

1. Mobilograms contain less scans (_e.g._ ≈400-1000 per [frame](../../terminology/ion-mobility-terminology.md#accumulations-mobility-scans-and-frames), depending on instrument type and acquisition settings) compared to regular EICs (_e.g._ ≈4500 scans for 15 minutes LC run and scan rate of 0.2 seconds). Therefore, a lower [chromatographic threshold](#chromatographic-threshold) (_e.g._ 80%) is recommended to avoid relevant data points in the mobilogram being discarded.

2. Different vendors use different unit of mobility. For instance, [TIMS](../../terminology/ion-mobility-terminology.md#trapped-ion-mobility-spectrometry-tims) express ions' mobility as XXX, whereas [time dispersive IM devices](../../terminology/ion-mobility-terminology.md#time-dispersve-ion-mobility-spectrometry-dtims-and-twims) (DTIMS and TWIMS) use the ions' drift time (expressed milliseconds). TIMS values are numerically smaller (_e.g._ 0.01) than DTIMS or TWIMS; therefore, a lower [minimum search range](#minimum-search-range-rtmobility-absolute) should be used for the local minima search.  


3. Raw data are used. Resolved mobilograms are recalculated from the raw data and any applied smoothing(LINK)
- Mobiligrams tend to be more jagged (see Figure). As a consequence, some parameters, such as [Minimum absolute height](#minimum-absolute-height), or [Minimum absolute height](#min--of-data-points), and [Min ratio of peak top/edge](#min-ratio-of-peak-topedge) should be adjusted respec to wha normally used in the resolution of the RT dimension.
- Smoothing must be reapplied, if needed.

SCREENSHOT OF IM DIMENSION

![](mobilityresolving.png)




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