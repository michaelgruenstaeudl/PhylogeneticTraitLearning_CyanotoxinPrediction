#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phylogeny-aware machine learning model that predicts cyanotoxin presence by
learning statistical associations between clade structure and tip-level traits
Author: Michael Gruenstaeudl, PhD | Email: m_gruenstaeudl@fhsu.edu
"""

'''
  Input:
    - Rooted phylogenetic tree (in PHYLIP format)

    - Table associating tree leaf names with various cyanotoxin features (in CSV format)
    Details on features:
        Tip character columns might be:
          - Presence/absence of gene cluster for cyanotoxin biosynthesis (e.g., mcy, cyr, sxt, ana)
          - Counts of toxin gene copies in genome
          - BLAST hits in genome against cyanotoxin genes
          Note: Features may need to be scaled/standardized (e.g., log1p-transformation of toxin gene copy count)
        Tip labels (supervision) might be:
          - confirmed cyanotoxicity

  Output:
    - Probability that cyanotoxin present in specific nodes of phylogeny

  Model:
    - The model needed for this script is a phylogeny-aware neural network that
      operates directly on a rooted phylogenetic tree (i.e., a tree-structured
      neural network whose computation follows the topology of a phylogeny). It
      can be viewed as a specialized graph neural network for phylogenetic trees,
      where information is propagated from the leaves along branches to the
      internal nodes using aggregation functions. Algorithimcally, the model
      needs to perform hierarchical representation learning: it shall construct
      trait embeddings (i.e., numerical representations of the evaluated
      characters) at all nodes (leaves, internal nodes, root).
'''
########################################
# READING INPUTS
########################################

# READING ROOTED PHYLOGENETIC TREE
# in_tree = Read/parse rooted phylogenetic tree (input 1) in PHYLIP/NEWICK format
# Test if phylogenetic tree rooted; continue only if yes
# root_node = Extract the root node of in_tree
# tip_nodes = Extract the tip nodes of in_tree
# tip_labels_from_tree = Extract the tip labels of in_tree; must be connected to the tip_nodes

# READING TABLE ASSOCIATING TREE LEAF NAMES WITH CYANOTOXIN FEATURES
# in_table = Read/parse tip-character table (input 2) in CSV format
# tip_labels_from_table = Extract the tip labels of in_table

# DECONSTRUCT THE in_table INTO A DICTIONARY
# Dict_tiplabel_chars = a dictionary with structure {'tiplabel_01' = ['char1_val', 'char2_val', 'char3_val'], ...}

# VALIDATE CORRESPONDENCE (BTW TREE TIPS AND TABLE ROWS)
# for label in tip_labels_from_tree:
#    if label not in Dict_tiplabel_chars:
#       throw_exception

# MISC:
# Ignore extra rows present in the CSV but not found as tips in the tree


########################################
# DEFINE A PHYLOGENY-AWARE NODE-WISE NEURAL NETWORK
########################################

# RAW BIOLOGICAL OBSERVATIONS BECOME A LEARNED REPRESENTATION
# Write a function ("tip_encoder") that contains a learnable linear transformation
# (which reweights and combines the raw characters and learns which in_table
# characters matter most for cyanotoxicity) and then applies a non-linear
# activation function (e.g., a hyperbolic tangent) that scales values into a
# simplistic range and allows non-linearity to allow the model to learn beyond
# the input data.
# General structure:
# function encode_tip_state(tip_chars):
#  return tanh( tip_encoder(tip_chars) )


# RENDERING THE MODEL PHYLOGENY-AWARE
# Write a function ("aggregate_descendant_clades") that aggregates all descendant
# embeddings (i.e., the numerical representations of the evaluated characters)
# into a single embedding for each internal node by assigning that node the
# average embedding signal of its descendants (i.e., mean pooling).
# By traversing the phylogenetic tree from the tips to the root, the function
# aims to answer the following question at each node: “Given what is known about
# all descendants of this node, what is the characteristic state of their most
# recent common ancestor (i.e., this node)?” This process produces a clade-level
# representation that summarizes trait information across all descendants of a node.
# General structure:
# function aggregate_descendant_clades(child_embeddings):
#   return mean(child_embeddings)


# TO BE CONTINUED ...
