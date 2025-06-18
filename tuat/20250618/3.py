import networkx as nx
N, M = map(int, input().split())
G = nx.Graph()
G.add_nodes_from(range(1, N + 1))
for _ in range(M):
    u, v = map(int, input().split())
    G.add_edge(u, v)

print(nx.number_connected_components(G))