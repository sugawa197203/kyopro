import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    s = sum([int(j) for j in str(i)])
    if A <= s <= B:
        ans += i
print(ans)
