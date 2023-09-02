import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

sumf = sum(F)
f = sumf
F.sort(reverse=True)
before = float('inf')
c = 0
while sumf < before:
	before = sumf
	c += 1
	for _ in range(D):
		if len(F) == 0:
			print(P * math.ceil(N / D))
			sys.exit()
		F.pop(0)
	sumf = sum(F) + P * c

print(before)