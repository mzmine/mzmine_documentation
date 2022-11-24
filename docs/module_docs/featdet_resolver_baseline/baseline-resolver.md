# **Baseline resolver**

## **Description**

:material-menu-open: **Feature detection → Chromatogram resolving → Baseline resolver**

A very simple method that can be used to demonstrate the functionality of chromatogram resolving. 

- First, the algorithm removes the lowest part of the chromatogram below a **Baseline level** specified by the user. 
- Remaining peaks above the baseline level are recognized if they fulfill the height and duration requirements.

## **Parameters**

#### **Suffix**

This string is added to feature list name as suffix

#### **Original feature list**

Defines the processing.

Standard is to KEEP the original feature list and create a new processed list.

REMOVE saves memory.

PROCESS IN PLACE is an advanced option to process directly in the feature list and reduce memory consumption more - this might come with side effects, apply with caution.

#### **MS/MS scan pairing**

Set MS/MS scan pairing parameters. For more details see [MS2 scan pairing](..//featdet_ms2_scan_pairing/ms2_scan_pairing.md)

#### **Min peak height**

Minimum acceptable feature height (absolute intensity)

#### **Peak duration range**

Range of acceptable feature durations

#### **Baseline level**

Level below which all data points of the chromatogram are removed (absolute intensity)

#### **Min # of data points**

Minimum number of data points on a feature

{{ git_page_authors }}