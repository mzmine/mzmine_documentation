# Calculate exposure from quantified results

Use this calculation to convert a native quantification result into a stated exposure scenario and
compare it with a reference value you supply. It records the arithmetic and assumptions; the result
is not a toxicological assessment or a regulatory decision.

## Prepare the inputs

First complete [quantification](quantification.md) in mzmine. Use that result from the same shared
feature table; manually typed measurement values cannot replace the native quantification result.
Select study samples that were not designated as calibrators or QC samples in quantification.
mzmine derives those roles from the calibration/QC lists, so there is no role field to edit afterward.
If the setup was wrong, correct it and repeat quantification before continuing.

Match the use scenario to the basis of the quantified result:

| Quantified basis | Scenario input |
| --- | --- |
| Amount per device | Devices used per day |
| Amount per mass of original sample | Sample mass used per day |
| Concentration in measured solution | Solution volume used per day |

Supply body mass when the reference is expressed per kilogram of body mass. Include relevant
preparation/dilution assumptions, a description of the scenario, and the selected reference's value,
unit, source, and version. Confirm that the reference applies to the question; mzassist does not
establish that applicability for you.

## Ask mzassist

> Use this completed quantification result for the stated use scenario. Show the eligible samples,
> quantity basis, unit conversions, and reference source before calculating the comparison.

## Check the calculation

As an **arithmetic illustration**, 2 ng/device used at 3 devices/day gives 6 ng/day.
A hypothetical reference of 3 ng/day would give a ratio of 2. These numbers are not a recommended
exposure scenario or reference value.

Inspect the selected samples, converted quantities, units, assumptions, reference ratio, and all
unavailable/flagged values. Surrogate-reference-equivalent quantities remain estimates and require
explicit acceptance before inclusion. Unsupported units, incompatible scenario inputs, or other
flags can exclude a value from the comparison.

Being above or below the supplied reference describes this calculation only. Preserve the native
calculation record and the reference source alongside the exported table.

{{ git_page_authors }}
