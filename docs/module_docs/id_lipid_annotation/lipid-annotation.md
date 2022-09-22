# **Lipid Annotation**

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search spectra → Lipid annotation**

This module contains methods to search for lipids in the feature lists. Potential lipids will be annotated according to their accurate mass on MS^1^ level. 

If MS/MS data is available, an identification on fatty acid residue level is also possible. MS/MS rules were derived from various sources [[2-4](#references)] or from MS/MS experiments performed in the [Hayen lab](https://www.uni-muenster.de/Chemie.ac/en/hayen/) (University of Münster, Germany)

:warning: If you use the Lipid Annotation Module, please cite the MZmine paper and the articles from the [references](#references) section.

## **References**

!!! quote ""

    1. Korf, A., Jeck, V., Schmid, R., Helmer, P. O., & Hayen, H. (2019). Lipid Species Annotation at Double Bond Position Level with Custom Databases by Extension of the MZmine Open-Source Software Package. Analytical chemistry, 91(8), 5098-5105. DOI: <a>10.1021/acs.analchem.8b05493</a>

    2. LipidBlast. Kind, T., Liu, K. H., Lee, D. Y., DeFelice, B., Meissen, J. K., & Fiehn, O. (2013). LipidBlast in silico tandem mass spectrometry database for lipid identification. Nature methods, 10(8), 755. <a>10.1038/nmeth.2551</a>

    3. MoNA <a>https://mona.fiehnlab.ucdavis.edu/</a>

    4. LipidMatch. Koelmel, J. P. et al. (2017). LipidMatch: an automated workflow for rule-based lipid identification using untargeted high-resolution tandem mass spectrometry data. BMC bioinformatics, 18(1), 331. DOI: <a>10.1186/s12859-017-1744-3</a>

## **Parameters**

#### **Lipid classes**

Selection of lipid classes to consider for annotation based on the backbone.

#### **Number of carbon in chains**

Set the number of carbon atoms in chains.

#### **Number of double bonds**

Set the number of double bonds in chains.

#### **m/z tolerance MS1 level**

Enter m/z tolerance for exact mass database matching on MS1 level

#### **Search for lipid class-specific fragments in MS/MS spectra**

Choose if you want to search for lipid class specific fragments in the MS/MS spectra. 

To see which lipid class has a MS/MS library check out the database table.

#### **Search for custom lipid class**

If chosen, the user can add their own custom class that will be used for further search. This feature allows the user to build any possible lipid, based on the already implemented lipids. This also allows the annotation of lipid derivatization products. Entered modifications can be exported and/or imported using the buttons on the right side.

#### **Show database**

By clicking the button "Show database" at the bottom of the window, the user can browse through a database table which holds the information of the created lipid database.

[//]: # (TODO Leave commented until bug is fixed)
[//]: # (All lipids are displayed in two Kendrick mass plots &#40;KMD CH2 left, KMD H right&#41;. Lipids that interfere in the selcted m/z window are marked yellow, isobaric lipids are marked red. The others are displayed green.)

[//]: # (TODO Add the plots)


## **Results description**

Peaks will be annotated as potential lipids by setting its peak identity. Always check for multiple assignments and compare the status with the database table and Kendrick plots! The comment holds information on the utilized ionization method, mass accuracy and MS/MS annotation. An MS/MS annotation will be added if MS/MS data was acquired and fragmentation information is listed in the database. More MS/MS data will be added in the future.