import networkx as n
N, Q = map(int, input().split())
u = n.utils.UnionFind()
for i in range(Q):
	p, a, b = map(int, input().split())
	if p == 0:
		u.union(a, b)
	else:
		print("Yes" if u[a] == u[b] else "No")