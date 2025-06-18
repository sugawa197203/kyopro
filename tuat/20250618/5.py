from collections import defaultdict
N, M = map(int, input().split())
if N != M:
    print("No")
    exit()
G = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

watched = [False] * N

stack = [1]
while stack:
    node = stack.pop()
    if watched[node - 1]:
        continue
    watched[node - 1] = True
    if len(G[node]) != 2:
        print("No")
        exit()
    for neighbor in G[node]:
        if not watched[neighbor - 1]:
            stack.append(neighbor)

print("Yes" if all(watched) else "No")
