# Scientific analyses with mzassist {#scientific-analysis-through-the-mzmine-mcp-local-connector}

A processed feature table can support concentration estimates, quality checks and comparisons.
Describe your question to mzassist; it helps select the relevant features and samples, explains
which additional information is needed, and runs the calculation locally in mzmine after review.

| Your question | Guide | Information that may be needed |
| --- | --- | --- |
| What concentration does this response represent? | [Quantification](analysis/quantification.md) | Calibration concentrations, units, analytes, internal standards and independent QCs |
| Which injections or features need a QC review? | [Batch diagnostics](analysis/batch-diagnostics.md) | Injection sequence, sample roles, reference values and your method's alert criteria |
| How do conditions or time points differ? | [Study comparison](analysis/study-comparison.md) | Conditions, independent samples, repeat injections and any pairing or time information |
| Which features track the measured assay activity? | [Activity association](analysis/activity-association.md) | Assay measurements matched to samples, endpoint, dose and activity direction |
| What does a quantified amount imply under this use scenario? | [Exposure calculation](analysis/exposure-calculation.md) | A completed quantification, use scenario and an applicable reference value |

These five calculations currently start through **mzassist**. Their result views in mzmine let
you inspect and save the output; mzmine does not yet provide standalone setup dialogs for these
same calculations. Ordinary processing, metadata editing and feature inspection remain available
through mzmine's existing menus and their respective guides.

## Information to review with mzassist {#shared-rules}

Start with the analytical question, rather than preparing every input by hand. mzassist can use
sample information already in the project after you approve sharing. It asks for facts that are
missing or ambiguous and shows the proposed assignments before calculating.

Your experiment records establish which files represent conditions, independent samples and repeat
injections. For example, two injections of one specimen are repeated measurements of one independent
sample. Confirming that distinction prevents a comparison from overstating the amount of evidence.
Calibration concentrations, assay results and exposure assumptions likewise come from your records;
they cannot be established from the mass spectra alone.

### How to interpret the measurements

Raw peak area is the usual starting measurement. Existing normalized area or height can be used
when appropriate; choosing them uses a previously calculated column and does not itself normalize
the data. Study comparison and activity association average technical repeats for each independent
sample. Quantification, batch diagnostics and exposure retain individual sample results.

An unavailable or invalid measurement remains missing rather than becoming zero. This can reduce
the number of samples contributing to a result. The output records those counts and exclusions so
you can judge whether the result answers your question. If you change the underlying table or
sample assignments, ask mzassist to update the analysis before interpreting the earlier result.

## Quantification

[Quantification](analysis/quantification.md) converts feature responses into concentrations using
calibration measurements. External calibration uses the analyte's own standards; internal-standard
calibration also accounts for the response of a specified internal standard. A surrogate-reference
calibration expresses an estimated quantity relative to a different reference compound.

The guide explains what calibration information to provide, how to review the proposed fit with
mzassist, and how to inspect the curve, independent QCs, dilution corrections and results outside
the calibrated range.

## Batch diagnostics

[Batch diagnostics](analysis/batch-diagnostics.md) help investigate QC precision, reference mass and
retention-time deviations, internal-standard response and possible carryover. The injection sequence
is needed to put each observation in context; a blank can support a carryover check only when its
position after the relevant injection is known.

Flags identify measurements for inspection using your method's criteria. See the guide for
interpreting those flags and the distinction between diagnostics and corrections.

## Study comparison

[Study comparison](analysis/study-comparison.md) summarizes differences between conditions or time
points and can calculate a statistical test suited to the design. mzassist helps review the sample
mapping, repeated measurements, transformation and proposed test before calculation.

Interpret effect sizes, uncertainty and independent-sample counts alongside p values. Multiple-testing
correction covers the eligible features selected for that analysis; changing the selection changes
the family of tests. The guide describes the supported tests and their limits.

## Activity association

[Activity association](analysis/activity-association.md) relates feature abundance to measured assay
activity across matched samples or fractions. The meaning of the assay endpoint matters: lower
viability and higher inhibition can both represent greater activity.

The guide explains how to interpret an association, including the effects of coeluting compounds
and shared sample trends.

## Exposure calculation {#exposure-assessment}

[Exposure calculation](analysis/exposure-calculation.md) uses a completed mzassist quantification
and your stated use scenario to compare an estimated exposure with a supplied reference value.
The guide explains quantity basis, unit conversions, eligible samples and the assumptions to review.

The guide also explains how to choose an applicable reference and interpret the resulting ratio.

## Next steps

Ask mzassist to open the completed calculation in mzmine and explain its main findings and exclusions.
From that result view, use **Save table (CSV)** and **Save calculation record (JSON)** to retain the
output and assumptions. See [Save and reproduce your work](mzassist-saving.md).

For a finding you intend to report, ask mzassist to open the supporting chromatograms or spectra
in mzmine. Resolve uncertain sample assignments, calibration inputs or reference assumptions before
using the calculation to draw a scientific conclusion.

{{ git_page_authors }}
