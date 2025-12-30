# Phylogenetic Trait Learning for Cyanotoxin Prediction

Phylogeny-aware machine learning model that predicts cyanotoxin presence by learning statistical associations between clade structure and tip-level traits

---

## Goal

This Python script aims to infer the probability of cyanotoxin presence by learning how toxin-related traits distributed across cyanobacterial taxa interact with phylogenetic structure to produce clade-level signals associated with toxin production.

---

## Description

Here, I implement a model that acts as a phylogenetic trait predictor. It learns statistical associations between tip-level characters (e.g., the presence of toxin biosynthesis genes like `mcy`, `cyr`, `sxt`, and `ana`; the copy number of cyanotoxin gene clusters; or prior knowledge of toxin production among specific taxa) and the underlying phylogenetic structure of the tree. By training the model on existing phylogenies with tip-level cyanotoxin data, it learns which tip-level features and phylogenetically aggregated patterns are most predictive of cyanotoxin presence.

---

## Rationale

A phylogeny contains essential information for cyanotoxin detection, since

- cyanotoxin production is often clade-structured rather than randomly distributed across lineages, and thus
- closely related taxa tend to share traits.

Without information on the phylogeny, a detection model would treat different cynobacteria as independent observations, whereas incorporating the phylogeny allows the model to learn general patterns, such as:

- the probability of toxin presence is high when multiple closely related taxa show toxin production,
- signal in weakly supported clades contributes less to the overall prediction than signal in strongly supported clades,
- signal in deep clades contributes less to the overall prediction than signal in shallow clades,
- certain features ([Note to self - provide example here]) being commonly associated with toxin presence.

---

## Implemented Model

The model I am trying to implement is a **graph neural network** that follows the structure of a phylogenetic tree. (By the way, I learned about graph neural networks from [this amazing introduction](https://distill.pub/2021/gnn-intro/).) Each taxon at the tips of the tree is represented by a set of traits related to cyanotoxicity, which are transformed into numerical embeddings by the model. These embeddings are combined step by step as the model moves from the tips toward the root, so that each internal node represents the combined embedding signal of all its descendants.

At every node in the tree, including both tips and internal clades, the model can estimate how likely that taxon or clade is to be cyanotoxic. This allows the model to identify not only individual species that are likely to produce cyanotoxins, but also entire groups of related taxa that share cyanotoxic traits (and, thus, indicating some taxa that stop cyanotoxin production only temporarily).

The model uses simple averaging of the embedding scores to combine information across related taxa. (I am considering adding more advanced weighting schemes using branch lengths later.)
