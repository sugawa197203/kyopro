N, M = map(int, input().split())
X, Y, Z = [0] * M, [0] * M, [0] * M
for i in range(M):
	X[i], Y[i], Z[i] = map(int, input().split())
from collections import defaultdict

G = defaultdict(list)

for i in range(M):
	G[X[i]].append((Y[i], Z[i]))
	G[Y[i]].append((X[i], Z[i]))

A = [-1] * (N + 1)

for i in range(1, N + 1):
	if A[i] == -1:
		stack = [(i, 0)]
		while stack:
			node, value = stack.pop()
			if A[node] != -1:
				if A[node] != value:
					print("-1")
					exit()
				continue
			A[node] = value
			for nextNode, xorValue in G[node]:
				if A[nextNode] != -1:
					if A[nextNode] != value ^ xorValue:
						print("-1")
						exit()
					continue
				stack.append((nextNode, value ^ xorValue))

print(*A[1:])
