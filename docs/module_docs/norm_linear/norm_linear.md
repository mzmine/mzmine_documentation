# **Linear normalizer**

## **Description**

:material-menu-open: **Feature list methods → Normalization → Linear normalizer**

Linear normalizer divides the height (or area) of each feature in the feature list by a normalization factor, chosen according to the "Normalization type" parameter. 

Each column of the feature list is normalized separately. In other words, normalization factor is determined independently for each raw data file.

### **Normalization factors**

Different normalization factors can be applied:

1. **Average intensity**

    Average height (or area) of all peaks in the column is calculated and used as the normalization factor

2. **Average squared intensity**

    Same as Average intensity, but values are squared before calculating the average

3. **Maximum peak intensity**

    Maximum height (or area) in the peak list column is used as the normalization factor

4. **Total raw signal**

    Sum of the height (or area) of all peaks in the peak list column is used as the normalization factor

## **Parameters**

#### **Name suffix**

Suffix to be added to a processed feature list name

#### **Normalization type**

Selection of the normalization factor. Available options:

- Average intensity
- Average squared intensity
- Maximum peak intensity
- Total raw signal

#### **Feature measurement type**

Selection of either feature height or feature area, which will be used to calculate the normalization factors

#### **Original feature list**

If REMOVE option is selected, the original feature list is  removed, allowing to save memory.