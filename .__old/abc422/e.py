from heapq import heappop, heappush, heapify
from math import gcd

N = int(input())
POS = [list(map(int, input().split())) for _ in range(N)]

counts = [(0, i, set()) for i in range(N)]

def vecFix(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    if dx == 0:
        return (0, 1)
    if dy == 0:
        return (1, 0)
    g = gcd(abs(dx), abs(dy))
    return (dx // g, dy // g)

while counts:
    nodeNode, fromVec = heappop(counts)
    watched = set()
    for c, node, vec in counts:
        if nowC < c:
            continue
        v = vecFix(POS[nodeNode], POS[node])
        if v in watched:
            continue
        watched.add(v)
        



