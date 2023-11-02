# SIMSEF Workflow

## Workflow description

The spatial ion mobility-scheduled exhaustive fragmentation (SIMSEF) module can be used in trapped
ion mobility (TIMS) imaging workflows to schedule fragmentation spectra acquisitions for every
detected feature across the tissue. This achieves high MS2 coverage and allows more confident
compound annotations. To use the SIMSEF tool, the prmMALDI prototype instrument control software is
required, which is distributed by Bruker Daltonics to cooperation partners. You can contact your
Bruker representative to ask for the prmMALDI prototype and refer to SIMSEF.

## Requirements

- access to timsTOF fleX instrument
- access to the prototypic timsControl 4.1 with the prm-MALDI option (contact your Bruker representative)
- [Download](https://github.com/SteffenHeu/simsef_py/releases) SIMSEF acquistion tool

## Procedure

**Note:** :warning: acquire MS1 data with a smaller laser spot size than raster size (= stage movement/pixel size)
    - this leaves some tissue for MS2 acquisition

1. Prepare the sample following your default procedure.
2. Setup the imaging run in flexImaging. Set the raster size bigger than the laser spot size in your
   imaging method (e.g. laser spot size = 20 µm, raster size = 50 µm).
3. Save the imaging run via "Save imaging run as...". This will store the geometry files for later
   use.
4. Restart timsControl (prm-MALDI prototype) to make the instrument recognize the geometry files.
   Recalibrate the instrument (recommended).
5. Start the MS1 imaging run.
6. Copy the raw data to a powerful data analysis machine (Windows and Linux support Bruker raw data)
7. Analyse the MS1 data and filter it to your liking (
   see [imaging worflow](../imagingworkflow/imaging-workflow.md)). If your IMS seperation allows,
   filter for
   [isotopic peaks](../../module_docs/filter_isotope_filter/isotope_filter.md).
8. Run the [SIMSEF scheduler](../../module_docs/tools_simsef/simsef.md). Using the preview, evaluate
   the fragmentation schedules.
9. Copy the schedule to the instrument computer.
10. Load the istrument method, you want to acquire the MS2 spectra with. Make sure the method is
    appropriate for your expected fragment ion m/z range.
    - Disable MALDI mode, enable PASEF mode, ensure that "advanced" is disabled for the collision
      energy settings.
    - Enable MALDI mode, save the method.
    - Set MS mode to MS/MS in the MALDI settings.
11. Set instrument to operate and recalibrate if needed.
12. Run "simsef_pewpew.exe" on the instrument computer.

{{ git_page_authors }}
