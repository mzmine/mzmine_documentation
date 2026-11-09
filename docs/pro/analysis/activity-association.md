# Relate features to measured activity

Use activity association to prioritize features whose abundance covaries with an assay measurement,
for example across fractions. It identifies associations for follow-up; it does not identify an
active compound or establish a biological mechanism.

## Prepare matched measurements

Map the assay measurements to the samples in the shared feature table. Supply the condition and
independent-unit identifier for each sample. Use one assay endpoint, dose, context, and direction
per analysis; split measurements from different assays or doses before calculating.

State whether higher or lower assay values mean greater activity. For example, a viability endpoint
and an inhibition endpoint can have opposite directions. Use the endpoint's meaning in your assay,
not just its numeric scale.

Choose raw area, height, an existing normalized measurement, or a compatible quantification result.
At least three independent units with both an assay and a feature measurement are needed for a
correlation. Repeat measurements within a unit are averaged before pairing. Missing values do not
become zero, and repeat injections do not increase the independent-unit count.

## Ask mzassist

> Associate the selected feature measurements with this assay endpoint across the mapped samples.
> Show the sample mapping, independent-unit counts, and activity direction. Explain whether Pearson
> or Spearman correlation matches the question before calculating.

Check the mapping before running, particularly if one sample has multiple assay measurements.
The current activity calculation does not offer the study-comparison log2 transformation option.

## Interpret the ranking

The output includes the paired values, correlation, matched-unit count, and a priority score whose
sign follows the declared activity direction. Changing that direction changes the interpretation
of the ranking. Constant values or too few matched units do not yield a usable correlation.

A confidence interval is available only for qualifying Pearson results; the calculation does not
report a p value. Inspect the observations and influential points, chromatograms, spectral evidence,
and correlated/coeluting features before choosing candidates for follow-up.

Save the table and calculation record with the assay endpoint, dose, context, direction, sample
mapping, and measurement choice. See [Save and reproduce your work](../mzassist-saving.md).

{{ git_page_authors }}
