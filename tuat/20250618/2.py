from collections import defaultdict
N, M = map(int, input().split())

G = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, N + 1):
    G[i].sort()
    print(f"{len(G[i])}", end=" ")
    print(*G[i])
