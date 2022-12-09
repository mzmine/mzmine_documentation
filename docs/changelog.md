# Changelog

## MZmine 3.3.0 - Released 10.12.2022

Main changes:

- Factor of lowest mass detector (robinschmid)
- MZmine now licensed under MIT license
- Fix GCMS workflow (asmirn1, tnguy271)
- Isotope filtering fixes (robinschmid, SteffenHeu)
- Update TDF import (SteffenHeu)
- 3D Massvoltammogram visualisation (WesMark)
- Batch mode updates (robinschmid)
- HILIC preset for wizard (SteffenHeu)
- Batch spectral library generation from feature list (robinschmid, SteffenHeu)
- MS2 spectra denormalisation (robinschmid)
- MS/MS quality scores (SteffenHeu, robinschmid)
- Alignment scores (robinschmid)
- Updated targeted feature detection (SteffenHeu)
- Fixed visualizations & link to online documentation (omokshyna)
- new themes (SteffenHeu)
- MSn peak picking module fixed (SteffenHeu, robinschmid)
- MetaboAnalyst export fixed (robinschmid)
- Fix NIST MS Search (Kevin-Murray)

Full changelog:

| Change                                                                  | Contributor   |
|-------------------------------------------------------------------------|---------------|
| Remove beta from version                                                | robinschmid   |
| Lowest factor mass detecotr, keep >0                                    | robinschmid   |
| Add warning log and icon for incorrectly centroided files               | robinschmid   |
| Update .mailmap                                                         | Tomas Pluskal |
| Removed offline help from feature filtering                             | omokshyna     |
| Create codeql-analysis.yml                                              | SteffenHeu    |
| Feature list methods help fix                                           | omokshyna     |
| Fix #888 concurrent mod in JFreeChart paint                             | robinschmid   |
| update default ms2 grouping selection (true = default)                  | SteffenHeu    |
| Fix bug in advanced data import = noise level was MS1 for both          | robinschmid   |
| add CompDbAnnotation -> CommentType to the feature list                 | SteffenHeu    |
| Grid mass fix                                                           | omokshyna     |
| Patch out of bound in IsotopeFinder                                     | robinschmid   |
| add removeRedundant isotopes to rows filter                             | SteffenHeu    |
| Resolvers help fix                                                      | omokshyna     |
| Fix no data in tdf                                                      | SteffenHeu    |
| Ransac aligner preview fix                                              | omokshyna     |
| Add online help for Alignment and Normalization modules                 | omokshyna     |
| Varun plot bug fix                                                      | varunotelli   |
| Fix preview in Spectral Deconvolution (MCR and Hierarchical Clustering) | asmirn1       |
| Enable preview                                                          | robinschmid   |
| fix shoulder peak filter not keeping file selection                     | SteffenHeu    |
| Fix and rename MultiMsMsVisualizer --> SpectraStackVisualizer           | robinschmid   |
| Massvoltammogramme                                                      | WesMark       |
| fix MobilityScanMering always summing                                   | SteffenHeu    |
| Frame visualiser                                                        | SteffenHeu    |
| Remove the Swing fontchooser dependency                                 | tomas-pluskal |
| License change to MIT license                                           | tomas-pluskal |
| Tdfsdk 2 21                                                             | SteffenHeu    |
| Annotations & Visualization online help update                          | omokshyna     |
| fix concurrent mod exception in ImsExpanderTask                         | SteffenHeu    |
| Bug fix - getScanNumbers                                                | Kevin-Murray  |
| Advanced batch mode                                                     | robinschmid   |
| Fix advanced batch mode                                                 | robinschmid   |
| Fix some issues in Spectral Deconvolution / Hierarchical Clusters #925  | asmirn1       |
| Empty scans handling                                                    | omokshyna     |
| Update datatype loadsafe                                                | SteffenHeu    |
| Update manual picker                                                    | SteffenHeu    |
| fix class cast in MirrorChartFactory                                    | SteffenHeu    |
| fix selected mz mobilogram and chrom in IMSRawDataOverviewPane          | SteffenHeu    |
| Update normalization                                                    | SteffenHeu    |
| Feature intensity plot                                                  | omokshyna     |
| add option to clear specific annotations                                | SteffenHeu    |
| Start dia msms impl                                                     | SteffenHeu    |
| Batch library generation                                                | robinschmid   |
| Merge minrelative                                                       | SteffenHeu    |
| fix wring xml name                                                      | SteffenHeu    |
| add ims type supported to Isofinder and rowsfilter                      | SteffenHeu    |
| fix adap error spam                                                     | SteffenHeu    |
| add DataType#getDefaultVisibility                                       | SteffenHeu    |
| add multiple precursor mzs to scan table                                | SteffenHeu    |
| Msms quality                                                            | SteffenHeu    |
| resolved alignment issue                                                | tnguy271      |
| Lib export refinement                                                   | SteffenHeu    |
| Distance of MS2 to apex                                                 | robinschmid   |
| add new simple learner module                                           | robinschmid   |
| FragmentScanSelection to select MSn spectra (merged and single)         | robinschmid   |
| pass actual file to ims expander                                        | SteffenHeu    |
| dont merge msms during export unless user wants to                      | SteffenHeu    |
| Fixed issue where selected scan is null after normalization             | tnguy271      |
| add spectra merging to ims raw data overview                            | SteffenHeu    |
| New GNPS json parser                                                    | robinschmid   |
| fix issue in alignment task where selected scans is null                | tnguy271      |
| Change Range to window (float) for precursor isolation window           | robinschmid   |
| Mass detection status                                                   | omokshyna     |
| MGF file format option for Batch and Single library export              | robinschmid   |
| Export all data types to mgf                                            | robinschmid   |
| Fix multichoice parameter                                               | robinschmid   |
| Minor fixes                                                             | omokshyna     |
| Added mass detection for IMS data overview                              | omokshyna     |
| Update to JDK19, keep javafx16                                          | robinschmid   |
| Fix chart graphics export clone issue                                   | robinschmid   |
| Update wizard                                                           | SteffenHeu    |
| Tag modules from the wizard as IMS ready                                | SteffenHeu    |
| Fixes                                                                   | SteffenHeu    |
| Denormalize MSn spectra                                                 | robinschmid   |
| add selected scans to MsnPeakPickingTask                                | SteffenHeu    |
| Alignment scores after alignment                                        | robinschmid   |
| Update image builder parameters                                         | SteffenHeu    |
| Themeparameter                                                          | SteffenHeu    |
| Targeted update                                                         | SteffenHeu    |
| Clean up alignment scores and FeatureListUtils                          | robinschmid   |
| More consistent theme, fix lipid class parameter                        | SteffenHeu    |
| Compound annotation score uses alignment score                          | robinschmid   |
| Fix metaboanalyst                                                       | robinschmid   |
| Tdf and tsf date import                                                 | SteffenHeu    |
| version 3.3.0                                                           | robinschmid   |
