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

![Mass detection](../../wf_featuredetection/lcmsworkflow/massdetection.png)

#### Setting the noise level

Choose the noise level to detect (= red dot) actual peaks but filter out detector noise. The
detector noise is usually determined by a lot of signals of the same intensity.

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
