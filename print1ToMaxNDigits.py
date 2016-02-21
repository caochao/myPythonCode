def increament( number ):
	isOverflow = False
	nTakeOver = 0
	nLen = len( number )
	i = nLen - 1
	while i >= 0:
		nSum = number[i] + nTakeOver
		if i == nLen - 1:
			nSum += 1
		if nSum >= 10:
			if i == 0:
				isOverflow = True
			else:
				nTakeOver = 1
				nSum = 0
				number[ i ] = nSum
		else:
			number[ i ] = nSum
			break
		i -= 1
	return isOverflow

def printNumber( number ):
	beginingNot0 = False
	for i in range( 0, len( number ) ):
		if number[i] != 0:
			beginingNot0 = True
		if beginingNot0:
			print( number[i], end = '' )
	print( '\t', end = '' )

def print1ToMaxNDigits( n ):
	number = [ 0 ] * n
	while not increament( number ):
		printNumber( number )

print1ToMaxNDigits( 5 )
