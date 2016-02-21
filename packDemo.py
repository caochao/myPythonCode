import struct

a = b'hello'
b = b'world!'
c = 2
d = 45.123

byteArr = struct.pack( '5s6sif', a, b, c, d )
print( byteArr )

print( struct.pack('hhl', 1, 2, 3) )