# **Spectral deconvolution: Multivariate Curve Resolution**

:construction: This module is being updated, which might affect its functionality

## **Description**

This ADAP-based method performs Spectral Deconvolution of detected peaks. It finds components (compounds, analytes, etc.) and determines their model peaks and fragmentation mass spectra.

The spectral deconvolution uses both constructed chromatograms and detected peaks. The feature list of constructed chromatograms is specified by selecting Specific peak lists for parameter Chromatograms, clicking on the ellipsis button, and choosing one or more lists with chromatograms in the popup window. The list of detected peaks is specified by selecting Specific peak lists for parameter Peaks, clicking on the ellipsis button, and choosing one or more lists with detected peaks in the popup window.


The Spectral Deconvolution consists of **two steps**:

1. Entire retention time interval is split into deconvolution windows so that

   - Peaks produced by the same component or by coeluting components belong to the same deconvolution window,
   - Number of peaks in deconvolution window is significantly smaller than the total number of peaks.

   The deconvolution windows are displayed in the top plot of the preview, where small dash lines denote peaks in the (retention time, m/z)-plane, and peaks belonging to one deconvolution window have the same color. The vertical sequences of peaks usually mark the presence of one or several compounds, so it is important that those peaks are assigned to the same deconvolution window, i.e. they have the same color on the plot. The deconvolution windows are controlled by the **Deconvolution window width** parameter.

   :warning: If deconvolution windows contain too many peaks, it will significantly slow down the spectral deconvolution computations, so the deconvolution windows should be as short (in the retention time domain) as possible.
2. The algorithm infers the number of components in each deconvolution window and construct their model peaks and fragmentation spectra. The inferred number of components is controlled by three parameters: **Retention time tolerance (min)**, **Minimum Number of Peaks**, and **Adjust Apex Ret Times**.

## **Parameters**

**Deconvolution window width (min)** 

The algorithm will produce deconvolution windows so that their width (in retention time domain) does not exceed the value of this parameter.

**Retention time tolerance (min)**

The smallest time-gap between any two components.

**Minimum Number of Peaks**

The smallest number of detected peaks to form a component.

**Adjust Apex Ret Times**

If **false**, then the retention time of each detected peak is determined by the retention time of its highest data point. 
If **true**, then the retention time of each detected peak is determined by fitting a parabola into the top half of that peak.

## **References**
- Pluskal, T., Castillo, S., Villar-Briones, A. & Oresic, M. MZmine 2: Modular framework for processing, visualizing, and analyzing mass spectrometry-based molecular profile data. _BMC Bioinformatics_ (2010). DOI: <a>10.1186/1471-2105-11-395</a>
- Smirnov A, Jia W, Walker D, Jones D, Du X: ADAP-GC 3.2: Graphical Software Tool for Efficient Spectral Deconvolution of Gas Cromatography—High-Resolution Mass Spectrometry Metabolomics Data. J. Proteome Res 2017, DOI: <a>10.1021/acs.jproteome.7b00633</a>
- Aleksandr Smirnov, Yunping Qiu, Wei Jia, Douglas I. Walker, Dean P. Jones, Xiuxia Du. ADAP-GC 4.0: Application of Clustering-Assisted Multivariate Curve Resolution to Spectral Deconvolution of Gas Chromatography–Mass Spectrometry Metabolomics Data. Analytical Chemistry 2019, 91 (14) , 9069-9077. <a>https://doi.org/10.1021/acs.analchem.9b01424</a>