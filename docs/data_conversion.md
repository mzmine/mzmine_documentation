# Data conversion to open formats (mzML / imzML)

## msconvert (ProteoWizard) to mzML
Recommended conversion settings for high-resolution MS data to mzML (newer than mzXML). Use **64 bit** for _m/z_ to retain accuracy. 
**Compression is optional** but reduces the size significantly without much information loss - this might be instrument dependent though.

The **peak picking** filter needs to be the first in the list - otherwise msconvert might default to another algorithm than the selected vendor-specific one. **Beware** that previous versions of msconvert had the titleMaker filter at the first position and the position needed to be switched accordingly to peak picking first.  

![](img/msconvert.png)



## Page Contributors

{{ git_page_authors }}
