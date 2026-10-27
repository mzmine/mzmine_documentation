# MRM to scans: implementation reference

This reference describes the reviewed knowledge-pack snapshot of the 4.10.107 development series; exposed inputs remain runtime-dependent. It expands the [MRM to scans guide](../../module_docs/mrm_mrmtoscans/mrm-to-scans.md).

## Inputs and prerequisites

Select raw data files containing MRM/SRM or SIM time-series. TIC, BPC and SIC traces, non-MS traces, and unrecognised traces are ignored. A transition needs Q1/Q3 information from its metadata or a supported chromatogram-name pattern; unparseable chromatograms are skipped with a warning. The operation replaces the selected raw file's scan collection, so retain the original project/file if that distinction matters.

## Parameters and validation

### Build chromatograms

Default **true**. Creates a feature list named `<raw-file name> mrm`; one detected row per grouped transition set. It is deliberately not created while a project-open task is running, even if enabled.

### Static baseline subtraction

Default **true**. Each transition intensity is reduced by its lowest non-zero intensity (or by zero if unavailable). It changes transition chromatograms and therefore derived feature intensities, but not the generated pseudo-scans.

### Raw or pre-processed

Default **pre-processed**. This chooses the corresponding trace representation; when a pre-processed trace is absent, raw traces are used as the fallback.

## Processing behavior

### Grouping and scan conversion

Eligible transitions are grouped by Q1 within ±0.005 m/z and compatible retention-time coverage. For every grouped set, mzmine generates pseudo-MS2 spectra from Q3/intensity pairs, then pseudo-MS1 scans whose Q1 intensity is the sum of that set's transition intensities in the time interval. Generated scans are retention-time ordered, with MS1 before MS2 at equal time, and receive a mass list.

### Chromatogram representation

The feature's primary chromatogram is the group's default quantifier transition; all transitions are stored with it. Duplicate mappings to the same generated MS1 scan are omitted during chromatogram construction.

## Outputs and side effects

The selected raw data file is cleared and repopulated with generated pseudo-scans. When enabled outside project loading, a new feature list carries copied applied-method history, MS1 selected scans, MRM transition data, and sequential row IDs. Empty inputs, no parseable transitions, no groups, or cancellation return without producing later artifacts.

## Edge cases and errors

An interval that cannot be mapped to a generated MS1 scan raises an error. A trace may be present but silently excluded because it is TIC/BPC/SIC, non-MS, or has no readable transition metadata/name. Baseline subtraction can make the first/lowest points zero; it is not a background model.

## Worked examples

### Two transitions for one precursor

Transitions 500→120 and 500.003→150 in the same acquisition window are within the fixed Q1 grouping tolerance. At one dwell with intensities 40 and 60, the pseudo-MS2 has Q3 signals 120/40 and 150/60; the corresponding pseudo-MS1 represents Q1 500 with intensity 100. A feature row retains both transitions while its default quantifier supplies the feature chromatogram.

### Requested pre-processed trace is unavailable

With **Raw or pre-processed = pre-processed**, a file whose MRM trace has no pre-processed representation falls back to the raw trace. If **Build chromatograms** is enabled during project loading, scans are still converted but no feature list is added in that pass.
