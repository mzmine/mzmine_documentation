# Batch spectral library generation

:material-menu-open: **Feature list methods → Export feature list → Spectral library batch generation** 

Provide here a concise description of the module functioning principles and usage. If possible, briefly describe the algorithm(s) employed by the module. If a detailed description of the algorithm functioning is needed, provide it in the [Algorithm](contribute_docu_template.md#algorithm) section). Please cite relevant references in this section using the following box:


## Parameters
![Example image description](img/contribute/example_dialog.png)

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


- The **Export file** is prefilled by your wizard settings
- Set the **Export format** if you want to change it NIST .msp or .mgf
- Set the **MS level filter** if you acquired MSn data and only want to export MS2. If you only acquired
  MS2 or want to export MSn, the setting can remain MSn
- The **Metadata** are prefilled by the wizard settings and can be also adapted here
- Set the **m/z tolerance (merging)** for grouping signals acquired by different collision energies
  and to merge those spectra (similar to stepped collision energy, when multiple energies are combined
  into one scan)
- Set the **Handle chimeric spectra**
- Set the **Quality parameters**