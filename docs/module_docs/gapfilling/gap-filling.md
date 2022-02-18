# Gap-filling

Some chromatographic peaks may not be detected in every sample for several reason:
- Reason 1
- Reason 2
- Reason 3


- This causes undesirable gaps (missing values) in the aligned feature table.
- To tackle this issue, a value for the peak needs to be imputed
- A simple gap-filling approach is to integrate the area where the peak is expected but not detected
- These areas usually correspond to spectral noise
- By doing so, no bias is introduced
- The gap-filled feature table can now be used in downstream data analysis
