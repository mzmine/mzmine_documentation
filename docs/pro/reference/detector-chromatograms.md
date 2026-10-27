# Other-detector chromatogram builder: implementation reference

This reference covers the reviewed knowledge-pack snapshot of the 4.10.111 development series. It extracts time series from spectral other-detector data; see the [user guide](../../module_docs/uv/uv_spectra_chromatogram_builder/spectrachrombuilder.md) for the workflow view. Runtime inputs determine what is available.

## Inputs and prerequisites

Select raw data files that contain other-data files with spectra. Files without spectra are skipped. The spectra must provide retention times and ordered domain values (normally wavelength). The module processes every spectral other-data file of each selected raw file.

## Parameters and validation

### Wavelengths

Enter one or more ranges in **nm**. Values inside each closed range are averaged. A one-sided entry is expanded around its value using the **Nanometer tolerance**, whose constructor default is **1 nm**. Extraction ranges are sorted by lower endpoint before use.

### Name

**Name** defaults to `Chromatograms` and becomes the description of the generated other-data file. A generated file with the same description is replaced in its raw data file.

## Processing behavior

For every spectrum and requested range, the builder finds the first domain value at or above the lower endpoint, then averages all intensities through the upper endpoint. If no point starts in the range, or no point is accumulated, the output is zero—not a missing point. Every output trace uses the source spectra's retention-time sequence.

The output chromatogram type is absorption if the source domain unit is `nm` **or** its range label is `Absorbance`; otherwise it is unknown.

## Outputs and side effects

One other-data time-series container is created per input spectral data set. It retains the source range label and unit and contains one raw trace per extraction range. Trace names use `Wv <lower>-<upper> nm`, formatted to at most two decimals; their wavelength metadata is the interval centre. An existing same-named other-data file is removed before the new one is added.

## Edge cases and errors

An empty range collection creates a container with no traces. The task does not reject a spectrum merely because a requested interval has no samples; it writes zeros. A same-name replacement can therefore discard an earlier generated container with that description.

## Worked examples

### Interval average

For a 250–252 nm request and a spectrum with values at 250, 251, and 252 nm, the corresponding chromatogram point is the arithmetic mean of those three intensities, not their sum.

### No sampled wavelength

If a spectrum has no domain value at or above the requested lower bound, the output still has that spectrum's retention time and an intensity of zero. This preserves point alignment across spectra.
