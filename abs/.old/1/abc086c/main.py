import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N = int(input())
t, x, y = 0, 0, 0
for _ in range(N):
    T, X, Y = map(int, input().split())
    dt = T - t
    dist = abs(X - x) + abs(Y - y)
    if dt < dist or (dt - dist) % 2 != 0:
        print('No')
        exit()
    t, x, y = T, X, Y

print('Yes')
