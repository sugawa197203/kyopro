N, K = map(int, input().split())
from collections import defaultdict
G = defaultdict(list)

if K == 1:
	print("Yes")
	exit()

for _ in range(N*K-1):
	u, v = map(int, input().split())
	G[u].append(v)
	G[v].append(u)

freeV = set()

stack = [1]
watched = set()
while stack:
	v = stack.pop()
	if v in watched:
		continue
	watched.add(v)
	nextV = [v for v in G[v] if v not in watched]
	if not nextV:
		freeV.add(v)
	else:
		stack.extend(nextV)
if len(G[1]) == 1:
	freeV.add(1)

