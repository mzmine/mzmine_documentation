# ADAP chromatogram builder

![adap chromatogram builder](../img/lcmsworkflow/adapchromatogrambuilder.png)

### Scan selection

The scan selection parameter specifies the scans that shall be processed for feature detection.
Usually, setting the ms level to 1 is sufficient. If a calibration segment is present, it can be cut
out via the retention time filter in the scan selection.

### Min group size in number of scans

This parameter specifies the number of consecutive detections of the same m/z value in a
chromatographic peak (rt dimension). This means that a single m/z has to be detected in, e.g, 5
scans with an intensity higher than zero. This parameter helps to filter noise. Usually no less than
5 should be set here if the MS1 acquisition rate is sufficient.

### Group intensity threshold

Specifies a minimum intensity that the number specified
by [min group size](#min-group-size-in-number-of-scans) have to exceed. In this example, the intensity in
at least 5 scans must be above 5E2.

### Minimum highest intensity

The highest point of a potential EIC must exceed this value.

### Scan to scan accuracy (m/z)

The **m/z tolerance** specifies the scan-to-scan tolerance for EICs. This tolerance depends on the
mass accuracy and resolution of the instrument. Usually, a good starting point for optimisations are
0.005 and 5-10 ppm for Orbitrap instruments, while 0.005 and 10-15 ppm can be used for TOF
instruments.
