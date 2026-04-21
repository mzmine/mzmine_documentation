# **Standard compound normalizer**

## **Description**

!!! info

    The internal standard normalizer is now part of the [**Intensity normalizer**](../norm_intensity/norm_intensity.md) to apply all normalization steps in a sequence. 

Applies an internal standard compound correction to each feature individually, accounting for
extraction efficiency and matrix effects within a sample. Internal standard features must be present
in the detected samples. User can select one or multiple
internal standard features, which must be present in all raw data files. Then feature height (and
area) of
each feature is normalized by either the **nearest standard** or a **weighted contribution** of all
standards.

In case a weighted contribution is used, the contributions of all standards are weighted by
distance. The distance of the standard feature to the feature being normalized is calculated as

$$distance = MZvsRT_{Balance} * MZ_{difference} + RT_{difference}$$

where $MZvsRT_{Balance}$ is a multiplier of m/z difference set by **m/z vs RT balance** parameter

:warning: Feature lists must be aligned prior to normalization.

## **Parameters**

#### Standard compounds

List of features to use as internal standards. Each selected feature provides a reference point
at its (m/z, RT) position for correction.

#### Normalization type

How the correction factor is derived from the available internal standards:

- **Nearest**: uses the single IS compound with the shortest distance (in m/z–RT space) to the
  feature being normalized.
- **Weighted**: uses a distance-weighted average over all IS compounds; features that are
  very close to a standard (distance = 0) are averaged directly.

#### m/z vs RT balance

Multiplier applied to the m/z difference when computing the distance between a feature and an
internal standard. Increase this value to weight m/z similarity more heavily relative to RT
similarity.

#### Reference samples

Sample types whose IS signal is used to build the correction model. Non-reference samples are
corrected by interpolating between the nearest reference samples in acquisition order. It is best to
add the same internal standards to all samples, but this option allows using internal standards
from standard injections like QCs to interpolate changes to other samples.

#### Require all standards

When enabled, normalization fails if any selected IS compound is missing from a raw file.
Disable to proceed with available standards when some may be absent in certain samples.

{{ git_page_authors }}
