# Supported formats

* Vendor formats:
*
    * .tdf (Native Bruker LC-IMS-MS and MALDI-IMS-MSI format)
*
    * .tsf (Native Bruker MALDI-IMS-MS (single shot) format)
* .mzML
*
    * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native Bruker
      data
*
    * Created via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native Waters
      data

**Note**: mzML via MSConvert from Agilent raw data can be imported, but certain restrictions might
hinder processsing workflows due to the nature of the raw data format.


***

# Background information and terminology

Since ion mobility spectrometry (IMS) resolved data is more complex due to the additional dimension
when compared to regular LC-MS data, some terms shall be clarified before going into details of the
processing steps.

## Mobility separation and data format

Ion mobility separation usually occurs on the millisecond timescale, fitting nicely in-between
liquid chromatography (LC) (few seconds per chromatographic peak) and mass spectra acquisition of
TOF instruments (several micro seconds). Therefore, the mobility dimension can be resolved by
acquiring multiple spectra during a mobility separation (e.g. 1000 spectra per 100 ms). This leads
to multiple mass spectra acquired at one IMS accumulation. Thus, at one retention time, multiple
spectra are acquired. A detailed comparison of LC-MS and LC-IMS-MS raw data can be
found [here](#graphical-comparison-of-lc-ms-and-lc-ims-ms-data).

## Frames and Mobility Scans

During one IMS accumulation and separation, multiple mass spectra are acquired to resolve the
mobility dimension. All mass spectra acquired during one mobility separation are termed "_mobility
scans_" in MZmine. The agglomerate of all mobility scans for one IMS accumulation are called
"_frame_". All _mobility scans_ of a single _frame_ can be summed, to represent a single mass
spectrum as in classic LC-MS.

## Mobilograms

A "_mobilogram_" represents the intensity of an m/z or m/z range along the mobility axis. A
_mobilogram_ may be build from multiple frames and summed or built from a single frame.

![mobilogram](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/mobilogram.png)

## Ion mobility traces

An "_ion mobility trace_" basically represents a mobility resolved extracted ion chromatogram (EIC).

![trace](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/trace.png)

***

# Raw data processing

## Raw data import

As any other data format, ion mobility data can be imported via the main menu **Raw data methods →
Raw data import**. Note that multiple .tdf data folders can be dropped into the
**MS data (advanced)** dialog. The Bruker TDF import can only select a single folder. When using
the **MS data (advanced)** dialog, inexperienced users should deactivate the direct mass detection
steps, since they alter the raw data on the import. Mass detection is then performend, when the
scans are loaded and only peaks above the noise level are imported.

Alternatively, you can simply drag & drop the raw data into the raw data list of the main window.

![grafik](https://user-images.githubusercontent.com/37407705/136391336-5722d04c-91c0-4c77-88db-00325e8ff41b.png) ![grafik](https://user-images.githubusercontent.com/37407705/136391465-c61eece6-0720-459f-8b2b-511021d7a058.png)

## Mass detection

The mass detection steps perform noise filtering (by a threshold) and centroiding of profile raw
data. Native Bruker raw data is already centroided, therefore the centroid mass detector should be
used. Waters .mzML raw data might come as profile data, which requires a different mass detector
such as **exact mass**.

The mass detection is launched via **Raw data methods → Mass detection → Mass detection** ([1] in
the figure). In the dropdown menu [2], an applicable mass detector should be chosen and configured
via the **Setup** button [2]. By selecting the _Show preview_ checkbox, a scan can be selected to
adjust the noise level. Note that a mobility scan should be selected to determine the noise level.
However, the same noise level will be applied to frames, too.

The output of the mass detection step, can be referred to as **mass list**, since it will only
contain a list of selected m/z values.

![Mass detection](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/massdetection.png)

### Setting the noise level

Choose the noise level to detect (= red dot) actual peaks but filter out detector noise. The
detector noise is usually determined by a lot of signals of the same intensity.

## Mobility scan merging

If a .mzML file is imported, the merged frame spectrum must be created via the **File merging →
Mobility scan merging** module. This is required to gain access to MZmine's regular LC-MS
functionality. This step uses the centroided and thresholded data produced by
the [mass detection](#Mass-detection)
step.

**This step is not required when importing native Bruker .tdf or .tsf data from .d folders.**
When importing native Bruker data, a merged spectrum for the frame is created automatically by the
vendor library.

# Feature detection workflows

Ion mobility data can be processed in MZmine 3 in two ways. The first few steps are different for
the two workflows.

1. LC-IMS-MS workflow via **Ion mobility trace builder / Recursive IMS builder**
    - directly build ion mobility traces (rt and mobility dimension)
    - smoothing (optional)
    - resolve retention time dimension
    - smoothing (optional)
    - resolve mobility dimension
    - smoothing (optional)
2. Regular LC-MS workflow via **ADAP Chromatogram builder and IMS expander**
    - build extracted ion chromatograms (rt dimension) from frame spectra
        - requires merged frame spectra (see [mobility scan merging](#Mobility-scan-merging))
    - smoothing (optional)
    - resolve retention time dimension
    - expand features into mobility dimension
    - smoothing (optional)
    - resolve mobility dimension
    - smoothing (optional)

While these lists might seem fairly similar, there are some differences in the processing approach.
The LC-IMS-MS workflow builds ion mobility traces from the data in the mobility scans, whilst the
LC-MS workflow builds EICs from the summed frames. Imagine setting the noise level to 200 and occurs
in 15 mobility scans with an intensity of 180 and in 20 with > 200, but the ion mobility trace
builder required at least 25 data points. At the same time, the ADAP chromatogram builder was set to
a minimum highest intensity of 1000 in a frame, which might have been reached due to summed
intensities.  
Since intensities are summed to build frames, the LC-MS workflow can be more sensitive to less
abundant compounds whilst the LC-IMS-MS workflow will directly detect ion mobility traces and be
less susceptible to noise. For .mzML data, this might not make a significant impact, because the
frame is built from the thresholded mass list. This means that the main impact on sensitivity for
low intense compounds is made by the user's noise level selection. However, for native Bruker raw
data, the summed frame is automatically built via the functionality of the vendor library without
the user's influence. Therefore, the more low abundant compounds might be detected, if the LC-MS
workflow is chosen.

## LC-IMS-MS workflow

The LC-IMS-MS workflow will directly build [ion mobility traces](#Ion-mobility-traces) from the raw
data in the mobility scans. This workflow does not necessarily require summed frame spectra.
However, if extracted ion chromatograms shall be visualized via
the [Chromatogram visualizer](Raw-data-visualisation.md#Chromatogram-plot), the frame intensities
are used. In case these are not present, the chromatograms will be blank. Note that feature
intensities from the LC-IMS-MS workflow might not exactly match the frame chromatograms due to
summing being executed prior to thresholding (for native Bruker data). Furthermore, multiple isomers
might hide behind a single chromatographic peak.

### Ion mobility trace builder

The **Ion mobility trace builder** will build [ion mobility traces](#Ion-mobility-traces) from the
raw data. Alternatively, the **Recursive IMS builder** can be used, which requires less ram but
takes longer.

The **Ion mobility trace builder** is found under **Feature detection → LC-IMS-MS → Ion mobility
trace builder**.

![imstracebuilder-dialog](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/imstracebuilderdialog.png)

#### Scan selection

The scan selection parameter specifies the scans that shall be processed for feature detection.
Usually, setting the ms level to 1 is sufficient. If a calibration segment is present, it can be cut
out via the retention time filter in the scan selection.

#### m/z tolerance

The **m/z tolerance** specifies the scan-to-scan tolerance for ion mobility traces. This tolerance
window may need to be set higher that for classic LC-MS feature detection (e.g. to 0.005 m/z and
15-20 ppm instead of 10 ppm) due to lower intensities therefore less accuracy in individual mobility
scans compared to LC-MS scans. Note that the overall accuracy is achieved via LC-IMS-MS is the same
due to the higher number of scans.

#### Minimum consecutive retention time data points

This parameter specifies the number of consecutive detections of the same m/z value in a
chromatographic peak (rt dimension only). This means that a single m/z has to be detected in, e.g, 5
frames with an intensity higher than zero. This parameter helps to filter noise. Consecutive
detections in the mobility dimension do not affect this parameter. Usually no less than 5 should be
set here if the MS1 acquisition rate is sufficient.

#### Minimum total signals

Specifies the total number of peaks in the mobility dimension in all mobility scans. Every "dot" in
an ion mobility trace represents a single datapoint. (
see [ion mobility traces](#Ion mobility traces))

#### Advanced parameters

For most applications, these parameters do not need to set/altered. For high mobility resolved data
the mobilograms might become noisy due to less ions reaching the detector at the same time. By
default, the number of binned scans is set to cover about 0.0008 Vs/cm^2 per bin. The effect of
binning can be
seen [here](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/binnedmobilogram.png)
. If you are unsure about the nature of your data, you can perform trace building with the standard
parameters and apply/preview the binning afterwards via the **Feature detection → Mobilogram
binning** module.

#### Processing result

After performing ion mobiltiy trace detection, a feature list is created in the feature list tab
(see [feature lists tab](Main-window-overview.md#ms-data-files-and-feature-lists-tab)). In the
feature table, multiple columns are created. The displayed columns can be set via the button on the
right of the feature table ([1]).

![featuretable](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/featuretable.png)

The **shapes** displays an EIC of the ion mobility trace (intensities summed in rt dimension). The
**mobilograms** column shows a mobilogram for the ion mobility trace (intensities summed in mobility
dimension). The shapes and projections can be smoothed and resolved. However, the ion mobility trace
is always represented by the raw data and remains unaltered. After resolving, the shapes and
mobilograms have to be recalculated from the raw data, which is why the smoothing is lost after
resolving.

### Smoothing in retention time dimension (optional)

The necessity of smoothing in RT dimension is determined by the noisiness of chromatographic peaks.
These can be influenced by the overall spray stability, instrument accumulation times, transfer
efficiency and many more.

The number of data points to be smoothed in rt dimension can be set at [1]. Note that the correct
preview dimension is selected at [2].

For large batch modes, the **Remove original feature list** parameter should be selected. While
parameters are being optimised, this is not recommended, because removing a feature list cannot be
undone.

![](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/smoothingdialog.png)

### Resolving in retention time dimension

Here, the **Feature detection → Resolving → Local minimum resolver** is used. However, the **ADAP
resolver** also produces great results, but takes longer to process.

Resolving traces/chromatograms into individual features, is one of the most crucial steps of data
processing. Well optimised parameters [1] can lead to recognition of all good features in a "good"
EICs [2] and to few noise recognised as feature in EIC that also contains chromatographic noise
[3].  
On the other hand, poorly optimised parameters [4] can still lead to recognition of all features in
a good EIC [5], but recognise a lot of noise as feature in a noisy EIC [6].  
Therefore, we recommend optimising the parameters on good EICs and checking the results of these
parameters with a noisy EIC. Most of the time, a noisy EIC can be found by sorting the feature table
by decreasing area.

![](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/chromatogramresolving.png)

#### MS/MS scan paring

Selecting this parameter will pair DDA MS/MS spectra to the resolved features. This is optional at
this stage, because it will be executed again during resolving in the mobility dimension.

#### Dimension

The dimension to be resolved can be selected here. Select _Retention time_ for now.

#### Chromatographic threshold

This parameter is crucial for removing noise from chromatograms. If this parameter is set to, e.g.,
50, the lowest 50 % of intensities will be removed. Since the _all_ retention time in the data file
are used for this determination, this value should be rather high (e.g., 95 %) to begin with and
only lowered if necessary.

#### Search minimum rt range (min)

Determines the step size that will be scanned for individual peaks. Setting this value too low, can
cause peak edges to be cut off, setting it too high might lead to incomplete separation of narrowly
eluting compounds.

#### Minimum relative height

Determines the minimum relative intensity of a individual feature in relation to the highest
intensity in the chromatogram. May lead to discrimination of low intensity features.

#### Minimum absolute height

Determines the minimum absolute intensity of a feature to be recognised by the algorithm. This
parameter depends on what you want to detect, the instrument and detector type. Usually, Orbitrap
instruments report higher intensities that TOF instruments. However, the noise level is also higher
for Orbitrap than for TOF instruments. For TOF instruments 1E3 or even 5E2 can be appropriate,
whilst Orbitraps can require 1E5 or 5E4.

#### Min ration of peak top/edge

Describes the minimum ratio of the highest point of a peak to the lowest point of a peak. This
mostly affects detection of low intensity and not-baseline-resolved signals and should be optimised
using such a signal as an example.

#### Peak duration range

Describes valid peak lengths. Can be used to filter out very short or long noise signals.

#### Minimum number of data points

Can be used in addition to **Peak duration range** to filter out noise. Should be set no lower than
5 in most cases.

### Smoothing  in mobility dimension (optional)

After resolving a feature in RT dimension, the mobilograms will be recalculated from the from the
raw data (the resolved ion mobility trace). Therefore, a smoothing step is necessary if the data
requires it. The smoothing dialog is opened via **Feature detection → Smoothing**

Select to smooth the mobility dimension [1] and select it as preview dimension [2]. The filter with
depends on the number of spectra acquired in the observed mobility range. Usually, a value between 5
and 15 should be appropriate.

![](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/mobilitysmoothing.png)

### Resolving in mobility dimension

In general, the same principles apply as in the retention time resolving step. However, a few
differences shall be noted. In the screenshot you can also see, that the resolved mobilograms are
recalculated from the raw data and previously apply smoothing steps are therefore lost and must be
reapplied if necessary.

![](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/mobilityresolving.png)

#### Dimension

Mobility has to be selected as a dimension to resolve mobilograms [1].

#### Chromatographic threshold

Since there are less scans in mobility dimension (e.g., 400 - >1000 per frame, depending on the
instrument type and setting) than in rt dimension (e.g. 5000 for LC-MS depending on acquisition
rate), the threshold should be lowered to 80 or less.

#### Search minimum range

This value determines the search range in mobility dimension. Therefore, this value has to be set
lower when resolving a TIMS (Bruker data) mobilogram, because the absolute numerical values are
smaller (e.g., 0.01). When resolving mobilograms from Waters or Agilent data (mobility as drift time
in ms), the values are higher and must therefore be increased.

Other parameters such as minimum intensities or minimum number of data points should be adjusted
depending on what you want to detect.

### Smoothing in rt and mobility dimension (optional)

Some recognised features might have rather noisy signals (in rt and mobility dimension) after the
mobility resolving step. If smoother shapes are required, the smoothing can be reapplied afterwards.
In that case, smoothing can be applied to both dimensions at once.

## LC-MS workflow

LC-IMS-MS data can also be processed via the regular LC-MS modules. If necessary, detected features
can be expanded into the mobility dimension.

For this workflow, generation of summed frame spectra via
the [Mobility scan merging](#mobility-scan-merging) module is a mandatory step, if the data was
imported from an .mzML file (automatically generated via native Bruker import).

## ADAP chromatogram builder



# Graphical comparison of LC-MS and LC-IMS-MS data

Classic LC-MS data consists of three dimensions: m/z, intensity, and retention time. At every
retention time, a whole mass spectrum is acquired (yellow). Putting all scans together creates a
three-dimensional plane. By slicing the three-dimensional data at a single m/z (+- a tolerance),
EICs can be created (green).

![lcimsmsdata](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/lcmsdataformat.png)

On the other hand, ion mobility resolved data consists of a three-dimensional data plane at each
retention time. The three dimensions being m/z, intentsity, and mobility (as drift time (ms) or
inverse reduced mobility 1/k0 [Vs/(cm^2)]). The 3D projection of regular LC-MS data can be created
by summing all mobility scans of a frame to create a frame spectrum.
(see [Mobility scan merging](#mobility-scan-merging))
![lcimsmsdata](https://raw.githubusercontent.com/mzmine/mzmine_documentation/master/images/imsworkflow/lcimsmsdataformat.png)

