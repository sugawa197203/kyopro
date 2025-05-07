import sys
sys.setrecursionlimit(1 << 25)

N, M = map(int, input().split())
if N != M:
	print("No")
	exit()

from collections import defaultdict

graph = defaultdict(list)
degree = [0] * (N + 1)

for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
	degree[a] += 1
	degree[b] += 1

for v in range(1, N + 1):
	if degree[v] != 2:
		print("No")
		exit()

visited = [False] * (N + 1)
def dfs(v):
	visited[v] = True
	for nv in graph[v]:
		if not visited[nv]:
			dfs(nv)

dfs(1)

if all(visited[1:]):
	print("Yes")
else:
	print("No")
