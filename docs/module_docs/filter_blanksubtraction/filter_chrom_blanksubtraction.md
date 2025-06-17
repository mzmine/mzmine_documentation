# **Chromatogram blank subtraction**

## **Description**

!!! warning

    This module should be applied after chromatogram builder and before the feature resolving steps. Project metadata is used to define blank samples. 

!!! tip

    This module works on the chromatogram level (quite early in the workflow) and can help reduce the processing time and false features detected. 
    Also check out the **[Feature list blank subtraction](filter_blanksubtraction.md)** that works on aligned feature lists and requires blank samples in the aligned list.

:material-menu-open: **Feature list methods → Feature list filtering → Chromatogram blank
subtraction**

Subtracts blank chromatograms from all other samples. Blank chromatograms are constructed by
maximizing intensity over multiple blank files. Uses **sample metadata** to define **blank** samples
in the **mzmine_sample_type** column.

By default, the blank samples will be not processed further because they will be empty after blank
subtraction.

## Parameters

#### m/z tolerance (sample-to-sample)

Matching tolerance to merge blank chromatograms and to then subtract from matching sample
chromatograms.

#### Suffix

The suffix for the new feature list.

#### Original feature list

Defines how to handle the original feature list.

{{ git_page_authors }}
