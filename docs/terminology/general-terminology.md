# General terminology

## MS
See [Mass Spectrometry: An Applied Approach, Chapter 3: Basic Definitions](https://doi.org/10.1002/9781119377368.ch3)

### Precursor and fragment ions
The precuror ion (a.k.a. "parent ion") is the ion that dissociates to a smaller fragment ions in a MS/MS experiment. A fragment ion (a.k.a. "daughter ion" or "product ion") is the charged product of an ion dissociation. A fragment ion may be stable itself or may dissociate further to form other charged fragment ions and neutral species of successively lower mass.

### Accurate mass, exact mass and mass accuracy 
The accurate mass is the experimentally-determined mass of an ion measured with an high-resolution mass spectormeter. The exact masss is the calculated mass of an ion based on its elemental formula, isotopic composition and charge state. While the accurate mass is an experimentally-measured quantity, the exact mass is a theretically-calculated quantity. The mass accuracy is defined as the difference between the measured value (accurate mass) and the true value (exact mass). It can be expressed either in absolute (mDa) or relative (ppm) terms.

### Monoisotopic mass
Exact mass of an ion calculated using the mass of the lightest isotope of each element.

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
The total ion current (TIC) chromatogram displays the summed signal intensity (y-axis) over the entire m/z range at any one retention time point (x-axis) in the LC-MS run. The following figure shows a TIC chromatogram of a 9-compounds mixture analysed on LC-MS system.
![TIC](TIC.png)
_Note_. In complex samples, the TIC chromatogram often provides limited information as multiple analytes elute simultaneously, obscuring individual species.

### Base peak chromatogram
The base peak chromatogram (BPC) displays the signal intensity of the most intense maass peak in the MS spectra at any one retention time point (x-axis) in the LC-MS run. The following figure shows the same data as above, visualized in BPI mode.
![BPC](BPC.png)


### Extracted ion chromatogram
The extracted ion chromatogram (EIC) displays the signal intensity of a specific m/z value, within a defined tolerance (e.g. ± 5 ppm), at any one retention time point in the LC-MS run. The following figure shows the EIC of _m/z_ 455.2945 ± 5 ppm (same sample as above).
![EIC](EIC.png)

### Chromatographic deconvolution
Peak overlapping, or co-elution, is a common problem in any chromatographic separation technique. In the case of LC-MS (especially untargeted _omics_ analysis), it is virtually impossible to obtain a full baseline separation for the hundreds (or thousands) of analytes eluted through the column. The process of XXX is called _chromatographic deconvolution_ and is one of the most crucial steps of data processing. TO FINISH

# MZmine-specific terminology

### Masses and Features
In MS data processing, the term _mass_ is normally used to refer to an individual signal in a mass spectrum, which corresponds to an ion detected by the mass spectrometer (see [Mass detection](../module_docs/featdet_mass_detection/mass-detection.md)).

In LC-MS, a _feature_ is defined as a bounded, two-dimensional (_m/z_ and RT dimensions) signal characterized by a pair of _m/z_ and RT values and associated with the detected signal intensity. In the case of LC-IM-MS data, a feature is also characterized by the ion mobility value recorded for the ion (see [LC-MS and LC-IMS-MS data comparison](../workflows/imsworkflow/lc-ms-and-lc-ims-ms-data-comparison.md). MZmine 3 provides a selection of different algorithms for LC-(IM)-MS feature detection, depending on the nature of the MS data (_e.g._ mass accuracy and resolution). However, they all follow the same logic: [EICs](#extracted-ion-chromatogram) are constructed starting from each _m/z_ value in the mass lists and subsequently deconvoluted into individual features (see figure).

![feature creation](feature-creation.png)


### Mass list
In MZmine we call _mass list_ the output of the [mass detection](../module_docs/featdet_mass_detection/mass-detection.md) module. A _mass list_ is a list of _m/z_ values (and corresponding signal intensities) found in each mass spectrum (MS or MSn) of each processed raw data file. 
Every mass spetrum contained in the raw file is processed indivudally and the signals exceeding the set noise threshold are included in the mass list. See [Mass detection](../module_docs/featdet_mass_detection/mass-detection.md) module.

### Feature list
In MZmine, _feature lists_ are the output of the feature detection process (see [Masses and features](#masses-and-features)). The set of detected features in each LC-MS run is stored as a list, hence the name "feature list" (see, for example, [ADAP chromatogram builder](../module_docs/featdet_adap_chromatogram_builder/adap-chromatogram-builder.md) and [Local mimimum resolver](../module_docs/featdet_resolver_local_minimum/local-minimum-resolver.md) for more details). Multiple feature lists can undergo further processing (_e.g._ feature alingment) which results in a tables (often referred to as _feature table_) where samples are arranged in columns, features in rows and each entry contains the signal intensity detected for the corresponding feature, in the corresponding sample.

### Intra- and inter-scan tolerances
To-do

## References
- Pluskal, T., Castillo, S., Villar-Briones, A. & Oresic, M. BMC Bioinformatics 11, 395 (2010). DOI: 10.1186/1471-2105-11-395
- Pluskal, T. et al. Processing Metabolomics and Proteomics Data with Open Software 232–254 (2020). DOI: 10.1039/9781788019880-00232
