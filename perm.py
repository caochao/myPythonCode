def perm( sofar, remain ):
	if remain == "":
		print( sofar )
	for i in range( 0, len( remain ) ):
		perm( sofar + remain[i], remain[0:i] + remain[i+1:] )

def permgen( array, n ):
	print( array, n )
	if n <= 0:
		print( array )
		return
	for i in range( 0, n ):
		array[i], array[n-1] = array[n-1], array[i]		#数组第i个元素和最后一个元素交换
		permgen( array, n-1 )							#生成其余元素的排列	
		array[i], array[n-1] = array[n-1], array[i]		#恢复第i个元素的位置

perm( "", "abc" )
permgen( [ 1, 2 ], 2 )