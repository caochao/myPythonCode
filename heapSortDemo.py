#将堆按层序遍历顺序保存在数组中

#沿左,右子节点较大者依次往下调整
def heapify( array, i, n ):
	j = i * 2 + 1
	while j < n:
		if j + 1 < n and array[j] < array[j + 1]:
			j += 1
		if array[i] > array[j]:
			break
		array[i], array[j] = array[j], array[i]
		i = j
		j = i * 2 + 1

#创建堆
def build_heap( array ):
	size = len( array )
	for i in range( size // 2 - 1, -1, -1 ):
		heapify( array, i, size )

#大顶堆排序
def heap_sort( array ):
	size = len( array )
	build_heap( array )
	#交换堆顶与最后一个结点,再调整堆
	for i in range( size - 1, 0, -1 ):
		array[0], array[i] = array[i], array[0]
		heapify( array, 0, i )

a = [ -3, 1, 3, 0, 9, 7 ]
heap_sort( a )
print( a )