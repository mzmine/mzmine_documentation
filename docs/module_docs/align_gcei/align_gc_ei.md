# GC-EI Feature Alignment

## Description
:material-menu-open: Feature list methods → Alignment → GC aligner

This module aligns GC/EI-MS feature lists by grouping deconvoluted features based on their retention times and spectral similarities to ensure accurate alignment of features across different samples.

!!! warning

    Before using this module run GC-EI spectral deconvolution 

## Parameters

### Feature Lists
  Select the feature lists to be aligned.

### m/z Tolerance  
  Tolerance for m/z values used for spectral similarity matching. 

### Retention Time Tolerance (min)  
  Maximum allowed difference between two retention time values for them to be considered for alignment.

### Weight for RT
  Score for perfectly matching RT values. The RT delta is divided by the RT tolerance and scaled 0-1. The weight then multiplies this score so that higher RT delta gives a penalty. The RT weight shifts the focus on RT or spectral similarity.

### Similarity Function
  Algorithm to calculate spectral similarity between samples. Pseudo spectra from GC-EI spectral deconvolution will be compared. 

### Feature List Name
  Name for the aligned feature list.

### Handle Original Feature List
  If checked, the original feature list will be removed.

!!! tip

    The alignment is performed independtly of the representative feature. Only spectral similarity and retention time are taken into account. The final representative feature will be determined as during the alignment. 

{{ git_page_authors }}

