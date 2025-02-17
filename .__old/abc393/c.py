N, M = map(int, input().split())
from collections import defaultdict
edge = defaultdict(list)
edgecount = defaultdict(int)
ans = 0

for i in range(M):
	u, v = map(int, input().split())
	
	if u == v:
		ans += 1
		continue

	if u > v:
		u, v = v, u
	
	if edgecount[(u, v)] == 0:
		edge[u].append(v)
		edge[v].append(u)
		edgecount[(u, v)] = 1
	else:
		ans += 1
print(ans)