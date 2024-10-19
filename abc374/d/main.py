import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; import networkx as nx; debug = lambda *arg : print(*arg, file=sys.stderr);

N, S, T = map(int, input().split())
A, B, C, D = [], [], [], []
for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

G = nx.Graph()

for a, b, c, d in zip(A, B, C, D):
    G.add_node((a, b, c, d))
for nodes in G.nodes():
    for node in G.nodes():
        if nodes == node:
            continue
        a, b, c, d = nodes
        e, f, g, h = node
        w = math.sqrt((a-c)**2 + (b-d)**2) / T
        G.add_edge((a, b, c, d), (e, f, g, h), weight=w+math.sqrt((c-e)**2 + (d-f)**2)/S)
        G.add_edge((a, b, c, d), (e, f, g, h), weight=w+math.sqrt((c-e)**2 + (d-f)**2)/S)
        G.add_edge((a, b, c, d), (e, f, g, h), weight=w+math.sqrt((a-e)**2 + (b-f)**2)/S)
        G.add_edge((a, b, c, d), (e, f, g, h), weight=w+math.sqrt((a-e)**2 + (b-f)**2)/S)

G.add_node((0, 0))
for _nodes in G.nodes():
    if _nodes == (0, 0):
        for nodes in G.nodes():
            if nodes == (0, 0):
                continue
            a, b, c, d = nodes
            G.add_edge((0, 0), nodes, weight=math.sqrt(a**2 + b**2)/S)
            G.add_edge((0, 0), nodes, weight=math.sqrt(a**2 + b**2)/S)

# start from (0, 0) floyd warshall

rightestcoust = 10**8


