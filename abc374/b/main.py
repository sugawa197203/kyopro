import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; import networkx as nx; debug = lambda *arg : print(*arg, file=sys.stderr);

S = input()
T = input()

for i, st in enumerate(zip(S, T)):
    s, t = st
    if s != t:
        print(i+1)
        break
else:
    if len(S) < len(T):
        print(len(S) + 1)
    elif len(S) > len(T):
        print(len(T) + 1)
    else:
        print(0)
