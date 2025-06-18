from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
	u, v, w = map(int, input().split())
	G[u].append((v, w))
	G[v].append((u, w))
G[0].append((1, 0))
__watched = [False] * (N + 1)
stack = [(0, 0, -1)] # (now, xor, from)
__xors = [1111111111_1111111111_1111111111] * (N + 1)

def dfs(now, xor, from_, watched, xors):
	nexts = G[now]
	watched[now] = True
	for n, w in nexts:
		xors[n] = min(xors[n], xor ^ w)

dfs(0, 0, -1, __watched, __xors)
