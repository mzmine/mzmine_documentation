# **Mass detection**
The mass detection module generates a [mass list](../../terminology/general-terminology.md#mass-list) (_i.e._ list of m/z values and correspoinding signal intensities) for each scan, in each raw data file. During the mass detection, profile raw data are centroided and a noise filtering is performed based on a user-defined threshold (see [Setting the noise level](#setting-the-noise-level)).

**Raw data methods → Mass detection → Mass detection**
![Mass detection](mass_detection_main.png)

**Raw data files**: To-do 

**Scans**: To-do 

**Scan types (IMS)**: To-do 

**Mass detector**: several mass detection algorithms are available and can be selected in the drop-down menu. The choice will depends on the raw data characteristics (profile/centroided, mass resolution, etc.). For already-centroided data the _Centroid_ algortihm must be used, while the other algorithms are suitable for profile raw data. The _Exact mass_ algorithm is recommended for HRMS data. <br><br>


### **Setting the noise level**
The threshold for the noise filtering can be set by hitting thee _Setup_ button next to the _Mass detector_ field. The following dialog box will open up:
![Noise level](noise_level.png)
The noise threshold can be entered either in standard or scientific notation. By checking the _Show preview_ box, an interactive visualization panel will open to help the user to adjust the noise level (see also [How do I determine the noise level in my data?](#how-do-i-determine-the-noise-level-in-my-data)). The red dots denotes the mass signals included in the mass list according to the set noise threshold. Different data files and scan numbers can be visualized using the corresponding drop-down menus. 

**Detect isotope signals below noise level**: To-do <br><br>

### **How do I determine the noise level in my data?**
To-do.
The detector noise is usually determined by a lot of signals of the same intensity.



<br><br><br><br>


#### **Detect isotope signals below noise level**
**Centroid** and **exact mass** detectors provide an additional parameter called **detect isotope signals below noise level**. This option allows to include additional peaks, corresponding to isotope masses, in the resulting mass list. By clicking the **Setup** button, you can specify the following parameters.



##### Chemical elements

Chemical elements which isotopes will be considered (select from the periodic table).

##### M/z tolerance

The maximum allowed difference between theoretical isotope m/z and measured m/z present in the scan to be considered the same.

##### Maximum charge of isotope m/z

Should be a positive integer (further denoted as K). All peaks having m/z equal to (up to m/z tolerance) theoretical isotope mass (any isotope of any specified chemical element) divided by any of 1, 2, ..., K will be included in the mass list. The default value is 1.

## LC-IMS-MS data
To-do

Native Bruker raw data is already centroided, therefore the centroid mass detector should be used. Waters .mzML raw data might come as profile data, which requires a different mass detector
such as **exact mass**.

Note that a mobility scan should be selected to determine the noise level.
However, the same noise level will be applied to frames, too.

