# Split aligned feature list

This module can be used to split an aligned feature list into separate feature lists, either on a
per-sample basis or on a metadata group basis.

The split feature tables will maintain the feature IDs of the aligned feature list. This makes this
module useful for processing data where e.g. report generation or spectral library machting is
required on a per-sample basis, without having to rely on post-alignment outside of mzmine, since 
all previously aligned features have the same ID.

## Parameters

#### Feature lists

Select the aligned feature list that shall be split.

#### Split by metadata group

If disabled, each raw data file in the aligned feature list will be placed in an individual feature
list.

If enabled, the aligned feature list will be split by the selected group in the metadata table. Each
metadata group will revieve its own feature list.
