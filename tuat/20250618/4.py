import networkx as nx
N, M = map(int, input().split())
G = nx.Graph()
for _ in range(M):
    u, v = map(int, input().split())
    G.add_edge(u, v)

print(*nx.dijkstra_path(G, 1, N))