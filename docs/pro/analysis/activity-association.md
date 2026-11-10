# Activity association {#relate-features-to-measured-activity}

Activity association prioritizes features whose abundance covaries with an assay measurement, for example across fractions. An association is a lead for follow-up; it does not identify an active compound or establish a biological mechanism.

## What you need {#prepare-matched-measurements}

Assay measurements must be mapped to samples in the shared feature table, with condition and independent unit identified for each sample. One analysis uses one assay endpoint, dose, context, and direction; measurements from different assays or doses need separate analyses.

The activity direction states whether higher or lower assay values mean greater activity. For example, viability and inhibition endpoints can have opposite directions. Choose raw area, height, an existing normalized measurement, or a compatible quantification result.

At least three independent units with both assay and feature measurements are needed for a correlation. Repeat measurements within a unit are averaged before pairing. Missing values do not become zero, and repeat injections do not increase the independent-unit count. This calculation does not offer the study-comparison log2 transformation option.

## Calculate with mzassist {#ask-mzassist}

1. Ask mzassist to associate feature measurements with the assay. For example:

    > Associate the selected feature measurements with this assay endpoint across the mapped samples. Show the sample mapping, independent-unit counts, and activity direction. Explain whether Pearson or Spearman correlation matches the question before calculating.

2. mzassist checks the metadata you approved for sharing. Provide only the assay, sample, and study-design facts it still needs. If needed, edit metadata under **Project → Sample metadata**; see [Sample metadata](../../module_docs/project_metadata/project_metadata.md).
3. Confirm the proposed mapping and calculation in chat, particularly where a sample has multiple assay measurements. Ask mzassist to calculate and open the results.
4. Inspect paired values, correlation, matched-unit count, and priority score. The score's sign follows the declared activity direction. Inspect observations and influential points, chromatograms, spectral evidence, and correlated or coeluting features before choosing candidates.
5. Use **Save table (CSV)** and **Save calculation record (JSON)** in the result view, preserving the endpoint, dose, context, direction, mapping, and measurement choice. See [Save and reproduce your work](../mzassist-saving.md).

## Interpretation {#interpret-the-ranking}

Constant values or too few matched units do not yield a usable correlation. A confidence interval is available only for qualifying Pearson results; the calculation does not report a p value.

{{ git_page_authors }}
