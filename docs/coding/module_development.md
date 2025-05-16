# **Key steps to mzmine module development**

## Coding tutorials

Detailed coding tutorials by Robin Schmid:

[01. First module and new columns](https://www.youtube.com/watch?v=T02H4rwyCvk&list=PL4L2Xw5k8ITzQEq677w-UicporguCgAt3&ab_channel=RobinSchmid)

[02. Git, GitHub, contribute code to MZmine](https://www.youtube.com/watch?v=tTJSoxw8fjU&ab_channel=RobinSchmid)

## **1. Define the role and functionality of your module**

Each module in mzmine belongs to some module category (see [MZmine architecture](general_structure.md)). Before starting, try to define category, to which your module will belong - raw data processing, feature detection, visualization, etc.

A good idea is to browse already existing modules. Currently, MZmine contains more than 100 modules, so there are high chances that one of the existing modules may carry similar functionality to the one you want to code. This can help you to create your own module. Assess the scale of the added functionality and how the new module can be integrated with the existing ones.
For example, if you'd like to add a new filter for the feature list rows, the best option might be not to create a new module but to add the new option as a parameter to the already existing Feature list rows filter.

## **2. Create a new branch locally for your changes**

You can either do it from command line using git command `git checkout -b new-branch-name` or directly from your IDE (detailed expanation can be found in the video tutorial).

## **3. Create a package for your module**

Go to the folder that corresponds to the functionality of your module (e.g., dataprocessing for the module that will be process features in the feature list). Create a new package in this folder. 

!!! tip
     Make sure that a package name starts with a meaningful prefix, such as "filter_" for a module that will filter rows in a feature table.

## **4. Create necessary classes**

Following the module structure described [here](general_structure.md), create Module, Parameters, and Task classes.

!!! tip
You can directly copy examples for all these classes from the `java/io/github/mzmine/modules/example` folder and **rename them** accordingly. These example files also contain some useful tips.

## **5. Define module name, description, and category**

Start by defining MODULE_NAME and MODULE_DESCRIPTION variables. Assign your module a category by modifying `getModuleCategory()` method. Available categories are listed in MZmineModuleCategory file.

## **6. Work on your Parameters class**

You can search for available parameters in the Parameters package or copy them from similar modules. 
After you have described all parameters, add parameters to the constructor of your Parameters class 

`super(new Parameter[]{parameters go here})`

!!! warning 
 A parameter in the Parameters class should be public static final. 

## **7. Define `runModule()` method [For the runnable modules]**

Here you are creating a task that will be launched after user has chosen parameters. You do not need to worry about task scheduling here, the task is only created and passed here.

## **8. Work on your Task class**

As you extend the AbstractTask class, some functionality will already be defined. To get the values of the parameters from ParameterSet, use the following approach `parameters.getValue(YourClassParameters.paramererName.getValue()`. 
You can modify the message by the logger, check for cancelled state, and update progress. Before progress update, implement the logic of your calculations. 

!!! warning 
     Do not forget to modify `addAppliedMethodsAndResultsToProject`, so that the method info will be accessible in the feature list information.

!!! tip 
    If you have to implement some method to process scans, check ScanUtils first, it might already have been implemented.


## **9. Integrate a newly created module into mzmine GUI**

As the last step, for your module to be accessible, add it to the AbstractWorkspace.java or the AcademicWorkspace.java file. If you wish your module to be accessible in the batch mode, add it in the BatchModeModulesList

## **10. Test and debug**

Before pushing your final changes to the remote branch, try to thoroughly test your code. Think about corner cases and possible bugs. Using IDE tools can be extremely useful in this step.

## **11. Create documentation**

Prepare a description for your module that will go into the documentation. Creating a thorough documentation will help more people to used and understand your module. The documentation template can be found [here](../contribute_docu_template.md)

## **12. Push to the remote branch and create a pull request**

After you coded and tested your module, you can push your changes to the remote branch and create a pull request. After your pull request will be reviewed by one of the main contributors. There might be some comments that you'll have to address. After that, your module will be merged into the master branch and become a part of MZmine!

[//]: # (TODO Add more details here)

{{ git_page_authors }}
