# General terminology

## MS
See https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119377368.ch3

### Parent ion
Todo. A.k.a. precursor ion

### Fragment ion 
Todo. A.k.a. daughter ion, product ion

### Mass range
Todo

### Mass accuracy 
Todo. Can be expressed either in absolute (mDa) or relative (ppm) terms

### Mass resolution 
Todo. Often called/expressed as mass resolvin power

### Full scan acqusition mode
Todo

### Data-dependent acqusition mode
In data-dependent acquisition (DDA) schemes, the mass spectrometer detects 'suitable' precursor ions in each MS scan and selects them for fragmentation in consecutive MS2 scans.<br>
Todo:'Cycle time' and 'topN' acquisition schemes

### Data-independent acqusition mode
Todo


## LC-MS
### Total ion current chromatogram
The total ion current (TIC) chromatogram displays the summed signal intensity (y-axis) over the entire m/z range at any one retention time point (x-axis) in the LC-MS run. In complex samples, the TIC chromatogram often provides limited information as multiple analytes elute simultaneously, obscuring individual species.

### Base peak chromatogram
The base peak chromatogram (BPC) displays the signal intensity of the most intense maass peak in the MS spectra at any one retention time point (x-axis) in the LC-MS run.<br>

### Extracted ion chromatogram
The extracted ion chromatogram (EIC) displays the signal intensity of a specific m/z value, wthin a defined tolerance (e.g. ±5 ppm), at any one retention time point in the LC-MS run.<br>

                                                                          FIGURE


# MZmine-specific terminology

### Masses and Features
Mass is ...individual signal in a mass spectrum, which corresponds to an ion detected by the mass spectrometer.

In LC-MS, a 'feature' is defined as a pair of m/z and retention time, normally associated with a signal intensity.

The term ‘feature’ is used to emphasize the 3D nature of the signal, as opposed to the term ‘peak’, which is typically used for 2D datasets (e.g., m/z in a mass spectrum).


In this context, a emph{feature} is defined as the two-dimensional integration with respect to retention time (RT) and mass-over-charge (m/z) of the eluting signal belonging to a single charge variant of a measurand (e.g., a peptide). Features are characterized by attributes like average mass-to-charge ratio, centroid retention time, intensity, and quality. 


### Mass list
In MZmine we call 'mass list' the list of m/z values and corresponding signal intensities found in each mass spectrum of the LC-MS run. To do so, each MS (and MS2) spectrum is processed separately to detect individual ion peaks. See [Mass detection](../module_docs/massdetection/mass-detection.md) module.

### Feature list
List of ....

Essentially, [EICs](#total-ion-current-base-peak-and-extracted-ion-chromatogram) are constructed for each m/z value in the mass lists and subsequently deconvoluted into individual features. The latter are then stored as XXX. MZmine 3 provides a selection of diﬀerent algorithms for the EIC construction and deconvolution, depending on the nature of the MS data (e.g. mass accuracy and resolution). See, for example, [ADAP chromatogram builder](../module_docs/adapchromatogrambuilder/adap-chromatogram-builder.md) and [Local minimum resolver](../module_docs/localminimumresolver/local-minimum-resolver.md) modules for more details.

![feature creation](feature-creation.png)

## References
- Pluskal, T., Castillo, S., Villar-Briones, A. & Oresic, M. BMC Bioinformatics 11, 395 (2010). https://doi.org/10.1186/1471-2105-11-395
- Pluskal, T. et al. Processing Metabolomics and Proteomics Data with Open Software 232–254 (2020). https://doi.org/10.1039/9781788019880-00232
