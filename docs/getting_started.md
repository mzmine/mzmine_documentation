# Getting Started

## Installation
The latest version of MZmine 3 can be downloaded [here](https://github.com/mzmine/mzmine3/releases/latest). We provide both installer packages (preferred but might require admin permissions) and portable versions for Windows, macOS and Linux. Windows and macOS users might need to confirm to trust software from an unknown source.

!!! info
  
    MZmine comes integrated with _Java Runtime Environment_; therefore, the local _Java_ installation has no impact on MZmine. 

## Set User Preferences
Before start processing your data, we recommend to [set up a few things](#set-user-preferences) to ensure a smooth running of the software:

1. Set a temporary file directory. Go to _Project_ → _Set preferences_ → _Temporary file directory_.
   This requires a restart to take effect.
    2. We recommend setting the directory to an SSD with enough space for fast processing and
       visualizations.
    3. On Windows, old temporary files are deleted when a new session is started.
2. MZmine 2 projects cannot be imported due to changes in the data structure.
3. MZmine 2 batch files cannot be imported due to parameter optimizations.

## Start processing 

An excellent place to start would be [MZmine video tutorials on YouTube](https://www.youtube.com/@mzmineproject/playlists).

A quick insight to data processing workflows can be found
here: [LC-MS workflow](workflows/lcmsworkflow/lcms-workflow.md)
or [LC-IMS-IMS workflow](workflows/imsworkflow/ion-mobility-data-processing-workflow.md)

You can also check out the new processing wizard under [Processing wizard](wizard.md) in the main menu. 

## Running MZmine

MZmine provides a user-friendly graphical user interface (GUI) that facilitates data exploration, batch optimization, and results validation. If the batch processing is optimized and the goal is to solely produce the output files without the need for GUI, we recommend [running MZmine as a command-line tool](commandline_tool.md). 



## Older MZmine versions on macOS

Currently, MZmine 3 lacks a signature for macOS. While we are working on this, user can allow MZmine
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
