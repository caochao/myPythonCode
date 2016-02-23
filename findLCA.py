from base.structure import bin_tree_node
from base.structure_util import bintree_traverse_in_order
from base.structure_util import bintree_traverse_level_order

def swap( node1, node2 ):
	node1.value = node1.value ^ node2.value
	node2.value = node1.value ^ node2.value
	node1.value = node1.value ^ node2.value

'''
在bst中寻找node1, node2的最低公共祖先
'''
def find_bst_lca( root, node1, node2 ):
	if not root:
		return None
	if node1.value > node2.value:
		swap( node1, node2 )
	if root.value >= node1.value and root.value <= node2.value:
		return root
	elif root.value < node1.value:
		return find_bst_lca( root.rchild, node1, node2 )
	else:
		return find_bst_lca( root.lchild, node1, node2 )

if __name__ == '__main__':
	node6 = bin_tree_node( 6 )
	node2 = bin_tree_node( 2 )
	node8 = bin_tree_node( 8 )
	node0 = bin_tree_node( 0 )
	node4 = bin_tree_node( 4 )
	node7 = bin_tree_node( 7 )
	node9 = bin_tree_node( 9 )
	node3 = bin_tree_node( 3 )
	node5 = bin_tree_node( 5 )

	node6.lchild = node2
	node6.rchild = node8
	node2.lchild = node0
	node2.rchild = node4
	node8.lchild = node7
	node8.rchild = node9
	node4.lchild = node3
	node4.rchild = node5

	#bintree_traverse_in_order( node6 )
	node = find_bst_lca( node6, node6, node4 )
	print( node.value if node else 'no lca' )