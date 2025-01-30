# MRM aligner

The MRM aligner offers feature alignment that is specific to the MRM workflow. This aligner allows the option to only align features that only contain the same MRMs (see [Only allow matches to same MRM](#only-allow-matches-to-same-mrm)).

In principle, the [Join aligner](../align_join_aligner/join_aligner.md) can be used to align MRM files, but will not take the transitions into account. However, the Join aligner can be used to align an already aligned MRM feature list to an HRMS feature list, although this would require really stable chromatography, as scoring by _m_/_z_ may not produce the desired results.

## Parameters

#### Feature lists
Select the feature lists that shall be aligned. All feature lists must contain only MRM features.

#### m/z tolerance (sample-to-sample)
The _m_/_z_ tolerance between two MRM features in different samples. As the _m_/_z_ values in MRM acquisitions usually resemble the set _m_/_z_ in the acquisition software, this parameter may be set smaller than for full-scan low resolution data.

#### Retention time tolerance
The RT tolerance for the same feature in two different samples/raw files. 

#### Only allow matches to same MRM
If this parameter is selected, alignment of two rows is only allowed, if:

    a. they have the same number of transitions
    b. their transitions have the same Q1 and Q3 masses
    c. they have the same quantifier ion mass
    
#### Feature list name 

The name of the created aligned feature list.

#### Original feature list

Specify if the feature lists that are aligned in this step shall be removed from the project or if they should be retained. 

## Algorithm

The MRM aligner searches for matches in all feature lists within the given _m_/_z_ and RT tolerances. All matching features will then be checked for the same MRMs, if the [Only allow matches to same MRM](#only-allow-matches-to-same-mrm) parameter is enabled. In case there are multiple rows, that match the criteria, only the RT will be used to find the best match.

After the alignment, all aligned rows will be set to the same quantifier ion _m_/_z_. By default, this is the quantifier of the most intense feature. If the [Only allow matches to same MRM](#only-allow-matches-to-same-mrm) was disabled and the most intense feature has a quantifier transition set, that is not available in all aligned features, an error will be produced and the alignment will fail, because the results would not be valid. To circumvent that, only align features with the same MRM, or manually set a quantifier ion that appears in all samples using the [Set MRM quantifiers](../mrm_setquant/mrm-set-quant-mass.md) module prior to the alignment step.
