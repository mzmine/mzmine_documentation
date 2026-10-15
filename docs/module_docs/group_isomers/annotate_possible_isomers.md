# Annotate possible isomers

## Description

This Module searches for signals with a very similar m/z within user-defined retention time
boundaries and annotates them to allow easier identification of potential isomeric features. Ion
mobility spectrometry helps to resolve such potential isomers.

## Parameters

#### Feature lists

Select the feature lists you want to be analyzed.

#### mz tolerance

The maximum allowed mz tolerance between two potential isomeric features.

#### RT tolerance

Maximum allowed tolerance for potential isomeric signals.

#### Maximum mobility change

Specifies the maximum change of mobility for a possible isomer. Used to rule out fragmented
multimers. 

#### Skip multimer fragments

If checked, the results will be refined to not falsely annotate fragments of multimers as isomeric
compounds. Requires prior use of the Ion identity networking module. The given tolerance will be
applied between a possible multimer and the multimer fragment.

#### Quality parameters - Minimum intensity

Minimum intensity of a possible isomer to be annotated.

#### Quality parameters - Minimum number of data points

Minimum number of data points in ion mobility trace to be recognised as a isomeric compound.
Used to filter out noise after resolving.

![multiimsvisualiser.png](multiimsvisualiser.png)
