import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = sum(a[::2])
bob = sum(a[1::2])

print(alice - bob)
