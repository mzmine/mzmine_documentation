# **Baseline correction**

## **Description**

:material-menu-open: **Raw data methods → Raw data filtering → Baseline correction**

This module performs baseline correction on raw data files. It is designed to **compensate for gradual shifts** in the chromatographic baseline by detecting the baseline and then subtracting it from the raw data intensity values. 

The module proceeds as follows for each raw data file passed to it:

- The full range of m/z values present in the raw data is divided into a series of bins of a specified width (see m/z bin width).
- For each bin a chromatogram is constructed from the raw data points whose m/z values fall within the bin. This chromatogram may be either the [base peak chromatogram](../../terminology/general-terminology.md#base-peak-chromatogram) or [total ion count (TIC) chromatogram](../../terminology/general-terminology.md#total-ion-current-chromatogram). 
- The raw intensity values of each data point in a bin are corrected by subtracting the bin's baseline. Subtraction of baseline intensity values proceeds according to the type of chromatogram used to determine the baseline.

    If the **base peak chromatogram** was used then the corrected intensity values are calculated as follows:

    $$I_{corr}=max(0,I_{orig}-I_{base})$$

    If the **TIC chromatogram** was used then the corrected intensity values are calculated as follows:
    
    $$I_{corr}=max(0,I_{orig}*(1-I_{base}/I_{max}))$$

    where $I_{orig}$, $I_{base}$, $I_{max}$, and $I_{corr}$ are the original, baseline, maximum and corrected intensity values, respectively, for a given scan and m/z bin. 

    If $I_{base}$ is less or equal to zero then no correction is performed, i.e. $I_{corr}=I_{orig}$.

- A new raw data file is generated from the corrected intensity values.

## **Parameters**

#### **Filename suffix**

The text to append to the name of the baseline corrected raw data file.

#### **Chromatogram type**

TIC: total ion count, i.e. summed intensities per scan, or

Base peak intensity: maximum intensity per scan.

#### **MS-level**

MS level to which to apply correction. Select "0" for all levels.

#### **Use m/z bins**

Baselines can be calculated and data points corrected per m/z bin or to the entire raw data file. If no binning is performed then a single chromatogram is calculated for the entire raw data file and its baseline used to correct the full data file. No binning is very quick but much less accurate and so is only suitable for fine-tuning the smoothing and asymmetry parameters.

#### **m/z bin width**

The width of the m/z bins if binning is performed (see use m/z bins). Smaller bin widths result in longer processing times and greater memory requirements. Avoid values below 0.01.

#### **Correction method**

The width of the m/z bins if binning is performed (see use m/z bins). Smaller bin widths result in longer processing times and greater memory requirements. Avoid values below 0.01.

#### **R engine**

This option allows you to choose between two Java libraries to communicate with R - RServe or RCaller.

#### **Remove source file after baseline correction**

Whether to remove the original raw data file once baseline correction is complete.

## **Correction methods** 

More information on correction methods is available in [CRAN decription of baseline package](https://cran.r-project.org/web/packages/baseline/) 

### **Asymmetric Baseline Corrector**

This corrector estimates a baseline using asymmetric least squares and subtracts it from the data.

#### **Additional parameters**

**Smoothing**

The smoothing factor (>=0), generally ranges from 1E5 to 1E8. The larger this factor is, the smoother the baseline.

**Asymmetry**

Default value is 1E-3.
The weight (0 <= p <= 1) for points above the trend line, whereas 1-p is the weight for points below it. Naturally, p should be small for estimating baselines.

### **Rolling Ball Corrector**

The corrector estimates a trend based on the **Rolling Ball algorithm**, and subtracts it from the raw data intensity values.
(Ideas from **Rolling Ball algorithm for X-ray spectra by M.A.Kneen and H.J. Annegarn**. Variable window width has been left out).

#### **Additional parameters**

**wm (number of scans)**

Width of local window for minimization/maximization (in number of scans).

**ws (number of scans)**
Width of local window for smoothing (in number of scans).

### **Peak Detection Baseline Corrector**

The corrector estimates a trend based on the Peak Detection algorithm, and subtracts it from the raw data intensity values.
Peak detection is done in several steps sorting out real peaks through different criteria. Peaks are removed from spectra and minimums and medians are used to smooth the remaining parts of the spectra. (A translation from **Kevin R. Coombes et al.'s MATLAB code** for detecting peaks and removing baselines).

#### **Additional parameters**

**left (number of scans)**

Smallest window size for peak widths (in number of scans).

**right (number of scans)**

Largest window size for peak widths (in number of scans).

**lwin (number of scans)**

Smallest window size for minimums and medians in peak removed spectra (in number of scans).

**rwin (number of scans)**

Largest window size for minimums and medians in peak removed spectra (in number of scans).

**snminimum**

Minimum signal to noise ratio for accepting peaks.

**mono**

Monotonically decreasing baseline if ‘mono’ > 0.

**multiplier**

Internal window size multiplier.

### **Rubber Band Corrector**

The corrector estimates a trend based on the Rubber Band algorithm (which determines a convex envelope for the spectra - underneath side), and subtracts it from the raw data intensity values.

#### **Additional parameters**

**noise**

Ignored if **"auto noise"** is checked. Noise level to be taken into account.

**auto noise**

Determine noise level automatically (from lower intensity scan).

**df**
Degree of freedom.

**spline**

Logical indicating whether the baseline should be an interpolating spline through the support points or piecewise linear.

**bend factor**

Does nothing if equals to zero. Helps fitting better with low **"df"**. 

:material-lightbulb: Try starting with value around 5E4.

### **Local Minima + LOESS Corrector**

The corrector estimates a trend based on Local Minima + LOESS (smoothed low-percentile intensity), and subtracts it from the raw data intensity values.

#### **Additional parameters**

**method**

"**loess**" (smoothed low-percentile intensity) or "**approx**" (linear interpolation).

**bw**

The bandwidth to be passed to loess.

**breaks**

Number of breaks set to m/z values for finding the local minima or points below a certain quantile of intensities; breaks -1 equally spaced intervals on the log(m/z) scale.

**break width (number of scans)**

Width of a single break. Usually the maximum width (in number of scans) of the largest peak.

:warning: Overrides **"breaks"** value. 

**qntl**

If 0, find local minima; if >0 find intensities < qntl*100th quantile locally.

## **Requirements**

:warning: This module relies on the local installation of R statistical computing software and several R packages.

**Quick install** 

The whole thing can be setup as follows by running the following code in R:

	install.packages(c("Rserve", "ptw", "baseline", "hyperSpec"))
	source("http://bioconductor.org/biocLite.R")
	biocLite("PROcess")


**Details**

- Rserve (All correctors): provides an interface between MZmine and R. To install Rserve from CRAN packages run R and enter:

      install.packages("Rserve")

- ptw (Asymmetric corrector): parametric time-warping provides the asymmetric least-squares implementation. To install ptw run R and enter:

      install.packages("ptw")

- baseline (RollingBall and PeakDetection correctors): provides a trend based on "Rolling Ball" and "Peak Detection" algorithms implementation. To install baseline run R and enter:
      
      install.packages("baseline")

- hyperSpec (RubberBand corrector): provides a trend based on "Rubber Band" algorithm (which determines a convex envelope for the spectra) implementation. To install hyperSpec run R and enter:

      install.packages("hyperSpec")

- PROcess (Local Minima + LOESS corrector): provides the local minima search + LOESS (smoothed low-percentile intensity) implementation. To install PROcess run R and enter:

      source("http://bioconductor.org/biocLite.R")
      biocLite("PROcess")

## **References**

[1]	Boelens, H.F.M., Eilers, P.H.C., Hankemeier, T. (2005) "Sign constraints improve the detection of differences between complex spectral data sets: LC-IR as an example", Analytical Chemistry, 77, 7998 – 8007.	

[2]	Rserve "A TCP/IP server which allows other programs to use facilities of R"

<a>https://rforge.net/Rserve</a>.

TODO Add images for each type of baseline correction