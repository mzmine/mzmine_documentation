# Troubleshooting

## GUI freezes

The graphical user interface freezes sometimes on remote desktops if the user logs out and logs in
again. This is a known issue and might be fixed in future JavaFX versions.

## MZmine does not start

Maybe the MZmine configuration got corrupted (broke). Delete it and reinstall MZmine. The *
*.mzmine3.conf** file can be found in the user folder and might be hidden. On Windows, activate "
Show hidden items" in the Explorer/View menu.

## mzML files not importing

An illegal character might exist in the mzML file. When converting the raw data files to mzML, the
path of the file is added to the resulting mzML file. The path may contain characters that are not
parsed correctly by MZmine.

Solution: Reconvert the file and place the input and output directory to a path with only Roman
characters.

## Thermo raw files not importing

Error message usually contains "No scans found".

Solution: Search for the "mzmine_thermo_raw_parser" folder in the mzmine temp folder and the system
temp folder and delete it.

## Scans not sorted in retention time dimension

This issue often occurs with raw data from Waters instruments. We recommend re-converting the files
using the [Waters data connect tool](data_conversion.md#waters).

## Scans were recognised as empty

This is displayed as a warning and means that some scans did not contain any data. This is not
considered as an error. The warning **may** indicate that a threshold was too high, if conversion
was applied. You may consider lowering said threshold. If no thresholding was applied, consider
this a false positive.

## Zero intensity values in scans

0 intensities in scans.

This error occurs when converting files using an old MSConvert version and the "Peak picking" filter
being used after the "title maker". This caused the wrong peak picking algorithm to be used and not
just adds zero values but also causes falsely recognised m/z values. We highly recommend to
re-convert the files with the most recent MSConvert version.

## Reporting issues

Report issues on the [MZmine GitHub](https://github.com/mzmine/mzmine3/issues), providing all
information to reproduce the issue.

**This might include**

- **Input data**? provide example file
- ** Batch file** defining processing steps and settings
- attach the log file located in the user folder: **mzmine_0_0.log**
- **Expected behavior**
- **Issue** 
