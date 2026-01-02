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

# IMPORTS
from ete3 import Tree

########################################
# READING INPUTS
########################################

# READING ROOTED PHYLOGENETIC TREE
# in_tree = Read/parse rooted phylogenetic tree (input 1) via ETE3 ( in_tree = Tree("input_tree.nwk", format=1) )
# Test if phylogenetic tree rooted; continue only if yes
# root_node = Extract the root node of in_tree
# tree_tips = Extract the tip nodes of in_tree
# tip_labels_from_tree = Extract the tip labels of in_tree; must be connected to the tree_tips

# READING TABLE ASSOCIATING TREE LEAF NAMES WITH CYANOTOXIN FEATURES
# in_table = Read/parse tip-character table (input 2) in CSV format
# tip_labels_from_table = Extract the tip labels of in_table

# DECONSTRUCT THE in_table INTO A DICTIONARY
# compiled_tip_chars_dict = a dictionary with structure {'tiplabel_01' = ['char1_val', 'char2_val', 'char3_val'], ...}

# VALIDATE CORRESPONDENCE (BTW TREE TIPS AND TABLE ROWS)
# for label in tip_labels_from_tree:
#    if label not in compiled_tip_chars_dict:
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
# Write a function ("aggregate_descendant_embeddings") that aggregates all descendant
# embeddings (i.e., the numerical representations of the evaluated characters)
# into a single embedding for each internal node by assigning that node the
# average embedding signal of its descendants (i.e., mean pooling).
# By traversing the phylogenetic tree from the tips to the root, the function
# aims to answer the following question at each node: “Given what is known about
# all descendants of this node, what is the characteristic state of their most
# recent common ancestor (i.e., this node)?” This process produces a clade-level
# representation that summarizes trait information across all descendants of a node.
# General structure:
# function aggregate_descendant_embeddings(child_embeddings_dict):
#   return mean(child_embeddings_dict)


# TRAVERSE THROUGH TREE AND CALCULATE EMBEDDINGS FOR TIPS AND NODES
# Write a function that iterates over all nodes of an input tree, decides 
# if the node is a tree tip of an internal node, and then either calculates
# the embeddings directly (i.e., if a tree tip) or uses the above function
# aggregate_descendant_embeddings() to infer the average embedding signal 
# of all descendants of the node (i.e., if an internal node). In either case, 
# every node receives a single embedding (which is highly dimensional). 
# The function then converts each embedding to a logit (a raw confidence 
# value) and then further into a probability using a sigmoid transformation.
# General structure:
# function traverse_across_nodes(in_tree, root_node, tree_tips, compiled_tip_chars_dict):
#	for node in in_tree.traverse():  # ETE3 function
#	   if node is tip:
#			embedding_dict[node.name] = encode_tip_state(node)
#	   else:
#			child_embeddings_dict = some_function(node)
#			embedding_dict[node.name] = aggregate_descendant_embeddings(child_embeddings_dict)
#		logit_dict[node.name] = embedding_to_logit(embedding_dict[node.name])
#		prob_dict[node.name] = logit_to_prob(logit_dict[node.name])
#	return logit_dict, prob_dict


# CALCULATE LOSSES FOR TREE TIPS GIVEN GROUND TRUTH
# Write a function that iterates over all tree tips and calculates the 
# loss function (e.g., binary cross-entropy loss) given known tree tip values
# (e.g., known cyanotoxin values) to infer a classification (into 
# cyanotoxic or not cyanotoxic) from the loss values. That way, the 
# function computes how far the model’s prediction is from the truth.
# General structure:
# function calculate_losses(logits_dict, tree_tips, known_tree_tip_values_binary):
# 	for node in tree_tips:
#		if node is tip:
#			losses_dict[node.name] = binary_cross_entropy_with_logits(logit_dict[node.name], known_tree_tip_values_binary[node.name])
#	return losses_dict[node.name]


########################################
# MAIN
########################################

# MAIN FUNCTION
def main():
	pass
'''
	# STEP 1. Inferring probabilities for all nodes and saving them as node names
	prob_dict, _ = traverse_across_nodes(in_tree, root_node, tree_tips, compiled_tip_chars_dict)
	for node in in_tree.traverse():
		if node.name in prob_dict.keys():
			node.name = f"{node.name}|P(cyanotoxic)={prob_dict[node.name]:.6g}"
	in_tree.write(outfile="tree_with_node_labels.tre", format=1)

	# STEP 2. Training a model
	for epoch in 1..E:
	  _, logits_dict = traverse_across_nodes(in_tree, root_node, tree_tips, compiled_tip_chars_dict)
	  losses = calculate_losses(logits_dict, tree_tips, known_tree_tip_values_binary)
	  loss = mean(losses)
	  loss.backward()
	  optimizer.step()
	  optimizer.zero_grad()
'''

if __name__ == "__main__":
    main()
