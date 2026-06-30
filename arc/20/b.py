from collections import defaultdict
N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

g1 = defaultdict(int)
g2 = defaultdict(int)

for i in range(N):
    if i % 2 == 0:
        g1[A[i]] += 1
    else:
        g2[A[i]] += 1

g1 = sorted(g1.items(), key=lambda x: x[1], reverse=True)
g2 = sorted(g2.items(), key=lambda x: x[1], reverse=True)

ans = 0

if g1[0][0] != g2[0][0]:
    for g in g1[1:]:
        ans += g[1]
    for g in g2[1:]:
        ans += g[1]
else:
    if g1[0][1] > g2[0][1]:
        for g in g1[1:]:
            ans += g[1]
        ans += g2[0][1]
        for g in g2[2:]:
            ans += g[1]
    else:
        for g in g2[1:]:
            ans += g[1]
        ans += g1[0][1]
        for g in g1[2:]:
            ans += g[1]

print(ans * C)
