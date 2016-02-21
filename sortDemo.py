#分区方法，使得pivot前（后）的元素均小于（大于）pivot
#该方法用途广泛，可用于快排，求数组中第k大元素等
def partition( array, low, high ):
	# orglow = low
	pivot = array[ low ]
	while low < high:
		#从后往前找到第一个小于pivot的元素
		while low < high and array[ high ] >= pivot:
			high -= 1
		array[ low ] = array[ high ]

		#从后往前找到第一个小于pivot的元素
		while low < high and array[ low ] <= pivot:
			low += 1
		array[ high ] = array[ low ]
	array[ low ] = pivot
	return low

def qsort( array, low, high ):
	if low < high:
		pivot_idx = partition( array, low, high )
		qsort( array, low, pivot_idx - 1 )
		qsort( array, pivot_idx + 1, high )

arr = [ 6, 6, 5, 4, 3, 7, 0, -1, 99 ]
qsort( arr, 0, len( arr ) - 1 )
print( 'sorted array:', arr )

#将数组中奇数置于偶数前
def reorder_odd_even( array, low, high ):
	while low < high:
		while low < high and array[ low ] & 1 != 0:
			low += 1
		while low < high and array[ high ] & 1 == 0:
			high -= 1
		if low < high:
			array[ low ], array[ high ] = array[ high ], array[ low ]

reorder_odd_even( arr, 0, len( arr ) - 1 )
print( 'reorder array:', arr )

#获取数组中第k大元素，非已排序数组
def get_big_k_number( array, k ):
	low = 0
	high = len( array ) - 1
	if k < low or k > high:
		return 0
	pivot_idx = partition( array, low, high )
	while pivot_idx != k:
		if pivot_idx > k:
			high = pivot_idx - 1
			pivot_idx = partition( array, low, high )
		else:
			low = pivot_idx + 1
			pivot_idx = partition( array, low, high )
	print( array )
	return array[ k ]

k = 1
k_big = get_big_k_number( arr, 8 - k )
print( 'the no.%d big number is:' % k, k_big )
