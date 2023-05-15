# Command-line interface (CLI) for headless batch mode
Command-line arguments offer a variety of options that generally override the corresponding parameters in the preferences.

## Windows

An easy way to start MZmine with arguments is to create a shortcut to the MZmine.exe, right-click, and define the target with additional arguments. This example runs MZMine in batch mode (headless), imports the specified batch file, overrides the memory management to **none** (which is the default), effectively using memory mapping to store and access spectral, centroid, and feature data from temporary files stored in the defined temp directory. By leaving out the _memory_ or _temp_ arguments, the values stored in the current _preferences_ file will be used, or the default values if no _preferences_ file was found.  

**Process all .mzML files in a folder by the provided batch file**
```
"C:\Program Files\MZmine\MZmine.exe" -batch "D:\batch\my_batch_file.xml" -input "D:\Data\*.mzML"
```

**Defining the temp folder, otherwise uses the one specified in local configuration**
```
"C:\Program Files\MZmine\MZmine.exe" -batch "D:\batch\my_batch_file.xml" -temp "D:\tmpmzmine"
```

**Start MZmine batch with memory mapping (DEFAULT)**
```
"C:\Program Files\MZmine\MZmine.exe" -batch "D:\batch\my_batch_file.xml" -memory none -temp "D:\tmpmzmine"
```


**Start MZmine batch on machines with enough memory (RAM) with -memory all** this will disable memory mapping to temporary files. 
```
"C:\Program Files\MZmine\MZmine.exe" -batch "D:\batch\my_batch_file.xml" -memory all -temp "D:\tmpmzmine"
```

## macOS
If the app was installed to the _Applications_ folder, run this command in the terminal to run a batch file:
```
/Applications/MZmine.app/Contents/MacOS/MZmine -batch /path/to/batch_file.xml
```

```
/Applications/MZmine.app/Contents/MacOS/MZmine -batch /path/to/batch_file.xml -input "/path/to/data/*.mzML"
```

## Argument table

| Argument | Options (**default**) | Description |
| --- | --- | --- |
| -b and -batch | a path, e.g. "D:\batch.xml" | Path to batch file |
| -i and -input | a txt file or glob pattern, e.g., "D:\\Data\\*.mzML" | input data files. Either defined in a .txt text file with one file per line or by glob pattern matching. To match all .mzML files in a path: -i "D:\\Data\\*.mzML" |
| -m and -memory | **none**, all, features, centroids, raw, masses_features | Defines what data is kept in memory (RAM) or otherwise memory mapped to the temp directory. Generally this setting should be _none_. If memory is no issue this option might be set to _all_ process all spectral and feature data in memory. The option _masses_features_ keeps centroid mass lists and features in memory while memory mapping raw spectral data. |
| -t and -temp | a path, e.g., "-temp "D:\tmpmzmine\" | The defined directory should be on a fast drive (usually SSD > HDD > network drive) with enough free space. Local drives are usually preferred. MZmine uses memory mapping to efficiently store and access spectral and feature data. This can lead to a considerable temporary consumption of disk space. Make sure that the selected drive has enough space (maybe 20 GB + 1 GB/10 files; generously over estimated). |
| -p and -pref | a path, e.g., "D:\config.xml" | An MZmine configuration file in xml format. The general preferences. | 

{{ git_page_authors }}
