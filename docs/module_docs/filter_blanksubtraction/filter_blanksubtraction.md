# Feature list blank subtraction

:material-menu-open: **Feature list methods → Feature list filtering → Feature list blank subtraction**

Feature list blank subtraction removes background features from an aligned feature list by
comparing sample abundances with abundances measured in procedural blanks or controls. The result
contains only non-blank raw data files. Optionally, the module can create a second feature list with
the removed background features for inspection and workflow optimization.

!!! warning

    Run this module on an aligned feature list that contains both the selected blank/control files
    and the sample files. The task stops with an error if a selected blank file is not part of the
    input feature list.

By default, blank files are selected from the `mzmine_sample_type` metadata column where the value
is `blank`. The selection can be changed in the module dialog.

## Parameters

#### Aligned feature list

Selects the single aligned feature list to filter. It must contain every blank/control raw data file
selected below as well as the sample files to compare against the blanks.

#### Blank/Control raw data files

Selects the files treated as blanks. The default metadata-based selection uses files whose
`mzmine_sample_type` value is `blank`. At least one file must be selected.

#### Minimum # of detection in blanks

Sets the minimum number of selected blank files in which a row must have a detected feature before
blank subtraction is applied. The default is `1`. Rows with fewer blank detections are retained.

#### Abundance measure

Selects the feature abundance used for all comparisons. The available choices are **Height**,
**Area**, **Normalized height**, and **Normalized area**. The default is **Height**. The normalized
choices use the corresponding normalized abundance stored on each feature. A missing or non-finite
value for the selected measure is treated as zero.

#### Blank abundance ratio type

Defines the reference blank abundance for each row:

- **MAXIMUM** uses the highest abundance among the detected blank features. This is the default and
  the more conservative option.
- **AVERAGE** uses the mean abundance of the detected blank features. Missing blank features are not
  included as zeros in this mean.

#### Fold change increase _(Optional)_

Sets the minimum sample-to-blank abundance ratio required to retain a sample feature or row. The
displayed percentage acts as a multiplier: `300%` requires a sample abundance of at least three
times the reference blank abundance. The configured value is `300%` by default, but this option is
disabled by default; while disabled, the module applies `100%` (a ratio of `1`). Values equal to the
threshold are retained.

#### Check abundance of

Controls whether the threshold is applied to a complete row or to each sample feature:

- **Most abundant feature (keep/remove whole row)** compares the most abundant sample feature with
  the reference blank abundance. If it passes, all sample features in the row are retained;
  otherwise, all are removed. This is the default and is generally preferable for subsequent
  statistical analysis.
- **Each feature (keep/remove individual feature)** compares every sample feature separately. A row
  can therefore retain high-abundance sample features while losing lower-abundance ones. This can
  help inspect which samples exceed the blank, but may distort downstream statistical analysis.

#### Create secondary list of subtracted features

Creates an additional feature list with the suffix `subtractedBackground`. It contains rows in
which at least one sample feature was removed, including the corresponding blank features and the
removed sample features. A **Blank subtraction** annotation summarizes why each row was classified
as background. This option is disabled by default. The secondary list is excluded from the batch
mode **last feature list** selection so that subsequent steps continue with the filtered result.

#### Suffix

Sets the suffix of the filtered feature list. The default is `subtracted`.

#### Original feature list

Controls whether the original aligned feature list is kept or removed after processing. The default
is **KEEP**. Choosing **REMOVE** saves memory; the filtered result remains in the project.

---

## Algorithm {#algorithm}

For each row, the module separates detected features into blanks and non-blank samples. A row is
kept without applying the abundance threshold when it has fewer than the required blank detections
or when its reference blank abundance is zero. Otherwise, it calculates the threshold as:

\[
\text{threshold} = \text{blank abundance} \times \text{fold-change ratio}
\]

The selected **Check abundance of** mode then compares either the highest sample abundance or every
sample feature abundance with this threshold. Sample features that meet or exceed the threshold are
retained. Blank features are always omitted from the primary filtered result.

---

{{ git_page_authors }}
