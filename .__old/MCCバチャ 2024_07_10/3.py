N, M = map(int, input().split())
U, V = [0] * M, [0] * M
for i in range(M):
	U[i], V[i] = map(int, input().split())

G = dict()
for u, v in zip(U, V):
	G[u] = G.get(u, []) + [v]
	G[v] = G.get(v, []) + [u]

visited = [False] * (N + 1)

cc = 0

def dfs(_visited, _g, _v):
	_visited[_v] = True
	nextV = _g.get(_v, [])
	for nv in nextV:
		if not _visited[nv]:
			dfs(_visited, _g, nv)

for i in range(1, N+1):
	if not visited[i]:
		cc += 1
		dfs(visited, G, i)

print(cc)