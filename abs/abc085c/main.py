import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N, Y = map(int, input().split())

for y1 in range(N+1):
    for y2 in range(N-y1+1):
        y3 = N - y1 - y2
        if y3 < 0:
            continue
        if 10000*y1 + 5000*y2 + 1000*y3 == Y:
            print(y1, y2, y3)
            exit()
print(-1, -1, -1)
