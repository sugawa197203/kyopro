N, Q = map(int, input().split())
A = list(range(1, N + 1))
indexOffset = 0

for _ in range(Q):
	q, *px = map(int, input().split())
	if q == 1:
		p, x = px
		A[(p - 1 + indexOffset) % N] = x
	elif q == 2:
		p = px[0]
		print(A[(p - 1 + indexOffset) % N])
	elif q == 3:
		k = px[0]
		indexOffset = (indexOffset + k) % N