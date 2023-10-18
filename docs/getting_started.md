# Getting Started

## Installation
The latest version of MZmine 3 can be downloaded [here](https://github.com/mzmine/mzmine3/releases/latest). We provide both installer packages (preferred but might require admin permissions) and portable versions for Windows, macOS and Linux. Windows and macOS users might need to confirm to trust software from an unknown source.

!!! info
  
    MZmine comes integrated with _Java Runtime Environment_; therefore, the local _Java_ installation has no impact on MZmine. 

## Set temporary file directory
MZmine generates a significant amount (several gigabytes) of temporary files during processing. Therefore, we recommend to set the temporary file directory to a local drive (preferably SSD) with enough free space. To do so, go to '**Project → Set preferences → General → Temporary file directory**' and browse the desidered directory. On Windows, old temporary files are deleted when a new MZmine session is started.

!!! warning

    Changes in the temporary file directory require a restart of the software to take effect.

## Running MZmine
MZmine provides a user-friendly and interactive [graphical user interface](main-window-overview.md) (GUI) for data exploration, workflow optimization and results validation. Moreover, processing pipelines (including data import/export) can be run with a few clicks using the [batch mode](workflows/batch_processing/batch-processing.md). Finally, MZmine can also be run through the [command-line interface](commandline_tool.md) (CLI), which enable its integration into fully automated data analysis pipelines (e.g., QC systems).

## Useful resources
**TO-DO**



**TO-MOVE**
## Older MZmine versions on macOS
If running MZmine versions prior to 3.4.0, please see here.

MZmine versions prior to 3.4.0 lack macOS signining. Therefore, users need to allow MZmine
in the macOS Gatekeeper protection by running the following command in the terminal from the
Applications folder.

- Download MZmine and click the MZmine.dmg installer - Drag and drop MZmine into the Applications
  folder
- Open the Applciations folder, right click (CTRL click) anywhere, e.g., on the MZmine icon, and
  choose "New Terminal at folder" from the context menu
- Run the provided command to tell macOS to trust the installed version of MZmine. The terminal
  directory has to be the Applications folder. (Depending on the actual folder use or omit the `../`
  to jump to the parent directory).
- Approve command with user password
- Start MZmine

```
sudo xattr -cr ../MZmine.app

# if this fails try
# the app will appear in the security preferences and you will be able to choose the "Open anyway" option
sudo xattr -d com.apple.quarantine /Applications/MZmine.app
```

![](img/install_mac1.png){: style="height:150px"} ![](img/install_mac2.png){: style="width:150px"}

The Terminal does not output any log or message.
![](img/install_mac3.png)



{{ git_page_authors }}