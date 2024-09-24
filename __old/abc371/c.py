N = int(input())
import networkx as nx
MG = int(input())
G = nx.Graph()
G.add_nodes_from(range(1, N+1))
for i in range(MG):
    v1, v2 = map(int, input().split())
    G.add_edge(v1, v2)
    G.add_edge(v2, v1)

MH = int(input())
H = nx.Graph()
H.add_nodes_from(range(1, N+1))
for i in range(MH):
    v1, v2 = map(int, input().split())
    H.add_edge(v1, v2)
    H.add_edge(v2, v1)

A = dict()
for i in range(N - 1):
    l = list(map(int, input().split()))
    for j in range(i, N):
        A[(i, j)] = l[j]



print(G, H)
print(nx.is_isomorphic(G, H))