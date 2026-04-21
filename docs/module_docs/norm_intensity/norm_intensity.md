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
3. **QC drift correction**: removes signal drift within an analytical batch using reference
   samples (e.g., pooled QCs) and, when multiple batches are present, aligns batch medians to a
   global reference median.

Normalized values are written to dedicated **Normalized Height** and **Normalized Area** columns
and the normalization functions are stored with the feature list so that they can be automatically
re-applied to features added later (gap filling, manual integration).

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
normalization calculations.

---

#### Batch correction metadata column _(Optional)_

Metadata column whose values identify the analytical batch a sample belongs to (e.g.,
`Batch`). When enabled, the normalization pipeline is run independently per batch:

- Steps 2 and 3 are applied within each batch using only that batch's reference samples.
- After intra-batch correction, a final **inter-batch normalization** aligns the median
  reference-sample signal of every batch to the global median, correcting for between-run
  differences.

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
- **Internal standard compounds**: Normalization by internal standards is described in more detail [
  **here**](../norm_stand_cmpd/norm_stand_cmpd.md).

#### Inter-sample correction: Step 3

Corrects signal drift across samples using a set of reference injections (typically pooled QCs) or
all samples.
This step runs after metadata normalization (step 1) and internal standard correction (step 2).
Intra-batch correction is applied first; if multiple batches are defined, inter-batch alignment
is performed afterward by centering the median batch reference abundance against a global median.

Available options:

- **No normalization**: step 3 is skipped.
- **By feature abundances**: see sub-parameters below.
- **Spectral TIC**: see sub-parameters below.

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

---

## Algorithm {#algorithm}

### Normalization pipeline

The three correction steps are always applied in the following order. Each step is independent
and optional; any combination can be enabled:

| Step | Parameter                     | Scope                        |
|------|-------------------------------|------------------------------|
| 1    | Metadata normalization column | Per sample (constant factor) | 
| 2    | Intra-sample correction       | Per feature, per sample      | 
| 3    | Inter-sample correction       | Per sample (interpolated)    | 

When a **batch ID column** is provided, steps 2 and 3 are executed independently within each
batch, followed by an inter-batch alignment step to center the reference abundances across all batches.

### Normalization factors

Each normalization step contributes a factor per (sample, feature) pair. The factors from all
enabled steps are **multiplied together** into a single composite function per sample. The final
normalized abundance is:

$$
\text{NormalizedAbundance} = \text{OriginalAbundance} \times \prod_{i} f_i(m/z,\, RT)
$$

where each $f_i$ is the factor from normalization step $i$.

### Interpolation to non-reference samples

For steps 2 and 3, correction factors may be computed from **reference samples** (typically
pooled QCs). Non-reference samples receive a factor **linearly interpolated** between
the two nearest reference samples in acquisition order (based on acquisition timestamp from
metadata):

$$
f_{\text{sample}} = f_{\text{prev}} \cdot w_{\text{prev}} + f_{\text{next}} \cdot w_{\text{next}}
\quad \text{where } w_{\text{prev}} + w_{\text{next}} = 1
$$

Samples before the first or after the last reference injection receive the factor of the nearest
reference (no extrapolation).

### Batch-aware inter-batch normalization

When a batch ID column is enabled and multiple batches are present:

1. Steps 2 and 3 are run independently within each batch.
2. The median reference-sample metric is recorded for each batch.
3. A global median is calculated across all batches.
4. Each batch receives an additional scaling factor: `globalMedian / batchMedian`.

This aligns the overall signal level of all batches without disturbing the intra-batch corrections.

### Persistence and re-application

The normalization functions are serialized as part of the feature list's applied-methods record.
When features are added later (e.g., by gap filling or manual integration), mzmine can retrieve the
stored functions and applies the same normalization to the new features.

---

{{ git_page_authors }}
