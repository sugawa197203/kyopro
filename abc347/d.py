a, b, C = map(int, input().split())

cPop = C.bit_count()
cBitLen = C.bit_length()

if abs(a - b) <= cPop and abs(a - b) % 2 == 0:
	print("-1")
	exit()

