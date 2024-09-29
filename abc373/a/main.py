import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);



s = 0
for i in range(12):
    if len(input()) == i + 1:
        s += 1

print(s)
debug(s)
