# **Online compound database search**

**Module is currently removed and no longer maintained.**

:construction: This module has known bugs and is being updated, which might affect its functionality

## **Description**

:material-menu-open: **Feature list methods → Annotation → Search precursor mass → Online compound database search**

This module allows identification of peaks or whole peak lists using an on-line compound database. Databases are queried for the calculated neutral mass of the peak and matching compounds are returned.

[//]: # (TODO Add comment about DBs and Sirius)

:material-lightbulb: If a user is interested in more comprehensive online compound database search, they can export their data to [Sirius](https://bio.informatik.uni-jena.de/software/sirius/) software. 

## **Parameters**

#### **Database**

On-line database to search ([list of the available databases](#currently-supported-databases)).

#### **Ionization type**

Type of ionization that produced the peak subjected to identification. 

#### **Number of results**

Limit for the number of results to be retrieved from the on-line database.

#### **m/z tolerance**

Maximum allowed m/z difference to set an identification to a peak.

#### **Isotope pattern filter**

If selected, only results which fit the required isotope pattern similarity score will be returned.

### **Currently supported databases** 

Supported databases are listed below. Support for other databases may be implemented as additional plugins.

<!-- markdown-link-check-disable -->
- **KEGG**

    KEGG database (<a>http://www.genome.jp/kegg/</a>) contains metabolites and other biomolecules present in natural metabolic pathways.

- **PubChem**

    PubChem database (<a>http://pubchem.ncbi.nlm.nih.gov/</a>) contains millions of chemical compound structures. 

- **HMDB**

    The Human Metabolome Database (HMDB) (<a>http://www.hmdb.ca/</a>) contains over 7,000 known metabolites found in human body. 

- **YMDB**

    The Yeast Metabolome Database (YMDB) (<a>http://www.ymdb.ca</a>) is a manually curated database of small molecule metabolites found in or produced by Saccharomyces cerevisiae (also known as Baker’s yeast and Brewer’s yeast).

- **LipidMaps**

    LipidMaps Structure Database (LMSD) (<a>https://www.lipidmaps.org/databases/lmsd</a>) is a database of structures and annotations of biologically relevant lipids, containing over 47000 different lipids.

- **MassBank.eu**

    MassBank (<a>https://massbank.eu/MassBank/</a>) is an open source mass spectral library for the identification of small chemical molecules of metabolomics, exposomics and environmental relevance. The majority of MassBank contents now features high-resolution mass spectrometry data.

- **ChemSpider**

    The ChemSpider database (<a>http://www.chemspider.com/</a>) contains over 67 million compounds. To search ChemSpider you must provide a "Security key" from your ChemSpider API account. If you don't have an account, please register at <a>https://developer.rsc.org</a>.

- **MetaCyc**

    MetaCyc (<a>https://metacyc.org/</a>) is a curated database of experimentally elucidated metabolic pathways from all biological domains. MetaCyc currently contains 2937 pathways, 17,780 reactions and 18,124 metabolites.

<!-- markdown-link-check-enable -->

{{ git_page_authors }}
