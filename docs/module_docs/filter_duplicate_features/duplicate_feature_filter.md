# **Duplicate feature filter**

## **Description**

:material-menu-open: **Feature list method → Feature list filtering → Duplicate feature filter**.

This filter can help eliminate misaligned feature list rows after the gap-filling process. 

It has three different **modes**:

- **Old average (the old filter)**:
    
    Keeps only the feature list row with the maximum average area. Compares rows with the average m/z and RT.

- **New average**: 

    Compares rows with the average m/z and RT and creates a consensus row.Two peaks are considered duplicates when their average m/z and retention time differences are lower than the tolerances set by the user. 
    
    When two (or more) duplicates are found, a **consensus row** is created with the lowest row ID of all duplicates. For this consensus row, all DETECTED features are favored over ESTIMATED (gap-filled) and ESTIMATED are favored over UNKNOWN. Furthermore, if there are only ESTIMATED features in a raw data file, the highest is chosen.

- **Single feature**: 

    Compares rows on a raw data file basis. Marks rows as duplicates if they share one feature within the RT and m/z tolerance in the same raw data file. Creates a consensus row.

## **Parameters** 

#### **Name suffix**
This is the suffix to identify the new aligned peak list.

#### **Filter mode**
User can choose one of three modes: old average, new average, and single feature.

#### **m/z tolerance**
Maximum m/z difference between duplicate peaks.

#### **RT tolerance**
Maximum retention time difference between duplicate peaks.

#### **Require same identification**
If the checkbox is selected duplicate peaks must have the same identification.

#### **Original feature list**
Can be either processed in place of, kept or replaced. 

{{ git_page_authors }}
