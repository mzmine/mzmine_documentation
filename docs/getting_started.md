# Getting Started

## Installation
The latest version of MZmine 3 can be downloaded [here](https://github.com/mzmine/mzmine3/releases/latest). We provide both installer packages (preferred but might require admin permissions) and portable versions for Windows, macOS and Linux. MZmine comes integrated with _Java Runtime Environment_; therefore, the local _Java_ installation has no impact on MZmine. Windows and macOS users might need to confirm to trust software from an unknown source.

!!! warning
  
    Macos signature was introduced in MZmine version 3.4.0. If you are running older versions of the software, you will need to allow MZmine in the macOS Gatekeeper (see [here](macos_sign.md)).
 

## Set temporary file directory
MZmine generates a significant amount (several gigabytes) of temporary files during processing. Therefore, we recommend to set the temporary file directory to a local drive (preferably SSD) with enough free space. To do so, go to '**Project → Set preferences → General → Temporary file directory**' and browse the desidered directory. On Windows, old temporary files are deleted when a new MZmine session is started.

!!! warning

    Changes in the temporary file directory require a restart of the software to take effect.

## Running MZmine
MZmine provides a user-friendly and interactive [graphical user interface](main-window-overview.md) (GUI) for data exploration, workflow optimization and results validation. Moreover, processing pipelines (including data import/export) can be run with a few clicks using the [batch mode](workflows/batch_processing/batch-processing.md). Finally, MZmine can also be run through the [command-line interface](commandline_tool.md) (CLI), which enable its integration into fully automated data analysis pipelines (e.g., QC systems).

## Useful resources
If you are new to mass spectrometry data processing in MZmine, checkout our [learners corner](learners_corner.md) with tutorial videos, webinars and other resources!

New MZmine users can also take advantage of the new [_Processing wizard_](wizard.md) for the quick and beginner-friendly generation of data processing workflows for different MS platforms.


{{ git_page_authors }}