from base.structure import bin_tree_node
from base.structure_util import bintree_traverse_pre_order
from base.structure_util import bintree_traverse_in_order
from base.structure_util import bintree_traverse_post_order
from base.structure_util import bintree_traverse_level_order
import math

'''
计算完全二叉树的节点数
可以将一颗完全二叉树拆分成满二叉树和一颗小的完全二叉树
'''
def count_completed_tree_nodes( root ):
	if not root:
		return 0
	hl = 1
	hr = 1
	lchild = root.lchild
	rchild = root.rchild
	while lchild:
		hl += 1
		lchild = lchild.lchild
	while rchild:
		hr += 1
		rchild = rchild.rchild
	if hl == hr:
		return math.pow( 2, hl ) - 1
	return count_completed_tree_nodes( root.lchild ) + count_completed_tree_nodes( root.rchild ) + 1

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

bintree_traverse_level_order( node1 )

print( count_completed_tree_nodes( node1 ) )


