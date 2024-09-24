N = int(input())
A = list(map(int, input().split()))

count = 0
ind = [0] * N

for i in range(N):
	memo = set()
	root = []
	if ind[i] == 0:
		c = 0
		gc = 0
		g = -1
		while True:
			c += 1
			root.append(i)
			memo.add(i)
			i = A[i] - 1
			if ind[i] != 0:
				gc = ind[i]
				c = c + gc
				break
			if i in memo:
				g = i
				gc = c
				break
		f = False
		for r in root:
			if f or r == g:
				ind[r] = c
				f = True
			else:
				ind[r] = c
				c -= 1
		count += gc
	else:
		count += ind[i]
print(sum(ind))
