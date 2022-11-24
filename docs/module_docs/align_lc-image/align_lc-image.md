# **LC-Image Aligner**

## **Description**

:material-menu-open: **Feature list methods → Alignment → LC-Image-Aligner**

Aligns LC and imaging measurements based on m/z and mobility.Images are aligned to all LC features that match, only the best match is retained.

## **Parameters**

#### **Feature lists**

Select at least two feature lists. The image feature list(s) are aligned to a single (pre-aligned) LC feature list.

#### **m/z tolerance**

The file-to-file tolerance for two features.

#### **m/z weight**

Maximum score for a perfectly matching m/z. Default value is 1.

#### **Mobility tolerance**

_Optional parameter_ 

The file-to-file mobility tolerance. If the files don't contain mobility information, this parameter will be ignored. Default value is 0.01.

#### **Mobility weight**

Maximum score for a perfectly matching mobility. Default value is 1.

#### **Feature list name**

The name of the new feature list. Use {lc} to use the name of the input (LC/DI) feature list.

{{ git_page_authors }}