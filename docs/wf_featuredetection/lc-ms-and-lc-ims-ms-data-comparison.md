# Graphical comparison of LC-MS and LC-IMS-MS data

Classic LC-MS data consists of three dimensions: m/z, intensity, and retention time. At every
retention time, a whole mass spectrum is acquired (yellow). Putting all scans together creates a
three-dimensional plane. By slicing the three-dimensional data at a single m/z (+- a tolerance),
EICs can be created (green).

![lcmsdata](../img/imsworkflow/lcmsdataformat.png)

On the other hand, ion mobility resolved data consists of a three-dimensional data plane at each
retention time. The three dimensions being m/z, intentsity, and mobility (as drift time (ms) or
inverse reduced mobility 1/k0 [Vs/(cm^2)]). The 3D projection of regular LC-MS data can be created
by summing all mobility scans of a frame to create a frame spectrum.
(see [Mobility scan merging](mobility-scan-merging.md))

![lcimsmsdata](../img/imsworkflow/lcimsmsdataformat.png)
