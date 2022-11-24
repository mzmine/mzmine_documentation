## **General structure of MZmine3 code**

# **MZmine architecture**

MZmine 3 is developed using Java technology, therefore it is completely platform independent, requiring only Java runtime for running. 
One of the main design goals is to keep a strict separation between the application core and modules for data processing and visualization. The general architecture of the modules is presented at the following scheme.

[//]: # (TODO Update scheme)

![Architecture](architecture.png)

[//]: # (TODO Describe application core)
[//]: # (Describe data processing modules)
[//]: # (Describe visualization specifics)

[//]: # (    System)

[//]: # (    Service)

[//]: # (    Layers)

[//]: # (    Components)

[//]: # (    Classes)

[//]: # (    Methods)

[//]: # (List of classes - modules correspondence)

!!! tip
    The practical instructions for MZmine coding can be found [here](module_development.md).

## **Libraries used**

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

## **Module structure**

Each module in MZmine necessarily contains three classes:

- [Name]Module.java
- [Name]Parameters.java
- [Name]Task.java

Optionally module can contain dialog class:

- [Name]Dialog.java

!!! tip
   You can fnd examples for all these classes in the `java/io/github/mzmine/modules/example` folder.

### **Module class** 

Each Module class implements one of three interfaces:

- **MZMineModule** interface - the most basic interface, aimed at any module that has to store some kind of parameters,
- **MZMineRunnableModule** interface - an interface that extends MZmine module and presents a `runModule()` method, which provides an opportunity to run task (for example, from the dialog),
- **MZMineProcessingModule** interface - an interface that extends MZMineRunnableModule and gives an opportunity to execute a module in a batch.


### **Parameters class**

The Parameters class is defined by the **ParameterSet interface**, which declares functions necessary to get, load, and save module parameters. Also, in this class additional information must be defined, such as compatibility of module with the IMS data and URL of online documentation. Typically, a module would use **SimpleParameterSet class**. 

[//]: # (TODO Add parameter types)

### Task

This is the part where the functionality of a module is implemented. The main specifications are defined by the **Task interface**, with methods that control and monitor the flow of a task execution (such as `cancel()`, `getTaskPriority()`, `getFinishedPercentage()`). Task interface is implemented by **AbstractTask class**, which defines some of the most common used methods.  

[//]: # (AbstractTask)
[//]: # (Here you can focus on algorithm implementation and performance.)

[//]: # (constructor)

[//]: # (initialize&#40;&#41;)

[//]: # (run&#40;&#41;)

[//]: # (### Dialog)


[//]: # (### Module)

[//]: # (TODO Create following subpages?)

[//]: # (## **Developing a new MZmine module**&#41;)

[//]: # ()
[//]: # ()
[//]: # (## **Adding a new feature**)

[//]: # ()
[//]: # ()
[//]: # (## **Fixing a bug**)

[//]: # (TODO Add more info on the following)

[//]: # (### Creating parameters&#41;)

[//]: # ()
[//]: # (constructor)

[//]: # (showSetupDialog)

[//]: # (#### i/o)

{{ git_page_authors }}