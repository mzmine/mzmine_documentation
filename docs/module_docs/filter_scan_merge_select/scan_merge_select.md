# Merge & select fragment scans

This parameter is used in many modules like spectral library search, molecular networking, scan
export, etc. to control which fragment spectra are filtered, merged, and selected.
The final list of scans used in those modules may be input scans, e.g., a single MS2 scan or a
GC-EI-MS pseudo MS2 scan, or they grouped and merged on various levels.
To make this complex process simple and to provide options, there are multiple ways to configure
this parameter.

**Merging is generally done in this order:**

- split scans by samples
- merge for each energy and across energies (for each sample)
- merge across all samples

**For MS^n data:**

- merge MS^n scans for each MS^n tree node (precursor ion) for each energy and across energies (for
  each sample)
- merge all MS^n scans to a pseudo MS^2 scan

### The four configuration options are:

1. **Merged (simple)**: Presets with few settings
2. **Merged (preset)**: Presets with more control
3. **Input scans**: Input scans without merging
4. **Advanced**: All options

### 1. Merged (simple)

Simple preset-based scan selection that will always merge scans across all samples. For more
control, choose **Merged (preset)**.
The final selection of scans is based on presets defined below.
In general, all presets include a scan merged across all energies and for MS^n data a pseudo MS^2
scan that merges the whole MS^n tree.

#### Presets

1. **Single scan: Merged across energies** - Merge all input MS^2 scans. For MS^n data also merge
   all MS^n to an additional pseudo MS^2. A great option for speed by limiting the number of
   fragment scans.
2. **Representative scans: Each energy & merged across energies** - Like **1** and adds scans for
   each fragmentation energy. This is a great option for algorithms where the intensity differences
   in various energies is important - like spectral library matching by cosine similarity.
3. **MS^n tree: Merged across energies & pseudo MS^2** - Like **1** when used on MS^2 data - but for
   MS^n one spectrum per tree node (precursor ion) will be added. This option can be used with MS^2
   data as well.
4. **Representative scans or MS^n tree: Each energy, merged across energies & pseudo MS^2** - Like *
   *2** and **3** this module will add spectra for each MS^n tree node and fragmentation energy for
   each. This option can be used with MS^2 data as well.

#### Merging m/z tolerance

Used to match signals across scans and merge them. This tolerance is typically higher than the
advertised mass accuracy. As it is from scan-to-scan and across samples.

### 2. Merged (advanced)

Similar to the simple preset-based setup. The same presets but with more additional parameters, as
described below:

#### Merge

Select one or multiple options how to handle multiple samples:

- Across samples (like the simple setup)
- Each sample

#### Intensity merging mode

- **Summed** - suppresses low intensity signals and spurious noise but changes the amplitude
- **Maximum value** - retains the general amplitude 
- **Average** - average intensity of signals across all merged scans

### 3. Input scans

Options to disable merging and choose the input scans instead. This is either:

1. **Most intense scan across samples**: One scan per fragmentation energy across all samples with the highest summed intensity
2. **Most intense scan per sample**: One scan per fragmentation energy for each sample with the highest summed intensity
3. **All scans**: All input scans will be selected

### 4. Advanced

This is the full setup with the highest flexibility. The advanced option allows to combine multiple
different scan selections.

#### Merging options

Select multiple options that will be combined with each other. Options include handling of multiple
samples, fragmentation energies, and MS^n data.

1. **Across samples** - Merging happens across all samples .
2. **Each sample** - Merging happens for each sample separately and also across samples if selected.
3. **Across energies** - Merging happens across energies to combine all into one.
4. **Each energy** - Merging happens for each fragmentation energy and also across energies if
   selected.
5. **MS^n tree** - Merging happens for each MS^n tree node (precursor) - this option will be
   combined with sample and energy handling. This has no effect on MS^2 data.
6. **MS^n to pseudo MS^2** - Merges all MS^n spectra into a single 'MS^2' spectrum. This has no effect on MS^2 data.

#### Also include input scans

Also include unmerged input scans into the final scan selection. This is from the "raw" or "source" scans that are input to the merging. 

1. **Most intense scan across samples**: One scan per fragmentation energy across all samples with the highest summed intensity
2. **Most intense scan per sample**: One scan per fragmentation energy for each sample with the highest summed intensity
3. **All scans**: All input scans will be selected
4. **None**: Select **no** input scan but rely only on merged scans. This requires merging to be active, by selecting valid **merging options**

#### Examples

**Example 1:** **Across samples + across energies**: This will produce a single scan that is merged
across all scans of all energies and samples.
Adding **each sample** will then also export one more scan for each sample (if this sample has
fragmentation spectra).
Adding **each energy** will then add scans for each energy state. If across samples and each sample
are selected, this means there will be spectra added for each sample and then merged across all
samples.

**Example 2:** **Each sample** + **Single most intense scan** + **across energies**: This
combination will export the single best scan in each sample and then one merged scan per sample -
both only if there are fragment scans in this sample.

---

{{ git_page_authors }}
