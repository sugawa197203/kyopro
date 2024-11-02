import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

debug = lambda *x: print(*x, file=sys.stderr)

N = int(input())
A = list(map(int, input().split()))
Adic = {}
B = [-1] * N

for i, a in enumerate(A):
	if a in Adic:
		B[i] = Adic[a]
	Adic[a] = i + 1

print(*B)