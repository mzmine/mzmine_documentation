# GC-EI Feature Alignment

## Description
:material-menu-open: Feature list methods → Alignment → GC aligner

This module aligns GC/EI-MS feature lists by grouping deconvoluted features based on their retention 
times and spectral similarities to ensure accurate alignment of features across different samples.

!!! tip

    GC aligner requires mass spectra to be constructed prior to the alignment (using GC-EI spectral deconvolution).
  
    A typical workflow can be constructed with the [mzwizard](../../wizard.md) by selecting GC-EI-MS.
    See [this page](../../workflows/gcmsworkflow/gcms-workflow.md)for a more detailed description of the workflow.

## Parameters

### Feature lists
  Select the feature lists to be aligned.

### m/z Tolerance (scan-to-scan) 
  Tolerance for m/z values used for spectral similarity matching. 

### Retention time tolerance
  Maximum allowed difference between two retention time values for them to be considered for alignment.

### Weight for RT
  Score for perfectly matching RT values. The RT delta is divided by the RT tolerance and scaled 0-1. The weight then multiplies this score so that higher RT delta gives a penalty. The RT weight shifts the focus on RT or spectral similarity.

### Similarity
  Algorithm to calculate spectral similarity between samples. Pseudo spectra from GC-EI spectral deconvolution will be compared.
  Usually uses the **Composite cosine identity** which is similar to the algorithm in NIST search for GC-EI data.

### Feature list name
  Name for the aligned feature list.

### Original feature list
  Either keep or remove the original feature lists.

!!! tip

    The alignment is performed independtly of the representative feature. Only spectral similarity and retention time are taken into account. The final representative feature will be determined as during the alignment. 

{{ git_page_authors }}

