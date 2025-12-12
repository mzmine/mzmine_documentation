# System requirements

## Installation

Installation of mzmine is described on the [getting started](getting_started.md#install-update) page.
mzmine is available as an installable package or a portable version. The portable version does not
require administrator rights to be run, making it useful for users without elevated
permissions.

## Hardware requirements

**Minimum** (small datasets < 30 LC-MS files):

- 64 bit CPU, 4 Cores (2.5 GHz, Intel Core i5 or AMD Ryzen 5), 16 GB RAM, secondary Sata SSD drive (512 GB),
  integrated graphics
- Display 1920 x 1080 pixel (Full HD)
- Internet connection for login and spectral library/machine learning model download
- Keyboard and mouse

**Recommended** (medium to large data sets ≥ 100 LC-MS files, or IMS-MS in general):

- 64 bit CPU, ≥ 16 Cores (≥3 GHz, Hyper threading), ≥ 64 GB RAM (scales with data files), secondary NVMe SSD
  drive (≥ 1 TB), integrated graphics
- Display 2560 x 1440 pixel or higher
- Internet connection for login and spectral library/machine learning model download
- Keyboard and mouse
- dedicated GPU (CUDA enabled) for accelerated machine learning models (not required)

!!! Info
    Offline login is possible, see [Offline use](services/users.md#offline-use).

!!! Info
    Processing speed scales with CPU cores/threads and speed of the SSD for temporary files. We 
    recommend setting the temporary files directory to a fast, secondary SSD in the mzmine 
    preferences (CTRL+P, **Project -> Preferences**). (see [](getting_started.md#set-user-preferences))

## Software requirements

<!-- markdown-link-check-disable -->

- Up-to-date operating system, e.g., Windows 10 or newer, recent Linux or MacOS (academic only) versions. 
- mzmine does not require a dedicated Java installation, as it is a self-contained Java software with its own Java Virtual Machine. All
requirements are shipped with mzmine.
- Microsoft Visual Studio C++ Redist for Bruker raw data import [download page](https://learn.microsoft.com/de-de/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- MSConvert (on Windows) for native Agilent, Sciex, Waters, Shimadzu, and MOBILion data support [download page](https://proteowizard.sourceforge.io/download.html)

<!-- markdown-link-check-enable -->

## Internet connection

- An internet connection is recommended, but not strictly required for core processing
- Offline user login is possible, see [Offline use](services/users.md#offline-use).
- To allow mzmine to download spectral libraries and the recent versions of machine learing models
for spectral networking using MS2Deepscore and DReaMS, an internet connection is required
- A proxy may need to be set in the **Preferences** if your University/Company uses one (**Project -> Preferences**, CTRL+P)
<!-- markdown-link-check-disable -->
- Required URLS (in case University/Company blocks unknown):
    - https://auth.mzio.io/ must be accessible user login
    - https://zenodo.org/ machine learning models
    - https://djl.ai/ machine learning models
    - https://zenodo.org/ spectral libraries
    - https://external.gnps2.org/gnpslibrary spectral libraries
<!-- markdown-link-check-enable -->

## Operating system compatibility {#compatibility}

### Windows

Currently, all modules are compatible with Microsoft Windows 10 and higher.

Some libraries for the raw data support for vendor-specific formats are only available for Windows.
Read more about data support and [data conversion](data_conversion.md).

### Linux

Some libraries for the raw data support for vendor-specific formats are only available for Windows. 

The Linux version **supports** raw data formats from:
- **Thermo**, **Bruker**, **Waters**

Data from other Vendors may need to be **converted** to the open .mzML format before, including:
- **Agilent**, **Sciex**, **Shimadzu**, **MOBILion**

### macOS

Some libraries for the raw data support for vendor-specific formats are only available for Windows and Linux. 

The macOS version **supports** raw data formats from:
- Thermo

Data from other Vendors may need to be **converted** to the open .mzML format before, including:
- Agilent, Sciex, Shimadzu, MOBILion, Bruker, Waters
