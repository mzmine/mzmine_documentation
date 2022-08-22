# **Neutral loss filter**

## **Description**

:material-menu-open: **Feature list methods → Feature list filtering → Neutral loss filter**

This module can scan acquired MS data for neutral losses. 

The result is a new feature list containing only features and their neutral-loss equivalents. 

The results will be displayed in the following manner:

- The feature with higher mass without the neutral loss will be named **"Parent"**. The description will contain the ID of the corresponding feature with the neutral loss. 
- The feature with lower mass will be named **"Child"**. The description of the child feature will contain the ID of the parent feature and a ppm-shift relative to the calculated mass.

## **Parameters**

**m/z tolerance** 

m/z window size around the expected features.

**Check RT**

Specify whether the algorithm should compare RT to those of a parent in found peaks or not. 

:warning: We recommend to not use it for direct infusion.

:material-lightbulb: If evaluating chromatographic data we recommend to use this parameter.

**Retention time tolerance** 

Tolerance range of the retention time.

**Minimum height** 

Minimium height of a feature to be considered a parent or child.

**Neutral loss (m/z)** 

m/z ratio of the neutral loss to be detected. If the text box of "Molecule" is not left blank, this parameter will be ignored.

**Molecule** 

Element combination/Molecule of the neutral loss (e.g. HI) This module will calculate the mass of the given molecule and ignore the input in the "Neutral loss" text box.