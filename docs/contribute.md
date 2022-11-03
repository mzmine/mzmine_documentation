# **How to contribute to the MZmine documentation** 

## **About the documentation**

Supporting and updating the documentation is especially important for MZmine due to the variety and complexity of the modules. If you wish to contribute by creating a module, please, create a corresponding documentation. In this way, the MZmine community will be able to easier adapt the novel modules in their workflows and everyday practice.

MZmine documentation uses [MkDocs site generator]("https://www.mkdocs.org/"). Documentation source is created in Markdown and configured using a single YAML file. If you are new to MkDocs or Markdown, the detailed User guide can be found [here]("https://www.mkdocs.org/user-guide/writing-your-docs/").

[//]: # (TODO Describe local installation of documentation)

## **Pages structure**

Structure of the pages is described in ```mkdocs.yml``` file, which represents the tree-like structure:

```
nav:
  - Home page: index.md
  - Getting started: getting_started.md
  - Main window overview: main-window-overview.md
  - Data conversion: data_conversion.md
  - Citations: citations.md

  - Coding:
    - General structure: coding/general_structure.md
    - Module development: coding/module_development.md
    - Raw data structure: coding/raw_data_structure.md
    - Feature data structure: coding/feature_data_structure.md
    - Example module - Spectral entropy: coding/example_module.md
```
[//]: # (yaml)
When a new documentation page or subsection is added, yaml structure changes correspondingly. For example:

```
nav:
  - Home page: index.md
  - Getting started: getting_started.md
  - Main window overview: main-window-overview.md
  - Data conversion: data_conversion.md
  - Citations: citations.md

  - Coding:
    - General structure: coding/general_structure.md
    - Module development: coding/module_development.md
    - Raw data structure: coding/raw_data_structure.md
    - Feature data structure: coding/feature_data_structure.md
    - Example module - Spectral entropy: coding/example_module.md
  - NEW SECTION:
    - NEW PAGE: new_section/new_page.md
```

## **How to edit the documentation pages**

**1. Make a GitHub Account**

You'll need to make a [GitHub Account](https://github.com/join).

**2. Click Edit Button on Page You Want to Edit**
![editbutton](img/contribute/editbutton.jpg)

**3. Fork the Repository When Prompted (only the first time)**

![fork](https://ccms-ucsd.github.io/GNPSDocumentation/img/edit-pages/fork.png)

**4. Make the Edits in MarkDown**

![img.png](img/contribute/makechanges.jpg)

**5. Propose Changes**

Please describe the change you are making.

![](img/contribute/proposechanges.jpg)

**6. Create Pull Request**

![](img/contribute/createpr.jpg)

**7. Finalize Pull Request with Description**

![](img/contribute/openpr.jpg)

## **How to create a new page**

**Follow steps 1 - 3.**

**Navigate to mzmine_documentation/docs in your fork and create a new file**

![new_file](img/contribute/newfile.jpg)

**Follow steps 4 - 7.**

## **Additional useful information**
### **Using icons**

To highlight some points in the prepared documentation, it is advised to use icons. **Material for MkDocs** is integrated into MZmine documentation and suggests a wide range of icons, logos, and more. Icons can be found [here]("https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/").

[//]: # (Used icons)

[//]: # (:material-menu-open: )

[//]: # ()
[//]: # (:warning:)

[//]: # ()
[//]: # (:material-lightbulb:)

### **Using mathematical formulas**

To add mathematical formulas, it is recommended to use LaTex notation, which can be directly incorporated into MkDocs pages.

To insert inline formula, one can use single "\$" signs, like this `$x^n + y^n = z^n$"`, resulting in $x^n + y^n = z^n$. To insert formula on a new line, use double "\$" signs, for example `$$E=mc^2$$`, resulting in

$$E=mc^2$$

The excellent reference guide to different mathematical expressions can be found [here]("https://www.overleaf.com/learn").

## Page Contributors

{{ git_page_authors }}

This page was adapted from the [GNPS documentation](https://ccms-ucsd.github.io/GNPSDocumentation/gnps_community/).
