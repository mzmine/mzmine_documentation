# **Markdown template to create online documentation for a processing module**

To facilitate a consistent contribution to the MZmine online documentation from new users, please refer to the present Markdown template. Changes in the structure are of course allowed, but will have to be justified in the pull request.

--- 
<br><br>

# **Module Name**
Please start this section with the module's location within the MZmine menu as follow:

:material-menu-open: **Menu1 → Menu2 → Module** 

Provide here a concise description of the module functioning principles and usage. If possible, briefly describe the algorithm(s) employed by the module. If a detailed description of the algorithm functioning is needed, provide it in the [Algorithm](contribute_docu_template.md#algorithm) section). Please cite relevant references in this section using the following box:

!!! info inline

    **References** 
    
    1. Reference #1
    2. Reference #2
    3. ....

---

## **Parameters**
Provide here a concise description of each processing parameter to be set. Where possible, provide default values and/or recommended values to start the tuning from.

Please start this section with a screenshot of the module's dialogue box and continue with the parameters' description following the scheme provided below:

#### **Parameter #1**
Provide here a brief description for Parameter #1.

#### **Parameter #2**
Provide here a brief description for Parameter #2.

#### **Parameter #3 _(Optional)_**
Provide here a brief description for Parameter #3. Optional parameters should be labelled as _(Optional)_ following the parameter's name.

---

## **Algorithm**
A more detailed description of the algorithm(s) employed by the module can be provided in this section.

---

## _Warnings and admonitions_
In order not to interrupt the document flow, we encourage the use of admonition boxes to provide warnings, tips, and side contents in general. A few examples are provided below, while a variety of other options is avaiable [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/).

<br>

!!! danger inline

    This module is currently under maintenance / deprecated / etc.

<br>

!!! warning inline

    Since mass lists are taken as input by EIC building algorithms, the Mass detection module must be run first

<br>      
    
!!! tip inline

    A good starting point for 'Parameter #1' is between 0.1 and 0.5.

---

{{ git_page_authors }}


[//]: # (TODO Make a downloadable version)

[//]: # (TODO Tips & warnings boxes - examples, bug or danger for maintained modules)
[//]: # (TODO )