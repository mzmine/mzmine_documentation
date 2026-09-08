# Score intra-row purity by MS2 similarity

:material-menu-open: **Feature list methods → Processing → Score intra-row purity by MS2 similarity**

Compares all MS/MS spectra that belong to the *same* feature list row against each other and scores
their pairwise modified cosine similarity. A row whose spectra disagree is suspicious: the row
either aggregates fragmentation spectra of co-eluting isomers or isobars, or - on an aligned feature
list - it aligned features of different compounds.

The result is a quality measure per row that is independent of any annotation, so it can be used
before or without spectral library search.

## Where this is useful

- **MALDI MS2 pairing and the SIMSEF workflow.** In
  [MALDI MS2 scan pairing (SIMSEF)](../featdet_ms2_scan_pairing/ms2_maldi_scan_pairing.md) a single
  feature collects fragmentation spectra acquired on many different MALDI spots. Those spectra
  should be identical apart from noise. A low intra-row similarity indicates that the imaged spots
  do not contain the same compound at that *m/z*, or that the isolation was chimeric on part of the
  measurement area. Scoring the row purity is therefore a natural QC step after running the
  [SIMSEF scheduler](../tools_simsef/simsef.md) and pairing the acquired MS2 spectra, and before
  generating a spectral library from the data.
- **Aligned feature lists.** Low scores point to rows where features of different compounds were
  aligned.

## Results

Each processed row receives an `Intra-row MS2 similarity` column containing the summary statistics
(average, minimum, maximum, and number of compared pairs) of all similarity values of that row,
together with a group label that bins the average score into `< 0.4`, `[0.4, 0.6)`, `[0.6, 0.85)`,
and `>= 0.85`. Sorting the feature table by this column brings the most suspicious rows to the top.

!!! tip

    Rows with only a single fragmentation spectrum cannot be scored and stay empty. This is expected
    and does not indicate a problem.

---

## Parameters

#### Feature lists

The feature list to process.

#### Export to file _(Optional)_

Additionally writes a CSV file with the columns `row_id` and `cosine_similarity`, containing one
line per compared spectrum pair. Useful to inspect the score distribution outside of mzmine.
Disabled by default.

#### m/z tolerance (MS2)

Tolerance for matching signals between two MS/MS spectra. Default is 0.003 Da or 10 ppm.

!!! tip

    Keep a reasonable absolute tolerance. A purely relative tolerance such as 5 ppm is too narrow to
    cover small neutral losses at low *m/z* values, for example around *m/z* 18.

#### Minimum signals

Minimum number of signals a spectrum must contain to be compared. Low quality scans below this
threshold are skipped. Default is 4.

#### Signal filters

Filters applied to each spectrum before comparison:

- **Remove residual precursor m/z** - removes signals around the precursor, including its isotopes.
  Strongly recommended, because precursor signals always match and would inflate the similarity.
  Enabled by default with a window of *m/z* 10.
- **Crop to top N signals** - keeps only the most abundant signals. Default is 250.
- **Signal threshold (intensity filter)** - above this number of signals, the spectrum is reduced to
  the top signals that make up the configured intensity percentage. Default is 50.
- **Intensity filter at >N signals** - the intensity fraction retained by the filter above. Default
  is 98%.

#### Split by collision energy

If enabled (default), only spectra acquired with exactly the same collision energy are compared.
Disable this only if your acquisition uses varying or ramped energies that should still be treated
as comparable.

!!! warning

    With this option disabled, spectra of different collision energies are compared directly, which
    lowers the similarity of perfectly pure rows.

---

{{ git_page_authors }}
