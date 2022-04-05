# **Welcome to the MZmine 3 wiki!**
MZmine 3 is an open-source and platform-independent software for mass spectrometry (MS) data processing and visualization. It enables large-scale metabolomics and lipidomics research by spectral preprocessing, feature detection, and various options for compound identification, including spectral library querying and creation.

Since the introduction of MZmine 2 in 2010, the project has matured into a into a community-driven, highly collaborative platform and its functions continue to expand based on the MS community needs and feedbacks. This progress was made possible by the invaluable contribution of many [developers](https://github.com/mzmine/mzmine3/graphs/contributors) from research labs distributed all over the world.

Want to get started with MZmine 3? Check out our [getting started](getting_started.md) page!
 
---
## **What's new compared to MZmine 2?**
MZmine 3 comes with a redesigned and fully customizable [GUI](main-window-overview.md) based on the JavaFX technology that allow an interactive visualization and validation of results from every processing step.

A completely new data structure provides the flexibility to process any type of mass spectrometry, including LC-MS, GC-MS and MS-imaging. Moreover, MZmine 3 now support ion mobility, with a dedicated [LC-IM-MS data visualization](visualization_modules/ims_raw_data_overview/IM-data-visualisation.md) module and [feature detection](workflows/imsworkflow/ion-mobility-data-processing-workflow.md) algorithms. While offering numerous new data analysis options, significant effort was also devoted to trace memory issues and bottlenecks, resulting in an unprecendent processing performance and scalability.

Finally, recent developments have strengthened the ties to other open source projects, including the [GNPS](https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp) platform with Ion Identity Molecular Networking and the [SIRIUS](https://bio.informatik.uni-jena.de/software/sirius/) suite for _in silico_ metabolite annotation.


---
## **About this documentation**
Here you can find documentation for both processing and visualization modules in MZmine 3. Moreover, data processing pipelines for untargeted [LC-MS](workflows/lcmsworkflow/lcms-workflow.md) and [LC-IMS-MS](workflows/imsworkflow/ion-mobility-data-processing-workflow.md) feature detection are described and general recommendations are given.

**COMING SOON!** We are currently working on a series of short videotutorials to help get you started with the main features of MZmine 3!

---
## **How to contribute**
The MZmine community is always welcoming new developers and contributions! You can contribute by improving existing modules or even adding new featurs in MZmine 3! Please, check out our brief [tutorial](http://mzmine.github.io/development.html).

You can also contribute to this wiki and help new users to get started with MZmine 3! See [here](contribute.md) how to contribute to the documentation.
