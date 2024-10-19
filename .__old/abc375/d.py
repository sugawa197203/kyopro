import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

S = input()
start = {}
ans = 0

def comb(n, r):
	return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i, s in enumerate(S):
	if not s in start:
		start[s] = i
		continue

for i, s in enumerate(S[::-1]):
	if not s in start:
		continue
	ans += len(S) - i - start[s] - 1
	print(i, s, start[s], ans)

print(ans)