# Intensity normalizer

:material-menu-open: **Feature list methods → Normalization → Intensity normalizer**

The Intensity Normalizer corrects feature abundances (height or area) through a configurable
multi-step normalization pipeline. Up to three correction steps are applied in sequence, each
optional:

1. **Metadata-based pre-normalization**: divides or multiplies each sample's intensities by a
   numeric metadata value such as sample weight, dilution factor, or injection volume.
2. **Internal standard correction**: corrects each feature individually by the nearest or
   distance-weighted internal standard compound, accounting for extraction efficiency and matrix
   effects.
3. **Inter-sample correction**: removes signal drift within an analytical batch using reference
   samples (e.g., pooled QCs). Two kinds of methods are available:
    - **Sample-wide methods** (*By feature abundances*, *Spectral TIC*) compute one factor per
      sample and, when multiple batches are present, align batch medians to a global reference
      median.
    - **Feature specific QC drift correction (QC-RLSC)** fits a separate
      drift curve for every feature in every batch, so that each feature gets its own correction
      factor per sample. Batches are aligned in the same step.

Normalized values are written to dedicated **Normalized Height** and **Normalized Area** columns
and the normalization functions are stored with the feature list so that they can be automatically
re-applied to features added later (gap filling, manual integration). Processing steps that change
feature intensities or row identities drop or adapt the stored normalization, see
[When the normalization is dropped](#dropped).

## Recommended citations

!!! info

    When using the **Feature specific QC drift correction (QC-RLSC)**, please consider citing:<br>
    Dunn W.B., Broadhurst D., Begley P., et al. Procedures for large-scale metabolic profiling of serum and plasma using gas chromatography and liquid chromatography coupled to mass spectrometry. Nature Protocols 6, 1060–1083 (2011), doi:10.1038/nprot.2011.335.

---

## Parameters

#### Feature lists

Feature lists to normalize.

#### Name suffix

String appended to the output feature list name (default: `norm`).

#### Original feature list

Controls whether the original feature list is kept, removed, or modified in-place after
normalization.

#### Feature measurement type

Whether feature height or feature area is used as the abundance measure throughout all
normalization calculations. The resulting factors are applied to both the normalized height and
the normalized area.

---

#### Batch correction metadata column _(Optional)_

Metadata column whose values identify the analytical batch a sample belongs to (e.g.,
`Batch`). When enabled, the normalization pipeline is run independently per batch:

- Steps 2 and 3 are applied within each batch using only that batch's reference samples.
- For the sample-wide step 3 methods, a final **inter-batch normalization** aligns the median
  reference-sample signal of every batch to the global median, correcting for between-run
  differences.
- For the **Feature specific QC drift correction**, each feature is fitted within each batch and all batches are
  rescaled to one common target per feature, which aligns the batches in the same step. No
  separate inter-batch step is applied (see [Feature specific QC drift correction](#qc-rlsc)).

Without a batch ID column, all samples are treated as one continuous sequence.

!!! tip

    Use this parameter whenever samples were acquired in multiple separate analytical runs with
    their own QC injections to avoid over-correcting within a run while still aligning runs to each
    other.

---

#### Metadata normalization column: Step 1 _(Optional)_

Selects a numeric sample metadata column whose value is used to pre-normalize each sample before any
other correction. Only a single column, a single value per sample can be used. Typical uses:

| Example column        | Operation | Effect                         |
|-----------------------|-----------|--------------------------------|
| Sample weight (mg)    | Divide    | Normalizes to per-mg intensity |
| Injection volume (µL) | Divide    | Normalizes to per-µL intensity |
| Dilution factor       | Multiply  | Corrects for sample dilution   |

Set a sample's metadata value to `0` to skip normalization for that sample.

Choose **divide** or **multiply** depending on whether the metadata column represents a quantity
to scale down by (e.g., weight) or scale up by (e.g., dilution factor).

---

#### Intra-sample correction: Step 2 _(Optional)_

Applies an internal standard compound correction to each feature individually, accounting for
extraction efficiency and matrix effects within a sample. This step runs after step 1 (metadata
normalization).

Available options:

- **No normalization**: step 2 is skipped.
- **Internal standard compounds**: loads internal standards from a CSV/TSV file, matches them to
  feature-list rows by m/z, RT, and optional mobility, then normalizes each feature by the nearest
  or weighted standard. This workflow is described in more detail
  [**here**](../norm_stand_cmpd/norm_stand_cmpd.md).

#### Inter-sample correction: Step 3

Corrects signal drift across samples using a set of reference injections (typically pooled QCs) or
all samples.
This step runs after metadata normalization (step 1) and internal standard correction (step 2).
For the sample-wide methods, intra-batch correction is applied first; if multiple batches are
defined, inter-batch alignment is performed afterward by centering the median batch reference
abundance against a global median.

Available options:

- **No normalization**: step 3 is skipped.
- **By feature abundances**: one factor per sample from a summary of all feature abundances. See
  sub-parameters below.
- **Spectral TIC**: one factor per sample from the total ion current of the mass lists. See
  sub-parameters below.
- **Feature specific QC drift correction (QC-RLSC)**: one factor per feature and sample from a QC
  drift curve fitted per feature. See sub-parameters below.

##### By feature abundances sub-parameters

###### Reference samples

Sample types, as defined in the sample metadata in column _mzmine_sample_type_, used as the
normalization reference (default: QC). Non-reference samples are
normalized by interpolating correction factors between the nearest reference samples in
acquisition order.

###### Normalize by feature abundances

Statistic used to summarize the feature intensity distribution of each sample:

| Mode             | Description                                          |
|------------------|------------------------------------------------------|
| Median (default) | Median of all feature abundances: robust to outliers |
| Sum (TIC)        | Sum of all feature abundances                        |
| Average          | Mean of all feature abundances                       |
| Max              | Maximum feature abundance                            |

The correction factor for each sample is:
`median across all references / specific reference metric`.

##### Spectral TIC sub-parameters

###### Reference samples

Sample types, as defined in the sample metadata in column _mzmine_sample_type_, used as the
normalization reference (default: QC). Non-reference samples are
normalized by interpolating correction factors between the nearest reference samples in
acquisition order. The distance is defined by the run date in the sample metadata or as read from
raw data file metadata.

The correction factor is: `median TIC across all references / specific sample TIC`, where TIC is computed from
mass lists (noise-filtered spectra).

!!! warning

    Spectral TIC is sensitive to noise and baseline signal. Prefer **By feature abundances** when
    the feature list has already been filtered, as it is more robust.

##### Feature specific QC drift correction (QC-RLSC) sub-parameters

Fits the drift of every feature in every batch on its pooled QC injections with robust LOESS
smoothing and corrects all samples of that batch by the fitted curve (QC-RLSC). The algorithm is
described in [Feature specific QC drift correction](#qc-rlsc).

!!! warning "Prerequisites"

    - Every raw data file needs an acquisition timestamp (run date) in the sample metadata or in
      the raw data file metadata. Two samples of the same batch must not share the same timestamp.
    - Each batch needs at least five usable QC injections per feature (see **Minimum usable QCs**).
    - The **Feature measurement type** must be raw **Height** or **Area**.

###### Reference samples

Sample types, as defined in the sample metadata in column _mzmine_sample_type_, used to fit the
drift of each feature (default: QC). Select comparable pooled QC samples only.

!!! tip "Conditioning QCs"

    Dunn et al. exclude the first QC injections of each batch (three for GC-MS, eight for UPLC-MS)
    that condition the system. Assign these injections a different sample type than the reference
    samples, or remove them from the feature list, so that they are not used for fitting.

###### Smoothing

Selects how the drift curve of each feature and batch is smoothed:

- **QC-RLSC** (default): selects the LOESS bandwidth (neighborhood size) and the polynomial degree
  (linear or quadratic) separately for each feature and batch by leave-one-out cross-validation on
  the QC injections, as described by Dunn et al. No parameters. Uses two robustness iterations.
- **Manual LOESS**: uses the same bandwidth, polynomial degree, and robustness iterations for all
  features and batches. No cross-validation.

**Manual LOESS** parameters:

- **LOESS bandwidth** (default `0.75`): fraction of the usable QCs of a batch that form each local
  fit, rounded up to a whole number of neighbors. At least *polynomial degree + 2* neighbors are
  needed, otherwise the fit of this feature in this batch fails. Larger values give smoother
  curves.
- **Polynomial degree** (default `1`): `1` for local linear, `2` for local quadratic fitting.
- **Robustness iterations** (default `2`): number of robust reweighting iterations of the LOESS
  fit. Each iteration down-weights QC injections with large residuals (bisquare weights), which
  limits the influence of single outlier QCs. `0` disables the robust reweighting.

###### Minimum usable QCs

Default: `5`, minimum `5`. Minimum number of usable QC observations (positive, finite abundance)
of a feature in a batch. Batches with fewer usable QCs are not corrected for this feature.

###### Maximum correction factor

Default: `10`. Largest allowed change of a feature's value, up or down: with `10`, values may be
multiplied by up to 10 or divided by up to 10 (factors between `0.1` and `10`). If any sample of a
batch would need a larger correction, the feature gets no normalized values in that batch. The
factor is never capped. The factors include both the drift within the batch and the offset of the
batch from the common target.

Very large factors usually indicate an unreliable fit, e.g., a feature close to the noise level in
the QCs or a curve that drops close to zero between QCs. This limit is an mzmine safeguard and not
part of QC-RLSC by Dunn et al., who instead remove features with a high QC RSD after correction.

###### Global missing QC fraction

Default: `0.5`. A feature is not corrected in any batch if the fraction of QC injections (across
all batches) in which it has no usable abundance exceeds this value. Independently of this
setting, a feature is not corrected in a batch where more than 50% of the QCs are missing.

!!! tip

    Run the Feature specific QC drift correction after gap filling. The QC drift curves are calculated once from the
    abundances present at that time. Features added later by gap filling or manual integration get
    the stored factor of their row and sample, but the curves are not refitted.

---

## Algorithm {#algorithm}

### Normalization pipeline

The three correction steps are always applied in the following order. Each step is independent
and optional; any combination can be enabled:

| Step | Parameter                                          | Scope                                   |
|------|----------------------------------------------------|-----------------------------------------|
| 1    | Metadata normalization column                      | Per sample (constant factor)            |
| 2    | Intra-sample correction                            | Per feature, per sample                 |
| 3    | Inter-sample correction: sample-wide methods       | Per sample (interpolated)               |
| 3    | Inter-sample correction: Feature specific QC drift correction       | Per feature row, per sample (QC-RLSC)   |

When a **batch ID column** is provided, steps 2 and 3 are executed independently within each
batch. For the sample-wide step 3 methods, this is followed by an inter-batch alignment step to
center the reference abundances across all batches.

### Normalization factors

Each normalization step contributes a factor per (sample, feature) pair. The factors from all
enabled steps are **multiplied together** into a single composite function per sample. The final
normalized abundance is:

$$
\text{NormalizedAbundance} = \text{OriginalAbundance} \times \prod_{i} f_i
$$

where each $f_i$ is the factor from normalization step $i$. Steps 1 and the sample-wide step 3
methods depend only on the sample, step 2 on the sample and the feature's m/z and RT, and the feature
specific QC drift correction on the sample and the feature list row.

If any step has no factor for a feature, the feature receives **no normalized values** (empty
Normalized Height and Normalized Area). There is no fallback to the factors of the remaining steps.

### Interpolation to non-reference samples

For step 2 and the sample-wide step 3 methods, correction factors may be computed from **reference
samples** (typically pooled QCs). Non-reference samples receive a factor **linearly interpolated**
between the two nearest reference samples in acquisition order (based on acquisition timestamp from
metadata):

$$
f_{\text{sample}} = f_{\text{prev}} \cdot w_{\text{prev}} + f_{\text{next}} \cdot w_{\text{next}}
\quad \text{where } w_{\text{prev}} + w_{\text{next}} = 1
$$

Samples before the first or after the last reference injection receive the factor of the nearest
reference (no extrapolation).

The Feature specific QC drift correction does not use this linear interpolation; it evaluates a smooth curve
fitted to the QCs, see below.

### Batch-aware inter-batch normalization

When a batch ID column is enabled, a sample-wide step 3 method is selected, and multiple batches
are present:

1. Steps 2 and 3 are run independently within each batch.
2. The median reference-sample metric is recorded for each batch.
3. A global median is calculated across all batches.
4. Each batch receives an additional scaling factor: `globalMedian / batchMedian`.

This aligns the overall signal level of all batches without disturbing the intra-batch corrections.
This step is not applied for the Feature specific QC drift correction, which aligns the batches per feature through
its common correction target.

### Feature specific QC drift correction (QC-RLSC) {#qc-rlsc}

The Feature specific QC drift correction follows the QC robust LOESS signal correction (QC-RLSC) described by
Dunn et al. (2011). It is calculated separately for each feature list row and each batch:

1. **Input abundances**: the raw height or area of each feature, multiplied by the factors of steps
   1 and 2. Missing features (including features with status *unknown*), non-positive or
   non-finite values are not used. Gap-filled features are used.
2. **Acquisition order**: within each batch, samples are sorted by their acquisition timestamp and
   numbered 1, 2, 3, … The drift is modeled against this ordinal position, not against the elapsed
   time.
3. **Availability checks**: the feature is skipped
    - in all batches if its fraction of missing QCs over all batches exceeds the **Global missing
      QC fraction**,
    - in a batch if it has fewer than **Minimum usable QCs** usable QCs or more than 50% missing QCs
      in that batch.
4. **Robust LOESS fit**: the QC abundances are scaled by their median and smoothed with locally
   weighted linear or quadratic regression (tricube distance weights), followed by robust bisquare
   residual reweighting (two iterations for QC-RLSC, **Robustness iterations** for manual LOESS).
    - *QC-RLSC*: all combinations of degree 1 and 2 and neighborhood sizes from *degree + 2* up to
      the number of usable QCs are scored by the leave-one-out mean squared error over the QCs. The
      best candidate is selected; ties prefer the larger neighborhood (smoother curve), then the
      lower degree.
    - *Manual LOESS*: the neighborhood size is `ceil(bandwidth × usable QCs)` with the selected
      degree.
5. **Curve**: the smoothed QC values are connected by a natural cubic spline. Samples acquired
   before the first or after the last usable QC of the batch receive the curve value of the nearest
   QC (no extrapolation).
6. **Correction factor**: for every sample $s$ of the batch, including samples in which the
   feature was not detected,

    $$
    f_s = \frac{\tilde{y}_{\text{QC}}}{\hat{y}(s)}
    $$

    where $\hat{y}(s)$ is the fitted curve value at the sample's position in its batch and
    $\tilde{y}_{\text{QC}}$ is the median of the usable QC abundances of this feature across
    **all batches**. Dividing by the fitted curve removes the drift and the offset of each batch,
    as in Dunn et al.; multiplying by the common median keeps the abundance scale. After correction,
    the QCs of all batches are centered on the same level.
7. **Rejection**: the whole feature/batch combination is rejected if the fit fails, a curve value
   is not positive or not finite, or any factor lies outside the **Maximum correction factor**
   bounds. The remaining batches of the same feature are still corrected.

!!! tip

    The batch column defines which samples share one drift curve. Dunn et al. fit one curve per
    analytical block (e.g., two batches acquired within one week). Group the samples accordingly if
    the drift is continuous across several batches.

#### Unavailable features

Features without a factor keep their raw abundances but receive no normalized values for the
affected samples (see [Normalization factors](#normalization-factors)). The reasons are recorded per
row (and batch):

| Reason                          | Scope         | Cause                                                               |
|---------------------------------|---------------|---------------------------------------------------------------------|
| `NO_QC_REFERENCES`              | Feature       | No sample matches the reference sample types                        |
| `GLOBAL_MISSING_QC_THRESHOLD`   | Feature       | Missing QC fraction over all batches exceeds the global threshold   |
| `BATCH_INSUFFICIENT_USABLE_QCS` | Feature/batch | Fewer usable QCs than **Minimum usable QCs**                        |
| `BATCH_MISSING_QC_THRESHOLD`    | Feature/batch | More than 50% of the QCs in this batch are missing                  |
| `FIT_FAILED`                    | Feature/batch | No valid LOESS fit, e.g., too few neighbors for manual LOESS        |
| `INVALID_PREDICTION`            | Feature/batch | Fitted curve value not positive or not finite for a sample          |
| `FACTOR_OUT_OF_BOUNDS`          | Feature/batch | A factor exceeds the **Maximum correction factor** bounds           |

#### QC diagnostics

The task log and the applied method list a summary: the number of fully, partially, and not
corrected rows, globally skipped rows, and the number of corrected and unavailable feature/sample
pairs.

To inspect the Feature specific QC drift correction per row, open
**Feature lists tab → right-click a feature list → Show feature list summary**, select the intensity
normalization in the list of applied methods, and click **QC diagnostics**. For each row, the
dialog shows the availability (fully, partially, or not corrected, or the global skip reason), the
usable and total QC count, and the number of batches. Selecting a row shows the per-batch details:
skip reason, usable QCs and their position range, number of samples outside the QC range, QC RSD
before and after correction, leave-one-out error (QC-RLSC only), factor range, selected
degree, span and neighborhood size, correction target (QC median across all batches), and the observed and fitted
QC values along the curve.

### Persistence and re-application

The normalization functions are stored in the settings of the feature list and saved with the
project. Diagnostics (messages and Feature specific QC drift correction diagnostics) are stored with the applied
method. When features are added later (e.g., by gap filling or manual integration), mzmine
retrieves the stored functions and applies the same normalization to the new features.

The Feature specific QC drift correction stores its factors by **feature list row ID**. Gap-filled or manually
integrated features receive the stored factor of their row and sample; the QC curves are not
refitted.

### When the normalization is dropped, adapted, or blocked {#dropped}

Some processing steps after normalization invalidate the stored normalization. mzmine then removes
the normalization functions from the resulting feature list and clears the Normalized Height and
Normalized Area values. Run the Intensity normalizer again afterward.

| Processing step                                                     | Effect on the normalization                                                                                                                                                       |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feature resolving, smoothing, IMS expander                          | **Dropped**: the new features have new intensities                                                                                                                               |
| Feature list blank subtraction                                      | **Dropped** in both result lists: removing features changes the basis of all normalization factors, including sample-wide factors such as the feature median                     |
| Split aligned feature list                                          | **Dropped** in each split list: these lists are meant to be reprocessed per sample group                                                                                         |
| Row filters or copies that keep no rows                             | **Dropped**                                                                                                                                                                       |
| Row filters and other steps that copy, filter, or renumber rows    | Feature specific QC drift correction factors are **remapped** to the new row IDs; factors of removed rows are discarded                                                                            |
| Rows removed from a feature list in place                          | Feature specific QC drift correction factors of the removed rows are **discarded**, so that a later row with a reused ID does not inherit them                                                     |
| Gap filling, manual integration                                     | Normalization is **re-applied** to the new features with the stored functions                                                                                                    |
| Merging or aligning multiple feature lists                         | **Blocked** with an error if any input list has a Feature specific QC drift correction normalization, because row IDs of different feature lists collide. Normalize again after alignment instead |

The other normalization methods do not depend on row IDs and are kept when rows are copied,
filtered, or removed.

---

{{ git_page_authors }}
