import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
SUM = sum(A)
subtop = SUM - A[-1]
subfront = SUM - A[0]
subside = SUM - A[0] - A[-1]

r = []
r.append(0)
r.append(X - subside)
r.append(A[-1])

for _r in r:
	a = A.copy()
	a.append(_r)
	a.sort()
	if X <= sum(a[1:-1]):
		print(_r)
		sys.exit()

print(-1)
