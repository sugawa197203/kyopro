import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

M = int(input())
D = list(map(int, input().split()))

s = sum(D)
_s = s // 2
total = 0
for i, d in enumerate(D):
	total += d

	if total > _s:
		print(1 + i, d - (total - _s) + 1)
		sys.exit()
