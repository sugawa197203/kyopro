


while True:
	N = int(input())
	if N == 0:
		break
	if N == 1:
		print(1, 1)
		continue

	pos = []
	pos.append((0, 0))
	
	for i in range(N - 1):
		n, d = map(int, input().split(' '))

		p = pos[n]

		if d == 0:
			newpos = (p[0] - 1, p[1])
		elif d == 1:
			newpos = (p[0], p[1] - 1)
		elif d == 2:
			newpos = (p[0] + 1, p[1])
		elif d == 3:
			newpos = (p[0], p[1] + 1)
		
		pos.append(newpos)
		
	minx = min(pos, key=lambda a: a[0])[0]
	maxx = max(pos, key=lambda a: a[0])[0]
	miny = min(pos, key=lambda a: a[1])[1]
	maxy = max(pos, key=lambda a: a[1])[1]
	
	print(maxx - minx + 1, maxy - miny + 1)


