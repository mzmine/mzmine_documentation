# **MZmine architecture**

MZmine 3 is developed using Java technology, therefore it is completely platform independent, requiring only Java runtime for running. One of the main design goals is to keep a strict separation between the application core and modules for data processing and visualization.

[//]: # (Describe application core)
[//]: # (Describe data processing modules)
[//]: # (Describe visualization specifics)

    System
    Service
    Layers
    Components
    Classes
    Methods

[//]: # (List of classes - modules correspondence)
## Module structure

- Module
- Parameters
- Task
- Dialog

### Creating parameters

constructor
showSetupDialog

#### i/o

### Task

This is the part where the functionality of your module is implemented. Here you can focus on algorithm implementation and performance.

AbstractTask
constructor
initialize()
run()

### Dialog

### Module

## Libraries used

    Apache XML Graphics - EPS image export
    Chemistry Development Kit - Isotope pattern and molecular calculations
    Freehep - EMF image export
    Google Guava - Utility classes
    JavaHelp - Help system
    JChemPaint - 2D molecule visualization
    JFreeChart - TIC, Spectra and 2D visualizers
    JMol - 3D molecule visualization
    jmzml - mzML file import
    jmzTab - mzTab file import and export
    NetCDF-Java - NetCDF file import
    VisAD - 3D visualizer
    WEKA - Clustering and other machine learning algorithms
