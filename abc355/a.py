a, b = map(int, input().split())
if a == b:
	print(-1)
else:
	l = [1, 2, 3]
	l.remove(a)
	l.remove(b)
	print(l[0])