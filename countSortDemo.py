
'''
@param plist [0,n]正整数数组
'''
def count_sort( plist ):
	_max = max( plist )
	counter = [ 0 ] * ( _max + 1 )
	output = [ 0 ] * len( plist )

	# 计算每个数字出现的次数
	for i in plist:
		counter[ i ] += 1

	# 计算小于等于i的数字个数
	for i in range( 1, len( counter ) ):
		counter[ i ] += counter[ i - 1 ]

	# 排序, 例如小于6的数字有3个, 则将6放在位置4
	for i in range( len( plist ) - 1, -1, -1 ):
		output[ counter[ plist[ i ] ] - 1 ] = plist[ i ]
		counter[ plist[ i ] ] -= 1
	return output

if __name__ == '__main__':
	print( count_sort( [ 2, 5, 3, 0, 2, 3, 0, 3 ] ) )
