import random

'''
从数组里随机挑选m个元素
思路：每次将随机到的元素和数组末尾的元素交换(O(m))，避免直接弹出元素引起的数组移动(O(n^2))。
'''
def random_get_m_from_array( array, m ):
	array_len = len( array )
	random_idx = 0
	i = m
	while ( i > 0 ):
		random_idx = int( random.random() * array_len )
		array[ random_idx], array[ array_len - 1 ] = array[ array_len - 1 ], array[ random_idx ]
		array_len -= 1
		print( array )
		i -= 1
	return array[ -m : ]

ret = random_get_m_from_array( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], 2 )
print( ret )