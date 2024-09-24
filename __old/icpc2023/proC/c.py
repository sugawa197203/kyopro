
def change(x, y, n):
	slidex = 0 if y % 2 == 0 else n // 2
	_x = (x + slidex) % n
	slidey = 0 if _x % 2 == 0 else n // 2
	return _x, (y + slidey) % n


while True:
	n = int(input())
	if n == 0:
		exit(0)
	
	a = []
	for i in range(n):
		a.append(list(map(int, input().split(' '))))
	
	newa = []
	for i in range(n):
		newa.append([0 for _ in range(n)])
	
	for y in range(n):
		for x in range(n):
			_x, _y = change(x, y, n)
			newa[_y][_x] = a[y][x]
	
	for i in range(n):
		sa = [str(ssa) for ssa in newa[i]]
		print(" ".join(sa))
	
