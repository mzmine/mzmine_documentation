# Command-line interface (CLI) for headless batch mode
Command-line arguments offer a variety of options that generally override the corresponding parameters in the preferences.

## Selecting a user

Running mzmine in CLI mode requires a [user](services/users.md). Either login via graphical-user interface (GUI) or via command-line argument **-login** (web browser support required) or via **-login-console**. 
Then locate the user file in your system USER directory under /.mzmine/users/. The most recently active user is automatically selected for mzmine processing,
but an .mzuser file can be passed in as command-line argument to **-user**.


## Windows

For command-line mode, the mzmine_console.exe is preferred as it will print the logging output to the console. 

An easy way to start mzmine with arguments is to create a shortcut to the mzmine.exe or the mzmine_console.exe, right-click, and define the target with additional arguments. This example runs mzmine in batch mode (headless), imports the specified batch file, overrides the memory management to **none** (which is the default), effectively using memory mapping to store and access spectral, centroid, and feature data from temporary files stored in the defined temp directory. By leaving out the _memory_ or _temp_ arguments, the values stored in the current _preferences_ file will be used, or the default values if no _preferences_ file was found.  

**Login to a user in command-line mode**
```
# login in browser
"C:\Program Files\mzmine\mzmine_console.exe" -login

# or in the terminal
"C:\Program Files\mzmine\mzmine_console.exe" -login-console 
```


**Process all .mzML files in a folder by the provided batch file**
```
"C:\Program Files\mzmine\mzmine_console.exe" -user "D:\user\testuser.mzuser" -batch "D:\batch\my_batch_file.xml" -input "D:\Data\*.mzML"
```

**Defining the temp folder, otherwise uses the one specified in local configuration**
```
"C:\Program Files\mzmine\mzmine_console.exe" -user "D:\user\testuser.mzuser" -batch "D:\batch\my_batch_file.xml" -temp "D:\tmpmzmine"
```

**Start mzmine batch with memory mapping (DEFAULT)**
```
"C:\Program Files\mzmine\mzmine_console.exe" -user "D:\user\testuser.mzuser" -batch "D:\batch\my_batch_file.xml" -memory none -temp "D:\tmpmzmine"
```


**Start mzmine batch on machines with enough memory (RAM) with -memory all** this will disable memory mapping to temporary files. 
```
"C:\Program Files\mzmine\mzmine_console.exe" -user "D:\user\testuser.mzuser" -batch "D:\batch\my_batch_file.xml" -memory all -temp "D:\tmpmzmine"
```

## macOS
If the app was installed to the _Applications_ folder, run this command in the terminal to run a batch file:
```
/Applications/mzmine.app/Contents/MacOS/mzmine -user "path/to/testuser.mzuser" -batch /path/to/batch_file.xml
```

```
/Applications/mzmine.app/Contents/MacOS/mzmine -user "path/to/testuser.mzuser" -batch /path/to/batch_file.xml -input "/path/to/data/*.mzML"
```

## Linux
If mzmine was installed (see instructions) correctly, run the code below to start mzmine in GUI mode or CLI batch mode:
```bash
/opt/mzmine/bin/mzmine
# some older versions or bad installations may be in:
# /opt/mzmine-linux-installer/bin/mzmine
```

```bash
# login and run batch
/opt/mzmine/bin/mzmine -login-console -batch /path/to/batch_file.xml
```

## Argument table


| Argument          | Options (**default**)                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -h and -help      | no argument                                              | show help                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -u and -user      | a path, e.g., "D:\myuser.mzuser"                         | Path to an .mzuser file to login a user. This file is copied to the users directory. To obtain a user file, login in the mzmine graphical user interface (GUI) or command line interface (CLI). User files can be found in your system USER directory in /.mzmine/users/ after login. A user can be used in an offline environment for a certain duration.                                                                                     |
| -login            | no argument                                              | Use the command-line to login to a user. This will open the login website in the system internet browser, if supported, or prompts an input for the user credentials into the console. After successful login, a user file will be copied to your system USER directory in /.mzmine/users/. And the current user will be saved to the configuration. The created user file can be accessed with the -user argument on the next startup.        |
| -login-console    | no argument                                              | Use the command-line to login to a user. This option prompts the user for username and password. After successful login, a user file will be copied to your system USER directory in /.mzmine/users/. And the current user will be saved to the configuration. The created user file can be accessed with the -user argument on the next startup. |
| -list-users       | no argument                                              | List all users available on this system. The users are read from the system USER directory /.mzmine/users/.                                                                                                                                                                                                                                                                                                                                    |
| -b and -batch     | a path, e.g., "D:\batch.xml"                             | Path to batch file that will be run in command-line mode.                                                                                                                                                                                                                                                                                                                                                                                      |
| -i and -input     | a txt file or glob pattern, e.g., "D:\Data\*.mzML"       | input data files. Either defined in a .txt text file with one file per line or by glob pattern matching. To match all .mzML files in a path: -i "D:\\Data\\\*.mzML"                                                                                                                                                                                                                                                                            |
| -l and -libraries | a txt file or glob pattern, e.g., "D:\Data\*.json"       | spectral library files. Either defined in a .txt text file with one file per line or by glob pattern matching. To match all .json or .mgf files in a path: -libraries "D:\\Data\\\*.json"                                                                                                                                                                                                                                                      |
| -o and -output    | An output path and base filename, e.g., "D:\basename"    | The base file name will be extended by default module names to export all files.                                                                                                                                                                                                                                                                                                                                                               |
| -m and -memory    | **none**, all, features, centroids, raw, masses_features | Defines what data is kept in memory (RAM) or otherwise memory mapped to the temp directory. Generally this setting should be _none_. If memory is no issue this option might be set to _all_ process all spectral and feature data in memory. The option _masses_features_ keeps centroid mass lists and features in memory while memory mapping raw spectral data.                                                                            |
| -t and -temp      | a path, e.g., "-temp "D:\tmpmzmine\"                     | The defined directory should be on a fast drive (usually SSD > HDD > network drive) with enough free space. Local drives are usually preferred. mzmine uses memory mapping to efficiently store and access spectral and feature data. This can lead to a considerable temporary consumption of disk space. Make sure that the selected drive has enough space (maybe 20 GB + 1 GB/10 files; generously over estimated).                        |
| -p and -pref      | a path, e.g., "D:\config.xml"                            | An mzmine configuration file in xml format. The general preferences.                                                                                                                                                                                                                                                                                                                                                                           | 
| -threads          | int number of threads or 'auto'                          | replace the preference parameter with either 'auto' to detect the number of available cores - or an int number of threads for processing.                                                                                                                                                                                                                                                                                                      |


{{ git_page_authors }}
