'''
单链表
'''
class link_node:
	def __init__( self, value ):
		self.value = value
		self.next = None

'''
二叉树
'''
class bin_tree_node:
	def __init__( self, value ):
		self.value = value
		self.lchild = None
		self.rchild = None

'''
基于单链表实现的栈
'''
class stack:
	def __init__( self ):
		self._top = None

	def top( self ):
		if not self._top:
			return None
		return self._top.value

	def push( self, value ):
		node = link_node( value )
		node.next = self._top
		self._top = node

	def pop( self ):
		if not self._top:
			return None
		old_top = self._top
		self._top = old_top.next
		return old_top.value

	def is_empty( self ):
		return self._top == None

	def tostring( self ):
		if not self._top:
			return 'empty stack'
		else:
			ret = '(stack top -> bottom): '
			node = self._top
			while node.next:
				ret += '%d -> ' % node.value
				node = node.next
			ret += str( node.value )
		return ret

'''
基于单链表实现的队列
'''
class queue:
	def __init__( self ):
		self.head = None
		self.tail = None

	def enqueue( self, value ):
		node = link_node( value )
		if not self.tail:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node

	def dequeue( self ):
		if not self.head:
			return None
		old_head = self.head
		self.head = old_head.next
		if not self.head:
			self.tail = None
		return old_head.value

	def is_empty( self ):
		return self.tail == None

	def tostring( self ):
		if not self.head:
			return 'empty queue'
		else:
			ret = '(queue head -> tail): '
			node = self.head
			while node.next:
				ret += '%d -> ' % node.value
				node = node.next
			ret += str( node.value )
		return ret

if __name__ == '__main__':
	print( '---------------test stack---------------' )
	s = stack()
	s.push( 1 )
	s.push( 2 )
	s.push( 3 )
	print( s.tostring() )
	s.pop()
	print( s.tostring() )
	s.pop()
	s.pop()
	print( s.tostring() )
	s.push( 3 )
	print( s.tostring() )
	s.pop()
	s.pop()
	print( s.tostring() )

	print( '---------------test queue---------------' )
	q = queue()
	print( q.tostring() )
	q.enqueue( 1 )
	print( q.tostring() )
	q.dequeue()
	q.dequeue()
	q.dequeue()
	print( q.tostring() )
	q.enqueue( 1 )
	q.enqueue( 2 )
	q.enqueue( 3 )
	print( q.tostring() )
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	print( q.tostring() )