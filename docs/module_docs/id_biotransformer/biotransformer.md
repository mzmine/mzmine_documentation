# **BioTransformer 3.0**

## **Description**

:material-menu-open: **Feature list methods -> Annotation -> Search precursor mass -> BioTransformer 3.0**

or, for one annotated feature row:

:material-menu-open: right-click a row in the feature table and choose **Identification -> Compute transformation products (BioTransformer 3)**

The BioTransformer 3.0 module predicts possible transformation products for compounds that are
already annotated with a structure. MZmine sends the educt SMILES string to an external
BioTransformer 3 `.jar`, imports the generated CSV file, calculates product ions from the selected
ion library, and adds matching products as compound annotations to feature list rows.

Use this module after a spectral library search or compound database search has produced
annotations with SMILES structures. BioTransformer 3.0 does not identify unknown educts by itself:
it starts from an existing annotation, predicts transformation products, and searches for those
products in the same feature list.

!!! warning

    BioTransformer 3.0 is not bundled with MZmine. Download the BioTransformer `.jar` from the
    [BioTransformer 3.0 jar downloads](https://bitbucket.org/wishartlab/biotransformer3.0jar/downloads/)
    or the [BioTransformer download page](https://biotransformer.ca/download), and keep the
    extracted BioTransformer files together in one folder. MZmine runs the selected jar via
    `java -jar`, so the `java` command must be available to MZmine.

!!! tip

    Start with a restrictive m/z tolerance and, when retention time behavior is expected, enable
    the advanced RT tolerance filter. This keeps predicted products from being assigned to unrelated
    features with similar m/z values.

## **Recommended citations**

!!! info

    When using MZmine for your work, please consider citing:<br>
    Schmid R., Heuckeroth S., Korf A., et al. Integrative analysis of multimodal mass spectrometry
    data in MZmine 3, Nature Biotechnology (2023), doi:10.1038/s41587-023-01690-2.

    When using this module, please also cite the BioTransformer publication(s):<br>
    Djoumbou Feunang Y., Fiamoncini J., de la Fuente A.G., Manach C., Greiner R., Wishart D.S.
    BioTransformer: a comprehensive computational tool for small molecule metabolism prediction and
    metabolite identification. Journal of Cheminformatics 11, 2 (2019).
    doi:10.1186/s13321-018-0324-5.

    Wishart D.S., Tian S., Allen D., Oler E., Peters H., Lui V.W., Gautam V.,
    Djoumbou Feunang Y., Greiner R., Metz T.O. BioTransformer 3.0 - A Web Server for Accurately
    Predicting Metabolic Transformation Products.

---

## **Parameters**

#### **Feature lists**

Feature list(s) to process. Each selected feature list is processed independently.

#### **BioTransformer .jar path**

Path to the BioTransformer 3 `.jar` file. Select the jar inside the folder that contains the
unpacked BioTransformer download.

#### **Transformation type**

BioTransformer prediction mode. The available modes are:

- **EC-based (Enzyme Commission)**
- **CYP450**
- **Phase II**
- **Gut microbial**
- **All human**
- **Super bio**
- **Environmental microbial** (default)

#### **Iterations**

Number of BioTransformer prediction iterations. One iteration predicts direct products of the
input compound. Higher values also predict products of previous products. Default: `1`.
Allowed range: `1` to `10`.

#### **m/z tolerance**

Maximum m/z difference for matching predicted product ions to feature list rows. Default:
`0.003 m/z` or `5 ppm`.

#### **Ion library**

Ion types used to calculate product m/z values from the predicted neutral products. The default is
the MZmine main ion library for both positive and negative polarity.

#### **Filter parameters** _(Optional)_

Additional filters for choosing educt rows and product rows. Disabled by default.

- **Educt must have MS/MS**: only predicts transformations for rows with an MS/MS spectrum.
- **Minimum Educt intensity**: only predicts transformations for rows whose best feature height is
  at least the selected intensity. The embedded default value is `1E4`, but the filter is disabled
  until selected.
- **Product must have MS/MS**: only assigns predicted products to rows with an MS/MS spectrum.
- **Minimum Product intensity**: only assigns predicted products to rows whose best feature height
  is at least the selected intensity. The embedded default value is `1E4`, but the filter is
  disabled until selected.

#### **SMILES source**

Annotation source used to obtain the educt SMILES in the full feature-list workflow.

- **Spectral library**: use the first spectral library match with structure information.
- **Compound DB**: use the first compound database annotation with structure information.
- **All** (default): prefer the first spectral library match; if none is available, use the first
  compound database annotation.

This parameter is not shown in the single-row context-menu workflow. The context action uses the
first spectral library match with structure information, or the first compound database annotation
with structure information if no spectral library match is available.

#### **Advanced parameters**

Extra matching and annotation-ranking options.

- **RT tolerance filter** _(Optional)_: only assigns predicted products within the selected
  retention-time tolerance around the educt row. Default embedded value: `0.15 min`.
- **Filter by row correlation**: only assigns predicted products to rows that are correlated with
  the educt row. The feature list must have been grouped by correlation, for example with the
  correlation grouping module.
- **Re-rank annotations**: controls whether compound annotations are re-ranked by highest score
  after BioTransformer matches are added. Enabled by default when advanced parameters are enabled.

---

## **Algorithm** {#algorithm}

### Selecting educts

In the full feature-list workflow, MZmine scans the selected feature list and looks for rows that
pass the optional educt filters and contain a usable SMILES structure. The selected annotation is:

1. the first spectral library match, if the SMILES source allows spectral library annotations and
   the match has structure information,
2. otherwise the first compound database annotation, if the SMILES source allows compound database
   annotations and the annotation has structure information.

Rows without a usable structure are skipped. Identical canonical SMILES strings are predicted only
once per feature list.

In the single-row workflow, MZmine uses the selected row's first spectral library match with a
structure, or the first compound database annotation with a structure if no spectral library match
is available.

!!! warning

    BioTransformer is not run for educt structures whose calculated monoisotopic mass is above
    `1000 Da`, because the BioTransformer command-line tool cannot process those compounds.

### Running BioTransformer

For each selected educt SMILES, MZmine creates a temporary CSV file and runs BioTransformer in
prediction mode:

```text
java -jar BioTransformer3.0.jar -k pred -b <transformation type> -s <iterations> -ismi <SMILES> -ocsv <temporary CSV>
```

The BioTransformer result CSV is imported as compound database annotations. MZmine reads the
product formula, SMILES, InChI, InChIKey, reaction, enzyme information, ALogP, and metabolite ID
columns when present. Product names are prefixed with the educt compound name.

### Matching products to the feature list

Imported products are ionized with the selected ion library. Each generated product ion is compared
against rows in the same feature list:

1. m/z must match within the configured m/z tolerance.
2. If the RT tolerance filter is enabled, the product must also match within the RT window around
   the educt row.
3. If the row correlation filter is enabled, the product row must be correlated with the educt row.
4. If product filters are enabled, the product row must pass the selected MS/MS and intensity
   filters.

Matching product ions are added as compound annotations. The match score and deviation columns are
calculated by the compound database annotation matcher.

### Output columns

BioTransformer matches are stored as compound annotations in the feature list. Depending on the
available product data and enabled filters, annotations can include:

| Column | Description |
| --- | --- |
| Compound name | BioTransformer metabolite ID prefixed by the educt name |
| Molecular formula | Product molecular formula |
| SMILES | Product SMILES |
| InChI / InChIKey | Product structure identifiers |
| Reaction | BioTransformer reaction rule |
| Enzyme(s) | Enzyme or biosystem information reported by BioTransformer |
| ALogP | Predicted ALogP value reported by BioTransformer |
| Ion type | Product ion type from the selected ion library |
| Precursor m/z | Calculated product ion m/z |
| Compound annotation score | Score from matching the predicted product ion to the row |
| m/z ppm difference | Mass error in ppm |
| m/z absolute difference | Absolute mass difference |
| RT absolute difference | RT difference, if RT filtering was enabled |
| RT relative error (%) | Relative RT error, if RT filtering was enabled |

---

{{ git_page_authors }}
