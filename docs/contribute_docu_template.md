# **Markdown template for a module**

To make the creation of documentation easier, a convenient Markdown structure is discussed below. You can just copy, paste, and modify the provided template.

[//]: # (TODO Make a downloadable vesrion)



    # **Module Name**

    ## **Description**

    :material-menu-open: **Menu1 → Menu2 → Module** 

    [WARNINGS]

    [MAIN TEXT]

    [TIPS]

    ## **References**

    [TEXT]

    ## **Parameters**


    #### **Parameter 1**

    [Description of parameter 1]

    #### **Parameter 2**
    _Optional parameter_
    ...

## **Sections**

The documentation page for the module should follow the following structure:

    # **Module Name**

    ## **Description**

    ### **Algorithms**

    ## **References**

    ## **Parameters**

## **Description section**

In this section you can provide a brief and concise description of what module does, which algorithms it uses, and when it can be applied (usage cases).

The section should start with the module location :material-menu-open: **Menu1 → Menu2 → Module** 

    :material-menu-open: **Menu1 → Menu2 → Module** [Please, add the location of your module here]

Then you can supply any warning that a user needs to know to successfully use the module. For that you can use MkDocs warning admonition box.

!!! warning

    Here you can put your warning. For example, 'This module requires aligned feature list'.

The Markdown for the warning is:

    !!! warning

    Here you can put your warning. For example, 'This module requires aligned feature list'.

If the modules are under maintenance, additional danger box can be added 

!!! danger

    This module is under maintenance/ has known bugs / is outdated and under update / etc.

The Markdown for this box is the following:

    !!! danger

    This module is under maintenance/ has known bugs / is outdated and under update / etc.

After the warnings, the main description text should follow. At the end of the main text, one can include tips to further facilitate module usage.


!!! tip

    Here you can put the tip. For example, 'The good starting value for the Parameter 1 might be between 0.1 and 0.5.

The Markdown for the tip is:

    !!! tip

    Here you can put the tip. For example, 'The good starting value for the Parameter 1 might be between 0.1 and 0.5.

If a more detailed description for the used algorithms is needed, you can add it under a separate subsection "Algorithms".

## **Parameters section**

Start the section with a screenshot of the parameter dialogue, with reference values of parameters included.
Follow with a list of parameters, their brief descriptions, and available values for each parameter.
If a parameter is optional it can be indicated after the parameter name.


[//]: # (TODO Tips & warnings boxes - examples, bug or danger for maintained modules)
[//]: # (TODO )

{{ git_page_authors }}