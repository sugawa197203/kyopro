import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);



S = input()
now = S.index("A")
cost = 0
for a in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    cost += abs(now - S.index(a))
    now = S.index(a)

print(cost)