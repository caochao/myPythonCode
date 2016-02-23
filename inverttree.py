from base.structure import bin_tree_node
from base.structure_util import bintree_traverse_in_order


'''
反转二叉树
'''
def invert_bin_tree( root ):
	if not root:
		return None
	tmp = root.lchild
	root.lchild = invert_bin_tree( root.rchild )
	root.rchild = invert_bin_tree( tmp )
	return root

node1 = bin_tree_node( 1 )
node2 = bin_tree_node( 2 )
node3 = bin_tree_node( 3 )
node4 = bin_tree_node( 4 )
node5 = bin_tree_node( 5 )
node6 = bin_tree_node( 6 )

node1.lchild = node2
node1.rchild = node3
node2.lchild = node4
node2.rchild = node5
node3.lchild = node6

bintree_traverse_in_order( node1 )
invert_bin_tree( node1 )
bintree_traverse_in_order( node1 )

	# 			1
	# 	2				3
	# 4		5		6

	# 			1
	# 	3				2
	# 		6		5		4