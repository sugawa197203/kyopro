N, M, X = map(int, input().split())
from collections import defaultdict
g = defaultdict(list)

for i in range(M):
	u, v = map(int, input().split())
	g[u].append(v)
	g[v+N].append(u+N)

for i in range(1, N+1):
	g[i].append(i+N)
	g[i+N].append(i)

from heapq import heappop, heappush

now = 1
costs = [float("inf")] * (N + 1) * 2
costs[1] = 0

q = [(0, 1)]

while q:
	cost, node = heappop(q)
	if costs[node] < cost:
		continue

	for next_node in g[node]:
		if abs(node - next_node) == N:
			c = cost + X
		else:
			c = cost + 1

		if costs[next_node] > c:
			costs[next_node] = c
			heappush(q, (c, next_node))


print(min(costs[N], costs[N * 2]))
