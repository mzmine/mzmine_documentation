# Wavelet resolver: implementation reference

The Wavelet resolver is experimental. Validate results on representative data and see the [Wavelet resolver guide](../../module_docs/featdet_resolver_wavelet/wavelet_resolver.md).

## Inputs and prerequisites

The resolver operates on a chromatogram intensity series with matching RT and intensity arrays. It supports ion mobility. General resolver controls select feature lists/dimension, minimum data points, suffix, original-list handling and optional MS2 grouping. Their base defaults are retention-time resolving, MS/MS pairing enabled, minimum 3 data points, suffix `resolved`, and retain original feature lists. Invalid arrays (null, unequal lengths, or fewer than five points) yield no resolved ranges.

## Parameters and validation

### Core filters

**Signal to noise (SNR) threshold** defaults to 5 and accepts values ≥1. **Minimum height** defaults to 1,000 and accepts ≥0. **Noise calculation** defaults to Standard deviation; Median absolute deviation is the alternative. **Baseline estimation** defaults to edge average. **Dip filter** defaults enabled, while built-in GC presets disable it. **Re-split unresolved double peaks** is off by default; when enabled its default apex-to-valley factor is 1.5 and must be ≥1.

### Advanced defaults

Advanced controls default to scales `0.5, 1, 1.5, 2, 3, 5, 8, 10`; noise-window factor 3 (never effectively below 1); required fitting scales 2; robustness iteration **Default** (enabled); edge detector **Absolute minimum window jagged + FWHM**; sign changes every 2 points; maximum similar-height background ratio 0.10; and saturation filter **Default** (enabled). Empty/invalid comma-separated scales fail validation. “Off” for scales retains default scales; off for required fits/sign changes uses 1; off for similar-height ratio uses 1.

## Processing behavior

The resolver computes continuous-wavelet coefficients at sorted configured scales, finds wavelet-supported candidate maxima, rejects low-height candidates, determines boundaries, merges overlapping ranges, and then applies dip, saturation, and jaggedness filters. A peak is rejected when `max(0, direction reversals − 1) × N / point count > 1` in the jaggedness step.

Local background excludes potential-peak regions. Noise estimation and baseline selection produce an SNR filter; a robustness iteration repeats that estimation after rejected peaks have been removed. With fewer than six background points, the resolver instead tests peak-top/mean-edge baseline; a non-finite or failing fallback becomes indeterminate (“surrounded”). Such a candidate is retained only if a neighbouring SNR-passing peak supplies noise and the recomputed edge-baseline SNR passes. Optional double-peak splitting occurs last, using an edge-to-edge interpolated baseline, so it is independent of the configured baseline method. Returned ranges are sorted by lower RT.

## Outputs and side effects

For each accepted peak the resolver returns its RT interval to the general resolving workflow; that workflow constructs the resolved features/list according to its common settings. Resolver output itself is an ordered list of RT ranges, not a quantification table. The saturation threshold is calculated per raw data file as 90% of its maximum scan base-peak intensity.

## Edge cases and errors

Invalid short/mismatched data returns an empty result with a warning. No CWT candidate, no valid boundary, or no passing SNR candidate also returns no ranges. A peak must satisfy the common minimum-data-points setting after boundaries are determined. An invalid configured scale list can fail parameter validation; an empty scale array reaching construction is rejected.

## Worked examples

### A short trace

An RT/intensity series of four points is not resolved: fewer than five points triggers the input guard and produces an empty result, independent of SNR or scale selection.

### An unresolved doublet

With the split control disabled, a partially separated signal that survives CWT, boundaries and SNR remains one resolved range. Enable it at the default 1.5 only when both maxima are at least 1.5 times the internal valley after edge-to-edge baseline correction; then it may produce two ranges at the final split stage.
