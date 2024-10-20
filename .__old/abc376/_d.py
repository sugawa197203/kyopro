N, M = map(int, input().split())
A, B = [], []
import sys
import networkx as nx
debug = lambda *args: print(*args, file=sys.stderr)
for _ in range(M):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

G = nx.Graph()
nodes = list(range(1, N + 1))
G.add_node_from(nodes)
for a, b in zip(A, B):
	G.add_edge(a, b)

# 1 to 1 shortest path
try:
	print(nx.shortest_path_length(G, 1, N))
except nx.NetworkXNoPath:
	print(-1)