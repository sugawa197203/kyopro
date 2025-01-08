N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
import networkx as nx
d = nx.DiGraph()

for i in range(N):
    a, b = i + 1, A[i][0] + 1
    if a < b:
        a, b = b, a
    for j in range(1, N-1):
        _a, _b = i + 1, A[i][j] + 1
        if _a < _b:
            _a, _b = _b, _a
        
        # add node
        if not d.has_node((a, b)):
            d.add_node((a, b))
        if not d.has_node((_a, _b)):
            d.add_node((_a, _b))

        d.add_edge(a, b)
        a, b = _a, _b
print(d.edges)
if nx.cycle_basis(d):
    print(-1)
    exit()

print(max(nx.shortest_path_length(d, source=(i + 1, A[i][0] + 1)) for i in range(N)))
