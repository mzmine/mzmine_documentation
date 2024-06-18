!!! danger

    This module is currently under maintenance / deprecated / etc.

# **Spectral deconvolution: Multivariate Curve Resolution**

!!! danger

    This module is not supported on macOS

## **Description**

:material-menu-open: **Feature list methods → Spectral deconvolution (GC) → Multivariate Curve Resolution**

This **ADAP-based method** performs Spectral Deconvolution of detected features. It finds components (compounds, analytes, etc.) and determines their model feature and pseudo fragmentation mass spectra.

The spectral deconvolution uses both constructed chromatograms and detected features. The feature list of constructed chromatograms is specified by selecting specific feature lists for parameter chromatograms and choosing one or more lists with chromatograms in the popup window. The list of detected peaks is specified by selecting Specific peak lists for parameter Peaks, clicking on the ellipsis button, and choosing one or more lists with detected peaks in the popup window.


The Spectral Deconvolution consists of **two steps**:

1. Entire retention time interval is split into deconvolution windows so that

   - Features produced by the same component or by coeluting components belong to the same deconvolution window,
   - Number of features in deconvolution window is significantly smaller than the total number of features.

   The deconvolution windows are displayed in the top plot of the preview, where small dash lines denote features in the (retention time, m/z)-plane, and features belonging to one deconvolution window have the same color. The vertical sequences of features usually mark the presence of one or several compounds, so it is important that those features are assigned to the same deconvolution window, i.e. they have the same color on the plot. The deconvolution windows are controlled by the **Deconvolution window width** parameter.

   :warning: If deconvolution windows contain too many features, it will significantly slow down the spectral deconvolution computations, so the deconvolution windows should be as short (in the retention time domain) as possible.
2. The algorithm infers the number of components in each deconvolution window and construct their model feature and pseudo fragmentation spectra. The inferred number of components is controlled by three parameters: **Retention time tolerance (min)**, **Minimum Number of Peaks**, and **Adjust Apex Ret Times**.

## **References**

!!! info

     1. Robin Schmid, Steffen Heuckeroth, Ansgar Korf et al. Integrative analysis of multimodal mass spectrometry data in MZmine 3. Nature Biotechnology (2023), doi:10.1038/s41587-023-01690-2 

     2. Smirnov A, Jia W, Walker D, Jones D, Du X: ADAP-GC 3.2: Graphical Software Tool for Efficient Spectral Deconvolution of Gas Cromatography—High-Resolution Mass Spectrometry Metabolomics Data. J. Proteome Res 2017, DOI: <a>10.1021/acs.jproteome.7b00633</a>

     3. Aleksandr Smirnov, Yunping Qiu, Wei Jia, Douglas I. Walker, Dean P. Jones, Xiuxia Du. ADAP-GC 4.0: Application of Clustering-Assisted Multivariate Curve Resolution to Spectral Deconvolution of Gas Chromatography–Mass Spectrometry Metabolomics Data. Analytical Chemistry 2019, 91 (14) , 9069-9077. <a>10.1021/acs.analchem.9b01424</a>

## **Parameters**

#### **Deconvolution window width (min)** 

The algorithm will produce deconvolution windows so that their width (in retention time domain) does not exceed the value of this parameter.

#### **Retention time tolerance (min)**

The smallest time-gap between any two components.

#### **Minimum number of features**

The smallest number of detected features to form a component.

#### **Adjust Apex Ret Times**

If **false**, then the retention time of each detected peak is determined by the retention time of its highest data point. 
If **true**, then the retention time of each detected peak is determined by fitting a parabola into the top half of that peak.

{{ git_page_authors }}