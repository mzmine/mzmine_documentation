# Markdown template to create online documentation for a processing module

To facilitate a consistent contribution to the MZmine online documentation from new users, please refer to the present Markdown template. Changes in the structure are of course allowed, but will have to be justified in the pull request. Remove this top part from the new page and start at **Module name**.

In order not to interrupt the document flow, we encourage the use of admonition boxes insight any point of the document to provide warnings, tips, and side contents in general. A few examples are provided below, while a variety of other options is avaiable [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/).

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
<br><br>

# Module name
Point to the menu path to start the module:

:material-menu-open: **Menu1 → Menu2 → Module** 

Provide here a concise description of the module functioning principles and usage. If possible, briefly describe the algorithm(s) employed by the module. If a detailed description of the algorithm functioning is needed, provide it in the [Algorithm](contribute_docu_template.md#algorithm) section). Please cite relevant references in this section using the following box:

!!! info inline

    **References** 
    When using this module, please consider citing the following:
    Schmid, R., Petras, D., Nothias, LF. et al. Ion identity molecular networking for mass spectrometry-based metabolomics in the GNPS environment. Nat Commun 12, 3832 (2021). https://doi.org/10.1038/s41467-021-23953-9
    2. Reference #2
    3. ....

---


## Parameters
![Example image description](../img/contribute/example_dialog.png)

Screenshot of the module dialog should contain default values. If multiple sub dialogs are available from parameters, either create one or multiple dialog images.

Provide here a concise description of each processing parameter. Where possible, provide default values and/or recommended values to start the tuning from.

#### Parameter #1
Provide here a brief description for Parameter #1. Default values, tunig points, hints...

#### Parameter #2
Provide here a brief description for Parameter #2.

#### Parameter #3 _(Optional)_
Provide here a brief description for Parameter #3. Optional parameters should be labelled as _(Optional)_ following the parameter's name.

---

## Algorithm
Optional: A more detailed description of the algorithm(s) employed by the module can be provided in this section.


---

{{ git_page_authors }}