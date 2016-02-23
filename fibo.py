'''
求第n(从1开始)位fibonacci数
fibonacci数列前两位为0, 1. 后面每一位数字等于前两位数字之和
'''
def fibonacci( n ):
	if n <= 2:
		return n - 1
	f = 0
	g = 1
	while n - 2 > 0:
		g = g + f
		f = g - f
		n -= 1
		print( f, g )
	return g

print( fibonacci( 100 ) )

'''
与上述函数等价的递归写法
'''
def fib_iter( f, g, n ):
	if n <= 0:
		return g
	else:
		return fib_iter( g, f + g, n - 1 )

def fib( n ):
	if n <= 2:
		return n - 1
	return fib_iter( 0, 1, n - 2 )

print( fib( 100 ) )