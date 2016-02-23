'''
判断一个数是否2的冥次方, 这个题与求二进制中1的个数思路一致.
'''

'''
2的n次方数,其二进制表示为(1, 10, 100, ...),所以只要判断二进制中1的个数为1就行了
'''
# def is_pow_of_2( num ):
# 	if num <= 0:
# 		return False
# 	count1 = 0
# 	while num > 0:
# 		count1 += num & 1
# 		num >>= 1
# 	return count1 == 1

'''
2的n次方数,其二进制表示为(1, 10, 100, ...),另一种方法判断二进制中1的个数
'''
def  is_pow_of_2( num ):
	if num <= 0:
		return False
	count1 = 0
	while num > 0:
		count1 += 1
		num &= num - 1
	return count1 == 1

'''
由2的n次方数二进制表示法规律可知计算一次就够了
'''
def  is_pow_of_2( num ):
	if num <= 0:
		return False
	return num & ( num - 1 ) == 0

print( is_pow_of_2( 4 ) )