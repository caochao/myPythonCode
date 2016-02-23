'''
-----------------单链表遍历算法----------------
'''

def linklist_traverse( head, visit_func = lambda node:print( node.value ) ):
	if not head:
		print( 'empty linklist' )
	ret = '(linklist head -> tail): '
	node = head
	while node:
		ret += '%d %s ' % ( node.value, node.next and '->' or '' )
		node = node.next
	print( ret )


'''
-----------------二叉树非递归遍历算法----------------
'''
from base.structure import stack
from base.structure import queue

'''
先序遍历
'''
def bintree_traverse_pre_order( root, visit_func = lambda node:print( node.value ) ):
	if not root: return
	s = stack()
	s.push( root )
	while not s.is_empty():
		node = s.pop()
		visit_func( node )
		if node.rchild:
			s.push( node.rchild )
		if node.lchild:
			s.push( node.lchild )

'''
中序遍历
'''
def bintree_traverse_in_order( root, visit_func = lambda node:print( node.value ) ):
	if not root: return
	s = stack()
	node = root
	while node or not s.is_empty():
 		if node:
 			s.push( node )
 			node = node.lchild
 		else:
 			node = s.pop()
 			visit_func( node )
 			node = node.rchild

'''
后序遍历
'''
def bintree_traverse_post_order( root, visit_func = lambda node:print( node.value ) ):
	curr = root
	prev = None
	s = stack()
	s.push( curr )
	while not s.is_empty():
		curr = s.top()
		if ( not curr.lchild and not curr.rchild ) or ( prev and ( prev == curr.lchild or prev == curr.rchild ) ):
			visit_func( curr )
			s.pop()
			prev = curr
		else:
			if curr.rchild:
				s.push( curr.rchild )
			if curr.lchild:
				s.push( curr.lchild )

'''
层序遍历
'''
def bintree_traverse_level_order( root, visit_func = lambda node:print( node.value ) ):
	q = queue()
	q.enqueue( root )
	while not q.is_empty():
		node = q.dequeue()
		visit_func( node )
		if node.lchild:
			q.enqueue( node.lchild )
		if node.rchild:
			q.enqueue( node.rchild )