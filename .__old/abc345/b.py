X = int(input())

_X = X // 10
x = X % 10

if _X >= 0:
	print(_X if x == 0 else _X + 1)
else:
	print(_X if x == 0 else _X + 1)