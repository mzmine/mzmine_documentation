# Data handling (supported formats)

mzmine supports both **open** (e.g., .mzML, .mzXML, .imzML, .netCDF) and many **proprietary** 
vendor data formats. For many vendor formats it is recommended to use the original data files and 
to only apply conversion where needed. Data files can be imported by drag-and-dropping files into 
the mzmine graphical user interface or using the _import MS data_ module. 

**Supported raw data formats include:**

- Bruker Daltonics (.d and .tdf/tsf) 
- Thermo Fisher (.raw)
- Waters (.raw folders)
- Agilent (.d)
- Sciex (.wiff/.wiff2)
- Shimadzu (.lcd)
- MOBILion (.mbi)
- mzML or mzXML/mzData/netCDF (prefer mzML if possible due to better metadata coverage)
- imzML (MS imaging)

!!! warning
    
    Some vendor data formats are **only supported** on specific **operating systems** due to the limited 
    support by their respective data access libraries. All data formats are supported on Windows 
    and many on Linux (see full [compatibility list here](system_requirements.md#compatibility)).
    Many data formats are unsupported on macOS, requiring data conversion to open formats, usually
    on a Windows or Linux computer.

## External dependencies

Many data formats are supported without external dependencies, directly through the mzmine version.
Other formats may require another third-party software to be downloaded and installed.

**MSConvert:** This tool is provided by ProteoWizard and the default data converter for MS data. 
While our team is expanding the native data support for all major vendor formats, we recommend to
install MSConvert for some formats. This will grant direct access to these files and mzmine will
use MSConvert with some internal optimizations to load data files in the background. Formats that 
currently require MSConvert for direct support include:

- Agilent (.d)
- Sciex (.wiff/.wiff2)
- Shimadzu (.lcd)
- MOBILion (.mbi)

## Data conversion to open formats (.mzML / .imzML)

When converting data, prefer the latest standard formats mzML (or imzML for MS imaging data).
Other older open formats like mzData or mzXML may cover less metadata.
It is **recommended** to convert raw data to centroided .mzML files.
**Exceptions:** timsTOF native data as .tdf and .tsf inside the Bruker .d folder are best imported 
in their original format. This is also true for timsTOF fleX MS imaging data.

**This conversion can be applied automatically during the import if the user has MSConvert installed.**
If you want to convert the files yourself, see the sections below.


### MSConvert (ProteoWizard) to mzML

!!! info

    mzmine can use MSConvert automatically. Make sure to setup the MSConvert installation path in 
    the mzmine preferences. (only supported on Windows)

![MSConvert_settings](MSConvert_settings.png)

MSConvert supports the conversion of AB SCIEX, Agilent, Bruker, Shimadzu, Thermo Scientific, MOBILion,
and [Waters](data_conversion.md#waters) raw data. More information about the formats can be found in
the [ProteoWizard Documentation for Users](https://proteowizard.sourceforge.io/doc_users.html).
Furthermore, profile data can be centroided to reduce the file size and memory consumption,
which can be important when processing larger datasets.

Recommended conversion settings for high-resolution MS data to mzML (newer than mzXML). Use **64 bit
** for _m/z_ to retain accuracy.
**Compression is optional** but reduces the size significantly without much information loss - this
might be instrument dependent though.

The **peak picking** filter needs to be the first in the list - otherwise MSConvert might default to
another algorithm
than the selected vendor-specific one. **Beware** that previous versions of MSConvert had the
titleMaker filter at the
first position and the peak picking algorithm was added manually and the position needed to be
switched accordingly to
peak picking first.

![](img/msconvert.png)

### MSConvert command line interface

Example Microsoft windows command to convert all .raw to .mzML. Can be in a .bat-batchfile located
together with the raw data files.
By default, the _m/z_ is encoded in **64 bit**, whereas the intensity is encoded in **32 bit**.
NumpressPic compresses the intensity, whereas the numpressLinear compresses the _m/z_ and RT and
a [toler] can be set. The peakPicking
can be set to specific MS levels (here MS1- for multistage fragmentation)

```bash
"C:\Users\**USERNAME**\AppData\Local\Apps\ProteoWizard 3.0.22166.28b1b7b 64-bit\msconvert.exe" *.raw --filter "peakPicking true 1-" --zlib --numpressPic --numpressLinear -v -o mzml
pause 1
```

More details can be found in
the [ProteoWizard documentation](https://proteowizard.sourceforge.io/tools/msconvert.html).

### ThermoRawFileParser

It is used to convert ThermoFisher .raw files into .mgf, .mzML, .parquet. This converter is
important if an internal calibrant was used (e.g., EASY-IC). This mass is excluded in the FreeStyle
view, whereas MSConvert remains all signals in the mzML, including the calibrant. If those masses 
together with some flagged signals by Thermo, should be removed use this converter with the option 
**--excludeExceptionData**.

!!! Note

    **mzmine 4.8** and higher supports Thermo Raw data directly, there is no need to install external 
    dependencies.

    **Earlier mzmine versions** can use the ThermoRawFileParser automatically to import your data 
    without conversion. In the preferences (CTRL+P) set the "Thermo data import" to "Thermo raw 
    file parser" instead of MSConvert. The raw file parser is supported on Mac, Linux, and Windows.

Example for command line interface with the exclusion of exception data:

```bash
"C:\Users\**USERNAME**\AppData\Local\Apps\ThermoRawFileParser\ThermoRawFileParser.exe" *.raw -d=INPUT_DIRECTORY -o="./mzml_ThermoRawFileParser_excl_data/" --excludeExceptionData 
pause 1
```

More details can be found on [GitHub](https://github.com/compomics/ThermoRawFileParser).

Alternatively, you can use the ThermoRawFileParserGUI to convert Thermo files to mzml without having
to use the CLI: https://github.com/compomics/ThermoRawFileParserGUI

### Bruker

Bruker data is supported in .tdf, .tsf, and .baf format without out prior conversion. Calibrations for .tdf and .tsf are directly imported if they are present.

#### Recalibrated baf files

For Bruker recalibrated data in .baf format, it is recommended to perform **export analysis to mzXML** using the
Bruker's Data Analysis software (for automation, apply Bruker’s processing script during data
acquisition) prior to importing to mzmine. Compared to the mzML and mzData formats, the mzXML format
best retains the full scan definition and sample recalibration properties. In mzML the MS1 scans
were recalibrated but the MS2 scan definition of the precursor _m/z_ did stay unchanged, leading to
differences between MS1 and MS2.

The same problem is observed with Waters data. The solution is to use a precursor m/z values
corrector by applying a script on .mzML or .mzXML files after conversion. The script and the manual
how to use it can be found [here](https://github.com/elnurgar/mzxml-precursor-corrector).

### Waters

Direct Waters data support is currently in beta phase. 

Waters recently released a tool called **Waters data connect**, which allows conversion of DDA, DIA,
and HD-DDA data to mzML. Lock mass correction is applied during the conversion. We also recommend to
enable centroiding (2D peak picking).

<!-- markdown-link-check-disable -->
The tool is available for
[UNIFI](https://videos.waters.com/detail/video/6233843222001/export-data-in-mzml-format-in-unifi?q=How%20to%20set%20up%20MS%20Convert)
and [MassLynx](https://videos.waters.com/detail/video/6342765707112/set-up-msconvert-with-waters_connect-3.0.0).
Additional information can be
found [here](https://support.waters.com/KB_Inf/Other/WKB238107_How_to_obtain_Waters_software_using_the_Waters_Digital_Software_Delivery_and_License_Entitlement_platform)
<!-- markdown-link-check-enable -->

Alternatively, you can try to import the .raw file directly into mzmine, if you have MSConvert
installed on your computer.

## Data sharing (FAIR)

Nowadays, modern scientific knowledge requires the comprehensive description and accessibility of
experimental and
computational approaches used in a study. Therefore, the results should be **Findable, Accessible,
Interoperable,
and Reusable (FAIR)**. This is critical in support of both the initial reviewing of a research
article, and to ensure
its reproducibility and impact.
When publishing, the following information should be added in the method/data availability section:

+ Input files

  Provide the input files that were used for the study by using the deposition number given by the
  data repository
  (see Data repositories). Make sure to provide the raw data file and if used the converted (and
  centroided)
  format (both can be stored in the same repository).
+ Metadata table file

  This file should describe the list of input files and their respective experimental information.
  Best if
  already stored within the data repository.

+ mzmine Version

  The mzmine version, for example mzmine 4.3.0, that was used for processing the data and describes
  the major.minor.patch
  version. Stable releases are provided through GitHub permanently. In contrast, the mzmine
  development versions
  are not permanently available. When using such a version for a publication either make sure the
  results are the same
  with the previous or next release, or upload and provide a link to the version on a permanent
  storage.
+ mzmine .mzbatch file

  This batch contains all parameters of the processing. Starting with MZmine 3.4.0, batch files also
  contain information
  on the version that created the file. However, the version should be still denoted in the
  manuscript. This batch can
  be created a posteriori from any feature list by **right click → Feature list information → Show
  batch**. This batch
  file contains all steps that were used to create this specific feature list.
+ Result files

  These files, e.g., feature lists or .mgf files, can be used for direct statistical (re-)analysis
  and spectral
  (re-)annotations.
+ mzmine project file

  Although this file can be very large, sharing it remains the best approach to make your data 100%
  FAIR.

## Data repositories

Data files should be uploaded to a public mass spectral data repository. Popular repositories are
[GNPS/MassIVE](https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp),
[MetaboLights](https://www.ebi.ac.uk/metabolights/), and
[MetabolomicsWorkbench](https://www.metabolomicsworkbench.org/). All detailed information about the
submission requirements
and needed information can be found on each webpage. If possible and used for data processing,
upload both the original
raw and the converted (centroided) data files. The converted (open format) file enables the easy
integration in other tools,
while the original raw data might contain metadata and profile data that remains uncovered by the
converted format. Additionally, a
metadata file should be added, containing information about the input files and their experimental
information.

## Page Contributors

{{ git_page_authors }}
