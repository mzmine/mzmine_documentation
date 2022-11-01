# Data conversion to open formats (mzML / imzML)

## MSConvert (ProteoWizard) to mzML
Recommended conversion settings for high-resolution MS data to mzML (newer than mzXML). Use **64 bit** for _m/z_ to retain accuracy. 
**Compression is optional** but reduces the size significantly without much information loss - this might be instrument dependent though.

The **peak picking** filter needs to be the first in the list - otherwise MSConvert might default to another algorithm 
than the selected vendor-specific one. **Beware** that previous versions of MSConvert had the titleMaker filter at the 
first position and the peak picking algorithm was added manually and the position needed to be switched accordingly to 
peak picking first.  

![](img/msconvert.png)

### MSConvert command line interface
Example Microsoft windows command to convert all .raw to .mzML. Can be in a .bat-batchfile located together with the raw data files.
By default, the _m/z_ is encoded in **64 bit**, whereas the intensity is encoded in **32 bit**. NumpressPic compresses the intensity, whereas the numpressLinear compresses the _m/z_ and RT and a [toler] can be set. The peakPicking
can be set to specific MS levels (here MS1- for multistage fragmentation)
```bash
"C:\Users\**USERNAME**\AppData\Local\Apps\ProteoWizard 3.0.22166.28b1b7b 64-bit\msconvert.exe" *.raw --filter "peakPicking true 1-" --zlib --numpressPic --numpressLinear -v -o mzml
pause 1
```
More details can be found in the proteowizard documentation. 

https://proteowizard.sourceforge.io/tools/msconvert.html

## Bruker: Recalibrated files to the data conversion guide

For Bruker recalibrated data, it is recommended to perform **export analysis to mzXML** using the Bruker's Data Analysis software (for automation, apply Bruker’s processing script during data acquisition) prior to importing to MZmine. Compared to the mzML and mzData formats, the mzXML format best retains the full scan definition and sample recalibration properties. In mzML the MS1 scans were recalibrated but the MS2 scan definition of the precursor _m/z_ did stay unchanged, leading to differences between MS1 and MS2.


## Page Contributors

{{ git_page_authors }}
