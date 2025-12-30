# Phylogenetic Trait Learning for Cyanotoxin Prediction
Phylogeny-aware machine learning model that predicts cyanotoxin presence by learning statistical associations between clade structure and tip-level traits

#### Goal
This Python script aims to infer the probability of cyanotoxin presence by learning how toxin-related traits distributed across cyanobacterial taxa interact with phylogenetic structure to produce clade-level signals associated with toxin production.

#### Description
Here, I implement a model that acts as a phylogenetic trait predictor. It learns statistical associations between tip-level characters (e.g., the presence of toxin biosynthesis genes like `mcy`, `cyr`, `sxt`, and `ana`; the abundance of toxin gene clusters; or prior knowledge of toxin production among specific taxa) and the underlying phylogenetic structure of the tree. By training the model on existing phylogenies, it learns which tip-level features and phylogenetically aggregated patterns are most predictive of cyanotoxin presence.

#### Rationale
A phylogeny contains essential information for cyanotoxin detection, since
- cyanotoxin production is often clade-structured rather than randomly distributed across lineages, and thus
- closely related taxa tend to share traits.

Without information on the phylogeny, a detection model would treat different cynobacteria as independent observations, whereas incorporating the phylogeny allows the model to learn general patterns, such as:
- the probability of toxin presence is high when multiple closely related taxa show toxin production,
- signal in weakly supported clades contributes less to the overall prediction than signal in strongly supported clades,
- signal in deep clades contributes less to the overall prediction than signal in shallow clades,
- certain features ([Note to self - give example here]) being commonly associated with toxin presence.
