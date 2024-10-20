N, M = map(int, input().split())
A, B = [], []
import sys
debug = lambda *args: print(*args, file=sys.stderr)
for _ in range(M):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

G = dict()
for a, b in zip(A, B):
	if a not in G:
		G[a] = []
	G[a].append(b)

# dfs
stack = [(1, 0)]
length = [0] * (N + 1)
length[1] = -1
visited = [False] * (N + 1)
while stack:
	node, dist = stack.pop()
	if node not in G:
		continue
	if visited[node]:
		continue
	visited[node] = True
	for next_node in G[node]:
		stack.append((next_node, dist + 1))
		length[next_node] = min(length[next_node], dist + 1)

print(length[1])
