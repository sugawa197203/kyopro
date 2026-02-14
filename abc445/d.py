from collections import defaultdict

H, W, N = map(int, input().split())

_HW = [tuple(map(int, input().split())) for _ in range(N)]

HW = defaultdict(set)
WH = defaultdict(set)

for i, (h, w) in enumerate(_HW):
    HW[h].add((w, i))
    WH[w].add((h, i))

nokoriH = H
nokoriW = W
pos = (1, 1)

ans = [(-1, -1)] * N
for _ in range(N - 1):
    if nokoriH in HW:
        w = HW[nokoriH].pop()
        if not HW[nokoriH]:
            del HW[nokoriH]
        ans[w[1]] = pos
        pos = (pos[0], pos[1] + w[0])
        nokoriW -= w[0]
        
        WH[w[0]].remove((nokoriH, w[1]))
        if not WH[w[0]]:
            del WH[w[0]]

    else:
        h = WH[nokoriW].pop()
        if not WH[nokoriW]:
            del WH[nokoriW]
        ans[h[1]] = pos
        pos = (pos[0] + h[0], pos[1])
        nokoriH -= h[0]
        
        HW[h[0]].remove((nokoriW, h[1]))
        if not HW[h[0]]:
            del HW[h[0]]


for i in range(N):
    if ans[i] == (-1, -1):
        ans[i] = pos
    print(*ans[i])

