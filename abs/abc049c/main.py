import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

S = input()

w = ['dream', 'dreamer', 'erase', 'eraser']

while len(S) > 0:
    for i in range(4):
        if S.endswith(w[i]):
            S = S[:-len(w[i])]
            break
    else:
        print('NO')
        exit()
print('YES')
