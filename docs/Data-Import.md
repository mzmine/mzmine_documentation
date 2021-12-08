# Data Import
***
## Supported formats
MZmine 3 can read and process both low-resolution (unit mass) and high-resolution (exact mass) data in both continuous and centroided modes, including fragmentation (MSn) scans. The following data formats are supported: 
- Vendor formts:
  * Thermo (.raw)
  * Bruker (.tdf and .tsf)
  * Waters (.raw)
  * **Other data formats?**
- Open formats:
  * mzML (converted via [MSConvert](https://proteowizard.sourceforge.io/download.html) from native vendors data)
  * mzXML (mzXML versions 2.0, 2.1 and 3.0)
  * mzData (mzData versions 1.04 and 1.05)
  * NetCDF (no MSn data support)
  * **Other data formats?**
 
**Note**: it is strongly recommended to convert native vendor data files into the mzML format using [MSConvert](https://proteowizard.sourceforge.io/download.html) to avoid [...].

???+ danger Converted Agilent raw data
  mzML file converted from Agilent raw data can be imported, but certain restrictions might hinder processsing workflows due to the nature of the raw data format.
