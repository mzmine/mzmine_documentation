# Annotation graphics export

## Export in batch mode (head less, CLI)

!!! warning
    To export the annotation graphics in head less mode, a display needs to be configured to render the
    graphics.
    If you are running on a desktop computer, this is usually the case. 
    If you are running on a server, e.g., ubuntu, you can use GTK and run it via Xvfb.

!!! note
    This export only covers annotated features. Features without an annotation will not be exported.

## Parameters

#### Export directory
Set a parent directory to which the graphics shall be exported. A sub directory with the name of the selected feature list will be created by the export module. An individual file will be created for each of the exported graphics. The file names follow this pattern:

`%d-%s_mz-%s_score-%s_%s_match-%d`

which will be replaced like this:

`<featureid>-<graphic type>_mz-<feature mz>_score-<match score>_<additional note>_match-<match number>`

#### Feature lists

Select the feature lists to export

#### Number of matches to export

Define how many matches per annotation type (supported: spectral library matches and lipid annotations) shall be exported to a graphic. The match number will refer to the ranking in an annotation type.

#### DPI scaling factor
Defines a scaling factor for pixels in exported png images.

#### Export shapes

If selected, chromatogram charts will be exported for each row.

#### Export mobilograms

If selected, mobilogram charts will be exported for each row.

#### Export images

If selected, each feature will be exported as ion image (for imaging data files).

#### Export lipid matches
If selected, a chart of the matched lipid signals in the MS2 spectrum will be exported.

#### Export spectral library matches
If selected, the spectral library match will be exported as a mirror plot with metadata information. The png export will contain more metadata information, but cannot be edited. The pdf export can be edited using a vector graphics tool.

#### Export PDF
If selected, the plots will be exported as PDF.

#### Export PNG
If selected, the plots will be exported as PNG.

#### Chart export parameters
Define chart export parameters.
