from collections import defaultdict
N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
for i in range(1, N + 1):
    count = 0
    for nighbor in G[i]:
        if nighbor < i:
            count += 1
    if count == 1:
        ans += 1 

print(ans)       