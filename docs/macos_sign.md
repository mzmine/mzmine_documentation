## Older MZmine versions on macOS
Macos signature for MZmine was introduced with version 3.4.0. Therefore, users need to allow MZmine
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
