# Local Minimum Resolver

Resolving traces/chromatograms into individual features, is one of the most **crucial** steps of data
processing. Well optimised parameters [1] can lead to recognition of all good features in a "good"
EICs [2] and to few noise recognised as feature in EIC that also contains chromatographic noise
[3].
On the other hand, poorly optimised parameters [4] can still lead to recognition of all features in
a good EIC [5], but recognise a lot of noise as feature in a noisy EIC [6].  
Therefore, we recommend optimising the parameters on good EICs and checking the results of these
parameters with a noisy EIC. Most of the time, a noisy EIC can be found by sorting the feature table
by decreasing area.

![](../img/imsworkflow/chromatogramresolving.png)

### Parameter settings

##### MS/MS scan paring

Selecting this parameter will pair DDA MS/MS spectra to the resolved features. This is optional at
this stage, because it will be executed again during resolving in the mobility dimension.

##### Dimension

The dimension to be resolved can be selected here. Select _Retention time_.

##### Chromatographic threshold

This parameter is crucial for removing noise from chromatograms. If this parameter is set to, e.g.,
50, the lowest 50 % of intensities will be removed. Since the _all_ retention time in the data file
are used for this determination, this value should be rather high (e.g., 95 %) to begin with and
only lowered if necessary.

##### Search minimum rt range (min)

Determines the step size that will be scanned for individual peaks. Setting this value too low, can
cause peak edges to be cut off, setting it too high might lead to incomplete separation of narrowly
eluting compounds.

##### Minimum relative height

Determines the minimum relative intensity of a individual feature in relation to the highest
intensity in the chromatogram. May lead to discrimination of low intensity features.

##### Minimum absolute height

Determines the minimum absolute intensity of a feature to be recognised by the algorithm. This
parameter depends on what you want to detect, the instrument and detector type. Usually, Orbitrap
instruments report higher intensities that TOF instruments. However, the noise level is also higher
for Orbitrap than for TOF instruments. For TOF instruments 1E3 or even 5E2 can be appropriate,
whilst Orbitraps can require 1E5 or 5E4.

##### Min ration of peak top/edge

Describes the minimum ratio of the highest point of a peak to the lowest point of a peak. This
mostly affects detection of low intensity and not-baseline-resolved signals and should be optimised
using such a signal as an example.

##### Peak duration range

Describes valid peak lengths. Can be used to filter out very short or long noise signals.

##### Minimum number of data points

Can be used in addition to **Peak duration range** to filter out noise. Should be set no lower than
5 in most cases.


## Ion mobility data

In general, the same principles apply as in the retention time resolving step. However, a few
differences shall be noted. In the screenshot you can also see, that the resolved mobilograms are
recalculated from the raw data and previously apply smoothing steps are therefore lost and must be
reapplied if necessary.

![](../img/imsworkflow/mobilityresolving.png)

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
