N, M = map(int, input().split())
from collections import defaultdict

G = defaultdict(list)

for _ in range(M):
	u, v, w = map(int, input().split())
	G[u].append((v, w))
	G[v].append((u, w))

ans = float('inf')

stack = [(1, 0, set())]

while stack:
	u, w, visited = stack.pop()
	if u in visited:
		continue
	visited.add(u)
	for v, w2 in G[u]:
		if v == N:
			ans = min(ans, w ^ w2)
		else:
			stack.append((v, w ^ w2, visited.copy()))

print(ans)
