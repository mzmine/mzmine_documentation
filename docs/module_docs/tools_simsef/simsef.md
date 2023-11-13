# Spatial ion mobility-scheduled exhaustive fragmentation (SIMSEF)

## Description

The spatial ion mobility-scheduled exhaustive fragmentation (SIMSEF) module can be used in trapped
ion mobility (TIMS) imaging workflows to schedule fragmentation spectra acquisitions for every
detected feature across the tissue. This achieves high MS2 coverage and allows more confident
compound annotations. To use the SIMSEF tool, the prmMALDI prototype instrument control software is
required, which is distributed by Bruker Daltonics to cooperation partners.

**Note:** :warning: Due to the size of IMS-MS imaging data, we recommend to use 10,000-40,000 pixels
in your MS1 run for SIMSEF experiments

## Parameters

### Feature lists

Select the feature list to create the MS2 events for.

### Data location

File path to store the schedule in. This directory must also exist on the data acquisition PC and
not contain spaces or special characters.

### Path to msmsmaldi.exe

Path to the simsef_pewpew.exe

#### Number of MS2 spectra

Sets the desired number of MS2 events to be scheduled per precursor and collision energy.

#### Collision energies

Lists the collision energies to acquire MS2 spectra for every precursor.

#### Minimum distance of MS2 pixels

Defines the spatial pixel-based distance between MS2 events of the same precursor ion and with the
same collision energy.

#### Minimum MS1 intensity

Describes a relative and absolute intensity threshold for the precursor in an MS1 pixel to be
selected for MS2 experiments. Specified as absolute and relative parameter, which will use the
larger of the two values with regard to the feature.

#### Minimum purity score

Defines an exclusion criterion for scheduling MS2 events in a pixel, in case the quadrupole
isolation would lead to chimeric MS2 spectra composed of multiple precursor ions.

#### Export MSMS lists only

Exports only the MS2 lists and does not start an acquisition.

### Advanced parameters

#### Quadrupole switch time (ms)

Defines the assumed switch time of the quadrupole. This influences how close multiple precursors
will be scheduled. Low values may lead to co-isolation and overlapping of precursor values.

#### Isolation width

Sets the quadrupole isolation window in the instrument parameters and influences the purity score
calculation.

#### Minimum mobility window and Maximum mobility window

Describe the minimum and maximum length of a precursor isolation width in the mobility dimension.
The features detected mobility range will be cropped or extended to be within the minimum and
maximum mobility window.

## Output

The scheduling module creates a folder including an "acquisition.txt" including the acquisition
table, collision energy table(s), precursor lists for every spot, and "precursors.csv" and "
spots.csv" files. The "precursors.csv" and "spots.csv" files allow statistical evaluation of the
expected MS2 coverage prior to the analysis.

To acquire the MS2 spectra, the whole folder must be copied to the acquisition computer to the
location specified as the "data location" parameter.

## References

[1] Wolf, C. et al. Mobility-Resolved Broadband Dissociation and Parallel Reaction Monitoring for
Laser Desorption/ionization-Mass Spectrometry - Tattoo Pigment Identification Supported by Trapped
Ion Mobility Spectrometry. Anal. Chim. Acta 2023, 1242, 340796.
<!-- markdown-link-check-disable-next-line -->
doi: https://doi.org/10.1016/j.aca.2023.340796

{{ git_page_authors }}
