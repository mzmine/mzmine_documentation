# mzmine architecture & development process

## Technology

mzmine is developed in modern Java, and the distributed installers and portable versions ship with a
matching Java Runtime. This makes mzmine standalone platform independent. There is no need to
install Java on the target machine. Updates can be installed over older releases and follow semantic
versioning, i.e., major.minor.patch like 4.8.0. In rare cases, the mzmine installer may ask for
manual removal of a previous installation. Run mzmine through its graphical user interface (GUI),
built with JavaFX, or via [command line interface](../commandline_tool.md) (CLI) to run batch
processing.

Contributions to the mzmine [source code](https://github.com/mzmine/mzmine)
and [documentation](https://github.com/mzmine/mzmine_documentation) are possible through pull
requests (code) or issues to the respective repositories. Feel free to create a fork of each
repository to work on feature branches. We recommend that you reach out to our team early in your
idea or development phase to boost your productivity. We can provide help to new developers to get
started with mzmine development and provide pointers to already existing resources.

- How to contribute to the [documentation](../contribute.md)?
- How to contribute to the [mzmine code base](../contribute_intellij.md)?

!!! tip
    
    The practical instructions for mzmine coding can be found [here](module_development.md).

## GitHub issues as a pool of ideas and feedback:

- Providing **feedback** on specific modules or functions
- Outlining **feature requests**: This can be small improvements or full module ideas. Useful
  information includes: Links to articles, reference implementations, and descriptions of user
  inputs, expected results, and example use cases.
- Reporting **bugs**: Provide all details on how to reproduce bugs, the log file, batch
  configuration, example data

One of the main design goals is to keep a strict separation between the application core and modules
for data processing and visualization. The general architecture of the modules is presented at the
following scheme.

## Roadmap

The development process of mzmine is agile and driven by multiple factors:

- **User Feature Requests**: Community needs and feedback shape our development priorities
- **Strategic Partnerships**: Collaborations with academic and industry partners guide development
  directions
- **Contracted Development**: Specific features can be developed through funded projects
- **Community Contributors**: Open-source contributions from developers worldwide
- **Internal Planning**: Strategic development guided by the mzio team's expertise and vision

Our roadmap remains flexible to accommodate emerging needs while maintaining focus on core
functionality improvements.

# Development

## Core architecture

mzmine's core architecture is built on several key components that enable efficient and modular data
processing:

### Task controller

The TaskController manages the execution of processing tasks, allowing multiple operations to run in
parallel. It handles task scheduling, priority management, and resource allocation to optimize
performance on multi-core systems. Tasks can be monitored through progress tracking and canceled if
needed.

### Module system

mzmine uses a modular architecture where each processing step is implemented as an independent
module. This design:

- Ensures loose coupling between different processing steps
- Makes modules reusable across different workflows
- Simplifies maintenance and testing
- Allows easy addition of new functionality without modifying existing code

### GUI framework

The graphical user interface is built with JavaFX following the Model-View-Controller (MVC) pattern:

- Interactive data visualization dashboards
- Real-time updates of processing results
- Flexible window management for multiple views
- Custom controls for mass spectrometry data visualization
- Interactive linking between dashboards through reactive programming (binding of JavaFx properties)

### Parameter system

User parameters are easy to design and extend in their functionality and offer:

- Consistent, auto generated user interfaces across all modules
- Type-safe parameter handling
- Automatic validation of user inputs
- Persistent storage of parameter values
- Versioning of parameters, offering handling of simple changes in parameter behavior or to notify
  about impactful changes

## Module development

Each module in mzmine is built from three classes:

- [Name]Module.java
- [Name]Parameters.java
- [Name]Task.java

!!! tip

    You can fnd examples for all these classes in the
    `java/io/github/mzmine/modules/example` [folder](https://github.com/mzmine/mzmine/tree/master/mzmine-community/src/main/java/io/github/mzmine/modules/example)

### Module class

The module holds metadata like the name, description, and ParameterSet class.

Each Module class implements one of three interfaces or its subclasses:

- **MZMineModule** interface - the most basic interface, aimed at any module that has to store some
  kind of parameters,
- **MZMineRunnableModule** interface - an interface that extends mzmine module and presents a
  `runModule()` method, which provides an opportunity to run task (for example, from the dialog),
- **MZMineProcessingModule** interface - an interface that extends MZMineRunnableModule and gives an
  opportunity to execute a module in a batch.

!!! tip

    There are special implementations of Module to make the definition and scheduling easier, like
    [TaskPerFeatureListModule](https://github.com/mzmine/mzmine/blob/master/mzmine-community/src/main/java/io/github/mzmine/modules/impl/TaskPerFeatureListModule.java)
    that splits the work in one task per feature list, and 
    [SingleTaskFeatureListsModule](https://github.com/mzmine/mzmine/blob/master/mzmine-community/src/main/java/io/github/mzmine/modules/impl/SingleTaskFeatureListsModule.java)
    that processes all feature lists in a single task.

### ParameterSet class

The Parameters class is defined by the **ParameterSet interface**, which declares functions
necessary to get, load, and save module parameters. This class provides versioning with mapping
functions to load parameters that were saved by a previous version of mzmine. This includes simple
mapping of parameter values, e.g., if a parameter changed its data type, or more complex handling of
version changes to ensure compatibility with newer versions. The parameters are displayed in a
**ParameterSetupDialog** and interfaces are auto-generated to allow user optimization. Custom *
*ParameterSetupDialog**s may provide charts and other visual feedback to facilitate parameter
tuning.
The ParameterSet class also points to this documentation by providing a URL. If you develop a
module, please provide a documentation and link as well.
information must

**ParameterSets** are made up of **Parameters** that are accessed through static instances of these
parameters. Each **Parameter** defines the GUI controls, saving and loading, and value validation.

!!! typ

    Typically, new Parameters classes can extend the [**SimpleParameterSet class**.](https://github.com/mzmine/mzmine/blob/master/mzmine-community/src/main/java/io/github/mzmine/parameters/impl/SimpleParameterSet.java)

#### Latest module parameters

MZmineCore contains a map of the latest module parameters. This ParameterSet is often copied as the
starting point for creating the parameter setup dialog. Once the user runs a module with different
parameters, those latest parameters are updated.

### Task

This class implements the logic of a module. The main specifications are
defined by the **Task interface** and its abstract child classes. It defines methods that control
and monitor the flow of a task execution (such as `cancel()`, `getTaskPriority()`,
`getFinishedPercentage()`, `getStatus()`).

A new task is usually created by its module, added to the TaskController with a specified
TaskPriority (HIGH, NORMAL), and the task controller will call its **run** method. If successful,
the task should add an applied method to the processed RawDataFiles and FeatureLists. These applied
methods hold a trace of all operations applied to data files and feature lists and will enable later
generation of batch configurations from the processing history.

The best starting points are newer abstract classes like **AbstractSimpleTask**,
**AbstractFeatureListTask**, or **AbstractRawDataFileTask** that already define much of the control
flow logic and facilitate the creation of applied methods.

{{ git_page_authors }}
