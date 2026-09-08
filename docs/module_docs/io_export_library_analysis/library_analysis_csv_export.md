# Library analysis csv export

:material-menu-open: **Tools → Libraries → Library analysis csv export**

Compares **all pairs of spectra** within one or more loaded spectral libraries and exports the
pairwise spectral similarities to CSV. This is an analysis tool for library and method development,
for example to study how cosine, modified cosine, and neutral loss similarity behave on a known set
of compounds.

For every pair of library entries three similarity types are calculated:

- `cos` - cosine similarity of the fragment spectra
- `modcos` - modified cosine similarity, which additionally matches signals shifted by the precursor
  *m/z* difference
- `nl` - cosine similarity of the neutral loss spectra

See [spectral similarity measures](../id_spectral_library_search/spectral-similarity-measures.md)
for the definitions.

!!! warning

    The number of compared pairs grows quadratically with the library size. A library with 10,000
    entries produces about 50 million pairs. Start with a small or filtered library.

## Output files

Two files are written next to each other:

- `<filename>.csv` - the edge table. Each line describes one spectrum pair with the columns `IDa`,
  `IDb` followed by, for each of the three similarity types, the columns `matched_n`,
  `matched_rel`, `matched_intensity`, `matched_intensity_a`, `matched_intensity_b`, `score`,
  `max_contribution`, `signal_contributions`, and `signals_contr_gr_0_05`.
- `<filename>_nodes.csv` - the node table describing the individual library entries with the columns
  `ID`, `name`, `mz`, `mass`, `adduct`, `formula`, `ion_mode`, `instrument`, `instrument_type`,
  `smiles`, `isomeric_smiles`, `inchi`, `inchi_key`, and `signals`.

The two files can be loaded directly as an edge and node table in network visualization software
such as Cytoscape.

---

## Parameters

#### Spectral libraries

The loaded spectral libraries to analyze.

#### Filename

Name of the output CSV file. An existing file is overwritten.

#### Field separator

Character used to separate fields. Default is `,`.

#### Weights

*m/z* and intensity weighting applied to all signals before scoring. Default is `SQRT`.

#### Remove +-m/z around precursor _(Optional)_

Removes residual precursor signals from the spectra before scoring. Enabled by default with a
tolerance of 17 Da, which also removes typical water and ammonia losses of the precursor.

#### 13C deisotoping _(Optional)_

Removes 13C isotope signals from the spectra before scoring. Disabled by default.

#### Minimum matched signals

Minimum number of signals a spectrum must retain after filtering to be included in the analysis, and
minimum number of matched signals required for a reported pair. Default is 6.

#### Spectral m/z tolerance

Tolerance used to match signals between two spectra. This is usually wider than a precursor
tolerance. Default is 0.01 Da or 10 ppm.

!!! warning

    Library entries without a precursor *m/z*, entries containing signals with zero intensity, and
    entries with fewer than `Minimum matched signals` remaining signals are excluded. The number of
    excluded entries per reason is written to the mzmine log.

---

{{ git_page_authors }}
