# General terminology

### Full scan acqusition mode
In full scan acquisition mode, the mass spectrometer acquires [...]. Full scan spectra are often, as well as in MZmine, referred to as MS spectra.

### MS2 data-dependent acqusition mode
In data-dependent acquisition (DDA) schemes, the mass spectrometer detects 'suitable' precursor ions in each MS scan and selects them for fragmentation in consecutive MS2 scans.
- 'Cycle time' and 'topN' acquisition schemes


### Total ion current, Base peak and Extracted ion chromatogram
The total ion current (TIC) chromatogram displays the summed signal intensity (y-axis) over the entire m/z range at any one retention time point (x-axis) obtained from a LC-MS experiment. In complex samples, the TIC chromatogram often provides limited information as multiple analytes elute simultaneously, obscuring individual species.<br>

The base peak chromatogram (BPC) displays the signal intensity of the most intense maass peak in the MS spectra at any one retention time point (x-axis) obtained from a LC-MS experiment.<br>

The extracted ion chromatogram (EIC) displays the signal intensity of the XXX at any one retention time point obtained from a LC-MS experiment.<br>

                                                                          FIGURE


# MZmine-specific terminology

### Masses and Features
Mass is ...individual signal in a mass spectrum, which corresponds to an ion detected by the mass spectrometer.

Feature = Pair of m/z and retention time, normally associated with a signal intensity. The term ‘feature’ is used to emphasize the 3D nature of the signal, as opposed to the term ‘peak’, which is typically used for 2D datasets (e.g., m/z in a mass spectrum).

### Mass list
In MZmine we call 'mass list' the list of m/z values and corresponding signal intensities found in each mass spectrum of the LC-MS run. To do so, each MS (and MS2) spectrum is processed separately to detect individual ion peaks. See [Mass detection](../module_docs/massdetection/mass-detection.md) module.

### Feature list
List of ....

Essentially, [EICs](#total-ion-current-base-peak-and-extracted-ion-chromatogram) are constructed for each m/z value in the mass lists and subsequently deconvoluted into individual features. The latter are then stored as XXX. MZmine 3 provides a selection of diﬀerent algorithms for the EIC construction and deconvolution, depending on the nature of the MS data (e.g. mass accuracy and resolution). See, for example, [ADAP chromatogram builder](../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md) and [Local minimum resolver](../module_docs/localminimumresolver/local-minimum-resolver.md) modules for more details.
