# **Spectral similarity measures**

## **Weighted cosine spectral similarity**

The most common spectral similarity measure for library search is the **weighted cosine similarity**. Generally,the cosine similarity is calculated as following:

$$similarity = cos\theta = (u \cdot v) / (\sqrt{(sum(u^2))} * \sqrt{(sum(v^2))})$$

In case of weighted cosine similarity, the previous formula is modified according to the weighting function. In case of weighting function in form $m/z^a*{Intensity}^b$ (where a, b are weights) the weighted cosine similarity is calculated as follows:

$$weighted\;similarity = (u' \cdot v') / (\sqrt{(sum(u^2))} * \sqrt{(sum(v^2))})$$

$$u' = sum(u_i) = sum(m{u_i}^a*I{u_i}^b)$$

$$v' = sum(v_i) = sum(m_{v_i}^a*I_{v_i}^b)$$

where u and v are the aligned vectors of the two spectra.

It is used to determine the similarity between two spectra (usually library and query spectra). Both spectra are turned into vectors and cosine similarity is calculated by division of vectors dot product over cosine value of the angle between them.

## **Composite weighted cosine spectral similarity (identity)**

This similarity measure can be especially useful for very reproducible generation of spectra (GC-EI-MS). This measure is modified by a ratio based on the relative intensities of adjacent m/z signals in the two spectra.

Composite weighted cosine similarity is calculated as follows:

$$composite\;similarity = \frac{N*{cosine\;similarity}+overlap*{ratio\;factor}}{N+overlap}$$

$$ratio\;factor=\frac{min(r_{lib},r_{query})}{max(r_{lib},r_{query})}$$

$$r_{lib}=I_i(lib)/I_{i-1}(lib);\;r_{query}=I_i(query)/I_{i-1}(query)$$

where $N$ - number of signals in a query spectrum, cosine similarity is calculated as described [previously](#weighted-cosine-spectral-similarity), overlap - number of matching signals in query and library spectra, $ratio\;factor$ - relative intensities ratio, $r_{lib}$ - relative ratio of adjacent signals in a library spectrum, $r_{query}$ - relative ratio of adjacent signals in a query spectrum.

[//]: # (TODO So is it abundance or intensities)

It is used to determine the similarity between two spectra (usually library and query spectra).

## **Parameters**

#### **Weights**

For calculating the cosine similarity, different weighting strategies for  m/z and signal intensities can be applied.

[//]: # (Weights are applied to m/z and intensity as follows $m/z^a*{Intensity}^b$.)

Several weighting schemes are available:

- None $m/z^0*I^1$ (weighting only by intensities)
- SQRT $m/z^0*I^0.5$ (weighting only by intensities)
- MassBank $m/z^2*I^0.5$
- NIST11 (LC) $m/z^{1.3}*I^{0.53}$
- NIST (GC) $m/z^3*I^{0.6}$

:material-lightbulb: Choice of the similarity measure depends on your data, and intensity-based schemes might work better on homogenous datasets. However, recommended approach for choosing the weighting scheme would be trial-and-error.

#### **Minimum cosine similarity**

This option defines the minimum accepted similarity  score that is taken into account for annotation. The similarity score depends on the data handling of unmatched signals.

#### **Handle unmatched signals**

Signals that only occur within one scan (query OR library entry) can be handled in different ways to affect the cosine similarity and controlling the quality  of matching results.

- KEEP ALL AND MATCH TO ZERO (default)

    This is the standard conservative approach where all unmatched signals weigh negatively on the score. It is used for both GC-EI-MS and MS^2^ spectra.

- REMOVE ALL

    The opposite option that discards all unaligned signals, which increases the similarity score artificially.

    :material-lightbulb: This option is only feasible if both the library and query spectrum are considered to be complex mixtures. Therefore, the next two options are more conservative.

- KEEP LIBRARY SIGNALS

    Results in discarding all unaligned signals of the query scan, whereas all unaligned library signals are matched to zero, setting the library spectrum as the ground truth.

    :material-lightbulb: Here, the negative impact of contaminating signals in the query scans are reduced. This might be helpful for mixed spectra of multiple compounds, especially during imaging techniques without any further separation or all ion fragmentation/data independent fragmentation workflows.

- KEEP EXPERIMENTAL SIGNALS

    Results in discarding all unaligned signals of the library scan, whereas all unaligned query signals are matched to zero.

    Has reversed effects compared to the previous option.

{{ git_page_authors }}
