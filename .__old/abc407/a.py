A, B = map(int, input().split())

ab = A / B

_AB  = A // B

__AB = _AB + 1

if ab - float(_AB) > __AB - ab:
	print(__AB)
else:
	print(_AB)