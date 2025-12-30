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

# TO BE CONTINUED ...
