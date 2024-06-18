!!! danger

    This module is currently under maintenance

# **ADAP Aligner (GC)**

## **Description**

:material-menu-open: **Feature list methods → Alignment → ADAP aligner (GC)**

This alignment algorithm has been developed as part of ADAP-GC v1.0, Automatic Data Analysis Pipeline for processing GC-MS metabolomics data.

ADAP Aligner aligns features based on their mass spectra and retention time similarity. Unlike **Join Aligner** (which aligns peaks across all samples, using their m/z and retention time similarity), ADAP Aligner uses mass spectra and retention time to detect similar features in each sample and align them together. In fact, this algorithm is similar to **Hierarchical Aligner (GC)**, but it uses a different clustering method.

Similarity between two features $f1$ and $f2$ is calculated by the following score:

$$S(f1, f2) = w*S_{time}(f1, f2) + (1 - w)*S_{spec}(f1, f2)$$

where $S_{time}(f1, f2)$ is the relative retention time difference between two features, $S_{spec}(f1, f2)$ is the spectrum similarity between two features.

For more details, see reference [[1](#references)].


### **Requirements**

ADAP Aligner requires mass spectra to be constructed prior to the alignment (e.g. using Spectral Deconvolution).

A typical workflow can be as following:

- "Raw data methods → Raw data import" to import raw data files
- "Raw data methods → Mass detection" to detect masses in the raw data

[//]: # (TODO Check if old version is properly "translated" into the new one)

[//]: # ([//]: # &#40;- Old version)

[//]: # (Raw datamethods / Peak detection / ADAP Chromatogram builder builds extracted-ion chromatograms)

[//]: # (Peak list methods / Peak deteciton / Chromatogram deconvoltion detects peaks &#40;features&#41; in each chromatogram&#41;)

- "Feature detection → ADAP Chromatogram builder" to build extracted-ion chromatograms
- "Feature detection → Chromatogram resolving → ADAP Resolver" to detect peaks (features) in each chromatogram
- "Feature list methods → Spectral deconvolution (GC) → Multivariate Curve Resolution" to combine the detected peaks (features) into analytes and builds pure fragmentation mass spectra for each analyte
- "Feature list methods → Alignment → ADAP Aligner (GC)" to align the analytes produced by the previous step
- "Feature list methods → Export feature list → MSP file (ADAP)" to export fragmentation mass spectra into MSP format

## **References**

!!! quote " "

    1. Jiang, W.; Qiu, Y.; Ni, Y.; Su, M.; Jia, W.; Du, X.: An automated data analysis pipeline for GC-TOF-MS metabonomics studies. Journal of proteome research 2010, 9 (11), 5974-81. DOI: <a>10.1021/pr1007703</a>

## **Parameters**

#### **Min confidence (between 0 and 1)** 

A fraction of the total number of samples. An aligned feature must be detected at least in several samples. This parameter determines the minimum number of samples where a feature must be detected. The default value is 0.7, so an aligned feature must be observed at least in 70% of all samples.

#### **Retention time tolerance** 

The maximum allowed retention time difference between aligned features from different samples.

#### **m/z tolerance** 

The maximum m/z difference, when two peaks from different mass spectra are considered equal.

#### **Score threshold (between 0 and 1)** 

The minimum value of the similarity function $S(f1, f2)$ required for features to be aligned together. The default value is 0.75.

#### **Score weight (between 0 and 1)** 

The weight $w$ that is used in the similarity function $S(f1, f2)$. The default value is 0.1.

#### **Retention time similarity** 

A method used for calculating the retention time similarity. The retention time difference (fast) is preferred method.

{{ git_page_authors }}