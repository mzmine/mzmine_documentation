# Export MRMs to TSV

The Export MRMs to TSV module exports MRM-specific metrics to a tsv or csv table.
An exemplary export is shown below:

![example-export](example-export.png)
**Figure 1:** Example export result with [Skip missing features](#skip-missing-features) disabled.

## Parameters 

#### Feature lists
Select the feature lists that shall be exported. 

#### Export file

Select the file to which the export should export to.


#### Skip missing features

Select if the export should skip missing features, if a feature was detected in file A but not in file B. An example of the behaviour is shown in the screenshot (Figure 1) above. Here, the [Skip missing features](#skip-missing-features) option was disabled, creating an empty line for the feature of ID 43 in FILE_B. The export contains the ID of the row the feature belongs and was aligned to, but no q1 or q3 masses, no area, no height, and no RT, since the feature was not detected. 

If the [Skip missing features](#skip-missing-features) option is enabled, this line would not exist.

---

{{ git_page_authors }}
