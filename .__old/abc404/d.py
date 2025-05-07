N, M = map(int, input().split())
C = list(map(int, input().split()))
doubutu = [[] for _ in range(N)]
for m in range(M):
	K, *A = map(int, input().split())
	for a in A:
		doubutu[a-1].append(m)

from itertools import product
cost = float('inf')
for bit in product((0, 1), repeat=N):
	watched = [0] * M
	for i, b in enumerate(bit):
		if b == 1:
			for a in doubutu[i]:
				watched[a] += 1
	if all(watched[a] >= 2 for a in range(M)):
		c = 0
		for i, b in enumerate(bit):
			if b == 1:
				c += C[i]
		cost = min(cost, c)
		continue
	
	_cost = 0
	for i, b in enumerate(bit):
		if b == 1:
			_cost += C[i]
	for _bit in product((0, 1), repeat=N):
		_watched = watched.copy()
		for i, b in enumerate(_bit):
			if b == 1:
				for a in doubutu[i]:
					_watched[a] += 1
		if all(_watched[a] >= 2 for a in range(M)):
			c = 0
			for i, b in enumerate(_bit):
				if b == 1:
					c += C[i]
			cost = min(cost, c + _cost)

	
print(cost)