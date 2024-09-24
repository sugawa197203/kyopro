import bisect
N = int(input())

G = dict()

for i in range(N-1):
	A, B = map(int, input().split())
	G[A] = G.get(A, []) + [B]
	G[B] = G.get(B, []) + [A]

for k in G:
	G[k].sort()

houmon = [False] * (N + 1)
houmon[1] = True
root = []
Q = [1]

while Q:
	v = Q.pop()
	root.append(v)
	for u in G[v]:
		if not houmon[u]:
			houmon[u] = True
			Q.append(u)
			
print(*root)