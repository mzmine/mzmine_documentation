# **Retention time calibration**

## **Description**

:material-menu-open: **Feature list methods → Normalization → Retention time calibration**

The retention time normalizer attempts to reduce the deviation of retention times between feature lists, by searching for common features in these feature lists and using them as normalization standards.

Ions present in all given feature lists (according to given m/z, RT tolerance and minimum intensity) in exactly one instance are considered as standards. Retention times of the standards are then averaged and equalized in all samples, and retention times of all other features are adjusted according to the retention times of neighboring standard features.

:warning: The method requires multiple feature lists of different samples, processed by deconvolution (for example, [Local minimum resolver](../featdet_resolver_local_minimum/local-minimum-resolver.md)) but prior to alignment.

## **Parameters**

#### **Name suffix**

Suffix to be added to a processed feature list name

#### **m/z tolerance**

Maximum allowed m/z difference for two values to be considered the same

#### **Retention time tolerance**

Maximum allowed difference between two retention time values

#### **Minimum standard intensity**

Minimum height of a feature to be selected as normalization standard

#### **Original feature list**

If REMOVE option is selected, the original feature list is  removed, allowing to save memory.

[//]: # (TODO Add the screenshot)
[//]: # (The folowing screenshot shows two feature lists &#40;top&#41; normalized by the Retention time normalizer &#40;bottom&#41; with the following parameters: m/z tolerance = 0.1, RT tolerance = 1:00, Minimum standard intensity = 1E6. The red color shows which peaks were selected as standards. The retention time of standards was averaged, and retention time of other peaks was adjusted accordingly &#40;blue color&#41;.)

{{ git_page_authors }}

