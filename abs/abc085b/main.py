import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d = sorted(d)
d = list(set(d))
print(len(d))
