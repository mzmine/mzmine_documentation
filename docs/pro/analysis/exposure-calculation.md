# Exposure calculation {#calculate-exposure-from-quantified-results}

Exposure calculation converts a completed quantification result into a stated exposure scenario and compares it with a reference value you supply. It records the arithmetic and assumptions; the result is not a toxicological assessment or regulatory decision.

## What you need {#prepare-the-inputs}

First complete [Quantification](quantification.md) in mzmine. Exposure calculation uses its result from the same shared feature table; manually typed measurement values cannot replace that result. Study samples must not have been designated as calibrators or QC samples in quantification. These roles derive from the calibration and QC lists; if the setup was wrong, correct it and repeat quantification.

The use scenario must match the quantified basis:

| Quantified basis | Scenario input |
| --- | --- |
| Amount per device | Devices used per day |
| Amount per mass of original sample | Sample mass used per day |
| Concentration in measured solution | Solution volume used per day |

Body mass is needed when the reference is expressed per kilogram of body mass. The scenario description and a reference value, unit, source URL, version, and confirmation that the reference applies to the scenario are also needed. mzassist accepts reference units of ng/day, µg/day, ng/kg/day, and µg/kg/day. Preparation and dilution corrections belong to the preceding [quantification setup](quantification.md#prepare-the-calibration), where the measured quantity is established.

## Calculate with mzassist {#ask-mzassist}

1. Ask mzassist to use the completed quantification. For example:

    > Use this completed quantification result for the stated use scenario. Show the eligible samples, quantity basis, unit conversions, and reference source before calculating the comparison.

2. mzassist checks the completed quantification and the metadata you approved for sharing. Provide the scenario and reference facts it still needs. If sample-preparation corrections need changing, update and repeat quantification first.
3. Confirm the proposed samples, conversions, reference, and calculation in chat. Ask mzassist to calculate and open the results.
4. Inspect selected samples, converted quantities, units, assumptions, reference ratio, and unavailable or flagged values. Surrogate-reference-equivalent quantities remain estimates and require explicit acceptance before inclusion. Unsupported units, incompatible scenario inputs, or other flags can exclude a value from the comparison.
5. Use **Save table (CSV)** and **Save calculation record (JSON)** in the result view, and preserve the reference source alongside them. See [Save and reproduce your work](../mzassist-saving.md).

## Interpretation {#check-the-calculation}

As an **arithmetic illustration**, 2 ng/device used at 3 devices/day gives 6 ng/day. A hypothetical reference of 3 ng/day gives a ratio of 2. These numbers are not a recommended scenario or reference value. Being above or below the supplied reference describes this calculation only.

{{ git_page_authors }}
