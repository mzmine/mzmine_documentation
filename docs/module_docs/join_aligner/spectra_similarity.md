#### Spectral m/z tolerance
Spectral m/z tolerance is used to match all signals between spectra of two compared raw files.

#### MS level
 MS level of scans that should be compared. It can be 1 for MS1 or 2 for MS2 level.

#### Compare spectra similarity

 1. **Weighted dot-product cosine** - used to determine the similarity between two spectra (usually library and query spectra).This option is used for MS2 level.


 2. **Composite dot-product identity** - used to determine the similarity between two spectra (usually library and query spectra). Especially useful for very reproducible generation of spectra (GC-EI-MS). Takes into account the relative intensities of neighbouring signals in the two spectra. This option is used for MS1 level.

 Additional setup of spectra similarity comparison enables modification of the following parameters:

#### Weights
Weights for the m/z and intensity values. Usually, MassBank is used, in which higher m/z values contribute more to the cosine similarity calculation.

#### Minimum cos similarity
Minimum cosine similarity for a match between compared spectra.

#### Handle unmatched signals
Usually, **keep all and match to zero** is used, which will take all signals into account, and the unmatched ones will decrease the cosine similarity. 
