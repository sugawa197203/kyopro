N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))

maxok = 0
for mask in range(1 << N):
    ok = 0
    for u, v in edges:
        if ((mask >> u) & 1) != ((mask >> v) & 1):
            ok += 1
    if ok > maxok:
        maxok = ok

print(M - maxok)

