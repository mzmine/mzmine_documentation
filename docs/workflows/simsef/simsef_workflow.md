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
- access to the prototypic timsControl 4.1/5.0 with the prm-MALDI option (contact your Bruker
  representative)
- [Download](https://github.com/SteffenHeu/simsef_py/releases) SIMSEF acquisition tool

## Procedure

**Note:** :warning: acquire MS1 data with a smaller laser spot size than raster size (= stage
movement/pixel size)
**Note:** :warning: Due to the size of IMS-MS imaging data, we recommend to use 10,000-40,000 pixels
in your MS1 run for SIMSEF experiments

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
   the fragmentation schedules and optimise the parameters. Check the task manager for running
   tasks. The scheduling may need some time.
9. Copy the schedule to the instrument computer. (**Must be the same path as selected on the
   analysis computer, not including spaces or special characters**)
10. Load the instrument method, you want to acquire the MS2 spectra with. Make sure the method is
    appropriate for your expected fragment ion m/z range.
    - Disable MALDI mode, enable PASEF mode, ensure that "advanced" is disabled for the collision
      energy settings.
    - Enable MALDI mode, save the method.
    - Set MS mode to MS/MS in the MALDI settings.
11. Set instrument to operate and recalibrate if needed (recommended).
12. Select the correct geometry file on the instrument computer (saved in step 3)
12. Run "simsef_pewpew.exe" on the instrument computer, select the acquisition.txt and click "Run
    acquisition."
13. After the acquisition, copy the folder to the analysis computer.
14. [Import all MS2 files](../../module_docs/io/data-import.md)
15. Run [Mass detection](../../module_docs/featdet_mass_detection/mass-detection.md) with the
    centroid mass detector and noise level 50-100 (starting point, for MS2 only!)
16. Pair the MS2 spectra to the image features using
    the [Assign MALDI MS2s to features](../../module_docs/featdet_MS2_scan_pairing/ms2_maldi_scan_pairing.md)
    module
17. Annotate using any annotation module in MZmine

{{ git_page_authors }}
