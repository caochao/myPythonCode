class myHashTable:
	KEY_NOT_FOUNDED = -999
	def __init__( self, size ):
		self._size = size
		self._elems = [ None ] * size
		self._linearHashDelta = [ x for x in range( 1, size ) ]

	'''
	hash函数，求key在数组中的索引
	'''
	def _hashFunc( self, key ):
		asciiSum = 0
		for c in key:
			asciiSum += ord( c )
		print( 'key:%s, asciiSum:%d, hashIndex:%d' % ( key, asciiSum, asciiSum % self._size ) )
		return asciiSum % self._size

	'''
	开放定址法（线性探测再散列）处理冲突
	@param collisionHashIndex 冲突时的hash地址
	@param delta 标识第几次处理冲突
	'''
	def _collisionFunc( self, collisionHashIndex, delta ):
		if delta >= self._size - 1:
			print( 'hashTable overflow' )
			return myHashTable.KEY_NOT_FOUNDED
		return ( collisionHashIndex + self._linearHashDelta[ delta ] ) % self._size

	'''
	寻找hashKey对应的hash地址
	'''
	def _search( self, key ):
		tmpHashIndex = self._hashFunc( key )
		hashIndex = tmpHashIndex
		hashData = self._elems[ tmpHashIndex ]
		delta = 0
		while hashData and hashData['key'] != key:
			hashIndex = self._collisionFunc( tmpHashIndex, delta )
			if hashIndex == myHashTable.KEY_NOT_FOUNDED: break
			hashData = self._elems[ hashIndex ]
			delta += 1
		return hashIndex

	def get( self, key ):
		hashIndex = self._search( key )
		if hashIndex == myHashTable.KEY_NOT_FOUNDED:
			return None
		hashData = self._elems[ hashIndex ]
		if not hashData:
			return None
		return hashData['value']

	def put( self, key, value ):
		hashIndex = self._search( key )
		self._elems[ hashIndex ] = { 'key': key, 'value': value }

hashTab = myHashTable( 6 )

hashTab.put( 'aj', 'value1' )
print( hashTab.get( 'aj' ) )

hashTab.put( 'bi', 'value2' )
print( hashTab.get( 'bi' ) )

hashTab.put( 'ch', 'value3' )
print( hashTab.get( 'ch' ) )

hashTab.put( 'dg', 'value4' )
print( hashTab.get( 'dg' ) )

hashTab.put( 'ef', 'value5' )
print( hashTab.get( 'ef' ) )

hashTab.put( 'hahaha44444444444444444444', 'value5' )
print( hashTab.get( 'hahaha' ) )

print( hashTab._elems )


#a b c d e f g h i j