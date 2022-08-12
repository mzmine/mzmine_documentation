# **Merge raw data files**

## **Description**

This module merges all raw data files into a new. For example to combine positive and negative scans with MS2, all from different raw data files.

TODO: Usage examples or cases

## **Method parameters**

**Raw data files**

Raw data files the module will take as an input.

**Mode**

+ MERGE PATTERN: 

    Merge files based on a grouping identifier which can be a name suffix or prefix. (e.g., Sample_A_1, Sample_B_1: Use AFTER LAST _ to combine these files)

+ MERGE SELECTED: 

    Merge all selected files to a new

**Grouping identifier position**

Search for the specific group identifier before the first or after the last marker.

**Position marker**

The marker that splits the specific group identifier from the rest of the file names.

**MS2 marker**

If a raw data file has this marker in its name, it will only be used as a source of MS2 (MSn) scans. All MS1 scans of this file will be discarded. 

TODO - what does this mean (e.g., MS2, TOP4, ...)

**Suffix**

Suffix to be added to the new file name.