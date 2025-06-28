N, M = map(int, input().split())

G = [set() for _ in range(N)]

def check(G):
	g = [set() for _ in range(N)]
	for (u, v) in G:
		g[u].add(v)
		g[v].add(u)
	
	if all([len(g[i]) == 2 for i in range(N)]):
		return True

for _ in range(M):
	u, v = map(int, input().split())
	u -= 1
	v -= 1
	if u > v:
		u, v = v, u
	G[u].add(v)

from collections import deque
q = deque()


