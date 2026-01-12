# Ion libraries

!!! info

    Define new ion libraries, ion types, and ion building blocks in the **Define global ions** tab.
    This tab is described below in more detail, briefly, **ion building blocks** define molecular 
    formulas with their charge state and mass. **Ion types** combine ion building blocks.  

An Ion library defines a list of ion types, each describing what happened to a molecule from
ionization until detection.
This includes:

1. the ionizing adducts, like [M+H]+ or [M+Na]+
2. multimers where multiple molecules stack, like [2M]
3. neutral losses, like [M-H2O]
4. ion clusters, like [M+ACN]

Ion libraries are used throughout mzmine in many modules to define what ion types to consider.
Examples include [Ion Identity Networking (IIN)](../module_docs/id_ion_networking/iin/iin.md) where
the ion library defines ions that are matched pairwise to find two feature list rows where
corresponding ion types describe their mass difference.

## Molecular formulas

In mzmine there are many fields to capture the molecular formula, often just named formula. Special
properties of molecular formulas can be defined in various formats which are provided below:

- Regular formula: C6H12O6 (will be harmonized and cleaned)
- Formula **charge state**: [Fe]+2 [Fe]2+ (Fe)+2 Fe+2 but never (Fe)2+ as this describes 2xFe single
  charge
- **Isotopes**: C4[13]C2H12O6 (hexose with 2x [13]C and 4x [12]C, no need to define mass number on
  major isotopes)
- **Isotopes and charge combined example**: [C[13]CH3O2]-

## Ion building blocks

The smallest unit is an ion building block, which defines the molecular formula, charge, and neutral
mass of an ion modification like an adduct or neutral loss (in-source fragment). Usually the formula
is used as the display name but can be exchanged for an alternative name. This can be useful for
formulas often written in a different order to the convention, like NH4 which would usually be H4N.
The formula is optional, providing an option to declare more complex modifications just by name,
charge, and mass.

## Ion types

An ion type defines the whole ionization and potential in-source modifications to a molecule. It
combines **ion building blocks** to calculate a total mass difference, charge, and added/removed
formulas / isotopes. Ion types also define a multimer count to describe how many molecules [xM] are
clustered together.

# Define global ions tab

This tab has multiple internal tabs to switch between defining ion library, ion types, and ion
building blocks.

## Define ion libraries {#define-libraries}

The list on the left shows all ion libraries, including mzmine defaults and user-defined locally
saved libraries. Select one to see its content ion types on the right. mzmine's default libraries

[//]: # (TODO add screenshots once done and describe rest of the tab)


## Define ion types {#define-types}

[//]: # (TODO add screenshots once done and describe rest of the tab)


## Define ion building blocks {#define-parts}

Define ion building blocks to define the specific charge state and delta mass of a molecular formula
or a more complex change. Either the molecular formula or the name + mass needs to be defined. 

[//]: # (TODO add screenshots once done and describe rest of the tab)




