# Mass detection

## LC-MS data

The mass detection steps perform noise filtering (by a threshold) and centroiding of profile raw
data. The raw data format can either be centroided or in profile mode. If the data is centroided,
the **centroid** mass detector can be used. Profile data requires a different mass detector such as
**exact mass**.

The mass detection is launched via **Raw data methods → Mass detection → Mass detection** ([1] in
the figure). In the dropdown menu [2], an applicable mass detector should be chosen and configured
via the **Setup** button [2]. By selecting the _Show preview_ checkbox, a scan can be selected to
adjust the noise level.

The output of the mass detection step, can be referred to as **mass list**, since it will only
contain a list of selected m/z values.

![Mass detection](massdetection.png)

#### Setting the noise level

Choose the noise level to detect (= red dot) actual peaks but filter out detector noise. The
detector noise is usually determined by a lot of signals of the same intensity.

#### Detect isotope signals below noise level

**Centroid** and **exact mass** detectors provide an additional parameter called **detect isotope signals below noise level**. This option allows to include additional peaks, corresponding to isotope masses, in the resulting mass list. By clicking the **Setup** button, you can specify the following parameters.

##### Chemical elements

Chemical elements which isotopes will be considered (select from the periodic table).

##### M/z tolerance

The maximum allowed difference between theoretical isotope m/z and measured m/z present in the scan to be considered the same.

##### Maximum charge of isotope m/z

Should be a positive integer (further denoted as K). All peaks having m/z equal to (up to m/z tolerance) theoretical isotope mass (any isotope of any specified chemical element) divided by any of 1, 2, ..., K will be included in the mass list. The default value is 1.

## LC-IMS-MS data

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

![Mass detection](massdetection.png)

#### Setting the noise level

Choose the noise level to detect (= red dot) actual peaks but filter out detector noise. The
detector noise is usually determined by a lot of signals of the same intensity.
