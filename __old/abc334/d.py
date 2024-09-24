import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, Q = map(int, input().split())
R = list(map(int, input().split()))
X = [int(x) for x in sys.stdin.readlines()]

R.sort()

sumR = []

_r = 0
for r in R:
	_r += r
	sumR.append(_r)

for x in X:
	print(bisect.bisect_right(sumR, x))
